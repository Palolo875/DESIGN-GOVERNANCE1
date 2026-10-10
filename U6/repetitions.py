#!/usr/bin/env python3
"""Repère les longs paragraphes exacts servis dans plusieurs routes complètes."""
import hashlib
import json
import re
from collections import defaultdict
from pathlib import Path

root = Path(__file__).resolve().parent
results = {}
for case in sorted((root / "runs").iterdir()):
    log = case / "lectures.jsonl"
    if not log.exists():
        continue
    receipts = [json.loads(line) for line in log.read_text().splitlines()]
    counts = defaultdict(set)
    for key in {item["key"] for item in receipts}:
        body = (case / "textes-servis" / (hashlib.sha256(key.encode()).hexdigest()[:16] + ".txt")).read_text()
        selected = [item for item in receipts if item["key"] == key]
        assert all(hashlib.sha256(body.encode()).hexdigest() == item["full_sha256"] and len(body) == item["full_chars"] for item in selected)
        end = 0
        for a, b in sorted((item["offset"], item["end"]) for item in selected):
            assert 0 <= a <= b <= len(body)
            if a > end:
                break
            end = max(end, b)
        if end < len(body):
            continue
        for paragraph in re.split(r"\n\s*\n", body):
            paragraph = paragraph.strip()
            if len(paragraph) >= 250 and not paragraph.startswith("#"):
                counts[paragraph].add(key)
    duplicates = [{"sha256": hashlib.sha256(p.encode()).hexdigest(), "chars": len(p),
                   "routes": sorted(keys), "excerpt": p[:140]}
                  for p, keys in counts.items() if len(keys) > 1]
    duplicates.sort(key=lambda item: (len(item["routes"]) - 1) * item["chars"], reverse=True)
    results[case.name] = {
        "method": "Paragraphes exacts >=250 caractères, uniquement textes complètement servis ; aucun jeton estimé.",
        "count": len(duplicates),
        "repeated_paragraph_chars": sum((len(item["routes"]) - 1) * item["chars"] for item in duplicates),
        "duplicates": duplicates, "reader_text_integrity": "PASS",
    }
(root / "repetitions-observees.json").write_text(json.dumps(results, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({key: {name: value[name] for name in ["count", "repeated_paragraph_chars", "reader_text_integrity"]} for key, value in results.items()}))
