#!/usr/bin/env python3
"""Capture pleine page après défilement complet, pour déclencher les contenus révélés au scroll.

Usage : capture_defilee.py PAGE.html DOSSIER_SORTIE
Même largeurs et même attente que check_render (390 et 1440 px, 1500 ms), polices externes autorisées.
"""
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

page_path, out = Path(sys.argv[1]).resolve(), Path(sys.argv[2])
out.mkdir(parents=True, exist_ok=True)
with sync_playwright() as pw:
    browser = pw.chromium.launch()
    for w in (390, 1440):
        h = 844 if w < 700 else 900
        ctx = browser.new_context(viewport={"width": w, "height": h})
        page = ctx.new_page()
        page.goto(page_path.as_uri(), wait_until="load")
        page.wait_for_timeout(1500)
        y, total = 0, page.evaluate("document.documentElement.scrollHeight")
        while y < total:
            page.evaluate(f"window.scrollTo(0, {y})")
            page.wait_for_timeout(250)
            y += h // 2
            total = page.evaluate("document.documentElement.scrollHeight")
        page.evaluate("window.scrollTo(0, 0)")
        page.wait_for_timeout(800)
        page.screenshot(path=str(out / f"capture-{w}px.png"), full_page=True)
        ctx.close()
    browser.close()
print("ok", out)
