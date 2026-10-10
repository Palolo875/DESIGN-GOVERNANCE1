#!/usr/bin/env python3
"""Préparer deux dossiers de jugement contenant uniquement captures et briefs."""
import argparse
import hashlib
import json
import shutil
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("destination", type=Path)
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    protocol = json.loads((root / "protocole.json").read_text())
    sources = []
    for case in protocol["cases"]:
        audit = root / "runs" / case["run"] / "audit-final"
        observation = audit / "observations.json"
        if not observation.is_file():
            parser.error(f"Capture indépendante absente pour {case['run']} ; dossier anonyme non créé.")
        report = json.loads(observation.read_text())
        if not report.get("source_unchanged"):
            parser.error(f"Livrable modifié pendant les mesures : {case['run']}.")
        output = Path(case["output"])
        current = {str(p.relative_to(output)): hashlib.sha256(p.read_bytes()).hexdigest()
                   for p in sorted(output.rglob("*")) if p.is_file()}
        if current != report["output_sha256"]:
            parser.error(f"Livrable modifié après les mesures : {case['run']}.")
        for name, expected in report["evidence_sha256"].items():
            if hashlib.sha256((audit / name).read_bytes()).hexdigest() != expected:
                parser.error(f"Preuve modifiée : {case['run']}/{name}.")
        sources.append((case, audit))
    destination = args.destination.resolve()
    if destination.exists():
        parser.error("La destination existe déjà ; aucun dossier de jugement n'est écrasé.")
    # L'ordre est fixé par le protocole, sans révéler les conditions aux juges.
    labels = {c["run"]: c["anonymous_label"] for c in protocol["cases"]}
    pairs = [[labels["run-01"], labels["run-02"]],
             [labels["run-04"], labels["run-03"]],
             [labels["run-06"], labels["run-05"]]]
    repetitions = [[labels["run-01"], labels["run-04"]],
                   [labels["run-02"], labels["run-03"]]]
    for judge in [1, 2]:
        folder = destination / f"juge-{judge}"
        folder.mkdir(parents=True)
        shutil.copyfile(root / "grille-aveugle.md", folder / "consigne.md")
        public = {
            "pages": [],
            "comparisons": pairs if judge == 1 else [p[::-1] for p in pairs[::-1]],
            "repetitions": repetitions if judge == 1 else [p[::-1] for p in repetitions[::-1]],
        }
        for case, audit in sources:
            label = case["anonymous_label"]
            page = {"label": label, "brief": case["brief"], "screenshots": []}
            for width in [1440, 390]:
                for kind in ["premiere", "complete"]:
                    name = f"{label}-{width}-{kind}.png"
                    shutil.copyfile(audit / f"{width}-{kind}.png", folder / name)
                    page["screenshots"].append(name)
            public["pages"].append(page)
        public["pages"].sort(key=lambda page: page["label"], reverse=judge == 2)
        (folder / "ordre.json").write_text(json.dumps(public, ensure_ascii=False, indent=2) + "\n")
        hashes = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(folder.iterdir()) if p.is_file()}
        (folder / "SHA256.json").write_text(json.dumps(hashes, indent=2) + "\n")
    print("Deux dossiers anonymisés créés. Ils ne contiennent ni code, ni version, ni trace.")


if __name__ == "__main__":
    main()
