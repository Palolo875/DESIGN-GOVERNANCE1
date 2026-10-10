#!/usr/bin/env python3
"""Fige un livrable après ses contrôles, sans modifier la page ou ses preuves."""
import argparse
import hashlib
import json
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("run")
args = parser.parse_args()
root = Path(__file__).resolve().parent
protocol = json.loads((root / "protocole.json").read_text())
case = next((c for c in protocol["cases"] if c["run"] == args.run), None)
if case is None:
    parser.error("Run absent du protocole.")
run = root / "runs" / args.run
audit = json.loads((run / "audit-final" / "observations.json").read_text())
journeys = json.loads((run / "parcours-coordinateur.json").read_text())
output = Path(case["output"])
actual = {str(p.relative_to(output)): hashlib.sha256(p.read_bytes()).hexdigest()
          for p in sorted(output.rglob("*")) if p.is_file()}
if not audit["source_unchanged"] or not journeys["source_unchanged"] or actual != audit["output_sha256"]:
    parser.error("Source modifiée après ou pendant les mesures.")
packet = json.loads((run / "paquet-manifest.json").read_text())
for name, digest in packet.items():
    if hashlib.sha256((run / "paquet" / name).read_bytes()).hexdigest() != digest:
        parser.error(f"Paquet de la condition modifié : {name}.")
for name, digest in audit["evidence_sha256"].items():
    if hashlib.sha256((run / "audit-final" / name).read_bytes()).hexdigest() != digest:
        parser.error(f"Capture indépendante modifiée : {name}.")
target = run / "livrable-manifest.json"
if target.exists():
    if json.loads(target.read_text()) != actual:
        parser.error("Le manifeste déjà figé diffère du livrable.")
else:
    target.write_text(json.dumps(actual, indent=2) + "\n")
print(json.dumps({"run": args.run, "files": len(actual), "packet_files_unchanged": len(packet),
                  "passed": journeys["passed"], "failed": journeys["failed"], "integrity": "PASS"}))
