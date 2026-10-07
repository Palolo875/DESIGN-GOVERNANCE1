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
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit

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
  const hidden = e => { for (let n = e; n && n.nodeType === 1; n = n.parentElement) {
    const s = getComputedStyle(n);
    if (n.getAttribute('aria-hidden') === 'true' || n.hasAttribute('hidden') || s.display === 'none' ||
        s.visibility === 'hidden' || s.visibility === 'collapse') return true;
  } return false; };
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
    if (['SVG', 'CANVAS'].includes(n.tagName.toUpperCase())) uncertain = true;
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
    const cs = getComputedStyle(el), fg = color(cs.color);
    if (!fg) { if (!seenUk.has(k)) { seenUk.add(k); res.unknown.push({sel: k, value: cs.color}); } continue; }
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


def sha12(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()[:12]


def measure(args: argparse.Namespace) -> dict:
    """Ouvre la page dans Chromium et retourne les mesures brutes. Lève ImportError si Playwright manque."""
    from playwright.sync_api import Error as PlaywrightError, sync_playwright  # import optionnel
    target = args.page
    is_url = re.match(r"^https?://", target) is not None
    url = target if is_url else Path(target).resolve().as_uri()
    origin = None
    if is_url:
        sp = urlsplit(target)
        origin = f"{sp.scheme}://{sp.netloc}"
    widths = [int(w) for w in args.widths.split(",") if w.strip()]
    state = {"blocked": 0}
    raw: dict = {"widths": widths, "per_width": {}, "running": []}
    with sync_playwright() as pw:
        try:
            browser = pw.chromium.launch()
        except PlaywrightError as exc:
            raise BrowserUnavailable(str(exc).splitlines()[0][:160]) from exc

        def open_page(width: int, reduced: bool = False):
            ctx = browser.new_context(viewport={"width": width, "height": 844 if width < 700 else 900},
                                      reduced_motion="reduce" if reduced else "no-preference")
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
            for sel in args.click:
                page.click(sel)
                page.wait_for_timeout(300)
            return ctx, page, errs

        for w in widths:
            ctx, page, errs = open_page(w)
            dims = page.evaluate("({sw: document.documentElement.scrollWidth, cw: document.documentElement.clientWidth})")
            offenders = page.evaluate("""() => [...document.querySelectorAll('body *')].filter(e => {
                const r = e.getBoundingClientRect(); return r.right > document.documentElement.clientWidth + 1 && getComputedStyle(e).position !== 'fixed'; })
                .slice(0, 4).map(e => e.tagName.toLowerCase() + (e.className && e.className.baseVal === undefined ? '.' + String(e.className).split(' ')[0] : ''))""")
            audit = page.evaluate(AUDIT_JS, FOC)
            proof = None
            if args.proof:
                page.evaluate("window.scrollTo(0, 0)")
                proof = page.evaluate(PROOF_JS, args.proof)
            keyboard = page.evaluate(BASELINE_JS, FOC)
            stops: list[str] = []
            missing: list[str] = []
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
            keyboard.update(reason=reason, tab_limit=args.tab_stops, visited=sorted(visited),
                            unreached=[e['id'] for e in keyboard['expected'] if e['key'] not in visited], unexpected=unexpected)
            raw["per_width"][w] = {"overflow": dims, "offenders": offenders, "errs": errs, "audit": audit, "proof": proof,
                                   "stops": stops, "missing_ind": missing, "keyboard": keyboard}
            ctx.close()

        ctx, page, _ = open_page(widths[0], reduced=True)
        raw["running"] = page.evaluate("""() => document.getAnimations().filter(a => a.playState === 'running').map(a => ({
            name: a.animationName || a.transitionProperty || 'anim', infinite: a.effect.getComputedTiming().iterations === Infinity}))""")
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
        limits.append("fond en dégradé ou en image, non évalué : " + ", ".join(nonsolid[:5]) + (f" +{len(nonsolid)-5}" if len(nonsolid) > 5 else ""))
    if svg_text:
        limits.append("texte SVG non évalué (" + ", ".join(svg_text[:3]) + ") : relever fill/stroke, opacités et fond réel, "
                      "puis calculer le contraste ; méthode dans ACTION/GATE-A")
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
                   ' ; '.join(keyboard_details + keyboard_limits) + ' ; style observé, visibilité et contraste du focus à vérifier'))

    running = raw.get("running", [])
    inf = [a for a in running if a["infinite"]]
    checks.append(("Mouvement réduit respecté", RETURN if inf else (RESERVE if running else PASS),
                   (f"animation infinie encore active : {', '.join(a['name'] for a in inf)}" if inf else
                    f"{len(running)} animation(s) finie(s) encore active(s)" if running else "aucune animation active")))

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


def run(args: argparse.Namespace) -> int:
    target = args.page
    is_url = re.match(r"^https?://", target) is not None
    path = None if is_url else Path(target)
    if path is not None and not path.is_file():
        print(f"{NOTVER} : fichier introuvable : {target}", file=sys.stderr)
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
            "scope": f"état initial{' puis ' + ' puis '.join(args.click) if args.click else ''}, largeurs {','.join(map(str, raw['widths']))} px",
            "external_requests_blocked": raw["blocked"]}
    print(f"Recette AUTOMATED (GATE-A) — {target}\n")
    for title, status, detail in checks:
        print(f"[{status:<21}] {title} : {detail}")
    print("\nProvenance : " + " · ".join(f"{k}={v}" for k, v in prov.items()))
    print("Limites : seules les fautes objectivables sont contrôlées, à l'état et aux largeurs observés. "
          f"{raw['blocked']} requête(s) externe(s) bloquée(s) : les mesures utilisent alors les polices de repli. "
          "Les fonds en dégradé ou en image, les opacités de groupe, le texte SVG, le texte natif des contrôles et des pseudo-éléments ne sont pas évalués ; leur présence détectée conserve une réserve. "
          "La couverture du contraste est bornée au DOM inspecté. L'objet de preuve mesure CSS et rectangle, sans vérifier les pixels ni l'occlusion. "
          "Les noms sont des candidats DOM, pas un calcul AccName ; leur présence conserve une réserve. "
          "Le clavier porte sur les candidats du périmètre actif et les arrêts observés ; une borne atteinte conserve une réserve. "
          "Cette recette ne valide ni la direction visuelle, ni l'utilisabilité, ni un verdict global.")
    if args.json:
        coverage = {str(w): {**d.get('keyboard', {}), 'observed_stops': len(d['stops'])} for w, d in raw['per_width'].items()}
        Path(args.json).write_text(json.dumps({"provenance": prov, "checks": [{"check": t, "status": s, "detail": d} for t, s, d in checks],
                                              'keyboard_coverage': coverage,
                                              'contrast_coverage': {str(w): d['audit'].get('contrastCoverage', {}) for w, d in raw['per_width'].items()},
                                              'proof_observations': {str(w): d['proof'] for w, d in raw['per_width'].items()}},
                                              ensure_ascii=False, indent=2), encoding="utf-8")
    return 1 if any(s == RETURN for _, s, _ in checks) else 0


def parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(description="Recette AUTOMATED optionnelle d'un rendu HTML (ACTION/GATE-A).")
    ap.add_argument("page", help="chemin d'un fichier HTML ou URL")
    ap.add_argument("--widths", default="390,768,1440", help="largeurs en px, séparées par des virgules")
    ap.add_argument("--proof", default="", help="sélecteur CSS de l'objet de preuve déclaré par l'auteur")
    ap.add_argument("--click", action="append", default=[], help="sélecteur à cliquer avant la mesure (répétable)")
    ap.add_argument("--wait-ms", type=int, default=1500, help="attente après chargement (animations d'entrée)")
    ap.add_argument("--tab-stops", type=int, default=60, help="nombre maximal de tabulations observées")
    ap.add_argument("--allow-external", action="store_true", help="laisser passer les requêtes vers d'autres origines")
    ap.add_argument("--json", default="", help="écrit les résultats et la provenance dans ce fichier")
    return ap


def main() -> int:
    return run(parser().parse_args())


if __name__ == "__main__":
    sys.exit(main())
