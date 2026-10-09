#!/usr/bin/env python3
"""Orchestre les contrôles de cohérence, de projection et de distribution."""
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def run(command: list[str]) -> None:
    print("+", " ".join(command))
    subprocess.run(command, cwd=ROOT, check=True)

def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()

def expect_failure(command: list[str], label: str, expected_message: str) -> None:
    """Vérifie qu’un scénario d’entrée invalide échoue réellement, et pour le motif attendu."""
    target = next((Path(part) for part in command if part.endswith(".json")), None)
    if target is not None and not target.is_absolute():
        target = ROOT / target  # chemins résolus depuis ROOT, jamais depuis le dossier courant
    if target is not None and not target.is_file() and label not in {"fichier absent", "JSON malformé"}:
        raise SystemExit(f"CLI REGRESSION FAILED — {label} : fixture absente : {target}")
    result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True)
    if result.returncode == 0:
        output = (result.stdout + result.stderr).strip()
        raise SystemExit(f"CLI REGRESSION FAILED — {label} a réussi à tort : {output}")
    output = result.stdout + result.stderr
    if "Traceback (most recent call last)" in output:
        raise SystemExit(f"CLI REGRESSION FAILED — {label} a échoué par exception non gouvernée")
    if expected_message not in output:
        raise SystemExit(f"CLI REGRESSION FAILED — {label} a échoué pour un autre motif : attendu {expected_message!r}")
    print(f"+ expected failure ({label})")

def check_craft_regressions() -> None:
    """Exerce les défauts réellement corrigés, sans modifier les sources livrées.

    Ces mutations contrôlent l'activation et ses garde-fous documentaires ;
    elles ne mesurent ni le goût ni l'effet perceptuel d'un geste.
    """
    sys.path.insert(0, str(ROOT / "scripts"))
    import validate_reading_map as reading_map

    baseline = reading_map.load_texts()
    if not reading_map.lcf_46(baseline):
        raise SystemExit("CRAFT REGRESSION FAILED — LCF-46 baseline invalide")
    for line in (
        "Le détourage porte un halo clair sur le fond réel.",
        "Comparer la séparation du bord sans halo.",
    ):
        case = dict(baseline)
        case["S"] += "\n" + line
        if not reading_map.lcf_46(case):
            raise SystemExit("CRAFT REGRESSION FAILED — défaut de production confondu avec une vague")
    for line in ("Ajouter des halos décoratifs à la scène.", "Des halos lumineux entourent les cartes.",
                 "Un halo violet derrière le titre."):
        case = dict(baseline)
        case["S"] += "\n" + line + "\n"
        if reading_map.lcf_46(case):
            raise SystemExit("CRAFT REGRESSION FAILED — marqueur de vague non daté accepté : " + line)

    with tempfile.TemporaryDirectory(prefix="design-governance-craft-") as temp_dir:
        for name, change, expected in (
            (
                "wrong_owner",
                lambda s: s.replace("vocabulaire perceptuel de `SAVOIR/STATE`",
                                    "vocabulaire perceptuel de `SAVOIR/CRAFT`", 1),
                "renvoi SAVOIR/CRAFT/CFT-00 → FIN-01",
            ),
            (
                "closed_gestures",
                lambda s: s.replace("Les gestes proposés sont des points de départ, pas une liste fermée",
                                    "Le geste retenu est l’un de ses diffs", 1),
                "vocabulaire retiré",
            ),
            (
                "missing_activation",
                lambda s: s.replace("<!-- concept:FIN-01 -->", "", 1),
                "FIN-01",
            ),
        ):
            case_root = Path(temp_dir) / name
            shutil.copytree(ROOT, case_root, ignore=shutil.ignore_patterns(
                ".git", ".build", "dist", "__pycache__", "*.zip"))
            # Le texte visé est cherché dans les fichiers qui portent SAVOIR aujourd'hui (table LIEUX du lecteur).
            for candidate in reading_map.rr.lieu("SAVOIR.md"):
                source = case_root / candidate.relative_to(ROOT)
                before = source.read_text(encoding="utf-8")
                after = change(before)
                if before != after:
                    break
            else:
                raise SystemExit(f"CRAFT REGRESSION FAILED — mutation {name} non exercée")
            source.write_text(after, encoding="utf-8")
            subprocess.run([sys.executable, "scripts/build_core.py"], cwd=case_root,
                           check=True, capture_output=True, text=True)
            result = subprocess.run([sys.executable, "scripts/validate_structure.py"],
                                    cwd=case_root, capture_output=True, text=True)
            output = result.stdout + result.stderr
            if result.returncode == 0 or expected not in output or "Traceback" in output:
                raise SystemExit(f"CRAFT REGRESSION FAILED — mutation {name} non détectée pour le motif attendu")
    print("CRAFT REGRESSIONS PASSED — 2 cas de halo de production admis, 3 marqueurs de vague non datés et 3 mutations d’activation rejetés")

def check_move_regression() -> None:
    """Le rangement déplace du texte et met à jour la seule table LIEUX : lecteur, noyau et validateurs suivent.

    Sur une copie, la route SAVOIR/TYPE (avec un bloc du noyau) part dans un nouveau fichier ; tout doit rester vert,
    la skill compilée doit rester identique et la route doit être servie depuis son nouveau lieu.
    Sans la mise à jour de LIEUX, le même déplacement doit échouer.
    """
    sys.path.insert(0, str(ROOT / "scripts"))
    import read_route as rr
    savoir = rr.lieu("SAVOIR.md")
    if len(savoir) != 1:
        print("MOVE REGRESSION SKIPPED — SAVOIR déjà réparti sur plusieurs fichiers ; le rangement réel en tient lieu")
        return
    import build_core as bc
    rel = savoir[0].relative_to(ROOT).as_posix()
    skill_rel = bc.SKILL.relative_to(ROOT)
    layout = "local" if rel.startswith("official/") else "github"  # export Local ou distribution GitHub
    target = "design/savoir/typographie-essai.md"
    with tempfile.TemporaryDirectory(prefix="design-governance-move-") as temp_dir:
        for with_table, duplicate in ((True, False), (False, False), (True, True)):
            case = Path(temp_dir) / ("avec-lieux" if with_table else "sans-lieux") / ("doublon" if duplicate else "simple")
            case.parent.mkdir(parents=True, exist_ok=True)
            shutil.copytree(ROOT, case, ignore=shutil.ignore_patterns(".git", ".build", "dist", "__pycache__", "*.zip"))
            text = (case / rel).read_text(encoding="utf-8")
            start, end = text.find("\n# SAVOIR/TYPE"), text.find("\n# SAVOIR/STATE")
            if start < 0 or end < start:
                raise SystemExit("MOVE REGRESSION FAILED — section SAVOIR/TYPE introuvable")
            (case / target).parent.mkdir(parents=True)
            (case / target).write_text(text[start + 1:end + 1], encoding="utf-8")
            remaining = text[:start + 1] + text[end + 1:]
            if duplicate:  # le même locator porté par deux fichiers de la source doit être refusé
                remaining += "\n# SAVOIR/TYPE — doublon\n\nTexte.\n"
            (case / rel).write_text(remaining, encoding="utf-8")
            manifest = case / "scripts/package_manifest.json"
            data = json.loads(manifest.read_text(encoding="utf-8"))
            data[layout].append(target)
            manifest.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
            if with_table:
                reader = case / "scripts/read_route.py"
                src = reader.read_text(encoding="utf-8")
                anchor = "\ndef chemin_lieu("
                if src.count(anchor) != 1:
                    raise SystemExit("MOVE REGRESSION FAILED — table LIEUX introuvable dans read_route.py")
                reader.write_text(src.replace(anchor, f"\nLIEUX['SAVOIR.md'] = ({rel!r}, {target!r})\n{anchor}"),
                                  encoding="utf-8")
            skill_before = (ROOT / skill_rel).read_bytes()
            steps = [[sys.executable, "scripts/build_core.py", "--check"],
                     [sys.executable, "scripts/validate_structure.py"],
                     [sys.executable, "scripts/validate_reading_map.py"],
                     [sys.executable, "scripts/validate_design_governance.py"],
                     [sys.executable, "scripts/read_route.py", "SAVOIR/TYPE"]]
            results = [subprocess.run(s, cwd=case, capture_output=True, text=True) for s in steps]
            failed = [" ".join(s[1:]) for s, r in zip(steps, results) if r.returncode != 0 or "Traceback" in r.stdout + r.stderr]
            if duplicate:
                if "scripts/validate_reading_map.py" not in failed:
                    raise SystemExit("MOVE REGRESSION FAILED — un locator porté par deux fichiers de la même source n'est pas refusé")
            elif with_table:
                if failed:
                    raise SystemExit(f"MOVE REGRESSION FAILED — après déplacement et mise à jour de LIEUX : {', '.join(failed)}")
                if f"OWNER: {target}" not in results[-1].stdout:
                    raise SystemExit("MOVE REGRESSION FAILED — SAVOIR/TYPE n'est pas servie depuis son nouveau lieu")
                if (case / skill_rel).read_bytes() != skill_before:
                    raise SystemExit("MOVE REGRESSION FAILED — la skill a changé")
            elif not failed:
                raise SystemExit("MOVE REGRESSION FAILED — un déplacement sans mise à jour de LIEUX passe inaperçu")
    print("MOVE REGRESSION PASSED — route déplacée avec son bloc de noyau : lecteur, noyau et validateurs suivent la table LIEUX ; "
          "sans elle, le déplacement est détecté ; un locator porté par deux fichiers est refusé")


def build_outputs() -> dict[str, tuple[int, int]]:
    """Empreinte (date, taille) des sorties du build : dist/, .build/ et archives à la racine."""
    paths = [p for d in ("dist", ".build") for p in (ROOT / d).rglob("*") if p.is_file()]
    paths += sorted(ROOT.glob("Design_Governance_V1_*.zip"))
    return {p.relative_to(ROOT).as_posix(): (p.stat().st_mtime_ns, p.stat().st_size) for p in paths}

def main() -> int:
    parser = argparse.ArgumentParser(description="Contrôler le package et ses distributions ; les tests navigateur restent explicitement non vérifiés s’ils sont indisponibles.")
    parser.add_argument("--require-browser", action="store_true", help="exiger l’exécution des tests navigateur, sinon échouer")
    parser.add_argument("--lecture-seule", action="store_true", help="tout contrôler sans construire : ni dist/ ni archives ne sont écrits ; build et reproductibilité restent non vérifiés")
    args = parser.parse_args()
    before = build_outputs() if args.lecture_seule else None
    scripts = sorted(p.relative_to(ROOT).as_posix() for p in (ROOT / "scripts").glob("*.py"))
    run([sys.executable, "-m", "py_compile", *scripts])
    run([sys.executable, "scripts/build_core.py", "--check"])
    run([sys.executable, "scripts/validate_design_governance.py"])
    run([sys.executable, "scripts/validate_run_card.py"])
    run([sys.executable, "scripts/validate_contracts.py"])
    run([sys.executable, "scripts/validate_reading_map.py"])
    run([sys.executable, "scripts/validate_structure.py"])
    check_craft_regressions()
    check_move_regression()
    run([sys.executable, "scripts/test_core_budget.py"])
    run([sys.executable, "scripts/test_read_route.py"])
    run([sys.executable, "scripts/test_audit_regressions.py"])
    if (ROOT / "scripts/test_preparer_livraison.py").is_file():
        run([sys.executable, "scripts/test_preparer_livraison.py"])
    run([sys.executable, "scripts/test_check_render.py", *(["--require-browser"] if args.require_browser else [])])
    run([sys.executable, "scripts/read_route.py", "DIRECTION/START"])
    found = subprocess.run([sys.executable, "scripts/read_route.py", "--trouver", "Cohérence de rayon"], cwd=ROOT, capture_output=True, text=True)
    if found.returncode != 0 or "SAVOIR/STATE" not in found.stdout:
        raise SystemExit("FINDABILITY FAILED — « Cohérence de rayon » ne mène plus à SAVOIR/STATE")
    print("FINDABILITY PASSED — read_route --trouver relie un terme à sa route")
    expect_failure(
        [sys.executable, "scripts/read_route.py", "DIRECTION/UNKNOWN"],
        "locator inconnu",
        "locator inconnu : DIRECTION/UNKNOWN",
    )
    run([sys.executable, "scripts/validate_contracts.py", "schemas/examples/domain_frame.example.json"])
    run([sys.executable, "scripts/validate_run_card.py", "schemas/run_card.example.json"])
    for fixture, motif in (
        ("invalid_capability_profile_missing_basis.json", "capability_profile exige basis non vide"),
        ("invalid_accepted_lost_in_build.json", "LOST-IN-BUILD ne peut pas produire un verdict accepté"),
        ("invalid_critical_without_protection.json", "un risque critical exige une critical_protection structurée"),
        ("invalid_critical_placeholder_protection.json", "critical_protection.control ne peut pas être un placeholder"),
    ):
        expect_failure(
            [sys.executable, "scripts/validate_run_card.py", f"schemas/fixtures/{fixture}"],
            fixture,
            motif,
        )
    with tempfile.TemporaryDirectory(prefix="design-governance-cli-") as temp_dir:
        temp = Path(temp_dir)
        strict_card = temp / "strict_card.json"
        strict_card.write_text((ROOT / "schemas/run_card.example.json").read_text(encoding="utf-8").replace("chemin-ou-url-local", (ROOT / "schemas/run_card.example.json").as_posix()).replace("ticket-ou-chemin-de-run", (ROOT / "schemas/run_card.example.json").as_posix()), encoding="utf-8")
        (temp / "captures").mkdir()
        (temp / "captures/premiere-scene-v1.png").write_bytes(b"")
        expect_failure(
            [sys.executable, "scripts/validate_run_card.py", "--strict", str(strict_card)],
            "strict capture B1b absente",
            "strict : capture B1b après local absent",
        )
        (temp / "captures/premiere-scene-v1-sans-objet.png").write_bytes(b"")
        run([sys.executable, "scripts/validate_run_card.py", "--strict", str(strict_card)])
        expect_failure(
            [sys.executable, "scripts/validate_run_card.py", "--strict", "schemas/run_card.example.json"],
            "strict placeholder",
            "strict : placeholder",
        )
        malformed = temp / "malformed.json"
        malformed.write_text('{"run_card":', encoding="utf-8")
        expect_failure(
            [sys.executable, "scripts/validate_run_card.py", str(malformed)],
            "JSON malformé",
            "lecture JSON impossible",
        )
        expect_failure(
            [sys.executable, "scripts/validate_run_card.py", str(temp / "missing.json")],
            "fichier absent",
            "lecture JSON impossible",
        )
    if args.lecture_seule:
        if build_outputs() != before:
            raise SystemExit("READ-ONLY FAILED — un contrôle a écrit dans dist/, .build/ ou les archives")
        print("READ-ONLY VALIDATION PASSED — contrôles exécutés sans écrire ; build et reproductibilité NOT-VERIFIED (relancer sans --lecture-seule)")
        return 0
    build_script = ROOT / "scripts/build_distributions.sh"
    if not build_script.is_file():
        print("LOCAL VALIDATION PASSED — contrôles documentaires, RUN_CARD et CLI ; build et reproductibilité hors périmètre de l’export Local")
        return 0
    run(["bash", "scripts/build_distributions.sh"])
    github = ROOT / "Design_Governance_V1_GITHUB.zip"
    local = ROOT / "Design_Governance_V1_LOCAL.zip"
    first = (sha256(github), sha256(local))
    run(["bash", "scripts/build_distributions.sh"])
    second = (sha256(github), sha256(local))
    if first != second:
        raise SystemExit("REPRODUCIBILITY FAILED — les archives diffèrent entre deux builds")
    print("FULL VALIDATION PASSED — package, RUN_CARD, build et reproductibilité")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
