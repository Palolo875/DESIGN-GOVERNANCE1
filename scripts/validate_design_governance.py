"""Validation légère et reproductible de Design Governance V1.

Le même script fonctionne depuis la distribution GitHub ou depuis l’export Local.
"""

from __future__ import annotations

import os
import re
import shlex
import sys
import html
import unicodedata
from pathlib import Path
from urllib.parse import unquote

from read_route import headings, lieu, non_code_lines as indexed_non_code_lines
import read_route as routes

ROOT = Path(__file__).resolve().parents[1]
IS_LOCAL = not (ROOT / "scripts" / "build_distributions.sh").is_file()  # export Local : même arborescence, sans les outils de préparation

MANIFEST = ROOT / "scripts" / "package_manifest.json"
try:
    import json
    def _unique_keys(pairs: list) -> dict:  # une clé répétée est refusée, pas écrasée
        keys = [key for key, _ in pairs]
        repeated = sorted({key for key in keys if keys.count(key) > 1})
        if repeated:
            raise ValueError(f"clé répétée : {', '.join(repeated)}")
        return dict(pairs)

    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"), object_pairs_hook=_unique_keys)
    if not isinstance(manifest, dict):
        raise ValueError("le manifest racine doit être un objet")
    EXPECTED = manifest["local" if IS_LOCAL else "github"]
    if not isinstance(EXPECTED, list) or not all(isinstance(item, str) for item in EXPECTED):
        raise ValueError("la liste de chemins du manifest est invalide")
    OFFICIAL = routes.OFFICIAL
    LISTS = {name: manifest.get(name) for name in ("github", "local")}
    VERSION = manifest.get("version")
except (OSError, ValueError, KeyError, TypeError) as exc:
    print(f"PACKAGE VALIDATION FAILED — manifest illisible : {exc}")
    sys.exit(1)

STATE_VALUES = {"INTAKE", "CLASSIFIED", "SPECCED", "BUILDING", "CHECKING", "DECIDED", "CLOSED"}
ISSUE_VALUES = {"BLOCKED", "RETURNED", "RECLASSIFIED", "EXPLORATORY", "FAIL-ASSUMED", "ESCALATED", "null"}
VERDICT_VALUES = {
    "PASS",
    "PASS-WITH-RESERVATION",
    "RETURN",
    "N/A-JUSTIFIED",
    "NOT-VERIFIED",
    "ACCEPTED",
    "ACCEPTED-WITH-RESERVATION",
    "RETURN-DIRECTION",
    "EXPLORATORY",
    "SYSTEM-ESCALATION",
    "null",
}
DIRECTION_VALUES = {"HELD", "HELD-WITH-ACCEPTED-DIFFERENCE", "PARTIALLY-HELD", "LOST-IN-BUILD"}


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def read(path: Path, errors: list[str]) -> str:
    """Une source requise absente est citée ; les autres contrôles continuent."""
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        fail(errors, f"source requise absente ou illisible : {path.relative_to(ROOT).as_posix()} ({type(exc).__name__})")
        return ""


def read_source(name: str, errors: list[str]) -> str:
    """Source historique lue à son lieu actuel (table LIEUX du lecteur) ; absente : citée, contrôles poursuivis."""
    paths = [p for p in lieu(name) if p.is_file()]
    if not paths:
        fail(errors, f"source requise absente ou illisible : {name} (FileNotFoundError)")
        return ""
    return "\n".join(read(p, errors) for p in paths)


def check_manifest(errors: list[str]) -> None:
    """Doublons du manifeste et source unique de version (CHANGELOG)."""
    for name, items in LISTS.items():
        if isinstance(items, list):
            seen: set[str] = set()
            for item in items:
                if item in seen:
                    fail(errors, f"manifeste {name} : entrée en doublon : {item}")
                seen.add(item)
    changelog = read_source("CHANGELOG.md", errors)
    match = re.search(r"\*\*Version expérimentale :\*\* `V(\d+\.\d+\.\d+)`", changelog)
    if not isinstance(VERSION, str) or not VERSION:
        fail(errors, "version absente du manifeste (source : CHANGELOG)")
        return
    if not match:
        fail(errors, "version expérimentale introuvable dans le CHANGELOG (attendu : « **Version expérimentale :** `Vx.y.z` »)")
        return
    if VERSION != match.group(1):
        fail(errors, f"version du manifeste divergente : {VERSION} (CHANGELOG : {match.group(1)})")
    titles = [("README.md", ROOT / "README.md"), ("README.md (sources)", None), ("QUICKSTART.md", None),
              ("RELEASE_NOTES.md", ROOT / "RELEASE_NOTES.md")]
    for label, path in titles:
        if path == ROOT / "RELEASE_NOTES.md" and not path.is_file():
            continue  # RELEASE_NOTES n’existe pas dans l’export Local
        text = read(path, errors) if path else read_source(label.split(" ")[0], errors)
        first = text.splitlines()[:1]
        if first and f"V{match.group(1)}" not in first[0]:
            fail(errors, f"version du titre divergente : {label} (attendu V{match.group(1)})")


# Dossier d'installation d'un agent (copie de la skill, réglages) : il peut vivre dans le dossier du package
# sans en faire partie, comme le README le propose ; ni inventaire, ni liens, ni valeurs n'y sont contrôlés.
INSTALL_ROOT = {".claude"}


def in_package(path: Path) -> bool:
    parts = path.relative_to(ROOT).parts
    return not parts or parts[0] not in INSTALL_ROOT | {"dist", ".build", ".dist.previous", ".git"}


def check_expected_files(errors: list[str]) -> None:
    expected = set(EXPECTED)
    for relative in EXPECTED:
        if not (ROOT / relative).is_file():
            fail(errors, f"fichier attendu absent : {relative}")
    # C8 O-4 : sorties de build, journaux et métadonnées du checkout ne sont exclus qu’à la racine ;
    # `__pycache__` l’est partout, puisque le build le purge avant l’archivage.
    generated_root = {"dist", ".build", ".dist.previous", ".git", ".logs", ".distribution.lock", *INSTALL_ROOT}
    allowed_root_artifacts = {
        "Design_Governance_V1_GITHUB.zip",
        "Design_Governance_V1_LOCAL.zip",
        ".git",  # métadonnées d’un worktree ; jamais copiées dans une archive
    }
    actual = set()
    for directory, dirnames, filenames in os.walk(ROOT, followlinks=False):
        base = Path(directory)
        relative_dir = base.relative_to(ROOT)
        kept = []
        for name in dirnames:
            candidate = base / name
            parts = (relative_dir / name).parts
            if name == "__pycache__" or (len(parts) == 1 and name in generated_root):
                continue
            if candidate.is_symlink():  # C8 O-3 : politique de liens = refus
                fail(errors, f"lien symbolique dans le package : {(relative_dir / name).as_posix()}")
                continue
            kept.append(name)
        dirnames[:] = kept
        for name in filenames:
            candidate = base / name
            relative = (relative_dir / name).as_posix()
            if candidate.is_symlink():
                fail(errors, f"lien symbolique dans le package : {relative}")
                continue
            if relative not in allowed_root_artifacts:
                actual.add(relative)
    extras = sorted(actual - expected)
    for relative in extras:
        fail(errors, f"fichier inattendu dans le package : {relative}")


def non_code_lines(text: str) -> list[str]:
    """Lignes hors clôtures de code Markdown ; un exemple n'est pas une destination."""
    return [line for _, line in indexed_non_code_lines(text.splitlines())]


def markdown_anchors(text: str) -> set[str]:
    """Ancres des titres ATX et ancres HTML explicites du sous-ensemble livré.

    Règles de base GitHub : texte visible, minuscules, espaces, ponctuation et
    suffixes de titres répétés. Ce n'est pas un parseur Markdown complet.
    """
    lines = non_code_lines(text)
    anchors: set[str] = set()
    for _, _, title in headings(lines):
        title = re.sub(r"^#{1,6}\s+", "", title)
        title = re.sub(r"\s+#+\s*$", "", title)
        title = re.sub(r"!?\[([^\]]+)\]\([^)]*\)", r"\1", title)
        title = html.unescape(re.sub(r"<[^>]+>", "", title))
        title = re.sub(r"`+([^`]+)`+", r"\1", title)
        for _ in range(3):
            title = re.sub(r"(\*\*|__|\*|_|~~)(.+?)\1", r"\2", title)
        base = "".join(char for char in title.strip().lower().replace(" ", "-")
                       if char.isalnum() or char in "-_" or unicodedata.category(char).startswith("M"))
        anchor, suffix = base, 0
        while anchor in anchors:
            suffix += 1
            anchor = f"{base}-{suffix}"
        anchors.add(anchor)
    for match in re.finditer(r"<a\b[^>]*\b(?:name|id)\s*=\s*([\"'])(.*?)\1[^>]*>", "\n".join(lines), re.I):
        anchors.add(match[2])
    return anchors


def check_links(errors: list[str]) -> None:
    link_pattern = re.compile(r"\]\(([^)]+)\)")
    for path in filter(in_package, ROOT.rglob("*.md")):
        if "/dist/" in str(path):
            continue
        text = path.read_text(encoding="utf-8")
        for raw_target in link_pattern.findall("\n".join(non_code_lines(text))):
            target = unquote(raw_target.split("#", 1)[0])
            if target.startswith(("http://", "https://", "mailto:")):
                continue
            resolved = (path.parent / target).resolve() if target else path.resolve()
            if ROOT not in resolved.parents and resolved != ROOT:
                fail(errors, f"lien relatif hors package : {path.relative_to(ROOT)} -> {target}")
            elif not resolved.is_file():
                fail(errors, f"lien relatif cassé : {path.relative_to(ROOT)} -> {target}")
            elif "#" in raw_target and resolved.suffix.lower() == ".md":
                fragment = unquote(raw_target.split("#", 1)[1])
                linked_text = resolved.read_text(encoding="utf-8")
                if fragment and fragment not in markdown_anchors(linked_text):
                    fail(errors, f"fragment Markdown introuvable : {path.relative_to(ROOT)} -> {raw_target}")


def check_source_locations(errors: list[str]) -> None:
    """Un déplacement ne peut pas laisser une source absente ou une provenance hors registre."""
    for prefix in routes.PREFIXES:
        if f"{prefix}.md" not in routes.LIEUX:
            fail(errors, f"responsabilité sans emplacements déclarés : {prefix}")
    for name, relatives in routes.LIEUX.items():
        if not relatives or len(relatives) != len(set(relatives)):
            fail(errors, f"registre des sources vide ou répété : {name}")
        for path in lieu(name):
            if not path.resolve().is_relative_to(ROOT.resolve()) or not path.is_file():
                fail(errors, f"emplacement déclaré absent ou hors package : {name} -> {path}")
    for relative in EXPECTED:
        path = ROOT / relative
        if path.suffix != ".md" or not path.is_file():
            continue
        for _, line in indexed_non_code_lines(path.read_text(encoding="utf-8").splitlines()):
            origin = routes.ORIGINE.match(line)
            if origin and origin[1] not in set(routes.LIEUX) | {"README.md"}:
                fail(errors, f"provenance inconnue : {relative} -> {origin[1]}")
            if origin and origin[1].removesuffix(".md") in routes.PREFIXES:
                if path.resolve() not in {p.resolve() for p in lieu(origin[1])}:
                    fail(errors, f"provenance sans emplacement déclaré : {relative} -> {origin[1]}")


def check_inline_references(errors: list[str]) -> None:
    """Contrôle les fichiers, scripts et routes entre accents graves, hors exemples explicites.

    Un nom simple se résout depuis le document, la racine, puis un fichier unique
    du manifeste. Un chemin d'exemple se marque `exemple: chemin/fiche.md` ou
    reste dans un bloc de code ; il n'est pas traité comme une dépendance livrée.
    Les arguments utilisateur d'une commande ne sont jamais exécutés.
    """
    by_name: dict[str, list[Path]] = {}
    for relative in EXPECTED:
        by_name.setdefault(Path(relative).name, []).append(ROOT / relative)
    resolved_routes: dict[str, str | None] = {}
    file_pattern = re.compile(r"[\w./-]+\.(?:md|markdown|py|json|sh|bash|yml|yaml|html|htm|css|js|mjs|cjs|ts|tsx|jsx|toml|txt)(?:#[\w-]+)?", re.I)
    retired_names = {"QUICKSTART": "guides/equipe.md", "GLOSSAIRE": "guides/glossaire.md",
                     "ORCHESTRATION_MAP": "V1/sections/READING_MAP.md"}

    def file_reference(doc: Path, value: str, distribution: str | None = None) -> None:
        name, _, fragment = value.partition("#")
        if distribution and distribution != ("local" if IS_LOCAL else "github"):
            declared = LISTS.get(distribution)
            if not isinstance(declared, list):
                fail(errors, f"manifeste de la portée de référence invalide : {distribution}")
                return
            if name in declared and not fragment:
                return  # référence explicitement destinée à l'autre distribution, déclarée dans son manifeste
        candidates = [doc.parent / name, ROOT / name]
        if "/" not in name:
            matches = by_name.get(name, [])
            if len(matches) == 1:
                candidates.extend(matches)
        target = next((p for p in candidates if p.is_file() and p.resolve().is_relative_to(ROOT.resolve())), None)
        if target is None:
            fail(errors, f"référence opérationnelle absente : {doc.relative_to(ROOT)} -> {value}")
        elif fragment and target.suffix == ".md" and fragment not in markdown_anchors(target.read_text(encoding="utf-8")):
            fail(errors, f"fragment opérationnel introuvable : {doc.relative_to(ROOT)} -> {value}")

    def route_reference(doc: Path, value: str) -> None:
        if value not in resolved_routes:
            try:
                routes.resolve(value)
                resolved_routes[value] = None
            except (routes.RouteError, OSError) as exc:
                resolved_routes[value] = str(exc)
        if resolved_routes[value]:
            fail(errors, f"route opérationnelle non résolue : {doc.relative_to(ROOT)} -> {value} ({resolved_routes[value]})")

    for relative in EXPECTED:
        doc = ROOT / relative
        if doc.suffix != ".md" or not doc.is_file():
            continue
        raw_lines = non_code_lines(doc.read_text(encoding="utf-8"))
        text = re.sub(r"<!--.*?-->", lambda m: "\n" * m[0].count("\n"), "\n".join(raw_lines), flags=re.S)
        values = []
        for raw, line in zip(raw_lines, text.split("\n")):
            scope = re.search(r"<!-- références:([^>]+) -->", raw)
            distribution = scope[1].strip() if scope else None
            if distribution and distribution not in {"github", "local"}:
                fail(errors, f"portée de référence inconnue : {relative} -> {distribution}")
                distribution = None
            values.extend((value, distribution) for value in re.findall(r"(?<!`)`([^`\n]+)`(?!`)", line))
        for value, distribution in values:
            if value.startswith("exemple:"):
                continue
            if value in retired_names:
                fail(errors, f"ancienne référence opérationnelle : {relative} -> {value} ; utiliser {retired_names[value]}")
            elif file_pattern.fullmatch(value) or value.partition("#")[0] in EXPECTED or value in by_name:
                file_reference(doc, value, distribution)
            elif re.match(r"(?:python(?:3(?:\.\d+)?)?|bash|sh)\s", value):
                try:
                    words = shlex.split(value)
                except ValueError:
                    fail(errors, f"commande mal formée : {relative} -> {value}")
                    continue
                # Modules et code en ligne ne désignent pas un script du paquet.
                # Les options simples sont sautées ; aucune commande n'est exécutée.
                script_index = 1
                simple_flags = ({"-u", "-B", "-E", "-I", "-s", "--"} if words[0].startswith("python")
                                else {"-n", "-e", "-x", "-v", "-eu", "-eux", "--"})
                while script_index < len(words) and words[script_index] in simple_flags:
                    flag = words[script_index]
                    script_index += 1
                    if flag == "--":
                        break
                if script_index < len(words) and not words[script_index].startswith("-"):
                    script = words[script_index]
                    file_reference(doc, script, distribution)
                    if script.removeprefix("./") == "scripts/read_route.py" and len(words) > script_index + 1:
                        arg = words[script_index + 1]
                        if not arg.startswith("-") and arg not in {"LOCATOR", "ADRESSE", "…"}:
                            route_reference(doc, arg)
            elif value == "CHANGELOG":
                route_reference(doc, value)
            elif re.fullmatch(r"(?:DIRECTION|ACTION|SAVOIR|BIBLIOTHEQUE|CHANGELOG)/[A-Z0-9_-]+(?:/[A-Z0-9_-]+)?", value):
                route_reference(doc, value)
            elif value in routes.ADRESSES or re.fullmatch(r"(?:design/)?[a-z][a-z0-9-]*/[a-z0-9-]+(?:#[a-z0-9-]+)?", value):
                if not (ROOT / value).is_dir():
                    route_reference(doc, value)


def check_action_projection_source(errors: list[str]) -> None:
    """Keep the structured RUN_CARD example canonical and machine-validatable.

    ACTION.md may explain the transport contract, but it must not carry a second
    YAML/JSON projection that can drift from gouvernance/schemas/run_card.example.json.
    """
    if not any(p.is_file() for p in lieu("ACTION.md")):
        return
    text = read_source("ACTION.md", errors)
    if "schemas/run_card.example.json" not in text:
        fail(errors, "ACTION ne référence pas l’exemple RUN_CARD canonique")
    if re.search(r"(?im)^\s*(```|~~~)(?:yaml|yml|json)\s*$", text):  # insensible à la casse
        fail(errors, "ACTION contient une projection YAML/JSON embarquée : utiliser gouvernance/schemas/run_card.example.json")


def check_structured_values(errors: list[str]) -> None:
    patterns = {
        "STATE": (re.compile(r"^\s*STATE:\s*([^\s`]+)"), STATE_VALUES),
        "ISSUE": (re.compile(r"^\s*ISSUE:\s*([^\s`]+)"), ISSUE_VALUES),
        "VERDICT": (re.compile(r"^\s*VERDICT:\s*([^\s`]+)"), VERDICT_VALUES),
        "DIRECTION-STATUS": (re.compile(r"^\s*DIRECTION-STATUS:\s*([^\s`]+)"), DIRECTION_VALUES),
    }
    for path in filter(in_package, ROOT.rglob("*.md")):
        if "/dist/" in str(path):
            continue
        lines = path.read_text(encoding="utf-8").splitlines()
        for line_number, line in enumerate(lines, 1):
            for field, (pattern, allowed) in patterns.items():
                match = pattern.match(line)
                if match and match.group(1) not in allowed:
                    fail(errors, f"{field} non canonique : {path.relative_to(ROOT)}:{line_number} = {match.group(1)}")


def check_state_direction_separation(errors: list[str]) -> None:
    for path in filter(in_package, ROOT.rglob("*.md")):
        if "/dist/" in str(path):
            continue
        text = path.read_text(encoding="utf-8")
        if re.search(r"(?im)^\s*STATE:\s*HELD\b", text) or re.search(r"(?im)^\s*state:\s*HELD\b", text):
            fail(errors, f"statut de direction utilisé comme STATE : {path.relative_to(ROOT)}")


def check_canonicity_language(errors: list[str]) -> None:
    readme = read_source("README.md", errors)
    changelog = read_source("CHANGELOG.md", errors)
    if readme and not all(term in readme for term in ("section propriétaire", "emplacement actuel", "responsabilités normatives")):
        fail(errors, "la hiérarchie des sources normatives n’est pas formulée dans le README officiel")
    if "Les cinq fichiers suivants sont les **seules sources normatives**" in readme:
        fail(errors, "l’autorité est encore limitée à cinq fichiers physiques")
    if "exactement sept fichiers canoniques" in changelog or "sept fichiers actifs" in changelog:
        fail(errors, "ancienne formulation contradictoire sur les fichiers canoniques")
    for relative in ("README.md", "design/README.md", "gouvernance/README.md"):
        path = ROOT / relative
        if path.is_file():
            text = "\n".join(non_code_lines(path.read_text(encoding="utf-8")))
            if re.search(r"(?:gouvernance|ce module|le module)[^.\n]*n[’']est jamais requis|"
                         r"\bgouvernance\s+(?:est|reste|devient)\s+(?:toujours|systématiquement)\s+obligatoire\b", text, re.I):
                fail(errors, f"gouvernance présentée sans adaptation au contexte : {relative}")


def check_lifecycle_contract(errors: list[str]) -> None:
    changelog = read_source("CHANGELOG.md", errors)
    if not changelog:
        return
    required_terms = ("SEED", "PILOT", "ADOPTED", "DEPRECATED", "ABANDONED", "routes présentes dans le seed", "Migration des anciens aliases")
    for term in required_terms:
        if term not in changelog:
            fail(errors, f"contrat de cycle de vie incomplet dans CHANGELOG : {term}")
    for alias in ("REFERENCES/QUERY", "REFERENCES/SOURCE", "REFERENCES/ASSET", "REFERENCES/MEMORY", "REFERENCES/CORPUS"):
        if alias not in changelog:
            fail(errors, f"alias de migration absent du CHANGELOG : {alias}")

    bibliography = read_source("BIBLIOTHEQUE.md", errors)
    if bibliography and "section « Migration des anciens aliases » de `maintenance/evolution.md`" not in bibliography:
        fail(errors, "BIBLIOTHEQUE ne pointe pas vers le propriétaire de sa migration")


def check_reading_contract(errors: list[str]) -> None:
    action = read_source("ACTION.md", errors)
    if not action:
        return
    for mode in ("LITE", "ITER", "STANDARD", "DIRECTION", "SYSTÈME"):
        if f"`{mode}`" not in action:
            fail(errors, f"mode absent de la carte de lecture ACTION : {mode}")
    for term in ("Carte de lecture par mode", "RUN_CARD"):
        if term not in action:
            fail(errors, f"orientation ACTION absente : {term}")
    if "FAST-PATH" not in action or "sixième voie" not in action:
        fail(errors, "orientation ACTION absente : FAST-PATH doit être qualifié comme vue et non comme voie")

    official_readme = read_source("README.md", errors)
    if official_readme and "la `RUN_CARD` rassemble" not in official_readme:
        fail(errors, "RUN_CARD insuffisamment introduite dans le README officiel")


def check_experimental_position(errors: list[str]) -> None:
    # Chaque source historique porte le marqueur une fois, quel que soit le nombre de fichiers qui la portent.
    historic = ("DIRECTION.md", "ACTION.md", "SAVOIR.md", "BIBLIOTHEQUE.md", "README.md", "QUICKSTART.md", "CHANGELOG.md")
    public_entry_docs = [ROOT / "README.md", ROOT / "RELEASE_NOTES.md"]
    marker = "expérimentation maintenue"
    # Phrase normative qui NIE la maturité : elle contient « release publique » et reste permise.
    negation = re.compile(r"[^.\n]*n’est pas présentée comme une release publique[^.\n]*\.?", re.IGNORECASE)
    # Toute autre revendication de maturité publique est interdite (« version publique », « première version
    # publique », « release publique », « distribution publique »). Le texte et le contrôle ne doivent pas diverger.
    claim = re.compile(r"\b(?:première\s+)?(?:version|release|distribution)\s+publique\b", re.IGNORECASE)
    items = [(f"{OFFICIAL.relative_to(ROOT).as_posix()}/{n}", read_source(n, errors)) for n in historic]
    items += [(p.relative_to(ROOT).as_posix(), read(p, errors)) for p in public_entry_docs if p.is_file()]
    for label, text in items:
        if text and marker not in text.lower():
            fail(errors, f"marqueur expérimental absent ou divergent : {label}")
        if text:
            leftover = negation.sub("", text)
            hit = claim.search(leftover)
            if hit:
                fail(errors, f"revendication de maturité publique interdite ({hit.group(0)!r}) : {label}")


def check_local_autonomy(errors: list[str]) -> None:
    if not IS_LOCAL:
        return
    readme = read(ROOT / "README.md", errors)
    if re.search(r"(?i)consulter.*github|d[ée]pend.*github|depuis github", readme):
        fail(errors, "le README de l’export Local renvoie encore vers GitHub comme dépendance")


def main() -> int:
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import read_route  # encodage nommé avant toute lecture

    bad = read_route.non_utf8(ROOT)
    if bad:
        print(f"VALIDATION FAILED — Markdown non UTF-8 : {', '.join(bad)}")
        return 1
    errors: list[str] = []
    check_manifest(errors)
    check_expected_files(errors)
    check_links(errors)
    check_source_locations(errors)
    check_inline_references(errors)
    check_action_projection_source(errors)
    check_structured_values(errors)
    check_state_direction_separation(errors)
    check_canonicity_language(errors)
    check_lifecycle_contract(errors)
    check_reading_contract(errors)
    check_experimental_position(errors)
    check_local_autonomy(errors)

    if errors:
        print("VALIDATION FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    kind = "Local" if IS_LOCAL else "GitHub"
    print(f"VALIDATION PASSED — {kind}, {len(EXPECTED)} fichiers attendus, liens, références opérationnelles, sources, vocabulaire et convention contrôlés")
    return 0


if __name__ == "__main__":
    sys.exit(main())
