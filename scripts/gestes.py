#!/usr/bin/env python3
"""Gestes liés aux sorties des recettes : le savoir de craft arrive là où l'agent regarde.

Les deux recettes (`check_render.py`, `check_caractere.py`) sont les outils qu'un run appelle le plus ; leurs
signaux restent des faits. Ce module ajoute, sous leurs résultats, la ligne du tableau des gestes de
`SAVOIR/STATE` (bloc `COMP-VOCABULAIRE`, « Vocabulaire perceptuel ») qui correspond au signal : symptôme, geste
et condition, réinspection. Le tableau est lu dans sa source à chaque appel ; rien n'est recopié ici, sauf la
correspondance entre un contrôle et les termes du tableau (`LIENS`).

Un geste est un point de départ, pas une prescription : il se choisit pour le défaut dominant, se compare
avant/après et se retire s'il ne sert pas. Un geste par contrôle signalé, au plus `PLAFOND` par appel. Avec
`DG_JOURNAL`, un geste déjà servi dans le même journal n'est rappelé que par son nom.

`suite()` ajoute deux rendez-vous, même sans les gestes : quand une recette ouvre une correction, la carte
« regard » (`read_route.py --moment regard`) si le journal ne la montre pas déjà lue ; quand deux passages de la
recette de rendu ne relèvent plus rien de bloquant (référence `--baseline` sans RETURN, ou passage précédent
sur la même page dans le journal), la planche de regard humain (`DIRECTION/DOUBLE-LOOP`).

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


def termes_pour(outil: str, resultats: list[tuple[str, str, str]], servis: frozenset[str] | set[str] = frozenset()) -> list[tuple[str, str]]:
    """(terme, contrôle) dans l'ordre des résultats, un par contrôle, sans doublon ; un terme pas encore servi
    passe avant un terme déjà servi. `resultats` : (statut, contrôle, détail)."""
    vus: list[tuple[str, str]] = []
    for statut, controle, detail in resultats:
        for o, debut, statuts, motif, termes in LIENS:
            if o != outil or not controle.startswith(debut) or statut not in statuts:
                continue
            if motif and not re.search(motif, detail or ""):
                continue
            # Un geste par contrôle : le premier terme lié qui n'est pas déjà servi par un autre contrôle.
            pris = {x for x, _ in vus}
            libre = next((t for t in termes if t not in pris and t not in servis), None) \
                or next((t for t in termes if t not in pris), None)
            if libre and controle not in {c for _, c in vus}:
                vus.append((libre, controle))
    return vus


def journal() -> list[dict]:
    """Entrées du journal du run (DG_JOURNAL) ; liste vide sans journal ou s'il est illisible."""
    chemin = os.environ.get("DG_JOURNAL")
    if not chemin or not Path(chemin).is_file():
        return []
    try:
        return [json.loads(l) for l in Path(chemin).read_text(encoding="utf-8").splitlines() if l.strip()]
    except (OSError, json.JSONDecodeError):
        return []


def deja_servis() -> set[str]:
    """Termes déjà servis dans le journal du run ; ensemble vide sans journal."""
    return {g for e in journal() for g in e.get("gestes", [])}


def _option(cmd: list[str], nom: str) -> str | None:
    for i, c in enumerate(cmd):
        if c == nom and i + 1 < len(cmd):
            return cmd[i + 1]
        if c.startswith(nom + "="):
            return c[len(nom) + 1:]
    return None


def _meme_page(cmd: list[str], page: str) -> bool:
    try:
        cible = Path(page).resolve()
        return any(c.endswith(".html") and Path(c).resolve() == cible for c in cmd)
    except OSError:
        return False


def suite(outil: str, resultats: list[tuple[str, str, str]], page: str = "", precedent_sans_retour: bool = False) -> str:
    """Rendez-vous à imprimer sous une recette : carte « regard » quand une correction s'ouvre, planche quand deux
    passages de la recette de rendu ne relèvent plus rien de bloquant. Chaîne vide sinon."""
    entrees = journal()
    ouvrant = "RETURN" if outil == "check_render" else "SIGNAL"
    ouvre = any(s == ouvrant for s, _, _ in resultats)
    lignes = []
    regard_lu = any(e.get("outil") == "read_route" and _option(e.get("commande", []), "--moment") == "regard"
                    and e.get("code") == 0 for e in entrees)
    if ouvre and not regard_lu:
        lignes.append("Correction ouverte : avant de modifier, `python3 scripts/read_route.py --moment regard` sert les gestes "
                      "du regard et des cas observés, si elle n’est pas déjà lue dans ce run (`DIRECTION/CHARGE`).")
    if outil == "check_render" and not ouvre:
        modes = {_option(e.get("commande", []), o) for e in entrees for o in ("--mode", "--tronc")} - {None}
        avant = [e for e in entrees if e.get("outil") == "check_render" and page and _meme_page(e.get("commande", []), page)]
        deux = precedent_sans_retour or bool(avant and "RETURN" not in (avant[-1].get("resultats") or {}))
        planche_faite = any(e.get("outil") == "planche" for e in entrees)
        if deux and not planche_faite and (not modes or "DIRECTION" in modes):
            lignes.append("Deux passages sans défaut bloquant : la finition qui reste (alignement perçu, rythme, raccord, matière, "
                          "objet dessiné) échappe à la recette. Nommez-la dans la trace, ou préparez la planche : "
                          f"`python3 scripts/planche.py {page or 'PAGE'} --sortie planche/ --defaut \"…\"` (`DIRECTION/DOUBLE-LOOP`).")
    return ("\n" + "\n".join(lignes)) if lignes else ""


def bloc(outil: str, resultats: list[tuple[str, str, str]]) -> str:
    """Texte à imprimer sous les résultats d'une recette ; chaîne vide si aucun signal n'a de geste lié."""
    servis = deja_servis()
    lies = termes_pour(outil, resultats, servis)
    if not lies:
        return ""
    try:
        table = tableau()
    except (GestesError, OSError, read_route.RouteError) as exc:
        return f"\nGestes liés : non servis ({exc}). Lire {ROUTE} (« Vocabulaire perceptuel »)."
    lignes = [f"\nGestes liés ({ROUTE}, « Vocabulaire perceptuel » ; un point de départ pour le défaut dominant, "
              "à comparer avant/après, à retirer s'il ne sert pas) :"]
    for terme, controle in lies[:PLAFOND]:
        row = table.get(terme)
        if row is None:
            lignes.append(f"{PUCE}{terme} [{controle}] — terme absent du tableau : lire {ROUTE}.")
        elif terme in servis:
            lignes.append(f"{PUCE}{terme} [{controle}] — déjà servi dans ce run ; relire la ligne si besoin : {ROUTE}.")
        else:
            lignes.append(f"{PUCE}{terme} [{controle}] — Geste : {row['geste']}\n    Réinspecter : {row['reinspection']}")
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
