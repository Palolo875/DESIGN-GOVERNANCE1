#!/usr/bin/env bash
set -euo pipefail

dg_repo=/workspace/DESIGN-GOVERNANCE1
dg_setup=/workspace/cloud-setup/design-governance
for dg_tool in python3 bash zip unzip node chromium; do
  command -v "$dg_tool"
done
python3 -c 'import sys; assert sys.version_info >= (3, 10), "Python >=3.10 requis"'
test -f "$dg_repo/scripts/validate_all.py"
mkdir -p "$dg_setup"
if [[ ! -x "$dg_setup/venv/bin/python" ]]; then
  python3 -m venv "$dg_setup/venv"
fi
dg_python="$dg_setup/venv/bin/python"
export PATH="$dg_setup/venv/bin:$PATH"
if ! "$dg_python" -c 'from importlib.metadata import version; assert version("playwright") == "1.56.0"' >/dev/null 2>&1; then
  PIP_CACHE_DIR="$dg_setup/pip-cache" "$dg_python" -m pip install --disable-pip-version-check 'playwright==1.56.0'
fi
if [[ -f "$dg_repo/supports/fonts/requirements.txt" ]]; then
  if ! "$dg_python" -c 'from importlib.metadata import version; assert version("fonttools") == "4.60.1" and version("brotli") == "1.1.0"' >/dev/null 2>&1; then
    PIP_CACHE_DIR="$dg_setup/pip-cache" "$dg_python" -m pip install --disable-pip-version-check -r "$dg_repo/supports/fonts/requirements.txt"
  fi
  "$dg_python" "$dg_repo/supports/preparer_police.py" --check
fi
export DG_BROWSER_EXECUTABLE="$(command -v chromium)"
export DG_RENDER_SERVE_LOCAL=1
"$DG_BROWSER_EXECUTABLE" --version
node --version
cd "$dg_repo"
"$dg_python" scripts/build_core.py --check
"$dg_python" scripts/validate_design_governance.py
"$dg_python" scripts/read_route.py DIRECTION/START/TREE > "$dg_setup/start-route.log"
"$dg_python" scripts/read_route.py --mode STANDARD > "$dg_setup/mode-route.log"
printf 'Environnement prêt : %s\n' "$dg_repo"
printf 'Suite complète : source "%s/venv/bin/activate" && DG_BROWSER_EXECUTABLE="%s" DG_RENDER_SERVE_LOCAL=1 python scripts/validate_all.py --require-browser\n' "$dg_setup" "$DG_BROWSER_EXECUTABLE"

