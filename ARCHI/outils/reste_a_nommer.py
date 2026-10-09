#!/usr/bin/env python3
"""Phase 2 : codes visibles (au moins 3 occurrences) qui n'apparaissent pas encore dans vocabulaire.md.

Usage : reste_a_nommer.py VOCABULAIRE.md  (ajoute ou remplace l'annexe générée à la fin du fichier)
"""
import re, subprocess, sys
from collections import Counter
from pathlib import Path
REPO = Path("/home/user/DESIGN-GOVERNANCE1")
voc = Path(sys.argv[1])
text = voc.read_text(encoding="utf-8").split("\n<!-- annexe générée -->")[0]
known = set(re.findall(r"[A-Z][A-Z0-9_/\-]+[a-z]?", text))
known |= {part for k in list(known) for part in re.split(r"[/]", k)}
known |= {part for k in list(known) for part in k.split("-") if len(part) >= 3}
SIGLES = {"HTML", "JSON", "WCAG", "CSS", "SVG", "PNG", "README", "SKILL", "URL", "API", "ARIA", "UTF", "UTF-8", "HTTP", "HTTPS",
          "RGAA", "GITHUB", "LOCAL", "OKLCH", "SAAS", "DOM", "CLI", "YAML", "PDF", "SIL", "OFL", "FFL", "AVIF", "WEBP", "JPEG",
          "GIF", "MIT", "CTA", "FAQ", "RGB", "HSL", "APCA", "LCP", "CLS", "INP", "GPU", "CPU", "PID", "AA", "AAA", "SEO", "PWA"}
c = Counter()
for f in subprocess.run(["git", "-C", str(REPO), "ls-files", "*.md"], capture_output=True, text=True).stdout.split():
    t = re.sub(r"<!--.*?-->", "", (REPO / f).read_text(encoding="utf-8"), flags=re.S)
    t = re.sub(r"\b(?:DIRECTION|ACTION|SAVOIR|BIBLIOTHEQUE|CHANGELOG)/[A-Za-z0-9_\-/]+", " ", t)
    for m in re.findall(r"\b[A-Z][A-Z0-9]+(?:[_\-][A-Z0-9]+)+\b|\b[A-Z]{3,}\b", t):
        c[m] += 1
rest = [(k, v) for k, v in c.most_common() if v >= 3 and k not in known and k not in SIGLES]
annex = ["", "<!-- annexe générée -->", "### Annexe générée — codes restants (au moins 3 occurrences)", "",
         "Produite par `ARCHI/outils/reste_a_nommer.py`. Les mots en capitales qui sont du texte ordinaire mis en relief "
         "(REQUIS, MODULE…) seront simplement écrits en minuscules.", "",
         ", ".join(f"`{k}` ({v})" for k, v in rest)]
voc.write_text(text.rstrip("\n") + "\n" + "\n".join(annex) + "\n", encoding="utf-8")
print(len(rest), "codes restants")
