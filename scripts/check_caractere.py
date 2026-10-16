#!/usr/bin/env python3
"""Recette de caractère (à l'essai) : confronte le caractère déclaré d'un run au rendu HTML.

Elle émet des SIGNAL et des RELEVÉ, jamais PASS ni RETURN : un signal attend une réponse dans la
trace (corrigé, ou gardé avec sa raison) ; un relevé informe sans rien demander. Elle ne juge ni la
qualité d'une direction, ni le goût, ni l'usage. Méthode, déclaration et limites : ACTION/RECETTE-CARACTERE.

Usage : python3 scripts/check_caractere.py page.html declaration.json [--json SORTIE]
Requiert Playwright avec Chromium, numpy et Pillow ; sans eux, la recette rend NOT-VERIFIED (code 2).
"""
from __future__ import annotations

import argparse
import io
import json
import math
import sys
from pathlib import Path

# Bornes provisoires, réglées sur cinq pages d'essai et trois runs [À CALIBRER]. Figées entre deux recalibrations :
# un run ne les retouche pas ; recalibration par lot, sur au moins cinq runs qui n'ont pas servi à les régler.
BORNES = {"comp_void": .45, "resp_void": .60,
          "retenue_max": 40, "intensite_min": 10, "capture_min": .8, "focus_concentre": .65,
          "bande_vide_vh": .15, "marge_matiere": 1.25}
MATIERES = {"plan": "aplats", "image": "image", "typographie": "texte"}

COLLECTE = r"""(proof) => { const vw=innerWidth, vh=innerHeight, C=8, cw=Math.ceil(vw/C), ch=Math.ceil(vh/C);
 const g=()=>new Uint8Array(cw*ch), T=g(), I=g(), F=g(); let n=0;
 const mark=(G,r)=>{ for(let y=Math.max(0,Math.floor(r.top/C)); y<Math.min(ch,Math.ceil(r.bottom/C)); y++) for(let x=Math.max(0,Math.floor(r.left/C)); x<Math.min(cw,Math.ceil(r.right/C)); x++) G[y*cw+x]=1; };
 const fond=getComputedStyle(document.body).backgroundColor, vide=/rgba\(0, 0, 0, 0\)|transparent/;
 for (const el of document.body.querySelectorAll('*')) { const s=getComputedStyle(el); if (s.display==='none'||s.visibility==='hidden'||+s.opacity===0) continue;
  const r=el.getBoundingClientRect(); if (r.width<1||r.height<1||r.bottom<0||r.top>vh) continue;
  const own=[...el.childNodes].filter(x=>x.nodeType===3).map(x=>x.textContent).join('').trim();
  if (own) { el.setAttribute('data-cdir', n++); const rg=document.createRange(); rg.selectNodeContents(el); for (const q of rg.getClientRects()) mark(T,q); }
  if (['IMG','SVG','VIDEO','CANVAS'].includes(el.tagName.toUpperCase()) || (el.getAttribute('role')==='img' && !el.textContent.trim()) || (s.backgroundImage!=='none' && !/data:image\/svg/.test(s.backgroundImage))) mark(I,r);
  else if (!vide.test(s.backgroundColor) && s.backgroundColor!==fond) mark(F,r); }
 const part=G=>G.reduce((a,b)=>a+b,0)/(cw*ch);
 let p=null; if (proof) { const e=document.querySelector(proof); if (e) { const r=e.getBoundingClientRect(); p={x:Math.max(0,r.left),y:Math.max(0,r.top),x2:Math.min(vw,r.right),y2:Math.min(vh,r.bottom)}; } }
 return {texte: part(T), image: part(I), aplats: part(F), proof: p}; }"""


def mesures(png: bytes, dom: dict):
    import numpy as np
    from PIL import Image
    im = Image.open(io.BytesIO(png)).convert("RGB")
    rgb = np.asarray(im, float); g = np.asarray(im.convert("L"), float); h, w = g.shape
    gy, gx = np.gradient(g); densite = float((np.hypot(gx, gy) > 40).mean())
    c = 16; cells = g[: h // c * c, : w // c * c].reshape(h // c, c, w // c, c).std(axis=(1, 3)) < 4
    vide = float(cells.mean()); lignes = cells.all(axis=1); pleines = np.where(~lignes)[0]
    bande = meilleure = 0
    for r in (lignes[pleines[0]:pleines[-1] + 1] if len(pleines) else []):
        bande = bande + 1 if r else 0; meilleure = max(meilleure, bande)
    # saillance par résidu spectral (Hou et Zhang, 2007)
    sw = 64; sh = max(1, int(sw * h / w))
    small = np.asarray(im.convert("L").resize((sw, sh)), float)
    F = np.fft.fft2(small); logA = np.log(np.abs(F) + 1e-9)
    k = np.ones((3, 3)) / 9; pad = np.pad(logA, 1, mode="edge")
    moy = sum(pad[i:i + sh, j:j + sw] * k[i, j] for i in range(3) for j in range(3))
    sal = np.abs(np.fft.ifft2(np.exp(logA - moy + 1j * np.angle(F)))) ** 2
    sal = np.asarray(Image.fromarray(sal.astype("float32")).resize((w, h)), float); sal /= sal.sum() + 1e-12
    top10 = float(np.sort(sal.ravel())[::-1][: sal.size // 10].sum())
    capture = surface = None
    if dom.get("proof"):
        p = dom["proof"]; y0, y1, x0, x1 = int(p["y"]), int(p["y2"]), int(p["x"]), int(p["x2"])
        capture = float(sal[y0:y1, x0:x1].sum()); surface = max(0, x1 - x0) * max(0, y1 - y0) / (w * h)
    R, G, B = rgb[..., 0], rgb[..., 1], rgb[..., 2]; rg, yb = R - G, .5 * (R + G) - B
    colorful = math.hypot(rg.std(), yb.std()) + .3 * math.hypot(rg.mean(), yb.mean())
    return {"densite": round(densite, 3), "vide": round(vide, 2), "bande_vide_px": int(meilleure * c), "hauteur": h,
            "saillance_top10": round(top10, 2), "capture_preuve": None if capture is None else round(capture, 2),
            "surface_preuve": None if surface is None else round(surface, 2), "colorfulness": round(colorful, 1),
            "texte": round(dom["texte"], 2), "image": round(dom["image"], 2), "aplats": round(dom["aplats"], 2)}


def evaluer(m: dict, d: dict, polices_hors: dict | None = None) -> list[dict]:
    """SIGNAL pour les indicateurs qui ont changé des décisions ; RELEVÉ pour les autres (à l'essai)."""
    out, B = [], BORNES
    def add(kind, ctrl, detail, route): out.append({"statut": kind, "controle": ctrl, "detail": detail, "savoir": route})
    if polices_hors:
        tot = sum(polices_hors.values())
        add("SIGNAL", "Polices rendues", f"glyphes hors des polices déclarées : " + ", ".join(f"{k} ({v})" for k, v in polices_hors.items()) + f", {tot} au total", "SAVOIR/TYPE")
    # la densité se lit sur la part de vide ; la densité de bords varie trop avec la police (relevé seulement)
    if d.get("density") == "respiration" and m["vide"] <= B["comp_void"]:
        add("SIGNAL", "Densité", f"respiration déclarée ; rendu compressé (vide {m['vide']}, bords {m['densite']})", "BIBLIOTHEQUE/TENSION ; SAVOIR/CRAFT/CFT-03")
    if d.get("density") == "compression" and m["vide"] >= B["resp_void"]:
        add("SIGNAL", "Densité", f"compression déclarée ; rendu aéré (vide {m['vide']}, bords {m['densite']})", "BIBLIOTHEQUE/TENSION ; SAVOIR/CRAFT/CFT-03")
    if d.get("material") in MATIERES:
        parts = {k: m[v] for k, v in MATIERES.items()}; top = max(parts, key=parts.get)
        if top != d["material"] and parts[top] > B["marge_matiere"] * parts[d["material"]]:
            add("SIGNAL", "Matière dominante", f"{d['material']} déclarée ; rendu dominé par {top} (" + ", ".join(f"{k} {v:.0%}" for k, v in parts.items()) + ")", "DIRECTION/VISUAL_TARGET (matière)")
    if d.get("focus") == "unique" and m["capture_preuve"] is not None and m["surface_preuve"]:
        if m["capture_preuve"] < m["surface_preuve"] * B["capture_min"]:
            add("RELEVÉ", "Foyer", f"l'objet de preuve capte {m['capture_preuve']:.0%} de la saillance pour {m['surface_preuve']:.0%} de la surface", "SAVOIR/FRAME/COMPOSITION")
    if d.get("focus") == "distribué" and m["saillance_top10"] >= B["focus_concentre"]:
        add("RELEVÉ", "Foyer", f"foyer distribué déclaré ; regard concentré ({m['saillance_top10']:.2f} de la saillance sur 10 % des pixels)", "BIBLIOTHEQUE/TENSION")
    if d.get("intensity") == "retenue" and m["colorfulness"] > B["retenue_max"] or d.get("intensity") == "intensité" and m["colorfulness"] < B["intensite_min"]:
        add("RELEVÉ", "Intensité", f"{d['intensity']} déclarée ; colorfulness {m['colorfulness']}", "SAVOIR/CRAFT/CFT-05")
    if not d.get("intended_voids") and m["bande_vide_px"] >= B["bande_vide_vh"] * m["hauteur"]:
        add("RELEVÉ", "Vide", f"bande vide de {m['bande_vide_px']} px entre deux contenus, non déclarée", "SAVOIR/FRAME/COMPOSITION")
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description="Recette de caractère (à l'essai) : caractère déclaré face au rendu.")
    ap.add_argument("page"); ap.add_argument("declaration"); ap.add_argument("--json")
    a = ap.parse_args()
    d = json.loads(Path(a.declaration).read_text(encoding="utf-8"))
    try:
        import numpy  # noqa: F401
        from PIL import Image  # noqa: F401
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        print(f"NOT-VERIFIED — dépendance absente ({exc.name}) : numpy, Pillow et Playwright sont requis."); return 2
    url, polices = Path(a.page).resolve().as_uri(), [f.lower() for f in d.get("fonts", [])]
    resultats = []
    try:
        with sync_playwright() as p:
            b = p.chromium.launch()
            for w in d.get("widths", [390, 1440]):
                for st in d.get("states", [""]):
                    pg = b.new_page(viewport={"width": w, "height": 844 if w < 900 else 900})
                    pg.goto(url + st); pg.wait_for_timeout(600)
                    dom = pg.evaluate(COLLECTE, d.get("proof")); png = pg.screenshot()
                    hors = {}
                    if polices:
                        cdp = pg.context.new_cdp_session(pg); cdp.send("DOM.enable"); cdp.send("CSS.enable")
                        root = cdp.send("DOM.getDocument", {"depth": -1})["root"]["nodeId"]
                        for nid in cdp.send("DOM.querySelectorAll", {"nodeId": root, "selector": "[data-cdir]"})["nodeIds"]:
                            for f in cdp.send("CSS.getPlatformFontsForNode", {"nodeId": nid})["fonts"]:
                                if not any(f["familyName"].lower().startswith(x) for x in polices):
                                    hors[f["familyName"]] = hors.get(f["familyName"], 0) + f["glyphCount"]
                    m = mesures(png, dom)
                    for s in evaluer(m, d, hors):
                        s["ou"] = f"{w}px{(' ' + st) if st else ''}"; resultats.append(s)
                    resultats.append({"statut": "MESURES", "ou": f"{w}px{(' ' + st) if st else ''}", "mesures": m})
                    pg.close()
            b.close()
    except Exception as exc:  # navigateur indisponible : jamais simulé
        print(f"NOT-VERIFIED — navigateur indisponible ({exc.__class__.__name__})."); return 2
    for r in resultats:
        if r["statut"] != "MESURES":
            print(f"[{r['statut']}] {r['ou']} · {r['controle']} · {r['detail']} · savoir : {r['savoir']}")
    n = sum(r["statut"] == "SIGNAL" for r in resultats)
    print(f"{n} signal(aux) à traiter dans la trace. Bornes provisoires [À CALIBRER] ; ni verdict de goût, ni preuve de qualité.")
    if a.json:
        Path(a.json).write_text(json.dumps(resultats, ensure_ascii=False, indent=2), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
