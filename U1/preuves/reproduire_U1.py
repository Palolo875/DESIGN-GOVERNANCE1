#!/usr/bin/env python3
"""Rejoue les vérifications de l'unité U1 de la refonte Design Governance.

Usage : python3 reproduire_U1.py CHEMIN_DU_DEPOT [--sans-navigateur]

Chaque test imprime un identifiant (T-xx), le résultat observé et le code de sortie utile.
Aucun fichier du dépôt n'est modifié : les mutations ont lieu dans des dossiers temporaires
et dans une copie de travail git détachée, supprimée à la fin.
"""
from __future__ import annotations

import copy
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ICI = Path(__file__).resolve().parent


def run(cmd, cwd, **kw):
    return subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, **kw)


def titre(t):
    print(f"\n=== {t} ===")


def main() -> int:
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    repo = Path(sys.argv[1]).resolve()
    navigateur = "--sans-navigateur" not in sys.argv
    py = sys.executable
    tmp = Path(tempfile.mkdtemp(prefix="dg-u1-"))
    head = run(["git", "rev-parse", "--short", "HEAD"], repo).stdout.strip()
    print(f"Dépôt : {repo} @ {head}")

    # ---------- T-01 à T-05 : restauration depuis la copie Markdown ----------
    titre("T-01..T-05 restauration (script embarqué dans la copie complète)")
    copie = tmp / "copie.md"
    gen = run([py, "scripts/preparer_livraison.py", "--markdown", str(tmp / "md"), "--log", str(tmp / "prep.log")], repo)
    if gen.returncode != 0:
        print("préparation impossible :", gen.stdout[-400:], gen.stderr[-400:])
        return 1
    shutil.copy(tmp / "md" / "Design_Governance_V1_complet.md", copie)
    rest = ICI / "restaurer_embarque.py"

    def restaurer(dest):
        return run([py, "-I", str(rest), str(copie), str(dest)], tmp)

    d1 = tmp / "d1"; d1.mkdir(); (d1 / "README.md").write_text("MON README PERSONNEL")
    r = restaurer(d1)
    print(f"T-01 fichier local différent : exit={r.returncode} ; écrasé={'MON README' not in (d1 / 'README.md').read_text()}")
    d2 = tmp / "d2"; d2.mkdir(); (d2 / "notes.txt").write_text("CIBLE INTERNE"); (d2 / "README.md").symlink_to("notes.txt")
    r = restaurer(d2)
    print(f"T-02 lien vers fichier interne : exit={r.returncode} ; cible modifiée={'CIBLE INTERNE' not in (d2 / 'notes.txt').read_text()}")
    d3 = tmp / "d3"; (d3 / "autre").mkdir(parents=True); (d3 / "scripts").symlink_to("autre")
    r = restaurer(d3)
    print(f"T-03 dossier lié interne : exit={r.returncode} ; fichiers reçus par le dossier cible={len(list((d3 / 'autre').iterdir()))}")
    d4 = tmp / "d4"; d4.mkdir(); ext = tmp / "ext"; ext.mkdir(); (ext / "x").write_text("EXTERNE"); (d4 / "README.md").symlink_to(ext / "x")
    r = restaurer(d4)
    print(f"T-04 lien vers cible externe : exit={r.returncode} ; message={r.stdout.strip() or r.stderr.strip()[-80:]} ; externe intact={(ext / 'x').read_text() == 'EXTERNE'}")
    d5 = tmp / "d5"; d5.mkdir(); (d5 / "perso.txt").write_text("garde")
    r = restaurer(d5)
    print(f"T-05 dossier non vide (fichier hors inventaire) : exit={r.returncode} ; fichier conservé={(d5 / 'perso.txt').exists()}")

    # ---------- T-06 à T-14 : validateur de RUN_CARD ----------
    titre("T-06..T-14 validateur RUN_CARD (mutations de l'exemple canonique)")
    base = json.loads((repo / "schemas/run_card.example.json").read_text(encoding="utf-8"))
    loc = str((repo / "schemas/run_card.example.json").resolve())

    def carte(nom, mut, strict=False, locaux=False):
        d = copy.deepcopy(base)
        rc = d["run_card"] if "run_card" in d else d
        if locaux:
            rc["artifact"]["locator"] = loc; rc["trace_locator"] = loc; rc["proof"]["provenance"]["artifact_locator"] = loc
        mut(rc)
        p = tmp / f"{nom}.json"; p.write_text(json.dumps(d, ensure_ascii=False), encoding="utf-8")
        args = [py, "scripts/validate_run_card.py"] + (["--strict"] if strict else []) + [str(p)]
        r = run(args, repo)
        lignes = (r.stdout + r.stderr).strip().splitlines()
        motif = lignes[1] if r.returncode and len(lignes) > 1 else lignes[0] if lignes else ""
        print(f"{nom:44} exit={r.returncode} :: {motif[:150]}")

    def creux(rc):
        rc["proof"]["observed"] = ["ok"]; rc["proof"]["provenance"]["method"] = "ok"
        for k in ("artifact",):
            rc[k]["locator"] = "https://cdn.acme-preuves.io/capture-finale.png"
        rc["proof"]["provenance"]["artifact_locator"] = "https://cdn.acme-preuves.io/capture-finale.png"
        rc["trace_locator"] = "https://tickets.acme-preuves.io/RUN-42"

    carte("T-06 strict, exemple à locators locaux", lambda rc: None, strict=True, locaux=True)
    carte("T-07 strict, preuve « ok » et URL inventées", creux, strict=True, locaux=True)

    def gen(rc, cal=None, verdict=None):
        for a in rc["anchors"]:
            a["type"] = "generated"
        rc["direction"]["identity_stake"] = "high"
        if cal:
            rc["direction"]["calibration"] = cal
        if verdict:
            rc["closure"]["verdict"] = verdict

    carte("T-08 enjeu élevé, ancres générées, sans calibr.", lambda rc: gen(rc))
    carte("T-09 idem, réserve générée, verdict AWR", lambda rc: gen(rc, {"basis": "generated_only_reserved", "detail": "x"}))
    carte("T-10 idem, réserve générée, verdict ACCEPTED", lambda rc: gen(rc, {"basis": "generated_only_reserved", "detail": "x"}, "ACCEPTED"))
    carte("T-11 A2 : direction acceptée sans ancre", lambda rc: rc.__setitem__("anchors", []))
    carte("T-12 A4 : sans decision_intent", lambda rc: rc.pop("decision_intent", None))
    carte("T-13 A1 : DIRECTION close sans creative_close", lambda rc: rc.pop("creative_close", None))
    carte("T-14 A3 : sans preuve", lambda rc: rc.pop("proof", None))

    # ---------- T-15 : charge par parcours ----------
    titre("T-15 charge des parcours (octets servis par read_route + SKILL.md)")
    skill = (repo / "skills/design-governance-practice/SKILL.md").stat().st_size

    def octets(r):
        out = run([py, "scripts/read_route.py", r], repo).stdout.splitlines()[4:]
        return sum(len((l + "\n").encode()) for l in out)

    parcours = {
        "P1 LITE (contraste)": ["DIRECTION/START/TREE", "ACTION/RUN-LITE", "ACTION/FAST-PATH", "ACTION/GATE-A", "ACTION/GATE-B"],
        "P2 DIRECTION, trace légère (CHARGE)": ["DIRECTION/START", "DIRECTION/EXTERNAL-START", "DIRECTION/CREATIVE-BOOT",
                                                "DIRECTION/VISUAL_TARGET", "DIRECTION/FIRST-OBJECT", "ACTION/FIRST-RENDER",
                                                "ACTION/UI-UX-REALITY", "ACTION/RUN-DIRECTION", "ACTION/GATE-A", "ACTION/GATE-C"],
        "P2 renvois probables hors CHARGE": ["ACTION/PIPELINE-DIRECTION", "ACTION/VISUAL_PROOF", "SAVOIR/TOOLS/CONVERGENCE",
                                             "BIBLIOTHEQUE/SELECT", "SAVOIR/TYPE", "DIRECTION/DIRECTION-ATELIER", "SAVOIR/CRAFT/CFT-00"],
    }
    print(f"SKILL.md : {skill} o")
    for nom, routes in parcours.items():
        detail = [(r, octets(r)) for r in routes]
        print(f"{nom} : {sum(n for _, n in detail)} o -> " + ", ".join(f"{r.split('/', 1)[1]}={n}" for r, n in detail))

    # ---------- T-16 : parcours 1, rendu réel ----------
    if navigateur:
        titre("T-16 parcours 1 : check_render avant / après la retouche de contraste")
        for f in ("avant", "apres"):
            r = run([py, "scripts/check_render.py", str(ICI / "p1" / f"{f}.html"), "--widths", "390,1280",
                     "--json", str(ICI / "p1" / f"{f}.json")], repo)
            ligne = next((l for l in r.stdout.splitlines() if "Contraste du texte" in l), "?")
            print(f"{f}: exit={r.returncode} :: {ligne[:150]}")

    # ---------- T-17 : parcours 3, changement canonique ----------
    titre("T-17 parcours 3 : formulation §9.2 du plan appliquée à DIRECTION (copie de travail détachée)")
    wt = tmp / "wt"
    run(["git", "worktree", "add", "-q", "--detach", str(wt), "HEAD"], repo)
    try:
        p = wt / "V1/official/DIRECTION.md"; t = p.read_text(encoding="utf-8")
        old = ("Brief riche : aucune. Humain présent : les demandes partent avant le build, en un seul message ; le build suit "
               "la réponse, avec des hypothèses nommées pour ce qui manque encore. Humain absent : hypothèses nommées, plafond "
               "déclaré, demandes listées à la livraison. Le rendu est construit dans tous les cas.")
        new = ("Brief riche : aucune. Construis la première scène avec des hypothèses nommées. Pose ces demandes dans la "
               "proposition ; n’attends pas la réponse pour construire, sauf checkpoint demandé ou action irréversible ou coûteuse.")
        assert t.count(old) == 1, "passage canonique introuvable"
        p.write_text(t.replace(old, new), encoding="utf-8")
        run([py, "scripts/build_core.py"], wt)
        r = run([py, "scripts/validate_all.py"], wt, timeout=900)
        print("a) source + noyau modifiés : exit", r.returncode, "::", " | ".join(l for l in r.stdout.splitlines() if l.startswith("- "))[:300])
        vs = wt / "scripts/validate_structure.py"
        vs.write_text("".join(l for l in vs.read_text(encoding="utf-8").splitlines(True) if '("prise de brief : humain présent"' not in l), encoding="utf-8")
        r = run([py, "scripts/validate_all.py"], wt, timeout=900)
        print("b) garde de fidélité retirée : exit", r.returncode, "::", (r.stdout.strip().splitlines() or ["?"])[-1][:120])
        for f, motif in (("V1/official/QUICKSTART.md", "précèdent le build"), ("README.md", "avant de construire"),
                         ("skills/design-governance-practice/references/examples.md", "avant le build :** la personne est présente")):
            print(f"   ancienne règle encore présente dans {f} : {motif in (wt / f).read_text(encoding='utf-8')}")
    finally:
        run(["git", "worktree", "remove", "--force", str(wt)], repo)
        run(["git", "worktree", "prune"], repo)

    shutil.rmtree(tmp, ignore_errors=True)
    print("\nFin. Dépôt non modifié :", run(["git", "status", "--porcelain"], repo).stdout.strip() == "")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
