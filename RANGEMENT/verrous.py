#!/usr/bin/env python3
"""Registre des phrases verrouillées : chaque chaîne littérale d'un script (24 caractères ou plus) que l'on retrouve
mot pour mot dans un document du système. Sert à convertir les verrous fichier par fichier en phase 4.

Pour chaque verrou : script, ligne, contrôle englobant (fonction ou table), chaîne, documents (nom historique) qui la portent.
Usage : verrous.py DEPOT SORTIE.csv
"""
import ast, csv, re, subprocess, sys
from collections import Counter
from pathlib import Path

repo, out = Path(sys.argv[1]), Path(sys.argv[2])
docs = {p: re.sub(r"\s+", " ", (repo / p).read_text(encoding="utf-8"))
        for p in subprocess.run(["git", "-C", str(repo), "ls-files", "*.md"], capture_output=True, text=True).stdout.split()}
rows = []
for script in sorted((repo / "scripts").glob("*.py")):
    tree = ast.parse(script.read_text(encoding="utf-8"))
    owner = {}
    for top in tree.body:
        name = top.name if isinstance(top, (ast.FunctionDef, ast.ClassDef)) else \
            ",".join(t.id for t in getattr(top, "targets", []) if isinstance(t, ast.Name)) or \
            (top.target.id if isinstance(top, ast.AnnAssign) and isinstance(top.target, ast.Name) else "")
        for node in ast.walk(top):
            owner[id(node)] = name
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            s = re.sub(r"\s+", " ", node.value).strip()
            if len(s) < 24 or "{" in s:
                continue
            where = [p for p, t in docs.items() if s in t]
            if where:
                rows.append({"script": script.name, "ligne": node.lineno, "controle": owner.get(id(node), ""),
                             "chaine": s[:160], "documents": " ; ".join(where)})
with out.open("w", newline="", encoding="utf-8") as fh:
    w = csv.DictWriter(fh, fieldnames=["script", "ligne", "controle", "chaine", "documents"])
    w.writeheader()
    w.writerows(rows)
print(len(rows), "verrous ;", dict(Counter(r["script"] for r in rows)))
print("par document :", dict(Counter(d for r in rows for d in r["documents"].split(" ; ")).most_common(8)))
