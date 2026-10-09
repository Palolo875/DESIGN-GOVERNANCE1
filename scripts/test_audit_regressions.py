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
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "gouvernance" / "outils"))
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


class OperationalReferenceTests(unittest.TestCase):
    def check(self, text, extra=None):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            files = {"README.md": text, **(extra or {})}
            for name, content in files.items():
                target = root / name
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(content, encoding="utf-8")
            errors = []
            with patch.multiple(package, ROOT=root, EXPECTED=list(files)):
                package.check_inline_references(errors)
            return errors

    def test_deleted_changelog_reference_is_rejected(self):
        self.assertTrue(any("CHANGELOG.md" in e for e in self.check("Lire `CHANGELOG.md`.")))

    def test_moved_document_is_resolved_at_current_path(self):
        self.assertEqual(self.check("Lire `maintenance/versions.md`.", {"maintenance/versions.md": "# Versions"}), [])

    def test_relative_reference_and_unique_basename_are_supported(self):
        self.assertEqual(self.check("Lire `guides/equipe.md` et `equipe.md`.", {"guides/equipe.md": "# Équipe"}), [])

    def test_ambiguous_basename_is_rejected(self):
        self.assertTrue(self.check("Lire `aide.md`.", {"guides/aide.md": "# A", "design/aide.md": "# B"}))

    def test_nonexistent_fragment_is_rejected(self):
        self.assertTrue(any("fragment opérationnel" in e for e in self.check("Lire `README.md#absent`.")))

    def test_existing_fragment_is_accepted(self):
        self.assertEqual(self.check("# Entrée\nLire `README.md#entrée`."), [])

    def test_operational_command_checks_its_script(self):
        self.assertTrue(any("scripts/absent.py" in e for e in self.check("Lancer `python3 scripts/absent.py chemin/run.json`.")))

    def test_user_argument_is_not_a_package_dependency(self):
        self.assertEqual(self.check("Lancer `python3 scripts/test.py chemin/run.json`.", {"scripts/test.py": ""}), [])

    def test_bad_readable_address_is_rejected(self):
        self.assertTrue(any("route opérationnelle" in e for e in self.check("Lire `savoir/section-absente`.")))

    def test_bad_route_in_command_is_rejected(self):
        self.assertTrue(any("DIRECTION/ABSENT" in e for e in self.check("Lancer `python3 scripts/read_route.py DIRECTION/ABSENT`.",
                                                                         {"scripts/read_route.py": ""})))

    def test_explicit_examples_fences_and_provenance_are_not_dependencies(self):
        self.assertEqual(self.check("`exemple: chemin/fiche.md`\n<!-- origine:CHANGELOG.md -->\n"
                                    "````md\n```\n`absent.md`\n```\n````\n"), [])

    def test_existing_directory_is_not_a_route(self):
        self.assertEqual(self.check("Les fichiers sont dans `gouvernance/schemas`.",
                                    {"gouvernance/schemas/a.json": "{}"}), [])

    def test_explicit_other_distribution_uses_its_manifest(self):
        with patch.multiple(package, IS_LOCAL=True, LISTS={"github": ["scripts/github.py"], "local": []}):
            self.assertEqual(self.check("Dans GitHub : `python3 scripts/github.py`. <!-- références:github -->"), [])

    def test_scope_cannot_hide_an_undeclared_reference(self):
        with patch.multiple(package, IS_LOCAL=True, LISTS={"github": [], "local": []}):
            self.assertTrue(self.check("`scripts/absent.py` <!-- références:github -->"))

    def test_unscoped_github_instruction_is_rejected_in_local_export(self):
        with patch.multiple(package, IS_LOCAL=True, LISTS={"github": ["scripts/github.py"], "local": []}):
            self.assertTrue(self.check("Lancer `python3 scripts/github.py`."))

    def test_missing_scope_manifest_is_rejected_without_exception(self):
        with patch.multiple(package, IS_LOCAL=True, LISTS={"local": []}):
            self.assertTrue(any("manifeste de la portée" in e for e in self.check("`scripts/github.py` <!-- références:github -->")))

    def test_reference_outside_package_is_rejected(self):
        self.assertTrue(self.check("Lire `../README.md`."))


class SourceLocationTests(unittest.TestCase):
    def check(self, missing=False, unregistered=False, unknown=False):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            document = root / "source.md"
            document.write_text("<!-- origine:" + ("INCONNU.md" if unknown else "SAVOIR.md") + " -->\n# Savoir\n", encoding="utf-8")
            mapping = {f"{p}.md": ("source.md",) for p in routes.PREFIXES}
            if missing:
                mapping["SAVOIR.md"] += ("section-perdue.md",)
            if unregistered:
                other = root / "autre.md"
                other.write_text("# Autre\n")
                mapping["SAVOIR.md"] = ("autre.md",)
            errors = []
            with patch.multiple(package, ROOT=root, EXPECTED=["source.md"]), patch.multiple(routes, ROOT=root, LIEUX=mapping):
                package.check_source_locations(errors)
            return errors

    def test_missing_source_section_is_rejected(self):
        self.assertTrue(any("section-perdue.md" in e for e in self.check(missing=True)))

    def test_unregistered_provenance_is_rejected(self):
        self.assertTrue(any("provenance sans emplacement" in e for e in self.check(unregistered=True)))

    def test_registered_source_is_accepted(self):
        self.assertEqual(self.check(), [])

    def test_unknown_provenance_is_rejected(self):
        self.assertTrue(any("provenance inconnue" in e for e in self.check(unknown=True)))


class GovernancePresentationTests(unittest.TestCase):
    def test_contextual_governance_is_allowed(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "README.md").write_text("La gouvernance n’est pas toujours obligatoire ; elle s’adapte au contexte.")
            errors = []
            with patch.object(package, "ROOT", root):
                package.check_canonicity_language(errors)
            self.assertEqual(errors, [])

    def test_unconditional_exemption_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "design").mkdir()
            (root / "design/README.md").write_text("Le module de gouvernance peut s’ajouter ; il n’est jamais requis.")
            errors = []
            with patch.object(package, "ROOT", root):
                package.check_canonicity_language(errors)
            self.assertTrue(any("sans adaptation au contexte" in e for e in errors), errors)

    def test_unconditional_obligation_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "README.md").write_text("La gouvernance est toujours obligatoire.")
            errors = []
            with patch.object(package, "ROOT", root):
                package.check_canonicity_language(errors)
            self.assertTrue(any("sans adaptation au contexte" in e for e in errors), errors)


class CapabilityTests(unittest.TestCase):
    def setUp(self):
        self.document = cards.load_json(ROOT / "gouvernance/schemas/fixtures/valid_direction_exploratory_untransformed.json")
        self.schema = cards.load_json(ROOT / "gouvernance/schemas/run_card.schema.json")
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
        schema = cards.load_json(ROOT / 'gouvernance/schemas/run_card.schema.json')
        baseline = cards.load_json(ROOT / 'gouvernance/schemas/run_card.example.json')
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
