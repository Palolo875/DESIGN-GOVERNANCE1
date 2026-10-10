# Produit — premier rendu

La qualité attendue dès le premier rendu, et l’interface réelle construite avec la tâche.

<!-- origine:ACTION.md -->
## ACTION/FIRST-RENDER — qualité initiale attendue

Le premier rendu n’est pas une simple ébauche destinée à être rendue présentable plus tard. Lorsqu’un run produit une surface, un composant, un flow ou une scène, le premier artefact doit déjà être **composé, crédible, spécifique au produit et suffisamment résolu pour être jugé comme un objet réel**, dans la proportion du mode et du risque. Le slop est un risque possible, mais la cible positive est la qualité : présence, hiérarchie, typographie, contenu, états, matière ou retenue, relation à la preuve et finition pertinente.

| Mode | Qualité initiale attendue au premier rendu |
|---|---|
| `LITE` | Le delta est propre, lisible, cohérent avec le système et ne dégrade pas le rendu existant. |
| `ITER` | Le delta est visible, intentionnel, fidèle à la direction retrouvable et inspectable dans les états touchés. |
| `STANDARD` | La vue ou le flow est déjà composé : contenu crédible, hiérarchie, typographie, états pertinents, responsive applicable et finition suffisante pour juger la proposition. |
| `DIRECTION` | La première scène porte déjà la présence, le point de vue, la composition, la typographie, la matière ou la retenue, l’objet de preuve et l’intégration d’asset nécessaires à la décision. |
| `SYSTÈME` | Le composant ou token est montré dans ses usages réels, avec baseline, états, consommateurs et risque de régression identifiables. |

Un rendu peut rester `EXPLORATORY` lorsqu’une preuve manque, mais ce statut ne justifie pas un artefact volontairement creux lorsque les capacités nécessaires sont disponibles ; sinon, plafond déclaré avant le build (`FABRICATION`). La qualité initiale est une cible de construction, non un score et non un verdict esthétique.

### ACTION/UI-UX-REALITY — construire l’interface et la tâche ensemble

Pour une surface UI/UX nouvelle ou substantiellement modifiée, le premier objet doit rendre observables, dans la proportion du mode et du risque : hiérarchie de contenu, premier geste, feedback, états `loading`, `empty`, `error`, `unavailable`, `disabled` et succès partiel lorsque pertinents, contenu long ou multilingue, responsive recomposé, focus et récupération. Une capture de l’état nominal ne suffit pas lorsque l’état, la tâche ou la récupération fait partie de la décision. L’état qui ouvre la page est rempli, avec des valeurs marquées comme exemple si besoin ; l’état vide se conçoit pour l’usage réel, il n’accueille pas le visiteur.

Le contrat de production relie :

```text
CONTENT-MODEL: données et hiérarchie réellement portées
PRIMARY-TASK: tâche et résultat attendu
FIRST-GESTURE: action initiale et feedback associé
CRITICAL-STATES: états, erreurs, permissions et récupération applicables
RESPONSIVE-RELATION: ce qui est préservé, recomposé ou remplacé selon le viewport
ACCESSIBILITY-BASIS: sémantique, nom, focus, clavier, contraste et alternative selon le risque
ROBUSTNESS-BASIS: contenu extrême, chargement, compatibilité, performance ou non-régression selon le risque
EXPECTED-SCOPE: scope attendu — surface, état, viewport, données, population ou runtime à observer (avant build)
OBSERVED-SCOPE: scope observé — surface, état, viewport, données, population ou runtime réellement observé (après observation)
```

La couverture de chaque exigence emploie `OBSERVED`, `NOT-VERIFIED` ou `N/A-JUSTIFIED` avec sa raison. `OBSERVED` n’est pas `PASS` : une observation peut être négative, et son résultat vit dans `EVALUATION_CASE` ou dans la trace. `NOT-OBSERVED` n’y est pas employé : il qualifie une conséquence de décision (`ACTION/STATUS`).

Ces lignes décrivent les décisions de construction et la couverture attendue ; elles ne créent pas un nouveau gate ni un formulaire universel. `ACTION` garde les preuves, les limites et le verdict ; `SAVOIR/CONTEXT` et `SAVOIR/TECH` sont chargés seulement lorsque leurs questions peuvent changer la décision, la preuve ou la limite. Lorsque la capacité nécessaire manque, déclare `NOT-VERIFIED` ou l’issue appropriée au lieu de réduire silencieusement l’ambition de protection.

**Source de classification.** Le mode est classé par `DIRECTION/START`. ACTION ne reclassifie pas silencieusement une tâche parce qu’une capacité, un outil ou une preuve manque. Il déclare alors la limite, le statut et la prochaine preuve.

---
