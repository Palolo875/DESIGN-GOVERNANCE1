import sys, pathlib, asyncio
from playwright.sync_api import sync_playwright
ici = pathlib.Path(__file__).resolve().parent
page_url = (ici.parent / "index.html").as_uri()
out = ici / sys.argv[1]; out.mkdir(exist_ok=True)
cas = [
 ("sophie-390", page_url, 390, None, "light", ['[data-tech="Sophie Lambert"]']),
 ("karim-retard-vide-390", page_url, 390, None, "light", ['[data-tech="Karim Benali"]', '#choix-statut [data-statut="En retard"]']),
 ("erreur-390", page_url+"?etat=erreur", 390, None, "light", []),
 ("chargement-390", page_url+"?etat=chargement", 390, None, "light", []),
 ("horsligne-390", page_url+"?etat=horsligne", 390, None, "light", ['[data-tech="Théo Girard"]']),
 ("equipe-sombre-1440", page_url, 1440, None, "dark", ['[data-tech="equipe"]']),
 ("theo-1440", page_url, 1440, None, "light", ['[data-tech="Théo Girard"]']),
]
with sync_playwright() as p:
    b = p.chromium.launch()
    for nom, url, w, _, scheme, clics in cas:
        ctx = b.new_context(viewport={"width": w, "height": 900}, color_scheme=scheme)
        pg = ctx.new_page(); pg.goto(url); pg.wait_for_timeout(900)
        for c in clics: pg.click(c); pg.wait_for_timeout(200)
        pg.evaluate("window.scrollTo(0,0)")
        pg.screenshot(path=str(out/f"{nom}.png"), full_page=True)
        ctx.close()
    b.close()
print("ok")
