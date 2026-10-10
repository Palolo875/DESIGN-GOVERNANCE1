#!/usr/bin/env python3
"""Régressions du budget : fichier complet, seuil, octets UTF-8 et refus sans écriture."""
from __future__ import annotations

import contextlib
import io
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import build_core as bc
import read_route as rr
import validate_structure as structure


class BudgetTests(unittest.TestCase):
    def test_below_limit_accepted(self):
        self.assertEqual(bc.check_budget(b"x" * 45_999), 45_999)

    def test_exact_limit_accepted(self):
        self.assertEqual(bc.check_budget(b"x" * 46_000), 46_000)

    def test_one_byte_over_limit_refused(self):
        with self.assertRaisesRegex(bc.CoreError, "CORE BUDGET FAILED.*46001"):
            bc.check_budget(b"x" * 46_001)

    def test_utf8_bytes_counted_instead_of_characters(self):
        text = "é" * 23_001
        self.assertLess(len(text), 46_000)
        with self.assertRaisesRegex(bc.CoreError, "46002 octets UTF-8"):
            bc.check_budget(text.encode("utf-8"))

    def test_complete_file_includes_content_outside_generated_section(self):
        text = bc.BEGIN + "\npetit noyau\n" + bc.END
        raw = text.encode() + b"x" * (46_001 - len(text.encode()))
        with self.assertRaises(bc.CoreError):
            bc.check_budget(raw)

    def test_structural_validation_refuses_both_layouts(self):
        with tempfile.TemporaryDirectory() as tmp:
            for layout in ("agent/skill/SKILL.md", "skill/SKILL.md"):
                with self.subTest(layout=layout):
                    skill = Path(tmp) / layout
                    skill.parent.mkdir(parents=True, exist_ok=True)
                    skill.write_bytes(b"x" * 46_001)
                    with patch.object(bc, "SKILL", skill):
                        errors = []
                        structure.check_noyau({}, errors)
                    self.assertTrue(any("CORE BUDGET FAILED" in e for e in errors), errors)

    def test_oversized_compilation_preserves_previous_skill(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill = Path(tmp) / "SKILL.md"
            before = bc.BEGIN + "\nancien\n" + bc.END
            skill.write_bytes(before.encode())
            with patch.object(bc, "SKILL", skill), patch.object(bc, "compile_core", return_value="x" * 46_001), patch.object(rr, "non_utf8", return_value=[]), patch.object(sys, "argv", ["build_core.py"]), contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(bc.main(), 1)
            self.assertEqual(skill.read_bytes(), before.encode())

    def test_check_refuses_oversized_file_without_rewriting(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill = Path(tmp) / "SKILL.md"
            text = bc.BEGIN + "\nx\n" + bc.END
            raw = text.encode() + b"x" * (46_001 - len(text.encode()))
            skill.write_bytes(raw)
            with patch.object(bc, "SKILL", skill), patch.object(bc, "compile_core", return_value="x\n"), patch.object(rr, "non_utf8", return_value=[]), patch.object(sys, "argv", ["build_core.py", "--check"]), contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(bc.main(), 1)
            self.assertEqual(skill.read_bytes(), raw)

    def test_missing_skill_is_governed_failure(self):
        with tempfile.TemporaryDirectory() as tmp:
            output = io.StringIO()
            with patch.object(bc, "SKILL", Path(tmp) / "absent.md"), patch.object(rr, "non_utf8", return_value=[]), patch.object(sys, "argv", ["build_core.py", "--check"]), contextlib.redirect_stdout(output):
                self.assertEqual(bc.main(), 1)
            self.assertIn("NOYAU : erreur", output.getvalue())

    def test_unknown_option_cannot_compile_or_write(self):
        with patch.object(sys, "argv", ["build_core.py", "--inconnu"]), patch.object(bc, "compile_core") as compile_core, contextlib.redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit) as result:
                bc.main()
            self.assertEqual(result.exception.code, 2)
            compile_core.assert_not_called()


class DeferredKnowledgeTests(unittest.TestCase):
    def test_current_registry_compiles_and_serves_all_details(self):
        compiled = bc.compile_core()
        self.assertIn("python3 scripts/read_route.py --mode MODE", compiled)
        self.assertNotIn("| Cohérence de rayon |", compiled)

    def test_missing_deferred_block_cannot_compile(self):
        real = bc.blocks_of_source

        def missing(fname):
            blocks = real(fname)
            blocks.pop("COMP-VOCABULAIRE", None)
            return blocks

        with patch.object(bc, "blocks_of_source", side_effect=missing):
            with self.assertRaisesRegex(bc.CoreError, "bloc COMP-VOCABULAIRE absent"):
                bc.compile_core()

    def test_existing_wrong_route_cannot_hide_deferred_knowledge(self):
        with patch.dict(bc.DETAILS, {"COMP-VOCABULAIRE": "SAVOIR/TYPE"}):
            with self.assertRaisesRegex(bc.CoreError, "COMP-VOCABULAIRE.*bloc complet"):
                bc.compile_core()

    def test_missing_deferred_route_cannot_compile(self):
        with patch.dict(bc.DETAILS, {"COMP-VOCABULAIRE": "SAVOIR/ABSENT"}):
            with self.assertRaisesRegex(bc.CoreError, "COMP-VOCABULAIRE.*indisponible"):
                bc.compile_core()

    def test_unclassified_block_cannot_disappear(self):
        with patch.object(bc, "COMMUN", bc.COMMUN - {"ROLE"}):
            with self.assertRaisesRegex(bc.CoreError, "chaque bloc"):
                bc.compile_core()

    def test_block_cannot_be_both_common_and_deferred(self):
        with patch.dict(bc.DETAILS, {"ROLE": "DIRECTION/START"}):
            with self.assertRaisesRegex(bc.CoreError, "chaque bloc"):
                bc.compile_core()

    def test_removing_block_from_both_registries_does_not_orphan_source(self):
        registry = [(title, [item for item in items if item[0] != "COMP-VOCABULAIRE"])
                    for title, items in bc.NOYAU]
        details = {key: value for key, value in bc.DETAILS.items() if key != "COMP-VOCABULAIRE"}
        with patch.object(bc, "NOYAU", registry), patch.object(bc, "DETAILS", details):
            with self.assertRaisesRegex(bc.CoreError, "bloc source non classé.*COMP-VOCABULAIRE"):
                bc.compile_core()

    def test_readable_detail_without_activation_cannot_compile(self):
        real = bc.blocks_of_source
        original_extract = rr.extract

        def without_relay(fname):
            return {bid: [line.replace("`SAVOIR/INTEGRITY/REPASSE`", "renvoi supprimé") for line in body]
                    for bid, body in real(fname).items()}

        with patch.object(bc, "blocks_of_source", side_effect=without_relay):
            def without_charge_relay(lines, index):
                body = original_extract(lines, index)
                return [line.replace("`SAVOIR/INTEGRITY/REPASSE`", "renvoi supprimé") for line in body] \
                    if lines[index].startswith("## DIRECTION/CHARGE") else body

            with patch.object(rr, "extract", side_effect=without_charge_relay):
                with self.assertRaisesRegex(bc.CoreError, "BOUCLE-REPASSE.*renvoi.*absent"):
                    bc.compile_core()


if __name__ == "__main__":
    result = unittest.TextTestRunner(stream=sys.stdout).run(unittest.defaultTestLoader.loadTestsFromModule(sys.modules[__name__]))
    print(f"CORE BUDGET TESTS {'PASSED' if result.wasSuccessful() else 'FAILED'} — {result.testsRun} cas")
    sys.exit(0 if result.wasSuccessful() else 1)
