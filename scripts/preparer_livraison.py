#!/usr/bin/env python3
"""Préparer la livraison du paquet depuis sa distribution GitHub, sans envoi ni déploiement.

Par défaut, deux étapes, celles que le système exige :
  1. compiler le noyau de la skill (`scripts/build_core.py`) ;
  2. lancer la validation complète (`scripts/validate_all.py`) : contrôles documentaires, tests,
     construction des distributions GitHub et Local, reproductibilité.

Options, jamais requises :
  --markdown DOSSIER  écrit deux copies de lecture tirées de l'archive GitHub : une copie complète,
                      restaurable à l'octet près, et une copie des documents seuls ; la restauration
                      est vérifiée avant de rendre la main.
  --empreintes        affiche l'empreinte sha256 des archives, pour un suivi tenu hors du paquet.
  --log CHEMIN        journal détaillé des étapes (défaut : .logs/preparer_livraison.log).
  --journal CHEMIN    alias compatible de --log.
  --require-browser   exiger l'exécution des tests navigateur, sinon échouer.

Codes de sortie : 0 livraison préparée ; 1 préparation échouée ; 2 arguments invalides.
Les limites des contrôles sont visibles même lorsqu'une étape réussit.
"""
from __future__ import annotations

import argparse
import datetime
import hashlib
import re
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARCHIVES = ("Design_Governance_V1_GITHUB.zip", "Design_Governance_V1_LOCAL.zip")
LANG = {"json": "json", "py": "python", "sh": "bash", "yml": "yaml"}
FIRST = ["README.md", "RELEASE_NOTES.md", "V1/official/README.md", "V1/official/QUICKSTART.md", "V1/official/READING_MAP.md",
         "V1/official/DIRECTION.md", "V1/official/ACTION.md", "V1/official/SAVOIR.md", "V1/official/BIBLIOTHEQUE.md",
         "V1/official/CHANGELOG.md"]
# Script de restauration embarqué dans la copie complète. Le motif est découpé pour ne jamais contenir le marqueur littéral.
RESTORE = '''import re, sys, hashlib, pathlib
src, dest = sys.argv[1], pathlib.Path(sys.argv[2])
text = pathlib.Path(src).read_bytes().decode("utf-8")
pat = r"<!-" r"- BEGIN FILE ([^\\n]+?) sha256=([0-9a-f]{64}) fence=(\\d*) -->\\n((?s:.*?))\\n<!-" r"- END FILE -->"
items = re.findall(pat, text)
count = re.search(r"<!-" r"- DG-COPY files=(\\d+) -->", text)
if not count or not items or len(items) != int(count.group(1)):
    raise SystemExit("restauration refusée : inventaire incomplet ou absent")
files = {}; destinations = {}; base = dest.resolve()
for path, sha, fence, body in items:
    rel = pathlib.PurePosixPath(path)
    if rel.is_absolute() or ".." in rel.parts or "\\\\" in path or path != rel.as_posix() or path in files:
        raise SystemExit("restauration refusée : chemin incorrect ou répété : " + path)
    if fence:
        lines = body.split("\\n"); marker = "`" * int(fence)
        if int(fence) < 3 or not lines[0].startswith(marker) or lines[-1] != marker:
            raise SystemExit("restauration refusée : clôture incorrecte : " + path)
        body = "\\n".join(lines[1:-1])
    raw = body.encode("utf-8")
    if hashlib.sha256(raw).hexdigest() != sha:
        raise SystemExit("restauration refusée : empreinte divergente : " + path)
    out = (base / path).resolve()
    if out == base or not out.is_relative_to(base):
        raise SystemExit("restauration refusée : chemin hors destination : " + path)
    if out in destinations or any(out in previous.parents or previous in out.parents for previous in destinations):
        raise SystemExit("restauration refusée : destinations équivalentes ou fichier/dossier en collision : " + path)
    if (out.exists() and not out.is_file()) or any(parent.exists() and not parent.is_dir() for parent in out.parents):
        raise SystemExit("restauration refusée : destination incompatible : " + path)
    files[path] = raw
    destinations[out] = path
for path, raw in files.items():
    out = dest / path; out.parent.mkdir(parents=True, exist_ok=True); out.write_bytes(raw)
print(len(files), "fichiers restaurés et empreintes vérifiées dans", dest)'''


def step(title: str, command: list[str], journal: Path) -> None:
    print(f"… {title}", flush=True)
    done = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
    with journal.open("a", encoding="utf-8") as log:
        log.write(f"\n## {title}\nCommande : {' '.join(command)}\nCode : {done.returncode}\n")
        log.write(done.stdout + done.stderr)
    if done.returncode != 0:
        print(done.stdout[-4000:] + done.stderr[-4000:])
        raise SystemExit(f"PRÉPARATION ÉCHOUÉE — étape : {title} (code {done.returncode}) ; journal : {journal}")
    # Les résultats synthétiques des fixtures ne sont pas des réserves sur une livraison.
    # Conserver les bilans et les limites déclarées par les contrôles, sans recopier chaque cas.
    shown = set()
    for line in (done.stdout + done.stderr).splitlines():
        if re.match(r"^\s*(?:NOT-VERIFIED\b|WARNING\b|RÉSERVE\b|CORE BUDGET (?:TESTS )?PASSED|READ_ROUTE TESTS PASSED|PREPARATION TESTS PASSED|CHECK_RENDER TESTS PASSED|FULL VALIDATION PASSED|LOCAL VALIDATION PASSED)", line):
            if line not in shown:
                print("  " + line.strip()); shown.add(line)
    if done.stderr.strip():
        print("  Sortie stderr conservée dans le journal : " + done.stderr.strip()[-1000:])


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def order(name: str) -> tuple:
    if name in FIRST:
        return (0, FIRST.index(name), name)
    group = 0 if name.startswith("V1/") else 1 if name.startswith("skills/") else 2 if name.startswith("schemas/") else 3 if name.startswith("scripts/") else 4
    return (1 + group, 0, name)


def markdown_copy(archive: Path, only_docs: bool) -> str:
    z = zipfile.ZipFile(archive)
    names = sorted((n for n in z.namelist() if not n.endswith("/") and (n.endswith(".md") or not only_docs)), key=order)
    changelog = (ROOT / "V1" / "official" / "CHANGELOG.md").read_text(encoding="utf-8")
    version = (re.search(r"`(V\d+\.\d+\.\d+)`", changelog) or [None, "V1"])[1]
    revision = re.search(r"Révision[^`\n]*`([^`]+)`", (ROOT / "README.md").read_text(encoding="utf-8"))
    title = f"Design Governance {version} — " + ("documents en Markdown" if only_docs else "copie complète en Markdown")
    head = [f"# {title}\n",
            f"<!-- DG-COPY files={len(names)} -->\n",
            f"Design Governance {version} est une expérimentation maintenue. Cette copie de lecture ne crée aucune règle : "
            "l’autorité reste aux sources normatives du paquet.\n",
            f"- **Contenu** : {'documents seuls ; sans scripts, schémas ni CI' if only_docs else f'les {len(names)} fichiers du paquet'}.",
            f"- **Provenance** : `{archive.name}` (sha256 `{sha256(archive)[:12]}…`)"
            + (f", révision `{revision.group(1)}`" if revision else "")
            + f", copie générée le {datetime.date.today().isoformat()}.",
            "- **Lecture** : chaque fichier est précédé de son chemin et de son empreinte. Ne pas charger cette copie entière dans un agent : "
            "le paquet se lit par route (`scripts/read_route.py`)."]
    if only_docs:
        head.append("- **Limite** : cette version ne permet pas de reconstituer le paquet exécutable.\n")
    else:
        head += ["- **Restauration** : enregistrer le script ci-dessous puis `python3 restaurer.py cette_copie.md dossier`.\n",
                 "```python", RESTORE, "```\n"]
    head += ["## Table des fichiers\n", "| N° | Chemin | Octets | sha256 (12) |", "|---:|---|---:|---|"]
    body = []
    for i, name in enumerate(names, 1):
        raw = z.read(name)
        text, digest = raw.decode("utf-8"), hashlib.sha256(raw).hexdigest()
        head.append(f"| {i} | [`{name}`](#f-{i}) | {len(raw)} | `{digest[:12]}` |")
        if name.endswith(".md"):
            fence, inner = "", text
        else:
            fence = "`" * (max([len(m) for m in re.findall(r"`+", text)] + [2]) + 1)
            ext = name.rsplit(".", 1)[-1] if "." in name.split("/")[-1] else "text"
            inner = f"{fence}{LANG.get(ext, 'text')}\n{text}\n{fence}"
        body.append(f"\n---\n\n<a id=\"f-{i}\"></a>\n**Fichier {i}/{len(names)} · `{name}` · {len(raw)} octets**\n\n"
                    f"<!-- BEGIN FILE {name} sha256={digest} fence={len(fence) if fence else ''} -->\n{inner}\n<!-- END FILE -->\n")
    return "\n".join(head) + "\n" + "".join(body)


def verify(copy: Path, archive: Path, only_docs: bool) -> None:
    """Restaure la copie avec le script qu'elle embarque (ou le même, pour la copie des documents) et compare à l'octet."""
    with tempfile.TemporaryDirectory() as tmp:
        script = Path(tmp) / "restaurer.py"
        script.write_text(RESTORE, encoding="utf-8")
        out = Path(tmp) / "out"
        done = subprocess.run([sys.executable, str(script), str(copy), str(out)], capture_output=True, text=True)
        if done.returncode != 0:
            raise SystemExit(f"PRÉPARATION ÉCHOUÉE — restauration de {copy.name} : {done.stderr.strip()[-300:]}")
        z = zipfile.ZipFile(archive)
        expected = {n: z.read(n) for n in z.namelist() if not n.endswith("/") and (n.endswith(".md") or not only_docs)}
        got = {str(p.relative_to(out)): p.read_bytes() for p in out.rglob("*") if p.is_file()}
        if got != expected:
            raise SystemExit(f"PRÉPARATION ÉCHOUÉE — {copy.name} ne restitue pas l’archive à l’octet près")


def main() -> int:
    ap = argparse.ArgumentParser(description="Prépare la livraison depuis la distribution GitHub : compilation, contrôles et exports, sans envoi ni déploiement.")
    ap.add_argument("--markdown", metavar="DOSSIER", help="écrire aussi les deux copies de lecture en Markdown (option)")
    ap.add_argument("--empreintes", action="store_true", help="afficher l'empreinte sha256 des archives (option)")
    ap.add_argument("--log", "--journal", dest="log", default=".logs/preparer_livraison.log", metavar="CHEMIN", help="conserver la sortie détaillée des contrôles (--journal est un alias)")
    ap.add_argument("--require-browser", action="store_true", help="exiger l’exécution des tests navigateur, sinon échouer")
    args = ap.parse_args()
    if not (ROOT / "scripts/build_distributions.sh").is_file() or not (ROOT / "V1/official").is_dir():
        raise SystemExit("PRÉPARATION ÉCHOUÉE — commande réservée à la distribution GitHub. "
                         "Dans l’export Local, utiliser python3 scripts/validate_all.py.")
    journal = Path(args.log).resolve()
    if journal.is_relative_to(ROOT / ".build") or journal.is_relative_to(ROOT / "dist"):
        ap.error("le journal doit être hors des répertoires de construction .build et dist")
    if journal == ROOT or journal.suffix != ".log":
        ap.error("le journal doit être un fichier .log")
    journal.parent.mkdir(parents=True, exist_ok=True)
    journal.write_text("Design Governance — journal de préparation de livraison\n", encoding="utf-8")
    print(f"Journal détaillé : {journal}", flush=True)
    step("compilation du noyau", [sys.executable, "scripts/build_core.py"], journal)
    command = [sys.executable, "scripts/validate_all.py"]
    if args.require_browser:
        command.append("--require-browser")
    step("contrôles du package, distributions et reproductibilité", command, journal)
    archives = [ROOT / name for name in ARCHIVES]
    missing = [a.name for a in archives if not a.is_file()]
    if missing:
        raise SystemExit(f"PRÉPARATION ÉCHOUÉE — archive absente : {', '.join(missing)}")
    if args.markdown:
        target = Path(args.markdown)
        target.mkdir(parents=True, exist_ok=True)
        for only_docs, name in ((False, "Design_Governance_V1_complet.md"), (True, "Design_Governance_V1_documents.md")):
            copy = target / name
            copy.write_text(markdown_copy(archives[0], only_docs), encoding="utf-8", newline="")
            verify(copy, archives[0], only_docs)
            print(f"… copie Markdown vérifiée : {copy}")
    print("LIVRAISON PRÉPARÉE — contrôles du package exécutés, distributions : " + ", ".join(a.name for a in archives))
    print("Cette préparation ne certifie aucun rendu ni résultat d’usage. Journal : " + str(journal))
    if args.empreintes:
        for a in archives:
            print(f"  {a.name} sha256 {sha256(a)}")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, UnicodeError, zipfile.BadZipFile) as exc:
        print(f"PRÉPARATION ÉCHOUÉE — {type(exc).__name__} : {exc}", file=sys.stderr)
        sys.exit(1)
