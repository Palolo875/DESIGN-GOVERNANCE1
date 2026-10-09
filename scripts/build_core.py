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

ROOT = Path(__file__).resolve().parents[1]
OFFICIAL = ROOT / "V1" / "official" if (ROOT / "V1" / "official").is_dir() else ROOT / "official"
SKILL_DIR = ROOT / "skills" / "design-governance-practice" if (ROOT / "skills").is_dir() else ROOT / "skill"
SKILL = SKILL_DIR / "SKILL.md"
BEGIN, END = "<!-- noyau:compilé début -->", "<!-- noyau:compilé fin -->"
BLOCK = re.compile(r"^<!-- noyau:(début|fin) ([A-Z0-9\-]+) -->$")
CONCEPT = re.compile(r"^\s*<!-- concept:[A-Z0-9\-]+ -->\s*$")
CORE_BUDGET_BYTES = 46_000

# Registre : (titre de section, [(identifiant de bloc, source historique propriétaire, colonnes gardées ou None)]).
# Une source historique se lit à son lieu actuel (table LIEUX de read_route.py) : déplacer un bloc ne change pas ce registre.
NOYAU: list[tuple[str, list[tuple[str, str, tuple[int, ...] | None]]]] = [
    ("Rôle et posture", [("ROLE", "DIRECTION.md", None), ("POSTURE", "DIRECTION.md", None)]),
    ("Classer, puis charger", [("CHARGE-REGLE", "DIRECTION.md", None), ("CHARGE-TABLE", "DIRECTION.md", None),
                               ("CHARGE-FIN", "DIRECTION.md", None)]),
    ("Prendre le brief et viser le premier objet", [("BRIEF", "DIRECTION.md", None), ("CONTENU", "DIRECTION.md", None),
                                                    ("PREMIER-OBJET", "DIRECTION.md", None)]),
    ("Moyens et vérité", [("MOY-PLAFOND", "DIRECTION.md", None), ("ANCRE", "DIRECTION.md", None), ("MOY-CARTE", "SAVOIR.md", None),
                          ("MOY-ASSETS", "SAVOIR.md", None), ("MOY-CALIBRATION", "SAVOIR.md", None),
                          ("VER-FAUX-ASSET", "SAVOIR.md", None), ("VER-SCENE", "DIRECTION.md", None),
                          ("VER-AUDIENCE", "DIRECTION.md", None)]),
    ("Structure", [("STRUCT-OU", "BIBLIOTHEQUE.md", None), ("STRUCT-EXPRESSION", "BIBLIOTHEQUE.md", None),
                   ("STRUCT-TENSION", "BIBLIOTHEQUE.md", None), ("STRUCT-ACTIVATION", "BIBLIOTHEQUE.md", None),
                   ("STRUCT-SIGNAUX", "BIBLIOTHEQUE.md", None)]),
    ("Composition", [("COMP-GRAMMAIRE", "SAVOIR.md", None), ("COMP-SINGULARITE", "SAVOIR.md", None),
                     ("COMP-FORME", "SAVOIR.md", None), ("COMP-CONTROLES", "SAVOIR.md", None),
                     ("COMP-TYPO", "SAVOIR.md", None), ("COMP-TITRE", "SAVOIR.md", None), ("COMP-TEXTE-IMAGE", "SAVOIR.md", None)]),
    ("Gestes de finition", [("COMP-VOCABULAIRE", "SAVOIR.md", None)]),
    ("Couleur et convergence", [("COMP-COULEUR", "SAVOIR.md", None), ("COMP-CONVERGENCE", "SAVOIR.md", None),
                                ("COMP-VAGUES", "SAVOIR.md", None)]),
    ("Boucle d’édition", [("BOUCLE", "DIRECTION.md", None), ("BOUCLE-DIAGNOSTIC", "DIRECTION.md", None),
                          ("BOUCLE-ATELIER", "ACTION.md", None), ("BOUCLE-REVUE", "SAVOIR.md", None),
                          ("BOUCLE-QUESTIONS", "DIRECTION.md", None), ("BOUCLE-REPASSE", "SAVOIR.md", None),
                          ("BOUCLE-AXE", "SAVOIR.md", None)]),
    ("Proposition, sortie et trace", [("CHECKPOINT", "ACTION.md", None), ("SORTIE", "ACTION.md", None),
                                      ("TRACE", "ACTION.md", None)]),
]


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
    if fname in read_route.LIEUX:
        return [ROOT / rel for rel in read_route.LIEUX[fname]]
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
    cache: dict[str, dict[str, list[str]]] = {}
    parts = ["_Section générée par `scripts/build_core.py` depuis les blocs « noyau » des sources ; ne pas modifier à la main._", ""]
    for n, (title, items) in enumerate(NOYAU, 1):
        parts.append(f"### {n}. {title}")
        parts.append("")
        for bid, fname, cols in items:
            if fname not in cache:
                cache[fname] = blocks_of_source(fname)
            if bid not in cache[fname]:
                raise CoreError(f"bloc {bid} absent de {fname}")
            body = project(cache[fname][bid], cols)
            parts.extend(body)
            parts.append("")
    return "\n".join(parts).rstrip() + "\n"


def render(skill_text: str, core: str) -> str:
    i, j = skill_text.find(BEGIN), skill_text.find(END)
    if i < 0 or j < i:
        raise CoreError("marqueurs de section compilée absents de la skill")
    return skill_text[: i + len(BEGIN)] + "\n" + core + skill_text[j:]


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
    if args.check:
        if new != text:
            print("NOYAU : la skill diffère de sa compilation (lancer scripts/build_core.py)")
            return 1
        print("NOYAU : skill conforme à sa compilation")
        print(f"CORE BUDGET PASSED — SKILL.md complet {size} / {CORE_BUDGET_BYTES} octets UTF-8")
        return 0
    SKILL.write_bytes(new.encode("utf-8"))
    print("NOYAU : section compilée écrite dans la skill")
    print(f"CORE BUDGET PASSED — SKILL.md complet {size} / {CORE_BUDGET_BYTES} octets UTF-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
