#!/usr/bin/env python3
"""Rangement : recalculer les liens relatifs après le renommage de fichiers entiers (git mv).

1. Dans chaque fichier renommé, les liens relatifs sont recalculés depuis sa nouvelle place.
2. Dans tous les autres fichiers Markdown, un lien vers un ancien chemin est redirigé vers le nouveau.
Seules les cibles des liens changent ; le texte, les libellés et les ancres restent identiques.

Usage : renommer_liens.py DEPOT ANCIEN=NOUVEAU [ANCIEN=NOUVEAU ...]
"""
import posixpath, re, sys
from pathlib import Path

repo = Path(sys.argv[1])
moves = dict(a.split("=", 1) for a in sys.argv[2:])
LINK = re.compile(r"(\]\()([^)\s]+)(\))")
SKIP = {"dist", ".build", ".git", ".claude"}


def fix(text: str, old_rel: str, new_rel: str) -> tuple[str, int]:
    count = 0

    def one(m):
        nonlocal count
        target = m.group(2)
        if target.startswith(("http://", "https://", "mailto:", "#")):
            return m.group(0)
        path, _, frag = target.partition("#")
        absolute = posixpath.normpath(posixpath.join(posixpath.dirname(old_rel), path))
        absolute = moves.get(absolute, absolute)
        new = posixpath.relpath(absolute, posixpath.dirname(new_rel))
        if posixpath.dirname(new_rel) == posixpath.dirname(absolute) and not new.startswith("."):
            new = new if not path.startswith("./") else "./" + new
        out = f"{m.group(1)}{new}{'#' + frag if frag else ''}{m.group(3)}"
        if out != m.group(0):
            count += 1
        return out
    return LINK.sub(one, text), count


total = 0
inverse = {v: k for k, v in moves.items()}
for path in sorted(repo.rglob("*.md")):
    rel = path.relative_to(repo).as_posix()
    if rel.split("/")[0] in SKIP:
        continue
    old_rel = inverse.get(rel, rel)
    text = path.read_text(encoding="utf-8")
    new_text, n = fix(text, old_rel, rel)
    if n:
        path.write_text(new_text, encoding="utf-8")
        print(f"  {rel} : {n} lien(s)")
        total += n
print(f"{total} lien(s) recalculé(s)")
