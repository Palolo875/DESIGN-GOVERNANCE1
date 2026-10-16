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

Pour un rendu HTML, `python3 scripts/check_render.py page.html --captures DOSSIER` produit les captures entières, une par largeur (390, 768 et 1440 px par défaut), à l’état observé (`--click` pour un autre état). Chaque version va dans son propre dossier : la recette n’écrase jamais une capture existante, ce qui garde la paire avant/après de B1b. Vues de détail et de masses restent à produire autrement. Pour une non-régression, enregistrez la mesure de la version d’avant avec `--json`, puis mesurez la nouvelle avec `--baseline` suivi de ce fichier, aux mêmes largeurs, état et réglages : chaque contrôle est dit inchangé, amélioré, dégradé, introduit ou disparu, sans changer les statuts ; un défaut préexistant reste un défaut. Pour un contenu calculé ou un état animé, la preuve se prend à l’état qui compte : `--click` puis `--wait-after-ms MS` amènent la page à cet état, `--assert EXPRESSION` (répétable) recoupe un texte dérivé avec ses valeurs et échoue si l’expression JavaScript n’est pas vraie, `--in-frame SÉLECTEUR@CADRE` (répétable) échoue si un élément de l’état clé a son centre hors du cadre (la fenêtre si `@CADRE` est omis). Le contrôle « Chevauchement et troncature de texte » relève, sur les rectangles de lignes ramenés à l’interligne et hors calques fixes ou collants, les textes qui se recouvrent (`RETURN`) et ceux qui sont tronqués (réserve, à juger).

<!-- concept:HON-07 -->
Une capture prouve le rendu, pas l’indépendance du jugement, l’accessibilité complète ou la réussite d’une tâche. Un regard humain ou externe prouve un avis situé, pas une mesure technique. Un asset généré est une ancre possible, jamais une preuve de rendu.

---
