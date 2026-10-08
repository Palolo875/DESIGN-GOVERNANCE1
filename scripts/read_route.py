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

Recherche de routes par terme : `--trouver TERME` cherche le terme en mots entiers, avec ses alias
(synonymes et traductions stricts d'ALIAS_GROUPS), puis en correspondance partielle, puis mot à mot sur
une même ligne ; les routes sont classées et les premières affichées (`--tout` pour toutes).
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
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OFFICIAL = ROOT / "V1" / "official" if (ROOT / "V1" / "official").is_dir() else ROOT / "official"
MAP = OFFICIAL / "READING_MAP.md"
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


def owner_file(locator: str) -> Path:
    prefix = locator.split("/", 1)[0]
    if prefix not in PREFIXES:
        raise RouteError(f"locator inconnu : {locator}")
    return OFFICIAL / f"{prefix}.md"


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
        if not MAP.is_file():
            raise RouteError("READING_MAP.md absent")
        text = MAP.read_text(encoding="utf-8")
    revision, entries = parse_connections(text)
    changelog = OFFICIAL / "CHANGELOG.md"
    if not changelog.is_file():
        raise RouteError("propriétaire absent : CHANGELOG.md")
    versions = re.findall(r"^\*\*Révision :\*\*\s*`([^`]+)`", changelog.read_text(encoding="utf-8"), re.M)
    if len(versions) != 1 or revision != versions[0]:
        raise RouteError("révision des connexions différente du CHANGELOG ; réexaminer les sources")
    routes = parse_routes(text)
    for entry in entries.values():
        connection_sources(entry, routes)
    return revision, entries


def resolve(locator: str, routes: dict[str, tuple[str, list[str]]] | None = None) -> tuple[Path, list[str], int]:
    """Renvoie (fichier, lignes, index du titre servi)."""
    parts = locator.split("/")
    if len(parts) == 2 and parts[0] in STRUCTURE_PARENTS:
        locator = f"BIBLIOTHEQUE/{STRUCTURE_PARENTS[parts[0]]}/{parts[1]}"
    elif len(parts) == 3 and parts[0] == "BIBLIOTHEQUE" and parts[1] in STRUCTURE_PARENTS:
        locator = f"BIBLIOTHEQUE/{STRUCTURE_PARENTS[parts[1]]}/{parts[2]}"
    if routes is None:
        if not MAP.is_file():
            raise RouteError("READING_MAP.md absent")
        routes = parse_routes(MAP.read_text(encoding="utf-8"))
    if locator in routes:  # 1. table
        owner_name, chain = routes[locator]
        root_locator = "/".join(locator.split("/")[:2])
        # C11 : mêmes contrôles que validate_reading_map, pour le lecteur autonome.
        if owner_name != f"{locator.split('/', 1)[0]}.md":
            raise RouteError(f"propriétaire incohérent : {locator} → {owner_name}")
        if not chain or heading_locator(chain[0]) != root_locator:
            raise RouteError(f"destination ne correspond pas au locator : {locator} → {chain[0] if chain else '(vide)'}")
        path = OFFICIAL / owner_name
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
        raise RouteError(f"propriétaire absent : {path.name}")
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


CONCEPT_MARKER = re.compile(r"^\s*<!-- (?:concept:[A-Z0-9\-]+|noyau:(?:début|fin) [A-Z0-9\-]+) -->\s*$")


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
    routes = parse_routes(MAP.read_text(encoding="utf-8"))
    locators = set(routes)
    for prefix in PREFIXES:
        path = OFFICIAL / f"{prefix}.md"
        if not path.is_file():
            raise RouteError(f"propriétaire absent : {path.name}")
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
    sources = [OFFICIAL / f"{prefix}.md" for prefix in PREFIXES]
    if include_guides:
        sources += sorted(p for p in OFFICIAL.glob("*.md") if p not in sources)
        sources += guide_extras()
    for path in sources:
        name = path.name if path.parent == OFFICIAL else path.relative_to(ROOT).as_posix()
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
    patterns = [_word(t) for t in terms]
    results = _scan(lambda folded: any(p.search(folded) for p in patterns), include_guides)
    if results:
        return "mots entiers", terms, results
    folded_terms = [_fold(t) for t in terms]
    results = _scan(lambda folded: any(f in folded for f in folded_terms), include_guides)
    if results:
        return "correspondance partielle", terms, results
    words = [w for w in re.split(r"[^a-z0-9]+", _fold(term)) if len(w) > 1 and w not in STOPWORDS]
    if len(words) > 1:
        word_patterns = [re.compile(r"(?<![a-z0-9])" + re.escape(w)) for w in words]
        results = _scan(lambda folded: all(p.search(folded) for p in word_patterns), include_guides)
        if results:
            return "mots séparés sur une même ligne", words, results
    return "aucun", terms, []


def topics(text: str | None = None) -> dict[str, tuple[str, str, list[str]]]:
    """Carte des sujets de READING_MAP : sujet replié → (sujet, propriétaire, voir aussi)."""
    text = MAP.read_text(encoding="utf-8") if text is None else text
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
    skill = ROOT / "skills" / "design-governance-practice" / "SKILL.md"
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
    for prefix in PREFIXES[:4]:
        path = OFFICIAL / f"{prefix}.md"
        lines = path.read_text(encoding="utf-8").splitlines()
        heads = headings(lines)
        for index, _, text in heads:
            locator = heading_locator(text)
            if not locator:
                continue
            body = extract(lines, index)
            end = block_end(lines, heads, index)
            subs = sum(1 for i, _, _ in heads if index < i < end)
            rows.append((locator, path.name, sum(len(l) + 1 for l in body), subs, _role(body[1:])))
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
    for pattern in ("skills/*/references/*.md", "skill/references/*.md"):
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
    parser.add_argument("--tout", action="store_true", help="avec --trouver : toutes les routes trouvées, pas seulement les premières")
    parser.add_argument("--sommaire", nargs="?", const="", metavar="LOCATOR", help="liste des routes avec leur rôle, ou table des matières d’une route")
    parser.add_argument("--guides", action="store_true", help="ajouter les documents d’orientation (guides, README racine, références de la skill) à une recherche --trouver")
    parser.add_argument("--connexions", nargs="?", const="", metavar="Cxx", help="sommaire des connexions situées, ou entrée Cxx")
    args = parser.parse_args(argv)
    if sum((args.locator is not None, args.trouver is not None, args.connexions is not None, args.sommaire is not None)) != 1:
        parser.error("donner soit un locator, soit --trouver TERME, soit --connexions [Cxx], soit --sommaire [LOCATOR]")
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
                print(f"{locator:<34} {size // 100 / 10:>5.1f} k  {subs:>2} s.-s.  {role}")
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
        normative = [r for r in results if r[1] in {f"{p}.md" for p in PREFIXES}]
        guides = [r for r in results if r not in normative]
        ranked = rank_routes(normative, terms)
        outside = [r for r in normative if r[0] is None]
        shown = ranked if args.tout else ranked[:TOP_ROUTES]
        extra = f" ; alias : {', '.join(terms[1:])}" if len(terms) > 1 and mode != "mots séparés sur une même ligne" else ""
        print(f"TROUVER ({mode}{extra}) : « {args.trouver} » — {len(normative)} ligne(s) normative(s), "
              f"{len(ranked)} route(s) ; {len(guides)} ligne(s) de guide")
        topic = topic_for(args.trouver)
        if topic:
            print(f"SUJET « {topic[0]} » (carte dérivée, READING_MAP) — propriétaire : {topic[1]}"
                  + (f" ; voir aussi : {', '.join(topic[2])}" if topic[2] else ""))
        if shown or outside:
            print("SOURCES NORMATIVES — routes classées (nom ou titre, noyau, nombre de lignes)")
            for locator, lines in shown:
                print(f"{locator:<34} {len(lines)} ligne(s)")
                for _, name, number, line in lines[:2]:
                    print(f"    {name}:{number:<5} {_excerpt_any(line, terms)}")
            if len(ranked) > len(shown):
                print(f"… {len(ranked) - len(shown)} autre(s) route(s) : ajouter --tout")
            for _, name, number, line in outside[:3]:
                print(f"(hors route)                       {name}:{number:<5} {_excerpt_any(line, terms)}")
        if guides:
            print("GUIDES — orientation, sans autorité normative")
            for _, name, number, line in guides:
                print(f"    {name}:{number:<5} {_excerpt_any(line, terms)}")
        print("Lire une route : python3 scripts/read_route.py LOCATOR ; ses sous-sections : --sommaire LOCATOR")
        return 0
    try:
        path, lines, index = resolve(args.locator)
    except RouteError as exc:
        fail(str(exc))
    print(f"ROUTE: {args.locator}")
    print(f"OWNER: {path.relative_to(ROOT)}")
    print(f"HEADING: {lines[index].strip()}")
    print("---")
    print("\n".join(extract(lines, index)))
    return 0


if __name__ == "__main__":
    try:
        code = main()
        sys.stdout.flush()
    except BrokenPipeError:  # sortie coupée par le lecteur (| head) : fin silencieuse
        os.dup2(os.open(os.devnull, os.O_WRONLY), sys.stdout.fileno())
        code = 0
    raise SystemExit(code)
