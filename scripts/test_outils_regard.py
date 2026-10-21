#!/usr/bin/env python3
"""Tests des outils du regard : registre des choix, spécimen de voix, planche, cartes de moment.

Partie A, sans navigateur : catégories et comparaisons du registre, pages du spécimen et de la planche
(échappement, repli, contenu), cartes de moment lues dans DIRECTION/CHARGE, manques de la fiche de mobilisation.
Partie B, dans un navigateur : registre, spécimen et planche sur une page d'essai. Sans navigateur, la partie B
reste NOT-VERIFIED ; `--require-browser` la rend obligatoire.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import journal_mobilisation as jm  # noqa: E402
import planche  # noqa: E402
import read_route  # noqa: E402
import registre_choix as rc  # noqa: E402
import specimen  # noqa: E402

failures: list[str] = []
count = {"A": 0, "B": 0}


def expect(part: str, label: str, got, want) -> None:
    count[part] += 1
    ok = got == want
    print(f"  [{'ok' if ok else 'ÉCHEC'}] {label}" + ("" if ok else f" : obtenu {got!r}, attendu {want!r}"))
    if not ok:
        failures.append(f"{part} {label}")


def part_a() -> None:
    print("Partie A — sans navigateur")
    expect("A", "fond sombre", rc.famille_fond({"L": 0.15, "C": 0.01, "H": 250}), "sombre")
    expect("A", "fond crème", rc.famille_fond({"L": 0.96, "C": 0.012, "H": 85}), "crème ou beige")
    expect("A", "fond clair neutre", rc.famille_fond({"L": 0.98, "C": 0.002, "H": 90}), "clair neutre")
    expect("A", "fond non évalué", rc.famille_fond(None), "non évalué (image ou dégradé)")
    expect("A", "teinte orange", rc.teinte(40), "orange")
    expect("A", "teinte rouge (bord du cercle)", rc.teinte(355), "rouge")
    m = {"titre": {"famille": "Serif X"}, "familles": ["Sans Y", "Serif X"], "rendues": {"titre": "Serif X", "corps": "Sans Y"},
         "palette": {"fond": {"hex": "#f5f3ee", "L": 0.96, "C": 0.01, "H": 85}, "chromatiques": [{"hex": "#c03", "H": 5}]}}
    e = rc.entree(m, "/a.html", "brief 1")
    expect("A", "entrée : police, fichier rendu, fond, accent",
           [e["police_titre"], e["rendue_corps"], e["famille_fond"], e["teinte_accent"]], ["Serif X", "Sans Y", "crème ou beige", "rouge"])
    expect("A", "registre vide : rien à comparer", rc.comparer(e, [])[0].startswith("Premier choix"), True)
    meme_page = dict(e)
    expect("A", "la même page n'est pas comparée à elle-même", rc.comparer(e, [meme_page])[0].startswith("Premier choix"), True)
    autre = dict(e, page="/b.html", police_titre="Autre", familles=["Nom local"], rendue_titre="Autre", rendue_corps="Sans Y")
    lignes = rc.comparer(e, [autre])
    expect("A", "fichier rendu partagé malgré un nom local différent", any("Sans Y" in l and "nom interne" in l for l in lignes), True)
    expect("A", "fond partagé signalé", any(l.startswith("Fond « crème ou beige »") for l in lignes), True)
    expect("A", "synthèse : fichiers rendus comptés", any("Sans Y ×2" in l for l in rc.synthese([e, autre])), True)

    voix = specimen.lire_voix(["Fraunces=f.woff2", "Georgia"])
    expect("A", "voix lues", voix, [("Fraunces", "f.woff2"), ("Georgia", None)])
    html = specimen.page('Titre <b>"x"</b>', voix, "corps", {"Fraunces": "f.woff2"})
    expect("A", "spécimen : titre échappé", "<b>" not in html and "&lt;b&gt;" in html, True)
    expect("A", "spécimen : famille entre guillemets échappés dans l'attribut", 'font-family:&quot;specimen-0&quot;' in html, True)
    expect("A", "spécimen : @font-face pour un fichier", '@font-face{font-family:"specimen-0";src:url("f.woff2")' in html, True)

    p = planche.planche("page.html", "défaut <x>", ["geste & effet"], [], ["capture-390px.png", "capture-1440px.png"])
    expect("A", "planche : défaut et geste échappés", "défaut &lt;x&gt;" in p and "geste &amp; effet" in p, True)
    expect("A", "planche : questions par défaut", all(q.split(",")[0] in p for q in planche.QUESTIONS), True)
    expect("A", "planche : champ de correction nommée", 'id="changer"' in p and "Ce que je changerais d’abord" in p, True)
    expect("A", "planche : captures citées", 'src="capture-390px.png"' in p and 'src="capture-1440px.png"' in p, True)

    for m_ in read_route.MOMENTS:
        routes = read_route.moment_routes(m_)
        expect("A", f"carte « {m_} » : routes lues dans DIRECTION/CHARGE et résolues",
               all(read_route.resolve(r) for r in routes) and len(routes) >= 2, True)
    chunks, total = read_route.moment_text("regard")
    expect("A", "carte « regard » : tableau des gestes servi", any(l == "SAVOIR/STATE/Vocabulaire" for l, _ in chunks)
           and "Cohérence de rayon" in dict(chunks)["SAVOIR/STATE/Vocabulaire"], True)
    entrees = [{"outil": "read_route", "commande": ["--tronc", "DIRECTION"], "code": 0, "routes_lues": []},
               {"outil": "read_route", "commande": ["--moment", "regard"], "code": 0, "routes_lues": ["SAVOIR/STATE/Vocabulaire"]}]
    fiche = jm.fiche(entrees)
    expect("A", "fiche : cartes sautées signalées en DIRECTION", "Cartes de moment non consultées (DIRECTION) : avant, sortie" in fiche, True)
    fiche = jm.fiche([{"outil": "read_route", "commande": ["--tronc", "STANDARD"], "code": 0, "routes_lues": []}])
    expect("A", "fiche : aucune carte exigée hors DIRECTION", "Cartes de moment" in fiche, False)


PAGE = ('<!doctype html><html lang="fr"><head><meta charset="utf-8"><title>Essai</title></head>'
        '<body style="margin:0;background:#f5f3ee;font-family:serif"><h1>Fromagerie Brunet</h1>'
        '<p>Trois marchés par semaine, six fromages du moment, une seule cave au fond de la cour.</p>'
        '<p style="color:#b42318">Samedi, place du Marché</p></body></html>')


def part_b(require: bool) -> str:
    print("Partie B — dans un navigateur")
    try:
        import playwright.sync_api  # noqa: F401
    except ImportError:
        msg = "NOT-VERIFIED : Playwright absent"
        print("  " + msg)
        if require:
            failures.append("B navigateur requis")
        return msg
    with tempfile.TemporaryDirectory() as tmp:
        d = Path(tmp)
        (d / "page.html").write_text(PAGE, encoding="utf-8")
        env = dict(os.environ)
        env.pop("DG_JOURNAL", None)
        run = lambda *a: subprocess.run([sys.executable, *a], capture_output=True, text=True, env=env, cwd=HERE.parent)
        r = run("scripts/registre_choix.py", str(d / "page.html"), "--registre", str(d / "r.jsonl"))
        if r.returncode == 2 and "NOT-VERIFIED" in r.stdout:
            msg = "NOT-VERIFIED : navigateur indisponible (" + r.stdout.strip()[:120] + ")"
            print("  " + msg)
            if require:
                failures.append("B navigateur requis")
            return msg
        expect("B", "registre : entrée écrite", r.returncode == 0 and len((d / "r.jsonl").read_text().splitlines()) == 1, True)
        entree = json.loads((d / "r.jsonl").read_text().splitlines()[0])
        expect("B", "registre : fond crème relevé", entree["famille_fond"], "crème ou beige")
        expect("B", "registre : fichier de police rendu relevé", bool(entree["rendue_titre"]), True)
        (d / "copie.html").write_text(PAGE, encoding="utf-8")
        r = run("scripts/registre_choix.py", str(d / "copie.html"), "--registre", str(d / "r.jsonl"))
        expect("B", "registre : une seconde page identique est signalée", "déjà dans 1 des 1" in r.stdout, True)
        r = run("scripts/registre_choix.py", str(d / "page.html"))
        expect("B", "registre : rien sans fichier de registre", r.returncode, 2)
        r = run("scripts/specimen.py", "--titre", "Fromagerie Brunet", "--voix", "Police Absente Du Système", "--voix", "serif",
                "--sortie", str(d / "spec"))
        expect("B", "spécimen : deux captures", all((d / "spec" / f"specimen-{w}px.png").is_file() for w in specimen.LARGEURS), True)
        expect("B", "spécimen : repli signalé pour une police absente", "Police Absente Du Système : rendue par" in r.stdout
               and "REPLI" in r.stdout.split("Police Absente Du Système")[1].splitlines()[0], True)
        r = run("scripts/specimen.py", "--titre", "x", "--voix", "Seule", "--sortie", str(d / "spec2"))
        expect("B", "spécimen : une seule voix refusée", r.returncode, 2)
        r = run("scripts/planche.py", str(d / "page.html"), "--sortie", str(d / "pl"), "--defaut", "le titre flotte")
        expect("B", "planche : page et captures écrites", r.returncode == 0 and (d / "pl" / "planche.html").is_file()
               and all((d / "pl" / f"capture-{w}px.png").is_file() for w in planche.LARGEURS), True)
    return f"{count['B']} cas"


if __name__ == "__main__":
    require = "--require-browser" in sys.argv
    part_a()
    b = part_b(require)
    if failures:
        print(f"OUTILS DU REGARD TESTS FAILED — {len(failures)} échec(s) : " + "; ".join(failures))
        sys.exit(1)
    print(f"OUTILS DU REGARD TESTS PASSED — A : {count['A']} cas ; B : {b}")
