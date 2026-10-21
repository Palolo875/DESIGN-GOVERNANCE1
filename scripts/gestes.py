#!/usr/bin/env python3
"""Gestes liés aux sorties des recettes : le savoir de craft arrive là où l'agent regarde.

Les deux recettes (`check_render.py`, `check_caractere.py`) sont les outils qu'un run appelle le plus ; leurs
signaux restent des faits. Ce module ajoute, sous leurs résultats, la ligne du tableau des gestes de
`SAVOIR/STATE` (bloc `COMP-VOCABULAIRE`, « Vocabulaire perceptuel ») qui correspond au signal : symptôme, geste
et condition, réinspection. Le tableau est lu dans sa source à chaque appel ; rien n'est recopié ici, sauf la
correspondance entre un contrôle et les termes du tableau (`LIENS`).

Un geste est un point de départ, pas une prescription : il se choisit pour le défaut dominant, se compare
avant/après et se retire s'il ne sert pas. Au plus `PLAFOND` gestes par appel. Avec `DG_JOURNAL`, un geste déjà
servi dans le même journal n'est rappelé que par son nom.

Usage direct : python3 scripts/gestes.py            (liste les termes lus dans la source)
               python3 scripts/gestes.py "Surface"  (sert la ligne d'un terme)
"""
from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import read_route  # noqa: E402

BLOC = "COMP-VOCABULAIRE"
ROUTE = "SAVOIR/STATE"
PLAFOND = 3

# (outil, début du nom du contrôle, statuts, motif facultatif du détail, termes du tableau).
# Un terme absent du tableau est une erreur de maintenance, détectée par scripts/test_gestes.py.
LIENS: tuple[tuple[str, str, frozenset[str], str | None, tuple[str, ...]], ...] = (
    ("check_render", "Contraste du texte sur fond uni", frozenset({"RETURN"}), None, ("Texte secondaire",)),
    ("check_render", "Contraste du texte sur fond uni", frozenset({"PASS-WITH-RESERVATION"}),
     r"en image|dégradé|translucide", ("Image intégrée",)),
    ("check_render", "Chevauchement et troncature de texte", frozenset({"RETURN", "PASS-WITH-RESERVATION"}), None,
     ("Gestion du vide",)),
    ("check_render", "Contraste de l’indicateur de focus", frozenset({"PASS-WITH-RESERVATION"}), None, ("États",)),
    ("check_render", "Parcours clavier", frozenset({"PASS-WITH-RESERVATION"}), None, ("États",)),
    ("check_render", "Mouvement réduit respecté", frozenset({"RETURN", "PASS-WITH-RESERVATION"}), None, ("Mouvement",)),
    ("check_caractere", "Densité", frozenset({"SIGNAL"}), None, ("Gestion du vide", "Masse visuelle")),
    ("check_caractere", "Matière dominante", frozenset({"SIGNAL"}), None, ("Masse visuelle", "Surface")),
    ("check_caractere", "Foyer", frozenset({"RELEVÉ"}), None, ("Silhouette", "Masse visuelle")),
    ("check_caractere", "Intensité", frozenset({"RELEVÉ"}), None, ("Accent",)),
    ("check_caractere", "Vide", frozenset({"RELEVÉ"}), None, ("Gestion du vide",)),
)

PUCE = "  • "
LIGNE_PUCE = re.compile(r"^  • ([^\[\n—]+?) \[", re.M)


class GestesError(Exception):
    pass


def _cellules(ligne: str) -> list[str]:
    return [c.strip() for c in ligne.strip().strip("|").split(" | ")]


def tableau() -> dict[str, dict[str, str]]:
    """Lignes du tableau des gestes, lues dans leur source propriétaire : {terme: {signal, geste, reinspection}}."""
    for path in read_route.sources_normatives():
        lines = path.read_text(encoding="utf-8").splitlines()
        try:
            debut = next(i for i, l in enumerate(lines) if l.strip() == f"<!-- noyau:début {BLOC} -->")
        except StopIteration:
            continue
        fin = next((i for i in range(debut, len(lines)) if lines[i].strip() == f"<!-- noyau:fin {BLOC} -->"), None)
        if fin is None:
            raise GestesError(f"bloc {BLOC} non fermé dans {path.name}")
        rows = [l for l in lines[debut:fin] if l.startswith("| ") and not l.startswith("| Terme") and not l.startswith("|---")]
        out = {}
        for row in rows:
            cells = _cellules(row)
            if len(cells) == 4:
                out[cells[0]] = {"signal": cells[1], "geste": cells[2], "reinspection": cells[3]}
        if not out:
            raise GestesError(f"tableau des gestes vide dans {path.name}")
        return out
    raise GestesError(f"bloc {BLOC} introuvable dans les sources normatives")


def termes_pour(outil: str, resultats: list[tuple[str, str, str]]) -> list[tuple[str, str]]:
    """(terme, contrôle) dans l'ordre des résultats, sans doublon. `resultats` : (statut, contrôle, détail)."""
    vus: list[tuple[str, str]] = []
    for statut, controle, detail in resultats:
        for o, debut, statuts, motif, termes in LIENS:
            if o != outil or not controle.startswith(debut) or statut not in statuts:
                continue
            if motif and not re.search(motif, detail or ""):
                continue
            for t in termes:
                if t not in {x for x, _ in vus}:
                    vus.append((t, controle))
    return vus


def deja_servis() -> set[str]:
    """Termes déjà servis dans le journal du run (DG_JOURNAL) ; ensemble vide sans journal ou s'il est illisible."""
    chemin = os.environ.get("DG_JOURNAL")
    if not chemin or not Path(chemin).is_file():
        return set()
    servis: set[str] = set()
    try:
        for ligne in Path(chemin).read_text(encoding="utf-8").splitlines():
            if ligne.strip():
                servis.update(json.loads(ligne).get("gestes", []))
    except (OSError, json.JSONDecodeError):
        return set()
    return servis


def bloc(outil: str, resultats: list[tuple[str, str, str]]) -> str:
    """Texte à imprimer sous les résultats d'une recette ; chaîne vide si aucun signal n'a de geste lié."""
    lies = termes_pour(outil, resultats)
    if not lies:
        return ""
    try:
        table = tableau()
    except (GestesError, OSError, read_route.RouteError) as exc:
        return f"\nGestes liés : non servis ({exc}). Lire {ROUTE} (« Vocabulaire perceptuel »)."
    servis = deja_servis()
    lignes = [f"\nGestes liés ({ROUTE}, « Vocabulaire perceptuel » ; un point de départ pour le défaut dominant, "
              "à comparer avant/après, à retirer s'il ne sert pas) :"]
    for terme, controle in lies[:PLAFOND]:
        row = table.get(terme)
        if row is None:
            lignes.append(f"{PUCE}{terme} [{controle}] — terme absent du tableau : lire {ROUTE}.")
        elif terme in servis:
            lignes.append(f"{PUCE}{terme} [{controle}] — déjà servi dans ce run ; relire la ligne si besoin : {ROUTE}.")
        else:
            lignes.append(f"{PUCE}{terme} [{controle}] — Signal : {row['signal']}\n"
                          f"    Geste : {row['geste']}\n    Réinspecter : {row['reinspection']}")
    if len(lies) > PLAFOND:
        lignes.append(f"    … et {len(lies) - PLAFOND} autre(s) : " + ", ".join(t for t, _ in lies[PLAFOND:]))
    return "\n".join(lignes)


def servis_dans(texte: str) -> list[str]:
    """Termes servis dans une sortie de recette, pour le journal."""
    return list(dict.fromkeys(m.strip() for m in LIGNE_PUCE.findall(texte)))


def main(argv: list[str] | None = None) -> int:
    args = sys.argv[1:] if argv is None else argv
    try:
        table = tableau()
    except (GestesError, OSError, read_route.RouteError) as exc:
        print(f"tableau des gestes illisible : {exc}", file=sys.stderr)
        return 1
    if not args:
        print(f"GESTES — {len(table)} termes lus dans {ROUTE} (bloc {BLOC}) :")
        for terme, row in table.items():
            print(f"{PUCE}{terme} — {row['signal']}")
        return 0
    terme = args[0]
    row = table.get(terme)
    if row is None:
        print(f"terme inconnu : {terme} ; termes : {', '.join(table)}", file=sys.stderr)
        return 1
    print(f"{terme}\nSignal : {row['signal']}\nGeste : {row['geste']}\nRéinspecter : {row['reinspection']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
