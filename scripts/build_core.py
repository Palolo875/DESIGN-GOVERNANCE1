#!/usr/bin/env python3
"""Compile le noyau de fabrication dans la skill.

Les blocs du noyau restent normatifs dans leur fichier propriétaire, encadrés par
`<!-- noyau:début ID -->` et `<!-- noyau:fin ID -->`. Ce script les assemble, dans l'ordre du registre
ci-dessous, entre `<!-- noyau:compilé début -->` et `<!-- noyau:compilé fin -->` dans SKILL.md.
La copie est générée : elle ne se modifie jamais à la main (`validate_structure.py` compare).

Usage :
  python3 scripts/build_core.py           # écrit la section compilée de la skill
  python3 scripts/build_core.py --check   # code 1 si la skill diffère ou dépasse son budget

Le plafond s'applique au fichier SKILL.md complet, en octets UTF-8. Une compilation
qui le dépasserait est refusée avant écriture ; le même contrôle est utilisé par
la validation structurelle des distributions GitHub et Local.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from read_route import source_directory

ROOT = Path(__file__).resolve().parents[1]
OFFICIAL = source_directory(ROOT)
SKILL_DIR = ROOT  # le paquet est la skill : SKILL.md à la racine, références dans references/
SKILL = SKILL_DIR / "SKILL.md"
BEGIN, END = "<!-- noyau:compilé début -->", "<!-- noyau:compilé fin -->"
BLOCK = re.compile(r"^<!-- noyau:(début|fin) ([A-Z0-9\-]+) -->$")
CONCEPT = re.compile(r"^\s*<!-- concept:[A-Z0-9\-]+ -->\s*$")
CORE_BUDGET_BYTES = 46_000

# Registre : (titre de section, [(identifiant de bloc, source historique propriétaire, colonnes gardées ou None)]).
# Une source historique se lit à son lieu actuel (table LIEUX de read_route.py) : déplacer un bloc ne change pas ce registre.
NOYAU: list[tuple[str, list[tuple[str, str, tuple[int, ...] | None]]]] = [
    # Ordre par moment du run : posture, classement, avant de construire, en construisant,
    # en regardant, en répondant, puis renvois. Les blocs restent normatifs dans leur source.
    ("Rôle et posture", [("ROLE", "DIRECTION.md", None), ("POSTURE", "DIRECTION.md", None), ("ABSOLUS", "DIRECTION.md", None)]),
    ("Classer, puis charger", [("CHARGE-REGLE", "DIRECTION.md", None), ("CHARGE-RECHERCHE", "DIRECTION.md", None),
                               ("CHARGE-TABLE", "DIRECTION.md", None), ("CHARGE-FIN", "DIRECTION.md", None),
                               ("CHARGE-LECTEUR", "DIRECTION.md", None)]),
    ("Avant de construire — contenu réel et premier objet", [("BRIEF", "DIRECTION.md", None), ("CONTENU", "DIRECTION.md", None),
                                                    ("PREMIER-OBJET", "DIRECTION.md", None), ("MOY-PLAFOND", "DIRECTION.md", None),
                                                    ("RECONCILIATION", "DIRECTION.md", None)]),
    ("Avant de construire — situer l’interface et son caractère", [("STRUCT-OU", "BIBLIOTHEQUE.md", None),
                   ("STRUCT-EXPRESSION", "BIBLIOTHEQUE.md", None), ("STRUCT-LEVIERS", "BIBLIOTHEQUE.md", None),
                   ("STRUCT-TENSION", "BIBLIOTHEQUE.md", None), ("STRUCT-ACTIVATION", "BIBLIOTHEQUE.md", None),
                   ("STRUCT-SIGNAUX", "BIBLIOTHEQUE.md", None)]),
    ("En construisant — composition et typographie", [("COMP-GRAMMAIRE", "SAVOIR.md", None), ("COMP-SINGULARITE", "SAVOIR.md", None),
                     ("COMP-FORME", "SAVOIR.md", None), ("COMP-CONTROLES", "SAVOIR.md", None),
                     ("COMP-TYPO", "SAVOIR.md", None), ("COMP-TITRE", "SAVOIR.md", None), ("COMP-TEXTE-IMAGE", "SAVOIR.md", None)]),
    ("Gestes de finition", [("COMP-VOCABULAIRE", "SAVOIR.md", None)]),
    ("En construisant — couleur et convergence", [("COMP-COULEUR", "SAVOIR.md", None), ("COMP-CONVERGENCE", "SAVOIR.md", None),
                                ("COMP-VAGUES", "SAVOIR.md", None)]),
    ("En construisant — moyens et vérité", [("ANCRE", "DIRECTION.md", None), ("MOY-CARTE", "SAVOIR.md", None),
                          ("MOY-ASSETS", "SAVOIR.md", None), ("MOY-CALIBRATION", "SAVOIR.md", None),
                          ("VER-FAUX-ASSET", "SAVOIR.md", None), ("VER-SCENE", "DIRECTION.md", None),
                          ("VER-AUDIENCE", "DIRECTION.md", None)]),
    ("En regardant — boucle d’édition", [("BOUCLE", "DIRECTION.md", None), ("BOUCLE-DIAGNOSTIC", "DIRECTION.md", None),
                          ("BOUCLE-ATELIER", "ACTION.md", None), ("BOUCLE-REVUE", "SAVOIR.md", None),
                          ("BOUCLE-QUESTIONS", "DIRECTION.md", None), ("BOUCLE-REPASSE", "SAVOIR.md", None),
                          ("BOUCLE-AXE", "SAVOIR.md", None)]),
    ("En répondant — proposition, sortie et trace", [("CHECKPOINT", "ACTION.md", None), ("SORTIE", "ACTION.md", None),
                                      ("TRACE", "ACTION.md", None)]),
    ("Lire les détails selon le signal", [("CHARGE-DETAILS", "DIRECTION.md", None)]),
]

# Le registre conserve tous les blocs protégés ; seule cette partie est chargée
# systématiquement. Les autres restent entiers dans leur route propriétaire.
COMMUN = frozenset({
    "ROLE", "POSTURE", "ABSOLUS", "CHARGE-REGLE", "CHARGE-FIN", "CHARGE-DETAILS",
    "CONTENU", "ANCRE", "MOY-CARTE", "VER-FAUX-ASSET", "VER-SCENE", "VER-AUDIENCE",
    "STRUCT-OU", "COMP-TYPO", "COMP-COULEUR", "COMP-VAGUES", "BOUCLE",
    "BOUCLE-DIAGNOSTIC", "CHECKPOINT", "SORTIE", "TRACE",
    # Savoir de fabrication chargé à chaque run : premier objet, composition, typographie,
    # convergence et revue créative. Une section à l'essai reste servie par sa route.
    "PREMIER-OBJET", "MOY-PLAFOND", "RECONCILIATION", "STRUCT-EXPRESSION", "STRUCT-TENSION",
    "COMP-GRAMMAIRE", "COMP-SINGULARITE", "COMP-FORME", "COMP-CONTROLES",
    "COMP-TITRE", "COMP-TEXTE-IMAGE", "COMP-CONVERGENCE", "BOUCLE-REVUE", "BOUCLE-AXE",
})
DETAILS = {
    "STRUCT-LEVIERS": "BIBLIOTHEQUE/READ",
    "CHARGE-TABLE": "DIRECTION/CHARGE",
    "CHARGE-RECHERCHE": "DIRECTION/CHARGE",
    "CHARGE-LECTEUR": "DIRECTION/CHARGE",
    "BRIEF": "DIRECTION/EXTERNAL-START",
    "MOY-ASSETS": "SAVOIR/SOURCE",
    "MOY-CALIBRATION": "SAVOIR/SOURCE",
    "STRUCT-ACTIVATION": "BIBLIOTHEQUE/SELECT",
    "STRUCT-SIGNAUX": "BIBLIOTHEQUE/SELECT",
    "COMP-VOCABULAIRE": "SAVOIR/STATE",
    "BOUCLE-ATELIER": "ACTION/ATELIER-EDITION",
    "BOUCLE-QUESTIONS": "DIRECTION/DOUBLE-LOOP",
    "BOUCLE-REPASSE": "SAVOIR/INTEGRITY/REPASSE",
}


class CoreError(Exception):
    pass


def check_budget(raw: bytes) -> int:
    """Contrôle le fichier complet, y compris métadonnées et contenu hors noyau."""
    size = len(raw)
    if size > CORE_BUDGET_BYTES:
        raise CoreError(f"CORE BUDGET FAILED — SKILL.md complet {size} octets UTF-8 > "
                        f"budget {CORE_BUDGET_BYTES} : retirer une redondance ou déplacer "
                        "un détail vers une route en conservant son activation")
    return size


def blocks_of(path: Path) -> dict[str, list[str]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    found: dict[str, list[str]] = {}
    current, buf = None, []
    for line in lines:
        m = BLOCK.match(line.strip())
        if m and m.group(1) == "début":
            if current:
                raise CoreError(f"{path.name} : bloc {m.group(2)} ouvert dans {current}")
            current, buf = m.group(2), []
        elif m and m.group(1) == "fin":
            if m.group(2) != current:
                raise CoreError(f"{path.name} : fin {m.group(2)} sans début correspondant")
            if current in found:
                raise CoreError(f"{path.name} : bloc {current} défini deux fois")
            found[current] = buf
            current = None
        elif current:
            if not CONCEPT.match(line):
                buf.append(line)
    if current:
        raise CoreError(f"{path.name} : bloc {current} non fermé")
    return found


def project(lines: list[str], cols: tuple[int, ...] | None) -> list[str]:
    if cols is None:
        return lines
    out = []
    for line in lines:
        if line.lstrip().startswith("|"):
            cells = line.strip().strip("|").split("|")
            out.append("| " + " | ".join(cells[i].strip() for i in cols) + " |")
        else:
            out.append(line)
    return out


def lieu(fname: str) -> list[Path]:
    """Fichiers de la source historique `fname` (table LIEUX du lecteur ; sinon le fichier de OFFICIAL)."""
    sys.path.insert(0, str(ROOT / "scripts"))
    import read_route  # import tardif : read_route n'importe pas ce module
    if fname in read_route.LIEUX:  # « sections/ » désigne le dossier des sources de cette disposition
        return [OFFICIAL / rel[len("sections/"):] if rel.startswith("sections/") else ROOT / rel
                for rel in read_route.LIEUX[fname]]
    return [OFFICIAL / fname]


def blocks_of_source(fname: str) -> dict[str, list[str]]:
    """Blocs de tous les fichiers de la source ; un bloc défini dans deux fichiers est une erreur."""
    found: dict[str, list[str]] = {}
    for path in lieu(fname):
        if not path.is_file():
            continue
        for bid, body in blocks_of(path).items():
            if bid in found:
                raise CoreError(f"{fname} : bloc {bid} défini dans deux fichiers")
            found[bid] = body
    return found


def compile_core() -> str:
    import read_route

    cache: dict[str, dict[str, list[str]]] = {}
    parts = ["_Section générée par `scripts/build_core.py` depuis les blocs « noyau » des sources ; ne pas modifier à la main._", ""]
    registered = [bid for _, items in NOYAU for bid, _, _ in items]
    if len(registered) != len(set(registered)) or set(registered) != COMMUN | DETAILS.keys() or COMMUN & DETAILS.keys():
        raise CoreError("registre du noyau : chaque bloc doit être commun ou servi par une route unique")
    n = 0
    for title, items in NOYAU:
        loaded = []
        for bid, fname, cols in items:
            if fname not in cache:
                cache[fname] = blocks_of_source(fname)
            if bid not in cache[fname]:
                raise CoreError(f"bloc {bid} absent de {fname}")
            body = project(cache[fname][bid], cols)
            if bid in COMMUN:
                loaded.extend(body)
                loaded.append("")
            else:
                locator = DETAILS[bid]
                try:
                    _, lines, index = read_route.resolve(locator)
                    served = "\n".join(read_route.extract(lines, index))
                except (read_route.RouteError, OSError) as exc:
                    raise CoreError(f"activation de {bid} : {locator} indisponible ({exc})") from exc
                if "\n".join(body).strip() not in served:
                    raise CoreError(f"activation de {bid} : {locator} ne sert pas le bloc complet")
        if not loaded:
            continue
        n += 1
        parts.append(f"### {n}. {title}")
        parts.append("")
        parts.extend(loaded)
    available = {bid for blocks in cache.values() for bid in blocks}
    if available != set(registered):
        raise CoreError("registre du noyau : bloc source non classé : " + ", ".join(sorted(available - set(registered))))
    core = "\n".join(parts).rstrip() + "\n"
    _, lines, index = read_route.resolve("DIRECTION/CHARGE")
    activation = core + "\n" + "\n".join(read_route.extract(lines, index))
    for bid, locator in DETAILS.items():
        if bid == "CHARGE-TABLE" and "python3 scripts/read_route.py --mode MODE" in core:
            continue  # --mode résout la table propriétaire, sans en recopier le locator.
        if f"`{locator}`" not in activation:
            raise CoreError(f"activation de {bid} : renvoi {locator} absent du noyau et de CHARGE")
    return core


def render(skill_text: str, core: str) -> str:
    i, j = skill_text.find(BEGIN), skill_text.find(END)
    if i < 0 or j < i:
        raise CoreError("marqueurs de section compilée absents de la skill")
    return skill_text[: i + len(BEGIN)] + "\n" + core + skill_text[j:]


LIEUX_BEGIN, LIEUX_END = "<!-- lieux:début -->", "<!-- lieux:fin -->"
ROUTE_HEADING = re.compile(r"^#{1,4}\s+`?([A-Z]+(?:/[A-Za-z0-9_\-]+)+)`?")


def bandeau(name: str) -> str | None:
    """Bandeau généré depuis LIEUX : ce que le fichier sections/ ne contient pas, et où le trouver."""
    import read_route
    resp = name.removesuffix(".md")
    out = [LIEUX_BEGIN,
           f"> **Ce fichier ne contient pas toute la responsabilité `{resp}`.** Il contient les sections rangées dans ce fichier ; "
           f"les autres sections `{resp}` vivent à leur emplacement, avec la même autorité, et ne sont pas recopiées ici. "
           "Une route se lit avec `python3 scripts/read_route.py LOCATOR`, qui trouve son fichier. "
           "_Bandeau généré par `scripts/build_core.py` depuis le registre `LIEUX` ; ne pas modifier à la main._",
           ">"]
    for rel in read_route.LIEUX[name][1:]:
        path = read_route.chemin_lieu(rel)
        routes = []
        for line in path.read_text(encoding="utf-8").splitlines():
            m = ROUTE_HEADING.match(line)
            if m and m.group(1).startswith(resp + "/") and m.group(1) not in routes:
                routes.append(m.group(1))
        if routes:
            out.append(f"> - [`{rel}`](../{rel}) : " + ", ".join(f"`{r}`" for r in routes))
    if len(out) == 3:
        return None  # aucune route de cette responsabilité ailleurs : pas de bandeau
    out.append(LIEUX_END)
    return "\n".join(out)


def bandeaux() -> dict[Path, tuple[str, str]]:
    """(texte actuel, texte attendu) de chaque fichier sections/ qui partage sa responsabilité avec d'autres fichiers."""
    import read_route
    result = {}
    for name, rels in read_route.LIEUX.items():
        if not rels or not rels[0].startswith("sections/") or len(rels) < 2:
            continue
        path = read_route.chemin_lieu(rels[0])
        text = path.read_text(encoding="utf-8")
        block = bandeau(name)
        i, j = text.find(LIEUX_BEGIN), text.find(LIEUX_END)
        if block is None:
            if i >= 0 and j > i:
                result[path] = (text, text[:i] + text[j + len(LIEUX_END):].lstrip("\n"))
            continue
        if i >= 0 and j > i:
            new = text[:i] + block + text[j + len(LIEUX_END):]
        else:
            k = text.find("\n## ")
            if k < 0:
                raise CoreError(f"{rels[0]} : aucun titre de section pour placer le bandeau LIEUX")
            new = text[:k + 1] + block + "\n\n" + text[k + 1:]
        result[path] = (text, new)
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description="Compiler le noyau et contrôler le budget du fichier SKILL.md complet.")
    parser.add_argument("--check", action="store_true", help="vérifier sans écrire : compilation et budget")
    args = parser.parse_args()
    import read_route  # encodage nommé avant toute lecture

    bad = read_route.non_utf8(read_route.ROOT)
    if bad:
        print(f"NOYAU : erreur — Markdown non UTF-8 : {', '.join(bad)}")
        return 1
    try:
        raw = SKILL.read_bytes()
        text = raw.decode("utf-8")
        new = render(text, compile_core())
        size = check_budget(raw if args.check else new.encode("utf-8"))
    except (CoreError, OSError, UnicodeError) as exc:
        print(f"NOYAU : erreur — {exc}")
        return 1
    try:
        lieux = bandeaux()
    except (CoreError, OSError) as exc:
        print(f"LIEUX : erreur — {exc}")
        return 1
    stale = [path for path, (cur, exp) in lieux.items() if cur != exp]
    if args.check:
        if stale:
            print("LIEUX : bandeau sections/ différent du registre (lancer scripts/build_core.py) : "
                  + ", ".join(p.name for p in stale))
            return 1
        print(f"LIEUX : {len(lieux)} bandeau(x) sections/ conformes au registre")
        if new != text:
            print("NOYAU : la skill diffère de sa compilation (lancer scripts/build_core.py)")
            return 1
        print("NOYAU : skill conforme à sa compilation")
        print(f"CORE BUDGET PASSED — SKILL.md complet {size} / {CORE_BUDGET_BYTES} octets UTF-8")
        return 0
    for path in stale:
        path.write_text(lieux[path][1], encoding="utf-8")
    if stale:
        print(f"LIEUX : {len(stale)} bandeau(x) sections/ écrit(s) depuis le registre")
    SKILL.write_bytes(new.encode("utf-8"))
    print("NOYAU : section compilée écrite dans la skill")
    print(f"CORE BUDGET PASSED — SKILL.md complet {size} / {CORE_BUDGET_BYTES} octets UTF-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
