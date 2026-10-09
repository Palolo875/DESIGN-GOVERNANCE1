#!/usr/bin/env python3
"""Régressions de préparation : périmètre, limites visibles, journaux et restauration exacte.

Les sous-processus de validation sont simulés pour tester l'orchestration sans relancer validate_all
récursivement. Les copies et leur script de restauration sont réellement exécutés.
"""
from __future__ import annotations

import contextlib
import io
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path
from unittest.mock import patch

import preparer_livraison as prep
import build_core as bc
import validate_design_governance as package_validator


class CopyTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.archive = self.root / "fixture.zip"
        self.content = {"README.md": b"Fichier fiable.\n", "scripts/utf8.py": 'print("écriture")\r\n# ``` et ````\r\n'.encode(), "empty.json": b""}
        with zipfile.ZipFile(self.archive, "w") as z:
            for name, raw in self.content.items():
                z.writestr(name, raw)

    def tearDown(self):
        self.tmp.cleanup()

    def restore(self, text, optimized=False):
        source = self.root / "copy.md"; source.write_text(text, encoding="utf-8", newline="")
        script = self.root / "restore.py"; script.write_text(prep.RESTORE, encoding="utf-8")
        out = self.root / "restored"
        result = subprocess.run([sys.executable, *(["-O"] if optimized else []), str(script), str(source), str(out)], capture_output=True, text=True)
        return result, out

    def test_exact_bytes_with_utf8_crlf_empty_file_and_fences(self):
        r, out = self.restore(prep.markdown_copy(self.archive, False))
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual({str(p.relative_to(out)): p.read_bytes() for p in out.rglob("*") if p.is_file()}, self.content)

    def test_docs_copy_excludes_code(self):
        r, out = self.restore(prep.markdown_copy(self.archive, True))
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual([p.name for p in out.iterdir()], ["README.md"])

    def test_corruption_refused_before_writing(self):
        text = prep.markdown_copy(self.archive, False).replace("Fichier fiable.", "Contenu changé.")
        r, out = self.restore(text)
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("empreinte divergente", r.stderr)
        self.assertFalse(out.exists())

    def test_corruption_still_refused_with_python_optimized(self):
        text = prep.markdown_copy(self.archive, False).replace("Fichier fiable.", "Contenu changé.")
        r, out = self.restore(text, optimized=True)
        self.assertNotEqual(r.returncode, 0)
        self.assertFalse(out.exists())

    def test_incomplete_inventory_refused(self):
        text = prep.markdown_copy(self.archive, False)
        text = text[:text.rfind("\n---\n")]
        r, out = self.restore(text)
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("inventaire incomplet", r.stderr)
        self.assertFalse(out.exists())

    def test_duplicate_path_refused(self):
        text = prep.markdown_copy(self.archive, False).replace("BEGIN FILE empty.json", "BEGIN FILE README.md")
        r, out = self.restore(text)
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("chemin incorrect ou répété", r.stderr)
        self.assertFalse(out.exists())

    def test_path_outside_destination_refused(self):
        text = prep.markdown_copy(self.archive, False).replace("BEGIN FILE empty.json", "BEGIN FILE ../outside.json")
        r, out = self.restore(text)
        self.assertNotEqual(r.returncode, 0)
        self.assertFalse(out.exists())
        self.assertFalse((self.root / "outside.json").exists())

    def test_noncanonical_paths_refused_before_any_write(self):
        for alias in ('./README.md', 'scripts/../README.md', 'scripts//utf8.py', 'scripts/./utf8.py', '.', '/absolute.json'):
            with self.subTest(alias=alias):
                text = prep.markdown_copy(self.archive, False).replace('BEGIN FILE empty.json', 'BEGIN FILE ' + alias)
                r, out = self.restore(text)
                self.assertNotEqual(r.returncode, 0)
                self.assertFalse(out.exists())

    def test_file_directory_collision_refused_in_both_orders(self):
        for names in (('a', 'a/b'), ('a/b', 'a')):
            with self.subTest(names=names):
                text = prep.markdown_copy(self.archive, False).replace('BEGIN FILE README.md', 'BEGIN FILE ' + names[0]).replace('BEGIN FILE empty.json', 'BEGIN FILE ' + names[1])
                r, out = self.restore(text)
                self.assertNotEqual(r.returncode, 0)
                self.assertIn('collision', r.stderr)
                self.assertFalse(out.exists())

    def test_existing_directory_or_parent_file_refused_before_writing(self):
        for name, directory in [('README.md', True), ('scripts', False)]:
            with self.subTest(name=name):
                out = self.root / 'restored'; out.mkdir(exist_ok=True)
                incompatible = out / name
                if directory:
                    incompatible.mkdir()
                else:
                    incompatible.write_bytes(b'conserver')
                r, _ = self.restore(prep.markdown_copy(self.archive, False))
                self.assertNotEqual(r.returncode, 0)
                self.assertEqual(sorted(p.name for p in out.iterdir()), [name])
                if directory:
                    incompatible.rmdir()
                else:
                    self.assertEqual(incompatible.read_bytes(), b'conserver'); incompatible.unlink()
                out.rmdir()

    def test_symlink_alias_and_escape_refused_before_writing(self):
        for target in ('README.md', '../outside.json'):
            with self.subTest(target=target):
                out = self.root / 'restored'; out.mkdir()
                alias = out / 'empty.json'; alias.symlink_to(target)
                r, _ = self.restore(prep.markdown_copy(self.archive, False))
                self.assertNotEqual(r.returncode, 0)
                self.assertEqual([p.name for p in out.iterdir()], ['empty.json'])
                self.assertFalse((self.root / 'outside.json').exists())
                alias.unlink(); out.rmdir()

    def test_nonempty_or_linked_destination_refused_empty_accepted(self):
        out = self.root / 'restored'; out.mkdir()
        (out / 'README.md').write_bytes(b'conserver'); (out / 'hors_inventaire.txt').write_bytes(b'garder')
        r, _ = self.restore(prep.markdown_copy(self.archive, False))
        self.assertNotEqual(r.returncode, 0)
        self.assertIn('dossier vide', r.stderr)
        self.assertEqual((out / 'README.md').read_bytes(), b'conserver')
        shutil.rmtree(out)
        real = self.root / 'real'; real.mkdir(); out.symlink_to(real)
        r, _ = self.restore(prep.markdown_copy(self.archive, False))
        self.assertNotEqual(r.returncode, 0)
        self.assertEqual(list(real.iterdir()), [])
        out.unlink(); out.mkdir()
        r, _ = self.restore(prep.markdown_copy(self.archive, False))
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual({str(p.relative_to(out)): p.read_bytes() for p in out.rglob('*') if p.is_file()}, self.content)

    def test_verify_uses_embedded_restorer_for_both_copies(self):
        for docs in (False, True):
            copy = self.root / "verify.md"; copy.write_text(prep.markdown_copy(self.archive, docs), encoding="utf-8", newline="")
            prep.verify(copy, self.archive, docs)


class PreparationTests(unittest.TestCase):
    def test_existing_lock_owner_preserved_and_diagnosed(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); scripts = root / 'scripts'; scripts.mkdir()
            shutil.copyfile(prep.ROOT / 'scripts/build_distributions.sh', scripts / 'build_distributions.sh')
            lock = root / '.distribution.lock'; lock.mkdir()
            owner = 'pid=42\nstarted_utc=2026-10-04T08:00:00Z\nroot=' + str(root) + '\n'
            (lock / 'owner.txt').write_text(owner)
            result = subprocess.run(['bash', str(scripts / 'build_distributions.sh')], capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn(owner, result.stderr)
            self.assertIn('Reprendre une préparation interrompue', result.stderr)
            self.assertEqual((lock / 'owner.txt').read_text(), owner)
            self.assertEqual(sorted(p.name for p in root.iterdir()), ['.distribution.lock', 'scripts'])

    def test_checkout_metadata_and_logs_excluded_only_at_root(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); (root / "README.md").write_text("source")
            for folder in (".git", ".logs", ".distribution.lock"):
                (root / folder).mkdir(); (root / folder / "local.txt").touch()
            with patch.object(package_validator, "ROOT", root), patch.object(package_validator, "EXPECTED", ["README.md"]):
                errors = []; package_validator.check_expected_files(errors)
                self.assertEqual(errors, [])
                nested = root / "scripts/.git"; nested.mkdir(parents=True); (nested / "leak.txt").touch()
                errors = []; package_validator.check_expected_files(errors)
                self.assertTrue(any("scripts/.git/leak.txt" in error for error in errors))

    def test_agent_install_folder_is_not_part_of_the_package(self):
        # Le README propose de copier la skill dans .claude/skills/ du projet, qui peut être le dossier du package.
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); (root / "README.md").write_text("source")
            installed = root / ".claude/skills/design-governance-practice"; installed.mkdir(parents=True)
            (installed / "SKILL.md").write_text("[lien](../../V1/official/ABSENT.md)\n")
            with patch.object(package_validator, "ROOT", root), patch.object(package_validator, "EXPECTED", ["README.md"]):
                errors = []; package_validator.check_expected_files(errors)
                self.assertEqual(errors, [])
                self.assertFalse(package_validator.in_package(installed / "SKILL.md"))
                nested = root / "scripts/.claude"; nested.mkdir(parents=True); (nested / "leak.txt").touch()
                errors = []; package_validator.check_expected_files(errors)
                self.assertTrue(any("scripts/.claude/leak.txt" in error for error in errors))

    def test_success_keeps_limit_visible_and_complete_log(self):
        with tempfile.TemporaryDirectory() as tmp:
            journal = Path(tmp) / "audit.log"
            done = subprocess.CompletedProcess([], 0, "détail conservé\n  NOT-VERIFIED : Playwright absent\nCHECK_RENDER TESTS PASSED — A : 19 cas ; B : NOT-VERIFIED\n", "")
            output = io.StringIO()
            with patch.object(prep.subprocess, "run", return_value=done), contextlib.redirect_stdout(output):
                prep.step("contrôles", ["python", "validate_all.py"], journal)
            self.assertIn("NOT-VERIFIED", output.getvalue())
            self.assertNotIn("détail conservé", output.getvalue())
            self.assertIn("détail conservé", journal.read_text())

    def test_failed_step_stops_with_log(self):
        with tempfile.TemporaryDirectory() as tmp:
            journal = Path(tmp) / "audit.log"
            done = subprocess.CompletedProcess([], 1, "échec documenté", "raison du contrôle")
            with patch.object(prep.subprocess, "run", return_value=done), contextlib.redirect_stdout(io.StringIO()):
                with self.assertRaisesRegex(SystemExit, "PRÉPARATION ÉCHOUÉE"):
                    prep.step("contrôles", ["python"], journal)
            self.assertIn("raison du contrôle", journal.read_text())

    def test_local_rejected_before_compilation_or_writes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            with patch.object(prep, "ROOT", root), patch.object(prep, "step") as step, patch.object(sys, "argv", ["preparer_livraison.py"]):
                with self.assertRaisesRegex(SystemExit, "distribution GitHub"):
                    prep.main()
                step.assert_not_called()
            self.assertEqual(list(root.iterdir()), [])

    def test_browser_requirement_reaches_validation_command(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); (root / "scripts").mkdir(); (root / "scripts/build_distributions.sh").touch()
            (root / "V1/official").mkdir(parents=True)
            for name in prep.ARCHIVES:
                (root / name).touch()
            journal = root / "audit.log"
            with patch.object(prep, "ROOT", root), patch.object(prep, "step") as step, patch.object(sys, "argv", ["preparer_livraison.py", "--require-browser", "--log", str(journal)]), contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(prep.main(), 0)
                self.assertIn("--require-browser", step.call_args_list[1].args[1])

    def test_log_and_journal_aliases_prepare_the_same_log(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); (root / "scripts").mkdir()
            (root / "scripts/build_distributions.sh").touch()
            (root / "V1/official").mkdir(parents=True)
            for name in prep.ARCHIVES:
                (root / name).touch()
            log = root / "audit.log"
            contents = []
            for option in ("--log", "--journal"):
                with self.subTest(option=option), patch.object(prep, "ROOT", root), patch.object(prep, "step") as step, patch.object(sys, "argv", ["preparer_livraison.py", option, str(log)]), contextlib.redirect_stdout(io.StringIO()):
                    self.assertEqual(prep.main(), 0)
                    self.assertEqual(step.call_args_list[0].args[2], log)
                    self.assertEqual(step.call_args_list[1].args[2], log)
                contents.append(log.read_bytes())
            self.assertEqual(contents[0], contents[1])

    def test_direct_build_refuses_canonical_overflow_and_preserves_archives(self):
        # Le build refuse une skill qui dépasse le budget de 46 000 octets, sans toucher aux archives en place.
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            manifest = json.loads((prep.ROOT / "scripts/package_manifest.json").read_text())
            for name in manifest["github"]:
                path = root / name; path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes((prep.ROOT / name).read_bytes())
            # Le bloc CHARGE-REGLE est cherché là où il vit aujourd’hui (rangement : il a pu changer de fichier).
            source = next(root / n for n in manifest["github"] if n.endswith(".md") and "<!-- noyau:fin CHARGE-REGLE -->" in (root / n).read_text())
            skill = root / "agent/skill/SKILL.md"
            extra = 46_001 - skill.stat().st_size
            self.assertGreater(extra, 2)
            source.write_text(source.read_text().replace("<!-- noyau:fin CHARGE-REGLE -->", "x" * (extra - 2) + "\n\n<!-- noyau:fin CHARGE-REGLE -->", 1))
            with patch.object(bc, "OFFICIAL", root / "V1/official"), patch.object(bc, "ROOT", root):
                skill.write_bytes(bc.render(skill.read_text(), bc.compile_core()).encode())
            self.assertEqual(skill.stat().st_size, 46_001)
            for name in prep.ARCHIVES:
                (root / name).write_bytes(b"archive precedente")
            (root / "dist").mkdir(); (root / "dist/previous.txt").write_bytes(b"export precedent")
            before_skill = skill.read_bytes()
            result = subprocess.run(["bash", "scripts/build_distributions.sh"], cwd=root, capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("CORE BUDGET FAILED", result.stdout + result.stderr)
            self.assertNotIn("Traceback", result.stdout + result.stderr)
            self.assertEqual(skill.read_bytes(), before_skill)
            self.assertEqual((root / "dist/previous.txt").read_bytes(), b"export precedent")
            for name in prep.ARCHIVES:
                self.assertEqual((root / name).read_bytes(), b"archive precedente")
            self.assertFalse((root / ".build").exists())
            self.assertFalse((root / ".distribution.lock").exists())


if __name__ == "__main__":
    result = unittest.TextTestRunner(stream=sys.stdout).run(unittest.defaultTestLoader.loadTestsFromModule(sys.modules[__name__]))
    print(f"PREPARATION TESTS {'PASSED' if result.wasSuccessful() else 'FAILED'} — {result.testsRun} cas")
    sys.exit(0 if result.wasSuccessful() else 1)
