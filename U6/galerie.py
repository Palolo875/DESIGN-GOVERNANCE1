#!/usr/bin/env python3
"""Galerie autonome des captures ; noms anonymes et ordre de jugement conservés."""
import argparse
import base64
import hashlib
import html
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("judge_folder", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    folder = args.judge_folder.resolve()
    manifest = json.loads((folder / "SHA256.json").read_text())
    for name, digest in manifest.items():
        if hashlib.sha256((folder / name).read_bytes()).hexdigest() != digest:
            parser.error(f"Dossier anonyme modifié : {name}.")
    order = json.loads((folder / "ordre.json").read_text())
    pages = {}
    for page in order["pages"]:
        screenshots = {}
        for name in page["screenshots"]:
            screenshots[name] = "data:image/png;base64," + base64.b64encode((folder / name).read_bytes()).decode()
        pages[page["label"]] = {"brief": page["brief"], "screenshots": screenshots}
    # Les JSON sont placés dans un script non exécutable, avec échappement du HTML.
    payload = json.dumps({"pages": pages, "order": order}, ensure_ascii=False).replace("<", "\\u003c")
    options = "".join(f'<option value="{i}">Comparaison {i+1}</option>' for i in range(len(order["comparisons"])))
    options += "".join(f'<option value="{i+len(order["comparisons"])}">Variété {i+1}</option>' for i in range(len(order["repetitions"])))
    document = '''<!doctype html>
<html lang="fr"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>U6 · Pages anonymisées</title>
<style>
*{box-sizing:border-box}body{margin:0;background:#f3f3f3;color:#202020;font:16px/1.5 system-ui,sans-serif}
header{padding:20px 24px;background:white;border-bottom:1px solid #ddd}h1{font-size:22px;margin:0 0 8px}
.control{display:inline-flex;align-items:center;gap:8px;margin:8px 20px 0 0}select{font:inherit;min-height:44px;padding:4px 10px;border:1px solid #888;border-radius:4px;background:white;color:inherit}
p{margin:8px 0}.hint{font-size:14px;color:#555}.brief{max-width:980px;margin:24px auto;padding:0 20px}
main{display:grid;grid-template-columns:1fr 1fr;gap:20px;padding:0 20px 30px}article{min-width:0;background:white;border:1px solid #ccc}
h2{font-size:16px;padding:12px 16px;margin:0;border-bottom:1px solid #ddd}img{display:block;width:100%;height:auto}
body.mobile article{max-width:390px;width:100%;margin:auto}body.mobile main{max-width:850px;margin:auto}
@media(max-width:760px){main{grid-template-columns:1fr;gap:28px}header{padding:16px}.control{display:flex;margin-right:0}}
</style>
<header><h1>Six pages, sans indication de version</h1>
<p class="hint">Compare la direction, la pertinence, la variété et la finition. Les captures sont fixes ; elles ne démontrent pas le fonctionnement des parcours.</p>
<div class="control"><label for="pair">Pages</label><select id="pair">OPTIONS</select></div>
<div class="control"><label for="width">Largeur</label><select id="width"><option value="1440">Ordinateur · 1440 px</option><option value="390">Mobile · 390 px</option></select></div>
<div class="control"><label for="kind">Vue</label><select id="kind"><option value="premiere">Première scène</option><option value="complete">Page entière</option></select></div>
</header><p class="brief" id="brief"></p><main id="pages"></main>
<script type="application/json" id="data">PAYLOAD</script>
<script>
const data=JSON.parse(document.getElementById('data').textContent);
const groups=[...data.order.comparisons,...data.order.repetitions];
const pair=document.getElementById('pair'),width=document.getElementById('width'),kind=document.getElementById('kind');
function render(){
 const labels=groups[Number(pair.value)],target=document.getElementById('pages');target.replaceChildren();
 document.getElementById('brief').textContent=data.pages[labels[0]].brief;
 document.body.classList.toggle('mobile',width.value==='390');
 for(const label of labels){
  const article=document.createElement('article'),title=document.createElement('h2'),img=document.createElement('img');
  title.textContent='Page '+label;img.alt='Capture de la page '+label+' à '+width.value+' pixels, '+(kind.value==='premiere'?'première scène':'page entière');
  img.src=data.pages[label].screenshots[`${label}-${width.value}-${kind.value}.png`];article.append(title,img);target.append(article);
 }
}
for(const control of [pair,width,kind])control.addEventListener('change',render);render();
</script></html>'''.replace("OPTIONS", options).replace("PAYLOAD", payload)
    if args.output.exists():
        parser.error("La galerie existe déjà : choisir un nouveau nom.")
    args.output.write_text(document)
    print(f"Galerie autonome créée : {args.output}")


if __name__ == "__main__":
    main()
