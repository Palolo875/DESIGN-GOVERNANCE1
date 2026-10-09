#!/usr/bin/env python3
"""Audit 2 (phase 1) : mesures par fichier et par section, sans rien modifier.

Mesure les critères « outil » de la grille d'un fichier (F3, F4, F5, F6, F8, F9, F11, F12)
et l'inventaire des contrôles (S8). Lit le dépôt en lecture seule.

Usage : mesures.py DOSSIER_SORTIE
Sorties : mesures.json (tout), mesures.md (tableaux lisibles).
"""
import ast, json, re, statistics, subprocess, sys
from collections import Counter, defaultdict
from pathlib import Path

REPO = Path("/home/user/DESIGN-GOVERNANCE1")
OUT = Path(sys.argv[1])
FILES = subprocess.run(["git", "-C", str(REPO), "ls-files"], capture_output=True, text=True, check=True).stdout.split()
DOCS = [f for f in FILES if f.endswith(".md")]
SCRIPTS = [f for f in FILES if f.startswith("scripts/") or f.startswith(".github/")]
DATA = [f for f in FILES if f.startswith("schemas/")]

# Codes internes visibles : locators, identifiants numérotés, jetons en capitales composés, sous-gates.
LOCATOR = re.compile(r"\b(?:DIRECTION|ACTION|SAVOIR|BIBLIOTHEQUE|CHANGELOG)/[A-Za-z0-9_\-/]+")
NUMBERED = re.compile(r"\b[A-Z]{1,5}-\d{2}[a-z]?\b|\bC\d{2}\b")
COMPOUND = re.compile(r"\b[A-Z][A-Z0-9]+(?:[_\-/][A-Z0-9]+)+\b")
SUBGATE = re.compile(r"\bB\d[a-z]\b")
CAPS = re.compile(r"\b[A-ZÀ-Ý]{4,}\b")
CAPS_OK = {"HTML", "JSON", "WCAG", "UTF", "HTTP", "HTTPS", "README", "SKILL", "TODO", "NOTE", "PASS", "FAIL", "LITE",
           "MODE", "WARNING", "ERROR", "SVG", "PNG", "JPEG", "WEBP", "AVIF", "CSS", "ARIA", "RGAA", "GITHUB", "LOCAL",
           "OKLCH", "SAAS", "API", "URL"}
NOT_VERIFIED = re.compile(r"NOT-VERIFIED")
VESTIGE = re.compile(r"R20\d\d-\d\d-\d\d-[A-Z\-]+|\bdésormais\b|ne porte plus|pointeur de compatibilité|anciennement|"
                     r"révision précédente|révisions précédentes|\bU[1-9]\b|\bC[0-9]{2}\b(?=.*constat)", re.I)
LINK = re.compile(r"\]\(([^)#\s]+)(?:#[^)]*)?\)")
FILE_MENTION = re.compile(r"`?([A-Za-z_/\.\-]+\.(?:md|py|json|sh|yml))`?")
WORD = re.compile(r"[\wÀ-ÿ’'\-]+")


def prose_lines(lines):
    """Lignes de prose : hors blocs de code, commentaires HTML, tableaux et titres."""
    fence = False
    for n, line in enumerate(lines, 1):
        s = line.strip()
        if s.startswith("```"):
            fence = not fence
            continue
        if fence or not s or s.startswith(("<!--", "|", "#")):
            continue
        yield n, s


def sentences(lines):
    text = " ".join(s.lstrip("-*> ").strip() for _, s in prose_lines(lines))
    text = re.sub(r"`[^`]*`", "X", text)
    parts = re.split(r"(?<=[.!?;:])\s+(?=[A-ZÀ-Ý«`(*])", text)
    return [len(WORD.findall(p)) for p in parts if len(WORD.findall(p)) >= 3]


def codes(text):
    body = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    found = Counter()
    # Chaque occurrence n'est comptée qu'une fois : on retire ce qui est compté avant de passer au motif suivant.
    for rx, kind in ((LOCATOR, "route"), (NUMBERED, "numéro"), (COMPOUND, "composé"), (SUBGATE, "sous-gate")):
        found[kind] += len(rx.findall(body))
        body = rx.sub(" ", body)
    for m in CAPS.findall(body):
        if m not in CAPS_OK:
            found["capitales"] += 1
    return found


def headings(lines):
    fence = False
    out = []
    for n, line in enumerate(lines, 1):
        if line.strip().startswith("```"):
            fence = not fence
        elif not fence and re.match(r"^#{1,6} ", line):
            out.append((n, len(line) - len(line.lstrip("#")), line.lstrip("#").strip()))
    return out


def opening(lines):
    out = []
    for _, s in prose_lines(lines):
        out.append(s)
        if sum(len(x) for x in out) > 280:
            break
    return " ".join(out)[:320]


def sections(path, lines):
    heads = headings(lines)
    rows = []
    for i, (n, lvl, title) in enumerate(heads):
        if lvl > 3:
            continue
        end = next((m for m, l2, _ in heads[i + 1:] if l2 <= lvl), len(lines) + 1)
        body = "\n".join(lines[n - 1:end - 1])
        words = len(WORD.findall(body))
        c = codes(body)
        rows.append({"fichier": path, "ligne": n, "niveau": lvl, "titre": title[:90], "caracteres": len(body),
                     "mots": words, "codes": sum(c.values()),
                     "codes_pour_1000_mots": round(1000 * sum(c.values()) / max(words, 1)),
                     "non_verifie": len(NOT_VERIFIED.findall(body))})
    return rows


def shingles(path, lines, k=14):
    """Fenêtres de k mots de prose, pour repérer les passages répétés entre fichiers et dans un fichier."""
    out = defaultdict(set)
    for n, s in prose_lines(lines):
        words = [w.lower() for w in WORD.findall(re.sub(r"`[^`]*`", " ", s))]
        for i in range(0, max(len(words) - k + 1, 0)):
            out[" ".join(words[i:i + k])].add((path, n))
    return out


def core_lines():
    """Lignes de la skill qui sont la copie compilée du noyau (répétition voulue)."""
    lines = (REPO / "skills/design-governance-practice/SKILL.md").read_text(encoding="utf-8").splitlines()
    inside, keep = False, set()
    for n, line in enumerate(lines, 1):
        if "noyau:compilé début" in line:
            inside = True
        elif "noyau:compilé fin" in line:
            inside = False
        elif inside:
            keep.add(n)
    return keep


docs, all_sections, grams = [], [], defaultdict(set)
for path in DOCS:
    text = (REPO / path).read_text(encoding="utf-8")
    lines = text.splitlines()
    heads = headings(lines)
    words = len(WORD.findall(text))
    sl = sentences(lines)
    c = codes(text)
    secs = sections(path, lines)
    all_sections += secs
    for g, locs in shingles(path, lines).items():
        grams[g] |= locs
    links = [l for l in LINK.findall(text) if not l.startswith(("http", "mailto"))]
    mentions = sorted({m for m in FILE_MENTION.findall(text) if Path(m).name in {Path(f).name for f in FILES}})
    docs.append({
        "fichier": path, "caracteres": len(text), "mots": words, "lignes": len(lines),
        "titres_par_niveau": dict(Counter(l for _, l, _ in heads)),
        "profondeur_max": max((l for _, l, _ in heads), default=0),
        "plus_grosse_section": max(((s["caracteres"], s["titre"]) for s in secs if s["niveau"] >= 2), default=(0, ""))[::-1],
        "ouverture": opening(lines),
        "codes": dict(c), "codes_total": sum(c.values()),
        "codes_pour_1000_mots": round(1000 * sum(c.values()) / max(words, 1)),
        "non_verifie": len(NOT_VERIFIED.findall(text)),
        "vestiges": sorted({m.group(0) for m in VESTIGE.finditer(text)})[:20],
        "phrases": {"nombre": len(sl), "mots_moyenne": round(statistics.mean(sl), 1) if sl else 0,
                    "mots_p90": sorted(sl)[int(0.9 * (len(sl) - 1))] if sl else 0,
                    "part_plus_de_40_mots": round(sum(1 for x in sl if x > 40) / len(sl), 2) if sl else 0},
        "liens_relatifs": sorted(set(links)), "fichiers_cites": mentions,
    })

# Répétitions : fenêtres partagées, regroupées par paire de fichiers, hors copie compilée du noyau.
compiled = core_lines()
pairs = Counter()
examples = {}
for g, locs in grams.items():
    locs = {(p, n) for p, n in locs if not (p.endswith("SKILL.md") and n in compiled)}
    files = sorted({p for p, _ in locs})
    if len(locs) < 2:
        continue
    key = tuple(files) if len(files) > 1 else (files[0], files[0])
    pairs[key] += 1
    examples.setdefault(key, sorted(locs)[:4])
repetitions = [{"fichiers": list(k), "fenetres_de_14_mots": v, "exemple": examples[k]} for k, v in pairs.most_common()]

# Contrôles : identifiants de vérification, tests, phrases du texte verrouillées par des chaînes littérales.
doc_texts = {p: re.sub(r"\s+", " ", (REPO / p).read_text(encoding="utf-8")) for p in DOCS}
controls = []
for path in SCRIPTS:
    src = (REPO / path).read_text(encoding="utf-8")
    entry = {"fichier": path, "lignes": src.count("\n") + 1}
    if path.endswith(".py"):
        tree = ast.parse(src)
        literals = [n.value for n in ast.walk(tree) if isinstance(n, ast.Constant) and isinstance(n.value, str)]
        ids = sorted(set(re.findall(r"\b(?:[A-Z]{2,5})-\d{2}[a-z]?\b", src)))
        locked = defaultdict(int)
        for lit in literals:
            norm = re.sub(r"\s+", " ", lit).strip()
            if len(norm) < 24 or "{" in norm:
                continue
            for p, t in doc_texts.items():
                if norm in t:
                    locked[p] += 1
        entry.update({
            "fonctions": sum(isinstance(n, ast.FunctionDef) for n in ast.walk(tree)),
            "tests": sum(isinstance(n, ast.FunctionDef) and n.name.startswith("test_") for n in ast.walk(tree)),
            "identifiants_de_controle": len(ids), "identifiants_exemples": ids[:12],
            "phrases_verrouillees_par_fichier": dict(sorted(locked.items(), key=lambda x: -x[1])),
            "phrases_verrouillees_total": sum(locked.values()),
            "fichiers_ouverts": sorted({m for m in re.findall(r"[\"']([A-Za-z_/\.\-]+\.(?:md|json|py|sh|yml))[\"']", src)}),
        })
    controls.append(entry)

data = {"commit": subprocess.run(["git", "-C", str(REPO), "rev-parse", "--short", "HEAD"], capture_output=True, text=True).stdout.strip(),
        "documents": docs, "sections": all_sections, "repetitions": repetitions, "controles": controls,
        "donnees": [{"fichier": p, "caracteres": (REPO / p).stat().st_size} for p in DATA]}
OUT.mkdir(parents=True, exist_ok=True)
(OUT / "mesures.json").write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")

# Vue lisible.
md = [f"# Mesures par fichier — commit `{data['commit']}`", "",
      "Produit par `AUDIT2/outils/mesures.py` ; aucune saisie à la main. Codes : identifiants internes visibles "
      "(routes, numéros, jetons composés en capitales, sous-gates, mots en capitales hors sigles usuels).", "",
      "## Documents", "",
      "| Fichier | Caractères | Titres (niveaux) | Plus grosse section | Codes /1000 mots | Non vérifié | Phrases : moyenne / p90 / >40 mots | Vestiges |",
      "|---|---:|---|---|---:|---:|---|---|"]
for d in sorted(docs, key=lambda d: -d["caracteres"]):
    big = d["plus_grosse_section"]
    md.append(f"| `{d['fichier']}` | {d['caracteres']:,} | {d['titres_par_niveau']} | {big[0][:40]} ({big[1]:,}) | "
              f"{d['codes_pour_1000_mots']} | {d['non_verifie']} | {d['phrases']['mots_moyenne']} / {d['phrases']['mots_p90']} / "
              f"{int(100 * d['phrases']['part_plus_de_40_mots'])} % | {len(d['vestiges'])} |".replace(",", " "))
md += ["", "## Répétitions entre fichiers (fenêtres de 14 mots identiques, hors copie compilée du noyau)", "",
       "| Fichiers | Fenêtres | Exemple |", "|---|---:|---|"]
for r in repetitions[:30]:
    md.append(f"| {' ↔ '.join('`' + f + '`' for f in r['fichiers'])} | {r['fenetres_de_14_mots']} | "
              f"{', '.join(f'{p.split(chr(47))[-1]}:{n}' for p, n in r['exemple'])} |")
md += ["", "## Scripts et contrôles", "",
       "| Script | Lignes | Fonctions | Tests | Identifiants de contrôle | Phrases du texte verrouillées |",
       "|---|---:|---:|---:|---:|---:|"]
for c in sorted(controls, key=lambda c: -c["lignes"]):
    md.append(f"| `{c['fichier']}` | {c['lignes']} | {c.get('fonctions', '')} | {c.get('tests', '')} | "
              f"{c.get('identifiants_de_controle', '')} | {c.get('phrases_verrouillees_total', '')} |")
md += ["", "## Sections les plus lourdes (niveaux 2 et 3, plus de 8 000 caractères)", "",
       "| Fichier | Ligne | Section | Caractères | Codes /1000 mots | Non vérifié |", "|---|---:|---|---:|---:|---:|"]
for s in sorted((s for s in all_sections if s["niveau"] >= 2 and s["caracteres"] > 8000), key=lambda s: -s["caracteres"]):
    md.append(f"| `{s['fichier'].split('/')[-1]}` | {s['ligne']} | {s['titre'][:60]} | {s['caracteres']:,} | "
              f"{s['codes_pour_1000_mots']} | {s['non_verifie']} |".replace(",", " "))
(OUT / "mesures.md").write_text("\n".join(md) + "\n", encoding="utf-8")
print(f"{len(docs)} documents, {len(all_sections)} sections, {len(controls)} scripts, {len(repetitions)} paires répétées")
