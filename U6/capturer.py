#!/usr/bin/env python3
"""Captures comparables et observations techniques, sans modifier le livrable."""
import argparse
import hashlib
import json
import threading
from datetime import datetime, timezone
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

from playwright.sync_api import sync_playwright


def manifest(folder):
    result = {}
    for path in sorted(folder.rglob("*")):
        if path.is_symlink():
            raise ValueError(f"Lien symbolique interdit dans le livrable : {path.name}")
        if path.is_file():
            result[str(path.relative_to(folder))] = hashlib.sha256(path.read_bytes()).hexdigest()
    return result


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *_):
        pass


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path)
    parser.add_argument("audit", type=Path)
    args = parser.parse_args()
    output, audit = args.output.resolve(), args.audit.resolve()
    if audit == output or output in audit.parents or audit in output.parents:
        parser.error("Le dossier d'audit doit être séparé du livrable.")
    if not (output / "index.html").is_file():
        parser.error("Le livrable ne contient pas index.html ; aucune capture n'est inventée.")
    if audit.exists():
        parser.error("Le dossier d'audit existe déjà ; choisir un nouveau nom pour conserver les preuves.")
    before = manifest(output)
    audit.mkdir(parents=True)
    report = {
        "started_at": datetime.now(timezone.utc).isoformat(),
        "output_sha256": before,
        "status": "requires_manual_review",
        "functional_tests": "NOT-VERIFIED: actions et erreurs propres à la page à rejouer séparément",
        "limitations": [
            "Les observations automatiques ne sont pas un audit WCAG complet.",
            "Le parcours principal et la vérité du contenu nécessitent une vérification séparée.",
            "Le focus et les petites cibles sont des indices à inspecter, pas des verdicts automatiques.",
        ],
        "viewports": [],
    }
    server = ThreadingHTTPServer(("127.0.0.1", 0), partial(QuietHandler, directory=str(output)))
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    origin = f"http://127.0.0.1:{server.server_port}"
    try:
        with sync_playwright() as pw:
            browser = pw.chromium.launch(
                executable_path="/usr/bin/chromium",
                args=["--no-sandbox", "--disable-dev-shm-usage"],
            )
            report["browser_version"] = browser.version
            report["browser_executable"] = "/usr/bin/chromium"
            for width, height in [(1440, 1000), (390, 844), (320, 844)]:
                context = browser.new_context(viewport={"width": width, "height": height}, device_scale_factor=1)
                events = {"console_errors": [], "page_errors": [], "external_requests": [], "failed_requests": []}
                page = context.new_page()
                page.on("pageerror", lambda exc: events["page_errors"].append(str(exc)))
                page.on("console", lambda msg: events["console_errors"].append(msg.text) if msg.type == "error" else None)
                page.on("requestfailed", lambda req: events["failed_requests"].append({"url": req.url, "failure": req.failure}))

                def restrict(route):
                    url = route.request.url
                    parsed = urlparse(url)
                    if parsed.scheme in {"data", "blob", "about"} or url.startswith(origin + "/"):
                        route.continue_()
                    else:
                        events["external_requests"].append(url)
                        route.abort()

                context.route("**/*", restrict)
                response = page.goto(origin + "/index.html", wait_until="networkidle")
                page.evaluate("document.fonts.ready")
                page.wait_for_timeout(250)
                page.evaluate("window.scrollTo({top:0,behavior:'instant'})")
                page.wait_for_timeout(100)
                if page.evaluate("scrollY") != 0:
                    raise RuntimeError("La capture de première scène ne peut pas attester scrollY=0.")
                first_name = f"{width}-premiere.png"
                page.screenshot(path=str(audit / first_name), animations="disabled")
                # Faire entrer les images différées dans le viewport avant la capture longue.
                page.evaluate("""async () => {
                    for (let y=0; y<document.documentElement.scrollHeight; y+=window.innerHeight) {
                        window.scrollTo({top:y,behavior:'instant'});
                        await new Promise(resolve=>setTimeout(resolve,50));
                    }
                    await Promise.all([...document.images].map(img=>img.decode().catch(()=>null)));
                    window.scrollTo({top:0,behavior:'instant'});
                }""")
                page.wait_for_timeout(100)
                if page.evaluate("scrollY") != 0:
                    raise RuntimeError("La capture longue ne peut pas attester scrollY=0.")
                full_name = f"{width}-complete.png"
                page.screenshot(path=str(audit / full_name), full_page=True, animations="disabled")
                dom = page.evaluate("""() => {
                    const visible=e=>!!(e.getClientRects().length) && getComputedStyle(e).visibility!=='hidden';
                    const rect=e=>{const r=e.getBoundingClientRect();return {width:r.width,height:r.height};};
                    return {
                        title:document.title, lang:document.documentElement.lang,
                        client_width:document.documentElement.clientWidth,
                        scroll_width:document.documentElement.scrollWidth,
                        headings:[...document.querySelectorAll('h1,h2,h3,h4,h5,h6')].map(e=>({level:Number(e.tagName[1]),text:e.textContent.trim()})),
                        broken_images:[...document.images].filter(e=>!e.complete||e.naturalWidth===0).map(e=>e.getAttribute('src')?.slice(0,100)),
                        missing_alts:[...document.images].filter(e=>!e.hasAttribute('alt')).map(e=>e.outerHTML.slice(0,120)),
                        unlabelled_fields:[...document.querySelectorAll('input:not([type=hidden]):not([type=submit]):not([type=button]),select,textarea')]
                            .filter(e=>visible(e)&&!e.labels?.length&&!e.getAttribute('aria-label')&&!e.getAttribute('aria-labelledby'))
                            .map(e=>({tag:e.tagName,id:e.id,type:e.type})),
                        unresolved_anchors:[...document.querySelectorAll('a[href^="#"]')]
                            .filter(e=>e.getAttribute('href')==='#'||!document.getElementById(e.getAttribute('href').slice(1)))
                            .map(e=>({text:e.textContent.trim(),href:e.getAttribute('href')})),
                        small_targets:[...document.querySelectorAll('button,a,input,select')].filter(visible)
                            .filter(e=>{const r=rect(e);return r.width<24||r.height<24;})
                            .map(e=>({tag:e.tagName,text:(e.textContent||e.getAttribute('aria-label')||'').trim(),...rect(e)})),
                    };
                }""")
                focus_steps = []
                for _ in range(16):
                    page.keyboard.press("Tab")
                    focus_steps.append(page.evaluate("""() => {
                        const e=document.activeElement, s=getComputedStyle(e);
                        return {tag:e.tagName,id:e.id,text:(e.textContent||e.getAttribute('aria-label')||'').trim().slice(0,80),
                            focus_visible_match:e.matches(':focus-visible'),outline:s.outline,box_shadow:s.boxShadow};
                    }"""))
                report["viewports"].append({
                    "width": width, "height": height, "http_status": response.status,
                    "screenshots": {"first": first_name, "full": full_name},
                    "horizontal_overflow": dom["scroll_width"] > dom["client_width"] + 1,
                    "dom": dom, "focus_steps": focus_steps, "events": events,
                })
                context.close()
            browser.close()
        after = manifest(output)
        report["source_unchanged"] = before == after
        if before != after:
            raise RuntimeError("Le livrable a changé pendant les mesures ; preuves à invalider.")
        report["finished_at"] = datetime.now(timezone.utc).isoformat()
        report["evidence_sha256"] = manifest(audit)
        (audit / "observations.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
        print(json.dumps({"audit": str(audit), "status": report["status"], "viewports": len(report["viewports"])}, ensure_ascii=False))
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=5)


if __name__ == "__main__":
    main()
