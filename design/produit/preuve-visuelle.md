# Produit — preuve visuelle

Rendre la direction vérifiable sur le rendu.

<!-- origine:ACTION.md -->
## ACTION/VISUAL_PROOF — rendre la direction vérifiable

Visual Proof relie `DIRECTION/VISUAL_TARGET`, l’ancre, la spec et le rendu observé. Il s’exécute dès qu’une première scène significative est disponible.

Avant la preuve, déclare le périmètre : viewport, états, scènes, contenu, devices et axes couverts. Les éléments hors couverture sont mentionnés dans `COVERAGE-LIMIT` ou `NEXT-PROOF`.

| Preuve | Vérifie | Si absente ou inadaptée |
|---|---|---|
| Capture desktop entière | Support, silhouette, masses, vide, foyer, opération dominante et rapport scène/preuve. | V `NOT-VERIFIED` sur la surface. |
| Capture mobile entière | Recomposition, voisinage, priorité et action. | U/T `NOT-VERIFIED` si mobile est dans le périmètre ou le risque. |
| Vue de détail | Type, matière, cadrage, bordure, état ou contenu extrême lorsque pertinent. | `N/A-JUSTIFIED` seulement si aucun détail ne porte une décision. |
| Vue de masses | Foyer, poids relatifs, vides et foyer parasite sur une surface à risque hiérarchique. | `N/A-JUSTIFIED` si la hiérarchie n’est pas un risque du run. |
| État significatif | Loading, empty, error, focus, contenu long ou état dominant. | U/A/T `NOT-VERIFIED` sur l’état absent. |
| Comparaison d’écarts | Spec/ancre face au build sur les axes touchés. | `EXPLORATORY` ou `RETURN-DIRECTION`. |

Pour un rendu HTML, `python3 scripts/check_render.py page.html --captures DOSSIER` produit les captures entières, une par largeur (390, 768 et 1440 px par défaut), à l’état observé (`--click` pour un autre état). Chaque version va dans son propre dossier : la recette n’écrase jamais une capture existante, ce qui garde la paire avant/après de B1b. Vues de détail et de masses restent à produire autrement. Pour une non-régression, enregistrez la mesure de la version d’avant avec `--json`, puis mesurez la nouvelle avec `--baseline` suivi de ce fichier, aux mêmes largeurs, état et réglages : chaque contrôle est dit inchangé, amélioré, dégradé, introduit ou disparu, sans changer les statuts ; un défaut préexistant reste un défaut. Pour un contenu calculé ou un état animé, la preuve se prend à l’état qui compte : `--click` puis `--wait-after-ms MS` amènent la page à cet état, `--assert EXPRESSION` (répétable) recoupe un texte dérivé avec ses valeurs et échoue si l’expression JavaScript n’est pas vraie, `--in-frame SÉLECTEUR@CADRE` (répétable) échoue si un élément de l’état clé a son centre hors du cadre (la fenêtre si `@CADRE` est omis). Le contrôle « Chevauchement et troncature de texte » relève, sur les rectangles de lignes ramenés à l’interligne et hors calques fixes ou collants, les textes qui se recouvrent (`RETURN`), ceux qui sont tronqués, sur une ligne ou coupés à quelques lignes (`line-clamp`), et le texte décoratif superposé à un autre, masqué aux lecteurs d’écran, presque transparent ou en simple contour, comme un filigrane (réserve, à juger). La mesure se prend à l’état laissé par les clics, avant les captures. Les réglages de preuve d’état n’entrent dans la comparaison `--baseline` que s’ils sont employés.

Pour vérifier que le caractère déclaré est perçu (densité, matière dominante, polices réellement rendues), la recette de caractère, à l’essai, est décrite dans `ACTION/RECETTE-CARACTERE`.

<!-- concept:HON-07 -->
Une capture prouve le rendu, pas l’indépendance du jugement, l’accessibilité complète ou la réussite d’une tâche. Un regard humain ou externe prouve un avis situé, pas une mesure technique. Un asset généré est une ancre possible, jamais une preuve de rendu.

---

<!-- origine:ACTION.md -->
## ACTION/RECETTE-CARACTERE — recette de caractère, à l’essai

Recette `AUTOMATED` facultative qui confronte le caractère déclaré d’un run à son rendu HTML : `python3 scripts/check_caractere.py page.html declaration.json`. Elle sert la boucle d’édition lorsque la qualité perceptuelle fait partie de la décision. Elle ne juge ni la qualité d’une direction, ni le goût, ni l’usage, et ne remplace ni la revue de `SAVOIR/CRAFT/CFT-00`, ni `ACTION/GATE-A`, ni `ACTION/RECETTE-RENDU`.

**Déclaration.** Un fichier JSON tiré de `DIRECTION/VISUAL_TARGET` et des axes de `BIBLIOTHEQUE/TENSION`, écrit avant la construction et rangé à côté de l’artefact. Un champ absent n’est pas contrôlé. La trace la cite : en trace légère, sur la ligne « modal, trame et parti », sans ligne supplémentaire.

| Champ | Valeurs | Ce qui est confronté |
|---|---|---|
| `fonts` | familles déclarées | Polices réellement utilisées par le navigateur, glyphe par glyphe |
| `density` | `respiration`, `compression` | Part de vide du premier écran |
| `material` | `plan`, `image`, `typographie` | Part du premier écran occupée par les aplats, les images et le texte |
| `focus` | `unique`, `distribué` | Saillance captée par l’objet de preuve, ou concentration du regard |
| `proof` | sélecteur CSS | Objet de preuve, pour `focus` |
| `intensity` | `retenue`, `intensité` | Colorfulness du premier écran |
| `intended_voids` | `true`, `false` | Bandes vides entre deux contenus |
| `widths`, `states` | largeurs en px ; suffixes d’URL | Vues mesurées (par défaut 390 et 1440 px) |

**Sorties.** Un `SIGNAL` (polices, densité, matière) attend une réponse dans la trace : l’écart est corrigé dans l’artefact, ou gardé avec sa raison lorsque la déclaration était fausse ou l’écart voulu ; la trace dit lequel, sur la ligne du défaut dominant restant en trace légère. Un `RELEVÉ` (foyer, intensité, vide) informe sans rien exiger. Aucune sortie ne vaut `PASS`.

**Limites.** Statut `PILOT` : bornes provisoires `[À CALIBRER]`, réglées sur peu de pages. Elles restent figées entre deux recalibrations : un run ne les retouche pas ; une recalibration se fait par lot, sur au moins cinq runs qui n’ont pas servi à les régler, et la fiche de version en donne la date. La saillance est un modèle classique (résidu spectral), non entraîné sur des interfaces. Le caractère générique d’une page n’est pas mesuré. Une graisse synthétisée par le navigateur et une coupure de titre ne sont pas détectées. Sans Playwright, numpy et Pillow, la recette rend `NOT-VERIFIED`. Ses règles sont testées par `scripts/test_check_caractere.py`.

---
