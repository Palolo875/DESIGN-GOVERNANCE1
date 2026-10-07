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

Recherche de routes par terme : `--trouver TERME` recherche les lignes contenant littéralement le terme
dans les cinq sources normatives et indique la route la plus précise qui sert le passage.
La casse et les accents sont ignorés, pas les synonymes. `--guides` ajoute les documents d'orientation,
identifiés séparément. Les marqueurs internes sont exclus. Aucun résultat ne prouve l'absence du savoir.

`--connexions [Cxx]` expose un sommaire ou une connexion située de READING_MAP,
avec ses sources résolues et la révision propriétaire. Aucun classement,
diagnostic, choix de pertinence ou génération de snapshot n'est automatisé.
"""
from __future__ import annotations

import argparse
import re
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
    for path in sources:
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines()):
            if not CONCEPT_MARKER.match(line) and query in _fold(line):
                around = [b for b in blocks if b[0] == path and number in b[1]]
                best = min(around, key=lambda b: len(b[1]))[2] if around else None
                results.append((best, path.name, number + 1, line.strip()))
    return results


def _excerpt(line: str, term: str, width: int = 120) -> str:
    offsets = [i for i, char in enumerate(line) for _ in _fold(char)]
    folded = "".join(_fold(char) for char in line)
    match = folded.find(_fold(term.strip()))
    position = offsets[match] if match >= 0 and match < len(offsets) else 0
    start = max(0, position - width // 3)
    piece = line[start:start + width]
    return ("…" if start else "") + piece + ("…" if start + width < len(line) else "")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Charge un locator, trouve la route d’un terme ou expose les connexions situées.")
    parser.add_argument("locator", nargs="?", help="locator, par exemple DIRECTION/START ou SAVOIR/CRAFT/CFT-01")
    parser.add_argument("--trouver", metavar="TERME", help="liste les routes où le terme apparaît (casse et accents ignorés)")
    parser.add_argument("--guides", action="store_true", help="ajouter les documents d’orientation à une recherche --trouver")
    parser.add_argument("--connexions", nargs="?", const="", metavar="Cxx", help="sommaire des connexions situées, ou entrée Cxx")
    args = parser.parse_args(argv)
    if sum((args.locator is not None, args.trouver is not None, args.connexions is not None)) != 1:
        parser.error("donner soit un locator, soit --trouver TERME, soit --connexions [Cxx]")
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
    if args.trouver:
        try:
            results = find(args.trouver, args.guides)
        except (RouteError, OSError) as exc:
            fail(str(exc))
        if not results:
            print(f"AUCUNE OCCURRENCE LITTÉRALE — « {args.trouver} » dans le périmètre recherché. "
                  "Essayer une reformulation ; ce résultat ne prouve pas l’absence du savoir.")
            return 1
        normative = [r for r in results if r[1] in {f"{p}.md" for p in PREFIXES}]
        guides = [r for r in results if r not in normative]
        routes_hit = {r[0] for r in normative if r[0] is not None}
        print(f"TROUVER (littéral) : « {args.trouver} » — {len(normative)} ligne(s) normative(s), "
              f"{len(routes_hit)} route(s) ; {len(guides)} ligne(s) de guide")
        for label, items in (("SOURCES NORMATIVES", normative), ("GUIDES — orientation, sans autorité normative", guides)):
            if items:
                print(label)
                for locator, name, number, line in items:
                    print(f"{(locator or '(hors route)'):<34} {name}:{number:<5} {_excerpt(line, args.trouver)}")
        print("Lire une route : python3 scripts/read_route.py LOCATOR")
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
    raise SystemExit(main())
