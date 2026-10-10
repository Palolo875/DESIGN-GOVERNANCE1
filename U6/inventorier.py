#!/usr/bin/env python3
"""Inventaire descriptif identique des six pages ; aucune note esthétique."""
import json
import threading
from functools import partial
from http.server import ThreadingHTTPServer
from pathlib import Path

from playwright.sync_api import sync_playwright
from capturer import QuietHandler, manifest

root = Path(__file__).resolve().parent
protocol = json.loads((root / "protocole.json").read_text())
target = root / "inventaire-visuel.json"
if target.exists():
    raise SystemExit("Inventaire existant : ne pas écraser une preuve.")
for case in protocol["cases"]:
    if not (root / "runs" / case["run"] / "livrable-manifest.json").exists():
        raise SystemExit(f"Livrable non figé : {case['run']}.")

report = {"scope": "Styles calculés et séquence DOM à 1440 px ; pas de note de qualité ou de variété.", "pages": []}
with sync_playwright() as pw:
    browser = pw.chromium.launch(executable_path="/usr/bin/chromium", args=["--no-sandbox", "--disable-dev-shm-usage"])
    report["browser_version"] = browser.version
    try:
        for case in protocol["cases"]:
            output = Path(case["output"])
            before = manifest(output)
            expected = json.loads((root / "runs" / case["run"] / "livrable-manifest.json").read_text())
            if before != expected:
                raise ValueError(f"Livrable modifié : {case['run']}.")
            server = ThreadingHTTPServer(("127.0.0.1", 0), partial(QuietHandler, directory=str(output)))
            thread = threading.Thread(target=server.serve_forever, daemon=True)
            thread.start()
            context = browser.new_context(viewport={"width": 1440, "height": 1000})
            origin = f"http://127.0.0.1:{server.server_port}"
            external = []
            def restrict(route):
                if route.request.url.startswith(origin + "/"):
                    route.continue_()
                else:
                    external.append(route.request.url)
                    route.abort()
            context.route("**/*", restrict)
            try:
                page = context.new_page()
                page.goto(origin + "/index.html", wait_until="networkidle")
                page.evaluate("document.fonts.ready")
                inventory = page.evaluate("""() => {
                  const style = e => {const s=getComputedStyle(e);return {
                    tag:e.tagName, text:e.textContent.trim().replace(/\\s+/g,' ').slice(0,200),
                    font_family:s.fontFamily,font_size:s.fontSize,font_weight:s.fontWeight,
                    font_style:s.fontStyle,color:s.color,background:s.backgroundColor,
                    line_height:s.lineHeight,letter_spacing:s.letterSpacing};};
                  const main=document.querySelector('main')||document.body;
                  return {
                    body:style(document.body),title:style(document.querySelector('h1')),
                    h2_sequence:[...document.querySelectorAll('h2')].filter(e=>e.getClientRects().length).map(style),
                    first_scene_controls:[...main.querySelectorAll('a,button,input,select')]
                      .filter(e=>{const r=e.getBoundingClientRect();return r.width&&r.height&&r.top<1000&&r.bottom>0;}).map(style),
                    loaded_fonts:[...document.fonts].map(f=>({family:f.family,status:f.status,style:f.style,weight:f.weight})),
                    document_height:document.documentElement.scrollHeight
                  };
                }""")
                report["pages"].append({"run": case["run"], "label": case["anonymous_label"],
                    "condition": case["condition"], "inventory": inventory,
                    "external_requests": external, "source_unchanged": before == manifest(output)})
            finally:
                context.close()
                server.shutdown()
                server.server_close()
                thread.join(timeout=5)
    finally:
        browser.close()
target.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({"pages": len(report["pages"]), "source_unchanged": all(p["source_unchanged"] for p in report["pages"])}))
