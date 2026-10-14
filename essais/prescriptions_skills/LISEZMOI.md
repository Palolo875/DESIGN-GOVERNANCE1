# Essais de la manche 5 : prescriptions des skills de Taste Skill autres que la v2

Hors paquet (voir `../../SUIVI.md`, section 6). Trois pages d'atelier de vélos (même brief que la manche 3), écrites **au pied de la lettre**
des prescriptions de `soft-skill.md`, `brutalist-skill.md` et `stitch-skill.md` (dépôt `github.com/Leonxlnx/taste-skill`, MIT, dossier `skills/taste-skill/other/`),
puis passées dans les contrôleurs de la v2 de Taste Skill (`lint.mjs`, `inspect.mjs`) et dans `check_render.py` de Design Governance.

C'est **ma mise en œuvre** de ces prescriptions : un autre rédacteur aurait écrit une autre page. Chaque page porte en tête de son `<style>` les sections de la skill qu'elle applique.
Les couleurs prescrites par leur valeur hexadécimale (brutalist : `#E61919`, `#FF2A2A`, `#F4F4F0`, `#EAE8E3`, `#0A0A0A` ; stitch : `#71717A`, `#F9FAFB`) sont indépendantes de ma mise en œuvre.

| Chemin | Contenu |
|---|---|
| `pages/<skill>/index.html` + `photo1.png` | la page de test (le PNG est un dégradé généré, sans signification) |
| `resultats/ts_lint_<skill>.txt`, `ts_inspect_<skill>.json` | sorties de TS (le JSON porte des chemins absolus du conteneur d'origine) |
| `resultats/dg_check_render_<skill>.json` | sortie de `check_render.py --json` (version `ccr-38b0a56f-t8xdo8`, commit 471bedb) |
| `resultats/dg_avant_F1_<skill>.txt` | ligne « Mouvement réduit » de `check_render.py` **avant** le correctif F1 (révision 897ed35) |

Commandes : celles de `../LISEZMOI.md` (même enveloppe `--no-sandbox` pour Chromium en root), en remplaçant `pages/flawed` par `pages/<skill>`.

Limites : une page par skill, un seul brief ; les pages sont courtes (1 à 3 écrans, 1 image), ce qui fait échouer `few-pictures` et `still-page` à TS indépendamment des skills (à soustraire, voir SUIVI 6.3).
