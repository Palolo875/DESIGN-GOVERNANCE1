#!/usr/bin/env bash
set -euo pipefail

ROOT=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
DIST="$ROOT/dist"
WORK="$ROOT/.build"
BACKUP="$ROOT/.dist.previous"

ARCHIVES_BACKUP="$ROOT/.archives.previous"
ZIPS=(Design_Governance_V1_GITHUB.zip Design_Governance_V1_LOCAL.zip)
LOCK="$ROOT/.distribution.lock"
RUN=""
if ! mkdir "$LOCK" 2>/dev/null; then
  echo "BUILD FAILED — verrou de construction présent ($LOCK) ; ne pas lancer deux builds simultanément" >&2
  if [[ -f "$LOCK/owner.txt" ]]; then cat "$LOCK/owner.txt" >&2; fi
  echo "Diagnostic et reprise manuelle : README.md, section Reprendre une préparation interrompue" >&2
  exit 1
fi
cleanup() {
  if [[ -n "$RUN" ]]; then rm -rf "$RUN"; fi
  rm -f "$LOCK/owner.txt"
  rmdir "$LOCK"
}
trap cleanup EXIT
printf 'pid=%s\nstarted_utc=%s\nroot=%s\n' "$$" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$ROOT" > "$LOCK/owner.txt"

# Même contrôle sur la source canonique avant staging, puis sur chaque projection.
python3 "$ROOT/scripts/build_core.py" --check

# Une sauvegarde d’archives laissée par une restauration incomplète n’est ni restaurée à
# l’aveugle ni supprimée (impossible de savoir quelles archives en place sont neuves).
if [[ -e "$ARCHIVES_BACKUP" ]]; then
  echo "BUILD FAILED — sauvegarde d’archives $ARCHIVES_BACKUP présente : résolution manuelle requise (aucune suppression)" >&2
  exit 1
fi
# Une sauvegarde laissée par un échec précédent est restaurée, jamais supprimée.
if [[ -e "$BACKUP" ]]; then
  if [[ -e "$DIST" ]]; then
    echo "BUILD FAILED — sauvegarde $BACKUP et $DIST présents ensemble : résolution manuelle requise (aucune suppression)" >&2
    exit 1
  fi
  mv "$BACKUP" "$DIST"
  echo "dist antérieur restauré depuis la sauvegarde d’un échec précédent"
fi
mkdir -p "$WORK"
RUN=$(mktemp -d "$WORK/distributions.XXXXXX")
STAGE="$RUN/dist"
ARCHIVES="$RUN/archives"
mkdir -p "$STAGE/github" "$STAGE/local" "$ARCHIVES"

# GitHub : distribution canonique versionnée.
cp -a "$ROOT/README.md" "$STAGE/github/README.md"
cp -a "$ROOT/RELEASE_NOTES.md" "$STAGE/github/RELEASE_NOTES.md"
cp -a "$ROOT/.gitignore" "$STAGE/github/.gitignore"
cp -a "$ROOT/V1" "$STAGE/github/V1"
cp -a "$ROOT/gouvernance" "$STAGE/github/gouvernance"
cp -a "$ROOT/skills" "$STAGE/github/skills"
mkdir -p "$STAGE/github/scripts"
cp -a "$ROOT/scripts/validate_design_governance.py" "$STAGE/github/scripts/validate_design_governance.py"
cp -a "$ROOT/scripts/build_distributions.sh" "$STAGE/github/scripts/build_distributions.sh"
cp -a "$ROOT/scripts/package_manifest.json" "$STAGE/github/scripts/package_manifest.json"
cp -a "$ROOT/scripts/validate_all.py" "$STAGE/github/scripts/validate_all.py"
cp -a "$ROOT/scripts/validate_reading_map.py" "$STAGE/github/scripts/validate_reading_map.py"
cp -a "$ROOT/scripts/read_route.py" "$STAGE/github/scripts/read_route.py"
cp -a "$ROOT/scripts/preparer_livraison.py" "$STAGE/github/scripts/preparer_livraison.py"
cp -a "$ROOT/scripts/test_preparer_livraison.py" "$STAGE/github/scripts/test_preparer_livraison.py"
cp -a "$ROOT/scripts/test_read_route.py" "$STAGE/github/scripts/test_read_route.py"
cp -a "$ROOT/scripts/test_audit_regressions.py" "$STAGE/github/scripts/test_audit_regressions.py"
cp -a "$ROOT/scripts/test_core_budget.py" "$STAGE/github/scripts/test_core_budget.py"
cp -a "$ROOT/scripts/check_render.py" "$STAGE/github/scripts/check_render.py"
cp -a "$ROOT/scripts/test_check_render.py" "$STAGE/github/scripts/test_check_render.py"
cp -a "$ROOT/scripts/validate_structure.py" "$STAGE/github/scripts/validate_structure.py"
cp -a "$ROOT/scripts/build_core.py" "$STAGE/github/scripts/build_core.py"
mkdir -p "$STAGE/github/.github/workflows"
cp -a "$ROOT/.github/workflows/validate.yml" "$STAGE/github/.github/workflows/validate.yml"

# Local : export compact dérivé, avec les chemins directs d’activation.
cp -a "$ROOT/V1/official" "$STAGE/local/official"
cp -a "$ROOT/gouvernance" "$STAGE/local/gouvernance"
cp -a "$ROOT/skills/design-governance-practice" "$STAGE/local/skill"
mkdir -p "$STAGE/local/scripts"
cp -a "$ROOT/scripts/validate_design_governance.py" "$STAGE/local/scripts/validate_design_governance.py"
cp -a "$ROOT/scripts/package_manifest.json" "$STAGE/local/scripts/package_manifest.json"
cp -a "$ROOT/scripts/validate_all.py" "$STAGE/local/scripts/validate_all.py"
cp -a "$ROOT/scripts/validate_reading_map.py" "$STAGE/local/scripts/validate_reading_map.py"
cp -a "$ROOT/scripts/read_route.py" "$STAGE/local/scripts/read_route.py"
cp -a "$ROOT/scripts/test_read_route.py" "$STAGE/local/scripts/test_read_route.py"
cp -a "$ROOT/scripts/test_audit_regressions.py" "$STAGE/local/scripts/test_audit_regressions.py"
cp -a "$ROOT/scripts/test_core_budget.py" "$STAGE/local/scripts/test_core_budget.py"
cp -a "$ROOT/scripts/check_render.py" "$STAGE/local/scripts/check_render.py"
cp -a "$ROOT/scripts/test_check_render.py" "$STAGE/local/scripts/test_check_render.py"
cp -a "$ROOT/scripts/validate_structure.py" "$STAGE/local/scripts/validate_structure.py"
cp -a "$ROOT/scripts/build_core.py" "$STAGE/local/scripts/build_core.py"
cat > "$STAGE/local/README.md" <<'EOF'
# Design Governance V1.0.0 — export Local

Design Governance V1.0.0 est une expérimentation maintenue qui aide à transformer un brief en proposition de design visuellement dirigée, cultivée, spécifique, construite et polie, puis en travail vérifiable. Son usage recommandé est supervisé ; son efficacité réelle reste `NOT-VERIFIED`.

<!-- partage:entree -->

## Pour les agents et les opérateurs

Un agent entre par [`skill/SKILL.md`](skill/SKILL.md) : noyau de fabrication et liste de chargement unique (`DIRECTION/CHARGE`). Pour piloter un run, lisez le guide opérateur [`official/QUICKSTART.md`](official/QUICKSTART.md) ; le vocabulaire est dans [`official/GLOSSAIRE.md`](official/GLOSSAIRE.md). Le mode d’un run est choisi par l’agent avec `DIRECTION/START` ; il n’est jamais demandé à la personne qui fait la demande.

Pour installer la skill : gardez l’export entier ; avec Claude Code, copiez le dossier `skill` dans `.claude/skills/design-governance-practice/` du projet ou de `~/.claude/` ; avec un autre agent, donnez-lui `skill/SKILL.md` comme instructions. Les commandes de la skill s’exécutent depuis la racine de l’export : travaillez dans ce dossier ou indiquez son chemin à l’agent. Vérifiez avec `python3 scripts/read_route.py DIRECTION/START`. Sans accès à l’export, l’agent n’a que le noyau ; après une mise à jour, recopiez la skill.

<!-- partage:constitution -->

Pour charger un seul bloc :

```bash
python3 scripts/read_route.py DIRECTION/START
python3 scripts/read_route.py --trouver "terme"
python3 scripts/read_route.py --connexions
```

Pour renforcer une carte concrète, remplacez le chemin d’exemple par celui de votre fichier :

```bash
python3 gouvernance/outils/validate_run_card.py --strict chemin/vers/run_card.json
```

Les cinq sources normatives sont `official/DIRECTION.md`, `official/ACTION.md`, `official/SAVOIR.md`, `official/BIBLIOTHEQUE.md` et `official/CHANGELOG.md`. `README.md`, `QUICKSTART.md` et `GLOSSAIRE.md` orientent la lecture sans créer de règle concurrente.

La projection machine de référence se trouve dans `gouvernance/schemas/run_card.example.json`. Les contrôles documentaires et machine utilisent la bibliothèque standard Python et supposent Python 3.10 ou plus récent. La recette de rendu et les tests qui ouvrent des pages nécessitent en plus Playwright et son navigateur Chromium ; sans eux, ces tests restent `NOT-VERIFIED`. Pour contrôler la projection :

```bash
python3 gouvernance/outils/validate_run_card.py
```

`STATE: CLOSED` signifie que la trace est persistée ; cela ne signifie pas automatiquement que le résultat est accepté ou entièrement vérifié. La validation du package ou de la `RUN_CARD` confirme uniquement les contrôles exécutés ; elle ne prouve ni l’usage, ni l’accessibilité exécutée, ni la performance, ni la qualité visuelle du produit.

Cet export est autonome : il peut être lu, utilisé et contrôlé sans connexion à un dépôt distant.

Les contrôles disponibles sont :

```bash
python3 scripts/validate_design_governance.py
python3 gouvernance/outils/validate_run_card.py
python3 scripts/validate_reading_map.py
python3 scripts/validate_structure.py
python3 scripts/read_route.py DIRECTION/START
python3 scripts/validate_all.py
```

Dans l’export Local, `validate_all.py` contrôle le package, la projection, les fixtures et la CLI ; `--require-browser` exige les tests de pages, sinon leur indisponibilité reste explicite. Le build et la reproductibilité restent contrôlés depuis la distribution GitHub, avec `scripts/preparer_livraison.py` ; cette commande n’est pas livrée dans l’export Local.
EOF

# L’entrée humaine et la constitution du README Local sont reprises des blocs balisés du README du package
# (une seule source), avec les chemins propres au layout Local.
python3 - "$ROOT/README.md" "$STAGE/local/README.md" <<'PY'
import re
import sys
from pathlib import Path

source = Path(sys.argv[1]).read_text(encoding="utf-8")
target = Path(sys.argv[2])
text = target.read_text(encoding="utf-8")
for name in ("entree", "constitution"):
    found = re.findall(rf"<!-- {name}:début -->.*?<!-- {name}:fin -->", source, re.S)
    if len(found) != 1:
        raise SystemExit(f"BUILD FAILED — README du package : bloc partagé « {name} » trouvé {len(found)} fois (attendu : 1)")
    block = found[0].replace("V1/official/", "official/").replace("skills/design-governance-practice/", "skill/")
    placeholder = f"<!-- partage:{name} -->"
    if text.count(placeholder) != 1:
        raise SystemExit(f"BUILD FAILED — README Local : emplacement « {placeholder} » absent ou multiple")
    text = text.replace(placeholder, block)
target.write_text(text, encoding="utf-8")
PY

# E1 O-1 : chemins propres au layout Local, dans la skill, ses références et QUICKSTART.
python3 - "$STAGE/local" <<'PY'
from pathlib import Path
import sys

root = Path(sys.argv[1])
targets = sorted((root / "skill").rglob("*.md")) + [root / "official" / "QUICKSTART.md", root / "official" / "README.md"]
targets += sorted((root / "gouvernance").glob("*.md")) + sorted((root / "official").glob("*.md"))
for path in dict.fromkeys(targets):
    text = path.read_text(encoding="utf-8")
    rewritten = text.replace("V1/official/", "official/").replace("skills/design-governance-practice/", "skill/")
    # Le README du package est à ../../ depuis V1/official/, à ../ depuis official/ (Local).
    rewritten = rewritten.replace("](../../README.md", "](../README.md")
    # Le module gouvernance/ est à ../../ depuis V1/official/, à ../ depuis official/ (Local).
    rewritten = rewritten.replace("](../../gouvernance/", "](../gouvernance/")
    if rewritten != text:
        path.write_text(rewritten, encoding="utf-8")
PY

# Vérification de la distribution canonique avant archivage.
python3 "$STAGE/github/scripts/validate_design_governance.py"
python3 "$STAGE/github/gouvernance/outils/validate_run_card.py"
python3 "$STAGE/github/gouvernance/outils/validate_contracts.py"
python3 "$STAGE/github/scripts/validate_reading_map.py"
python3 "$STAGE/github/scripts/validate_structure.py"

# Valider les chemins relatifs du Local indépendamment, sans exiger la structure GitHub.
python3 - "$STAGE/local" <<'PY'
from pathlib import Path
import re
import sys

root = Path(sys.argv[1])
import json
manifest = json.loads((root / "scripts" / "package_manifest.json").read_text(encoding="utf-8"))
expected = manifest["local"]
for relative in expected:
    if not (root / relative).is_file():
        raise SystemExit(f"Local export missing: {relative}")
for path in root.rglob("*.md"):
    text = path.read_text(encoding="utf-8")
    for target in re.findall(r"\]\(([^)]+)\)", text):
        target = target.split("#", 1)[0]
        if not target or target.startswith(("http://", "https://", "mailto:")):
            continue
        if not (path.parent / target).exists():
            raise SystemExit(f"Broken Local link: {path} -> {target}")
    # E1 O-1 : chemins `.md` cités entre accents graves (avec un dossier), depuis la racine ou le fichier.
    for target in re.findall(r"`([^`\s]+/[^`\s]*\.md)(?:#[^`]*)?`", text):
        if not ((root / target).exists() or (path.parent / target).exists()):
            raise SystemExit(f"Broken Local path: {path} -> {target}")
print(f"LOCAL EXPORT PASSED — {len(expected)} fichiers attendus et liens contrôlés")
PY
python3 "$STAGE/local/scripts/validate_design_governance.py"
python3 "$STAGE/local/gouvernance/outils/validate_run_card.py"
python3 "$STAGE/local/gouvernance/outils/validate_contracts.py"
python3 "$STAGE/local/scripts/validate_reading_map.py"
python3 "$STAGE/local/scripts/validate_structure.py"
python3 "$STAGE/local/scripts/validate_all.py"

# Archives déterministes du contenu, sans répertoire de travail caché.
# Le build nettoie aussi les caches éventuels avant de copier les sources.
find "$STAGE/github" "$STAGE/local" -type d -name '__pycache__' -prune -exec rm -rf {} +
SOURCE_DATE_EPOCH="${SOURCE_DATE_EPOCH:-0}"
find "$STAGE/github" "$STAGE/local" -exec touch -h -d "@$SOURCE_DATE_EPOCH" {} +
# C8 O-1 : archives créées dans le répertoire de travail, à partir d’un fichier absent.
(
  cd "$STAGE/github"
  LC_ALL=C find . -type f -print | sort | zip -X -q "$ARCHIVES/Design_Governance_V1_GITHUB.zip" -@
)
(
  cd "$STAGE/local"
  LC_ALL=C find . -type f -print | sort | zip -X -q "$ARCHIVES/Design_Governance_V1_LOCAL.zip" -@
)

# C8 O-2 : membres de chaque archive = liste du manifeste, à l’identique, avant publication.
python3 - "$ROOT/scripts/package_manifest.json" "$ARCHIVES" <<'PY'
import json
import sys
import zipfile
from pathlib import Path

manifest = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
archives = Path(sys.argv[2])
for kind, name in (("github", "Design_Governance_V1_GITHUB.zip"), ("local", "Design_Governance_V1_LOCAL.zip")):
    with zipfile.ZipFile(archives / name) as archive:
        members = [info.filename for info in archive.infolist() if not info.is_dir()]
    expected = manifest[kind]
    if len(members) != len(set(members)) or set(members) != set(expected) or len(members) != len(expected):
        extra = sorted(set(members) - set(expected))
        missing = sorted(set(expected) - set(members))
        raise SystemExit(f"BUILD FAILED — membres de l’archive ≠ manifeste ({kind}) : en plus {extra} ; manquants {missing}")
print("ARCHIVE MEMBERS PASSED — membres = manifeste (GitHub et Local)")
PY

# Publier uniquement après validations et archivage réussis.
# Promotion transactionnelle ; en cas d’échec, la sauvegarde est restaurée avant tout nettoyage.
# La transaction couvre dist ET les deux archives ; un échec à n’importe quelle étape remet
# l’ensemble antérieur (dist et archives), puis une relance normale repart d’un état propre.
saved=" " published=" " dist_promoted=0
rollback() {
  local ok=1 name
  for name in "${ZIPS[@]}"; do
    if [[ "$saved" == *" $name "* ]]; then
      mv -f "$ARCHIVES_BACKUP/$name" "$ROOT/$name" || ok=0
    elif [[ "$published" == *" $name "* ]]; then
      rm -f "$ROOT/$name" || ok=0  # aucune archive antérieure : l’archive neuve est retirée
    fi
  done
  if (( dist_promoted )); then
    if [[ -e "$BACKUP" ]]; then
      { rm -rf "$DIST" && mv "$BACKUP" "$DIST"; } || ok=0
    else
      rm -rf "$DIST" || ok=0  # aucun dist antérieur : le dist neuf est retiré
    fi
  elif [[ -e "$BACKUP" && ! -e "$DIST" ]]; then
    mv "$BACKUP" "$DIST" || ok=0
  fi
  if (( ok )); then
    rmdir "$ARCHIVES_BACKUP" 2>/dev/null || true
    echo "BUILD FAILED — $1 ; dist et archives antérieurs restaurés" >&2
  else
    echo "BUILD FAILED — $1 ; restauration incomplète : sauvegardes conservées ($BACKUP, $ARCHIVES_BACKUP), résolution manuelle requise" >&2
  fi
  exit 1
}
mkdir "$ARCHIVES_BACKUP"
for name in "${ZIPS[@]}"; do
  if [[ -e "$ROOT/$name" ]]; then
    mv "$ROOT/$name" "$ARCHIVES_BACKUP/$name" || rollback "sauvegarde de $name impossible"
    saved+="$name "
  fi
done
if [[ -e "$DIST" ]]; then
  mv "$DIST" "$BACKUP" || rollback "sauvegarde de dist impossible"
fi
mv "$STAGE" "$DIST" || rollback "promotion de dist impossible"
dist_promoted=1
for name in "${ZIPS[@]}"; do
  mv -f "$ARCHIVES/$name" "$ROOT/$name" || rollback "publication de $name impossible"
  published+="$name "
done
rm -rf "$BACKUP" "$RUN" "$ARCHIVES_BACKUP"

printf 'Generated:\n  %s\n  %s\n' \
  "$ROOT/Design_Governance_V1_GITHUB.zip" \
  "$ROOT/Design_Governance_V1_LOCAL.zip"
