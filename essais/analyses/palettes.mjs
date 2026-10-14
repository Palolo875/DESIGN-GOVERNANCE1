// Contrôle des 56 palettes de la bibliothèque de Taste Skill v2 avec les règles de Taste Skill v2 lui-même.
// Usage : node palettes.mjs <dossier taste-skill (celui qui contient SKILL.md)>
import { readFileSync } from 'node:fs';
import { join } from 'node:path';
const root = process.argv[2];
const { colourFamily } = await import(join(root, 'scripts/lib/rules.mjs'));
const pal = JSON.parse(readFileSync(join(root, 'library/palettes.json'), 'utf8'));
function hexToHsl(hex){ hex=hex.replace('#',''); if(hex.length===3) hex=[...hex].map(c=>c+c).join(''); const r=parseInt(hex.slice(0,2),16)/255,g=parseInt(hex.slice(2,4),16)/255,b=parseInt(hex.slice(4,6),16)/255; const mx=Math.max(r,g,b),mn=Math.min(r,g,b); let h=0,s=0; const l=(mx+mn)/2; const d=mx-mn; if(d){ s=d/(1-Math.abs(2*l-1)); if(mx===r) h=((g-b)/d)%6; else if(mx===g) h=(b-r)/d+2; else h=(r-g)/d+4; h*=60; if(h<0)h+=360;} return {h,s:s*100,l:l*100}; }
const lum=(hex)=>{hex=hex.replace('#','');const [r,g,b]=[0,2,4].map(i=>parseInt(hex.slice(i,i+2),16)/255).map(c=>c<=0.03928?c/12.92:((c+0.055)/1.055)**2.4);return 0.2126*r+0.7152*g+0.0722*b;};
const cr=(a,b)=>{const x=lum(a),y=lum(b);const [hi,lo]=x>y?[x,y]:[y,x];return (hi+0.05)/(lo+0.05);};
const rows=[];
for(const p of pal){
  const fams=new Map(); const note=(l,hex)=>{const f=colourFamily(hexToHsl(hex)); if(f) fams.set(f,[...(fams.get(f)||[]),l]);};
  note('bg',p.bg); note('surface',p.surface); note('accent',p.accent); (p.fields||[]).forEach((f,i)=>note('field'+i+'.bg',f.bg));
  const flags=[]; if(fams.has('terracotta')&&fams.has('cream')) flags.push('palette-claude'); else if(fams.has('terracotta')) flags.push('terracotta'); else if(fams.has('cream')) flags.push('cream'); if(fams.has('ai-purple')) flags.push('ai-purple');
  rows.push({id:p.id, inkBg:cr(p.ink,p.bg), mutedBg:cr(p.muted,p.bg), accentInk:cr(p.accentInk,p.accent), accentBg:cr(p.accent,p.bg), fieldsMin:(p.fields||[]).length?Math.min(...p.fields.map(f=>cr(f.ink,f.bg))):null, flags});
}
const f=(x)=>x==null?'-':x.toFixed(1);
console.log('palettes',rows.length);
console.log('ink/bg < 7:', rows.filter(r=>r.inkBg<7).map(r=>r.id+':'+f(r.inkBg)));
console.log('muted/bg < 4.5:', rows.filter(r=>r.mutedBg<4.5).map(r=>r.id+':'+f(r.mutedBg)));
console.log('accentInk/accent < 4.5:', rows.filter(r=>r.accentInk<4.5).map(r=>r.id+':'+f(r.accentInk)));
console.log('field ink/bg < 4.5:', rows.filter(r=>r.fieldsMin!=null&&r.fieldsMin<4.5).map(r=>r.id+':'+f(r.fieldsMin)));
console.log('accent/bg < 4.5 (accent en texte sur le sol):', rows.filter(r=>r.accentBg<4.5).length, 'sur', rows.length);
console.log('accent/bg < 3 (contour de focus 2 px de base.css sur le sol):', rows.filter(r=>r.accentBg<3).length, 'sur', rows.length, rows.filter(r=>r.accentBg<3).map(r=>r.id+':'+f(r.accentBg)));
console.log('familles interdites détectées par colourFamily de TS:', rows.filter(r=>r.flags.length).map(r=>r.id+':'+r.flags.join('+')));
const q=(a)=>{a=[...a].sort((x,y)=>x-y);return [a[0],a[Math.floor(a.length/2)],a.at(-1)].map(v=>v.toFixed(1)).join(' / ')};
console.log('min / médiane / max : ink/bg', q(rows.map(r=>r.inkBg)),'| muted/bg', q(rows.map(r=>r.mutedBg)),'| accentInk/accent', q(rows.map(r=>r.accentInk)),'| accent/bg', q(rows.map(r=>r.accentBg)));
