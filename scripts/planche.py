#!/usr/bin/env python3
"""Planche de regard humain, à l'essai : demander une correction nommée sur la dernière finition.

Méthode : `DIRECTION/DOUBLE-LOOP`, « Regard humain sur la dernière finition ». Quand la boucle autonome ne change
plus la relation visée, la planche montre la page à 390 et 1440 px, le défaut dominant restant, les gestes déjà
essayés et quelques questions précises ; la personne répond par une correction nommée (« ce que je changerais
d'abord, et où »), qui revient dans la boucle comme un diagnostic. La planche ne note rien, ne garde rien en
mémoire et ne prouve ni l'usage, ni l'accessibilité, ni la qualité.

Usage :
  python3 scripts/planche.py page.html --sortie planche/ --defaut "le titre écrase la photo à 390 px" \
      [--essaye "Masse visuelle : titre réduit d'un cran"] [--question "Le titre doit-il passer sous l'image ?"]
Requiert Playwright avec Chromium pour les captures ; sans navigateur, NOT-VERIFIED (code 2), rien n'est écrit.
"""
from __future__ import annotations

import argparse
import html
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

LARGEURS = (390, 1440)
QUESTIONS = (
    "Qu’est-ce qui vous semble encore générique, ou pourrait appartenir à n’importe quel autre projet ?",
    "Quel détail n’est pas au niveau de l’idée (alignement, rythme, raccord, matière) ?",
)


def planche(page: str, defaut: str, essayes: list[str], questions: list[str], captures: list[str]) -> str:
    """Page HTML autonome de la planche ; les textes fournis sont échappés."""
    e = html.escape
    q = "".join(f"<li>{e(x)}</li>" for x in (questions or list(QUESTIONS)))
    g = "".join(f"<li>{e(x)}</li>" for x in essayes) or "<li>aucun geste noté</li>"
    figs = "".join(f'<figure><img src="{e(c)}" alt="Capture de la page à {e(c.split("-")[-1].split(".")[0])}" loading="lazy">'
                   f'<figcaption>{e(c.split("-")[-1].split(".")[0])}</figcaption></figure>' for c in captures)
    date = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    return f"""<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Planche de regard</title><style>
:root{{--fond:#fafaf8;--texte:#1b1b1b;--doux:#5b5b5b;--trait:#d9d9d4;--accent:#1f4fd1}}
@media (prefers-color-scheme:dark){{:root{{--fond:#141414;--texte:#ececec;--doux:#a8a8a8;--trait:#333;--accent:#8fb0ff}}}}
body{{margin:0;background:var(--fond);color:var(--texte);font:16px/1.55 system-ui,sans-serif}}
main{{max-width:1180px;margin:0 auto;padding:24px 16px 64px}}
h1{{font-size:clamp(22px,3vw,30px);margin:0 0 4px}} .meta{{color:var(--doux);margin:0 0 24px;word-break:break-all}}
.defaut{{font-size:clamp(18px,2.2vw,22px);border-left:4px solid var(--accent);padding:8px 0 8px 14px;margin:0 0 20px}}
.grille{{display:grid;grid-template-columns:minmax(0,1fr);gap:24px}} @media (min-width:860px){{.grille{{grid-template-columns:minmax(0,1fr) minmax(0,1.2fr)}}}}
.captures{{display:flex;gap:16px;align-items:flex-start;overflow-x:auto}} figure{{margin:0;flex:0 0 auto}}
figure:first-child img{{width:min(260px,70vw)}} figure:last-child img{{width:min(560px,85vw)}}
img{{display:block;border:1px solid var(--trait);height:auto}} figcaption{{color:var(--doux);font-size:14px;margin-top:6px}}
label{{display:block;font-weight:600;margin:16px 0 6px}} textarea{{width:100%;box-sizing:border-box;min-height:110px;font:inherit;padding:10px;border:1px solid var(--trait);background:transparent;color:inherit;border-radius:4px}}
button{{margin-top:12px;font:inherit;padding:10px 16px;border:0;border-radius:4px;background:var(--accent);color:#fff;cursor:pointer}}
button:focus-visible,textarea:focus-visible{{outline:3px solid var(--accent);outline-offset:2px}} ul{{padding-left:20px}}
</style></head><body><main>
<h1>Planche de regard</h1><p class="meta">{e(page)} · {e(date)}</p>
<p class="defaut"><strong>Défaut dominant restant :</strong> {e(defaut)}</p>
<div class="grille"><section><h2>Ce qui a déjà été essayé</h2><ul>{g}</ul>
<h2>Questions</h2><ol>{q}</ol>
<label for="changer">Ce que je changerais d’abord</label><textarea id="changer" placeholder="Une correction nommée : quoi, et dans quel sens"></textarea>
<label for="ou">Où (élément, zone, largeur)</label><textarea id="ou" placeholder="Par exemple : le titre à 390 px, la marge sous la photo"></textarea>
<button type="button" id="copier">Copier la réponse</button> <span id="etat" role="status" aria-live="polite"></span></section>
<section class="captures" aria-label="Captures de la page">{figs}</section></div>
<p class="meta">Une correction nommée vaut mieux qu’une note : elle revient dans la boucle comme un diagnostic. Cette planche ne garde rien en mémoire.</p>
</main><script>
document.getElementById('copier').addEventListener('click', async () => {{
  const t = 'Ce que je changerais d’abord : ' + document.getElementById('changer').value + '\\nOù : ' + document.getElementById('ou').value;
  const etat = document.getElementById('etat');
  try {{ await navigator.clipboard.writeText(t); etat.textContent = 'Réponse copiée.'; }}
  catch (e) {{ etat.textContent = 'Copie impossible : sélectionnez le texte à la main.'; }}
}});
</script></body></html>"""


def capturer(page: Path, sortie: Path) -> list[str]:
    from playwright.sync_api import sync_playwright
    exe = os.environ.get("DG_BROWSER_EXECUTABLE", "")
    noms = []
    with sync_playwright() as p:
        b = p.chromium.launch(**({"executable_path": exe} if exe else {}))
        for w in LARGEURS:
            pg = b.new_page(viewport={"width": w, "height": 844 if w < 900 else 900})
            pg.goto(page.resolve().as_uri()); pg.wait_for_timeout(800)
            nom = f"capture-{w}px.png"
            pg.screenshot(path=str(sortie / nom), full_page=True); noms.append(nom)
            pg.close()
        b.close()
    return noms


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Planche de regard humain (à l'essai) : une correction nommée sur la dernière finition.")
    ap.add_argument("page", help="page HTML à montrer")
    ap.add_argument("--sortie", required=True, help="dossier de la planche (planche.html et captures)")
    ap.add_argument("--defaut", required=True, help="défaut dominant restant, nommé")
    ap.add_argument("--essaye", action="append", default=[], help="geste déjà essayé et son effet (répétable)")
    ap.add_argument("--question", action="append", default=[], help="question précise à poser (répétable ; deux questions par défaut)")
    a = ap.parse_args(argv)
    src = Path(a.page)
    if not src.is_file():
        ap.error(f"page introuvable : {a.page}")
    if not a.defaut.strip():
        ap.error("le défaut dominant doit être nommé")
    sortie = Path(a.sortie); sortie.mkdir(parents=True, exist_ok=True)
    try:
        captures = capturer(src, sortie)
    except ImportError:
        print("NOT-VERIFIED — Playwright absent : planche non écrite."); return 2
    except Exception as exc:  # navigateur indisponible : jamais simulé
        print(f"NOT-VERIFIED — navigateur indisponible ({exc.__class__.__name__}) : planche non écrite."); return 2
    cible = sortie / "planche.html"
    cible.write_text(planche(str(src), a.defaut, a.essaye, a.question, captures), encoding="utf-8")
    print(f"PLANCHE — {cible} ; captures : {', '.join(captures)}")
    print("À montrer à la personne ; sa correction nommée revient dans la boucle d’édition (DIRECTION/DOUBLE-LOOP).")
    return 0


if __name__ == "__main__":
    import journal_mobilisation  # journal passif : n'écrit rien sans DG_JOURNAL
    sys.exit(journal_mobilisation.executer("planche", main, sys.argv[1:]))
