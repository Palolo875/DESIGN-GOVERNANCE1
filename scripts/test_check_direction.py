#!/usr/bin/env python3
"""Tests de la recette de caractère : règles de signal et de relevé, sans navigateur."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_direction as cd

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
                    {"focus": "unique", "intensity": "retenue"})
        self.assertEqual({s for s, _ in r}, {"RELEVÉ"})
        self.assertEqual({c for _, c in r}, {"Foyer", "Intensité", "Vide"})

    def test_vide_declare_muet(self):
        self.assertEqual(statuts({"bande_vide_px": 300}, {"intended_voids": True}), [])


if __name__ == "__main__":
    res = unittest.main(exit=False, verbosity=0).result
    n = res.testsRun
    if res.failures or res.errors:
        print(f"CHECK_DIRECTION TESTS FAILED — {len(res.failures) + len(res.errors)} échec(s) sur {n}"); sys.exit(1)
    print(f"CHECK_DIRECTION TESTS PASSED — {n} cas")
