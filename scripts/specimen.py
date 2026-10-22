#!/usr/bin/env python3
"""Spécimen de voix, à l'essai : le vrai titre composé dans plusieurs polices, côte à côte, sur capture.

`SAVOIR/TYPE` et la question de convergence (`SAVOIR/CRAFT/CFT-05`) demandent de comparer au moins deux voix
typographiques sur le vrai titre avant de choisir. Ce script rend cette comparaison visible et peu coûteuse :
il compose le titre (et, si on le donne, une ligne de texte courant) dans chaque voix, à la largeur d'un
téléphone et d'un bureau, écrit une page et deux captures, et signale toute voix rendue par une police de repli.
Il ne choisit rien : la voix se juge sur ce qu'elle porte (ton, chiffres, langue, lisibilité, licence).

Usage :
  python3 scripts/specimen.py --titre "Fromagerie Brunet" --voix "Fraunces=polices/fraunces.woff2" \
      --voix "Georgia" --corps "Trois marchés, six produits du moment." --sortie specimen/
Une voix s'écrit « Nom » (police installée) ou « Nom=chemin » (fichier local, copié dans la sortie).
Requiert Playwright avec Chromium ; sans navigateur, la page est écrite et les captures restent NOT-VERIFIED.
"""
from __future__ import annotations

import argparse
import html
import os
import shutil
import sys
from pathlib import Path

LARGEURS = (390, 1440)


def lire_voix(specs: list[str]) -> list[tuple[str, str | None]]:
    """(nom, chemin ou None) pour chaque « Nom » ou « Nom=chemin »."""
    voix = []
    for spec in specs:
        nom, _, chemin = spec.partition("=")
        if not nom.strip():
            raise ValueError(f"voix sans nom : {spec!r}")
        voix.append((nom.strip(), chemin.strip() or None))
    return voix


def page(titre: str, voix: list[tuple[str, str | None]], corps: str = "", fichiers: dict[str, str] | None = None) -> str:
    """Page du spécimen : une rangée par voix, titre en grand, ligne de corps éventuelle, nom de la voix."""
    fichiers = fichiers or {}
    faces = "".join(f'@font-face{{font-family:"specimen-{i}";src:url("{html.escape(fichiers[n])}");font-display:block}}'
                     for i, (n, _) in enumerate(voix) if n in fichiers)
    rangs = []
    for i, (nom, _) in enumerate(voix):
        famille = f'"specimen-{i}"' if nom in fichiers else f'"{nom}"'
        rangs.append(f'<section class="voix" data-voix="{i}"><p class="nom">{html.escape(nom)}</p>'
                     f'<h2 style="font-family:{html.escape(famille)},serif">{html.escape(titre)}</h2>'
                     + (f'<p class="corps" style="font-family:{html.escape(famille)},serif">{html.escape(corps)}</p>' if corps else "")
                     + "</section>")
    return ("<!doctype html><html lang=\"fr\"><head><meta charset=\"utf-8\"><meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">"
            f"<title>Spécimen — {html.escape(titre)}</title><style>{faces}"
            "body{margin:0;background:#fff;color:#111;font:16px/1.5 system-ui,sans-serif}"
            ".voix{padding:28px clamp(16px,4vw,48px);border-bottom:1px solid #ddd}"
            ".nom{margin:0 0 8px;font-size:13px;color:#555}"
            "h2{margin:0;font-size:clamp(36px,7vw,88px);line-height:1.02;font-weight:inherit;text-wrap:balance}"
            ".corps{margin:12px 0 0;font-size:18px;max-width:60ch}</style></head><body>"
            + "".join(rangs) + "</body></html>")


def capturer(chemin: Path, sortie: Path, n: int) -> list[str]:
    """Captures pleine page et polices réellement rendues pour chaque titre ; lignes de compte rendu."""
    from playwright.sync_api import sync_playwright
    exe = os.environ.get("DG_BROWSER_EXECUTABLE", "")
    lignes = []
    with sync_playwright() as p:
        b = p.chromium.launch(**({"executable_path": exe} if exe else {}))
        for w in LARGEURS:
            pg = b.new_page(viewport={"width": w, "height": 900})
            pg.goto(chemin.resolve().as_uri()); pg.wait_for_timeout(500)
            pg.screenshot(path=str(sortie / f"specimen-{w}px.png"), full_page=True)
            if w == LARGEURS[-1]:
                cdp = pg.context.new_cdp_session(pg); cdp.send("DOM.enable"); cdp.send("CSS.enable")
                root = cdp.send("DOM.getDocument", {"depth": -1})["root"]["nodeId"]
                for i in range(n):
                    ids = cdp.send("DOM.querySelectorAll", {"nodeId": root, "selector": f'[data-voix="{i}"] h2'})["nodeIds"]
                    fonts = cdp.send("CSS.getPlatformFontsForNode", {"nodeId": ids[0]})["fonts"] if ids else []
                    lignes.append(", ".join(f["familyName"] for f in sorted(fonts, key=lambda f: -f["glyphCount"])) or "non relevée")
            pg.close()
        b.close()
    return lignes


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Spécimen de voix (à l'essai) : le vrai titre dans plusieurs polices, sur capture.")
    ap.add_argument("--titre", required=True, help="le vrai titre, tel qu'il sera publié")
    ap.add_argument("--voix", action="append", required=True, help="« Nom » ou « Nom=chemin/vers/police.woff2 » (au moins deux)")
    ap.add_argument("--corps", default="", help="une ligne de texte courant réel, facultative")
    ap.add_argument("--sortie", required=True, help="dossier où écrire specimen.html et les captures")
    a = ap.parse_args(argv)
    try:
        voix = lire_voix(a.voix)
    except ValueError as exc:
        ap.error(str(exc))
    if len(voix) < 2:
        ap.error("au moins deux voix : la comparaison est l'objet du spécimen")
    sortie = Path(a.sortie); sortie.mkdir(parents=True, exist_ok=True)
    fichiers = {}
    for nom, chemin in voix:
        if chemin:
            src = Path(chemin)
            if not src.is_file():
                ap.error(f"fichier de police introuvable : {chemin}")
            dest = sortie / src.name
            if src.resolve() != dest.resolve():
                shutil.copyfile(src, dest)
            fichiers[nom] = src.name
    cible = sortie / "specimen.html"
    cible.write_text(page(a.titre, voix, a.corps, fichiers), encoding="utf-8")
    print(f"SPÉCIMEN — {len(voix)} voix sur « {a.titre} » : {cible}")
    try:
        rendues = capturer(cible, sortie, len(voix))
    except ImportError:
        print("NOT-VERIFIED — Playwright absent : page écrite, captures non produites.")
        return 2
    except Exception as exc:  # navigateur indisponible : jamais simulé
        print(f"NOT-VERIFIED — navigateur indisponible ({exc.__class__.__name__}) : page écrite, captures non produites.")
        return 2
    print("Captures : " + ", ".join(str(sortie / f"specimen-{w}px.png") for w in LARGEURS))
    for (nom, _), rendue in zip(voix, rendues):
        repli = "" if nom.lower() in rendue.lower() or rendue.lower().startswith(nom.lower()[:6]) else "  ← REPLI : la voix demandée n'est pas rendue"
        print(f"  {nom} : rendue par {rendue}{repli}")
    print("Comparer sur les captures : ton, coupe des lignes, chiffres et accents, tenue à 390 px. Le choix reste à justifier (SAVOIR/TYPE).")
    return 0


if __name__ == "__main__":
    import journal_mobilisation  # journal passif : n'écrit rien sans DG_JOURNAL
    sys.exit(journal_mobilisation.executer("specimen", main, sys.argv[1:]))
