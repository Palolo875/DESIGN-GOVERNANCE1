#!/usr/bin/env python3
"""Copie les preuves utiles sur la branche documentaire, sans copier les paquets."""
import argparse
import hashlib
import json
import shutil
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("destination", type=Path)
args = parser.parse_args()
root = Path(__file__).resolve().parent
state = json.loads((root / "etat-execution.json").read_text())
if len(state["audits_completed"]) != 6 or sorted(state["judges"].values()) != ["judge_complete", "judge_complete"]:
    parser.error("Résultats incomplets : ne pas livrer un état documentaire final.")
destination = args.destination.resolve()
if destination.exists():
    parser.error("Dossier documentaire existant : aucun écrasement.")
destination.mkdir(parents=True)
copied = {}
for path in sorted(root.rglob("*")):
    relative = path.relative_to(root)
    if path.is_symlink():
        parser.error(f"Lien symbolique inattendu : {relative}.")
    if not path.is_file() or "__pycache__" in relative.parts or path.suffix == ".pyc":
        continue
    if relative.parts[0] == "runs" and "paquet" in relative.parts:
        continue
    if relative.parts[0] == "moyens" and path.suffix == ".ttf":
        continue
    target = destination / relative
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(path, target)
    copied[str(relative)] = hashlib.sha256(path.read_bytes()).hexdigest()
(destination / "DEPOT-SHA256.json").write_text(json.dumps(copied, indent=2) + "\n")
print(json.dumps({"destination":str(destination),"files":len(copied),"scope":"preuves et outils ; paquets exacts et polices communes dans l'archive complète"}))
