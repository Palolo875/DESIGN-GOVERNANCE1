#!/usr/bin/env python3
"""Tests de la recette de caractère : règles de signal et de relevé (sans navigateur), puis mesures sur des pages
réelles dans un navigateur (NOT-VERIFIED si Playwright, numpy ou Pillow manquent ; --require-browser exige ces tests)."""
import argparse
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_caractere as cd

BASE = {"densite": .05, "vide": .54, "bande_vide_px": 0, "hauteur": 844, "saillance_top10": .5,
        "capture_preuve": .3, "surface_preuve": .3, "colorfulness": 5.0, "texte": .3, "image": 0, "aplats": .2}


def statuts(m=None, d=None, polices=None):
    return [(s["statut"], s["controle"]) for s in cd.evaluer({**BASE, **(m or {})}, d or {}, polices)]


class Regles(unittest.TestCase):
    def test_sans_declaration_rien(self):
        self.assertEqual(statuts(), [])

    def test_police_de_repli_signale(self):
        self.assertIn(("SIGNAL", "Polices rendues"), statuts(polices={"Liberation Serif": 82}))

    def test_densite_contredite_dans_les_deux_sens(self):
        self.assertIn(("SIGNAL", "Densité"), statuts({"vide": .41}, {"density": "respiration"}))
        self.assertIn(("SIGNAL", "Densité"), statuts({"vide": .66}, {"density": "compression"}))

    def test_zone_intermediaire_muette(self):
        self.assertEqual(statuts({"vide": .52}, {"density": "respiration"}), [])
        self.assertEqual(statuts({"vide": .52}, {"density": "compression"}), [])

    def test_matiere_quasi_egale_muette(self):
        self.assertEqual(statuts({"aplats": .28, "texte": .24}, {"material": "typographie"}), [])
        self.assertIn(("SIGNAL", "Matière dominante"), statuts({"aplats": .71, "texte": .34}, {"material": "typographie"}))

    def test_indicateurs_a_l_essai_restent_des_releves(self):
        r = statuts({"capture_preuve": .13, "surface_preuve": .26, "colorfulness": 69, "bande_vide_px": 144},
                    {"focus": "unique", "intensity": "retenue", "intended_voids": False})
        self.assertEqual({s for s, _ in r}, {"RELEVÉ"})
        self.assertEqual({c for _, c in r}, {"Foyer", "Intensité", "Vide"})

    def test_vide_declare_muet(self):
        self.assertEqual(statuts({"bande_vide_px": 300}, {"intended_voids": True}), [])

    def test_champ_absent_non_controle(self):
        # « Un champ absent n'est pas contrôlé » (ACTION/RECETTE-CARACTERE) : sans intended_voids, aucun relevé de vide.
        self.assertEqual(statuts({"bande_vide_px": 300}, {"density": "respiration", "vide": .52}), [])


PAGES = {
    "externe.html": '<link rel="stylesheet" href="https://fonts.example.invalid/police.css"><p style="margin:40px;font:16px serif">Texte.</p>',
    "aeree.html": '<p style="margin:40px;font:16px serif">Une seule ligne dans une page vide.</p>',
    "dense.html": '<div style="margin:0;font:16px/1.15 serif;text-align:justify">' + "Texte serré qui remplit tout l’écran sans respiration. " * 900 + "</div>",
    "aplats.html": ('<div style="display:grid;grid-template-columns:1fr 1fr;height:100vh">'
                    '<div style="background:#c33"></div><div style="background:#33c"><p style="margin:8px;color:#fff;font:14px serif">Légende</p></div></div>'),
}
CAS = [  # (page, déclaration, (statut, contrôle) attendu ou None si aucun signal de ce contrôle n'est attendu)
    ("aeree.html", {"density": "compression"}, ("SIGNAL", "Densité")),
    ("aeree.html", {"density": "respiration"}, None),
    ("dense.html", {"density": "respiration"}, ("SIGNAL", "Densité")),
    ("aplats.html", {"material": "typographie"}, ("SIGNAL", "Matière dominante")),
    ("aplats.html", {"material": "plan"}, None),
    ("aeree.html", {"fonts": ["Police absente du système"]}, ("SIGNAL", "Polices rendues")),
]


def navigateur(require: bool) -> str:
    """Mesures réelles : chaque cas lance la recette sur une page et lit sa sortie JSON."""
    try:
        import numpy  # noqa: F401
        from PIL import Image  # noqa: F401
        import playwright.sync_api  # noqa: F401
    except ImportError as exc:
        msg = f"NOT-VERIFIED : {exc.name} absent, mesures dans le navigateur non exécutées"
        print("  " + msg)
        if require:
            print("CHECK_CARACTERE TESTS FAILED — navigateur requis"); sys.exit(1)
        return msg
    echecs, indisponible = [], None
    with tempfile.TemporaryDirectory() as tmp:
        d = Path(tmp)
        for nom, corps in PAGES.items():
            (d / nom).write_text(f'<!doctype html><html lang="fr"><meta charset="utf-8"><title>t</title><body style="margin:0;background:#fff;color:#111">{corps}</body></html>', encoding="utf-8")
        for i, (page, decl, attendu) in enumerate(CAS):
            dfile, out = d / f"decl{i}.json", d / f"out{i}.json"
            dfile.write_text(json.dumps({"widths": [1280], **decl}), encoding="utf-8")
            r = subprocess.run([sys.executable, str(Path(__file__).with_name("check_caractere.py")), str(d / page), str(dfile), "--json", str(out)],
                               capture_output=True, text=True)
            if r.returncode == 2 and "navigateur indisponible" in r.stdout:
                indisponible = r.stdout.strip(); break
            if r.returncode != 0:
                echecs.append(f"{page} {decl} : code {r.returncode} {r.stdout.strip()[:120]}"); continue
            vus = {(x["statut"], x["controle"]) for x in json.loads(out.read_text(encoding="utf-8")) if x["statut"] != "MESURES"}
            controle = attendu[1] if attendu else {"density": "Densité", "material": "Matière dominante"}[next(iter(decl))]
            ok = attendu in vus if attendu else not any(c == controle for _, c in vus)
            print(f"  [{'ok' if ok else 'ÉCHEC'}] {page} {decl} : {sorted(vus) or 'aucun signal'}")
            if not ok:
                echecs.append(f"{page} {decl}")
        if indisponible is None:  # une ressource hébergée ailleurs est bloquée par défaut, comme dans check_render.py
            dfile = d / "externe.json"; dfile.write_text(json.dumps({"widths": [1280]}), encoding="utf-8")
            r = subprocess.run([sys.executable, str(Path(__file__).with_name("check_caractere.py")), str(d / "externe.html"), str(dfile)],
                               capture_output=True, text=True)
            ok = r.returncode == 0 and "externe(s) bloquée(s)" in r.stdout
            print(f"  [{'ok' if ok else 'ÉCHEC'}] externe.html : ressource externe bloquée par défaut")
            if not ok:
                echecs.append("externe.html : blocage externe non signalé")
    if indisponible is not None:
        msg = f"NOT-VERIFIED : Chromium indisponible, mesures dans le navigateur non exécutées ({indisponible[:160]})"
        print("  " + msg)
        if require:
            print("CHECK_CARACTERE TESTS FAILED — navigateur requis"); sys.exit(1)
        return msg
    if echecs:
        print(f"CHECK_CARACTERE TESTS FAILED — {len(echecs)} échec(s) dans le navigateur : {'; '.join(echecs)}"); sys.exit(1)
    return f"{len(CAS) + 1} cas dans le navigateur"


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Tests de la recette de caractère.")
    ap.add_argument("--require-browser", action="store_true", help="échouer si Playwright, numpy ou Pillow manquent")
    args = ap.parse_args()
    res = unittest.main(argv=[sys.argv[0]], exit=False, verbosity=0).result
    n = res.testsRun
    if res.failures or res.errors:
        print(f"CHECK_CARACTERE TESTS FAILED — {len(res.failures) + len(res.errors)} échec(s) sur {n}"); sys.exit(1)
    nav = navigateur(args.require_browser)
    print(f"CHECK_CARACTERE TESTS PASSED — règles : {n} cas ; {nav}")
