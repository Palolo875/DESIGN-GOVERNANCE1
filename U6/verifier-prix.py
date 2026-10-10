#!/usr/bin/env python3
"""Vérifie le défaut observé de chevauchement des mentions de prix de B."""
import argparse
import hashlib
import json
import threading
from functools import partial
from http.server import ThreadingHTTPServer
from pathlib import Path
from playwright.sync_api import sync_playwright
from capturer import QuietHandler

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("output", type=Path)
parser.add_argument("report", type=Path)
args = parser.parse_args()
assert not args.report.exists(), "Rapport existant"
source = args.output / "index.html"
before = hashlib.sha256(source.read_bytes()).hexdigest()
server = ThreadingHTTPServer(("127.0.0.1", 0), partial(QuietHandler, directory=str(args.output)))
thread = threading.Thread(target=server.serve_forever, daemon=True)
thread.start()
origin = f"http://127.0.0.1:{server.server_port}"
report = {"index_sha256": before, "viewports": []}
try:
    with sync_playwright() as pw:
        browser = pw.chromium.launch(executable_path="/usr/bin/chromium", args=["--no-sandbox", "--disable-dev-shm-usage"])
        report["browser_version"] = browser.version
        for width in [1440, 390, 320]:
            context = browser.new_context(viewport={"width": width, "height": 1000})
            external = []
            def restrict(route):
                if route.request.url.startswith(origin + "/"):
                    route.continue_()
                else:
                    external.append(route.request.url)
                    route.abort()
            context.route("**/*", restrict)
            page = context.new_page()
            page.goto(origin + "/index.html", wait_until="networkidle")
            page.evaluate("document.fonts.ready")
            rows = page.locator(".service-row").evaluate_all('''rows => rows.map(row => {
                const price=row.querySelector('.service-price'), note=price.querySelector('small'), button=row.querySelector('.pick');
                const b=button.getBoundingClientRect(), range=document.createRange();range.selectNodeContents(note);
                const lines=[...range.getClientRects()].map(r=>({left:r.left,right:r.right,top:r.top,bottom:r.bottom}));
                return {name:row.querySelector('h3').textContent, lines, button:{left:b.left,right:b.right,top:b.top,bottom:b.bottom},
                  overlap:lines.some(r=>r.left < b.right && r.right > b.left && r.top < b.bottom && r.bottom > b.top)};
            })''')
            assert len(rows) == 3
            report["viewports"].append({"width": width, "rows": rows, "external_requests": external,
                                        "status": "PASS" if not external and not any(row["overlap"] for row in rows) else "FAIL"})
            context.close()
        browser.close()
    report["source_unchanged"] = before == hashlib.sha256(source.read_bytes()).hexdigest()
    report["status"] = "PASS" if report["source_unchanged"] and all(v["status"] == "PASS" for v in report["viewports"]) else "FAIL"
    args.report.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"status": report["status"], "widths": [v["width"] for v in report["viewports"]], "source_unchanged": report["source_unchanged"]}))
    if report["status"] != "PASS":
        raise SystemExit(1)
finally:
    server.shutdown()
    server.server_close()
    thread.join(timeout=5)
