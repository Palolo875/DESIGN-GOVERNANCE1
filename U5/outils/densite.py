#!/usr/bin/env python3
"""Mesures de densité d'une page rendue (1440 px, après défilement) : texte visible, petits corps, mentions d'exemple, styles."""
import json, sys
from pathlib import Path
from playwright.sync_api import sync_playwright
JS = r"""() => {
 const out={words:0, small:0, smallWords:0, styles:new Set(), exemple:0, nodes:0};
 const walker=document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
 let n; while((n=walker.nextNode())){
   const t=n.textContent.trim(); if(!t) continue;
   const el=n.parentElement; const cs=getComputedStyle(el);
   if(cs.display==='none'||cs.visibility==='hidden'||parseFloat(cs.opacity)===0) continue;
   const r=el.getBoundingClientRect(); if(r.width===0||r.height===0) continue;
   const w=t.split(/\s+/).length; out.words+=w; out.nodes++;
   const fs=parseFloat(cs.fontSize);
   if(fs<14){out.small++; out.smallWords+=w;}
   out.styles.add(cs.fontFamily.split(',')[0]+'|'+Math.round(fs)+'|'+cs.fontWeight);
   const m=t.toLowerCase().match(/exemple|à confirmer|fictiv|démonstration|maquette/g); if(m) out.exemple+=m.length;
 }
 out.styles=out.styles.size; out.height=document.documentElement.scrollHeight; return out;}"""
res={}
with sync_playwright() as pw:
    b=pw.chromium.launch()
    for f in sys.argv[1:]:
        p=b.new_page(viewport={"width":1440,"height":900}); p.goto(Path(f).resolve().as_uri(), wait_until="load"); p.wait_for_timeout(1200)
        y=0
        while y < p.evaluate("document.documentElement.scrollHeight"):
            p.evaluate(f"window.scrollTo(0,{y})"); p.wait_for_timeout(120); y+=450
        p.wait_for_timeout(400)
        res[Path(f).parent.name]=p.evaluate(JS); p.close()
    b.close()
print(f"{'run':<12}{'mots':>6}{'mots<14px':>10}{'%petit':>8}{'styles':>8}{'exemple':>9}{'hauteur':>9}{'mots/écran':>11}")
for k,v in res.items():
    print(f"{k:<12}{v['words']:>6}{v['smallWords']:>10}{100*v['smallWords']/max(1,v['words']):>7.0f}%{v['styles']:>8}{v['exemple']:>9}{v['height']:>9}{v['words']/(v['height']/900):>11.0f}")
