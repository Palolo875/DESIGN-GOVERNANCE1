#!/usr/bin/env python3
"""Audit : inventaire des routes, chargement, citations, renvois et usage réel dans les runs (U3, U5).

Usage : inventaire.py SORTIE.json
"""
import json, re, subprocess, sys
from collections import Counter, defaultdict
from pathlib import Path
REPO = Path("/home/user/DESIGN-GOVERNANCE1")
sys.path.insert(0, str(REPO / "scripts"))
import read_route as rr
S = "/tmp/claude-0/-home-user-DESIGN-GOVERNANCE1/d50555cc-e888-5d84-bb8b-64d228442ef5"
RUNS = {"R2": "a675f495cc1b9f409", "R4": "a3b7c5b682eeb1822", "R6": "aaf771efaa8df1582", "R7": "a18b7323ba8ae2452",
        "N1": "aef4311c1f6d291f0", "N2": "ae45da357a53b77f7", "N3": "a5f69d7291791df20", "N4": "affdb1d86009267b9",
        "N5": "aacb7de37f3b8ac47"}
SRC = ("DIRECTION", "ACTION", "SAVOIR", "BIBLIOTHEQUE")
texts = {f: (rr.OFFICIAL / f"{f}.md").read_text(encoding="utf-8") for f in SRC}
skill = (REPO / "skills/design-governance-practice/SKILL.md").read_text(encoding="utf-8")
D = texts["DIRECTION"]
charge = D[D.find("<!-- noyau:début CHARGE-TABLE"):D.find("<!-- noyau:fin CHARGE-TABLE")]
rows = {l.split("|")[1].strip().strip("*"): l.split("|")[2:4] for l in charge.splitlines() if l.startswith("| **")}
LOC = re.compile(r"\b(?:DIRECTION|ACTION|SAVOIR|BIBLIOTHEQUE)/[A-Z0-9_\-]+(?:/[A-Za-z0-9_\-]+)?")

routes = []
for f in SRC:
    lines = texts[f].splitlines()
    heads = rr.headings(lines)
    for idx, lvl, h in heads:
        loc = rr.heading_locator(h)
        if not loc:
            continue
        end = rr.block_end(lines, heads, idx)
        body = "\n".join(lines[idx:end])
        subs = sum(1 for i, l2, _ in heads if idx < i < end)
        out_refs = sorted(set(m for m in LOC.findall(body) if not m.startswith(loc)))
        routes.append({"loc": loc, "file": f, "level": lvl, "chars": len(body), "sous_titres": subs,
                       "charge_dabord": [m for m, c in rows.items() if loc in c[0]],
                       "charge_si": [m for m, c in rows.items() if loc in c[1]],
                       "noyau": loc in skill, "renvois_sortants": out_refs})
alltxt = "\n".join(texts.values())
for r in routes:
    loc = r["loc"]
    r["citations"] = len(re.findall(re.escape(loc) + r"(?![A-Za-z0-9_\-])", alltxt)) + len(re.findall(re.escape(loc) + "/", alltxt)) - 1
    kind = loc.split("/")[1]
    r["citations_prefixe"] = len(re.findall(r"`" + re.escape(kind) + r"/[A-Z_]+`", alltxt)) if loc.startswith("BIBLIOTHEQUE/") and kind in rr.STRUCTURE_PARENTS else 0

# usage réel : commandes Bash contenant read_route dans les transcriptions complètes
usage = defaultdict(Counter); truncated = Counter(); searches = defaultdict(list)
for run, aid in RUNS.items():
    for line in open(f"{S}/tasks/{aid}.output", encoding="utf-8"):
        try:
            ev = json.loads(line)
        except json.JSONDecodeError:
            continue
        m = ev.get("message") or {}
        for p in (m.get("content") or []) if isinstance(m, dict) else []:
            if isinstance(p, dict) and p.get("type") == "tool_use":
                cmd = str((p.get("input") or {}).get("command") or "")
                if "read_route" not in cmd:
                    continue
                for t in re.findall(r'--trouver\s+"([^"]+)"|--trouver\s+(\S+)', cmd):
                    searches[run].append(t[0] or t[1])
                for loc in set(LOC.findall(cmd)):
                    usage[loc][run] += 1
                    if re.search(r"\|\s*(head|sed -n|cut)", cmd):
                        truncated[loc] += 1
for r in routes:
    r["lu_par"] = sorted(k for k in usage if k == r["loc"] or k.startswith(r["loc"] + "/") for k in [k])
    r["runs"] = sorted({run for k, c in usage.items() if k == r["loc"] or k.startswith(r["loc"] + "/") for run in c})
json.dump({"routes": routes, "usage": {k: dict(v) for k, v in usage.items()}, "tronques": dict(truncated),
           "recherches": dict(searches)}, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
print(len(routes), "routes ;", len(usage), "locators lus dans les runs")
