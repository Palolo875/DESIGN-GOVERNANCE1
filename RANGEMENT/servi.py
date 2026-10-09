#!/usr/bin/env python3
"""Rangement : ce que sert chaque route reste identique.

Le rangement déplace du texte sans changer ce que lit l'agent. Ce contrôle relève, pour chaque route et chaque
sous-route lisible, le texte servi par le lecteur (lecture complète, cibles de liens ignorées) ; puis vérifie
qu'il est inchangé. Un écart n'est admis que s'il est inscrit, avec sa raison, dans un fichier d'écarts.

Usage :
  servi.py --base DEPOT BASE.json
  servi.py DEPOT BASE.json [ECARTS.csv]
"""
import csv, hashlib, importlib, json, re, sys
from pathlib import Path


def snapshot(repo: Path) -> dict[str, str]:
    sys.path.insert(0, str(repo / "scripts"))
    rr = importlib.import_module("read_route")
    locators = []
    for row in rr.summary_rows():
        locators.append(row[0])
        for _, _, sub, _ in rr.outline(row[0]):
            if sub:
                locators.append(sub)
    out = {}
    for loc in dict.fromkeys(locators):
        path, lines, index = rr.resolve(loc)
        text = "\n".join(rr.extract(lines, index))
        text = re.sub(r"\]\([^)]*\)", "]()", text)
        out[loc] = hashlib.sha256(re.sub(r"\s+", " ", text).strip().encode("utf-8")).hexdigest()[:20]
    return out


def main(argv):
    if argv[:1] == ["--base"]:
        repo, out = Path(argv[1]), Path(argv[2])
        snap = snapshot(repo)
        out.write_text(json.dumps(snap, ensure_ascii=False, indent=0), encoding="utf-8")
        print(f"BASE SERVIE — {len(snap)} routes et sous-routes")
        return 0
    repo, base = Path(argv[0]), json.loads(Path(argv[1]).read_text(encoding="utf-8"))
    ecarts = {}
    if len(argv) > 2 and Path(argv[2]).is_file():
        for row in csv.DictReader(open(argv[2], encoding="utf-8")):
            if not row.get("raison", "").strip():
                print(f"ÉCART SANS RAISON — {row['locator']}")
                return 1
            ecarts[row["locator"]] = row["raison"]
    now = snapshot(repo)
    changed = [l for l in base if l not in ecarts and now.get(l) != base[l]]
    for l in changed:
        print(f"SERVI CHANGÉ — {l}" + (" (route introuvable)" if l not in now else ""))
    ok = not changed
    print(f"{'SERVI IDENTIQUE' if ok else 'SERVI MODIFIÉ'} — {len(base)} routes et sous-routes, {len(changed)} changées, "
          f"{len(ecarts)} écarts justifiés")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
