#!/usr/bin/env python3
"""Phase 4 : carte des verrous par suppression. Pour chaque section (ou bloc) d'un fichier cible, on la retire
dans une copie du dépôt et on note les contrôles qui échouent. Usage : balayage.py COPIE SORTIE.json FICHIER... [--blocs]"""
import json, re, subprocess, sys
from pathlib import Path

copy, out = Path(sys.argv[1]), Path(sys.argv[2])
blocs = "--blocs" in sys.argv
files = [a for a in sys.argv[3:] if a != "--blocs"]
CHECKS = [["scripts/validate_design_governance.py"], ["scripts/validate_reading_map.py"], ["scripts/validate_structure.py"],
          ["scripts/build_core.py", "--check"], ["scripts/test_read_route.py"], ["scripts/test_audit_regressions.py"]]


def run_checks():
    fails = []
    for c in CHECKS:
        r = subprocess.run([sys.executable, *c], cwd=copy, capture_output=True, text=True)
        if r.returncode:
            msg = [l.strip() for l in (r.stdout + r.stderr).splitlines()
                   if l.strip().startswith(("- ", "FAIL", "AssertionError")) or "FAILED —" in l][:6]
            fails.append({"controle": c[0].split("/")[-1], "messages": msg})
    return fails


def units(lines):
    if not blocs:  # sections : titre jusqu'au titre suivant de niveau quelconque
        heads = [i for i, l in enumerate(lines) if re.match(r"^#{1,6} ", l)]
        bounds = [0] + heads + [len(lines)]
        return [(a, b) for a, b in zip(bounds, bounds[1:]) if b > a]
    out, start = [], None
    for i, l in enumerate(lines + [""]):
        if l.strip() and start is None:
            start = i
        elif not l.strip() and start is not None:
            out.append((start, i)); start = None
    return out


base = run_checks()
assert not base, base
result = {}
for f in files:
    p = copy / f
    original = p.read_text(encoding="utf-8")
    lines = original.split("\n")
    rows = []
    for a, b in units(lines):
        if all(l.startswith("<!--") or not l.strip() for l in lines[a:b]):
            continue
        p.write_text("\n".join(lines[:a] + lines[b:]), encoding="utf-8")
        fails = run_checks()
        p.write_text(original, encoding="utf-8")
        rows.append({"lignes": f"{a+1}-{b}", "debut": lines[a][:90], "echecs": fails})
        print(f"{f}:{a+1} {'VERROU' if fails else 'libre '} {lines[a][:60]}", flush=True)
    result[f] = rows
out.write_text(json.dumps(result, ensure_ascii=False, indent=1), encoding="utf-8")
