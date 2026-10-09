#!/usr/bin/env python3
"""Audit 2 (S4) : trouvabilité sur le second jeu, bâti sans voir les alias du lecteur.

Succès : une route attendue figure dans les résultats de `read_route.py --trouver` ; on note son rang
et si elle est dans les trois premières (ce qu'un humain ou un agent regarde vraiment).

Usage : trouvabilite2.py JEU.json SORTIE.json
"""
import json, re, statistics, subprocess, sys
from collections import defaultdict
REPO = "/home/user/DESIGN-GOVERNANCE1"
jeu = json.load(open(sys.argv[1]))
res = []
for b in jeu:
    for t in b["termes"]:
        out = subprocess.run([sys.executable, "scripts/read_route.py", "--trouver", t], capture_output=True, text=True, cwd=REPO).stdout
        locs = []
        for line in out.splitlines():
            m = re.match(r"^((?:DIRECTION|ACTION|SAVOIR|BIBLIOTHEQUE)/\S+)\s", line)
            if m and m.group(1) not in locs:
                locs.append(m.group(1))
        hit = [i for i, l in enumerate(locs) if any(l == a or l.startswith(a + "/") or a.startswith(l + "/") for a in b["routes"])]
        res.append({"besoin": b["besoin"], "public": b["public"], "famille": b["famille"], "terme": t, "routes": len(locs),
                    "trouve": bool(hit), "rang": hit[0] + 1 if hit else None, "top3": bool(hit) and hit[0] < 3, "premieres": locs[:3]})
json.dump(res, open(sys.argv[2], "w"), ensure_ascii=False, indent=1)
ok = [r for r in res if r["trouve"]]
print(f"termes : {len(ok)}/{len(res)} trouvés ; {sum(r['top3'] for r in res)}/{len(res)} dans les 3 premières ; "
      f"rang médian {statistics.median([r['rang'] for r in ok]) if ok else '-'} ; aucun résultat : {sum(1 for r in res if not r['routes'])}")
for key in ("public", "famille"):
    g = defaultdict(list)
    for r in res:
        g[r[key]].append(r)
    print(key, {k: f"{sum(x['top3'] for x in v)}/{len(v)} top3, {sum(x['trouve'] for x in v)}/{len(v)}" for k, v in g.items()})
besoins = defaultdict(list)
for r in res:
    besoins[r["besoin"]].append(r)
print(f"besoins : {sum(any(x['top3'] for x in v) for v in besoins.values())}/{len(besoins)} ont au moins un terme en top 3 ; "
      f"{sum(all(x['top3'] for x in v) for v in besoins.values())}/{len(besoins)} tous")
print("échecs (aucune route attendue) :", [r["terme"] for r in res if not r["trouve"]])
