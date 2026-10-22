#!/usr/bin/env python3
"""Vignettes de direction, à l'essai : deux ou trois positions comparées sur capture avant d'en finir une.

Méthode : `ACTION/PIPELINE-DIRECTION`, « Vignettes ». Quand une alternative située se matérialise au niveau du
rendu, chaque position est un premier écran brut, sans finition. Ce script les capture au premier écran, à la
largeur d'un téléphone et d'un bureau, et les pose côte à côte dans une page, pour lire d'abord à faible détail
(silhouette, foyer, rapport texte/image), puis à taille réelle. Il ne choisit rien et ne note rien.

Usage :
  python3 scripts/vignettes.py a.html b.html [c.html] --sortie vignettes/ [--nom "Coupe" --nom "Gravure" ...]
Requiert Playwright avec Chromium ; sans navigateur, NOT-VERIFIED (code 2), rien n'est écrit.
"""
from __future__ import annotations

import argparse
import html
import os
import sys
from pathlib import Path

LARGEURS = ((390, 844), (1440, 900))
FLOU = 6  # px : la lecture à faible détail se fait sur l'image floutée, à côté de l'image nette


def page(positions: list[tuple[str, str]], captures: dict[tuple[int, int], str]) -> str:
    """Page de comparaison : une rangée par largeur, une colonne par position ; textes échappés."""
    e = html.escape
    rangs = []
    for w, _ in LARGEURS:
        cellules = "".join(
            f'<figure><figcaption>{e(nom)}</figcaption>'
            f'<img class="flou" src="{e(captures[(i, w)])}" alt="{e(nom)}, premier écran à {w} px, flouté">'
            f'<img src="{e(captures[(i, w)])}" alt="{e(nom)}, premier écran à {w} px"></figure>'
            for i, (nom, _) in enumerate(positions))
        rangs.append(f'<section><h2>{w} px</h2><div class="rang w{w}">{cellules}</div></section>')
    return ("<!doctype html><html lang=\"fr\"><head><meta charset=\"utf-8\"><meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">"
            "<title>Vignettes de direction</title><style>"
            "body{margin:0;background:#f4f4f2;color:#1b1b1b;font:15px/1.5 system-ui,sans-serif}"
            "main{padding:24px 16px 48px;max-width:1600px;margin:0 auto}h1{font-size:22px;margin:0 0 4px}"
            "p{margin:0 0 20px;color:#555;max-width:70ch}h2{font-size:15px;margin:24px 0 8px}"
            ".rang{display:grid;grid-auto-flow:column;grid-auto-columns:minmax(0,1fr);gap:16px;overflow-x:auto}"
            "figure{margin:0;display:grid;gap:6px;align-content:start}figcaption{font-weight:600}"
            f"img{{display:block;width:100%;height:auto;border:1px solid #d8d8d4}}.flou{{filter:blur({FLOU}px)}}"
            ".w390 figure{max-width:300px}"
            "</style></head><body><main><h1>Vignettes de direction</h1>"
            "<p>Lire d’abord les images floutées : quelle position a une silhouette, un foyer et un rapport texte/image "
            "propres au sujet ? Puis les images nettes, à taille réelle. Garder une position, nommer la raison dans la trace, "
            "ne pas finir les autres.</p>"
            + "".join(rangs) + "</main></body></html>")


def capturer(positions: list[tuple[str, str]], sortie: Path) -> dict[tuple[int, int], str]:
    from playwright.sync_api import sync_playwright
    exe = os.environ.get("DG_BROWSER_EXECUTABLE", "")
    noms: dict[tuple[int, int], str] = {}
    with sync_playwright() as p:
        b = p.chromium.launch(**({"executable_path": exe} if exe else {}))
        for i, (_, chemin) in enumerate(positions):
            for w, h in LARGEURS:
                pg = b.new_page(viewport={"width": w, "height": h})
                pg.goto(Path(chemin).resolve().as_uri()); pg.wait_for_timeout(700)
                nom = f"position-{i + 1}-{w}px.png"
                pg.screenshot(path=str(sortie / nom))  # premier écran seulement
                noms[(i, w)] = nom
                pg.close()
        b.close()
    return noms


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Vignettes de direction (à l'essai) : deux ou trois positions comparées sur capture.")
    ap.add_argument("pages", nargs="+", help="deux ou trois pages HTML, une par position")
    ap.add_argument("--sortie", required=True, help="dossier de la comparaison (vignettes.html et captures)")
    ap.add_argument("--nom", action="append", default=[], help="nom court de chaque position, dans l'ordre (répétable)")
    a = ap.parse_args(argv)
    if not 2 <= len(a.pages) <= 3:
        ap.error("deux ou trois positions : la comparaison est l'objet des vignettes, pas un catalogue")
    for chemin in a.pages:
        if not Path(chemin).is_file():
            ap.error(f"page introuvable : {chemin}")
    if a.nom and len(a.nom) != len(a.pages):
        ap.error("un nom par page, ou aucun")
    positions = [(a.nom[i] if a.nom else f"Position {i + 1}", c) for i, c in enumerate(a.pages)]
    sortie = Path(a.sortie); sortie.mkdir(parents=True, exist_ok=True)
    try:
        captures = capturer(positions, sortie)
    except ImportError:
        print("NOT-VERIFIED — Playwright absent : vignettes non écrites."); return 2
    except Exception as exc:  # navigateur indisponible : jamais simulé
        print(f"NOT-VERIFIED — navigateur indisponible ({exc.__class__.__name__}) : vignettes non écrites."); return 2
    cible = sortie / "vignettes.html"
    cible.write_text(page(positions, captures), encoding="utf-8")
    print(f"VIGNETTES — {len(positions)} positions : {cible}")
    print("Lire d’abord à faible détail (silhouette, foyer, rapport texte/image), puis à taille réelle ; garder une position "
          "et nommer la raison dans la trace (`ACTION/PIPELINE-DIRECTION`). Ne prouve ni l’usage ni la qualité.")
    return 0


if __name__ == "__main__":
    import journal_mobilisation  # journal passif : n'écrit rien sans DG_JOURNAL
    sys.exit(journal_mobilisation.executer("vignettes", main, sys.argv[1:]))
