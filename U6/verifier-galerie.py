#!/usr/bin/env python3
"""Vérifie l'affichage et les contrôles de la galerie autonome, puis capture les paires."""
import argparse
import hashlib
import json
import threading
from functools import partial
from http.server import ThreadingHTTPServer
from pathlib import Path

from playwright.sync_api import sync_playwright, expect
from capturer import QuietHandler

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("gallery", type=Path)
parser.add_argument("audit", type=Path)
args = parser.parse_args()
gallery, audit = args.gallery.resolve(), args.audit.resolve()
if audit.exists():
    parser.error("Audit existant : choisir un nouveau dossier.")
before = hashlib.sha256(gallery.read_bytes()).hexdigest()
audit.mkdir(parents=True)
server = ThreadingHTTPServer(("127.0.0.1", 0), partial(QuietHandler, directory=str(gallery.parent)))
thread = threading.Thread(target=server.serve_forever, daemon=True)
thread.start()
origin = f"http://127.0.0.1:{server.server_port}"
report = {"checks":[], "captures":{}, "gallery_sha256":before}
try:
    with sync_playwright() as pw:
        browser = pw.chromium.launch(executable_path="/usr/bin/chromium", args=["--no-sandbox", "--disable-dev-shm-usage"])
        report["browser_version"] = browser.version
        context = browser.new_context(viewport={"width":1440,"height":1000})
        external, errors = [], []
        def restrict(route):
            if route.request.url.startswith(origin + "/"):
                route.continue_()
            else:
                external.append(route.request.url)
                route.abort()
        context.route("**/*", restrict)
        page = context.new_page()
        page.on("pageerror",lambda exc:errors.append(str(exc)))
        page.goto(origin + "/" + gallery.name, wait_until="networkidle")
        for group, labels in enumerate([["F","A"],["E","C"],["B","D"],["F","E"],["A","C"]]):
            page.get_by_label("Pages",exact=True).select_option(str(group))
            expect(page.locator("article h2")).to_have_text(["Page "+label for label in labels])
            for width in [1440,390]:
                page.get_by_label("Largeur").select_option(str(width))
                for kind in ["premiere","complete"]:
                    page.get_by_label("Vue").select_option(kind)
                    page.evaluate("Promise.all([...document.images].map(img=>img.decode()))")
                    images = page.locator("article img").evaluate_all("imgs=>imgs.map(i=>({width:i.naturalWidth,height:i.naturalHeight,complete:i.complete}))")
                    assert all(i["width"]==width and i["height"]>0 and i["complete"] for i in images), images
                    report["checks"].append({"group":group,"labels":labels,"source_width":width,"kind":kind,"status":"PASS","images":images})
                    if group < 3 and kind == "premiere":
                        name=f"comparaison-{group+1}-{width}.png"
                        page.screenshot(path=str(audit/name),full_page=True)
                        report["captures"][name]=hashlib.sha256((audit/name).read_bytes()).hexdigest()
        for width in [1440,390,320]:
            page.set_viewport_size({"width":width,"height":1000})
            overflow=page.evaluate("document.documentElement.scrollWidth > document.documentElement.clientWidth")
            assert not overflow, width
            report["checks"].append({"gallery_viewport":width,"horizontal_overflow":overflow,"status":"PASS"})
        assert not external, external
        assert not errors, errors
        report["external_requests"],report["page_errors"]=external,errors
        report["source_unchanged"]=before==hashlib.sha256(gallery.read_bytes()).hexdigest()
        assert report["source_unchanged"]
        context.close()
        browser.close()
    report["status"]="PASS"
    (audit/"galerie-verification.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps({"checks":len(report["checks"]),"captures":len(report["captures"]),"status":report["status"]}))
except Exception as exc:
    report["status"]="FAIL"
    report["error"]=str(exc)
    report["source_unchanged"]=before==hashlib.sha256(gallery.read_bytes()).hexdigest()
    (audit/"galerie-verification.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
    raise
finally:
    server.shutdown()
    server.server_close()
    thread.join(timeout=5)
