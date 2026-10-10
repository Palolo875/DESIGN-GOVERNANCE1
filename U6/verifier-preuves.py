#!/usr/bin/env python3
"""Vérifie les empreintes U6 à partir de chemins relatifs, sans navigateur."""
import argparse
import hashlib
import json
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("root", nargs="?", type=Path, default=Path(__file__).resolve().parent)
parser.add_argument("--documentation", action="store_true", help="Paquets et TTF volontairement omis de la branche refonte.")
args = parser.parse_args()
root = args.root.resolve()
checked = 0


def check(path, digest):
    global checked
    assert path.is_file(), f"Absent : {path}"
    assert hashlib.sha256(path.read_bytes()).hexdigest() == digest, f"Empreinte différente : {path}"
    checked += 1


def read(path):
    return json.loads(path.read_text())


def files(folder):
    assert not any(p.is_symlink() for p in folder.rglob("*")), f"Symlink : {folder}"
    return {str(p.relative_to(folder)) for p in folder.rglob("*")
            if p.is_file() and "__pycache__" not in p.parts and p.suffix != ".pyc"}


for name in ["PROTOCOLE-SHA256SUMS", "CONTROLES-SHA256SUMS"]:
    for line in (root / name).read_text().splitlines():
        if not line.strip():
            continue
        digest, relative = line.split(maxsplit=1)
        check(root / relative.lstrip("*"), digest)

protocol = read(root / "protocole.json")
for case in protocol["cases"]:
    run = root / "runs" / case["run"]
    manifest = read(run / "livrable-manifest.json")
    assert files(run / "livrable") == set(manifest), f"Inventaire livrable : {run}"
    for name, digest in manifest.items():
        check(run / "livrable" / name, digest)
    audit = read(run / "audit-final" / "observations.json")
    journey = read(run / "parcours-coordinateur.json")
    assert audit["source_unchanged"] and journey["source_unchanged"], run
    assert manifest == audit["output_sha256"], run
    for name, digest in audit["evidence_sha256"].items():
        check(run / "audit-final" / name, digest)
    packet = read(run / "paquet-manifest.json")
    if args.documentation:
        assert not (run / "paquet").exists(), f"Paquet inattendu dans le périmètre documentaire : {run}"
    else:
        assert files(run / "paquet") == set(packet), f"Inventaire paquet : {run}"
        for name, digest in packet.items():
            check(run / "paquet" / name, digest)
    assert all(route["read_completely"] for route in read(root / "lecture-mesuree.json")[case["run"]]["routes"]), run

for name, digest in read(root / "moyens" / "manifest.json").items():
    if args.documentation and name.endswith(".ttf"):
        assert not (root / "moyens" / name).exists(), name
    else:
        check(root / "moyens" / name, digest)

for number in [1, 2]:
    judge = root / "jugements" / f"juge-{number}"
    manifest = read(judge / "SHA256.json")
    assert files(judge) == set(manifest) | {"SHA256.json"}, judge
    for name, digest in manifest.items():
        check(judge / name, digest)
    order = read(judge / "ordre.json")
    verdict = read(root / "jugements" / "resultats" / f"juge-{number}.json")
    expected = {name for page in order["pages"] for name in page["screenshots"]}
    inspected = set()
    for name in verdict["inspected_screenshots"]:
        path = Path(name)
        assert len(path.parts) == 1 or path.parts[-3:] == ("jugements", f"juge-{number}", path.name), name
        inspected.add(path.name)
    assert len(expected) == 24 and inspected == expected, judge
    assert [item["labels"] for item in verdict["comparisons"]] == order["comparisons"], judge
    assert [item["labels"] for item in verdict["repetitions"]] == order["repetitions"], judge
    for item in verdict["comparisons"]:
        assert item["preferred"] in item["labels"] + ["tie", "indeterminate"], judge
        assert item["confidence"] in ["low", "medium", "high"], judge
        assert item["evidence"] and item["reservation"], judge

for label in ["A", "B"]:
    folder = root / "corrections" / label
    audit = read(root / "corrections" / f"{label}-audit" / "observations.json")
    journey = read(root / "corrections" / f"{label}-parcours.json")
    assert files(folder) == set(audit["output_sha256"]), folder
    assert audit["source_unchanged"] and journey["source_unchanged"] and journey["failed"] == 0, folder
    for name, digest in audit["output_sha256"].items():
        check(folder / name, digest)
    for name, digest in audit["evidence_sha256"].items():
        check(root / "corrections" / f"{label}-audit" / name, digest)
assert read(root / "corrections" / "B-prix.json")["status"] == "PASS"

if args.documentation:
    for name, digest in read(root / "DEPOT-SHA256.json").items():
        check(root / name, digest)
else:
    archive_manifest = root / "ARCHIVE-SHA256.json"
    if archive_manifest.exists():
        for name, digest in read(archive_manifest).items():
            check(root / name, digest)

print(json.dumps({"status": "PASS", "sha256_checked": checked,
                  "scope": "documentation" if args.documentation else "full",
                  "limits": "Empreintes, inventaires et structure des jugements ; ne rejoue pas les parcours et ne certifie pas leurs conclusions."}, ensure_ascii=False))
