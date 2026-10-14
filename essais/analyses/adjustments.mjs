// Applique la fonction `adjustments()` de draw.mjs (Taste Skill v2) à chaque section et chaque héros de la bibliothèque,
// pour compter combien de modèles contredisent les règles de la maison et que la fiche doit corriger au moment du tirage.
// La fonction est extraite du fichier source puis exécutée sur les données ; draw.mjs n'est pas lancé.
// Usage : node adjustments.mjs <dossier taste-skill (contient SKILL.md)>
import { readFileSync } from 'node:fs';
import { join } from 'node:path';
const root = process.argv[2];
const src = readFileSync(join(root, 'scripts/draw.mjs'), 'utf8');
const a = src.indexOf('function adjustments(bp, s) {'); const b = src.indexOf('// Every blueprint of a role that suits');
const adjustments = new Function(src.slice(a, b) + '\nreturn adjustments;')();
const lib = (n) => JSON.parse(readFileSync(join(root, 'library', n + '.json'), 'utf8'));
const label = (n) => n.replace(/^It /, '').split(/[:;.]/)[0].slice(0, 62);
// corrections d'adaptation (mapper des couleurs ou des familles sur la fiche) : ne comptent pas comme contradiction d'une règle de la maison
const adaptation = (n) => /^It (names colours|names a kind of typeface|names its own corners)/.test(n);
for (const [kind, items] of [['sections', lib('sections')], ['héros', lib('heroes')]]) {
  let withNote = 0, withHard = 0; const byRule = new Map(); const counts = [];
  for (const x of items) {
    const notes = adjustments(x, { type: null }); counts.push(notes.length);
    if (notes.length) withNote++;
    if (notes.some((n) => !adaptation(n))) withHard++;
    for (const n of notes) byRule.set(label(n), (byRule.get(label(n)) || 0) + 1);
  }
  const med = [...counts].sort((p, q) => p - q)[Math.floor(counts.length / 2)];
  console.log(`${kind} : ${items.length} entrées, ${withNote} avec au moins une correction (${Math.round(100 * withNote / items.length)} %), médiane ${med} correction(s) par entrée, maximum ${Math.max(...counts)} ; dont ${withHard} (${Math.round(100 * withHard / items.length)} %) avec une correction qui ne se réduit pas à une adaptation de couleur, de famille ou de coins`);
  for (const [k, v] of [...byRule.entries()].sort((p, q) => q[1] - p[1])) console.log(`   ${String(v).padStart(3)}  ${k}`);
}
