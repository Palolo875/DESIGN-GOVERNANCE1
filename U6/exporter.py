#!/usr/bin/env python3
"""Archive les preuves complètes, sans écraser une livraison précédente."""
import argparse
import hashlib
import json
import zipfile
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("destination", type=Path)
args = parser.parse_args()
root = Path(__file__).resolve().parent
state = json.loads((root / "etat-execution.json").read_text())
if len(state["productions_completed"]) != 6 or len(state["audits_completed"]) != 6:
    parser.error("Les six productions et leurs contrôles doivent être terminés.")
if sorted(state["judges"].values()) != ["judge_complete", "judge_complete"]:
    parser.error("Les deux jugements doivent être reçus.")
destination = args.destination.resolve()
if destination.exists():
    parser.error("Archive existante : choisir une nouvelle destination.")
if destination == root or root in destination.parents:
    parser.error("L'archive doit se trouver hors du dossier de preuves.")
files = []
for path in sorted(root.rglob("*")):
    if path.is_symlink():
        parser.error(f"Lien symbolique inattendu : {path}.")
    if path.is_file() and "__pycache__" not in path.parts and path.suffix != ".pyc":
        files.append(path)
manifest = {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
destination.parent.mkdir(parents=True, exist_ok=True)
with zipfile.ZipFile(destination, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
    for path in files:
        info = zipfile.ZipInfo("U6/" + str(path.relative_to(root)), (2026, 10, 10, 0, 0, 0))
        info.external_attr = 0o100644 << 16
        info.compress_type = zipfile.ZIP_DEFLATED
        archive.writestr(info, path.read_bytes())
    info = zipfile.ZipInfo("U6/ARCHIVE-SHA256.json", (2026, 10, 10, 0, 0, 0))
    info.external_attr = 0o100644 << 16
    info.compress_type = zipfile.ZIP_DEFLATED
    archive.writestr(info, json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
with zipfile.ZipFile(destination) as archive:
    bad = archive.testzip()
    if bad:
        raise ValueError(f"CRC invalide : {bad}")
    for name, digest in manifest.items():
        if hashlib.sha256(archive.read("U6/" + name)).hexdigest() != digest:
            raise ValueError(f"Archive différente de la preuve : {name}")
summary = {"archive": str(destination), "files": len(files) + 1, "bytes": destination.stat().st_size,
           "sha256": hashlib.sha256(destination.read_bytes()).hexdigest(), "crc": "PASS", "every_file_sha256": "PASS"}
destination.with_suffix(".verification.json").write_text(json.dumps(summary, indent=2) + "\n")
print(json.dumps(summary))
