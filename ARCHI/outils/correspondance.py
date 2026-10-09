#!/usr/bin/env python3
"""Phase 2 : table de correspondance, section par section, de l'arborescence actuelle vers l'architecture cible.

Chaque titre (niveaux 1 à 3) de chaque document du système reçoit une destination et une disposition.
Les règles sont écrites à la main, à partir des fiches de la phase 1 (AUDIT2/fiches) et de l'architecture
(ARCHI/architecture.md) : une règle s'applique au titre de sa ligne et aux titres suivants jusqu'à la règle
suivante. Le script vérifie que chaque titre est couvert et que chaque destination est un fichier prévu.

Dispositions : déplacer (tel quel), scinder (le détail par paragraphe se fait au lot de rangement),
fusionner (avec une autre section qui dit la même chose), réécrire (forme), retirer (raison donnée),
phase 5 (changement de fond ou de comportement de l'agent, hors rangement).

Usage : correspondance.py SORTIE.csv SORTIE.md
"""
import csv, re, subprocess, sys
from collections import Counter, defaultdict
from pathlib import Path

REPO = Path("/home/user/DESIGN-GOVERNANCE1")

# Fichiers prévus par l'architecture cible (chemins relatifs à la racine, sans .md).
CIBLES = {
    "README", "guides/commencer", "guides/designer", "guides/equipe", "guides/glossaire",
    "design/README",
    "design/direction/cadrer", "design/direction/diriger", "design/direction/premier-objet", "design/direction/boucle",
    "design/direction/standard",
    "design/savoir/README", "design/savoir/fondements", "design/savoir/qualite-creative", "design/savoir/composition",
    "design/savoir/couleur", "design/savoir/typographie", "design/savoir/images-et-sources", "design/savoir/styles",
    "design/savoir/systeme-de-design", "design/savoir/contexte", "design/savoir/techniques",
    "design/savoir/gout-et-tendances", "design/savoir/pieges", "design/savoir/connexions",
    "design/formes/README", "design/formes/choisir", "design/formes/catalogue",
    "design/produit/README", "design/produit/premier-rendu", "design/produit/interface", "design/produit/plancher",
    "design/produit/finition", "design/produit/preuve-visuelle",
    "agent/skill/SKILL", "agent/skill/references", "agent/chemins", "agent/repondre",
    "gouvernance/README", "gouvernance/principes", "gouvernance/statuts", "gouvernance/travail",
    "gouvernance/verification", "gouvernance/cloture", "gouvernance/structure", "gouvernance/integrite",
    "gouvernance/projection-machine",
    "maintenance/README", "maintenance/evolution", "maintenance/versions",
    "RETIRÉ", "HORS PRODUIT (branche refonte)",
}

# (fichier, ligne de départ, destination(s) séparées par « + », disposition, note)
R = {
"V1/official/DIRECTION.md": [
 (1, "gouvernance/principes", "réécrire", "intro ; la mention d'expérimentation ne reste qu'une fois, dans le README"),
 (5, "design/direction/diriger", "déplacer", "rôle et posture en tête de la direction (blocs ROLE, POSTURE)"),
 (30, "gouvernance/principes", "scinder", "Constitution : propriétaires, contrats, activation"),
 (44, "RETIRÉ", "retirer", "récapitulatif qui reprend le corps ; après conversion du verrou ORD-01"),
 (56, "gouvernance/principes", "fusionner", "une seule table des propriétaires"),
 (78, "gouvernance/principes", "fusionner", "architecture d'activation avec les trois contrats"),
 (94, "design/direction/standard + gouvernance/principes", "scinder", "l.104-116 standard de qualité visuelle vers le design"),
 (120, "gouvernance/principes", "déplacer", ""),
 (124, "guides/glossaire + design/direction/standard", "réécrire", "légende : termes définis à la première apparition ; étiquettes inutilisées retirées (LCF-29)"),
 (143, "gouvernance/principes", "déplacer", "relation ou contrat"),
 (149, "agent/chemins", "déplacer", "classer avant d'agir"),
 (178, "agent/chemins", "réécrire", "entrée minimale en langage clair"),
 (193, "design/direction/diriger", "déplacer", "lancement créatif (bloc MOY-PLAFOND)"),
 (223, "design/direction/cadrer", "déplacer", "cadrage du domaine ; lien vers le schéma du module"),
 (252, "agent/chemins", "déplacer", "sortie immédiate"),
 (270, "agent/chemins", "fusionner", "avec « ITER se souvient »"),
 (280, "agent/chemins", "déplacer", "table de chargement (blocs CHARGE-*) ; séparation design/gouvernance des cellules en phase 5"),
 (312, "agent/chemins", "fusionner", "chemin court : renvoi sans contenu propre"),
 (320, "design/direction/cadrer", "déplacer", "demande vague (blocs BRIEF, CONTENU) ; gabarit en prose (phase 4)"),
 (351, "guides/commencer", "déplacer", "traduction humaine"),
 (366, "design/direction/premier-objet", "déplacer", "bloc PREMIER-OBJET"),
 (430, "design/direction/diriger", "déplacer", "cible visuelle"),
 (491, "gouvernance/verification", "déplacer", "réserve sur l'ancre générée"),
 (501, "design/direction/diriger", "déplacer", "atelier de direction (blocs VER-SCENE, VER-AUDIENCE)"),
 (541, "design/direction/boucle", "déplacer", "créer puis apprendre (blocs BOUCLE-*)"),
 (613, "maintenance/evolution", "déplacer", "signaux d'apprentissage expérimental"),
 (617, "design/direction/standard", "déplacer", "les cinq règles gardées ensemble comme cadre ; détails 2 à 4 dans la gouvernance"),
 (641, "gouvernance/principes + design/direction/standard", "scinder", "règle 2 : énoncé au standard, procédure au module (bloc ANCRE)"),
 (662, "gouvernance/principes + design/direction/standard", "scinder", "règles 3 et 4 : énoncé au standard, procédure au module"),
 (689, "design/direction/standard", "déplacer", "règle 5"),
 (707, "agent/chemins", "fusionner", "avec classer avant d'agir"),
 (723, "design/produit/interface", "déplacer", "cadrage de médium et de capacité"),
 (746, "design/direction/diriger", "déplacer", "direction divergente"),
 (763, "agent/chemins", "fusionner", "routage avec la table de chargement"),
 (805, "design/direction/standard", "déplacer", "invariants de jugement"),
 (825, "gouvernance/cloture", "déplacer", "clôture de direction"),
 (833, "maintenance/evolution", "déplacer", "lecture instrumentée (MNT-01)"),
],
"V1/official/ACTION.md": [
 (1, "gouvernance/README", "réécrire", "intro"),
 (5, "gouvernance/principes", "scinder", "responsabilité ; la phrase sur la qualité du premier rendu va au produit"),
 (11, "RETIRÉ", "retirer", "carte par mode qui renvoie à la table de chargement sans la répéter"),
 (21, "agent/repondre + gouvernance/travail", "scinder", "réponse visible et trace légère (blocs SORTIE, TRACE) ; trace persistante au module"),
 (62, "gouvernance/principes", "déplacer", "quatre registres ; l'ordre de preuve P0-P3 est cité au produit"),
 (88, "gouvernance/principes", "déplacer", "portée d'action"),
 (94, "RETIRÉ", "retirer", "renvoi circulaire vers le noyau"),
 (98, "design/produit/premier-rendu", "déplacer", ""),
 (112, "design/produit/interface", "déplacer", "interface réelle"),
 (138, "gouvernance/statuts", "déplacer", ""),
 (183, "RETIRÉ", "retirer", "doublon du chemin minimal"),
 (187, "design/produit/premier-rendu", "fusionner", "principe positif de qualité"),
 (192, "design/produit/finition + gouvernance/statuts", "scinder", "quatre questions de qualité au produit ; statuts au module"),
 (205, "gouvernance/statuts", "déplacer", ""),
 (218, "gouvernance/travail", "déplacer", "conditions de départ"),
 (271, "agent/chemins", "fusionner", "chemin court ; règle « un fix local reste court »"),
 (281, "gouvernance/travail", "déplacer", "fiche de travail"),
 (352, "design/produit/preuve-visuelle", "déplacer", "mode agent seul et preuve dégradée (HON-05)"),
 (366, "gouvernance/travail", "déplacer", ""),
 (415, "agent/chemins + gouvernance/travail", "scinder", "« Faire » de chaque mode au chemin ; entrée, sortie, clôture au module"),
 (471, "gouvernance/cloture", "déplacer", ""),
 (511, "agent/repondre", "réécrire", "droits et confidentialité en version courte (HON-08)"),
 (519, "design/produit/finition", "déplacer", "condition d'arrêt du polish"),
 (525, "gouvernance/travail", "scinder", "déroulé ; la règle one-shot va à la boucle"),
 (537, "design/direction/diriger", "déplacer", "situer, traduire l'émotion, alternative située"),
 (557, "design/produit/preuve-visuelle + gouvernance/travail", "scinder", "spec visuelle"),
 (571, "design/savoir/images-et-sources + gouvernance/travail", "scinder", "sourcer et tracer"),
 (579, "design/direction/diriger", "déplacer", "contre la facilité"),
 (585, "agent/repondre", "déplacer", "écrire la direction (bloc CHECKPOINT)"),
 (596, "design/produit/finition", "déplacer", "vérifier le rendu réel ; passe créative et polish"),
 (616, "gouvernance/verification", "scinder", "déclencheurs au module"),
 (634, "design/produit/preuve-visuelle", "déplacer", "carte de hiérarchie, partition typographique, fiche d'asset"),
 (692, "gouvernance/verification", "déplacer", "contrat de composant et baseline"),
 (702, "design/produit/preuve-visuelle", "déplacer", "contrat de motion"),
 (710, "design/produit/preuve-visuelle", "déplacer", ""),
 (732, "design/produit/plancher", "déplacer", "plancher produit"),
 (736, "gouvernance/verification", "déplacer", "portée, méthodes, adéquation des preuves"),
 (776, "design/produit/plancher", "déplacer", "contrôles applicables et profils"),
 (815, "gouvernance/verification", "scinder", "vérification en contexte"),
 (819, "design/produit/finition", "déplacer", "comparaison relationnelle"),
 (827, "design/produit/finition + gouvernance/verification", "scinder", "atelier sur capture (bloc BOUCLE-ATELIER) ; formalités au module"),
 (853, "gouvernance/verification", "déplacer", ""),
 (891, "design/produit/finition", "fusionner", "corrections ancrées, avec la passe créative"),
 (897, "gouvernance/verification", "déplacer", ""),
 (911, "design/produit/finition", "déplacer", "finition sur rendu"),
 (936, "design/produit/finition", "fusionner", "contre le générique, avec la finition"),
 (944, "gouvernance/verification", "déplacer", "dérogation et péremption"),
 (980, "design/produit/plancher + gouvernance/verification", "scinder", ""),
 (982, "design/produit/plancher", "fusionner", "politique de contraste"),
 (990, "gouvernance/verification", "déplacer", "inspection et ressources"),
 (1014, "agent/chemins", "fusionner", "prérequis : une seule liste avec la table de chargement"),
 (1035, "maintenance/evolution", "déplacer", ""),
 (1059, "gouvernance/cloture + design/produit/finition", "scinder", "Q1-Q8 au module ; Q9-Q10 au produit"),
 (1076, "maintenance/evolution", "déplacer", "mesure expérimentale"),
],
"V1/official/SAVOIR.md": [
 (1, "design/savoir/README", "réécrire", "préface pour un humain ; bannière retirée"),
 (26, "gouvernance/verification", "déplacer", "sortie vers l'action"),
 (34, "agent/chemins", "déplacer", "comment l'agent lit le savoir ; jugement rapide"),
 (48, "design/savoir/README", "déplacer", "niveaux d'autorité, en annexe de lecture"),
 (66, "guides/designer", "fusionner", "routes stables, avec la carte des sujets"),
 (86, "design/savoir/fondements", "déplacer", ""),
 (169, "design/savoir/fondements + gouvernance/verification", "scinder", "cadrage au savoir ; champs d'hypothèse au module"),
 (200, "design/savoir/qualite-creative", "déplacer", ""),
 (323, "design/savoir/composition", "déplacer", "composition, densité, harmonie"),
 (356, "design/savoir/qualite-creative", "déplacer", "émotion, premier contact"),
 (395, "design/savoir/couleur", "déplacer", ""),
 (419, "design/savoir/typographie", "déplacer", ""),
 (440, "design/savoir/typographie + gouvernance/verification", "scinder", "gabarit de preuve au module"),
 (464, "design/savoir/composition", "déplacer", "jugement visuel situé, vocabulaire perceptuel"),
 (528, "design/produit/interface", "déplacer", "états pertinents"),
 (539, "design/savoir/images-et-sources + gouvernance/verification", "scinder", "sourcing au savoir ; fiche et projection au module"),
 (547, "design/savoir/images-et-sources", "déplacer", ""),
 (606, "design/savoir/images-et-sources", "déplacer", "familles visuelles (bloc MOY-ASSETS)"),
 (646, "gouvernance/verification", "déplacer", "test de sélection et de non-recyclage"),
 (654, "design/savoir/styles", "déplacer", ""),
 (738, "design/savoir/typographie", "déplacer", "ponctuation située"),
 (744, "design/savoir/pieges", "déplacer", "slop procédural"),
 (752, "design/savoir/composition", "déplacer", "vocabulaire à rendre observable"),
 (770, "design/savoir/systeme-de-design", "déplacer", ""),
 (788, "design/savoir/contexte", "déplacer", "accessibilité, fort enjeu, responsive, motion"),
 (824, "design/savoir/techniques + gouvernance/verification", "scinder", "production par médium au savoir ; preuve par médium au module"),
 (877, "design/savoir/gout-et-tendances", "déplacer", ""),
 (879, "gouvernance/verification", "déplacer", "claims externes et péremption"),
 (909, "design/savoir/gout-et-tendances", "déplacer", "goût, tendances datées, moyens ; effet liste noire à traiter en phase 5"),
 (969, "gouvernance/integrite", "déplacer", ""),
 (971, "design/savoir/pieges", "déplacer", "non-récitation, modes d'échec"),
 (1006, "gouvernance/integrite", "déplacer", ""),
 (1035, "design/savoir/README", "déplacer", "règles d'or en tête du livre"),
 (1050, "design/direction/boucle", "fusionner", "méthodologie studio (bloc BOUCLE-REPASSE)"),
],
"V1/official/BIBLIOTHEQUE.md": [
 (1, "design/formes/README", "réécrire", "rôle, public ; bannière retirée"),
 (22, "gouvernance/structure", "fusionner", "entrée prioritaire et orientation ; « zéro route est valide » reste en tête du design"),
 (51, "design/formes/choisir", "scinder", "chaîne de lecture (bloc STRUCT-OU)"),
 (63, "design/formes/choisir", "déplacer", "lecture expressive, tension, signature, thèse (blocs STRUCT-EXPRESSION, STRUCT-TENSION)"),
 (114, "maintenance/evolution", "déplacer", "préfixes canoniques"),
 (131, "gouvernance/verification", "fusionner", "types de preuve : une seule table"),
 (148, "design/formes/choisir", "déplacer", "sélection (bloc STRUCT-ACTIVATION)"),
 (175, "gouvernance/structure", "fusionner", "avant-sélection"),
 (181, "design/formes/choisir", "déplacer", ""),
 (195, "agent/chemins", "fusionner", "sélection par mode"),
 (207, "design/direction/boucle", "fusionner", "one-shot et boucle structurelle"),
 (213, "design/formes/choisir", "déplacer", "garde-fou, dérivation (champs au module), signaux de convergence (bloc STRUCT-SIGNAUX)"),
 (274, "gouvernance/structure", "déplacer", "contrat commun de route"),
 (304, "design/formes/choisir", "déplacer", "calibration locale"),
 (324, "design/formes/catalogue", "déplacer", "supports"),
 (376, "design/formes/catalogue", "déplacer", "grilles"),
 (428, "design/formes/catalogue + gouvernance/structure", "scinder", "contrat de grille ; phrase mobile au catalogue"),
 (462, "design/formes/catalogue", "déplacer", "scènes, séquence, objets"),
 (583, "gouvernance/structure", "déplacer", "contrat d'objet"),
 (606, "design/formes/catalogue", "déplacer", "micro"),
 (628, "design/produit/finition", "déplacer", "avant/après"),
 (651, "design/formes/catalogue", "déplacer", "modificateurs, composants"),
 (688, "gouvernance/structure", "déplacer", "contrat de composant partagé"),
 (708, "design/formes/catalogue", "déplacer", "échelle de responsabilité, compatibilité"),
 (775, "gouvernance/structure", "déplacer", "contrat de compatibilité"),
 (783, "design/produit/finition + gouvernance/structure", "scinder", "tests au produit ; statuts au module (PRC-01)"),
 (808, "gouvernance/structure", "déplacer", ""),
 (820, "maintenance/evolution", "déplacer", "promotion et dépréciation ; liste d'alias retirée après adaptation du contrôle"),
 (876, "gouvernance/structure", "fusionner", "test de sortie"),
],
"V1/official/CHANGELOG.md": [
 (1, "maintenance/versions", "réécrire", "en-tête de version et de révision (lu par les scripts)"),
 (10, "maintenance/versions", "réécrire", "version initiale, en court"),
 (30, "maintenance/evolution + HORS PRODUIT (branche refonte)", "scinder", "règle d'évolution et budget au produit ; journal des décisions hors produit"),
 (58, "maintenance/evolution", "déplacer", "cycle de vie des routes"),
 (72, "maintenance/evolution", "déplacer", "migration des anciens alias"),
 (86, "maintenance/versions", "fusionner", "limites, avec la section unique des limites"),
],
"RELEASE_NOTES.md": [
 (1, "maintenance/versions", "réécrire", "journal court"),
 (7, "maintenance/versions + HORS PRODUIT (branche refonte)", "scinder", "une ligne par révision au journal ; détail hors produit"),
 (79, "README", "fusionner", "présentation, points clés, contenu, parcours : déjà dans le README"),
 (119, "maintenance/README", "fusionner", "contrôles inclus, ce que le validateur atteste"),
 (152, "README", "fusionner", "limites : une seule section"),
],
"README.md": [
 (1, "README", "réécrire", "titre ; paragraphe de révision retiré"),
 (10, "guides/commencer + README", "déplacer", "porte débutant (balise ENT-01) ; résumé de trois lignes au README"),
 (25, "maintenance/versions", "déplacer", "fiche de version"),
 (39, "README", "réécrire", "mission en tête"),
 (47, "README + guides/equipe", "scinder", "installer au README ; opérateurs au guide d'équipe"),
 (71, "README", "déplacer", "constitution minimale (balise CST-01)"),
 (78, "design/README", "réécrire", "double boucle : schéma à refaire (phase 6)"),
 (100, "README", "réécrire", "structure du dépôt, nouvelle arborescence"),
 (123, "maintenance/README", "déplacer", "source de vérité, distributions, reprise"),
 (171, "maintenance/README", "déplacer", "validation"),
 (202, "README", "fusionner", "limites : section unique"),
],
"V1/official/README.md": [
 (1, "README + guides/designer", "fusionner", "sources normatives : présentées par les portes"),
],
"V1/official/QUICKSTART.md": [
 (1, "guides/equipe", "réécrire", "guide opérateur devenu guide d'équipe"),
 (31, "guides/equipe", "fusionner", "carte de résolution"),
 (37, "guides/designer + guides/equipe", "scinder", "profondeur de lecture, façade, constitution"),
 (61, "guides/equipe", "déplacer", "ligne de travail et parcours complet"),
 (113, "guides/equipe", "fusionner", "choisir le mode : en clair, renvoi au chemin de l'agent"),
 (144, "guides/commencer + guides/equipe", "scinder", "qualité dès le premier rendu ; one-shot ; réponse"),
 (197, "RETIRÉ", "phase 5", "exemple complet recopiable : à retirer ou rendre abstrait (touche l'agent)"),
 (248, "guides/equipe", "déplacer", "observer, persister, fermer"),
 (281, "guides/equipe", "fusionner", "sources propriétaires : déjà dans les portes"),
],
"V1/official/GLOSSAIRE.md": [
 (1, "guides/glossaire", "réécrire", "réduit après le vocabulaire de la phase 2"),
 (82, "guides/commencer", "fusionner", "commencer sans vocabulaire"),
],
"V1/official/READING_MAP.md": [
 (1, "guides/designer", "réécrire", "utilisation"),
 (11, "agent/chemins", "fusionner", "chemin de démarrage, constitution, routage minimal : déjà au chemin de l'agent"),
 (40, "guides/designer", "déplacer", "carte des sujets en noms clairs (lue par le lecteur, SUJ-01)"),
 (69, "guides/designer", "déplacer", "combinaisons par résultat recherché"),
 (107, "design/savoir/connexions", "déplacer", "connexions C01-C09 : savoir quand plusieurs domaines se croisent (--connexions)"),
 (243, "guides/designer", "déplacer", "activation multi-perspective"),
 (261, "RETIRÉ", "retirer", "handoff minimal commun : doublon de la réponse de l'agent"),
 (283, "maintenance/README", "déplacer", "résolution des routes"),
 (298, "RETIRÉ", "retirer", "table de locators : remplacée par le sommaire du lecteur"),
 (332, "guides/designer", "déplacer", "condition d'arrêt"),
],
"V1/official/ORCHESTRATION_MAP.md": [
 (1, "RETIRÉ", "retirer", "pointeur sans contenu propre ; 5 citations ou contrôles à adapter"),
],
"skills/design-governance-practice/SKILL.md": [
 (6, "agent/skill/SKILL", "phase 5", "noyau compilé : identique à l'octet près jusqu'à la phase 5, quelle que soit la place des blocs"),
],
"skills/design-governance-practice/references/canonical_minimum.md": [
 (1, "agent/skill/references", "fusionner", "doublons retirés"),
],
"skills/design-governance-practice/references/examples.md": [
 (1, "agent/skill/references", "phase 5", "exemples recopiables ; SIMULATED non défini"),
],
"skills/design-governance-practice/references/flow.md": [
 (1, "design/README", "réécrire", "schéma à refaire (phase 6) ou retirer"),
],
"skills/design-governance-practice/references/machine_projection.md": [
 (1, "gouvernance/projection-machine", "déplacer", "doublons avec le README et l'exemple de schéma retirés (LCF-26, LCF-41)"),
],
}


def headings(path):
    fence, out = False, []
    lines = (REPO / path).read_text(encoding="utf-8").splitlines()
    for n, line in enumerate(lines, 1):
        if line.strip().startswith("```"):
            fence = not fence
        elif not fence and re.match(r"^#{1,3} ", line):
            out.append((n, len(line) - len(line.lstrip("#")), line.lstrip("#").strip()))
    sizes = []
    for i, (n, lvl, t) in enumerate(out):
        end = out[i + 1][0] if i + 1 < len(out) else len(lines) + 1
        sizes.append(sum(len(x) + 1 for x in lines[n - 1:end - 1]))
    return [(n, lvl, t, s) for (n, lvl, t), s in zip(out, sizes)]


docs = subprocess.run(["git", "-C", str(REPO), "ls-files", "*.md"], capture_output=True, text=True, check=True).stdout.split()
errors, rows = [], []
for path in docs:
    rules = sorted(R.get(path, []))
    if not rules:
        errors.append(f"aucune règle pour {path}")
        continue
    for n, lvl, title, size in headings(path):
        rule = [r for r in rules if r[0] <= n]
        if not rule:
            errors.append(f"{path}:{n} avant la première règle")
            continue
        _, dest, disp, note = rule[-1]
        for d in dest.split(" + "):
            if d not in CIBLES:
                errors.append(f"{path}:{n} destination inconnue « {d} »")
        rows.append({"fichier": path, "ligne": n, "niveau": lvl, "titre": title, "caracteres": size,
                     "destination": dest, "disposition": disp, "note": note if rule[-1][0] == n else ""})
for path, rules in R.items():
    lines = {n for n, *_ in headings(path)} if (REPO / path).exists() else set()
    for r in rules:
        if r[0] not in lines:
            errors.append(f"règle sur une ligne qui n'est pas un titre : {path}:{r[0]}")

out_csv, out_md = Path(sys.argv[1]), Path(sys.argv[2])
with out_csv.open("w", newline="", encoding="utf-8") as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0]))
    w.writeheader()
    w.writerows(rows)

par_dest = defaultdict(int)
for r in rows:
    dests = r["destination"].split(" + ")
    for d in dests:
        par_dest[d] += r["caracteres"] // len(dests)
disp = Counter(r["disposition"] for r in rows)
md = ["# Table de correspondance — synthèse", "",
      f"Produit par `ARCHI/outils/correspondance.py`. {len(rows)} sections (titres de niveau 1 à 3) de {len(docs)} documents ; "
      "le détail est dans `correspondance.csv`. Les tailles d'une section scindée sont réparties à parts égales entre ses "
      "destinations : c'est un ordre de grandeur, le partage exact se fait au rangement.", "",
      "## Dispositions", "", "| Disposition | Sections |", "|---|---:|"]
md += [f"| {k} | {v} |" for k, v in disp.most_common()]
md += ["", "## Volume approximatif par destination (caractères)", "", "| Destination | Caractères |", "|---|---:|"]
md += [f"| `{k}` | {v:,} |".replace(",", " ") for k, v in sorted(par_dest.items(), key=lambda x: -x[1])]
tot = defaultdict(int)
for k, v in par_dest.items():
    tot[k.split("/")[0] if "/" in k else k] += v
md += ["", "## Par grande partie", "", "| Partie | Caractères |", "|---|---:|"]
md += [f"| {k} | {v:,} |".replace(",", " ") for k, v in sorted(tot.items(), key=lambda x: -x[1])]
md += ["", "## Contrôle", "", "Aucune erreur." if not errors else "\n".join(f"- {e}" for e in errors)]
out_md.write_text("\n".join(md) + "\n", encoding="utf-8")
print(f"{len(rows)} sections ; erreurs : {len(errors)}")
for e in errors:
    print(" -", e)
