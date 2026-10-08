#!/usr/bin/env python3
"""Régressions du lecteur : propriété, recherche (littérale, alias, classement), sommaire, périmètre et erreurs CLI."""
from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import read_route as reader
import validate_structure as structure

ROOT = Path(__file__).resolve().parents[1]


class CodeFenceTests(unittest.TestCase):
    def test_nested_shorter_fence_is_code(self):
        lines=['````markdown','```','## ACTION/GATE-A — faux','```','````','## Titre réel']
        self.assertEqual(reader.headings(lines),[(5,2,'## Titre réel')])

    def test_tilde_fence_and_longer_close(self):
        lines=[' ~~~~md','~~~','## Faux','  ~~~~~','## Réel']
        self.assertEqual(reader.headings(lines),[(4,2,'## Réel')])

    def test_other_character_cannot_close(self):
        self.assertEqual(reader.headings(['```','~~~','## Faux','```','## Réel']),[(4,2,'## Réel')])

    def test_close_with_trailing_text_is_not_close(self):
        self.assertEqual(reader.headings(['```','```texte','## Faux','```','## Réel']),[(4,2,'## Réel')])

    def test_unclosed_fence_hides_tail(self):
        self.assertEqual(reader.headings(['## Avant','````','```','## Faux']),[(0,2,'## Avant')])

    def test_indices_preserved(self):
        self.assertEqual(list(reader.non_code_lines(['avant','```','code','```','après'])),[(0,'avant'),(4,'après')])

    def test_three_character_fence_kept(self):
        self.assertEqual(reader.headings(['```md','## Faux','```','## Réel']),[(3,2,'## Réel')])

    def test_structural_identifier_inside_four_character_fence_refused(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/'BIBLIOTHEQUE.md'
            p.write_text('# B\n## BIBLIOTHEQUE/OBJECT\n````md\n```\n| `OBJECT/PROOF` | faux |\n```\n````\n')
            with patch.object(reader,'OFFICIAL',Path(tmp)):
                with self.assertRaises(reader.RouteError):reader.resolve('OBJECT/PROOF')


class SearchTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.official = self.root / "official"
        self.official.mkdir()
        for prefix in reader.PREFIXES:
            (self.official / f"{prefix}.md").write_text(f"# {prefix}\n\n## {prefix}/TEST\nPassage de base.\n", encoding="utf-8")
        (self.official / "READING_MAP.md").write_text("# Carte\n## Locators principaux\n## Condition d’arrêt\n", encoding="utf-8")
        (self.official / "SAVOIR.md").write_text(
            "# Savoir\n## SAVOIR/STATE\nCohérence de rayon : signal utile.\n"
            "### SAVOIR/CHILD\nUn signal enfant précis.\n<!-- concept:TEST-MARKER -->\n", encoding="utf-8")
        (self.official / "QUICKSTART.md").write_text("Cohérence de rayon dans le guide.\n", encoding="utf-8")
        self.override = patch.multiple(reader, ROOT=self.root, OFFICIAL=self.official, MAP=self.official / "READING_MAP.md")
        self.override.start()

    def tearDown(self):
        self.override.stop()
        self.tmp.cleanup()

    def test_accents_and_case(self):
        result = reader.find("COHERENCE DE RAYON")
        self.assertEqual([(r[0], r[1]) for r in result], [("SAVOIR/STATE", "SAVOIR.md")])

    def test_guides_are_opt_in(self):
        self.assertEqual(len(reader.find("cohérence de rayon")), 1)
        self.assertEqual([r[1] for r in reader.find("cohérence de rayon", True)], ["SAVOIR.md", "QUICKSTART.md"])

    def test_guides_include_root_readme_and_skill_references(self):
        (self.root / "README.md").write_text("Cohérence de rayon à l’entrée.\n", encoding="utf-8")
        for refs in (self.root / "skills" / "practice" / "references", self.root / "skill" / "references"):
            refs.mkdir(parents=True)
            (refs / "examples.md").write_text("Cohérence de rayon en exemple.\n", encoding="utf-8")
        self.assertEqual(len(reader.find("cohérence de rayon")), 1)
        self.assertEqual([r[1] for r in reader.find("cohérence de rayon", True)],
                         ["SAVOIR.md", "QUICKSTART.md", "README.md",
                          "skills/practice/references/examples.md", "skill/references/examples.md"])

    def test_no_semantic_match(self):
        self.assertEqual(reader.find("courbure concentrique"), [])

    def test_internal_marker_excluded(self):
        self.assertEqual(reader.find("TEST-MARKER"), [])

    def test_precise_route_actually_serves_each_line(self):
        for locator, _, _, line in reader.find("signal"):
            self.assertIsNotNone(locator)
            _, lines, index = reader.resolve(locator)
            self.assertIn(line, [text.strip() for text in reader.extract(lines, index)])
        self.assertEqual(reader.find("enfant")[0][0], "SAVOIR/CHILD")

    def test_missing_source_refused(self):
        (self.official / "ACTION.md").unlink()
        with self.assertRaisesRegex(reader.RouteError, "propriétaire absent"):
            reader.find("signal")

    def test_ambiguous_route_refused_in_search(self):
        p = self.official / "SAVOIR.md"
        p.write_text(p.read_text() + "\n## SAVOIR/STATE\nAutre signal.\n", encoding="utf-8")
        with self.assertRaisesRegex(reader.RouteError, "locator ambigu"):
            reader.find("signal")

    def test_empty_query_refused(self):
        with self.assertRaisesRegex(reader.RouteError, "terme de recherche vide"):
            reader.find("  \t")

    def test_excerpt_keeps_match_after_unicode_expansion(self):
        line = "ﬃ" * 90 + " terme recherché " + "fin" * 90
        self.assertIn("terme recherché", reader._excerpt(line, "TERME RECHERCHE"))


class StructureIdentifierTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.official = Path(self.tmp.name)
        self.source = self.official / "BIBLIOTHEQUE.md"
        self.source.write_text(
            "# Bibliothèque\n## BIBLIOTHEQUE/GRID\n"
            "### `GRID/HIERARCHICAL`\nPriorité.\n"
            "### `GRID/COLUMN`\nComparaison.\n"
            "## BIBLIOTHEQUE/MICRO\n| Nom | Rôle |\n|---|---|\n"
            "| `MICRO/USAGE_LEDGER` | Mesure. |\n", encoding="utf-8")
        self.override = patch.object(reader, "OFFICIAL", self.official)
        self.override.start()

    def tearDown(self):
        self.override.stop()
        self.tmp.cleanup()

    def test_short_identifier_reads_only_its_heading(self):
        path, lines, index = reader.resolve("GRID/HIERARCHICAL", {})
        self.assertEqual(path, self.source)
        self.assertEqual(reader.extract(lines, index), ["### `GRID/HIERARCHICAL`", "Priorité."])

    def test_prefixed_identifier_reads_same_section(self):
        self.assertEqual(reader.resolve("BIBLIOTHEQUE/GRID/HIERARCHICAL", {}),
                         reader.resolve("GRID/HIERARCHICAL", {}))

    def test_table_identifier_returns_owning_section(self):
        _, lines, index = reader.resolve("MICRO/USAGE_LEDGER", {})
        self.assertEqual(lines[index], "## BIBLIOTHEQUE/MICRO")
        self.assertNotIn("Priorité.", reader.extract(lines, index))

    def test_unknown_identifier_is_not_its_parent(self):
        with self.assertRaisesRegex(reader.RouteError, "locator inconnu"):
            reader.resolve("MICRO/UNKNOWN", {})

    def test_duplicate_identifier_refused(self):
        self.source.write_text(self.source.read_text() + "| `MICRO/USAGE_LEDGER` | Autre. |\n", encoding="utf-8")
        with self.assertRaisesRegex(reader.RouteError, "ambigu"):
            reader.resolve("MICRO/USAGE_LEDGER", {})

    def test_code_example_is_not_a_catalogue_identifier(self):
        self.source.write_text(self.source.read_text() + "```md\n| `MICRO/EXAMPLE_ONLY` | Exemple. |\n```\n", encoding="utf-8")
        with self.assertRaisesRegex(reader.RouteError, "locator inconnu"):
            reader.resolve("MICRO/EXAMPLE_ONLY", {})

    def test_layer_identifier_uses_component_owner(self):
        self.source.write_text(self.source.read_text() +
                               "## BIBLIOTHEQUE/COMPONENTS\n### `LAYER/TOKENS`\nValeurs.\n", encoding="utf-8")
        _, lines, index = reader.resolve("LAYER/TOKENS", {})
        self.assertEqual(lines[index], "### `LAYER/TOKENS`")
        self.assertEqual(reader.resolve("BIBLIOTHEQUE/LAYER/TOKENS", {}),
                         reader.resolve("LAYER/TOKENS", {}))


class ConnectionTests(unittest.TestCase):
    def setUp(self):
        self.text = reader.MAP.read_text(encoding="utf-8")

    def test_every_connection_has_resolved_sources(self):
        revision, entries = reader.connections(self.text)
        self.assertTrue(revision)
        for key, entry in entries.items():
            with self.subTest(connection=key):
                self.assertTrue(reader.connection_sources(entry))

    def test_duplicate_connection_refused(self):
        with self.assertRaisesRegex(reader.RouteError, "connexion en double"):
            reader.parse_connections(self.text.replace("### C02 —", "### C01 —", 1))

    def test_missing_condition_refused(self):
        with self.assertRaisesRegex(reader.RouteError, "Condition et décision"):
            reader.parse_connections(self.text.replace("**Condition et décision.**", "", 1))

    def test_missing_contraindication_refused(self):
        with self.assertRaisesRegex(reader.RouteError, "Contre-indication et alternative"):
            reader.parse_connections(self.text.replace("**Contre-indication et alternative.**", "", 1))

    def test_duplicate_field_refused(self):
        with self.assertRaisesRegex(reader.RouteError, "champ inconnu ou répété"):
            reader.parse_connections(self.text.replace("**Sources.**", "**Sources.** passage\n\n**Sources.**", 1))

    def test_foreign_source_is_not_an_owner(self):
        with self.assertRaisesRegex(reader.RouteError, "non propriétaires"):
            reader.parse_connections(self.text.replace("`DIRECTION/DOMAIN-FRAME` ;", "`EXTERNAL/DOMAIN-FRAME` ;", 1))

    def test_unknown_route_refused(self):
        with self.assertRaisesRegex(reader.RouteError, "locator inconnu"):
            reader.connections(self.text.replace("`DIRECTION/DOMAIN-FRAME` ;", "`DIRECTION/ABSENT` ;", 1))

    def test_stale_revision_refused(self):
        revision, _ = reader.parse_connections(self.text)
        with self.assertRaisesRegex(reader.RouteError, "révision des connexions différente"):
            reader.connections(self.text.replace(f"**Base de sources :** `{revision}`.", "**Base de sources :** `ancienne`."))

    def test_sources_use_the_same_map_under_validation(self):
        row = next(line for line in self.text.splitlines() if line.startswith("| `DIRECTION/START` |"))
        changed = self.text.replace(row, row.replace("`DIRECTION.md`", "`SAVOIR.md`", 1))
        with self.assertRaisesRegex(reader.RouteError, "propriétaire incohérent"):
            reader.connections(changed)

    def test_code_example_is_not_a_connection(self):
        text = self.text.replace("## Activation multi-perspective", "```md\n### C98 — Exemple de code\n```\n\n## Activation multi-perspective", 1)
        self.assertIn("C98", text)
        _, entries = reader.connections(text)
        self.assertNotIn("C98", entries)


class CliTests(unittest.TestCase):
    def cli(self, *args):
        return subprocess.run([sys.executable, str(ROOT / "scripts/read_route.py"), *args], capture_output=True, text=True)

    def test_normative_results_not_inflated_by_guides(self):
        r = self.cli("--trouver", "COHERENCE DE RAYON")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("SAVOIR/STATE", r.stdout)
        self.assertNotIn("QUICKSTART.md:", r.stdout)
        self.assertIn("0 ligne(s) de guide", r.stdout)

    def test_guides_separated_from_normative_results(self):
        r = self.cli("--trouver", "cohérence de rayon", "--guides")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("GUIDES — orientation, sans autorité normative", r.stdout)
        self.assertIn("QUICKSTART.md:", r.stdout)

    def test_missing_term_reports_search_limit(self):
        r = self.cli("--trouver", "zztermeabsentpourtestzz")
        self.assertEqual(r.returncode, 1)
        self.assertIn("ne prouve pas l’absence du savoir", r.stdout)
        self.assertNotIn("Traceback", r.stderr)

    def test_guides_with_locator_refused(self):
        r = self.cli("DIRECTION/START", "--guides")
        self.assertEqual(r.returncode, 2)
        self.assertIn("--guides exige", r.stderr)

    def test_empty_cli_query_refused(self):
        r = self.cli("--trouver", "   ")
        self.assertEqual(r.returncode, 2)
        self.assertIn("terme de recherche vide", r.stderr)

    def test_locator_and_query_refused(self):
        r = self.cli("DIRECTION/START", "--trouver", "terme")
        self.assertEqual(r.returncode, 2)

    def test_known_route_still_readable(self):
        r = self.cli("SAVOIR/STATE")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("Cohérence de rayon", r.stdout)
        self.assertNotIn("<!-- concept:", r.stdout)

    def test_connection_summary_does_not_load_all_details(self):
        r = self.cli("--connexions")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("C07 — Ambition vers construction", r.stdout)
        self.assertIn("START et CHARGE", r.stdout)
        self.assertNotIn("**Moyens et limites.**", r.stdout)

    def test_connection_detail_keeps_sources_and_limits(self):
        r = self.cli("--connexions", "C03")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("**Contre-indication et alternative.**", r.stdout)
        self.assertIn("**Moyens et limites.**", r.stdout)
        self.assertIn("SOURCES RÉSOLUES", r.stdout)
        self.assertIn("SOURCE-VERSION:", r.stdout)
        self.assertNotIn("C04 —", r.stdout)

    def test_unknown_connection_refused(self):
        r = self.cli("--connexions", "C99")
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("connexion inconnue", r.stderr)
        self.assertNotIn("Traceback", r.stderr)

    def test_connection_and_locator_refused(self):
        self.assertEqual(self.cli("DIRECTION/START", "--connexions").returncode, 2)

    def test_connection_and_query_refused(self):
        self.assertEqual(self.cli("--trouver", "asset", "--connexions").returncode, 2)

    def test_connection_and_guides_refused(self):
        self.assertEqual(self.cli("--connexions", "--guides").returncode, 2)

    def test_blank_connection_refused(self):
        self.assertEqual(self.cli("--connexions", "  ").returncode, 2)


class SearchAndSummaryTests(unittest.TestCase):
    """Recherche par alias et mots entiers, classement, sommaire, sortie coupée (audit 2026-10-08)."""

    def cli(self, *args):
        return subprocess.run([sys.executable, str(ROOT / "scripts/read_route.py"), *args], capture_output=True, text=True)

    def test_cut_output_is_silent(self):
        proc = subprocess.Popen([sys.executable, str(ROOT / "scripts/read_route.py"), "--trouver", "composant", "--tout"],
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        proc.stdout.close()  # lecteur parti avant la première écriture, comme « | head »
        err = proc.stderr.read(); proc.wait()
        self.assertEqual(proc.returncode, 0, err)
        self.assertNotIn("Traceback", err)
        self.assertNotIn("Broken pipe", err)

    def test_alias_reaches_canonical_term(self):
        r = self.cli("--trouver", "premier écran")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("alias : premier contact", r.stdout)
        self.assertIn("SAVOIR/CRAFT", r.stdout)
        self.assertIn("ACTION/UI-UX-REALITY", self.cli("--trouver", "désactivé").stdout)

    def test_every_alias_group_reaches_sources(self):
        for group in reader.ALIAS_GROUPS:
            self.assertTrue(reader.search(group[0])[2], f"groupe d'alias sans occurrence : {group}")

    def test_whole_words_before_partial_match(self):
        mode, _, results = reader.search("age")
        self.assertEqual(mode, "mots entiers")
        for _, _, _, line in results:
            self.assertRegex(reader._fold(line), r"(?<![a-z0-9])age")

    def test_separate_words_fallback(self):
        mode, words, results = reader.search("image texte")
        self.assertEqual(mode, "mots séparés sur une même ligne")
        self.assertEqual(words, ["image", "texte"])
        self.assertIn("SAVOIR/CRAFT", {r[0] for r in results})

    def test_defining_route_ranked_first(self):
        routes = [l.split()[0] for l in self.cli("--trouver", "COHERENCE DE RAYON").stdout.splitlines() if l.startswith(("SAVOIR/", "ACTION/"))]
        self.assertEqual(routes[0], "SAVOIR/STATE")

    def test_top_routes_then_all(self):
        short, full = self.cli("--trouver", "composant").stdout, self.cli("--trouver", "composant", "--tout").stdout
        count = lambda out: sum(1 for l in out.splitlines() if l.split(" ")[0].count("/") >= 1 and "ligne(s)" in l)
        self.assertEqual(count(short), reader.TOP_ROUTES)
        self.assertIn("ajouter --tout", short)
        self.assertGreater(count(full), reader.TOP_ROUTES)

    def test_summary_lists_every_route(self):
        out = self.cli("--sommaire").stdout
        for prefix in ("DIRECTION", "ACTION", "SAVOIR", "BIBLIOTHEQUE"):
            lines = (reader.OFFICIAL / f"{prefix}.md").read_text(encoding="utf-8").splitlines()
            for _, _, text in reader.headings(lines):
                locator = reader.heading_locator(text)
                if locator:
                    self.assertIn(f"\n{locator} ", out)

    def test_route_outline_gives_readable_sublocators(self):
        rows = reader.outline("SAVOIR/CRAFT")
        subs = [sub for _, _, sub, _ in rows if sub]
        self.assertIn("SAVOIR/CRAFT/CFT-05", subs)
        self.assertIn("SUPPORT/FREE_FIELD", [s for _, _, s, _ in reader.outline("BIBLIOTHEQUE/SUPPORT") if s])
        for sub in subs:
            self.assertEqual(self.cli(sub).returncode, 0, sub)

    def test_new_options_refused_in_bad_combinations(self):
        self.assertEqual(self.cli("--tout").returncode, 2)
        self.assertEqual(self.cli("DIRECTION/START", "--sommaire").returncode, 2)
        r = self.cli("--sommaire", "NOPE/X")
        self.assertNotEqual(r.returncode, 0)
        self.assertNotIn("Traceback", r.stderr)


class ActivationTests(unittest.TestCase):
    def test_lookup_activation_cannot_disappear_from_compiled_core(self):
        source = (structure.SKILL_DIR / "SKILL.md").read_text(encoding="utf-8")
        with tempfile.TemporaryDirectory() as tmp:
            skill_dir = Path(tmp)
            (skill_dir / "SKILL.md").write_text(source.replace("python3 scripts/read_route.py --trouver", "commande retirée"), encoding="utf-8")
            with patch.object(structure, "SKILL_DIR", skill_dir):
                errors = []; structure.check_core_floor(errors)
            self.assertTrue(any("recherche conditionnelle" in e for e in errors))

    def test_lookup_limit_cannot_disappear_from_compiled_core(self):
        source = (structure.SKILL_DIR / "SKILL.md").read_text(encoding="utf-8")
        with tempfile.TemporaryDirectory() as tmp:
            skill_dir = Path(tmp)
            (skill_dir / "SKILL.md").write_text(source.replace("sans conclure à l’absence du savoir", "limite retirée"), encoding="utf-8")
            with patch.object(structure, "SKILL_DIR", skill_dir):
                errors = []; structure.check_core_floor(errors)
            self.assertTrue(any("limite de la recherche" in e for e in errors))


if __name__ == "__main__":
    result = unittest.TextTestRunner(stream=sys.stdout).run(unittest.defaultTestLoader.loadTestsFromModule(sys.modules[__name__]))
    print(f"READ_ROUTE TESTS {'PASSED' if result.wasSuccessful() else 'FAILED'} — {result.testsRun} cas")
    sys.exit(0 if result.wasSuccessful() else 1)
