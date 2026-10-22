#!/usr/bin/env python3
"""Recette AUTOMATED optionnelle : contrôle objectivable d'un rendu HTML (ACTION/GATE-A).

Ce script observe un artefact HTML dans un navigateur sans tête. Il fournit des preuves
`AUTOMATED` et la provenance minimale exigée par ACTION/GATE-A (`artifact_locator`,
`artifact_version`, `method`, `observed_at`). Il ne rend jamais de verdict global : il ne valide ni la
direction visuelle, ni l'utilisabilité, ni l'adéquation du positionnement.

Dépendance optionnelle : `pip install playwright && playwright install chromium`.
Sans navigateur, la recette sort `NOT-VERIFIED` (code 2) : une preuve web indisponible n'est jamais simulée.
Elle n'est volontairement pas appelée par `validate_all.py`, qui reste exécutable sans navigateur ;
ses comportements sont testés par `scripts/test_check_render.py`.

Statuts par contrôle (registre de gate d'ACTION) : PASS, PASS-WITH-RESERVATION, RETURN, NOT-VERIFIED.
Un contrôle qui ne peut pas conclure rend une réserve, jamais PASS. L'objet de preuve rend RETURN
s'il est introuvable, masqué, transparent ou sans surface ; sa position au premier écran reste à juger (réserve).
Codes de sortie : 0 aucun RETURN ; 1 au moins un RETURN ; 2 recette non exécutable.

Usage :
    python3 scripts/check_render.py page.html
    python3 scripts/check_render.py page.html --widths 390,768,1440 --proof "#estimateur" --json preuve.json
    python3 scripts/check_render.py http://127.0.0.1:8000/page.html          # même origine autorisée
    python3 scripts/check_render.py page.html --click "#ouvrir"               # observer un autre état
    python3 scripts/check_render.py page.html --captures captures/v1          # une capture pleine page par largeur
    python3 scripts/check_render.py page.html --baseline avant.json            # comparer à une mesure --json antérieure
    python3 scripts/check_render.py page.html --mesures                        # relevés de composition, sans seuil ni verdict

Mesures (--mesures) : relevés chiffrés de la page par largeur (titre d'accueil, corps, plus petit texte et sa part, tailles et familles,
longueur de ligne, images, texte centré, fonds de section, bords gauches, gros textes du premier écran couverts par un autre élément
ou au haut rogné, actions et navigation du premier écran, palette en OKLCH : fond, fonds voisins, encres, couleurs chromatiques). Ils ne passent pas par les contrôles : aucun statut, aucun code de sortie, aucun seuil.

Comparaison (--baseline) : chaque contrôle est rapproché du même contrôle d'une mesure antérieure, au même périmètre
(état et largeurs) et avec les mêmes réglages (--proof, --tab-stops, --allow-external, --wait-ms). Elle distingue un RETURN introduit, préexistant ou disparu ; elle ne change ni les statuts ni le
code de sortie : un défaut préexistant reste un défaut.
"""
from __future__ import annotations

import argparse
import functools
import hashlib
import http.server
import json
import os
import re
import sys
import threading
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote, urlsplit

PASS, RESERVE, RETURN, NOTVER = "PASS", "PASS-WITH-RESERVATION", "RETURN", "NOT-VERIFIED"
FOC = 'a[href],button,input:not([type=hidden]),select,textarea,summary,[role=button],[role=link],[tabindex]:not([tabindex="-1"])'


class BrowserUnavailable(Exception):
    """Playwright est présent, mais Chromium ne peut pas démarrer."""

# Candidat DOM borné, pas une implémentation d'AccName ni une lecture de l'arbre d'accessibilité.
# Les références explicites peuvent utiliser du texte masqué ; les descendants ordinaires ne le peuvent pas.
NAME_JS = r"""
(el) => {
  const clean = t => (t || '').replace(/\s+/g, ' ').trim();
  let uncertain = false;
  // aria-hidden, hidden et display:none d'un ancêtre sont irréversibles ; visibility est héritée mais peut être
  // rétablie sur un descendant : seule la valeur calculée de l'élément lui-même compte.
  const hidden = e => { const v = getComputedStyle(e).visibility; if (v === 'hidden' || v === 'collapse') return true;
    for (let n = e; n && n.nodeType === 1; n = n.parentElement) {
    if (n.getAttribute('aria-hidden') === 'true' || n.hasAttribute('hidden') || getComputedStyle(n).display === 'none') return true;
  } return false; };
  // Nom d'un SVG : aria-label et aria-labelledby sont traités avant l'appel ; reste son <title> enfant. Des formes seules
  // (path, circle, rect, g…) ne nomment rien : le candidat est alors vide, pas incertain, et une icône sans nom est un
  // défaut conclusif. Texte, <use>, <image>, <foreignObject>, lien ou nom ARIA interne : calcul non couvert, donc incertain.
  const svgName = s => {
    const kids = e => [...(e.childNodes || [])].filter(c => c.nodeType === 1);
    const title = kids(s).find(c => c.tagName.toLowerCase() === 'title');
    if (title && clean(title.textContent)) return clean(title.textContent);
    const unknown = e => kids(e).some(c => ['text', 'tspan', 'textpath', 'use', 'image', 'foreignobject', 'a'].includes(c.tagName.toLowerCase())
      || clean(c.getAttribute('aria-label')) || clean(c.getAttribute('aria-labelledby')) || unknown(c));
    if (unknown(s)) uncertain = true;
    return '';
  };
  const content = (n, includeHidden = false, referenced = false, ancestors = new Set()) => {
    if (n.nodeType === 3) return n.textContent || '';
    if (n.nodeType !== 1 || (!includeHidden && hidden(n)) || ancestors.has(n)) return '';
    const seen = new Set(ancestors); seen.add(n);
    if (!referenced) {
      const refs = clean(n.getAttribute('aria-labelledby')).split(' ').filter(Boolean).map(id => document.getElementById(id)).filter(Boolean);
      if (refs.length) return refs.map(t => content(t, hidden(t), true, ancestors)).join(' ');
    }
    const label = clean(n.getAttribute('aria-label')); if (label) return label;
    if (n.shadowRoot || n.tagName === 'SLOT') uncertain = true;
    for (const pseudo of ['::before', '::after']) {
      const c = getComputedStyle(n, pseudo).content;
      if (c && !['none', 'normal', '""', "''"].includes(c)) uncertain = true;
    }
    if (n.tagName === 'IMG') return n.getAttribute('alt') || n.getAttribute('title') || '';
    if (n.tagName.toLowerCase() === 'svg') return svgName(n);
    if (n.tagName.toUpperCase() === 'CANVAS') uncertain = true;
    if (n.labels && n.labels.length) return [...n.labels].map(t => content(t, hidden(t), true, seen)).join(' ');
    if (n.tagName === 'INPUT') {
      if (n !== el) uncertain = true;  // valeur de contrôle imbriqué : calcul AccName non couvert
      if (['submit', 'button', 'reset'].includes(n.type) && n.value) return n.value;
      if (['submit', 'reset', 'image'].includes(n.type) || n.hasAttribute('placeholder')) uncertain = true;
      return n.getAttribute('title') || '';
    }
    if (['SELECT', 'TEXTAREA'].includes(n.tagName) || !['BUTTON', 'A', 'SUMMARY', 'LABEL', 'SPAN', 'DIV', 'IMG'].includes(n.tagName)) uncertain = true;
    const text = [...n.childNodes].map(t => content(t, includeHidden, referenced, seen)).join('');
    return clean(text) || n.getAttribute('title') || '';
  };
  const candidate = clean(content(el));
  if (!candidate && el.tagName === 'SUMMARY') uncertain = true;  // nom natif par défaut
  return {candidate, uncertain, method: 'dom-candidate'};
}
"""

AUDIT_JS = r"""
(FOC) => {
  const px = v => parseFloat(v);
  // Toute couleur CSS est convertie en sRGB par le canvas ; une couleur non convertible est déclarée, jamais ignorée.
  const cv = document.createElement('canvas'); cv.width = cv.height = 1;
  const cx = cv.getContext('2d', {willReadFrequently: true}); const SENT = '#123457';
  const color = c => {
    if (!c) return null;
    const m = c.match(/^rgba?\(([^)]+)\)$/);
    if (m) { const p = m[1].split(/[ ,\/]+/).filter(Boolean).map(Number);
      if (p.length >= 3 && p.every(v => !isNaN(v))) return [p[0], p[1], p[2], p.length > 3 ? p[3] : 1]; }
    cx.fillStyle = SENT; cx.fillStyle = c;
    if (cx.fillStyle === SENT && c.replace(/\s/g, '').toLowerCase() !== SENT) return null;
    cx.clearRect(0, 0, 1, 1); cx.fillRect(0, 0, 1, 1);
    const d = cx.getImageData(0, 0, 1, 1).data; return [d[0], d[1], d[2], d[3] / 255];
  };
  const over = (f, b) => { const a = f[3]; return [f[0]*a + b[0]*(1-a), f[1]*a + b[1]*(1-a), f[2]*a + b[2]*(1-a), 1]; };
  const lum = c => { const s = c.slice(0, 3).map(v => { v /= 255; return v <= 0.03928 ? v/12.92 : Math.pow((v+0.055)/1.055, 2.4); });
    return 0.2126*s[0] + 0.7152*s[1] + 0.0722*s[2]; };
  const ratio = (a, b) => { const l1 = lum(a), l2 = lum(b); return (Math.max(l1, l2) + 0.05) / (Math.min(l1, l2) + 0.05); };
  const hex = c => '#' + c.slice(0, 3).map(v => Math.round(v).toString(16).padStart(2, '0')).join('');
  const sel = el => { if (el.id) return '#' + el.id; let s = el.tagName.toLowerCase();
    if (el.classList.length) s += '.' + [...el.classList].slice(0, 2).join('.'); return s; };
  const shown = el => { const r = el.getBoundingClientRect(); if (r.width < 2 || r.height < 2) return false; let o = 1;
    for (let e = el; e && e.nodeType === 1; e = e.parentElement) { const s = getComputedStyle(e);
      if (s.display === 'none' || s.visibility === 'hidden') return false; o *= parseFloat(s.opacity); }
    return o >= 0.05; };
  const opac = el => { let o = 1; for (let e = el; e && e.nodeType === 1; e = e.parentElement) o *= parseFloat(getComputedStyle(e).opacity); return o; };
  const effBg = el => { const layers = [];
    for (let e = el; e && e.nodeType === 1; e = e.parentElement) { const s = getComputedStyle(e);
      if (s.backgroundImage !== 'none') return {kind: 'image'};
      const c = color(s.backgroundColor); if (!c) return {kind: 'unknown', value: s.backgroundColor};
      // Surface translucide sur flou d'arrière-plan : ce qu'elle laisse voir n'est pas son ancêtre, non mesuré.
      const bf = s.backdropFilter || s.webkitBackdropFilter;
      if (bf && bf !== 'none' && c[3] < 1) return {kind: 'image'};
      if (c[3] > 0) { layers.push(c); if (c[3] >= 1) break; } }
    let base = [255, 255, 255, 1]; for (let i = layers.length - 1; i >= 0; i--) base = over(layers[i], base);
    return {kind: 'solid', c: base}; };

  const coverage = {method: 'dom-text-bounded', candidates: 0, evaluated: 0, excluded: 0, unmeasured: []};
  const textShown = el => { if (['hidden', 'collapse'].includes(getComputedStyle(el).visibility)) return false;
    for (let e = el; e && e.nodeType === 1; e = e.parentElement) {
      const s = getComputedStyle(e);
      if (s.display === 'none' || parseFloat(s.opacity) === 0) return false;
    } return true; };
  const res = {contrast: [], contrastCoverage: coverage, nonSolid: [], unknown: [], groupOpacity: [], svgText: [], targets: [], uaControls: 0,
               names: [], nameCandidates: [], nameUncertain: [], nameMethod: 'dom-candidate', nameControls: 0, imgs: [], inner: [], h1: 0,
               lang: document.documentElement.lang || '', title: document.title.trim()};
  const seen = new Set(), seenNs = new Set(), seenUk = new Set();
  for (const el of [document.body, ...document.querySelectorAll('body *')].filter(Boolean)) {
    if (['SCRIPT', 'STYLE', 'NOSCRIPT', 'SVG', 'PATH'].includes(el.tagName.toUpperCase())) continue;
    const k = sel(el), native = ['INPUT', 'TEXTAREA', 'SELECT'].includes(el.tagName.toUpperCase());
    const text = native ? '' : [...el.childNodes].filter(n => n.nodeType === 3).map(n => n.textContent).join('').trim();
    const excluded = el.closest(':disabled,[aria-disabled="true"]') || !textShown(el);
    const addUnmeasured = kind => { coverage.candidates++; if (excluded) coverage.excluded++;
      else coverage.unmeasured.push({sel: k, kind}); };
    // Les valeurs courantes, le placeholder affiché et le texte natif ne sont pas des childNodes.
    // Leur peinture native/pseudo n'est pas évaluée par cette méthode : réserve explicite, sans exposer la valeur.
    if (native && el.type !== 'hidden') {
      if (el.tagName === 'SELECT' || el.type === 'file') addUnmeasured('texte de contrôle natif');
      else if (!['checkbox', 'radio', 'range', 'color'].includes(el.type)) {
        if (String(el.value || '').length) addUnmeasured('valeur courante de contrôle');
        else if ((el.getAttribute('placeholder') || '').trim()) addUnmeasured('placeholder affiché');
        else if (['submit', 'reset', 'image'].includes(el.type)) addUnmeasured('texte natif implicite');
      }
    }
    for (const pseudo of ['::before', '::after']) {
      const c = getComputedStyle(el, pseudo).content;
      if (c && !['none', 'normal', '""', "''"].includes(c)) addUnmeasured('contenu ' + pseudo);
    }
    if (!text) continue;
    coverage.candidates++;
    if (excluded) { coverage.excluded++; continue; }
    if (el instanceof SVGElement || el.closest('svg')) { const k = sel(el); if (!seenNs.has('svg:' + k)) { seenNs.add('svg:' + k); res.svgText.push({sel: k}); } continue; }
    const cs = getComputedStyle(el), base = color(cs.color);
    if (!base) { if (!seenUk.has(k)) { seenUk.add(k); res.unknown.push({sel: k, value: cs.color}); } continue; }
    // La couleur qui remplit le texte peut différer de color (-webkit-text-fill-color) : c'est elle qui est peinte.
    const fill = cs.webkitTextFillColor ? color(cs.webkitTextFillColor) : null;
    let fg = base;
    if (fill && fill.join() !== base.join()) {
      // Remplissage transparent : le texte est peint par un fond (background-clip:text), non évalué.
      if (fill[3] === 0) { if (!seenNs.has(k)) { seenNs.add(k); res.nonSolid.push({sel: k}); } continue; }
      fg = fill;
    }
    const opacity = opac(el);
    if (opacity !== 1) { res.groupOpacity.push({sel: k, opacity}); continue; }
    const bg = effBg(el);
    if (bg.kind === 'image') { if (!seenNs.has(k)) { seenNs.add(k); res.nonSolid.push({sel: k}); } continue; }
    if (bg.kind === 'unknown') { if (!seenUk.has(k)) { seenUk.add(k); res.unknown.push({sel: k, value: bg.value}); } continue; }
    const f = over(fg, bg.c), r = ratio(f, bg.c), size = px(cs.fontSize), w = parseInt(cs.fontWeight) || 400;
    const large = size >= 24 || (size >= 18.66 && w >= 700), need = large ? 3 : 4.5;
    if (!Number.isFinite(size)) { res.unknown.push({sel: k, value: 'taille de texte inconnue'}); continue; }
    coverage.evaluated++;
    if (r < need) { const key = hex(f) + '|' + hex(bg.c) + '|' + size; if (!seen.has(key)) { seen.add(key);
      res.contrast.push({sel: k, fg: hex(f), bg: hex(bg.c), size, ratio: Math.round(r*100)/100, need, text: text.slice(0, 40)}); } }
  }
  const name = __NAME_JS__;
  const T = [];
  for (const el of document.querySelectorAll(FOC)) {
    if (el.disabled || el.closest('[aria-hidden="true"],[hidden]')) continue;
    const cs = getComputedStyle(el); if (cs.display === 'none' || cs.visibility === 'hidden') continue;
    // Un descendant d'un conteneur display:none (dont un dialog fermé) n'est pas rendu.
    // Son propre display peut pourtant être « block » : ne pas le déclarer sans nom.
    let notRendered = false;
    for (let ancestor = el.parentElement; ancestor; ancestor = ancestor.parentElement) {
      if (getComputedStyle(ancestor).display === 'none') { notRendered = true; break; }
    }
    if (notRendered) continue;
    res.nameControls++;
    const n = name(el);
    if (n.candidate) res.nameCandidates.push({sel: sel(el), candidate: n.candidate});
    if (n.uncertain) res.nameUncertain.push({sel: sel(el)});
    else if (!n.candidate) res.names.push({sel: sel(el)});
    if (!shown(el)) continue;
    const inline = cs.display === 'inline' && el.parentElement && [...el.parentElement.childNodes].some(n => n.nodeType === 3 && n.textContent.trim());
    if (inline) continue;                                         // exception WCAG : cible dans une phrase
    if (['checkbox', 'radio'].includes(el.type) && cs.appearance !== 'none') { res.uaControls++; continue; }  // contrôle natif du navigateur
    const r = el.getBoundingClientRect();
    T.push({el, r, small: Math.min(r.width, r.height) < 24, cx: r.left + r.width / 2, cy: r.top + r.height / 2});
  }
  // WCAG 2.2 (2.5.8) : une cible de moins de 24 px passe si un cercle de 24 px centré sur elle ne touche ni une autre
  // cible, ni le cercle d'une autre petite cible. Les exceptions « équivalent » et « essentiel » restent à juger.
  for (const u of T.filter(t => t.small)) {
    let spaced = true;
    for (const o of T) { if (o === u) continue;
      const dx = Math.max(o.r.left - u.cx, 0, u.cx - o.r.right), dy = Math.max(o.r.top - u.cy, 0, u.cy - o.r.bottom);
      if (dx*dx + dy*dy < 144 || (o.small && Math.hypot(o.cx - u.cx, o.cy - u.cy) < 24)) { spaced = false; break; } }
    res.targets.push({sel: sel(u.el), w: Math.round(u.r.width), h: Math.round(u.r.height), spaced});
  }
  for (const im of document.querySelectorAll('img')) { if (im.getAttribute('role') === 'presentation' || im.closest('[aria-hidden="true"]')) continue;
    if (!im.hasAttribute('alt')) res.imgs.push({sel: sel(im)}); }
  // Image visible sans source, ou dont le chargement est terminé sans pixel : introuvable, illisible ou bloquée (autre origine sans --allow-external).
  // Une image visible encore en chargement à la mesure n'est pas vérifiée.
  res.brokenImgs = []; res.pendingImgs = [];
  for (const im of document.querySelectorAll('img')) { const src = im.currentSrc || im.src;
    if (!shown(im)) continue;
    const declared = im.getAttribute('src') || im.getAttribute('srcset') || (im.parentElement && im.parentElement.tagName === 'PICTURE');
    if (!declared) { res.brokenImgs.push({sel: sel(im), external: false}); continue; }  // boîte d'image visible sans source
    if (!src) { res.pendingImgs.push({sel: sel(im)}); continue; }  // source déclarée, pas encore choisie
    if (!im.complete) { res.pendingImgs.push({sel: sel(im)}); continue; }
    if (im.naturalWidth > 0) continue;
    let external = false; try { const u = new URL(src, location.href); external = !/^(data|blob):$/.test(u.protocol) && u.origin !== location.origin; } catch (e) {}
    res.brokenImgs.push({sel: sel(im), external}); }
  for (const el of document.querySelectorAll('dialog[open], body *')) {
    if (el.scrollWidth <= el.clientWidth + 1 || el.clientWidth === 0) continue;
    const isDlg = el.tagName === 'DIALOG', ox = getComputedStyle(el).overflowX;
    if (isDlg || ox === 'auto' || ox === 'scroll') res.inner.push({sel: sel(el), dialog: isDlg, sw: el.scrollWidth, cw: el.clientWidth});
  }
  res.h1 = [...document.querySelectorAll('h1')].filter(shown).length;
  return res;
}
"""
AUDIT_JS = AUDIT_JS.replace('__NAME_JS__', NAME_JS)

# Référence de style hors focus, prise avant toute tabulation : un indicateur est un CHANGEMENT de style au focus,
# pas la simple présence d'un contour ou d'une ombre (une ombre décorative permanente ne compte pas).
# Brique couleur partagée par la mesure du focus et les relevés : conversion de toute couleur CSS en sRGB par le canvas (une couleur
# non convertible est déclarée, jamais ignorée), composition sur un fond, rapport de contraste WCAG, fond uni effectif et OKLCH.
# AUDIT_JS garde sa propre copie : ses tests de DOM simulés l'évaluent tel quel.
COLOR_JS = r"""
  const cv = document.createElement('canvas'); cv.width = cv.height = 1;
  const cx = cv.getContext('2d', {willReadFrequently: true}); const SENT = '#123457';
  const color = c => {
    if (!c) return null;
    const m = c.match(/^rgba?\(([^)]+)\)$/);
    if (m) { const p = m[1].split(/[ ,\/]+/).filter(Boolean).map(Number);
      if (p.length >= 3 && p.every(v => !isNaN(v))) return [p[0], p[1], p[2], p.length > 3 ? p[3] : 1]; }
    cx.fillStyle = SENT; cx.fillStyle = c;
    if (cx.fillStyle === SENT && c.replace(/\s/g, '').toLowerCase() !== SENT) return null;
    cx.clearRect(0, 0, 1, 1); cx.fillRect(0, 0, 1, 1);
    const d = cx.getImageData(0, 0, 1, 1).data; return [d[0], d[1], d[2], d[3] / 255];
  };
  const over = (f, b) => { const a = f[3]; return [f[0]*a + b[0]*(1-a), f[1]*a + b[1]*(1-a), f[2]*a + b[2]*(1-a), 1]; };
  const lin = v => { v /= 255; return v <= 0.04045 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4); };
  const lum = c => 0.2126 * lin(c[0]) + 0.7152 * lin(c[1]) + 0.0722 * lin(c[2]);
  const ratio = (a, b) => { const l1 = lum(a), l2 = lum(b); return (Math.max(l1, l2) + 0.05) / (Math.min(l1, l2) + 0.05); };
  const hex = c => '#' + c.slice(0, 3).map(v => Math.round(v).toString(16).padStart(2, '0')).join('');
  const oklch = c => { const r = lin(c[0]), g = lin(c[1]), b = lin(c[2]);
    const l = Math.cbrt(0.4122214708*r + 0.5363325363*g + 0.0514459929*b), m = Math.cbrt(0.2119034982*r + 0.6806995451*g + 0.1073969566*b),
          s = Math.cbrt(0.0883024619*r + 0.2817188376*g + 0.6299787005*b);
    const L = 0.2104542553*l + 0.7936177850*m - 0.0040720468*s, A = 1.9779984951*l - 2.4285922050*m + 0.4505937099*s, B = 0.0259040371*l + 0.7827717662*m - 0.8086757660*s;
    return {L, C: Math.hypot(A, B), H: (Math.atan2(B, A) * 180 / Math.PI + 360) % 360}; };
  const effBg = e0 => { const layers = [];
    for (let e = e0; e && e.nodeType === 1; e = e.parentElement) { const s = getComputedStyle(e);
      if (s.backgroundImage !== 'none') return {kind: 'image'};
      const c = color(s.backgroundColor); if (!c) return {kind: 'unknown'};
      if (c[3] > 0) { layers.push(c); if (c[3] >= 1) break; } }
    let base = [255, 255, 255, 1]; for (let i = layers.length - 1; i >= 0; i--) base = over(layers[i], base);
    return {kind: 'solid', c: base}; };
"""

BASELINE_JS = r"""
(FOC) => {
  const snap = e => { const s = getComputedStyle(e);
    return [s.outlineStyle, s.outlineWidth, s.outlineColor, s.boxShadow, s.borderTopColor, s.borderBottomColor,
            s.borderTopWidth, s.backgroundColor, s.color, s.textDecorationLine].join('|'); };
  const rel = a => [a, a.parentElement, ...(a.labels ? [...a.labels] : []), a.nextElementSibling].filter(Boolean);
  window.__crSnap = snap; window.__crRel = rel; window.__crBase = new Map(); window.__crStops = [];
  if (document.activeElement && document.activeElement !== document.body) document.activeElement.blur();
  // Point de départ explicite au début de la zone active (feuille modale ouverte, sinon la page) : sans lui,
  // la tabulation reprendrait après l'élément qui avait le focus et sauterait les arrêts situés avant.
  const root = [...document.querySelectorAll('dialog[open]')].filter(d => d.matches(':modal')).pop() || document.body;
  const start = document.createElement('span'); start.tabIndex = -1; start.id = '__cr_start';
  root.insertBefore(start, root.firstChild); start.focus();
  for (const el of document.querySelectorAll(FOC)) for (const t of rel(el)) if (!window.__crBase.has(t)) window.__crBase.set(t, snap(t));
  window.__crKeys = new Map();
  const expected = [], excluded = [];
  for (const el of root.querySelectorAll(FOC)) {
    const s = getComputedStyle(el), r = el.getBoundingClientRect();
    const id = el.id ? '#' + el.id : el.tagName.toLowerCase();
    if (el.matches(':disabled') || el.closest('[inert],[hidden],[aria-hidden="true"]') ||
        s.display === 'none' || ['hidden','collapse'].includes(s.visibility) || !r.width || !r.height) {
      excluded.push(id); continue;
    }
    const key = 'control-' + expected.length;
    window.__crKeys.set(el, key); expected.push({key, id});
  }
  return {expected, excluded, scope: root === document.body ? 'page' : 'dialogue modal'};
}
"""

# Les arrêts sont identifiés par l'élément lui-même, pas par un nom : deux boutons sans id restent deux arrêts.
FOCUS_JS = r"""
() => { const a = document.activeElement;
  if (!a || a === document.body || a === document.documentElement) return {end: true};
  const stops = window.__crStops, i = stops.indexOf(a);
  if (i >= 0) return {cycle: true};
  const id = a.id ? '#' + a.id : a.tagName.toLowerCase() + (a.classList.length ? '.' + a.classList[0] : '');
  const indicator = window.__crRel(a).some(t => { const b = window.__crBase.get(t); return b !== undefined && b !== window.__crSnap(t); });
  if (i < 0) stops.push(a);
  return {id, key: window.__crKeys.get(a), isNew: i < 0, indicator, count: stops.length}; }
"""

# Contraste de l'indicateur de focus (WCAG 1.4.11), mesuré sur l'élément qui vient de recevoir le focus. Seuls les indicateurs dont
# la couleur et la place sont lisibles dans le style calculé sont mesurés : un contour (hors contour du navigateur, déjà à deux tons)
# et un anneau d'ombre sans flou ni décalage. Un changement de fond, de couleur, de bordure, une ombre floue ou intérieure,
# un fond en dégradé ou en image : non mesuré. Les transitions en cours sont terminées avant la lecture.
FOCUS_CUE_JS = r"""
() => { const el = document.activeElement;
  if (!el || el === document.body || el === document.documentElement) return null;
  try { for (const a of el.getAnimations()) if (a.constructor.name === 'CSSTransition') a.finish(); } catch (e) {}
__COLOR_JS__
  const before = (window.__crBase.get(el) || '').split('|'), cs = getComputedStyle(el);
  const now = [cs.outlineStyle, cs.outlineWidth, cs.outlineColor, cs.boxShadow, cs.borderTopColor, cs.borderBottomColor,
               cs.borderTopWidth, cs.backgroundColor, cs.color, cs.textDecorationLine];
  const changed = now.map((v, i) => v !== before[i]);
  const cues = []; let other = false, ua = false;
  const measure = (fgStr, ground, kind) => { const fg = color(fgStr);
    if (!fg || ground.kind !== 'solid') { other = true; return; }
    const f = fg[3] < 1 ? over(fg, ground.c) : fg;
    cues.push({kind, fg: hex(f), bg: hex(ground.c), ratio: Math.round(ratio(f, ground.c) * 100) / 100}); };
  const outside = effBg(el.parentElement || el), inside = effBg(el);
  if (changed[0] || changed[1] || changed[2]) {
    if (cs.outlineStyle === 'auto') ua = true;
    else if (cs.outlineStyle !== 'none' && parseFloat(cs.outlineWidth) > 0) measure(cs.outlineColor, parseFloat(cs.outlineOffset) < 0 ? inside : outside, 'contour');
  }
  if (changed[3]) {
    const parts = v => (v || '').split(/,(?![^(]*\))/).map(x => x.trim()).filter(x => x && x !== 'none');
    const had = new Set(parts(before[3]));
    for (const sh of parts(cs.boxShadow)) { if (had.has(sh)) continue;
      const len = (sh.match(/-?[\d.]+px/g) || []).map(parseFloat), colour = sh.replace(/-?[\d.]+px/g, '').replace('inset', '').trim();
      if (/inset/.test(sh) || len.length < 4 || len[0] !== 0 || len[1] !== 0 || len[2] > 1 || len[3] <= 0) { other = true; continue; }
      measure(colour, outside, 'ombre'); }
  }
  if (changed[4] || changed[5] || changed[6] || changed[7] || changed[8] || changed[9] || !changed.some(Boolean)) other = true;
  return {cues, other, ua}; }
"""

FOCUS_CUE_JS = FOCUS_CUE_JS.replace('__COLOR_JS__', COLOR_JS)

# Défilement immédiat : une page en `scroll-behavior: smooth` ferait mesurer au milieu de l'animation de défilement.
SCROLL_TOP = "window.scrollTo({top: 0, left: 0, behavior: 'instant'})"


PROOF_JS = r"""
s => { const el = document.querySelector(s); if (!el) return {found: false};
  const r = el.getBoundingClientRect(); let hidden = ['hidden', 'collapse'].includes(getComputedStyle(el).visibility), opacity = 1; const limits = [];
  for (let e = el; e && e.nodeType === 1; e = e.parentElement) {
    // visibility est héritée mais peut être rétablie sur le descendant ; display:none ne le peut pas.
    const cs = getComputedStyle(e); hidden ||= cs.display === 'none';
    const o = parseFloat(cs.opacity); if (!Number.isFinite(o)) limits.push('opacité inconnue'); else opacity *= o;
    if ((cs.clipPath && cs.clipPath !== 'none') || (cs.maskImage && cs.maskImage !== 'none') ||
        (cs.clip && !['auto', 'rect(auto, auto, auto, auto)'].includes(cs.clip))) limits.push('découpe ou masque non évalué');
    if (e !== el && [cs.overflow, cs.overflowX, cs.overflowY].some(v => ['hidden', 'clip', 'scroll', 'auto'].includes(v)))
      limits.push('découpe par un ancêtre non évaluée');
    if (cs.contentVisibility && cs.contentVisibility !== 'visible') limits.push('content-visibility non évaluée');
  }
  const x = Math.max(0, Math.min(r.right, innerWidth) - Math.max(r.left, 0));
  const y = Math.max(0, Math.min(r.bottom, innerHeight) - Math.max(r.top, 0));
  return {found: true, method: 'css-rectangle-bounded', w: r.width, h: r.height, hidden, opacity,
          intersectionWidth: x, visible: y, limits: [...new Set(limits)]}; }
"""


# Enregistreur d'animations, injecté avant tout script de la page, sous préférence « mouvement réduit ». Un instantané
# des animations « en cours » à la fin de la mesure ne voit pas une animation d'entrée qui s'est terminée entre-temps :
# l'enregistreur note chaque animation ou transition dès son démarrage (CSS, Web Animations, `Element.animate`) et
# relève les propriétés animées pour dire si elle déplace quelque chose. Les animations pilotées par script sans API
# d'animation du navigateur (changements de style inline à chaque image) ne sont pas observées.
TEXT_LAYOUT_JS = r"""
() => {
  // Textes qui se recouvrent ou sont tronqués. Rectangles de lignes ramenés à l'interligne (la boîte de contenu
  // d'une fonte dépasse souvent l'interligne) ; calques fixes ou collants exclus (couverture : autre contrôle) ;
  // texte masqué, transparent ou hors de la largeur de la page exclu (liens d'évitement, texte pour lecteur d'écran).
  // Un texte décoratif (aria-hidden, ou encre effective sous 0,35 : opacité cumulée, alpha de la couleur ou du
  // remplissage, contour sur remplissage transparent), comme un filigrane, superposé à un autre est relevé à part :
  // la superposition peut être un parti typographique, elle se juge.
  const W = document.documentElement.clientWidth;
  const overlay = el => { for (let e = el; e && e !== document.body; e = e.parentElement) { const p = getComputedStyle(e).position; if (p === 'fixed' || p === 'sticky') return true; } return false; };
  const opacity = el => { let op = 1; for (let e = el; e; e = e.parentElement) op *= parseFloat(getComputedStyle(e).opacity); return op; };
  const alphaOf = c => {
    const m = /^rgba?\(([^)]*)\)/.exec(c || '');
    if (m) { const p = m[1].split(/[\s,\/]+/).filter(Boolean); return p.length > 3 ? parseFloat(p[3]) : 1; }
    const slash = (c || '').split('/')[1];
    return slash ? parseFloat(slash) : 1;
  };
  const ink = el => {
    const cs = getComputedStyle(el), fill = alphaOf(cs.webkitTextFillColor || cs.color);
    if (fill > 0) return fill;
    if (parseFloat(cs.webkitTextStrokeWidth) > 0) return 0;  // contour seul : texte de dessin
    return (cs.backgroundClip === 'text' || cs.webkitBackgroundClip === 'text') ? 1 : 0;  // texte en dégradé : lu
  };
  // visibility s'hérite : la valeur calculée du parent du texte suffit, et un descendant rendu visible reste mesuré.
  const hidden = (el, r) => {
    if (r.right <= 0 || r.left >= W || getComputedStyle(el).visibility === 'hidden') return true;
    // Contenu non rendu sans display:none : volet <details> fermé, content-visibility: hidden.
    if (el.checkVisibility && !el.checkVisibility()) return true;
    for (let e = el; e; e = e.parentElement) {
      const cs = getComputedStyle(e);
      if (cs.display === 'none' || cs.clip === 'rect(0px, 0px, 0px, 0px)' || cs.clipPath === 'inset(50%)') return true;
    }
    return opacity(el) < 0.05;
  };
  const leaves = [];
  const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  while (walker.nextNode() && leaves.length < 4000) {
    const n = walker.currentNode; if (!n.nodeValue.trim()) continue;
    const el = n.parentElement; if (!el || el.closest('script,style,noscript,title,template') || overlay(el)) continue;
    const range = document.createRange(); range.selectNodeContents(n);
    const lh = parseFloat(getComputedStyle(el).lineHeight);
    const deco = !!el.closest('[aria-hidden="true"]') || opacity(el) * ink(el) < 0.35;
    for (const x of range.getClientRects()) {
      if (x.width <= 1 || x.height <= 1 || hidden(el, x)) continue;
      let top = x.top, bottom = x.bottom;
      if (lh && lh < x.height) { const c = (top + bottom) / 2; top = c - lh / 2; bottom = c + lh / 2; }
      leaves.push({el, deco, t: n.nodeValue.trim().slice(0, 32), l: x.left, top, r: x.right, b: bottom});
    }
  }
  // Tri par haut de ligne : seules les lignes qui commencent avant la fin de la courante peuvent la recouvrir.
  leaves.sort((x, y) => x.top - y.top);
  const overlaps = [], decorative = [];
  outer: for (let i = 0; i < leaves.length; i++) {
    const a = leaves[i];
    for (let j = i + 1; j < leaves.length; j++) {
      const c = leaves[j];
      if (c.top >= a.b - 3) break;
      const ox = Math.min(a.r, c.r) - Math.max(a.l, c.l), oy = Math.min(a.b, c.b) - Math.max(a.top, c.top);
      if (ox > 2 && oy > 3) {
        if (a.el === c.el || a.el.contains(c.el) || c.el.contains(a.el)) continue;
        const pair = [a.t, c.t, Math.round(ox), Math.round(oy)];
        if (a.deco || c.deco) { if (decorative.length < 12) decorative.push(pair); }
        else { overlaps.push(pair); if (overlaps.length >= 12) break outer; }
      }
    }
  }
  const trunc = [];
  for (const e of document.querySelectorAll('body *')) {
    const cs = getComputedStyle(e);
    if (cs.display === 'none' || !e.clientWidth || overlay(e)) continue;
    // Texte porté directement, ou par des éléments en ligne (un lien ou un span dans la boîte qui rogne).
    const carries = [...e.childNodes].some(n => n.nodeType === 3 && n.nodeValue.trim())
      || [...e.children].some(c => getComputedStyle(c).display.startsWith('inline') && c.textContent.trim());
    if (!carries) continue;
    const clipped = cs.textOverflow === 'ellipsis' || ((cs.overflowX === 'hidden' || cs.overflowX === 'clip') && cs.whiteSpace !== 'normal');
    // Coupe sur plusieurs lignes (line-clamp) : le débordement est vertical.
    const clamp = cs.webkitLineClamp || cs.lineClamp || 'none';
    const clamped = clamp !== 'none' && (cs.overflowY === 'hidden' || cs.overflowY === 'clip');
    if ((clipped && e.scrollWidth > e.clientWidth + 1) || (clamped && e.scrollHeight > e.clientHeight + 1)) { trunc.push((e.textContent || '').trim().slice(0, 32)); if (trunc.length >= 8) break; }
  }
  return {leaves: leaves.length, overlaps, decorative, trunc};
}
"""

IN_FRAME_JS = r"""
(spec) => {
  // SÉLECTEUR@CADRE : chaque élément visible du sélecteur doit avoir son centre dans le cadre (la fenêtre si omis).
  // Le séparateur est le dernier @ hors chaîne et hors crochets : a[href="mailto:x@y.fr"] reste un sélecteur.
  let at = -1, quote = '', depth = 0;
  for (let i = 0; i < spec.length; i++) {
    const ch = spec[i];
    if (quote) { if (ch === '\\') i++; else if (ch === quote) quote = ''; }
    else if (ch === '"' || ch === "'") quote = ch;
    else if (ch === '[') depth++;
    else if (ch === ']') depth = Math.max(0, depth - 1);
    else if (ch === '@' && !depth) at = i;
  }
  const sel = at > 0 ? spec.slice(0, at) : spec, frame = at > 0 ? spec.slice(at + 1) : '';
  let els;
  try { els = [...document.querySelectorAll(sel)]; } catch (e) { return {spec, error: 'sélecteur invalide'}; }
  const shown = e => {
    if (getComputedStyle(e).visibility === 'hidden') return false;
    let op = 1; for (let x = e; x; x = x.parentElement) op *= parseFloat(getComputedStyle(x).opacity);
    return op >= 0.05;
  };
  els = els.filter(e => { const r = e.getBoundingClientRect(); return (r.width > 0 || r.height > 0) && shown(e); });
  let box = {l: 0, t: 0, r: innerWidth, b: innerHeight};
  if (frame) {
    let f; try { f = document.querySelector(frame); } catch (e) { return {spec, error: 'cadre invalide'}; }
    if (!f) return {spec, found: els.length, error: 'cadre introuvable'};
    const r = f.getBoundingClientRect(); box = {l: r.left, t: r.top, r: r.right, b: r.bottom};
  }
  let outside = 0;
  for (const e of els) { const r = e.getBoundingClientRect(), cx = (r.left + r.right) / 2, cy = (r.top + r.bottom) / 2; if (cx < box.l || cx > box.r || cy < box.t || cy > box.b) outside++; }
  return {spec, found: els.length, outside};
}
"""

MOTION_RECORDER_JS = r"""
(() => {
  if (window.__dgMotion) return;
  const MOVE = /^(transform|translate|rotate|scale|top|left|right|bottom|inset(-.*)?|margin(-.*)?|offset(-.*)?|clip-path|object-position|background-position(-.*)?|perspective(-.*)?)$/;
  const SKIP = new Set(['offset', 'easing', 'composite', 'computedOffset']);
  const seen = new Map();
  const sel = el => { if (!el || el.nodeType !== 1) return '?'; if (el.id) return '#' + el.id;
    let s = el.tagName.toLowerCase(); if (el.classList && el.classList.length) s += '.' + [...el.classList].slice(0, 2).join('.'); return s; };
  const props = a => { const p = new Set();
    try { for (const k of (a.effect && a.effect.getKeyframes ? a.effect.getKeyframes() : [])) for (const n of Object.keys(k))
      if (!SKIP.has(n)) p.add(n.replace(/[A-Z]/g, m => '-' + m.toLowerCase())); } catch (e) {}
    return [...p]; };
  // Chaque instance est lue une fois ; les instances d'une même cible et d'un même nom sont fusionnées sans perdre une
  // animation infinie. Une animation finie dont la durée active ne dépasse pas INSTANT ms (réinitialisation habituelle
  // du mouvement réduit, 0,01 ms) n'est pas un mouvement perceptible : elle n'est pas notée.
  const INSTANT = 10, read = new WeakSet();
  const note = a => { try {
    if (!a || read.has(a)) return; read.add(a);
    const t = a.effect.getComputedTiming(), infinite = t.iterations === Infinity;
    if (!infinite && t.activeDuration <= INSTANT) return;
    const target = sel(a.effect && a.effect.target), name = a.animationName || a.transitionProperty || 'anim', key = target + '|' + name;
    const p = props(a), had = seen.get(key);
    if (had) { had.infinite = had.infinite || infinite; for (const n of p) if (!had.props.includes(n)) had.props.push(n);
      had.moves = had.props.some(n => MOVE.test(n)); return; }
    seen.set(key, {name, target, infinite, props: p, moves: p.some(n => MOVE.test(n))});
  } catch (e) {} };
  const scan = () => { try { for (const a of (document.getAnimations ? document.getAnimations() : [])) note(a); } catch (e) {} };
  const hook = e => { try { for (const a of e.target.getAnimations()) note(a); } catch (x) {} };
  addEventListener('animationstart', hook, true);
  addEventListener('transitionrun', hook, true);
  const orig = Element.prototype.animate;
  if (orig) Element.prototype.animate = function (...args) { const r = orig.apply(this, args); note(r); return r; };
  (function tick(n) { scan(); if (n < 120) requestAnimationFrame(() => tick(n + 1)); })(0);
  window.__dgMotion = () => { scan(); return [...seen.values()]; };
})();
"""

MOTION_REPORT_JS = "() => window.__dgMotion ? window.__dgMotion() : []"

# Mesures de composition (option --mesures) : des relevés chiffrés de la page, sans seuil ni verdict. Elles ne passent pas par
# `interpret` : aucun statut, aucun code de sortie.
MESURES_JS = r"""
() => {
  const W = innerWidth, H = innerHeight, r1 = v => Math.round(v * 10) / 10;
__COLOR_JS__
  const shown = el => { const r = el.getBoundingClientRect(); if (r.width < 2 || r.height < 2) return false;
    for (let e = el; e && e.nodeType === 1; e = e.parentElement) { const s = getComputedStyle(e);
      if (s.display === 'none' || s.visibility === 'hidden' || parseFloat(s.opacity) === 0) return false; } return true; };
  const lineCount = el => { const rg = document.createRange(); rg.selectNodeContents(el);
    const rs = [...rg.getClientRects()].filter(r => r.width > 1 && r.height > 1).sort((a, b) => a.top - b.top), rows = [];
    for (const r of rs) { const row = rows.find(x => r.top < x.bottom - (x.bottom - x.top) * 0.5 && r.bottom > x.top + (x.bottom - x.top) * 0.5);
      if (row) { row.top = Math.min(row.top, r.top); row.bottom = Math.max(row.bottom, r.bottom); } else rows.push({top: r.top, bottom: r.bottom}); }
    return Math.max(1, rows.length); };
  const words = t => (t.trim().match(/\S+/g) || []).length;
  const familyOf = s => (s.fontFamily.split(',')[0] || '').replace(/["']/g, '').trim();
  const typo = el => { const s = getComputedStyle(el), size = parseFloat(s.fontSize), lh = s.lineHeight === 'normal' ? null : parseFloat(s.lineHeight) / size,
    ls = s.letterSpacing === 'normal' ? 0 : parseFloat(s.letterSpacing) / size;
    return {taille: r1(size), vw: r1(size / W * 100), interligne: lh === null ? 'normal' : r1(lh * 100) / 100, approche: r1(ls * 1000) / 1000,
            graisse: s.fontWeight, famille: familyOf(s)}; };
  // Recensement du texte visible, pondéré par le nombre de caractères.
  const cache = new Map(), isShown = el => { if (!cache.has(el)) cache.set(el, shown(el)); return cache.get(el); };
  const sizes = new Map(), fams = new Map(), inks = new Map(), weights = [];
  let chars = 0, centered = 0, total = 0;
  const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  for (let n = walker.nextNode(), seen = 0; n && seen < 6000; n = walker.nextNode(), seen++) {
    const p = n.parentElement; if (!p || ['SCRIPT', 'STYLE', 'NOSCRIPT'].includes(p.tagName) || !isShown(p)) continue;
    const t = n.textContent.replace(/\s+/g, ' ').trim(); if (t.length < 1) continue;
    const s = getComputedStyle(p), size = Math.round(parseFloat(s.fontSize) * 2) / 2;
    chars += t.length; total += words(t);
    sizes.set(size, (sizes.get(size) || 0) + t.length); inks.set(s.color, (inks.get(s.color) || 0) + t.length); const f = familyOf(s); fams.set(f, (fams.get(f) || 0) + t.length);
    if (s.textAlign === 'center') centered += t.length;
    weights.push([size, t.length]);
  }
  weights.sort((a, b) => a[0] - b[0]);
  let acc = 0, corps = null; for (const [size, c] of weights) { acc += c; if (acc >= chars / 2) { corps = size; break; } }
  const familles = [...fams.entries()].filter(([, c]) => c / chars >= 0.02).map(([f]) => f);
  const petit = sizes.size ? [...sizes.entries()].sort((a, b) => a[0] - b[0])[0] : null;
  // Titres visibles et titre d'accueil : le premier h1 visible, sinon le plus grand texte du premier écran.
  const heads = [...document.querySelectorAll('h1,h2,h3,h4,h5,h6')].filter(isShown).slice(0, 8);
  const info = el => { const t = (el.innerText || el.textContent || '').replace(/\s+/g, ' ').trim();
    return {texte: t.slice(0, 60), mots: words(t), caracteres: t.length, lignes: lineCount(el), ...typo(el)}; };
  const titres = heads.map(h => ({balise: h.tagName.toLowerCase(), ...info(h)}));
  let accueil = titres.find(t => t.balise === 'h1') || null;
  if (!accueil) { let best = null;
    for (const el of document.querySelectorAll('body *')) { if (!isShown(el) || !el.childNodes.length || ![...el.childNodes].some(c => c.nodeType === 3 && c.textContent.trim())) continue;
      const r = el.getBoundingClientRect(); if (r.top > H) continue; const size = parseFloat(getComputedStyle(el).fontSize); if (!best || size > best.size) best = {el, size}; }
    if (best) accueil = {balise: best.el.tagName.toLowerCase(), ...info(best.el)}; }
  // Mesure de ligne : caractères par ligne des paragraphes longs.
  const mesures = [...document.querySelectorAll('p,li,blockquote,dd')].filter(isShown).map(el => ({c: (el.innerText || '').trim().length, l: lineCount(el)}))
    .filter(x => x.c >= 60).map(x => Math.round(x.c / x.l)).sort((a, b) => a - b);
  // Images : raster visibles (un SVG ne compte pas), vidéo, canvas ; part du premier écran du média le plus étendu.
  const isSvg = u => /\.svg(\?|#|$)|^data:image\/svg/i.test(u || '');
  const rasters = [...document.images].filter(i => i.naturalWidth > 0 && !isSvg(i.currentSrc || i.src) && isShown(i) && i.getBoundingClientRect().width >= 80);
  const videos = [...document.querySelectorAll('video')].filter(isShown), canvases = [...document.querySelectorAll('canvas')].filter(isShown);
  const svgs = [...document.querySelectorAll('svg')].filter(s => !s.parentElement.closest('svg') && isShown(s) && s.getBoundingClientRect().width >= 80);
  let part = 0; for (const el of [...rasters, ...videos, ...canvases]) { const r = el.getBoundingClientRect();
    const x = Math.max(0, Math.min(r.right, W) - Math.max(r.left, 0)), y = Math.max(0, Math.min(r.bottom, H) - Math.max(r.top, 0)); part = Math.max(part, x * y / (W * H)); }
  // Fonds de section distincts et bords gauches des blocs de texte.
  const fonds = new Set(); for (const el of document.querySelectorAll('body > *, main > *, section')) { if (!isShown(el)) continue; const r = el.getBoundingClientRect();
    if (r.width < W * 0.5 || r.height < 120) continue; const c = getComputedStyle(el).backgroundColor; if (c && c !== 'rgba(0, 0, 0, 0)' && c !== 'transparent') fonds.add(c); }
  const bords = new Set(); for (const el of document.querySelectorAll('p,h1,h2,h3,h4,h5,h6,li,dt,dd,blockquote')) { if (!isShown(el) || (el.innerText || '').trim().length < 20) continue;
    bords.add(Math.round(el.getBoundingClientRect().left / 8) * 8); }
  // Gros texte du premier écran couvert ou rogné. Sur chaque ligne de texte de 24 px ou plus, huit points sont testés avec
  // elementFromPoint (pointer-events forcé le temps du relevé) : un point est couvert si un autre élément qui peint (média,
  // fond, texte) se trouve dessus. Le haut est rogné si un ancêtre à débordement masqué ou à clip-path coupe la ligne dans sa
  // partie haute. Premier écran seulement : le défilement et les états d'interaction ne sont pas parcourus.
  const gros = {testes: 0, couverts: [], hauts_rognes: []};
  const stl = document.createElement('style'); stl.textContent = '*,*::before,*::after{pointer-events:auto!important}';
  (document.head || document.documentElement).appendChild(stl);
  try {
    const MEDIA = /^(IMG|VIDEO|CANVAS|PICTURE|IFRAME|svg)$/;
    const paints = (h, el) => { for (let p = h; p && p !== document.body && !p.contains(el); p = p.parentElement) {
        if (MEDIA.test(p.tagName) || p.closest('svg')) return true;
        const s = getComputedStyle(p); if (s.backgroundImage !== 'none') return true;
        const m = s.backgroundColor.match(/rgba?\(([^)]+)\)/), parts = m ? m[1].split(/[,\s/]+/).filter(Boolean) : [];
        if (parts.length && (parts.length < 4 || parseFloat(parts[3]) > 0.05)) return true;
        if (p === h && [...p.childNodes].some(n => n.nodeType === 3 && n.nodeValue.trim())) return true; }
      return false; };
    const rg = document.createRange();
    for (const el of document.querySelectorAll('h1,h2,h3,h4,h5,h6,p,blockquote,li,a,button,span,div')) {
      let direct = ''; for (const n of el.childNodes) if (n.nodeType === 3) direct += n.nodeValue;
      if (direct.trim().length < 3) continue;
      const cs = getComputedStyle(el), size = parseFloat(cs.fontSize);
      if (size < 24 || !isShown(el) || el.getBoundingClientRect().top >= H) continue;
      gros.testes++;
      const unit = el.closest('h1,h2,h3,h4,h5,h6,p,blockquote'), clips = [];
      for (let p = el.parentElement; p && p !== document.body; p = p.parentElement) { const s = getComputedStyle(p);
        if (s.overflowX !== 'visible' || s.overflowY !== 'visible' || s.clipPath !== 'none') clips.push(p.getBoundingClientRect()); }
      let total = 0, hidden = 0, cut = false;
      for (const node of el.childNodes) { if (node.nodeType !== 3 || !node.nodeValue.trim()) continue;
        rg.selectNodeContents(node);
        for (const r of rg.getClientRects()) { if (r.width < 6 || r.bottom < 0 || r.top > H) continue;
          const lh = parseFloat(cs.lineHeight), band = Math.min(r.height, Number.isFinite(lh) ? lh : r.height);
          for (const dy of [-0.2, 0.2]) for (const fx of [0.12, 0.37, 0.63, 0.88]) {
            const x = r.left + r.width * fx, y = r.top + r.height * 0.55 + band * dy; if (x < 0 || x >= W || y < 0 || y >= H) continue;
            total++; const h = document.elementFromPoint(x, y);
            if (h && h !== el && !el.contains(h) && !h.contains(el) && !(unit && unit.contains(h) && !MEDIA.test(h.tagName) && !h.closest('svg')) && paints(h, el)) hidden++; }
          if (size >= 40 && r.top >= -4 && clips.some(c => c.top > r.top + r.height * 0.3 && c.top < r.bottom - r.height * 0.2)) cut = true; } }
      const texte = (el.innerText || direct).replace(/\s+/g, ' ').trim().slice(0, 48);
      if (total >= 4 && hidden / total >= 0.2) gros.couverts.push({texte, part: Math.round(hidden / total * 100)});
      if (cut) gros.hauts_rognes.push(texte);
    }
  } finally { stl.remove(); }
  gros.couverts = gros.couverts.slice(0, 5); gros.hauts_rognes = gros.hauts_rognes.slice(0, 5);
  // Premier écran : actions et navigation. Une action est un bouton, un lien d'action ou un champ d'envoi d'une taille de bouton (28 à 84 px
  // de haut, 64 px de large au moins) qui porte un fond opaque ou une bordure ; la navigation est le premier bloc de navigation ou d'en-tête,
  // sa hauteur est prise sur l'ancêtre fixe ou collant s'il y en a un. Relevé seulement : aucun nombre d'actions ni de liens n'est attendu.
  const actions = [...document.querySelectorAll('button, [role="button"], input[type="submit"], input[type="button"], a[href]')].filter(el => {
    if (!isShown(el) || el.closest('footer')) return false; const r = el.getBoundingClientRect();
    if (r.top >= H || r.bottom <= 0 || r.height < 28 || r.height > 84 || r.width < 64 || r.width > Math.min(W * 0.96, 900)) return false;
    const st = getComputedStyle(el), bg = color(st.backgroundColor); return (bg && bg[3] >= 0.5) || (parseFloat(st.borderTopWidth) || 0) >= 1; });
  const navEl = [...document.querySelectorAll('header nav, nav, header, [role="navigation"]')].find(isShown);
  let navigation = null;
  if (navEl) { let host = navEl, fixe = false;
    for (let p = navEl, i = 0; i < 4 && p && p !== document.body; i++, p = p.parentElement) { const pos = getComputedStyle(p).position; if (pos === 'fixed' || pos === 'sticky') { fixe = true; host = p; break; } }
    const hr = host.getBoundingClientRect(), liens = [...navEl.querySelectorAll('a')].filter(a => { const r = a.getBoundingClientRect(); return r.width > 0 && r.top < 140; }).length;
    navigation = {liens, fixe, hauteur: Math.round(hr.height), part: Math.round(Math.min(hr.height, Math.max(0, H - Math.max(hr.top, 0))) / H * 100)}; }
  const premier_ecran = {actions: actions.length, textes: actions.slice(0, 3).map(a => (a.innerText || a.value || '').replace(/\s+/g, ' ').trim().slice(0, 30)), navigation};
  // Palette, mesurée en OKLCH (L luminosité de 0 à 1, C chroma, H teinte en degrés) : fond, fonds de section voisins et leurs écarts de
  // luminosité, encres par part des caractères, couleurs chromatiques (C de 0,06 ou plus) par part du premier écran et des caractères.
  // Un relevé, aucun seuil : les fonds en image ou en dégradé et les textes translucides sur fond inconnu ne sont pas évalués.
  const rd = (v, d) => Math.round(v * 10 ** d) / 10 ** d;
  const desc = c => { const o = oklch(c); return {hex: hex(c), L: rd(o.L, 2), C: rd(o.C, 3), H: Math.round(o.H)}; };
  const groundBox = effBg(document.body), ground = groundBox.kind === 'solid' ? groundBox.c : null;
  const palette = {fond: ground ? desc(ground) : null, fonds: [], fonds_non_evalues: 0, ecarts: [], encres: [], chromatiques: [], teintes: 0};
  const cand = [...document.querySelectorAll('body > *, main > *, section')].filter(el => { if (!isShown(el)) return false;
    const r = el.getBoundingClientRect(); return r.width >= W * 0.5 && r.height >= 120; });
  const leaves = cand.filter(el => !cand.some(o => o !== el && el.contains(o)));
  const runs = [];
  for (const el of leaves.sort((a, b) => a.getBoundingClientRect().top - b.getBoundingClientRect().top)) { const box = effBg(el);
    if (box.kind !== 'solid') { palette.fonds_non_evalues++; continue; }
    const hx = hex(box.c); if (!runs.length || runs[runs.length - 1].hex !== hx) runs.push({hex: hx, c: box.c}); }
  palette.fonds = runs.slice(0, 12).map(x => desc(x.c));
  const hueGap = (a, b) => { const d = Math.abs(a - b) % 360; return d > 180 ? 360 - d : d; };
  for (let i = 1; i < palette.fonds.length; i++) { const a = palette.fonds[i - 1], b = palette.fonds[i];
    palette.ecarts.push({dL: rd(Math.abs(a.L - b.L), 2), dH: a.C >= 0.03 && b.C >= 0.03 ? Math.round(hueGap(a.H, b.H)) : null}); }
  const tally = new Map();   // hex -> {c, caracteres, surface}
  const entry = c => { const k = hex(c); if (!tally.has(k)) tally.set(k, {c, caracteres: 0, surface: 0}); return tally.get(k); };
  const inkTotal = [...inks.values()].reduce((a, b) => a + b, 0);
  for (const [str, n] of inks) { let c = color(str); if (!c) continue; if (c[3] < 1) { if (!ground) continue; c = over(c, ground); }
    entry(c).caracteres += n; }
  const chromatic = c => oklch(c).C >= 0.06;
  let seen = 0;
  for (const el of document.querySelectorAll('body *')) { if (++seen > 4000) break;
    const r = el.getBoundingClientRect(); if (r.bottom <= 0 || r.top >= H || r.width < 2 || r.height < 2) continue;
    const bg = color(getComputedStyle(el).backgroundColor); if (!bg || bg[3] < 0.9 || !chromatic(bg) || !isShown(el)) continue;
    const parent = el.parentElement ? effBg(el.parentElement) : null; if (parent && parent.kind === 'solid' && hex(parent.c) === hex(bg)) continue;
    const x = Math.max(0, Math.min(r.right, W) - Math.max(r.left, 0)), y = Math.max(0, Math.min(r.bottom, H) - Math.max(r.top, 0));
    entry(bg).surface += x * y / (W * H); }
  const all = [...tally.values()];
  palette.encres = all.filter(e => e.caracteres > 0 && !chromatic(e.c)).sort((a, b) => b.caracteres - a.caracteres).slice(0, 3)
    .map(e => ({...desc(e.c), part: Math.round(e.caracteres / Math.max(1, inkTotal) * 100)}));
  const chroma = all.filter(e => chromatic(e.c)).map(e => ({...desc(e.c), surface: rd(Math.min(1, e.surface) * 100, 1), caracteres: Math.round(e.caracteres / Math.max(1, inkTotal) * 100)}))
    .sort((a, b) => (b.surface + b.caracteres) - (a.surface + a.caracteres));
  palette.chromatiques = chroma.slice(0, 4);
  palette.teintes = new Set(chroma.filter(e => e.surface >= 1 || e.caracteres >= 1).map(e => Math.round(e.H / 30) % 12)).size;
  return {viewport: W, titre: accueil, titres, corps, tailles_distinctes: sizes.size, familles, plus_petit: petit ? {taille: petit[0], part: Math.round(petit[1] / chars * 100)} : null, gros_textes: gros, palette, premier_ecran, mesure_max: mesures.length ? mesures[mesures.length - 1] : null,
          mesure_mediane: mesures.length ? mesures[Math.floor(mesures.length / 2)] : null,
          images: {raster: rasters.length, video: videos.length, canvas: canvases.length, svg: svgs.length}, media_premier_ecran: Math.round(part * 100),
          centre_pour_cent: chars ? Math.round(centered / chars * 100) : 0, fonds_distincts: fonds.size, bords_gauches: bords.size,
          mots: total, ecrans: r1(document.documentElement.scrollHeight / H)};
}
"""

MESURES_JS = MESURES_JS.replace('__COLOR_JS__', COLOR_JS)


def format_mesures(per: dict) -> list[str]:
    """Lignes lisibles des mesures de composition, une par largeur. Aucune lecture de seuil : des relevés seulement."""
    lines = []
    for w, d in per.items():
        m = d.get("mesures")
        if not m:
            continue
        t, parts = m.get("titre"), []
        if t:
            parts.append(f"titre « {t['texte']} » {t['mots']} mot(s), {t['lignes']} ligne(s), {t['taille']} px ({t['vw']} vw), "
                         f"interligne {t['interligne']}, approche {t['approche']} em, graisse {t['graisse']}")
        else:
            parts.append("aucun titre visible")
        parts.append(f"corps {m.get('corps')} px, {m.get('tailles_distinctes')} taille(s) distincte(s), {len(m.get('familles', []))} famille(s) ({', '.join(m.get('familles', [])[:3])})")
        if m.get("plus_petit"):
            parts.append(f"plus petit texte {m['plus_petit']['taille']} px ({m['plus_petit']['part']} % des caractères)")
        pe = m.get("premier_ecran")
        if pe:
            nav = pe.get("navigation")
            parts.append(f"premier écran : {pe.get('actions', 0)} action(s)" + (f" ({', '.join('« ' + t + ' »' for t in pe.get('textes', []) if t)})" if pe.get("actions") else "")
                         + " ; " + (f"navigation {nav['liens']} lien(s), {nav['hauteur']} px ({nav['part']} % de la hauteur)" + (", fixe" if nav.get("fixe") else "") if nav else "aucune navigation repérée"))
        g = m.get("gros_textes")
        if g:
            found = [f"couvert à {c['part']} % « {c['texte']} »" for c in g.get("couverts", [])] + [f"haut rogné « {x} »" for x in g.get("hauts_rognes", [])]
            parts.append(f"gros textes du premier écran ({g.get('testes', 0)} testé(s)) : " + (", ".join(found) if found else "aucun couvert ni rogné"))
        parts.append(f"ligne de texte {m.get('mesure_mediane')} car. en médiane, {m.get('mesure_max')} au plus" if m.get("mesure_max") is not None else "aucun paragraphe long")
        im = m.get("images", {})
        parts.append(f"images : {im.get('raster', 0)} raster, {im.get('video', 0)} vidéo, {im.get('canvas', 0)} canvas, {im.get('svg', 0)} svg ; média dominant {m.get('media_premier_ecran')} % du premier écran")
        parts.append(f"texte centré {m.get('centre_pour_cent')} % ; {m.get('fonds_distincts')} fond(s) de section distinct(s) ; {m.get('bords_gauches')} bord(s) gauche(s) de texte ; {m.get('mots')} mots sur {m.get('ecrans')} écran(s)")
        lines.append(f"  {w} px : " + " ; ".join(parts))
        p = m.get("palette")
        if p:
            col = lambda x: f"{x['hex']} (L {x['L']}, C {x['C']}" + (f", H {x['H']}°)" if x['C'] >= 0.02 else ", teinte négligeable)")
            q = [f"fond {col(p['fond'])}" if p.get("fond") else "fond non évalué"]
            q.append(f"{len(p.get('fonds', []))} fond(s) de section de couleurs distinctes"
                     + (f", écart de luminosité entre voisins {', '.join(str(e['dL']) for e in p.get('ecarts', []))}" if p.get("ecarts") else "")
                     + (f" ; {p['fonds_non_evalues']} en image ou en dégradé, non évalué(s)" if p.get("fonds_non_evalues") else ""))
            q.append("encres " + (", ".join(f"{col(e)} {e['part']} % des caractères" for e in p.get("encres", [])) or "aucune mesurée"))
            q.append("couleurs chromatiques " + (", ".join(f"{col(e)} {e['surface']} % du premier écran, {e['caracteres']} % des caractères" for e in p.get("chromatiques", [])) or "aucune")
                     + f" ; {p.get('teintes', 0)} teinte(s) à 1 % ou plus")
            lines.append(f"  {w} px, palette : " + " ; ".join(q))
    return lines


def sha12(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()[:12]


@contextmanager
def page_url(args: argparse.Namespace):
    """Serveur local explicitement choisi pour les navigateurs qui refusent file://."""
    if re.match(r"^https?://", args.page):
        yield args.page
    elif not args.serve_local:
        yield Path(args.page).resolve().as_uri()
    else:
        target = Path(args.page).resolve()

        class QuietHandler(http.server.SimpleHTTPRequestHandler):
            def log_message(self, *_args):
                pass

        handler = functools.partial(QuietHandler, directory=str(target.parent))
        server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
        thread = threading.Thread(target=server.serve_forever, kwargs={"poll_interval": 0.05}, daemon=True)
        thread.start()
        try:
            yield f"http://127.0.0.1:{server.server_port}/{quote(target.name)}"
        finally:
            server.shutdown()
            server.server_close()
            thread.join()


def measure(args: argparse.Namespace) -> dict:
    with page_url(args) as url:
        return measure_url(args, url)


def measure_url(args: argparse.Namespace, url: str) -> dict:
    """Ouvre la page dans Chromium et retourne les mesures brutes. Lève ImportError si Playwright manque."""
    from playwright.sync_api import Error as PlaywrightError, sync_playwright  # import optionnel
    is_url = re.match(r"^https?://", url) is not None
    origin = None
    if is_url:
        sp = urlsplit(url)
        origin = f"{sp.scheme}://{sp.netloc}"
    widths = [int(w) for w in args.widths.split(",") if w.strip()]
    state = {"blocked": 0}
    raw: dict = {"widths": widths, "per_width": {}, "running": [], "captures": [],
                 "local_server": args.serve_local and not re.match(r"^https?://", args.page)}
    with sync_playwright() as pw:
        try:
            browser = pw.chromium.launch(**({"executable_path": args.browser_executable} if args.browser_executable else {}))
        except PlaywrightError as exc:
            raise BrowserUnavailable(str(exc).splitlines()[0][:160]) from exc
        raw["browser"] = {"engine": "chromium", "version": browser.version,
                          "executable": args.browser_executable or "playwright-managed"}

        def open_page(width: int, reduced: bool = False):
            ctx = browser.new_context(viewport={"width": width, "height": 844 if width < 700 else 900},
                                      reduced_motion="reduce" if reduced else "no-preference")
            if reduced:  # avant tout script de la page : une animation d'entrée courte serait sinon terminée à la mesure
                ctx.add_init_script(MOTION_RECORDER_JS)
            page = ctx.new_page()
            errs: list[str] = []

            def route(r):
                u = r.request.url
                # La page cible et sa propre origine passent ; le reste est bloqué sauf --allow-external.
                if args.allow_external or (origin and (u == origin or u.startswith(origin + "/"))):
                    r.continue_()
                else:
                    state["blocked"] += 1
                    r.abort()
            page.route(re.compile(r"^https?://"), route)
            page.on("pageerror", lambda e: errs.append(str(e)))
            page.on("console", lambda m: errs.append(m.text) if m.type == "error" and "ERR_" not in m.text and "Failed to load resource" not in m.text else None)
            page.goto(url, wait_until="load")
            page.wait_for_timeout(args.wait_ms)
            # Défilement complet : déclenche le contenu révélé au scroll, qui sera ainsi mesuré et capturé.
            step, y = page.viewport_size["height"] // 2, 0
            while y < page.evaluate("document.documentElement.scrollHeight"):
                page.evaluate(f"window.scrollTo({{top: {y}, behavior: 'instant'}})")
                page.wait_for_timeout(120)
                y += step
            page.evaluate(SCROLL_TOP)
            page.wait_for_timeout(300)
            for sel in args.click:
                page.click(sel)
                page.wait_for_timeout(300)
            if getattr(args, "wait_after_ms", 0):
                page.wait_for_timeout(args.wait_after_ms)
            return ctx, page, errs

        for w in widths:
            ctx, page, errs = open_page(w)
            # Preuve d'état : avant les captures, la tabulation et tout défilement, à l'état atteint par --click et
            # --wait-after-ms ; le résultat ne dépend donc pas de --captures.
            textlayout = page.evaluate(TEXT_LAYOUT_JS)
            asserts = []
            for expr in getattr(args, "assert_", []) or []:
                try:
                    value = page.evaluate(f"() => ({expr})")
                    asserts.append({"expr": expr, "ok": value is True, "value": value if isinstance(value, (bool, int, float, str)) or value is None else str(value)})
                except PlaywrightError as exc:
                    asserts.append({"expr": expr, "ok": False, "value": "erreur : " + str(exc).splitlines()[0][:120]})
            frames = [page.evaluate(IN_FRAME_JS, spec) for spec in (getattr(args, "in_frame", []) or [])]
            if args.captures:  # avant la tabulation, qui déplacerait le focus visible
                shot = capture_paths(args.captures, [w])[0]
                shot.parent.mkdir(parents=True, exist_ok=True)
                page.evaluate(SCROLL_TOP)
                page.screenshot(path=str(shot), full_page=True)
                raw["captures"].append(str(shot))
            dims = page.evaluate("({sw: document.documentElement.scrollWidth, cw: document.documentElement.clientWidth})")
            offenders = page.evaluate("""() => [...document.querySelectorAll('body *')].filter(e => {
                const r = e.getBoundingClientRect(); return r.right > document.documentElement.clientWidth + 1 && getComputedStyle(e).position !== 'fixed'; })
                .slice(0, 4).map(e => e.tagName.toLowerCase() + (e.className && e.className.baseVal === undefined ? '.' + String(e.className).split(' ')[0] : ''))""")
            audit = page.evaluate(AUDIT_JS, FOC)
            proof = None
            if args.proof:
                page.evaluate(SCROLL_TOP)
                proof = page.evaluate(PROOF_JS, args.proof)
            keyboard = page.evaluate(BASELINE_JS, FOC)
            stops: list[str] = []
            missing: list[str] = []
            focus_cues: list[dict] = []
            unexpected: list[str] = []
            visited: set[str] = set()
            reason = 'limit'
            for _ in range(args.tab_stops):
                page.keyboard.press("Tab")
                f = page.evaluate(FOCUS_JS)
                if f.get("end") or f.get("cycle"):
                    reason = 'end' if f.get('end') else 'cycle'
                    break
                if f["isNew"]:
                    stops.append(f["id"])
                    if f.get('key'):
                        visited.add(f['key'])
                    else:
                        unexpected.append(f['id'])
                    if not f["indicator"]:
                        missing.append(f["id"])
                    else:
                        cue = page.evaluate(FOCUS_CUE_JS) or {"cues": [], "other": True, "ua": False}
                        focus_cues.append({"id": f["id"], **cue})
            keyboard.update(reason=reason, tab_limit=args.tab_stops, visited=sorted(visited),
                            unreached=[e['id'] for e in keyboard['expected'] if e['key'] not in visited], unexpected=unexpected)
            raw["per_width"][w] = {"overflow": dims, "offenders": offenders, "errs": errs, "audit": audit, "proof": proof,
                                   "textlayout": textlayout, "asserts": asserts, "frames": frames,
                                   "stops": stops, "missing_ind": missing, "focus_cues": focus_cues, "keyboard": keyboard}
            ctx.close()
            if args.mesures:  # relevés seulement, jamais lus par interpret ; page à part : ils ne modifient pas la page contrôlée
                mctx, mpage, _ = open_page(w)
                raw["per_width"][w]["mesures"] = mpage.evaluate(MESURES_JS)
                mctx.close()

        ctx, page, _ = open_page(widths[0], reduced=True)
        raw["running"] = page.evaluate(MOTION_REPORT_JS)
        ctx.close()
        browser.close()
    raw["blocked"] = state["blocked"]
    return raw


def interpret(raw: dict, proof_sel: str = "") -> list[tuple[str, str, str]]:
    """Transforme les mesures brutes en contrôles. Fonction pure, testable sans navigateur."""
    widths, per = raw["widths"], raw["per_width"]
    checks: list[tuple[str, str, str]] = []
    ov = [f"{w} px : {d['overflow']['sw']} > {d['overflow']['cw']} ({', '.join(d['offenders']) or 'élément non isolé'})"
          for w, d in per.items() if d["overflow"]["sw"] > d["overflow"]["cw"] + 1]
    checks.append(("Débordement horizontal", RETURN if ov else PASS, "; ".join(ov) or f"aucun à {', '.join(map(str, widths))} px"))

    inner = [(w, i) for w, d in per.items() for i in d["audit"]["inner"]]
    dlg = sorted({f"{w} px : {i['sel']} {i['sw']} > {i['cw']}" for w, i in inner if i["dialog"]})
    scr = sorted({f"{i['sel']} {i['sw']} > {i['cw']}" for _, i in inner if not i["dialog"]})
    checks.append(("Défilement horizontal interne", RETURN if dlg else (RESERVE if scr else PASS),
                   ("feuille ouverte qui défile horizontalement : " + "; ".join(dlg[:3])) if dlg else
                   ("conteneur défilant horizontalement, voulu ou défaut : " + "; ".join(scr[:3])) if scr else "aucun"))

    errs = sorted({e for d in per.values() for e in d["errs"]})
    checks.append(("Erreurs JavaScript au chargement", RETURN if errs else PASS, "; ".join(errs)[:200] or "aucune"))

    # Textes qui se recouvrent ou sont tronqués (rectangles de lignes ; calques fixes ou collants exclus).
    layouts = {w: d.get("textlayout") for w, d in per.items()}
    if all(v is None for v in layouts.values()):
        checks.append(("Chevauchement et troncature de texte", NOTVER, "non mesuré"))
    else:
        overlap_parts = [f"{w} px : « {a} » et « {b} » ({ox}×{oy} px)" for w, v in layouts.items() if v for a, b, ox, oy in v.get("overlaps", [])[:3]]
        trunc_parts = [f"{w} px : « {x} »" for w, v in layouts.items() if v for x in v.get("trunc", [])[:3]]
        deco_parts = [f"{w} px : « {a} » et « {b} »" for w, v in layouts.items() if v for a, b, _, _ in v.get("decorative", [])[:3]]
        status = RETURN if overlap_parts else (RESERVE if trunc_parts or deco_parts else PASS)
        detail = "; ".join(overlap_parts + (["tronqué, à juger : " + ", ".join(trunc_parts)] if trunc_parts else [])
                           + (["texte décoratif superposé, à juger : " + ", ".join(deco_parts)] if deco_parts else []))
        checks.append(("Chevauchement et troncature de texte", status,
                       (detail or f"aucun à {', '.join(map(str, widths))} px") + " ; texte SVG compris, calques fixes ou collants exclus"))

    # Preuve d'état demandée par l'auteur : assertions et objet de l'état clé dans son cadre.
    if any(d.get("asserts") for d in per.values()):
        bad = [f"{w} px : {a['expr'][:60]} → {a['value']!r}"[:140] for w, d in per.items() for a in d.get("asserts", []) if not a["ok"]]
        total = sum(len(d.get("asserts", [])) for d in per.values())
        checks.append(("Assertions d’état (--assert)", RETURN if bad else PASS, "; ".join(bad[:4]) or f"{total} assertion(s) vraie(s) à l’état observé"))
    if any(d.get("frames") for d in per.values()):
        bad = []
        for w, d in per.items():
            for f in d.get("frames", []):
                if f.get("error"):
                    bad.append(f"{w} px : {f['spec']} : {f['error']}")
                elif not f.get("found"):
                    bad.append(f"{w} px : {f['spec']} : aucun élément visible")
                elif f.get("outside"):
                    bad.append(f"{w} px : {f['spec']} : {f['outside']} élément(s) sur {f['found']} hors du cadre")
        checks.append(("Objet de l’état clé dans son cadre (--in-frame)", RETURN if bad else PASS,
                       "; ".join(bad[:4]) or "tous les éléments ont leur centre dans le cadre, à l’état observé"))

    contrast = [c for d in per.values() for c in d["audit"]["contrast"]]
    nonsolid = sorted({n["sel"] for d in per.values() for n in d["audit"]["nonSolid"]})
    unknown = sorted({f"{u['sel']} ({u['value']})" for d in per.values() for u in d["audit"].get("unknown", [])})
    svg_text = sorted({s["sel"] for d in per.values() for s in d["audit"].get("svgText", [])})
    group_opacity = sorted({s["sel"] for d in per.values() for s in d['audit'].get('groupOpacity', [])})
    limits = []
    coverage_details = []
    for w, d in per.items():
        c = d['audit'].get('contrastCoverage')
        if not c or c.get('method') != 'dom-text-bounded':
            limits.append(f'{w} px : couverture du texte non enregistrée')
            continue
        coverage_details.append(f"{w} px : {c['evaluated']} texte(s) évalué(s), {c['candidates']} candidat(s), {c['excluded']} exclu(s)")
        if c.get('unmeasured'):
            limits.append(f"{w} px : texte non évalué : " + ', '.join(f"{u['sel']} ({u['kind']})" for u in c['unmeasured'][:6]))
        if c['evaluated'] + c['excluded'] + len(c.get('unmeasured', [])) < c['candidates']:
            limits.append(f'{w} px : candidat(s) restant hors évaluation')
    if group_opacity:
        limits.append('opacité de groupe, composition non évaluée : ' + ', '.join(group_opacity[:5]))
    if nonsolid:
        limits.append("fond en dégradé, en image ou translucide sur flou d’arrière-plan, non évalué : " + ", ".join(nonsolid[:5]) + (f" +{len(nonsolid)-5}" if len(nonsolid) > 5 else ""))
    if svg_text:
        limits.append("texte SVG non évalué (" + ", ".join(svg_text[:3]) + ") : relever fill/stroke, opacités et fond réel, "
                      "puis calculer le contraste ; méthode dans ACTION/RECETTE-RENDU")
    if unknown:
        limits.append("couleur non convertible, non évaluée : " + ", ".join(unknown[:4]) + (f" +{len(unknown)-4}" if len(unknown) > 4 else ""))
    if contrast:
        seen, lines = set(), []
        for c in contrast:
            k = (c["fg"], c["bg"], c["size"])
            if k not in seen:
                seen.add(k)
                lines.append(f"{c['sel']} {c['fg']} sur {c['bg']} = {c['ratio']}:1 (seuil {c['need']}:1, {c['size']} px, « {c['text']} »)")
        checks.append(("Contraste du texte sur fond uni", RETURN, " ; ".join(lines[:4]) + (f" ; +{len(lines)-4}" if len(lines) > 4 else "")
                       + (" ; " + " ; ".join(coverage_details + limits) if coverage_details or limits else "")))
    else:
        checks.append(("Contraste du texte sur fond uni", RESERVE if limits else PASS,
                       ("aucun texte évalué sous le seuil WCAG 2.2 AA" if any(d['audit'].get('contrastCoverage', {}).get('evaluated', 0) for d in per.values())
                        else "aucun texte évalué ; couverture incomplète" if limits else "aucun candidat applicable dans le DOM inspecté")
                       + (" ; " + " ; ".join(coverage_details + limits) if coverage_details or limits else "")))

    names = sorted({n["sel"] for d in per.values() for n in d["audit"]["names"]})
    name_measured = all(d['audit'].get('nameMethod') == 'dom-candidate' for d in per.values())
    name_count = max((d['audit'].get('nameControls', 0) for d in per.values()), default=0)
    name_detail = 'sans nom candidat dans les cas DOM couverts : ' + ', '.join(names[:6]) if names else (
        f'{name_count} contrôle(s) DOM inspecté(s) ; nom accessible calculé non vérifié' if name_count else 'aucun contrôle applicable dans le périmètre DOM inspecté')
    name_uncertain = sorted({n['sel'] for d in per.values() for n in d['audit'].get('nameUncertain', [])})
    if name_uncertain:
        name_detail += ' ; candidat hors couverture : ' + ', '.join(name_uncertain[:6])
    if not name_measured:
        name_detail += ' ; méthode et couverture non enregistrées'
    checks.append(("Nom accessible des contrôles (candidats DOM)", RETURN if names else (
        RESERVE if not name_measured or name_count else PASS), name_detail))

    small = {(t["sel"], t["w"], t["h"], t["spaced"]) for d in per.values() for t in d["audit"]["targets"]}
    crowded = sorted({f"{s} {w}×{h}" for s, w, h, sp in small if not sp})
    spaced = sorted({f"{s} {w}×{h}" for s, w, h, sp in small if sp})
    ua = max((d["audit"].get("uaControls", 0) for d in per.values()), default=0)
    note = (f" ; {len(spaced)} petite(s) cible(s) admise(s) par l'espacement" if spaced else "") + (f" ; {ua} contrôle(s) natif(s) exclu(s)" if ua else "")
    checks.append(("Taille des cibles (WCAG 2.2, 2.5.8)", RESERVE if crowded else PASS,
                   ("moins de 24 px sans l'espacement requis : " + ", ".join(crowded[:6]) + " ; exceptions « équivalent » ou « essentiel » à juger" + note)
                   if crowded else ("toutes les cibles hors texte courant satisfont la taille ou l'espacement" + note)))

    a0 = per[widths[0]]["audit"]
    imgs = sorted({i["sel"] for d in per.values() for i in d["audit"]["imgs"]})
    struct = []
    if imgs:
        struct.append("image sans alt : " + ", ".join(imgs[:4]))
    if not a0["lang"]:
        struct.append("attribut lang absent")
    if not a0["title"]:
        struct.append("titre du document vide")
    checks.append(("Structure du document (alt, lang, titre)", RETURN if struct else PASS, "; ".join(struct) or "alt, lang et titre présents"))
    checks.append(("Un seul titre de premier niveau visible", PASS if a0["h1"] == 1 else RESERVE, f"{a0['h1']} h1 visible(s)"))

    # Image cassée : aucune intention de design ne l'explique. Une image d'une autre origine, bloquée par la mesure
    # (pas de --allow-external), n'est pas vérifiée : réserve ; si rien n'a été bloqué, elle est réellement introuvable.
    broken = [(b["sel"], b["external"]) for d in per.values() for b in d["audit"].get("brokenImgs", [])]
    local = sorted({s for s, ext in broken if not ext})
    remote = sorted({s for s, ext in broken if ext})
    blocked = raw.get("blocked", 0) > 0
    if local or (remote and not blocked):
        broken_status = RETURN
    elif remote:
        broken_status = RESERVE
    else:
        broken_status = PASS
    pending = sorted({p["sel"] for d in per.values() for p in d["audit"].get("pendingImgs", [])})
    if pending and broken_status == PASS:
        broken_status = RESERVE
    broken_parts = ([f"image introuvable ou illisible : {', '.join(local[:4])}"] if local else []) + \
                   ([f"image d'une autre origine non chargée : {', '.join(remote[:4])}" + (" ; requêtes externes bloquées, --allow-external les charge" if blocked else " ; introuvable ou illisible")] if remote else []) + \
                   ([f"image encore en chargement à la mesure, non vérifiée : {', '.join(pending[:4])}"] if pending else [])
    checks.append(("Images chargées", broken_status, "; ".join(broken_parts) or "aucune image visible illisible"))

    miss = sorted({m for d in per.values() for m in d["missing_ind"]})
    keyboard_limits, keyboard_details = [], []
    for w, d in per.items():
        k = d.get('keyboard')
        keyboard_details.append(f"{len(d['stops'])} arrêt(s) à {w} px")
        if not k or not all(field in k for field in ('reason', 'expected', 'unreached', 'scope')):
            keyboard_limits.append(f'{w} px : couverture non enregistrée')
            continue
        keyboard_details.append(f"{w} px : {k['scope']}, fin={k['reason']}, {len(k['expected'])} candidat(s)")
        if k['reason'] not in ('end', 'cycle'):
            keyboard_limits.append(f"{w} px : parcours tronqué ({k['reason']})")
        if k['unreached']:
            keyboard_limits.append(f"{w} px : candidat(s) non atteint(s) : {', '.join(k['unreached'][:6])} ; vérifier aussi la navigation alternative")
        if k.get('unexpected'):
            keyboard_limits.append(f"{w} px : arrêt(s) hors inventaire de candidats : {', '.join(k['unexpected'][:6])}")
        if not k['expected'] and not d['stops']:
            keyboard_details.append(f'{w} px : aucun contrôle candidat applicable')
    if miss:
        keyboard_limits.append('aucun changement de style au focus sur : ' + ', '.join(miss[:6]))
    checks.append(("Parcours clavier : arrêts et indicateur de focus", RESERVE if keyboard_limits else PASS,
                   ' ; '.join(keyboard_details + keyboard_limits) + ' ; style observé, visibilité du focus à vérifier ; contraste : contrôle suivant'))

    # Contraste de l'indicateur de focus (WCAG 1.4.11, 3:1). Réserve si un indicateur mesuré est sous le seuil, même accompagné
    # d'un autre changement de style (fond, couleur, bordure, ombre floue) : non mesuré, celui-ci ne prouve pas que le focus se voit.
    # Les arrêts sans indicateur mesurable restent à juger, sans réserve.
    if any("focus_cues" in d for d in per.values()):
        low, good, unmeasured = {}, 0, set()
        for d in per.values():
            for c in d.get("focus_cues", []):
                best = max((m["ratio"] for m in c.get("cues", [])), default=None)
                if best is not None and best >= FOCUS_RATIO:
                    good += 1
                elif best is None and c.get("ua") and not c.get("other"):
                    good += 1
                elif best is not None:
                    m = max(c["cues"], key=lambda x: x["ratio"])
                    low[(c["id"] + (" (autre changement de style non mesuré)" if c.get("other") else ""), m["kind"], m["fg"], m["bg"], m["ratio"])] = None
                else:
                    unmeasured.add(c["id"])
        lines = [f"{i} : {k} {fg} sur {bg} = {r}:1" for (i, k, fg, bg, r) in list(low)[:4]]
        detail = ("indicateur sous le seuil de 3:1 (WCAG 1.4.11) : " + " ; ".join(lines) + (f" ; +{len(low)-4}" if len(low) > 4 else "") + " ; "
                  if low else "") + f"{good} arrêt(s) mesuré(s) ou à contour du navigateur sans défaut"
        if unmeasured:
            detail += f" ; non mesuré (changement de fond, couleur, bordure, ombre floue ou fond en image) : {', '.join(sorted(unmeasured)[:6])}"
        checks.append(("Contraste de l’indicateur de focus", RESERVE if low else PASS, detail))

    # `running` : animations démarrées sous préférence « mouvement réduit », même terminées à la mesure. Une entrée sans
    # `moves` (ancienne mesure) est traitée comme un déplacement, jamais écartée.
    running = raw.get("running", [])
    inf = [a for a in running if a["infinite"]]
    moving = [a for a in running if a.get("moves", True)]
    label = lambda a: (f"{a['target']} {a['name']}" if a.get("target") else a["name"])
    checks.append(("Mouvement réduit respecté", RETURN if inf else (RESERVE if running else PASS),
                   (f"animation infinie sous mouvement réduit : {', '.join(label(a) for a in inf)}" if inf else
                    f"{len(running)} animation(s) finie(s) démarrée(s) sous mouvement réduit, dont {len(moving)} avec déplacement"
                    + (f" ({', '.join(label(a) for a in moving[:4])})" if moving else "")
                    + " : vérifier qu'elles sont neutralisées pour cette préférence" if running else "aucune animation démarrée")))

    if proof_sel:
        parts, status = [], PASS
        for w, d in per.items():
            p = d["proof"]
            if not p or not p.get("found"):
                parts.append(f"{w} px : sélecteur introuvable"); status = RETURN
            elif p["hidden"] or p["w"] < 2 or p["h"] < 2:
                parts.append(f"{w} px : objet sans surface visible ({p['w']}×{p['h']})"); status = RETURN
            elif p.get('opacity') == 0:
                parts.append(f'{w} px : objet transparent (opacité cumulée nulle)'); status = RETURN
            else:
                covered = p.get('method') == 'css-rectangle-bounded' and all(field in p for field in ('intersectionWidth', 'opacity', 'limits'))
                ok = covered and p['intersectionWidth'] >= min(p['w'] * 0.4, 320) and p["visible"] >= min(p["h"] * 0.4, 320)
                parts.append(f"{w} px : intersection verticale {p['visible']} px sur {p['h']}, horizontale {p.get('intersectionWidth', 'inconnue')} px sur {p['w']}")
                if not covered:
                    parts.append('couverture CSS et intersection horizontale non enregistrées')
                elif p['limits'] or p['opacity'] != 1:
                    ok = False
                    parts.append('limites : ' + ', '.join(p['limits'] + (['opacité partielle'] if p['opacity'] != 1 else [])))
                if not ok and status == PASS:
                    status = RESERVE
        detail = "; ".join(parts) + ' ; rectangle et CSS observés, pixels et occlusion non vérifiés' + (" ; à juger : recomposition voulue ou défaut" if status == RESERVE else "")
        checks.append((f"Objet de preuve au premier écran ({proof_sel})", status, detail))
    else:
        checks.append(("Objet de preuve au premier écran", NOTVER, "aucun sélecteur fourni (--proof) : à juger à la main"))
    return checks


FOCUS_RATIO = 3.0
RANK = {PASS: 0, RESERVE: 1, RETURN: 2}


def measurement_settings(args: argparse.Namespace) -> dict:
    """Réglages qui changent les contrôles sans changer le périmètre : ils doivent être identiques pour comparer."""
    settings = {"proof": args.proof, "tab_stops": args.tab_stops, "allow_external": args.allow_external, "wait_ms": args.wait_ms}
    # Réglages de preuve d'état : inscrits seulement s'ils sont employés, pour qu'une mesure sans eux reste
    # comparable à une référence enregistrée avant leur existence.
    optional = {"wait_after_ms": getattr(args, "wait_after_ms", 0), "asserts": list(getattr(args, "assert_", []) or []),
                "in_frame": list(getattr(args, "in_frame", []) or [])}
    settings.update({key: value for key, value in optional.items() if value})
    return settings


def check_baseline_shape(baseline: object) -> None:
    if not isinstance(baseline, dict) or not isinstance(baseline.get("checks"), list) or not isinstance(baseline.get("provenance"), dict):
        raise ValueError("référence illisible : JSON produit par --json attendu (provenance et checks)")


def compare_baseline(checks: list[tuple[str, str, str]], scope: str, baseline: dict, settings: dict | None = None) -> dict:
    """Rapproche chaque contrôle de la mesure de référence (même périmètre et mêmes réglages) ; ne modifie aucun statut."""
    check_baseline_shape(baseline)
    before_scope = baseline["provenance"].get("scope")
    if before_scope != scope:
        return {"comparable": False, "reason": f"périmètre différent (référence : {before_scope} ; mesure : {scope})"}
    before_settings = baseline["provenance"].get("settings")
    if settings is not None and before_settings != settings:
        return {"comparable": False, "reason": f"réglages différents (référence : {before_settings} ; mesure : {settings})"}
    before = {c.get("check"): (c.get("status"), c.get("detail")) for c in baseline["checks"] if isinstance(c, dict)}
    rows = []
    for title, status, detail in checks:
        old_status, old_detail = before.pop(title, (None, None))
        if old_status is None:
            change = "nouveau contrôle en RETURN" if status == RETURN else "nouveau contrôle"
        elif status == RETURN and old_status == RETURN:
            change = "RETURN préexistant, inchangé" if detail == old_detail else "RETURN préexistant, détail modifié : à examiner"
        elif status == RETURN:
            change = "RETURN introduit"
        elif old_status == RETURN:
            change = "RETURN disparu"
        elif status in RANK and old_status in RANK and RANK[status] != RANK[old_status]:
            change = "dégradé" if RANK[status] > RANK[old_status] else "amélioré"
        else:
            change = "inchangé" if status == old_status else f"{old_status} → {status}"
        rows.append({"check": title, "before": old_status, "after": status, "change": change})
    rows += [{"check": title, "before": s, "after": None, "change": "contrôle absent de la mesure"} for title, (s, _) in before.items()]
    introduced = [r["check"] for r in rows if r["change"] in ("RETURN introduit", "nouveau contrôle en RETURN",
                                                              "RETURN préexistant, détail modifié : à examiner")]
    return {"comparable": True, "rows": rows, "introduced_or_to_examine": introduced}


def capture_paths(folder: str, widths: list[int]) -> list[Path]:
    return [Path(folder) / f"capture-{w}px.png" for w in widths]


def run(args: argparse.Namespace) -> int:
    target = args.page
    is_url = re.match(r"^https?://", target) is not None
    path = None if is_url else Path(target)
    if path is not None and not path.is_file():
        print(f"{NOTVER} : fichier introuvable : {target}", file=sys.stderr)
        return 2
    if args.captures:
        existing = [str(p) for p in capture_paths(args.captures, [int(w) for w in args.widths.split(",") if w.strip()]) if p.exists()]
        if existing:  # une capture « avant » ne doit jamais être écrasée par la suivante
            print(f"{NOTVER} : capture déjà présente, choisir un autre dossier : {', '.join(existing)}", file=sys.stderr)
            return 2
    baseline = None
    if args.baseline:
        try:
            baseline = json.loads(Path(args.baseline).read_text(encoding="utf-8"))
            check_baseline_shape(baseline)
        except (OSError, ValueError) as exc:
            print(f"{NOTVER} : référence illisible : {args.baseline} ({type(exc).__name__})", file=sys.stderr)
            return 2
    try:
        raw = measure(args)
    except ImportError:
        print(f"{NOTVER} : Playwright n'est pas installé. Aucune preuve AUTOMATED n'est produite "
              "(pip install playwright && playwright install chromium).", file=sys.stderr)
        return 2
    except Exception as exc:  # navigateur indisponible ou page non chargeable : pas de faux PASS
        print(f"{NOTVER} : la recette n'a pas pu s'exécuter ({type(exc).__name__}: {str(exc).splitlines()[0][:160]})", file=sys.stderr)
        return 2
    checks = interpret(raw, args.proof)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    prov = {"artifact_locator": target, "artifact_version": sha12(path) if path else "url (non versionnée)",
            "method": "AUTOMATED", "observed_at": now,
            "scope": f"état initial{' puis ' + ' puis '.join(args.click) if args.click else ''}{f', puis {args.wait_after_ms} ms' if args.wait_after_ms else ''}, largeurs {','.join(map(str, raw['widths']))} px",
            "external_requests_blocked": raw["blocked"], "settings": measurement_settings(args)}
    if raw.get("captures"):
        prov["captures"] = raw["captures"]
    if raw.get("browser"):
        prov["browser"] = raw["browser"]
    if raw.get("local_server"):
        prov["local_server"] = "127.0.0.1, temporaire"
    print(f"Recette AUTOMATED (GATE-A) — {target}\n")
    for title, status, detail in checks:
        print(f"[{status:<21}] {title} : {detail}")
    if not getattr(args, "sans_gestes", False):
        import gestes  # geste lié à chaque signal, lu dans SAVOIR/STATE (bloc COMP-VOCABULAIRE)
        servis = gestes.bloc("check_render", [(s, t, d) for t, s, d in checks])
        if servis:
            print(servis)
    import gestes  # rendez-vous : carte « regard » si une correction s'ouvre, planche après deux passages sans RETURN
    sans_retour_avant = baseline is not None and not any(c.get("status") == RETURN for c in baseline["checks"] if isinstance(c, dict))
    rendez_vous = gestes.suite("check_render", [(s, t, d) for t, s, d in checks],
                               "" if re.match(r"^https?://", args.page) else args.page, sans_retour_avant)
    if rendez_vous:
        print(rendez_vous)
    if getattr(args, "mesures", False):
        print("\nMesures de composition (relevés chiffrés, sans seuil ni verdict ; elles ne modifient ni les statuts ni le code de sortie) :")
        for line in format_mesures(raw["per_width"]):
            print(line)
    print("\nProvenance : " + " · ".join(f"{k}={v}" for k, v in prov.items()))
    print("Limites : seules les fautes objectivables sont contrôlées, à l'état et aux largeurs observés. "
          f"{raw['blocked']} requête(s) externe(s) bloquée(s) : les mesures utilisent alors les polices de repli. "
          "Les fonds en dégradé, en image ou translucides sur flou d’arrière-plan, les opacités de groupe, le texte SVG, le texte natif des contrôles et des pseudo-éléments ne sont pas évalués ; leur présence détectée conserve une réserve. "
          "La couverture du contraste est bornée au DOM inspecté ; le contraste non textuel des bordures et des icônes n'est pas mesuré ; celui de l'indicateur de focus ne l'est que pour un contour ou un anneau d'ombre net sur fond uni ; le ratio d'un texte qui passe n'est pas rapporté. L'objet de preuve mesure CSS et rectangle, sans vérifier les pixels ni l'occlusion. "
          "Les noms sont des candidats DOM, pas un calcul AccName ; leur présence conserve une réserve. "
          "Le clavier porte sur les candidats du périmètre actif et les arrêts observés ; une borne atteinte conserve une réserve. "
          "Le mouvement réduit enregistre les animations et transitions démarrées au chargement et au défilement, sur la première largeur ; "
          "les animations pilotées par script sans API d'animation du navigateur ne sont pas observées. "
          "Les captures montrent l'état observé ; elles ne jugent rien. "
          "Le chevauchement de texte est mesuré sur les rectangles de lignes, ramenés à l'interligne, hors calques fixes ou collants ; un texte décoratif superposé (aria-hidden ou très transparent) reste à juger ; il ne voit ni les glyphes ni les recouvrements par une image. "
          "Une assertion d'état ne prouve que ce qu'elle exprime, à l'état et aux largeurs observés. "
          "Cette recette ne valide ni la direction visuelle, ni le goût, ni l'utilisabilité, ni un verdict global.")
    comparison = None
    if baseline is not None:
        comparison = compare_baseline(checks, prov["scope"], baseline, prov["settings"])
        print(f"\nComparaison avec la référence {args.baseline} :")
        if not comparison["comparable"]:
            print(f"  non comparable : {comparison['reason']}")
        else:
            for row in comparison["rows"]:
                print(f"  {row['check']} : {row['change']}")
            introduced = comparison["introduced_or_to_examine"]
            print("  Défauts introduits ou à examiner : " + (", ".join(introduced) if introduced else "aucun")
                  + ". Les statuts et le code de sortie restent ceux de la mesure : un RETURN préexistant reste un défaut.")
    if args.json:
        coverage = {str(w): {**d.get('keyboard', {}), 'observed_stops': len(d['stops'])} for w, d in raw['per_width'].items()}
        Path(args.json).write_text(json.dumps({"provenance": prov, "checks": [{"check": t, "status": s, "detail": d} for t, s, d in checks],
                                              'keyboard_coverage': coverage,
                                              'contrast_coverage': {str(w): d['audit'].get('contrastCoverage', {}) for w, d in raw['per_width'].items()},
                                              'proof_observations': {str(w): d['proof'] for w, d in raw['per_width'].items()},
                                              **({'mesures': {str(w): d['mesures'] for w, d in raw['per_width'].items() if 'mesures' in d}} if getattr(args, 'mesures', False) else {}),
                                              **({'baseline_comparison': comparison} if comparison is not None else {})},
                                              ensure_ascii=False, indent=2), encoding="utf-8")
    return 1 if any(s == RETURN for _, s, _ in checks) else 0


def parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(description="Recette AUTOMATED optionnelle d'un rendu HTML (ACTION/GATE-A).")
    ap.add_argument("page", help="chemin d'un fichier HTML ou URL")
    ap.add_argument("--widths", default="390,768,1440", help="largeurs en px, séparées par des virgules")
    ap.add_argument("--proof", default="", help="sélecteur CSS de l'objet de preuve déclaré par l'auteur")
    ap.add_argument("--click", action="append", default=[], help="sélecteur à cliquer avant la mesure (répétable)")
    ap.add_argument("--wait-ms", type=int, default=1500, help="attente après chargement (animations d'entrée)")
    ap.add_argument("--wait-after-ms", type=int, default=0, help="attente après les clics, pour observer l'état qui compte (chargement, animation, résultat)")
    ap.add_argument("--assert", dest="assert_", action="append", default=[], metavar="EXPRESSION",
                    help="expression JavaScript qui doit valoir true à l'état observé (répétable) : recoupe un texte calculé avec ses valeurs ; RETURN sinon")
    ap.add_argument("--in-frame", dest="in_frame", action="append", default=[], metavar="SÉLECTEUR[@CADRE]",
                    help="chaque élément visible du sélecteur doit avoir son centre dans le cadre (la fenêtre si @CADRE est omis), à l'état observé (répétable) ; RETURN sinon")
    ap.add_argument("--tab-stops", type=int, default=60, help="nombre maximal de tabulations observées")
    ap.add_argument("--allow-external", action="store_true", help="laisser passer les requêtes vers d'autres origines")
    ap.add_argument("--json", default="", help="écrit les résultats et la provenance dans ce fichier")
    ap.add_argument("--captures", default="", metavar="DOSSIER",
                    help="écrit une capture pleine page par largeur (capture-<largeur>px.png), à l'état observé ; n'écrase rien")
    ap.add_argument("--mesures", action="store_true",
                    help="relève des mesures de composition (titres, corps, familles, images, bords), sans seuil ni verdict : aucun statut, aucun code de sortie")
    ap.add_argument("--sans-gestes", dest="sans_gestes", action="store_true",
                    help="n'ajoute pas, sous les résultats, les gestes de SAVOIR/STATE liés aux signaux")
    ap.add_argument("--baseline", default="", metavar="JSON",
                    help="comparer à une mesure --json antérieure du même périmètre (défauts introduits, préexistants ou disparus)")
    ap.add_argument("--browser-executable", default=os.environ.get("DG_BROWSER_EXECUTABLE", ""), metavar="CHEMIN",
                    help="Chromium installé à utiliser explicitement (ou DG_BROWSER_EXECUTABLE) ; sinon navigateur Playwright")
    ap.add_argument("--serve-local", action="store_true", default=os.environ.get("DG_RENDER_SERVE_LOCAL") == "1",
                    help="servir le fichier et ses ressources sur 127.0.0.1 pour cette mesure (ou DG_RENDER_SERVE_LOCAL=1)")
    return ap


def main() -> int:
    return run(parser().parse_args())


if __name__ == "__main__":
    import journal_mobilisation  # journal passif : n'écrit rien sans DG_JOURNAL
    sys.exit(journal_mobilisation.executer("check_render", main, sys.argv[1:]))
