#!/usr/bin/env python3
"""Préparer la livraison du paquet depuis sa distribution GitHub, sans envoi ni déploiement.

Par défaut, deux étapes, celles que le système exige :
  1. compiler le noyau de la skill (`scripts/build_core.py`) ;
  2. lancer la validation complète (`scripts/validate_all.py`) : contrôles documentaires, tests,
     construction des distributions GitHub et Local, reproductibilité.

Options, jamais requises :
  --empreintes        affiche l'empreinte sha256 des archives, pour un suivi tenu hors du paquet.
  --log CHEMIN        journal détaillé des étapes (défaut : .logs/preparer_livraison.log).
  --journal CHEMIN    alias compatible de --log.
  --require-browser   exiger l'exécution des tests navigateur, sinon échouer.

Codes de sortie : 0 livraison préparée ; 1 préparation échouée ; 2 arguments invalides.
Les limites des contrôles sont visibles même lorsqu'une étape réussit.
"""
from __future__ import annotations

import argparse
import hashlib
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARCHIVES = ("Design_Governance_V1_GITHUB.zip", "Design_Governance_V1_LOCAL.zip")

def step(title: str, command: list[str], journal: Path) -> None:
    print(f"… {title}", flush=True)
    done = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
    with journal.open("a", encoding="utf-8") as log:
        log.write(f"\n## {title}\nCommande : {' '.join(command)}\nCode : {done.returncode}\n")
        log.write(done.stdout + done.stderr)
    if done.returncode != 0:
        print(done.stdout[-4000:] + done.stderr[-4000:])
        raise SystemExit(f"PRÉPARATION ÉCHOUÉE — étape : {title} (code {done.returncode}) ; journal : {journal}")
    # Les résultats synthétiques des fixtures ne sont pas des réserves sur une livraison.
    # Conserver les bilans et les limites déclarées par les contrôles, sans recopier chaque cas.
    shown = set()
    for line in (done.stdout + done.stderr).splitlines():
        if re.match(r"^\s*(?:NOT-VERIFIED\b|WARNING\b|RÉSERVE\b|CORE BUDGET (?:TESTS )?PASSED|READ_ROUTE TESTS PASSED|PREPARATION TESTS PASSED|CHECK_RENDER TESTS PASSED|FULL VALIDATION PASSED|LOCAL VALIDATION PASSED)", line):
            if line not in shown:
                print("  " + line.strip()); shown.add(line)
    if done.stderr.strip():
        print("  Sortie stderr conservée dans le journal : " + done.stderr.strip()[-1000:])


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    ap = argparse.ArgumentParser(description="Prépare la livraison depuis la distribution GitHub : compilation, contrôles et exports, sans envoi ni déploiement.")
    ap.add_argument("--empreintes", action="store_true", help="afficher l'empreinte sha256 des archives (option)")
    ap.add_argument("--log", "--journal", dest="log", default=".logs/preparer_livraison.log", metavar="CHEMIN", help="conserver la sortie détaillée des contrôles (--journal est un alias)")
    ap.add_argument("--require-browser", action="store_true", help="exiger l’exécution des tests navigateur, sinon échouer")
    args = ap.parse_args()
    if not (ROOT / "scripts/build_distributions.sh").is_file() or not (ROOT / "V1/sections").is_dir():
        raise SystemExit("PRÉPARATION ÉCHOUÉE — commande réservée à la distribution GitHub. "
                         "Dans l’export Local, utiliser python3 scripts/validate_all.py.")
    journal = Path(args.log).resolve()
    if journal.is_relative_to(ROOT / ".build") or journal.is_relative_to(ROOT / "dist"):
        ap.error("le journal doit être hors des répertoires de construction .build et dist")
    if journal == ROOT or journal.suffix != ".log":
        ap.error("le journal doit être un fichier .log")
    journal.parent.mkdir(parents=True, exist_ok=True)
    journal.write_text("Design Governance — journal de préparation de livraison\n", encoding="utf-8")
    print(f"Journal détaillé : {journal}", flush=True)
    step("compilation du noyau", [sys.executable, "scripts/build_core.py"], journal)
    command = [sys.executable, "scripts/validate_all.py"]
    if args.require_browser:
        command.append("--require-browser")
    step("contrôles du package, distributions et reproductibilité", command, journal)
    archives = [ROOT / name for name in ARCHIVES]
    missing = [a.name for a in archives if not a.is_file()]
    if missing:
        raise SystemExit(f"PRÉPARATION ÉCHOUÉE — archive absente : {', '.join(missing)}")
    print("LIVRAISON PRÉPARÉE — contrôles du package exécutés, distributions : " + ", ".join(a.name for a in archives))
    print("Cette préparation ne certifie aucun rendu ni résultat d’usage. Journal : " + str(journal))
    if args.empreintes:
        for a in archives:
            print(f"  {a.name} sha256 {sha256(a)}")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, UnicodeError) as exc:
        print(f"PRÉPARATION ÉCHOUÉE — {type(exc).__name__} : {exc}", file=sys.stderr)
        sys.exit(1)
