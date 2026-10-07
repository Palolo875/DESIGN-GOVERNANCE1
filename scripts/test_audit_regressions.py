#!/usr/bin/env python3
"""Témoins de l'audit simulé : navigation réelle et profil de capacités cohérent.

Ces tests n'établissent ni une compréhension utilisateur ni un gain esthétique.
"""
from __future__ import annotations

import copy
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import validate_design_governance as package
import validate_run_card as cards
import validate_reading_map as reading_map
import validate_structure as structure
import read_route as routes

ROOT = Path(__file__).resolve().parents[1]


class MobilisationFacadeTests(unittest.TestCase):
    def setUp(self):
        self.texts = reading_map.load_texts()

    def assert_rejected(self, key, old, new, expected):
        texts = dict(self.texts)
        self.assertIn(old, texts[key])
        texts[key] = texts[key].replace(old, new, 1)
        errors = []
        with patch.object(reading_map, "load_texts", return_value=texts):
            reading_map.check_facades(errors)
        self.assertTrue(any(expected in error for error in errors), errors)

    def test_inheritance_cannot_become_non_applicability(self):
        self.assert_rejected("B", "conserve-la par héritage ou comme cas documentaire, avec sa source et sa justification.",
                             "conserve-la et justifie `N/A-JUSTIFIED`.", "LCF-51")

    def test_run_card_cannot_be_required_by_mode_alone(self):
        self.assert_rejected("G", "Son exigence dépend du niveau de trace et du mode ; une proposition en trace légère ne produit pas de RUN_CARD.",
                             "Elle est toujours exigée en STANDARD et DIRECTION.", "LCF-52")

    def test_domain_template_cannot_omit_risk_coverage(self):
        self.assert_rejected("D", "`required_controls`, `risk_coverage`, `depth_rules`", "`required_controls`, `depth_rules`", "LCF-53")

    def test_activation_cannot_disappear_from_compiled_core(self):
        self.assert_rejected("SK", "python3 scripts/read_route.py --connexions", "commande retirée", "LCF-54")

    def test_iter_cannot_capture_local_fix(self):
        self.assert_rejected('D','au-delà d’un fix ou delta local qui la conserve','y compris tout fix local','LCF-55')

    def test_quickstart_must_keep_iter_discriminant(self):
        self.assert_rejected('Q','au-delà d’un fix local qui la conserve','quel que soit le delta','LCF-55')

    def test_persistence_cannot_erase_short_lite_exception(self):
        self.assert_rejected('A','sauf la forme courte LITE définie ci-dessus','sans exception','LCF-56')

    def test_glossary_cannot_make_complete_trace_always_structured(self):
        self.assert_rejected('G','La forme courte LITE définie par `ACTION/HANDOFF` est complète sans RUN_CARD','Toute trace complète exige une RUN_CARD','LCF-56')

    def test_map_cannot_erase_short_lite_exception(self):
        self.assert_rejected('RM','sauf la forme courte LITE sans RUN_CARD définie','sans exception définie','LCF-56')

    def test_compiled_trace_keeps_short_lite_exception(self):
        self.assert_rejected('SK','La forme courte LITE conserve une trace complète sans RUN_CARD','Toute clôture exige une RUN_CARD','LCF-56')


class NavigationTests(unittest.TestCase):
    def check(self, text: str, extra: dict[str, str] | None = None) -> list[str]:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "README.md").write_text(text, encoding="utf-8")
            for name, content in (extra or {}).items():
                (root / name).write_text(content, encoding="utf-8")
            with patch.object(package, "ROOT", root):
                errors: list[str] = []
                package.check_links(errors)
                return errors

    def test_same_document_missing_section_refused(self):
        self.assertTrue(any("fragment Markdown introuvable" in e for e in self.check("# Entrée\n[aide](#absente)\n")))

    def test_same_document_existing_section_admitted(self):
        self.assertEqual(self.check("# Entrée\n[aide](#entrée)\n"), [])

    def test_code_example_is_not_a_destination(self):
        text = "# Entrée\n```md\n## Section fictive\n```\n[aide](guide.md#section-fictive)\n"
        self.assertTrue(any("fragment Markdown introuvable" in e for e in self.check(text, {"guide.md": text})))

    def test_nested_code_example_is_not_a_destination(self):
        text='# Entrée\n````md\n```\n## Faux\n```\n````\n[aide](#faux)\n'
        self.assertTrue(any('fragment Markdown introuvable' in e for e in self.check(text)))

    def test_formatted_heading_uses_visible_text(self):
        self.assertEqual(self.check("# `État` : _d’abord_ !\n[aide](#état--dabord-)\n"), [])

    def test_duplicate_heading_suffix_admitted(self):
        self.assertEqual(self.check("# Entrée\n## Aide\n## Aide\n[deuxième](#aide-1)\n"), [])

    def test_duplicate_suffix_without_heading_refused(self):
        self.assertTrue(any("fragment Markdown introuvable" in e for e in self.check("# Aide\n[absente](#aide-1)\n")))

    def test_custom_html_anchor_admitted(self):
        self.assertEqual(self.check('# Entrée\n<a name="reprise"></a>\n[aide](#reprise)\n'), [])

    def test_encoded_fragment_admitted(self):
        self.assertEqual(self.check("# Entrée\n[aide](#entr%C3%A9e)\n"), [])

    def test_external_link_is_not_fetched(self):
        self.assertEqual(self.check("# Entrée\n[externe](https://example.invalid/#absente)\n"), [])

    def test_missing_file_still_refused(self):
        self.assertTrue(any("lien relatif cassé" in e for e in self.check("# Entrée\n[aide](absent.md#aide)\n")))


class CapabilityTests(unittest.TestCase):
    def setUp(self):
        self.document = cards.load_json(ROOT / "schemas/fixtures/valid_direction_exploratory_untransformed.json")
        self.schema = cards.load_json(ROOT / "schemas/run_card.schema.json")
        self.profile = {"available": ["inspection vectorielle"], "unavailable": ["navigateur/capture"],
                        "not_required": ["connexion bancaire"], "basis": [
                            {"capability": "inspection vectorielle", "kind": "tool_result", "detail": "Rasterisation du SVG et inspection du rendu."}]}

    def validate(self, profile):
        document = copy.deepcopy(self.document)
        document["run_card"]["capability_profile"] = profile
        cards.validate_card(document, self.schema)

    def test_disjoint_categories_admitted(self):
        self.validate(self.profile)

    def test_available_and_unavailable_refused(self):
        self.profile["unavailable"].append("inspection vectorielle")
        with self.assertRaisesRegex(cards.ValidationError, "plusieurs catégories"):
            self.validate(self.profile)

    def test_available_and_not_required_refused(self):
        self.profile["not_required"].append("inspection vectorielle")
        with self.assertRaisesRegex(cards.ValidationError, "plusieurs catégories"):
            self.validate(self.profile)

    def test_unavailable_and_not_required_refused(self):
        self.profile["not_required"].append("navigateur/capture")
        with self.assertRaisesRegex(cards.ValidationError, "plusieurs catégories"):
            self.validate(self.profile)

    def test_surrounding_spaces_do_not_hide_conflict(self):
        self.profile["unavailable"].append(" inspection vectorielle ")
        with self.assertRaisesRegex(cards.ValidationError, "plusieurs catégories"):
            self.validate(self.profile)

    def test_empty_availability_is_not_success_or_failure(self):
        self.validate({"available": [], "unavailable": ["navigateur/capture"], "not_required": [], "basis": []})


class StrictHostTests(unittest.TestCase):
    def test_demo_families_for_artifact_and_trace_without_network(self):
        schema = cards.load_json(ROOT / 'schemas/run_card.schema.json')
        baseline = cards.load_json(ROOT / 'schemas/run_card.example.json')
        baseline['run_card']['artifact']['locator'] = 'https://production.audit-project.test/page'
        baseline['run_card']['proof']['provenance']['artifact_locator'] = baseline['run_card']['artifact']['locator']
        baseline['run_card']['trace_locator'] = 'trace-audit-42'
        pair = baseline['run_card']['closure']['b1b']['pair']  # captures non locales : hors contrôle d'existence (C47)
        pair['before_locator'], pair['after_locator'] = ('https://production.audit-project.test/v1.png',
                                                         'https://production.audit-project.test/v1b.png')
        cards.validate_card(baseline, schema, strict=True)
        for field in ('artifact', 'trace'):
            for host, rejected in [('example.com', True), ('EXAMPLE.COM', True), ('www.example.com', True),
                                   ('example.com.', True), ('demo.example.invalid', True), ('other.invalid.', True),
                                   ('x.example.org.', True), ('www.example.net', True),
                                   ('example.org.evil.test', False), ('myexample.com', False),
                                   ('production.audit-project.test', False)]:
                with self.subTest(field=field, host=host):
                    document = copy.deepcopy(baseline)
                    locator = 'https://' + host + '/page'
                    if field == 'artifact':
                        document['run_card']['artifact']['locator'] = locator
                        document['run_card']['proof']['provenance']['artifact_locator'] = locator
                    else:
                        document['run_card']['trace_locator'] = locator
                    if rejected:
                        with self.assertRaisesRegex(cards.ValidationError, 'URL de démonstration interdite'):
                            cards.validate_card(document, schema, strict=True)
                    else:
                        cards.validate_card(document, schema, strict=True)


class CoreResourceActivationTests(unittest.TestCase):
    def test_compiled_resource_relays_cannot_disappear(self):
        skill = structure.SKILL_DIR / 'SKILL.md'
        original = skill.read_text()
        for locator in ('SAVOIR/TOOLS/CONVERGENCE', 'SAVOIR/TOOLS/MOYENS'):
            with self.subTest(locator=locator), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp); (root / 'SKILL.md').write_text(original.replace('`' + locator + '`', 'relai retiré'))
                errors = []
                with patch.object(structure, 'SKILL_DIR', root):
                    structure.check_core_floor(errors)
                self.assertEqual(len(errors), 1, errors)
                self.assertIn('activation conditionnelle', errors[0])

    def test_dated_details_remain_reachable(self):
        for locator, expected in [('SAVOIR/TOOLS/CONVERGENCE', 'Signaux à confirmer'), ('SAVOIR/TOOLS/MOYENS', 'Typographie')]:
            with self.subTest(locator=locator):
                _, lines, index = routes.resolve(locator)
                self.assertIn(expected, '\n'.join(routes.extract(lines, index)))


if __name__ == "__main__":
    result = unittest.TextTestRunner(stream=sys.stdout).run(unittest.defaultTestLoader.loadTestsFromModule(sys.modules[__name__]))
    print(f"AUDIT REGRESSIONS {'PASSED' if result.wasSuccessful() else 'FAILED'} — {result.testsRun} cas")
    sys.exit(0 if result.wasSuccessful() else 1)
