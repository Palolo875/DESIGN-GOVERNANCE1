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
  echo "Diagnostic et reprise manuelle : maintenance/README.md, section Reprendre une préparation interrompue" >&2
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
cp -a "$ROOT/design" "$STAGE/github/design"
cp -a "$ROOT/agent" "$STAGE/github/agent"
cp -a "$ROOT/maintenance" "$STAGE/github/maintenance"
cp -a "$ROOT/guides" "$STAGE/github/guides"
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

# Local : même arborescence et même README que GitHub, sans les outils de préparation ni l’intégration continue.
cp -a "$STAGE/github/." "$STAGE/local/"
rm -rf "$STAGE/local/.github" "$STAGE/local/.gitignore" "$STAGE/local/scripts/build_distributions.sh" \
  "$STAGE/local/scripts/preparer_livraison.py" "$STAGE/local/scripts/test_preparer_livraison.py"

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
    # Un chemin entre accents graves ; pas la suite « ](… » d'un lien Markdown placé après un nom entre accents graves.
    for target in re.findall(r"`([^`\s\[\]()]+/[^`\s()]*\.md)(?:#[^`\s]*)?`", text):
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
