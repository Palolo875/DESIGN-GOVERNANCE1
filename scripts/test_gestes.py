#!/usr/bin/env python3
"""Tests des gestes liés aux recettes (scripts/gestes.py), sans navigateur.

Ils vérifient que le tableau est lu dans sa source, que chaque terme des correspondances existe, que la sortie
reste bornée, qu'un geste déjà servi dans le journal n'est que rappelé, et que le journal relève les gestes servis
sans modifier le relevé des résultats.
"""
from __future__ import annotations

import json
import os
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import gestes  # noqa: E402
import journal_mobilisation  # noqa: E402


class GestesTests(unittest.TestCase):
    def setUp(self):
        self._journal = os.environ.pop("DG_JOURNAL", None)

    def tearDown(self):
        os.environ.pop("DG_JOURNAL", None)
        if self._journal is not None:
            os.environ["DG_JOURNAL"] = self._journal

    def test_tableau_lu_dans_sa_source(self):
        table = gestes.tableau()
        self.assertGreaterEqual(len(table), 10)
        for row in table.values():
            self.assertTrue(row["signal"] and row["geste"] and row["reinspection"])

    def test_chaque_terme_lie_existe(self):
        table = gestes.tableau()
        manquants = {t for *_, termes in gestes.LIENS for t in termes if t not in table}
        self.assertEqual(manquants, set(), "terme des correspondances absent du tableau de SAVOIR/STATE")

    def test_correspondances(self):
        self.assertEqual(gestes.termes_pour("check_render", [("RETURN", "Contraste du texte sur fond uni", "x")]),
                         [("Texte secondaire", "Contraste du texte sur fond uni")])
        # une réserve de contraste ne sert « Image intégrée » que si un fond non uni est en cause
        self.assertEqual(gestes.termes_pour("check_render", [("PASS-WITH-RESERVATION", "Contraste du texte sur fond uni",
                                                              "texte SVG non évalué")]), [])
        self.assertEqual([t for t, _ in gestes.termes_pour("check_render", [("PASS-WITH-RESERVATION", "Contraste du texte sur fond uni",
                                                                             "fond en dégradé, en image ou translucide")])], ["Image intégrée"])
        self.assertEqual(gestes.termes_pour("check_render", [("PASS", "Contraste du texte sur fond uni", "x")]), [])
        # sans doublon, dans l'ordre des résultats
        termes = [t for t, _ in gestes.termes_pour("check_caractere", [("SIGNAL", "Densité", "x"), ("RELEVÉ", "Vide", "y")])]
        self.assertEqual(termes, ["Gestion du vide", "Masse visuelle"])
        self.assertEqual(gestes.termes_pour("check_caractere", [("SIGNAL", "Densité", "x")]),
                         gestes.termes_pour("check_caractere", [("SIGNAL", "Densité", "x")]))
        self.assertEqual(gestes.termes_pour("autre", [("SIGNAL", "Densité", "x")]), [])

    def test_bloc_borne_et_vide_sans_signal(self):
        self.assertEqual(gestes.bloc("check_render", [("PASS", "Débordement horizontal", "aucun")]), "")
        res = [("SIGNAL", "Densité", "x"), ("SIGNAL", "Matière dominante", "y"), ("RELEVÉ", "Foyer", "z"), ("RELEVÉ", "Intensité", "w")]
        texte = gestes.bloc("check_caractere", res)
        self.assertEqual(texte.count(gestes.PUCE), gestes.PLAFOND)
        self.assertIn("autre(s)", texte)
        self.assertIn("Geste :", texte)
        self.assertIn("Réinspecter :", texte)

    def test_rappel_si_deja_servi_dans_le_journal(self):
        with tempfile.TemporaryDirectory() as tmp:
            journal = Path(tmp) / "run.jsonl"
            journal.write_text(json.dumps({"outil": "check_caractere", "gestes": ["Gestion du vide"]}) + "\n", encoding="utf-8")
            os.environ["DG_JOURNAL"] = str(journal)
            texte = gestes.bloc("check_caractere", [("SIGNAL", "Densité", "x")])
        self.assertIn("Gestion du vide [Densité] — déjà servi", texte)
        self.assertIn("Masse visuelle [Densité] — Signal :", texte)

    def test_journal_releve_les_gestes_sans_fausser_les_resultats(self):
        sortie = ("[RETURN               ] Contraste du texte sur fond uni : #999 sur #fff\n"
                  "[PASS                 ] Débordement horizontal : aucun\n"
                  + gestes.bloc("check_render", [("RETURN", "Contraste du texte sur fond uni", "x")]))
        resume = journal_mobilisation.resumer("check_render", sortie)
        self.assertEqual(resume["gestes"], ["Texte secondaire"])
        self.assertEqual(resume["resultats"], {"RETURN": ["Contraste du texte sur fond uni"], "PASS": ["Débordement horizontal"]})
        caractere = ("[SIGNAL] 390px · Densité · respiration déclarée · savoir : X\n"
                     + gestes.bloc("check_caractere", [("SIGNAL", "Densité", "x")]))
        resume = journal_mobilisation.resumer("check_caractere", caractere)
        self.assertEqual(resume["resultats"], {"SIGNAL": ["Densité"]})
        self.assertEqual(resume["gestes"], ["Gestion du vide", "Masse visuelle"])

    def test_commande_directe(self):
        self.assertEqual(gestes.main(["Surface"]), 0)
        self.assertEqual(gestes.main(["Terme absent"]), 1)


if __name__ == "__main__":
    result = unittest.main(exit=False, verbosity=1).result
    ok = result.wasSuccessful()
    print("GESTES TESTS PASSED" if ok else "GESTES TESTS FAILED")
    sys.exit(0 if ok else 1)
