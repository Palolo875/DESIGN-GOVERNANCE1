#!/usr/bin/env python3
"""Carte visuelle de l'architecture cible, générée depuis correspondance.csv et AUDIT2/donnees/chemins.json.

Aucun chiffre n'est saisi à la main, sauf les cibles provisoires des chemins (architecture.md, §3).
Usage : carte_architecture.py SORTIE.html
"""
import csv, html, json, sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
rows = list(csv.DictReader(open(ROOT / "ARCHI/correspondance.csv", encoding="utf-8")))
chemins = json.load(open(ROOT / "AUDIT2/donnees/chemins.json", encoding="utf-8"))

vol = defaultdict(int)
flux = defaultdict(lambda: defaultdict(int))
for r in rows:
    dests = r["destination"].split(" + ")
    for d in dests:
        part = int(r["caracteres"]) // len(dests)
        vol[d] += part
        flux[r["fichier"]][d] += part

def k(n):
    return f"{round(n / 1000)} k" if n >= 1000 else f"{n}"

PARTS = [  # (clé, titre, rôle, couleur, fichiers : (chemin, rôle))
 ("guides", "Guides", "Les portes humaines", "ink", [
   ("guides/commencer", "débutant"), ("guides/designer", "designer"), ("guides/equipe", "équipe"), ("guides/glossaire", "glossaire")]),
 ("design/direction", "Direction", "Décider ce que la page doit être", "dir", [
   ("design/direction/cadrer", "demande vague, domaine"), ("design/direction/diriger", "lancement, cible, atelier"),
   ("design/direction/premier-objet", "le premier objet complet"), ("design/direction/boucle", "créer puis apprendre"),
   ("design/direction/standard", "standard visuel, cinq règles")]),
 ("design/savoir", "Savoir", "Le livre de référence", "sav", [
   ("design/savoir/README", "préface, règles d’or"), ("design/savoir/fondements", "fondements"),
   ("design/savoir/qualite-creative", "qualité créative"), ("design/savoir/composition", "composition"),
   ("design/savoir/couleur", "couleur"), ("design/savoir/typographie", "typographie"),
   ("design/savoir/images-et-sources", "images et sources"), ("design/savoir/styles", "styles"),
   ("design/savoir/systeme-de-design", "système de design"), ("design/savoir/contexte", "contexte, accessibilité"),
   ("design/savoir/techniques", "techniques par médium"), ("design/savoir/gout-et-tendances", "goût et tendances"),
   ("design/savoir/pieges", "pièges"), ("design/savoir/connexions", "domaines qui se croisent")]),
 ("design/formes", "Formes", "Les structures", "bib", [
   ("design/formes/README", "comment lire"), ("design/formes/choisir", "choisir une structure"),
   ("design/formes/catalogue", "le catalogue")]),
 ("design/produit", "Produit", "Ce qui fait un vrai produit", "pro", [
   ("design/produit/premier-rendu", "premier rendu"), ("design/produit/interface", "interface réelle, états"),
   ("design/produit/plancher", "accessibilité, contraste"), ("design/produit/finition", "finition sur rendu"),
   ("design/produit/preuve-visuelle", "preuve visuelle")]),
 ("agent", "Agent", "La skill et ses chemins", "ink", [
   ("agent/skill/SKILL", "la skill (noyau)"), ("agent/skill/references", "références"),
   ("agent/chemins", "classer, quoi lire"), ("agent/repondre", "répondre à la personne")]),
 ("gouvernance", "Gouvernance", "Module facultatif : livraison, audit, équipe", "gov", [
   ("gouvernance/principes", "principes"), ("gouvernance/statuts", "statuts"), ("gouvernance/travail", "fiche de travail"),
   ("gouvernance/verification", "vérification"), ("gouvernance/cloture", "clôture"), ("gouvernance/structure", "contrats de structure"),
   ("gouvernance/integrite", "intégrité"), ("gouvernance/projection-machine", "projection machine")]),
 ("maintenance", "Maintenance", "Faire évoluer le système", "ink", [
   ("maintenance/README", "validation, distributions"), ("maintenance/evolution", "règles d’évolution"),
   ("maintenance/versions", "versions")]),
]
MAXF = max(vol[f] for *_, files in PARTS for f, _ in files)

def part_block(key, title, role, color, files):
    total = sum(vol[f] for f, _ in files)
    items = "".join(
        f'<li><span class="fn">{html.escape(f.split("/")[-1])} <span class="fr">{html.escape(r)}</span></span><span class="fk">{k(vol[f])}</span>'
        f'<span class="fb"><i style="width:{max(2, round(100 * vol[f] / MAXF))}%"></i></span></li>'
        for f, r in files)
    cls = "part opt" if key == "gouvernance" else "part"
    tag = '<span class="tag">facultatif</span>' if key == "gouvernance" else ""
    return (f'<section class="{cls}" style="--c:var(--{color})" aria-labelledby="p-{key.replace("/", "-")}">'
            f'<header><h3 id="p-{key.replace("/", "-")}">{title}</h3>{tag}<span class="pk">{k(total)}</span></header>'
            f'<p class="role">{html.escape(role)}</p><ul class="files">{items}</ul></section>')

guides_html = part_block(*PARTS[0])
design_html = "".join(part_block(*p) for p in PARTS[1:5])
rest_html = "".join(part_block(*p) for p in PARTS[5:])
design_total = sum(vol[f] for p in PARTS[1:5] for f, _ in p[4])

# Chemins : aujourd'hui (mesuré) et cible provisoire.
skill = chemins["skill"]
C = chemins["chemins"]
paths = [
 ("Retouche", C["LITE (petite correction)"], 35000),
 ("Page ou écran", C["DIRECTION, trace légère (page nouvelle)"], 75000),
 ("Produit livré", C["DIRECTION, trace complète (produit livré)"], 110000),
]
SCALE = 140000
def seg(cls, n, label):
    return f'<i class="{cls}" style="width:{100 * n / SCALE:.2f}%" title="{label} : {k(n)}"></i>' if n else ""
path_rows = ""
for name, c, cible in paths:
    f = c["par_famille"]
    path_rows += (f'<div class="prow"><div class="pname"><b>{name}</b><span>aujourd’hui {k(c["avec_skill"])} · cible ≤ {k(cible)}</span></div>'
                  f'<div class="ptrack" role="img" aria-label="{name} : aujourd’hui {k(c["avec_skill"])} caractères lus avant de produire, '
                  f'dont skill {k(skill)}, design {k(f["design"])}, produit {k(f["produit"])}, gouvernance {k(f["gouvernance"])} ; cible {k(cible)}">'
                  f'{seg("s-skill", skill, "skill")}{seg("s-dir", f["design"], "design")}{seg("s-pro", f["produit"], "produit")}'
                  f'{seg("s-gov", f["gouvernance"], "gouvernance")}<b class="target" style="left:{100 * cible / SCALE:.2f}%"></b></div></div>')
ticks = "".join(f'<span style="left:{100 * t / SCALE:.2f}%"{" class=end" if t == SCALE else ""}>{k(t)}</span>' for t in range(0, SCALE + 1, 20000))

# D'où vient chaque partie : ancien fichier → grandes parties.
def grande(d):
    if d.startswith("design/"):
        return d.split("/")[1]
    if d in ("RETIRÉ", "HORS PRODUIT (branche refonte)"):
        return "sort"
    if d == "README":
        return "guides"
    return d.split("/")[0]
GCOL = [("direction", "dir", "direction"), ("savoir", "sav", "savoir"), ("formes", "bib", "formes"), ("produit", "pro", "produit"),
        ("agent", "ink", "agent"), ("guides", "ink2", "guides et accueil"), ("gouvernance", "gov", "gouvernance"),
        ("maintenance", "mnt", "maintenance"), ("sort", "out", "retiré ou hors produit")]
ORDER = ["V1/official/SAVOIR.md", "V1/official/ACTION.md", "V1/official/DIRECTION.md", "V1/official/BIBLIOTHEQUE.md",
         "skills/design-governance-practice/SKILL.md", "V1/official/READING_MAP.md", "V1/official/QUICKSTART.md", "README.md",
         "V1/official/CHANGELOG.md", "RELEASE_NOTES.md", "V1/official/GLOSSAIRE.md"]
MAXO = max(sum(flux[f].values()) for f in ORDER)
flow_rows = ""
for f in ORDER:
    g = defaultdict(int)
    for d, n in flux[f].items():
        g[grande(d)] += n
    tot = sum(g.values())
    segs = "".join(f'<i class="g-{c}" style="width:{100 * g[key] / MAXO:.2f}%" title="{lab} : {k(g[key])}"></i>'
                   for key, c, lab in GCOL if g[key])
    desc = ", ".join(f"{lab} {k(g[key])}" for key, c, lab in GCOL if g[key])
    flow_rows += (f'<div class="frow"><span class="fname">{html.escape(f.split("/")[-1])}</span>'
                  f'<div class="ftrack" role="img" aria-label="{html.escape(f)} ({k(tot)}) : {desc}">{segs}</div><span class="fk">{k(tot)}</span></div>')
legend = "".join(f'<span><i class="g-{c}"></i>{lab}</span>' for key, c, lab in GCOL)

page = (ROOT / "ARCHI/outils/carte_gabarit.html").read_text(encoding="utf-8")
for key, val in {"{{GUIDES}}": guides_html, "{{DESIGN}}": design_html, "{{REST}}": rest_html, "{{DESIGN_K}}": k(design_total),
                 "{{PATHS}}": path_rows, "{{TICKS}}": ticks, "{{FLOWS}}": flow_rows, "{{LEGEND}}": legend,
                 "{{N_SECTIONS}}": str(len(rows))}.items():
    page = page.replace(key, val)
Path(sys.argv[1]).write_text(page, encoding="utf-8")
print("écrit", sys.argv[1], len(page), "caractères ; design", k(design_total))
