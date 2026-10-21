#!/usr/bin/env python3
"""Registre des choix, à l'essai : rend visible, d'un run à l'autre, la convergence des polices et des palettes.

La question de convergence (`SAVOIR/CRAFT/CFT-05`) demande si une police ou une palette est celle que le modèle
produirait sans brief. Dans un seul run, la réponse dépend de la mémoire de l'agent ; ce registre la rend
factuelle. Pour une page, il relève sur le rendu (mesures de `check_render.py --mesures`, à 1440 px) la police du
titre, les familles employées, le nom interne des fichiers de police réellement rendus pour le titre et le corps
(un nom de famille local peut cacher un fichier déjà vu), le fond et la première couleur chromatique ; il les compare aux entrées
précédentes du registre, puis ajoute l'entrée.

Le registre est un fichier JSONL local, choisi par la personne (`--registre`, ou la variable `DG_REGISTRE`) :
rien n'est écrit sans lui, et rien ne quitte la machine. Une répétition n'est pas un défaut : elle appelle la
question de convergence, à laquelle un choix justifié répond (`SAVOIR/TOOLS/CONVERGENCE`). Aucun statut, aucun seuil.

Usage :
  python3 scripts/registre_choix.py page.html --registre choix.jsonl [--etiquette "brief 2"]
  python3 scripts/registre_choix.py --registre choix.jsonl --lire        (synthèse du registre)
Requiert Playwright avec Chromium ; sans navigateur, NOT-VERIFIED (code 2), rien n'est écrit.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

LARGEUR = 1440


def famille_fond(fond: dict | None) -> str:
    """Catégorie de fond, pour comparer des runs : sombre, crème ou beige, clair neutre, clair teinté, coloré."""
    if not fond:
        return "non évalué (image ou dégradé)"
    L, C, H = fond.get("L", 0), fond.get("C", 0), fond.get("H") or 0
    if L < 0.3:
        return "sombre"
    if L >= 0.88 and C < 0.006:
        return "clair neutre"
    if L >= 0.88 and C < 0.05 and 55 <= H <= 105:
        return "crème ou beige"
    if L >= 0.88:
        return "clair teinté"
    return "coloré"


def teinte(h: float | None) -> str | None:
    """Teinte arrondie par secteur de 30°, pour comparer des accents."""
    if h is None:
        return None
    noms = ["rouge", "orange", "jaune-orange", "jaune", "vert-jaune", "vert", "vert-bleu", "cyan", "bleu", "bleu-violet",
            "violet", "magenta"]
    return noms[int(((h + 15) % 360) // 30)]


def entree(mesures: dict, page: str, etiquette: str = "") -> dict:
    """Entrée du registre tirée des mesures de check_render (une largeur)."""
    titre = mesures.get("titre") or {}
    palette = mesures.get("palette") or {}
    fond = palette.get("fond")
    chroma = (palette.get("chromatiques") or [None])[0]
    return {"horodatage": datetime.now(timezone.utc).isoformat(timespec="seconds"), "page": page, "etiquette": etiquette,
            "police_titre": titre.get("famille"), "familles": mesures.get("familles", []),
            "rendue_titre": (mesures.get("rendues") or {}).get("titre"), "rendue_corps": (mesures.get("rendues") or {}).get("corps"),
            "fond": fond.get("hex") if fond else None, "famille_fond": famille_fond(fond),
            "accent": chroma.get("hex") if chroma else None, "teinte_accent": teinte(chroma.get("H")) if chroma else None}


def comparer(nouvelle: dict, anciennes: list[dict]) -> list[str]:
    """Lignes de convergence : ce que la nouvelle entrée partage avec les précédentes (autres pages)."""
    autres = [e for e in anciennes if e.get("page") != nouvelle.get("page")]
    n = len(autres)
    if not n:
        return ["Premier choix du registre pour une autre page : rien à comparer."]
    lignes = []
    def part(cle, valeur, libelle):
        if valeur:
            k = sum(1 for e in autres if e.get(cle) == valeur)
            if k:
                lignes.append(f"{libelle} « {valeur} » : déjà dans {k} des {n} entrée(s) précédente(s).")
    part("police_titre", nouvelle.get("police_titre"), "Police du titre")
    for f in nouvelle.get("familles", []):
        if f != nouvelle.get("police_titre"):
            k = sum(1 for e in autres if f in e.get("familles", []))
            if k:
                lignes.append(f"Famille « {f} » : déjà employée dans {k} des {n} entrée(s) précédente(s).")
    for role, libelle in (("rendue_titre", "Fichier de police du titre"), ("rendue_corps", "Fichier de police du corps")):
        valeur = nouvelle.get(role)
        if valeur:
            k = sum(1 for e in autres if valeur in (e.get("rendue_titre"), e.get("rendue_corps")))
            if k:
                lignes.append(f"{libelle} « {valeur} » (nom interne, rendu) : déjà dans {k} des {n} entrée(s) précédente(s).")
    part("famille_fond", nouvelle.get("famille_fond"), "Fond")
    part("teinte_accent", nouvelle.get("teinte_accent"), "Accent de teinte")
    return lignes or [f"Aucun choix relevé n’est partagé avec les {n} entrée(s) précédente(s)."]


def synthese(entrees: list[dict]) -> list[str]:
    """Fréquences du registre : polices de titre, familles, fonds et accents."""
    if not entrees:
        return ["Registre vide."]
    lignes = [f"REGISTRE — {len(entrees)} entrée(s), {len({e.get('page') for e in entrees})} page(s)"]
    for libelle, cle in (("Polices de titre", "police_titre"), ("Fonds", "famille_fond"), ("Accents", "teinte_accent")):
        c = Counter(e.get(cle) for e in entrees if e.get(cle))
        lignes.append(f"{libelle} : " + (", ".join(f"{k} ×{v}" for k, v in c.most_common(6)) or "aucun relevé"))
    c = Counter(f for e in entrees for f in set(e.get("familles", [])))
    lignes.append("Familles déclarées : " + (", ".join(f"{k} ×{v}" for k, v in c.most_common(8)) or "aucune relevée"))
    c = Counter(f for e in entrees for f in {e.get("rendue_titre"), e.get("rendue_corps")} if f)
    lignes.append("Fichiers de police rendus (titre ou corps) : " + (", ".join(f"{k} ×{v}" for k, v in c.most_common(8)) or "aucun relevé"))
    return lignes


def lire(chemin: Path) -> list[dict]:
    if not chemin.is_file():
        return []
    out = []
    for ligne in chemin.read_text(encoding="utf-8").splitlines():
        if ligne.strip():
            try:
                out.append(json.loads(ligne))
            except json.JSONDecodeError:
                print("ligne du registre illisible, ignorée", file=sys.stderr)
    return out


def polices_rendues(page: str) -> dict[str, str | None]:
    """Police réellement utilisée par le navigateur (nom interne du fichier) pour le titre et le corps :
    un nom de famille local (« Halle Texte ») peut cacher un fichier déjà vu ailleurs."""
    from playwright.sync_api import sync_playwright
    exe = os.environ.get("DG_BROWSER_EXECUTABLE", "")
    out: dict[str, str | None] = {"titre": None, "corps": None}
    with sync_playwright() as p:
        b = p.chromium.launch(**({"executable_path": exe} if exe else {}))
        pg = b.new_page(viewport={"width": LARGEUR, "height": 900})
        pg.goto(Path(page).resolve().as_uri()); pg.wait_for_timeout(600)
        pg.evaluate("""() => { const vis = e => { const r = e.getBoundingClientRect(); return r.width > 0 && r.height > 0; };
          const h = [...document.querySelectorAll('h1,h2')].find(vis); if (h) h.setAttribute('data-registre', 'titre');
          const c = [...document.querySelectorAll('p,li,dd,td')].find(e => vis(e) && e.textContent.trim().length >= 40);
          if (c) c.setAttribute('data-registre', 'corps'); }""")
        cdp = pg.context.new_cdp_session(pg); cdp.send("DOM.enable"); cdp.send("CSS.enable")
        root = cdp.send("DOM.getDocument", {"depth": -1})["root"]["nodeId"]
        for role in out:
            ids = cdp.send("DOM.querySelectorAll", {"nodeId": root, "selector": f"[data-registre={role}]"})["nodeIds"]
            if ids:
                fonts = cdp.send("CSS.getPlatformFontsForNode", {"nodeId": ids[0]})["fonts"]
                if fonts:
                    out[role] = max(fonts, key=lambda f: f["glyphCount"])["familyName"]
        b.close()
    return out


def mesurer(page: str) -> dict:
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import check_render as cr
    args = cr.parser().parse_args([page, "--widths", str(LARGEUR), "--mesures", "--wait-ms", "600"])
    raw = cr.measure(args)
    mesures = raw["per_width"][LARGEUR]["mesures"]
    mesures["rendues"] = polices_rendues(page)
    return mesures


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Registre des choix (à l'essai) : convergence des polices et des palettes d'un run à l'autre.")
    ap.add_argument("page", nargs="?", help="page HTML dont on relève les choix")
    ap.add_argument("--registre", default=os.environ.get("DG_REGISTRE", ""), help="fichier JSONL du registre (ou DG_REGISTRE)")
    ap.add_argument("--etiquette", default="", help="libellé libre de l'entrée (brief, projet, condition)")
    ap.add_argument("--lire", action="store_true", help="affiche la synthèse du registre, sans mesurer")
    a = ap.parse_args(argv)
    if not a.registre:
        ap.error("registre requis : --registre FICHIER ou variable DG_REGISTRE ; rien n'est écrit sans lui")
    chemin = Path(a.registre)
    if a.lire:
        print("\n".join(synthese(lire(chemin))))
        return 0
    if not a.page or not Path(a.page).is_file():
        ap.error("page HTML introuvable")
    try:
        mesures = mesurer(a.page)
    except ImportError:
        print("NOT-VERIFIED — Playwright absent : aucun choix relevé, rien n'est écrit.")
        return 2
    except Exception as exc:  # navigateur indisponible : jamais simulé
        print(f"NOT-VERIFIED — navigateur indisponible ({exc.__class__.__name__}) : rien n'est écrit.")
        return 2
    nouvelle = entree(mesures, str(Path(a.page).resolve()), a.etiquette)
    print(f"CHOIX RELEVÉS ({LARGEUR} px) — titre : {nouvelle['police_titre'] or 'non relevé'}"
          f" (rendu : {nouvelle['rendue_titre'] or '—'}) ; corps rendu : {nouvelle['rendue_corps'] or '—'} ; familles : "
          f"{', '.join(nouvelle['familles']) or 'non relevées'} ; fond : {nouvelle['fond'] or '—'} ({nouvelle['famille_fond']}) ; "
          f"accent : {nouvelle['accent'] or 'aucun'}{' (' + nouvelle['teinte_accent'] + ')' if nouvelle['teinte_accent'] else ''}")
    print("CONVERGENCE — " + "\n            ".join(comparer(nouvelle, lire(chemin))))
    print("Une répétition n’est pas un défaut : elle appelle la question de convergence (SAVOIR/CRAFT/CFT-05) ; "
          "un choix justifié par le produit reste valide. Familles relevées sur le rendu : une police bloquée ou absente apparaît sous son repli.")
    chemin.parent.mkdir(parents=True, exist_ok=True)
    with chemin.open("a", encoding="utf-8") as f:
        f.write(json.dumps(nouvelle, ensure_ascii=False) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
