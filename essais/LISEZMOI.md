# Essais de la manche 3 : reproduire les mesures

Hors paquet (voir `../SUIVI.md`). Cette branche est orpheline : pour exécuter `check_render.py`, il faut le paquet DG, sur une autre branche du dépôt. Tout a été exécuté le 2026-10-14 dans un conteneur Linux, en root.

## Contenu

| Chemin | Rôle |
|---|---|
| `pages/flawed/`, `pages/clean/` | deux pages d'atelier de vélos : défauts volontaires / corrigée (les PNG viennent de `make_pngs.py`) |
| `resultats/ts_inspect_*.json` | rapports de `inspect.mjs` (Taste Skill) |
| `resultats/dg_check_render_*.json` | sorties de `check_render.py --json` (DG) |
| `resultats/ts_draw_*.txt` | sortie de `draw.mjs` pour le brief, seed 42 (3 options, puis fiche `one-motif`) |

Les JSON contiennent des chemins absolus du conteneur d'origine.

## Prérequis

- Node 22+ et un Chromium ; Python 3.10+ et `playwright==1.56.0` (version de la CI de DG) avec son Chromium.
- Taste Skill : copie de `github.com/Leonxlnx/taste-skill` (MIT), dossier `skills/taste-skill/`. Avant exécution, `inspect.mjs`, `lint.mjs`, `lib/rules.mjs` et `lib/cdp.mjs` ont été lus en entier, et `draw.mjs` et `lib/probe.mjs` balayés par recherche de motifs réseau ou d'exécution (aucun trouvé ; `draw.mjs` écrit un historique dans `~/.taste-skill/` sauf si `TASTE_SKILL_HISTORY` est défini). `assets.mjs` (recherche d'images en ligne) n'a pas été exécuté ni lu en entier.

## Commandes

```bash
# 1. Régénérer les images (facultatif si les PNG sont présents)
python3 -I make_pngs.py "$(pwd)"

# 2. Taste Skill. En root, Chromium exige --no-sandbox : enveloppe de lancement.
printf '#!/bin/sh\nexec /chemin/vers/chrome --no-sandbox "$@"\n' > chrome-nosandbox.sh && chmod +x chrome-nosandbox.sh
export CHROME_PATH="$(pwd)/chrome-nosandbox.sh"
export TASTE_SKILL_HISTORY=/tmp/ts_history.json   # évite d'écrire dans ~/.taste-skill
( cd pages/flawed && node <taste-skill>/scripts/lint.mjs index.html )
( cd pages/flawed && node <taste-skill>/scripts/inspect.mjs index.html --out /tmp/ts_flawed )
( cd pages/clean  && node <taste-skill>/scripts/inspect.mjs index.html --out /tmp/ts_clean )

# 3. Design Governance (depuis la racine du dépôt DG ; <notes> = chemin de cette branche extraite)
python3 scripts/check_render.py <notes>/essais/pages/flawed/index.html --json /tmp/dg_flawed.json
python3 scripts/check_render.py <notes>/essais/pages/clean/index.html  --json /tmp/dg_clean.json

# 4. Test F1 (mouvement réduit) : même page, animation d'entrée de 0,8 s puis de 8 s
sed 's/up .8s ease both/up 8s ease both/' pages/flawed/index.html > /tmp/flawed_8s.html
python3 scripts/check_render.py /tmp/flawed_8s.html     # -> PASS-WITH-RESERVATION (avec 0,8 s : PASS)

# 5. Tirage Taste Skill
node <taste-skill>/scripts/draw.mjs --sector other --brief "Atelier de réparation de vélos à Gand" \
  --sections intro,list,gallery,contact,footer --seed 42 --out /tmp/ts_draw --options 3
node <taste-skill>/scripts/draw.mjs --sector other --brief "Atelier de réparation de vélos à Gand" \
  --sections intro,list,gallery,contact,footer --seed 42 --out /tmp/ts_draw --direction one-motif
```

Pour le test F1, la page copiée a besoin de `photo1.png` à côté d'elle.

## Limites

Une seule paire de pages, un seul brief, un seul tirage (seed 42). Ces mesures montrent **ce que chaque contrôleur détecte**, pas la qualité des rendus produits par les deux systèmes. Elles ne remplacent pas le protocole A/B (N4 dans `SUIVI.md`).
