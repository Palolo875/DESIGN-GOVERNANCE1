#!/usr/bin/env python3
"""Journal de mobilisation, passif : ce que le lecteur de routes et les recettes ont servi pendant un run.

Sans la variable d'environnement DG_JOURNAL, rien n'est écrit et les outils se comportent à l'identique.
Avec DG_JOURNAL=chemin.jsonl, chaque appel de read_route.py, check_render.py ou check_caractere.py ajoute
une ligne JSON : horodatage, commande, code de sortie, routes servies ou résultats. Un journal illisible
ou impossible à écrire ne bloque jamais l'outil : un avertissement part sur la sortie d'erreur.

Le journal observe des lectures et des appels, pas l'attention de l'agent : une route lue n'est pas une
route appliquée. La fiche produite par ce script laisse la conséquence et la preuve à remplir.

Usage : python3 scripts/journal_mobilisation.py JOURNAL.jsonl   (fiche de mobilisation en Markdown)
"""
from __future__ import annotations

import io
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable

VAR = "DG_JOURNAL"
ROUTE = r"[A-Z]+(?:/[A-Za-z0-9_\-]+)+"


def actif() -> bool:
    return bool(os.environ.get(VAR))


def noter(entree: dict) -> None:
    chemin = os.environ.get(VAR)
    if not chemin:
        return
    ligne = {"horodatage": datetime.now(timezone.utc).isoformat(timespec="seconds"), **entree}
    try:
        with open(chemin, "a", encoding="utf-8") as f:
            f.write(json.dumps(ligne, ensure_ascii=False) + "\n")
    except OSError as exc:
        print(f"journal de mobilisation non écrit ({exc.strerror or exc}) : {chemin}", file=sys.stderr)


class _Copie(io.TextIOBase):
    """Laisse passer la sortie et en garde une copie pour le résumé du journal."""

    def __init__(self, cible):
        self.cible, self.texte = cible, io.StringIO()

    def write(self, s):
        self.texte.write(s)
        return self.cible.write(s)

    def flush(self):
        self.cible.flush()

    @property
    def encoding(self):
        return getattr(self.cible, "encoding", "utf-8")

    def fileno(self):
        return self.cible.fileno()


def resumer(outil: str, texte: str) -> dict:
    """Ce que la sortie d'un outil dit de la mobilisation, sans interpréter au-delà."""
    if outil == "read_route":
        lues = re.findall(rf"^ROUTE: ({ROUTE})", texte, re.M) + re.findall(rf"^======== ({ROUTE}) \(", texte, re.M)
        proposees = [r for r in re.findall(rf"^\s*({ROUTE})\s{{2,}}\d+ ligne", texte, re.M) if r not in lues]
        return {"routes_lues": list(dict.fromkeys(lues)), "routes_proposees": list(dict.fromkeys(proposees)),
                "caracteres": len(texte)}
    if outil in ("registre_choix", "specimen", "planche"):  # outils du regard : leur première ligne dit ce qui a été produit
        return {"sortie": next((l.strip() for l in texte.splitlines() if l.strip()), ""), "non_verifie": "NOT-VERIFIED" in texte}
    if outil == "check_render":
        res = re.findall(r"^\[([A-Z-]+)\s*\] ([^:\n]+?) :", texte, re.M)
    else:
        res = re.findall(r"^\[([A-ZÉ]+)\] [^·\n]+· ([^·\n]+?) ·", texte, re.M)
    statuts: dict[str, list[str]] = {}
    for statut, controle in res:
        statuts.setdefault(statut, [])
        if controle.strip() not in statuts[statut]:
            statuts[statut].append(controle.strip())
    import gestes  # gestes de SAVOIR/STATE servis sous les résultats
    return {"resultats": statuts, "non_verifie": "NOT-VERIFIED —" in texte, "gestes": gestes.servis_dans(texte)}


def executer(outil: str, principal: Callable[[], int], argv: list[str]) -> int:
    """Lance l'outil ; avec DG_JOURNAL, note la commande, le code de sortie et le résumé de la sortie."""
    if not actif():
        return principal()
    copie, origine = _Copie(sys.stdout), sys.stdout
    sys.stdout = copie
    code = 1
    try:
        code = principal()
    except SystemExit as exc:
        code = exc.code if isinstance(exc.code, int) else (0 if exc.code is None else 1)
        raise
    finally:
        sys.stdout = origine
        noter({"outil": outil, "commande": argv, "code": code, **resumer(outil, copie.texte.getvalue())})
    return code


def lire(chemin: Path) -> list[dict]:
    entrees = []
    for n, ligne in enumerate(chemin.read_text(encoding="utf-8").splitlines(), 1):
        if ligne.strip():
            try:
                entrees.append(json.loads(ligne))
            except json.JSONDecodeError:
                print(f"ligne {n} illisible, ignorée", file=sys.stderr)
    return entrees


def option(cmd: list[str], nom: str) -> str | None:
    """Valeur d'une option, écrite « --nom VALEUR » ou « --nom=VALEUR »."""
    for i, c in enumerate(cmd):
        if c == nom and i + 1 < len(cmd):
            return cmd[i + 1]
        if c.startswith(nom + "="):
            return c[len(nom) + 1:]
    return None


def niveau_outil(e: dict) -> str:
    res = e.get("resultats") or {}
    if e.get("non_verifie"):
        return "sollicité, en échec (NOT-VERIFIED)"
    if "sortie" in e:
        return f"exécuté : {e['sortie'][:160]}" if e.get("code") == 0 else f"sollicité, en échec (code {e.get('code')})"
    if not res and e.get("code") not in (0, None):
        return f"sollicité, en échec (code {e.get('code')}, aucun résultat)"
    utiles = {k: v for k, v in res.items() if k in ("RETURN", "PASS-WITH-RESERVATION", "SIGNAL", "RELEVÉ")}
    if not utiles:
        return "exécuté, rien à traiter"
    servis = f" ; gestes servis : {', '.join(e['gestes'])}" if e.get("gestes") else ""
    if "--sans-gestes" in e.get("commande", []):
        servis = " ; gestes retirés (--sans-gestes)"
    return "exécuté : " + " ; ".join(f"{k} — {', '.join(v)}" for k, v in utiles.items()) + servis


def fiche(entrees: list[dict]) -> str:
    lignes = ["# Fiche de mobilisation", "",
              "Présent dans le contexte à chaque run : le noyau de la skill. Les lectures et appels ci-dessous sont observés ; "
              "la conséquence et la preuve restent à établir sur la trace et l'artefact.", "",
              "| Ordre | Heure (UTC) | Élément | Niveau observé | Conséquence | Preuve |", "|---|---|---|---|---|---|"]
    lues: set[str] = set()
    modes: set[str] = set()
    moments: set[str] = set()
    for i, e in enumerate(entrees, 1):
        heure = e.get("horodatage", "")[11:19]
        cmd = e.get("commande", [])
        for opt in ("--mode", "--tronc"):
            valeur = option(cmd, opt)
            if valeur:
                modes.add("SYSTÈME" if valeur == "SYSTEME" else valeur)
        if e.get("outil") == "read_route" and option(cmd, "--moment") and e.get("code") == 0:
            moments.add(option(cmd, "--moment"))
        if e.get("outil") == "read_route":
            for r in e.get("routes_lues", []):
                lues.add(r)
                lignes.append(f"| {i} | {heure} | `{r}` | consultée | | |")
            if e.get("routes_proposees"):
                terme = option(cmd, "--trouver") or ""
                lignes.append(f"| {i} | {heure} | recherche « {terme} » | proposée, non lue : {', '.join(f'`{r}`' for r in e['routes_proposees'][:6])} | | |")
            if not e.get("routes_lues") and not e.get("routes_proposees"):
                if option(cmd, "--mode") and e.get("code") == 0:
                    lignes.append(f"| {i} | {heure} | ligne du mode {option(cmd, '--mode')} | consultée (routes citées, non lues) | | |")
                else:
                    lignes.append(f"| {i} | {heure} | read_route {' '.join(cmd)} | code {e.get('code')}, rien servi | | |")
        else:
            cible = next((c for c in cmd if c.endswith(".html")), None)
            objet = f"{e.get('outil')} sur `{Path(cible).name}`" if cible else f"{e.get('outil')} {' '.join(c for c in cmd if c.startswith('--'))}".strip()
            lignes.append(f"| {i} | {heure} | {objet} | {niveau_outil(e)} | | |")
    manques = []
    if modes:
        sys.path.insert(0, str(Path(__file__).resolve().parent))
        import read_route
        for mode in sorted(modes):
            try:
                tronc = read_route.tronc_routes(mode)
            except Exception:  # ligne de mode illisible : signalé, jamais deviné
                manques.append(f"- Tronc du mode {mode} illisible : non contrôlé.")
                continue
            absentes = [r for r in tronc if r not in lues]
            if absentes:
                manques.append(f"- Tronc {mode} non consulté : {', '.join(f'`{r}`' for r in absentes)}.")
        if "DIRECTION" in modes:
            sautes = [m for m in read_route.MOMENTS if m not in moments]
            if sautes:
                manques.append(f"- Cartes de moment non consultées (DIRECTION) : {', '.join(sautes)} "
                               "(`read_route.py --moment`, DIRECTION/CHARGE).")
            if not any(e.get("outil") == "check_caractere" for e in entrees):
                manques.append("- Recette de caractère non lancée (DIRECTION) : caractère déclaré non confronté au rendu "
                               "(`ACTION/RECETTE-CARACTERE`, carte « sortie »).")
    lignes += ["", "## Manques", "",
               *(manques or ["- Aucun manque détecté dans le tronc des modes observés."]),
               "- À établir sur la trace : routes pertinentes jamais ouvertes, déclencheur mal formulé, problème non reconnu, "
               "moyen absent ou en échec."]
    return "\n".join(lignes) + "\n"


def main(argv: list[str] | None = None) -> int:
    args = sys.argv[1:] if argv is None else argv
    if len(args) != 1:
        print("Usage : python3 scripts/journal_mobilisation.py JOURNAL.jsonl", file=sys.stderr)
        return 2
    chemin = Path(args[0])
    if not chemin.is_file():
        print(f"journal introuvable : {chemin}", file=sys.stderr)
        return 2
    print(fiche(lire(chemin)), end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
