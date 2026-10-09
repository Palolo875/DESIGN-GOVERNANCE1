#!/usr/bin/env python3
"""Rangement : déplacer des sections entières, sans changer leur texte.

Plan JSON : liste de {"source": "V1/official/ACTION.md", "titre": "## ACTION/STATUS — …", "destination": "gouvernance/statuts.md"}.
Une section va de son titre exact jusqu'au titre suivant de niveau égal ou supérieur. Elle est retirée de sa source et
ajoutée à la fin de sa destination, dans l'ordre du plan. Les liens relatifs du texte déplacé sont recalculés depuis sa
nouvelle place ; les liens qui visaient, dans le fichier d'origine, une ancre déplacée sont redirigés, partout.
Le script n'écrit rien d'autre ; la table LIEUX, le manifeste et le build sont mis à jour à part, puis contrôlés.

Usage : deplacer.py DEPOT PLAN.json
"""
import json, os, posixpath, re, sys
from pathlib import Path

repo, plan = Path(sys.argv[1]), json.loads(Path(sys.argv[2]).read_text(encoding="utf-8"))
sys.path.insert(0, str(repo / "scripts"))
from validate_design_governance import markdown_anchors  # noqa: E402

LINK = re.compile(r"(\]\()([^)\s]+)(\))")


def section_bounds(lines, title):
    fence, hits = False, []
    heads = []
    for i, line in enumerate(lines):
        if line.strip().startswith("```"):
            fence = not fence
        elif not fence and re.match(r"^#{1,6} ", line):
            heads.append((i, len(line) - len(line.lstrip("#"))))
            if line.rstrip() == title:
                hits.append(i)
    if len(hits) != 1:
        raise SystemExit(f"titre trouvé {len(hits)} fois : {title}")
    start = hits[0]
    level = next(l for i, l in heads if i == start)
    end = next((i for i, l in heads if i > start and l <= level), len(lines))
    return start, end


def relink(text, old_rel, new_rel, moved_anchors_here):
    """Recalcule les liens relatifs d'un texte qui passe de old_rel à new_rel (chemins relatifs au dépôt)."""
    def fix(m):
        target = m.group(2)
        if target.startswith(("http://", "https://", "mailto:")):
            return m.group(0)
        path, _, frag = target.partition("#")
        if not path:  # ancre du même fichier
            if frag in moved_anchors_here:
                return m.group(0)
            absolute = old_rel
        else:
            absolute = posixpath.normpath(posixpath.join(posixpath.dirname(old_rel), path))
        new = posixpath.relpath(absolute, posixpath.dirname(new_rel))
        return f"{m.group(1)}{new}{'#' + frag if frag else ''}{m.group(3)}"
    return LINK.sub(fix, text)


# 1. Extraire chaque section, dans l'ordre du plan.
sources = {}
moved = []  # (source, destination, texte)
for step in plan:
    src = step["source"]
    if src not in sources:
        sources[src] = (repo / src).read_text(encoding="utf-8").split("\n")
    lines = sources[src]
    start, end = section_bounds(lines, step["titre"])
    block = lines[start:end]
    while block and not block[-1].strip():
        block.pop()
    moved.append((src, step["destination"], "\n".join(block)))
    del lines[start:end]
for src, lines in sources.items():
    (repo / src).write_text(re.sub(r"\n{3,}", "\n\n", "\n".join(lines)), encoding="utf-8")

# 2. Ancres déplacées : (fichier d'origine, ancre) → fichier de destination.
by_dest = {}
for src, dest, text in moved:
    by_dest.setdefault(dest, []).append((src, text))
anchor_moves = {}
for dest, items in by_dest.items():
    for src, text in items:
        for a in markdown_anchors(text):
            anchor_moves[(src, a)] = dest

# 3. Écrire les destinations, liens recalculés.
for dest, items in by_dest.items():
    here = {a for (s, a), d in anchor_moves.items() if d == dest}
    target = repo / dest
    target.parent.mkdir(parents=True, exist_ok=True)
    existing = target.read_text(encoding="utf-8").rstrip("\n") + "\n\n" if target.exists() else ""
    # Chaque section porte son origine (invisible à la lecture) : un fichier peut recevoir plusieurs sources.
    body = "\n\n".join(f"<!-- origine:{posixpath.basename(src)} -->\n" + relink(text, src, dest, here) for src, text in items)
    target.write_text(existing + body + "\n", encoding="utf-8")

# 4. Rediriger, dans tout le dépôt, les liens vers une ancre déplacée.
count = 0
for path in sorted(repo.rglob("*.md")):
    rel = path.relative_to(repo).as_posix()
    if rel.split("/")[0] in {"dist", ".build", ".git", ".claude"}:
        continue
    text = path.read_text(encoding="utf-8")

    def redirect(m):
        global count
        target = m.group(2)
        if target.startswith(("http://", "https://", "mailto:")) or "#" not in target:
            return m.group(0)
        p, _, frag = target.partition("#")
        absolute = posixpath.normpath(posixpath.join(posixpath.dirname(rel), p)) if p else rel
        dest = anchor_moves.get((absolute, frag))
        if not dest or dest == absolute:
            return m.group(0)
        count += 1
        new = posixpath.relpath(dest, posixpath.dirname(rel)) if dest != rel else ""
        return f"{m.group(1)}{new}#{frag}{m.group(3)}"
    new_text = LINK.sub(redirect, text)
    if new_text != text:
        path.write_text(new_text, encoding="utf-8")
print(f"{len(moved)} sections déplacées vers {len(by_dest)} fichier(s) ; {count} lien(s) redirigé(s)")
for dest, items in by_dest.items():
    print(f"  {dest} ← " + ", ".join(t.split(chr(10))[0][:50] for _, t in items))
