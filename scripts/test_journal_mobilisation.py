#!/usr/bin/env python3
"""Tests du journal de mobilisation : passif sans DG_JOURNAL, fidèle avec, jamais bloquant."""
import os
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import journal_mobilisation as jm


def lancer(*args, journal=None):
    env = {k: v for k, v in os.environ.items() if k != jm.VAR}
    if journal is not None:
        env[jm.VAR] = str(journal)
    return subprocess.run([sys.executable, str(ROOT / "scripts" / "read_route.py"), *args],
                          capture_output=True, text=True, encoding="utf-8", env=env, cwd=ROOT)


class Journal(unittest.TestCase):
    def test_sans_variable_rien_n_est_ecrit_et_la_sortie_est_identique(self):
        with tempfile.TemporaryDirectory() as tmp:
            chemin = Path(tmp) / "j.jsonl"
            sans, avec = lancer("SAVOIR/TYPE"), lancer("SAVOIR/TYPE", journal=chemin)
            self.assertEqual(sans.stdout, avec.stdout)
            self.assertEqual(sans.returncode, avec.returncode)
            self.assertFalse((Path(tmp) / "autre.jsonl").exists())
            entrees = jm.lire(chemin)
            self.assertEqual(len(entrees), 1)
            self.assertEqual(entrees[0]["routes_lues"], ["SAVOIR/TYPE"])
            self.assertEqual(entrees[0]["code"], 0)

    def test_echec_de_lecture_journalise_avec_son_code(self):
        with tempfile.TemporaryDirectory() as tmp:
            chemin = Path(tmp) / "j.jsonl"
            r = lancer("NEXISTE/PAS", journal=chemin)
            self.assertNotEqual(r.returncode, 0)
            self.assertEqual(jm.lire(chemin)[0]["code"], r.returncode)

    def test_journal_impossible_a_ecrire_ne_bloque_pas(self):
        with tempfile.TemporaryDirectory() as tmp:
            r = lancer("SAVOIR/TYPE", journal=Path(tmp))  # un dossier : écriture impossible
            self.assertEqual(r.returncode, 0)
            self.assertIn("ROUTE: SAVOIR/TYPE", r.stdout)
            self.assertIn("journal de mobilisation non écrit", r.stderr)

    def test_resume_des_recettes(self):
        rendu = "[RETURN               ] Contraste du texte sur fond uni : 2 textes\n[PASS                 ] Débordement : aucun\n"
        self.assertEqual(jm.resumer("check_render", rendu)["resultats"], {"RETURN": ["Contraste du texte sur fond uni"], "PASS": ["Débordement"]})
        caractere = "[SIGNAL] 390px · Polices rendues · glyphes hors · savoir : SAVOIR/TYPE\n[RELEVÉ] 390px · Foyer · x · savoir : y\n"
        self.assertEqual(jm.resumer("check_caractere", caractere)["resultats"], {"SIGNAL": ["Polices rendues"], "RELEVÉ": ["Foyer"]})
        self.assertTrue(jm.resumer("check_caractere", "NOT-VERIFIED — navigateur indisponible")["non_verifie"])

    def test_fiche_signale_le_tronc_non_consulte(self):
        entrees = [{"horodatage": "2026-10-21T10:00:00+00:00", "outil": "read_route", "commande": ["--mode", "ITER"], "code": 0,
                    "routes_lues": [], "routes_proposees": []}]
        texte = jm.fiche(entrees)
        self.assertIn("ligne du mode ITER", texte)
        self.assertIn("Tronc ITER non consulté", texte)
        lu = [{"outil": "read_route", "commande": ["--tronc", "ITER"], "code": 0, "routes_lues": ["ACTION/RUN-ITER", "ACTION/GATE-A"], "routes_proposees": []}]
        self.assertNotIn("Tronc ITER non consulté", jm.fiche(lu))

    def test_fiche_outil_en_echec(self):
        e = [{"outil": "check_caractere", "commande": ["p.html", "d.json"], "code": 2, "non_verifie": True, "resultats": {}}]
        self.assertIn("sollicité, en échec", jm.fiche(e))

    def test_sortie_en_erreur_sans_resultat_n_est_pas_un_succes(self):
        e = [{"outil": "check_caractere", "commande": ["p.html", "d.json"], "code": 1, "non_verifie": False, "resultats": {}}]
        self.assertIn("en échec (code 1, aucun résultat)", jm.fiche(e))
        usage = [{"outil": "check_render", "commande": ["--inconnue"], "code": 2, "non_verifie": False, "resultats": {}}]
        self.assertNotIn("NOT-VERIFIED", jm.fiche(usage))
        self.assertIn("en échec (code 2", jm.fiche(usage))
        retour = [{"outil": "check_render", "commande": ["p.html"], "code": 1, "non_verifie": False, "resultats": {"RETURN": ["Contraste"]}}]
        self.assertIn("RETURN — Contraste", jm.fiche(retour))

    def test_options_ecrites_avec_egal(self):
        e = [{"outil": "read_route", "commande": ["--mode=ITER"], "code": 0, "routes_lues": [], "routes_proposees": []}]
        texte = jm.fiche(e)
        self.assertIn("ligne du mode ITER", texte)
        self.assertIn("Tronc ITER non consulté", texte)
        self.assertEqual(jm.option(["--tronc=DIRECTION"], "--tronc"), "DIRECTION")

    def test_appel_avec_parametres_et_expressions(self):
        cmd = ["index.html?date=2026-12-01", "--widths", "1440", "--assert", "a || b", "--assert", "c", "--click=#go"]
        e = [{"outil": "check_render", "commande": cmd, "code": 0, "non_verifie": False, "resultats": {"PASS": ["x"]}}]
        ligne = [l for l in jm.fiche(e).splitlines() if l.startswith("| 1 |")][0]
        self.assertIn("`index.html` ?date=2026-12-01", ligne)
        self.assertIn("--assert ×2", ligne)
        self.assertIn("--click", ligne)
        self.assertNotIn("a || b", ligne)
        self.assertEqual(len(re.split(r"(?<!\\)\|", ligne)), 8)  # six cellules, aucune cassée par un « | »

    def test_journal_absent(self):
        self.assertEqual(jm.main(["/chemin/inexistant.jsonl"]), 2)


if __name__ == "__main__":
    res = unittest.main(exit=False, verbosity=0).result
    if res.failures or res.errors:
        print(f"JOURNAL TESTS FAILED — {len(res.failures) + len(res.errors)} échec(s) sur {res.testsRun}"); sys.exit(1)
    print(f"JOURNAL TESTS PASSED — {res.testsRun} cas")
