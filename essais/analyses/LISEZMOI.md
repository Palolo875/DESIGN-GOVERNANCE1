# Analyses de la manche 7 : données de Taste Skill (TS) et texte de Design Governance (DG)

Hors paquet (voir `../../COMPARAISON-COMPLEMENT.md`). **Aucun skill n'est lancé sur un brief** : ces scripts lisent et comptent.
TS = copie de `github.com/Leonxlnx/taste-skill` (MIT), dossier `skills/taste-skill/` (celui qui contient `SKILL.md`). DG = racine du paquet (branche `ccr-38b0a56f-t8xdo8`, commit `27db80d`).

| Script | Ce qu'il fait | Sortie |
|---|---|---|
| `palettes.mjs <TS>` | contraste de chaque palette (encre, texte atténué, texte sur accent, champs, accent sur sol), familles interdites par `colourFamily` de TS | `resultats/palettes.txt` |
| `analyses.py <TS> <DG>` | A2 polices contre les listes du `lint` ; A3 motifs bannis dans la prose des 240 entrées ; A4 couverture ; A5 stillness et `allow` ; A6 valeurs chiffrées ; A7 lexique | `resultats/analyses.txt` |
| `adjustments.mjs <TS>` | extrait la fonction `adjustments()` de `draw.mjs` et l'applique à chaque section et chaque héros (`draw.mjs` n'est pas lancé) | `resultats/adjustments.txt` |

```bash
node essais/analyses/palettes.mjs <TS>
python3 -I essais/analyses/analyses.py <TS> <DG>
node essais/analyses/adjustments.mjs <TS>
```

Prérequis : Node 18+ (`palettes.mjs` importe `scripts/lib/rules.mjs` de TS), Python 3.10+. `analyses.py` lit `design/**/*.md` de DG ; la numérotation « A » suit `COMPARAISON-COMPLEMENT.md`.

Limites : comptages par expressions régulières (approximations) ; contrastes calculés par la formule WCAG sur les valeurs hexadécimales, contre la couleur de sol de la palette ; `adjustments()` sur-signale les couleurs nommées.
