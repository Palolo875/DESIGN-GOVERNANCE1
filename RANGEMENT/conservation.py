#!/usr/bin/env python3
"""Rangement (phase 3) : contrôle « rien de perdu » et identité de la skill.

Mode `--base` : relève l'empreinte de chaque bloc de texte des documents du système (paragraphe, liste,
tableau, bloc de code, titre ; hors blocs faits seulement de commentaires HTML) et l'empreinte de la skill.
Mode contrôle (par défaut) : vérifie que chaque bloc de la base se retrouve dans un document du dépôt
(n'importe où, sous n'importe quel nom), sauf s'il figure dans `retraits.csv` avec sa raison ; vérifie que la
skill compilée est identique à l'octet près, sauf si `--skill-libre` est donné (phase 5).

Normalisation : espaces regroupés ; cibles des liens Markdown ignorées (un fichier déplacé change ses liens
relatifs sans changer son texte). Rien d'autre n'est toléré : un mot changé est un bloc perdu.

Usage :
  conservation.py --base DEPOT BASE.json [COMMIT]   relever la base (DEPOT peut être un export git archive)
  conservation.py DEPOT BASE.json [RETRAITS.csv] [--skill-libre]
"""
import csv, hashlib, json, re, subprocess, sys
from pathlib import Path

SKILL = "skills/design-governance-practice/SKILL.md"


def documents(repo: Path) -> list[Path]:
    if not (repo / ".git").exists():  # export (git archive) : tous les .md
        return sorted(p for p in repo.rglob("*.md") if p.is_file())
    out = subprocess.run(["git", "-C", str(repo), "ls-files", "--cached", "--others", "--exclude-standard", "*.md"],
                         capture_output=True, text=True, check=True).stdout.split()
    return sorted({repo / p for p in out if (repo / p).is_file()})


ITEM = re.compile(r"^\s{0,3}(?:[-*+]|\d+[.)])\s")


def units(start: int, block: str):
    """Un tableau se compte ligne par ligne, une liste item par item ; le reste, bloc entier.
    Ajouter une ligne à un tableau ou un item à une liste ne fait donc rien perdre."""
    lines = block.split("\n")
    if block.startswith("```"):
        yield start, block
    elif all(l.lstrip().startswith("|") for l in lines):
        for i, l in enumerate(lines):
            if not re.fullmatch(r"\s*\|[\s|:-]*\|?\s*", l):  # ligne de séparation ignorée
                yield start + i, l
    elif ITEM.match(lines[0]):
        cur, at = [], start
        for i, l in enumerate(lines):
            if ITEM.match(l) and cur:
                yield at, "\n".join(cur)
                cur, at = [], start + i
            cur.append(l)
        yield at, "\n".join(cur)
    else:
        yield start, block


def blocks(text: str):
    """Blocs séparés par des lignes vides ; un bloc de code clôturé reste entier."""
    lines = text.splitlines()
    cur, start, fence, n = [], 0, False, 0
    for n, line in enumerate(lines, 1):
        if line.strip().startswith("```"):
            if not cur:
                start = n
            cur.append(line)
            fence = not fence
            continue
        if fence:
            cur.append(line)
            continue
        if not line.strip() or re.match(r"^#{1,6} ", line):
            if cur:
                yield start, "\n".join(cur)
                cur = []
            if line.strip():
                yield n, line
            continue
        if not cur:
            start = n
        cur.append(line)
    if cur:
        yield start, "\n".join(cur)


RENOMMAGES: list[tuple[str, str]] = []  # (nouveau, ancien) : chemins renommés par un lot, ramenés à l'ancien avant comparaison
_rn = Path(__file__).with_name("renommages.csv")
if _rn.is_file():
    RENOMMAGES = [(r["nouveau"], r["ancien"]) for r in csv.DictReader(open(_rn, encoding="utf-8"))]


def norm(block: str) -> str:
    b = re.sub(r"\]\([^)]*\)", "]()", block)
    for nouveau, ancien in RENOMMAGES:
        b = b.replace(nouveau, ancien)
    return re.sub(r"\s+", " ", b).strip()


def only_comments(block: str) -> bool:
    return not re.sub(r"<!--.*?-->", "", block, flags=re.S).strip()


def digest(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()[:20]


def scan(repo: Path):
    found = {}
    for path in documents(repo):
        rel = path.relative_to(repo).as_posix()
        if rel == SKILL:
            continue  # copie compilée : contrôlée par son empreinte, pas comme source
        for line, b in (u for s, bl in blocks(path.read_text(encoding="utf-8")) for u in units(s, bl)):
            if only_comments(b):
                continue
            found.setdefault(digest(norm(b)), f"{rel}:{line}")
    return found


def main(argv):
    if argv[:1] == ["--base"]:
        repo, out = Path(argv[1]), Path(argv[2])
        base = {"commit": argv[3] if len(argv) > 3 else subprocess.run(["git", "-C", str(repo), "rev-parse", "--short", "HEAD"], capture_output=True, text=True).stdout.strip(),
                "skill_sha256": hashlib.sha256((repo / SKILL).read_bytes()).hexdigest(), "blocs": {}}
        for path in documents(repo):
            rel = path.relative_to(repo).as_posix()
            if rel == SKILL:
                continue
            for line, b in (u for s, bl in blocks(path.read_text(encoding="utf-8")) for u in units(s, bl)):
                if only_comments(b):
                    continue
                base["blocs"].setdefault(digest(norm(b)), {"origine": f"{rel}:{line}", "debut": norm(b)[:90]})
        out.write_text(json.dumps(base, ensure_ascii=False, indent=0), encoding="utf-8")
        print(f"BASE — {len(base['blocs'])} blocs, skill {base['skill_sha256'][:12]}, commit {base['commit']}")
        return 0
    free = "--skill-libre" in argv
    args = [a for a in argv if a not in ("--skill-libre", "--pertes")]
    repo, base = Path(args[0]), json.loads(Path(args[1]).read_text(encoding="utf-8"))
    retraits = {}
    if len(args) > 2 and Path(args[2]).is_file():
        for row in csv.DictReader(open(args[2], encoding="utf-8")):
            if not row.get("raison", "").strip():
                print(f"RETRAIT SANS RAISON — {row.get('empreinte')}")
                return 1
            retraits[row["empreinte"]] = row["raison"]
    now = scan(repo)
    lost = [(h, b) for h, b in base["blocs"].items() if h not in now and h not in retraits]
    stale = [h for h in retraits if h not in base["blocs"]]
    skill_ok = free or hashlib.sha256((repo / SKILL).read_bytes()).hexdigest() == base["skill_sha256"]
    if "--pertes" in argv:  # liste brute pour préparer retraits.csv : empreinte, origine, début
        for h, b in lost:
            print(f"{h}\t{b['origine']}\t{b['debut']}")
        return 0 if not lost else 1
    for h, b in lost[:40]:
        print(f"PERDU — {b['origine']} : {b['debut']}")
    if len(lost) > 40:
        print(f"… et {len(lost) - 40} autres")
    for h in stale:
        print(f"RETRAIT INCONNU — {h} n'est pas dans la base")
    if not skill_ok:
        print("SKILL MODIFIÉE — la skill compilée n'est plus identique à l'octet près (autorisé seulement en phase 5 : --skill-libre)")
    ok = not lost and not stale and skill_ok
    print(f"{'CONSERVATION PASSED' if ok else 'CONSERVATION FAILED'} — {len(base['blocs'])} blocs de base, "
          f"{len(base['blocs']) - len(lost) - len(retraits)} retrouvés, {len(retraits)} retirés avec raison, {len(lost)} perdus ; "
          f"skill {'libre (phase 5)' if free else 'identique' if skill_ok else 'MODIFIÉE'}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
