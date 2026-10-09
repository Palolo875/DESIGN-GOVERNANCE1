#!/usr/bin/env python3
"""Resolve a documented route and print only its owning section.

Résolution en trois étapes (READING_MAP, « Résolution des routes ») :
1. table « Locators principaux » (raccourcis et sous-locators) ;
2. préfixe : titre unique du propriétaire qui commence par le locator ;
3. sous-locator X/Y/Z : sous-titre commençant par Z dans le bloc de X/Y.
Plusieurs titres : « locator ambigu ». Les titres placés dans un bloc de code sont
ignorés. Un bloc servi exclut les sous-blocs qui portent leur propre locator.
Comme le validateur de carte : locator de table unique, propriétaire et titre cohérents, porteur unique.
Les identifiants structurels documentés (GRID/…, OBJECT/…, etc.) sont des raccourcis
vers BIBLIOTHEQUE : titre exact, ou section porteuse si l'identifiant est une ligne de table.
Un identifiant absent, ambigu ou présent seulement dans un bloc de code est refusé.
Une adresse lisible (`savoir/couleur`, `produit/plancher`, préfixe `design/` facultatif ; table ADRESSES)
est servie comme le locator qu'elle désigne ; l'ancien locator reste accepté.

Recherche de routes par terme : `--trouver TERME` cherche le terme en mots entiers, avec ses alias
(synonymes et traductions stricts d'ALIAS_GROUPS), puis en correspondance partielle, puis mot à mot sur
une même ligne ; enfin, pour une phrase (« quelle police choisir »), mot par mot avec racines et alias, les routes
classées par la rareté des mots qu'elles portent. Les routes sont classées et les premières affichées (`--tout` pour toutes).
La casse et les accents sont ignorés, pas le sens. `--sommaire [LOCATOR]` liste les routes et leur rôle,
ou les sous-sections d'une route. `--guides` ajoute les documents d'orientation
(guides du corpus, README racine, références de la skill), identifiés séparément. Les marqueurs internes sont exclus. Aucun résultat ne prouve l'absence du savoir.

`--connexions [Cxx]` expose un sommaire ou une connexion située de READING_MAP,
avec ses sources résolues et la révision propriétaire. Aucun classement,
diagnostic, choix de pertinence ou génération de snapshot n'est automatisé.
"""
from __future__ import annotations

import argparse
import os
import math
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OFFICIAL = ROOT / "V1" / "official" if (ROOT / "V1" / "official").is_dir() else ROOT / "official"
PREFIXES = ("DIRECTION", "ACTION", "SAVOIR", "BIBLIOTHEQUE", "CHANGELOG")
STRUCTURE_KINDS = ("SUPPORT", "GRID", "SCENE", "OBJECT", "MICRO", "MODIFIER", "LAYER")
STRUCTURE_PARENTS = {kind: ("COMPONENTS" if kind == "LAYER" else kind) for kind in STRUCTURE_KINDS}
HEADING_LOCATOR = re.compile(rf"^#+\s+`?((?:{'|'.join(PREFIXES)})/[A-Za-z0-9_\-]+)`?(?=\s|$)")
CONNECTION_FIELDS = ("Condition et décision", "Sources", "Intervention et effet attendu",
                     "Contre-indication et alternative", "Moyens et limites", "Observation et réexamen")
CONNECTION_HEADING = re.compile(r"^### (C[0-9]{2}) — (.+)$")
SOURCE_LOCATOR = re.compile(rf"(?:{'|'.join(PREFIXES)})(?:/[A-Z0-9_\-]+){{0,2}}")


class RouteError(Exception):
    """Échec de résolution gouverné."""


def fail(message: str) -> "NoReturn":
    raise SystemExit(f"ROUTE READ FAILED — {message}")


def parse_route_rows(text: str) -> list[tuple[str, str, list[str]]]:
    """Lignes de la table : (locator, fichier propriétaire, chaîne de titres). Les doublons sont conservés."""
    if "## Locators principaux" not in text:
        raise RouteError("section des locators principaux absente")
    section = text.split("## Locators principaux", 1)[1]
    if "## Condition d’arrêt" in section:
        section = section.split("## Condition d’arrêt", 1)[0]
    rows: list[tuple[str, str, list[str]]] = []
    for line in section.splitlines():
        if not line.startswith("| `") or " | `" not in line or not line.endswith(" |"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) != 2:
            continue
        locator_cell, destination = cells
        if not (locator_cell.startswith("`") and locator_cell.endswith("`")):
            continue
        match = re.fullmatch(r"`([^`]+)`\s+—\s+`(.+)`", destination)
        if not match:
            raise RouteError(f"destination mal formée pour {locator_cell}")
        owner_name, chain = match.groups()
        headings = [part.replace("\\`", "`").strip() for part in re.split(r"`\s+›\s+`", chain)]
        rows.append((locator_cell[1:-1], owner_name.strip(), headings))
    return rows


def parse_routes(text: str) -> dict[str, tuple[str, list[str]]]:
    """Un locator répété dans la table est refusé (la dernière ligne ne gagne plus)."""
    routes: dict[str, tuple[str, list[str]]] = {}
    for locator, owner, chain in parse_route_rows(text):
        if locator in routes:
            raise RouteError(f"locator en double dans READING_MAP : {locator}")
        routes[locator] = (owner, chain)
    return routes


def non_code_lines(lines: list[str]):
    """(index, ligne) hors blocs clôturés ; caractère et longueur préservés."""
    fence = None
    for index, line in enumerate(lines):
        marker = re.match(r'^ {0,3}(`{3,}|~{3,})(.*)$', line)
        if fence:
            if marker and marker[1][0] == fence[0] and len(marker[1]) >= fence[1] and not marker[2].strip():
                fence = None
            continue
        if marker and not (marker[1][0] == '`' and '`' in marker[2]):
            fence = (marker[1][0], len(marker[1]))
            continue
        yield index, line


def headings(lines: list[str]) -> list[tuple[int, int, str]]:
    """(index, niveau, ligne) des titres, hors blocs de code (F-RRT-001)."""
    found = []
    for index, line in non_code_lines(lines):
        if line.startswith("#"):
            level = len(line) - len(line.lstrip("#"))
            if level <= 6 and line[level:level + 1] in (" ", ""):
                found.append((index, level, line.strip()))
    return found


def heading_locator(heading: str) -> str | None:
    match = HEADING_LOCATOR.match(heading)
    return match.group(1) if match else None


def block_end(lines: list[str], heads: list[tuple[int, int, str]], start: int) -> int:
    level = next(lvl for idx, lvl, _ in heads if idx == start)
    return next((idx for idx, lvl, _ in heads if idx > start and lvl <= level), len(lines))


# Lieux : nom historique d’une source (« SAVOIR.md ») → fichiers, relatifs à la racine, qui portent aujourd’hui
# son contenu. Un nom absent de la table désigne le fichier du même nom dans OFFICIAL. Le rangement déplace le
# texte puis met à jour cette table, et elle seule : lecteur, compilation du noyau et validateurs passent par elle.
LIEUX: dict[str, tuple[str, ...]] = {
    # Rangement, lot 4 : la gouvernance formelle part dans le module gouvernance/ (texte inchangé).
    # Rangement, lot 5 : le cœur du design part dans design/ (direction, savoir, formes, produit ; texte inchangé).
    # Rangement, lot 6 : le chemin de l'agent (classer, quoi lire) et sa réponse partent dans agent/ (texte inchangé).
    # Rangement, lot 7a : l'évolution du système et le journal des versions partent dans maintenance/ (texte inchangé).
    "DIRECTION.md": ("V1/official/DIRECTION.md", "agent/chemins.md", "gouvernance/principes.md", "gouvernance/cloture.md",
                     "design/direction/cadrer.md", "design/direction/premier-objet.md", "design/direction/diriger.md",
                     "design/direction/boucle.md", "design/direction/standard.md", "design/produit/interface.md"),
    "ACTION.md": ("V1/official/ACTION.md", "agent/chemins.md", "agent/repondre.md", "gouvernance/principes.md", "gouvernance/statuts.md", "gouvernance/travail.md",
                  "gouvernance/verification.md", "gouvernance/cloture.md", "design/produit/premier-rendu.md",
                  "design/produit/plancher.md", "design/produit/finition.md", "design/produit/preuve-visuelle.md",
                  "maintenance/evolution.md"),
    "SAVOIR.md": ("V1/official/SAVOIR.md", "agent/chemins.md", "design/savoir/fondements.md", "design/savoir/qualite-creative.md",
                  "design/savoir/typographie.md", "design/savoir/composition.md", "design/savoir/images-et-sources.md",
                  "design/savoir/styles.md", "design/savoir/systeme-de-design.md", "design/savoir/contexte.md",
                  "design/savoir/techniques.md", "design/savoir/gout-et-tendances.md"),
    "BIBLIOTHEQUE.md": ("V1/official/BIBLIOTHEQUE.md", "gouvernance/structure.md", "design/formes/choisir.md",
                        "design/formes/catalogue.md", "maintenance/evolution.md"),
    "CHANGELOG.md": ("maintenance/versions.md", "maintenance/evolution.md"),
    # Rangement, lot 7b : guides par public (équipe, designer, glossaire) et connexions du savoir (texte inchangé).
    "QUICKSTART.md": ("guides/equipe.md",),
    "GLOSSAIRE.md": ("guides/glossaire.md",),
    "READING_MAP.md": ("V1/official/READING_MAP.md", "guides/designer.md", "design/savoir/connexions.md",
                       "maintenance/README.md"),
}


# Adresses lisibles (architecture cible, branche refonte : ARCHI/architecture.md §6) → locator actuel.
# On peut les donner au lecteur dès maintenant ; l'ancien locator reste accepté pendant toute la V1.
# Le préfixe « design/ » est facultatif. Quand une route change de titre (phase de langue), seule cette table change.
ADRESSES: dict[str, str] = {
    "direction/cadrer#demande-vague": "DIRECTION/EXTERNAL-START", "direction/cadrer#domaine": "DIRECTION/DOMAIN-FRAME",
    "direction/diriger#lancement": "DIRECTION/CREATIVE-BOOT", "direction/diriger#cible-visuelle": "DIRECTION/VISUAL_TARGET",
    "direction/diriger#atelier": "DIRECTION/DIRECTION-ATELIER", "direction/premier-objet": "DIRECTION/FIRST-OBJECT",
    "direction/boucle": "DIRECTION/DOUBLE-LOOP",
    "savoir/fondements": "SAVOIR/FRAME", "savoir/qualite-creative": "SAVOIR/CRAFT",
    "savoir/qualite-creative#ambition": "SAVOIR/CRAFT/CFT-00", "savoir/qualite-creative#forme-situee": "SAVOIR/CRAFT/CFT-01",
    "savoir/qualite-creative#registres": "SAVOIR/CRAFT/CFT-02", "savoir/qualite-creative#emotion": "SAVOIR/CRAFT/CFT-04",
    "savoir/qualite-creative#premier-contact": "SAVOIR/CRAFT/CFT-04a", "savoir/composition": "SAVOIR/CRAFT/CFT-03",
    "savoir/composition#jugement-visuel": "SAVOIR/STATE", "savoir/couleur": "SAVOIR/CRAFT/CFT-05",
    "savoir/typographie": "SAVOIR/TYPE", "savoir/images-et-sources": "SAVOIR/SOURCE",
    "savoir/images-et-sources#familles": "SAVOIR/DESIGN-ATLAS", "savoir/styles": "SAVOIR/STYLE",
    "savoir/systeme-de-design": "SAVOIR/SYSTEM", "savoir/contexte": "SAVOIR/CONTEXT", "savoir/techniques": "SAVOIR/TECH",
    "savoir/gout-et-tendances": "SAVOIR/TOOLS", "savoir/gout-et-tendances#tendances-datees": "SAVOIR/TOOLS/CONVERGENCE",
    "savoir/gout-et-tendances#ressources": "SAVOIR/TOOLS/MOYENS",
    "formes/choisir": "BIBLIOTHEQUE/SELECT", "formes/choisir#lire": "BIBLIOTHEQUE/READ",
    "formes/choisir#tension": "BIBLIOTHEQUE/TENSION", "formes/choisir#signature": "BIBLIOTHEQUE/SIGNATURE",
    "formes/choisir#deriver": "BIBLIOTHEQUE/DERIVE", "formes/catalogue#supports": "BIBLIOTHEQUE/SUPPORT",
    "formes/catalogue#grilles": "BIBLIOTHEQUE/GRID", "formes/catalogue#scenes": "BIBLIOTHEQUE/SCENE",
    "formes/catalogue#sequence": "BIBLIOTHEQUE/SEQUENCE", "formes/catalogue#objets": "BIBLIOTHEQUE/OBJECT",
    "formes/catalogue#micro": "BIBLIOTHEQUE/MICRO", "formes/catalogue#modificateurs": "BIBLIOTHEQUE/MODIFIER",
    "formes/catalogue#composants": "BIBLIOTHEQUE/COMPONENTS", "formes/catalogue#compatibilite": "BIBLIOTHEQUE/COMPAT",
    "produit/premier-rendu": "ACTION/FIRST-RENDER", "produit/interface": "ACTION/UI-UX-REALITY",
    "produit/plancher": "ACTION/GATE-A", "produit/plancher#contraste": "ACTION/POLICIES",
    "produit/finition": "ACTION/GATE-C", "produit/finition#contre-le-generique": "ACTION/ANTI-SLOP",
    "produit/preuve-visuelle": "ACTION/VISUAL_PROOF",
    "agent/chemins#classer": "DIRECTION/START", "agent/chemins#quoi-lire": "DIRECTION/CHARGE",
    "agent/chemins#chemin-court": "ACTION/FAST-PATH", "agent/chemins#lire-le-savoir": "SAVOIR/READ",
    "agent/chemins#jugement-rapide": "SAVOIR/JUGEMENT-COURT", "agent/chemins#prerequis": "ACTION/ROUTING",
    "agent/chemins#modes": "ACTION/RUN", "agent/chemins#retouche": "ACTION/RUN-LITE",
    "agent/chemins#iteration": "ACTION/RUN-ITER", "agent/chemins#ecran": "ACTION/RUN-STANDARD",
    "agent/chemins#direction": "ACTION/RUN-DIRECTION", "agent/chemins#systeme": "ACTION/RUN-SYSTEM",
    "agent/repondre": "ACTION/HANDOFF",
    "gouvernance/principes#relation-ou-contrat": "DIRECTION/SERVICE-BOUNDARY",
    "gouvernance/principes#portee": "ACTION/AUTHORITY", "gouvernance/statuts": "ACTION/STATUS",
    "gouvernance/travail": "ACTION/RUN_CARD", "gouvernance/travail#conditions": "ACTION/PRECONDITION",
    "gouvernance/travail#deroule": "ACTION/PIPELINE-DIRECTION", "gouvernance/cloture": "ACTION/CLOSE-PACKAGE",
    "gouvernance/cloture#test-de-sortie": "ACTION/CLOSE-EXIT-CHECK", "gouvernance/verification": "ACTION/GATE-B",
    "gouvernance/verification#contrats": "ACTION/STRUCTURED-PROOF", "gouvernance/verification#derogation": "ACTION/OVERRIDE",
    "gouvernance/structure": "BIBLIOTHEQUE/CONTRACTS", "gouvernance/structure#avant-selection": "BIBLIOTHEQUE/AVANT-SELECTION",
    "gouvernance/structure#controle": "BIBLIOTHEQUE/GATE", "gouvernance/integrite": "SAVOIR/INTEGRITY",
    "maintenance/evolution": "ACTION/MAINTENANCE", "maintenance/evolution#routes": "BIBLIOTHEQUE/EVOLUTION",
    "guides/designer#routes": "SAVOIR/ROUTING",
}
# Renvois sans contenu propre : pas d'adresse lisible, l'ancien locator reste servi.
SANS_ADRESSE = {"DIRECTION/FAST-PATH"}
ADRESSE_DE = {old: new for new, old in ADRESSES.items()}


def adresse(locator: str) -> str:
    """Locator actuel pour une adresse lisible (préfixe design/ facultatif) ; sinon le locator tel quel."""
    key = locator.strip().removeprefix("design/")
    return ADRESSES.get(key, locator)


def chemin_lieu(rel: str) -> Path:
    """Chemin d’une entrée de LIEUX ; « V1/official/ » désigne le dossier des sources (OFFICIAL), quelle que soit la disposition."""
    return OFFICIAL / rel[len("V1/official/"):] if rel.startswith("V1/official/") else ROOT / rel


def lieu(name: str) -> list[Path]:
    """Fichiers qui portent aujourd’hui le contenu de la source historique `name`, dans l’ordre de lecture."""
    if name in LIEUX:
        return [chemin_lieu(p) for p in LIEUX[name]]
    return [OFFICIAL / name]


ORIGINE = re.compile(r"^<!-- origine:([A-Za-z_]+\.md) -->$")


def part_de(path: Path, name: str) -> str:
    """Texte d’un fichier qui vient de la source `name`. Un fichier qui reçoit plusieurs sources marque l’origine
    de chaque section (`<!-- origine:NOM.md -->`) ; sans marque, tout le fichier vient de sa source."""
    lines = path.read_text(encoding="utf-8").split("\n")
    if not any(ORIGINE.match(l) for l in lines):
        return "\n".join(lines)
    kept, current = [], None
    for line in lines:
        m = ORIGINE.match(line)
        if m:
            current = m.group(1)
        elif current == name:
            kept.append(line)
    return "\n".join(kept)


def lieu_texte(name: str) -> str:
    """Texte de la source historique `name` (ses parts, fichier par fichier) ; échoue si aucun fichier n’existe."""
    paths = [p for p in lieu(name) if p.is_file()]
    if not paths:
        raise FileNotFoundError(name)
    return "\n".join(part_de(p, name) for p in paths)


def carte() -> str:
    """Texte de la carte de lecture (READING_MAP), à ses lieux actuels : table des routes, sujets, connexions."""
    try:
        return lieu_texte("READING_MAP.md")
    except FileNotFoundError:
        raise RouteError("READING_MAP.md absent")


def lieu_lignes(name: str) -> list[str]:
    return lieu_texte(name).splitlines()


def origines(path: Path) -> set[str]:
    """Sources historiques dont le fichier `path` porte du contenu."""
    target = path.resolve()
    names = {n for n, rels in LIEUX.items() if any(chemin_lieu(r).resolve() == target for r in rels)}
    if path.is_file():
        marked = {m.group(1) for m in map(ORIGINE.match, path.read_text(encoding="utf-8").split("\n")) if m}
        if marked:
            return marked
    if path.parent.resolve() == OFFICIAL.resolve() and path.name not in LIEUX:
        names.add(path.name)
    return names


def nom(path: Path) -> str:
    """Nom affiché : nom simple dans OFFICIAL, chemin relatif ailleurs."""
    if path.parent.resolve() == OFFICIAL.resolve():
        return path.name
    try:
        return path.resolve().relative_to(ROOT.resolve()).as_posix()
    except ValueError:
        return path.name


def noms_officiels() -> list[str]:
    """Noms historiques des fichiers officiels (présents dans OFFICIAL ou déclarés dans LIEUX)."""
    return sorted({p.name for p in OFFICIAL.glob("*.md")} | set(LIEUX))


def fichiers_officiels() -> list[Path]:
    """Tous les fichiers qui portent aujourd’hui le contenu officiel, sans doublon, dans un ordre stable."""
    seen, out = set(), []
    for name in noms_officiels():
        for path in lieu(name):
            if path.is_file() and path.resolve() not in seen:
                seen.add(path.resolve())
                out.append(path)
    return out


def sources_normatives() -> list[Path]:
    seen, out = set(), []
    for prefix in PREFIXES:
        for path in lieu(f"{prefix}.md"):
            if path.resolve() not in seen:
                seen.add(path.resolve())
                out.append(path)
    return out


def porteur(name: str, root_locator: str) -> Path:
    """Fichier de la source `name` qui porte le titre de `root_locator` ; le premier fichier si aucun ne le porte."""
    paths = lieu(name)
    carriers = [p for p in paths if p.is_file()
                and any(heading_locator(t) == root_locator for _, _, t in headings(p.read_text(encoding="utf-8").splitlines()))]
    if len(carriers) > 1:
        raise RouteError(f"locator ambigu : {root_locator} porté par {', '.join(nom(p) for p in carriers)}")
    return carriers[0] if carriers else paths[0]


def owner_file(locator: str) -> Path:
    prefix = locator.split("/", 1)[0]
    if prefix not in PREFIXES:
        raise RouteError(f"locator inconnu : {locator}")
    return porteur(f"{prefix}.md", "/".join(locator.split("/")[:2]))


def _unique(candidates: list[int], lines: list[str], locator: str) -> int:
    if len(candidates) > 1:
        shown = " | ".join(lines[i].strip() for i in candidates)
        raise RouteError(f"locator ambigu : {locator} ; candidats : {shown}")
    return candidates[0]


def parse_connections(text: str) -> tuple[str, dict[str, dict[str, str]]]:
    """Index dérivé : une révision et des entrées explicites, sans inférence de pertinence."""
    lines = text.splitlines()
    heads = headings(lines)
    starts = [i for i, _, h in heads if h == "## Connexions situées"]
    if len(starts) != 1:
        raise RouteError("index des connexions situé absent ou multiple")
    start, end = starts[0], block_end(lines, heads, starts[0])
    child_heads = [(i, h) for i, level, h in heads if start < i < end and level == 3]
    intro_end = child_heads[0][0] if child_heads else end
    revisions = re.findall(r"^\*\*Base de sources :\*\* `([^`]+)`\.$", "\n".join(lines[start:intro_end]), re.M)
    if len(revisions) != 1:
        raise RouteError("révision de l’index absente ou multiple")
    entries: dict[str, dict[str, str]] = {}
    for index, heading in child_heads:
        match = CONNECTION_HEADING.fullmatch(heading)
        if not match:
            if heading.startswith("### C"):
                raise RouteError(f"identifiant de connexion mal formé : {heading}")
            continue
        key, title = match.groups()
        if key in entries:
            raise RouteError(f"connexion en double : {key}")
        body = "\n".join(lines[index + 1:block_end(lines, heads, index)]).strip()
        fields: dict[str, str] = {}
        matches = list(re.finditer(r"^\*\*([^*\n]+)\.\*\*\s*", body, re.M))
        for number, field in enumerate(matches):
            name = field.group(1)
            if name not in CONNECTION_FIELDS or name in fields:
                raise RouteError(f"champ inconnu ou répété dans {key} : {name}")
            next_start = matches[number + 1].start() if number + 1 < len(matches) else len(body)
            fields[name] = body[field.end():next_start].strip()
        missing = [name for name in CONNECTION_FIELDS if not fields.get(name)]
        if missing:
            raise RouteError(f"connexion {key} incomplète : {', '.join(missing)}")
        locators = re.findall(r"`([^`]+)`", fields["Sources"])
        if not locators or any(not SOURCE_LOCATOR.fullmatch(value) for value in locators):
            raise RouteError(f"sources de connexion absentes ou non propriétaires : {key}")
        if len(locators) != len(set(locators)):
            raise RouteError(f"source répétée dans {key}")
        entries[key] = {"title": title, "body": body, **fields}
    if not entries:
        raise RouteError("index des connexions vide")
    return revisions[0], entries


def connection_sources(entry: dict[str, str], routes: dict[str, tuple[str, list[str]]] | None = None) -> list[tuple[str, Path, int, str]]:
    """Retourne les propriétaires retrouvables ; aucune lecture sémantique automatique."""
    sources = []
    for locator in re.findall(r"`([^`]+)`", entry["Sources"]):
        if locator in PREFIXES:
            path = owner_file(locator)
            if not path.is_file():
                raise RouteError(f"propriétaire absent : {path.name}")
            lines, index = path.read_text(encoding="utf-8").splitlines(), 0
            if not lines:
                raise RouteError(f"propriétaire vide : {path.name}")
        else:
            path, lines, index = resolve(locator, routes)
        sources.append((locator, path, index + 1, lines[index]))
    return sources


def connections(text: str | None = None) -> tuple[str, dict[str, dict[str, str]]]:
    """Refuse un index périmé ou non résolu avant de l’exposer."""
    if text is None:
        text = carte()
    revision, entries = parse_connections(text)
    try:
        changelog_text = lieu_texte("CHANGELOG.md")
    except FileNotFoundError:
        raise RouteError("propriétaire absent : CHANGELOG.md")
    versions = re.findall(r"^\*\*Révision :\*\*\s*`([^`]+)`", changelog_text, re.M)
    if len(versions) != 1 or revision != versions[0]:
        raise RouteError("révision des connexions différente du CHANGELOG ; réexaminer les sources")
    routes = parse_routes(text)
    for entry in entries.values():
        connection_sources(entry, routes)
    return revision, entries


def resolve(locator: str, routes: dict[str, tuple[str, list[str]]] | None = None) -> tuple[Path, list[str], int]:
    """Renvoie (fichier, lignes, index du titre servi). Accepte aussi une adresse lisible (table ADRESSES)."""
    locator = adresse(locator)
    parts = locator.split("/")
    if len(parts) == 2 and parts[0] in STRUCTURE_PARENTS:
        locator = f"BIBLIOTHEQUE/{STRUCTURE_PARENTS[parts[0]]}/{parts[1]}"
    elif len(parts) == 3 and parts[0] == "BIBLIOTHEQUE" and parts[1] in STRUCTURE_PARENTS:
        locator = f"BIBLIOTHEQUE/{STRUCTURE_PARENTS[parts[1]]}/{parts[2]}"
    if routes is None:
        routes = parse_routes(carte())
    if locator in routes:  # 1. table
        owner_name, chain = routes[locator]
        root_locator = "/".join(locator.split("/")[:2])
        # C11 : mêmes contrôles que validate_reading_map, pour le lecteur autonome.
        if owner_name != f"{locator.split('/', 1)[0]}.md":
            raise RouteError(f"propriétaire incohérent : {locator} → {owner_name}")
        if not chain or heading_locator(chain[0]) != root_locator:
            raise RouteError(f"destination ne correspond pas au locator : {locator} → {chain[0] if chain else '(vide)'}")
        path = porteur(owner_name, root_locator)
        if not path.is_file():
            raise RouteError(f"propriétaire absent : {owner_name}")
        lines = path.read_text(encoding="utf-8").splitlines()
        heads = headings(lines)
        carriers = [idx for idx, _, text in heads if heading_locator(text) == root_locator]
        if len(carriers) > 1:  # porteur dupliqué ; l'absence de titre est diagnostiquée plus bas (titre introuvable)
            _unique(carriers, lines, root_locator)
        low, high, index = 0, len(lines), -1
        for heading in chain:
            candidates = [idx for idx, _, text in heads if low <= idx < high and text == heading]
            if not candidates:
                raise RouteError(f"titre introuvable dans {owner_name} : {heading}")
            index = _unique(candidates, lines, locator)
            low, high = index + 1, block_end(lines, heads, index)
        return path, lines, index
    path = owner_file(locator)
    if not path.is_file():
        raise RouteError(f"propriétaire absent : {nom(path)}")
    lines = path.read_text(encoding="utf-8").splitlines()
    heads = headings(lines)
    candidates = [idx for idx, _, text in heads if heading_locator(text) == locator]  # 2. préfixe
    if candidates:
        return path, lines, _unique(candidates, lines, locator)
    parent, _, leaf = locator.rpartition("/")
    if parent.count("/") >= 1:  # 3. sous-locator X/Y/Z
        parent_path, parent_lines, parent_index = resolve(parent, routes)
        if parent_path == path:
            end = block_end(lines, heads, parent_index)
            kind = next((k for k, p in STRUCTURE_PARENTS.items() if parent == f"BIBLIOTHEQUE/{p}"), None)
            structure_id = f"{kind}/{leaf}"
            is_structure = kind is not None
            names = [leaf, structure_id] if is_structure else [leaf]
            pattern = re.compile(rf"^#+\s+`?(?:{'|'.join(re.escape(n) for n in names)})`?(?=\s|$)")
            sub = [idx for idx, _, text in heads if parent_index < idx < end and pattern.match(text)]
            if sub:
                return path, lines, _unique(sub, lines, locator)
            if is_structure:
                # Les objets et micro-interfaces sont parfois des lignes, pas des titres.
                # Renvoyer alors leur section porteuse, sans inventer un sous-bloc.
                rows = []
                row_pattern = re.compile(rf"^\s*\|\s*`{re.escape(structure_id)}`\s*\|")
                for i, line in non_code_lines(lines):
                    if parent_index < i < end and row_pattern.match(line):
                        rows.append(i)
                if len(rows) > 1:
                    raise RouteError(f"identifiant structurel ambigu : {structure_id}")
                if rows:
                    return path, lines, parent_index
    raise RouteError(f"locator inconnu : {locator}")


def non_utf8(root: Path) -> list[str]:
    """Fichiers Markdown du package illisibles en UTF-8, nommés avant toute lecture."""
    bad = []
    for path in sorted(root.rglob("*.md")):
        if any(part in {".build", "dist", "__pycache__", ".git", ".dist.previous"} for part in path.relative_to(root).parts):
            continue
        try:
            path.read_bytes().decode("utf-8")
        except UnicodeDecodeError as exc:
            bad.append(f"{path.relative_to(root)} (octet {exc.start})")
    return bad


CONCEPT_MARKER = re.compile(r"^\s*<!-- (?:concept:[A-Z0-9\-]+|noyau:(?:début|fin) [A-Z0-9\-]+|origine:[A-Za-z_]+\.md) -->\s*$")


def served_lines(lines: list[str], index: int) -> list[tuple[int, str]]:
    """(index source, texte servi), avec les mêmes exclusions pour lecture et recherche."""
    heads = headings(lines)
    titles = {idx: text for idx, _, text in heads}
    end = block_end(lines, heads, index)
    served, skip_until = [], -1
    for i in range(index, end):
        if i < skip_until:
            continue
        head = titles.get(i)
        own = heading_locator(head) if head and i != index else None
        if own:
            served.append((i, f"> `{own}` : servi séparément"))
            skip_until = block_end(lines, heads, i)
            continue
        if CONCEPT_MARKER.match(lines[i]):
            continue
        served.append((i, lines[i]))
    return served


def extract(lines: list[str], index: int) -> list[str]:
    """Bloc du titre servi, sans les sous-blocs porteurs de leur propre locator."""
    return [text for _, text in served_lines(lines, index)]


CORE_START = re.compile(r"^\s*<!-- noyau:début ([A-Z0-9\-]+) -->\s*$")
CORE_END = re.compile(r"^\s*<!-- noyau:fin ([A-Z0-9\-]+) -->\s*$")


def core_blocks(lines: list[str]) -> dict[int, str]:
    """Index source → nom du bloc compilé dans le noyau, pour les lignes entre marqueurs."""
    block_of, current = {}, None
    for i, line in enumerate(lines):
        start, end = CORE_START.match(line), CORE_END.match(line)
        if start:
            current = start.group(1)
        elif end:
            current = None
        elif current:
            block_of[i] = current
    return block_of


def core_section(first_line: str) -> str | None:
    """Section de la skill compilée (« 7. Gestes de finition ») qui contient cette ligne de bloc."""
    for skill in (ROOT / "agent" / "skill" / "SKILL.md", ROOT / "skill" / "SKILL.md"):
        if skill.is_file():
            section = None
            for line in skill.read_text(encoding="utf-8").splitlines():
                if line.startswith("### "):
                    section = line[4:].strip()
                if first_line and line.strip() == first_line.strip():
                    return section
    return None


def fold_core(lines: list[str], index: int) -> list[str]:
    """Texte servi où chaque bloc compilé dans le noyau de la skill devient une ligne de renvoi :
    l'agent a déjà ce bloc en contexte. La lecture complète reste disponible (--complet)."""
    block_of = core_blocks(lines)
    out, seen = [], set()
    for i, text in served_lines(lines, index):
        name = block_of.get(i)
        if name is None:
            out.append(text)
        elif name not in seen:
            seen.add(name)
            first = next((lines[k] for k in sorted(k for k, n in block_of.items() if n == name)
                          if lines[k].strip() and not CONCEPT_MARKER.match(lines[k])), "")
            section = core_section(first)
            where = f"section « {section} »" if section else "noyau"
            words = re.sub(r"[*`>]", "", first).strip()
            out.append(f"> [Déjà dans le noyau de la skill, {where} : « {words[:70]}… » — --complet pour l'afficher ici]")
    return out

def _fold(text: str) -> str:
    """Minuscules sans accents, pour une recherche tolérante."""
    return "".join(c for c in unicodedata.normalize("NFKD", text) if not unicodedata.combining(c)).casefold()


def find(term: str, include_guides: bool = False) -> list[tuple[str | None, str, int, str]]:
    """(locator le plus précis ou None, fichier, ligne, texte) pour chaque ligne contenant le terme."""
    query = _fold(term.strip())
    if not query:
        raise RouteError("terme de recherche vide")
    return _scan(lambda folded: query in folded, include_guides)


def _scan(match, include_guides: bool = False) -> list[tuple[str | None, str, int, str]]:
    """Lignes dont la forme repliée satisfait match, avec la route la plus précise qui les sert."""
    routes = parse_routes(carte())
    locators = set(routes)
    for path in sources_normatives():
        if not path.is_file():
            raise RouteError(f"propriétaire absent : {nom(path)}")
        for _, _, text in headings(path.read_text(encoding="utf-8").splitlines()):
            found = heading_locator(text)
            if found:
                locators.add(found)
    blocks = []
    for locator in sorted(locators):
        path, lines, index = resolve(locator, routes)
        indices = {i for i, text in served_lines(lines, index) if text == lines[i]}
        blocks.append((path, indices, locator))
    results = []
    sources = sources_normatives()
    if include_guides:
        sources += [p for p in fichiers_officiels() if p not in sources]
        sources += guide_extras()
    for path in sources:
        name = nom(path)
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines()):
            if not CONCEPT_MARKER.match(line) and match(_fold(line)):
                around = [b for b in blocks if b[0] == path and number in b[1]]
                best = min(around, key=lambda b: len(b[1]))[2] if around else None
                results.append((best, name, number + 1, line.strip()))
    return results


# Synonymes stricts et traductions : une requête sur un terme cherche aussi les autres termes du groupe.
# Chaque groupe garde au moins un terme présent dans les sources (test_read_route).
ALIAS_GROUPS = (
    ("premier écran", "premier contact", "premier regard", "hero", "above the fold", "first screen"),
    ("désactivé", "disabled", "inactif"),
    ("mode sombre", "thème sombre", "dark mode"),
    ("lecteur d'écran", "lecteur d’écran", "screen reader", "technologies d’assistance", "technologies d'assistance"),
    ("ombre", "ombres", "shadow"),
    ("espacement", "spacing"),
    ("graphique", "chart", "diagramme"),
    ("tarif", "tarifs", "prix", "pricing"),
    ("clavier", "keyboard"),
    ("taille des cibles", "cible tactile", "target size", "cible", "cibles"),
    ("tendance", "trend"),
    ("hiérarchie", "hierarchy"),
    ("témoignage", "témoignages", "testimonial", "avis client"),
    ("capture", "captures", "screenshot", "capture d'écran"),
    ("cartes", "cards"),
    ("pied de page", "footer", "colophon", "fin de page"),
    ("séquence", "enchaînement des sections"),
    ("transition", "transitions", "divider"),
    ("texte sur image", "texte sur photo", "overlay"),
    ("confidentialité", "vie privée", "privacy", "donnée personnelle", "données personnelles"),
    ("preuve sociale", "social proof", "réputation", "logos"),
    ("microcopie", "microcopy", "rédaction", "copywriting"),
    ("design system", "système de design", "token", "tokens"),
    ("multilingue", "multilingual", "localisation", "traduction", "i18n"),
    ("placeholder", "lorem", "lorem ipsum", "faux texte"),
    ("icône", "icônes", "icon", "pictogramme"),
    ("grain", "noise", "bruit"),
    ("navigation", "menu"),
    ("police", "polices", "font", "fonte", "typographie"),
    ("couleur", "couleurs", "color", "colour"),
    ("grille", "grid"),
    ("mouvement", "motion", "animation"),
    ("arrondi", "coins arrondis", "radius", "rayon"),
    ("contraste", "contrast"),
    ("mobile", "responsive", "petit écran"),
    ("état vide", "empty state", "empty"),
    ("tabulaire", "tabular", "chiffres tabulaires"),
    ("densité", "density"),
    # Ajouts du lot 2 du rangement : vocabulaire courant d'un débutant, d'un designer ou en anglais (moitié de réglage
    # du second jeu de trouvabilité ; l'autre moitié sert de témoin).
    ("accessibilité", "accessible", "accessibility", "handicap", "wcag", "a11y"),
    ("erreur", "erreurs", "error", "plante"),
    ("mise en page", "layout"),
    ("titre", "titres", "headline", "heading"),
    ("retour à la ligne", "line break", "line breaks", "césure", "orphelin"),
    ("style", "styles", "look"),
    ("tableau", "tableaux", "table", "dashboard", "tableau de bord"),
    ("token", "tokens", "variable", "variables"),
    ("test utilisateur", "usability", "utilisabilité", "test d’usage", "test d'usage"),
    ("fort enjeu", "médical", "santé", "healthcare", "high-stakes", "paiement"),
    ("péremption", "dépassé", "dépassée", "obsolète", "outdated"),
    ("fictif", "fictive", "fake", "inventé", "inventés"),
    ("largeur", "largeurs", "viewport", "widths", "breakpoint"),
    ("dérogation", "override", "known issue"),
    ("réponse", "answer", "compte rendu"),
    ("chargement", "charger", "load"),
)
STOPWORDS = {"le", "la", "les", "un", "une", "des", "de", "du", "d", "l", "et", "ou", "en", "a", "au", "aux", "sur",
             "pour", "par", "avec", "dans", "the", "of", "and", "to", "for"}
TOP_ROUTES = 8


def aliases(term: str) -> list[str]:
    """Termes à chercher : la requête puis les autres membres de ses groupes, sans doublon replié."""
    query = _fold(term.strip())
    terms = [term.strip()]
    for group in ALIAS_GROUPS:
        if query in {_fold(g) for g in group}:
            terms += [g for g in group if _fold(g) not in {_fold(x) for x in terms}]
    return terms


def _word(term: str) -> re.Pattern:
    """Mot ou expression entière, pluriel simple admis (s, x, es)."""
    return re.compile(r"(?<![a-z0-9])" + re.escape(_fold(term)) + r"(?:e?s|x)?(?![a-z0-9])")


def search(term: str, include_guides: bool = False) -> tuple[str, list[str], list[tuple[str | None, str, int, str]]]:
    """(mode, termes cherchés, lignes). Mots entiers et alias d'abord ; sinon correspondance partielle ;
    sinon tous les mots significatifs sur une même ligne."""
    terms = aliases(term)
    if not _fold(term.strip()):
        raise RouteError("terme de recherche vide")
    phrase = phrase_words(term)

    def enough(found):  # une phrase continue vers le mode suivant tant qu'aucune ligne trouvée n'est dans une route
        return found and (not phrase or any(r[0] is not None for r in found))
    patterns = [_word(t) for t in terms]
    results = _scan(lambda folded: any(p.search(folded) for p in patterns), include_guides)
    if enough(results):
        return "mots entiers", terms, results
    folded_terms = [_fold(t) for t in terms]
    results = _scan(lambda folded: any(f in folded for f in folded_terms), include_guides)
    if enough(results):
        return "correspondance partielle", terms, results
    words = [w for w in re.split(r"[^a-z0-9]+", _fold(term)) if len(w) > 1 and w not in STOPWORDS]
    if len(words) > 1:
        word_patterns = [re.compile(r"(?<![a-z0-9])" + re.escape(w)) for w in words]
        results = _scan(lambda folded: all(p.search(folded) for p in word_patterns), include_guides)
        if enough(results):
            return "mots séparés sur une même ligne", words, results
    if phrase:
        results = _scan(lambda folded: any(m(folded) for _, m in phrase), include_guides)
        if results:
            return "mots de la phrase", [w for w, _ in phrase], results
    return "aucun", terms, []


# Recherche par phrase : mots de liaison et mots de question ignorés, en français et en anglais.
PHRASE_STOPWORDS = STOPWORDS | {
    "quel", "quelle", "quels", "quelles", "que", "qui", "quoi", "comment", "pourquoi", "quand", "combien", "est", "sont",
    "mon", "ma", "mes", "ton", "ta", "tes", "son", "sa", "ses", "notre", "nos", "votre", "vos", "leur", "leurs",
    "je", "tu", "il", "elle", "on", "nous", "vous", "ils", "ce", "cet", "cette", "ces", "ca", "cela", "se", "ne", "pas",
    "plus", "tres", "trop", "bien", "sans", "sous", "entre", "faire", "fait", "mettre", "avoir", "etre", "veut", "dire",
    "a", "an", "is", "are", "how", "what", "which", "why", "when", "my", "your", "i", "you", "it", "do", "does",
    "should", "can", "with", "without", "on", "in", "from", "into", "use", "using", "make", "best", "this", "that"}


def phrase_words(term: str) -> list[tuple[str, object]]:
    """Mots significatifs d'une phrase, chacun avec son test de ligne : ses alias en mots entiers, sinon sa racine
    (pluriel retiré, fin de mot longue tronquée) en début de mot. Vide si la phrase a moins de deux mots significatifs."""
    words = [w for w in re.split(r"[^a-z0-9]+", _fold(term)) if len(w) > 2 and w not in PHRASE_STOPWORDS]
    words = list(dict.fromkeys(words))
    if len(words) < 2:
        return []
    out = []
    for w in words:
        root = w[:-1] if w.endswith(("s", "x")) and len(w) > 4 else w
        if len(root) > 6:  # racine : fin de mot retirée (choisir → chois, lisibilité → lisibili)
            root = root[:max(5, len(root) - 3)]
        patterns = [re.compile(r"(?<![a-z0-9])" + re.escape(root))] + [_word(a) for a in aliases(w)[1:]]
        out.append((w, lambda folded, ps=patterns: any(p.search(folded) for p in ps)))
    return out


def rank_phrase(results: list[tuple[str | None, str, int, str]], term: str) -> list[tuple[str, list[tuple[str | None, str, int, str]]]]:
    """Routes classées pour une phrase : somme, sur les mots de la phrase présents dans la route, de leur rareté
    (un mot présent dans peu de routes compte plus) ; au moins la moitié des mots requise."""
    phrase = phrase_words(term)
    grouped: dict[str, list] = {}
    for r in results:
        if r[0] is not None:
            grouped.setdefault(r[0], []).append(r)
    present = {loc: {w for w, m in phrase if any(m(_fold(line)) for _, _, _, line in lines)} for loc, lines in grouped.items()}
    total = max(len(grouped), 1)
    df = {w: sum(1 for found in present.values() if w in found) for w, _ in phrase}
    need = len(phrase) if len(phrase) <= 2 else (len(phrase) + 1) // 2
    kept = [(loc, lines) for loc, lines in grouped.items() if len(present[loc]) >= need]
    while not kept and need > 1:  # aucune route n'a assez de mots : les meilleures routes partielles
        need -= 1
        kept = [(loc, lines) for loc, lines in grouped.items() if len(present[loc]) >= need]
    titled = {loc: {w for w, m in phrase if any(line.lstrip().startswith("#") and m(_fold(line)) for _, _, _, line in lines)}
              for loc, lines in kept}

    def score(item):
        loc, lines = item
        weight = sum(math.log(1 + total / df[w]) * (2.5 if w in titled[loc] else 1) for w in present[loc])
        return (-round(weight, 6), -len(present[loc]), -min(len(lines), 5), loc)
    return sorted(kept, key=score)


def topics(text: str | None = None) -> dict[str, tuple[str, str, list[str]]]:
    """Carte des sujets de READING_MAP : sujet replié → (sujet, propriétaire, voir aussi)."""
    text = carte() if text is None else text
    if "## Carte des sujets" not in text:
        return {}
    section = text.split("## Carte des sujets", 1)[1].split("\n## ", 1)[0]
    found = {}
    for line in section.splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) == 3 and cells[1].startswith("`"):
            owner = cells[1].strip("`")
            also = re.findall(r"`([^`]+)`", cells[2])
            found[_fold(cells[0])] = (cells[0], owner, also)
    return found


def topic_for(term: str) -> tuple[str, str, list[str]] | None:
    """Entrée de la carte des sujets nommée par la requête ou l'un de ses alias."""
    table = topics()
    return next((table[_fold(t)] for t in aliases(term) if _fold(t) in table), None)


def rank_routes(results: list[tuple[str | None, str, int, str]], terms: list[str]) -> list[tuple[str, list[tuple[str | None, str, int, str]]]]:
    """Routes classées : terme dans le nom ou un titre de la route, puis citation dans le noyau, puis nombre de lignes."""
    skill = ROOT / "agent" / "skill" / "SKILL.md"
    if not skill.is_file():
        skill = ROOT / "skill" / "SKILL.md"
    core = _fold(skill.read_text(encoding="utf-8")) if skill.is_file() else ""
    folded_terms = [_fold(t) for t in terms]
    grouped: dict[str, list] = {}
    for r in results:
        if r[0] is not None:
            grouped.setdefault(r[0], []).append(r)

    def score(item):
        locator, lines = item
        named = any(f in _fold(locator.replace("-", " ").replace("_", " ")) for f in folded_terms)
        in_heading = any(line.lstrip().startswith("#") for _, _, _, line in lines)
        defines = any(_fold(line).lstrip("|>-*# ").lstrip("*`").startswith(f) for _, _, _, line in lines for f in folded_terms)
        return (-(10 * named + 4 * defines + 3 * in_heading + 2 * (_fold(locator) in core) + min(len(lines), 5)), locator)
    return sorted(grouped.items(), key=score)


def summary_rows() -> list[tuple[str, str, int, int, str]]:
    """(locator, fichier, taille servie, sous-sections, rôle) pour chaque route de premier niveau."""
    rows = []
    for path in [p for prefix in PREFIXES[:4] for p in lieu(f"{prefix}.md")]:
        lines = path.read_text(encoding="utf-8").splitlines()
        heads = headings(lines)
        for index, _, text in heads:
            locator = heading_locator(text)
            if not locator:
                continue
            body = extract(lines, index)
            end = block_end(lines, heads, index)
            subs = sum(1 for i, _, _ in heads if index < i < end)
            rows.append((locator, nom(path), sum(len(l) + 1 for l in body), subs, _role(body[1:])))
    return rows


def _role(body: list[str]) -> str:
    """Première phrase de prose de la route, sans balisage, tronquée."""
    for line in body:
        s = line.strip()
        if not s or s.startswith(("#", "|", "```", "<!--", "---")):
            continue
        s = re.sub(r"^[>*\-]\s*", "", s)
        s = re.sub(r"\[(REQUIS PAR LE MODULE[^\]]*|MÉTHODE|DURABLE|VEILLE[^\]]*|À ADAPTER)\]\s*", "", s)
        rest = re.sub(r"^\*\*[^*]{1,40}\*\*\s*", "", s)
        s = rest if rest else s
        s = re.sub(r"[*`]", "", s)
        s = re.split(r"(?<=[.;:])\s", s, maxsplit=1)[0]
        return s if len(s) <= 110 else s[:109].rstrip() + "…"
    return ""


def outline(locator: str) -> list[tuple[int, str, str | None, int]]:
    """(niveau relatif, titre, sous-locator lisible ou None, taille) des sous-sections d'une route."""
    path, lines, index = resolve(locator)
    heads = headings(lines)
    end = block_end(lines, heads, index)
    base = next(lvl for i, lvl, _ in heads if i == index)
    rows = []
    for i, lvl, text in heads:
        if not index < i < end:
            continue
        title = text.lstrip("#").strip()
        leaf = re.match(r"`?([A-Za-z0-9][A-Za-z0-9_\-]*(?:/[A-Za-z0-9_\-]+)?)`?", title)
        sub = None
        if leaf and re.search(r"[0-9]|^[A-Z][A-Z_\-/]+$", leaf.group(1)):
            for candidate in (f"{locator}/{leaf.group(1)}", leaf.group(1)):
                try:
                    if resolve(candidate)[2] == i:
                        sub = candidate
                        break
                except (RouteError, SystemExit, StopIteration):
                    pass
        size = sum(len(l) + 1 for l in lines[i:block_end(lines, heads, i)])
        rows.append((lvl - base, title, sub, size))
    return rows


def guide_extras() -> list[Path]:
    """Guides hors du corpus : README racine et références de la skill (dispositions GitHub et Local)."""
    extras = [ROOT / "README.md"] if (ROOT / "README.md").is_file() else []
    for pattern in ("agent/skill/references/*.md", "skill/references/*.md"):
        extras += sorted(ROOT.glob(pattern))
    return extras


def _excerpt(line: str, term: str, width: int = 120) -> str:
    offsets = [i for i, char in enumerate(line) for _ in _fold(char)]
    folded = "".join(_fold(char) for char in line)
    match = folded.find(_fold(term.strip()))
    position = offsets[match] if match >= 0 and match < len(offsets) else 0
    start = max(0, position - width // 3)
    piece = line[start:start + width]
    return ("…" if start else "") + piece + ("…" if start + width < len(line) else "")


def _excerpt_any(line: str, terms: list[str]) -> str:
    """Extrait centré sur le premier terme (requête ou alias) présent dans la ligne."""
    folded = _fold(line)
    hit = next((term for term in terms if _fold(term) in folded), terms[0])
    return _excerpt(line, hit)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Charge un locator, trouve la route d’un terme ou expose les connexions situées.")
    parser.add_argument("locator", nargs="?", help="locator, par exemple DIRECTION/START ou SAVOIR/CRAFT/CFT-01")
    parser.add_argument("--trouver", metavar="TERME", help="routes classées où le terme ou ses alias apparaissent (mots entiers, casse et accents ignorés)")
    parser.add_argument("--complet", action="store_true", help="avec un locator : affiche aussi les blocs déjà compilés dans le noyau de la skill")
    parser.add_argument("--tout", action="store_true", help="avec --trouver : toutes les routes trouvées, pas seulement les premières")
    parser.add_argument("--sommaire", nargs="?", const="", metavar="LOCATOR", help="liste des routes avec leur rôle, ou table des matières d’une route")
    parser.add_argument("--guides", action="store_true", help="ajouter les documents d’orientation (guides, README racine, références de la skill) à une recherche --trouver")
    parser.add_argument("--connexions", nargs="?", const="", metavar="Cxx", help="sommaire des connexions situées, ou entrée Cxx")
    args = parser.parse_args(argv)
    if sum((args.locator is not None, args.trouver is not None, args.connexions is not None, args.sommaire is not None)) != 1:
        parser.error("donner soit un locator, soit --trouver TERME, soit --connexions [Cxx], soit --sommaire [LOCATOR]")
    if args.complet and args.locator is None:
        parser.error("--complet exige un locator")
    if args.tout and not args.trouver:
        parser.error("--tout exige --trouver TERME")
    if args.guides and not args.trouver:
        parser.error("--guides exige --trouver TERME")
    if args.trouver is not None and not args.trouver.strip():
        parser.error("terme de recherche vide")
    if args.connexions and not re.fullmatch(r"C[0-9]{2}", args.connexions):
        parser.error("identifiant de connexion attendu : Cxx")
    bad = non_utf8(ROOT)
    if bad:
        fail(f"Markdown non UTF-8 : {', '.join(bad)}")
    if args.connexions is not None:
        try:
            revision, entries = connections()
            if args.connexions and args.connexions not in entries:
                raise RouteError(f"connexion inconnue : {args.connexions}")
            selected = entries.get(args.connexions)
            resolved = connection_sources(selected) if selected else []
        except (RouteError, OSError) as exc:
            fail(str(exc))
        print(f"CONNEXIONS — orientation dérivée ; SOURCE-VERSION: {revision}")
        print("Pertinence à examiner selon le contexte ; START et CHARGE restent propriétaires.")
        if selected:
            print(f"{args.connexions} — {selected['title']}\n\n{selected['body']}")
            print("\nSOURCES RÉSOLUES — lire le passage propriétaire avant application")
            for locator, path, line, heading in resolved:
                print(f"{locator}: {path.relative_to(ROOT)}:{line} — {heading}")
        else:
            for key, entry in entries.items():
                print(f"{key} — {entry['title']} : {entry['Condition et décision']}")
            print("Lire une entrée : python3 scripts/read_route.py --connexions Cxx")
        print("Effet attendu avant construction ; effet observé seulement après observation réelle.")
        return 0
    if args.sommaire is not None:
        try:
            rows = outline(args.sommaire) if args.sommaire else summary_rows()
        except (RouteError, OSError) as exc:
            fail(str(exc))
        if args.sommaire:
            print(f"SOMMAIRE — {args.sommaire} : {len(rows)} sous-section(s)")
            for level, title, sub, size in rows:
                print(f"{'  ' * max(level - 1, 0)}- {title}  ({size // 100 / 10:.1f} k)" + (f"  → {sub}" if sub else ""))
            print("Lire la route entière : python3 scripts/read_route.py " + args.sommaire)
        else:
            print(f"SOMMAIRE — {len(rows)} routes ; taille servie en milliers de caractères, nombre de sous-sections, rôle")
            current = None
            for locator, name, size, subs, role in rows:
                if name != current:
                    current = name
                    print(f"\n{name}")
                print(f"{locator:<34} {size // 100 / 10:>5.1f} k  {subs:>2} s.-s.  {role}"
                      + (f"  · {ADRESSE_DE[locator]}" if locator in ADRESSE_DE else ""))
            print("\nTable des matières d’une route : python3 scripts/read_route.py --sommaire LOCATOR")
        return 0
    if args.trouver:
        try:
            mode, terms, results = search(args.trouver, args.guides)
        except (RouteError, OSError) as exc:
            fail(str(exc))
        if not results:
            print(f"AUCUNE OCCURRENCE — « {args.trouver} »" + (f" (alias : {', '.join(terms[1:])})" if len(terms) > 1 else "")
                  + " dans le périmètre recherché. Essayer une reformulation ; ce résultat ne prouve pas l’absence du savoir.")
            return 1
        normative = [r for r in results if r[1] in {nom(p) for p in sources_normatives()}]
        guides = [r for r in results if r not in normative]
        ranked = rank_phrase(normative, args.trouver) if mode == "mots de la phrase" else rank_routes(normative, terms)
        core_index = {nom(p): core_blocks(p.read_text(encoding="utf-8").splitlines()) for p in sources_normatives()}
        outside = [r for r in normative if r[0] is None]
        shown = ranked if args.tout else ranked[:TOP_ROUTES]
        extra = (f" ; mots : {', '.join(terms)}" if mode == "mots de la phrase" else
                 f" ; alias : {', '.join(terms[1:])}" if len(terms) > 1 and mode != "mots séparés sur une même ligne" else "")
        print(f"TROUVER ({mode}{extra}) : « {args.trouver} » — {len(normative)} ligne(s) normative(s), "
              f"{len(ranked)} route(s) ; {len(guides)} ligne(s) de guide")
        topic = topic_for(args.trouver)
        if topic:
            print(f"SUJET « {topic[0]} » (carte dérivée, READING_MAP) — propriétaire : {topic[1]}"
                  + (f" ; voir aussi : {', '.join(topic[2])}" if topic[2] else ""))
        if shown or outside:
            print("SOURCES NORMATIVES — routes classées (nom ou titre, noyau, nombre de lignes)")
            for locator, lines in shown:
                print(f"{locator:<34} {len(lines)} ligne(s)" + (f"  · {ADRESSE_DE[locator]}" if locator in ADRESSE_DE else ""))
                for _, name, number, line in lines[:2]:
                    mark = " (noyau)" if number - 1 in core_index.get(name, {}) else ""
                    print(f"    {name}:{number:<5}{mark} {_excerpt_any(line, terms)}")
            if len(ranked) > len(shown):
                print(f"… {len(ranked) - len(shown)} autre(s) route(s) : ajouter --tout")
            for _, name, number, line in outside[:3]:
                print(f"(hors route)                       {name}:{number:<5} {_excerpt_any(line, terms)}")
        if guides:
            print("GUIDES — orientation, sans autorité normative")
            for _, name, number, line in guides:
                print(f"    {name}:{number:<5} {_excerpt_any(line, terms)}")
        print("Lire une route : python3 scripts/read_route.py LOCATOR ; ses sous-sections : --sommaire LOCATOR ; (noyau) : passage déjà chargé avec la skill")
        return 0
    try:
        path, lines, index = resolve(args.locator)
    except RouteError as exc:
        fail(str(exc))
    current = adresse(args.locator)
    print(f"ROUTE: {current}" + (f" (adresse : {args.locator})" if current != args.locator else
                                 f" (adresse : {ADRESSE_DE[current]})" if current in ADRESSE_DE else ""))
    print(f"OWNER: {path.relative_to(ROOT)}")
    print(f"HEADING: {lines[index].strip()}")
    print("---")
    print("\n".join(extract(lines, index) if args.complet else fold_core(lines, index)))
    return 0


if __name__ == "__main__":
    try:
        code = main()
        sys.stdout.flush()
    except BrokenPipeError:  # sortie coupée par le lecteur (| head) : fin silencieuse
        os.dup2(os.open(os.devnull, os.O_WRONLY), sys.stdout.fileno())
        code = 0
    raise SystemExit(code)
