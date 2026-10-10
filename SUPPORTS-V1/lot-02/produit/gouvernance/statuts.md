# Gouvernance — statuts

Les états, issues et verdicts d’un travail tracé.

<!-- origine:ACTION.md -->
## ACTION/STATUS — états, issues et verdicts

Cette section définit le vocabulaire canonique d’ACTION. Les documents voisins peuvent expliquer ces statuts, mais ne doivent pas créer de synonymes concurrents.

### États du run

| État | Entrer lorsque… | Quitter lorsque… |
|---|---|---|
| `INTAKE` | La demande est reçue, mais périmètre ou inconnue restent ouverts. | Mode, décision dominante, risque et prochaine preuve sont connus. |
| `CLASSIFIED` | La ligne de run et le mode sont nommés. | Le build direct est autorisé ou le contrat/spec requis existe. |
| `SPECCED` | Direction, hiérarchie, contrat ou ancre nécessaires sont disponibles. | Le build peut commencer. |
| `BUILDING` | L’artefact est en production. | Les contrôles applicables peuvent être exécutés. |
| `CHECKING` | Capture, tests, comparaison, gates ou regard pertinent sont en cours. | Verdicts, réserves et prochaine action sont déclarés. |
| `DECIDED` | Le verdict et le compromis sont connus. | La trace est persistée, clôturée, retournée ou escaladée. |
| `CLOSED` | Artefact et trace minimale sont persistés. | Une nouvelle demande ou une reprise `ITER` commence. |

Le verdict global reste `null` avant `CHECKING` ; il est présent à `DECIDED` et `CLOSED`.

`CLOSED` décrit la persistance et la clôture de la trace ; il ne signifie ni réussite, ni preuve complète, ni acceptation globale. Il peut coexister avec une issue `RETURNED`, `EXPLORATORY` ou `BLOCKED`, et avec un verdict global `RETURN`, `EXPLORATORY` ou `SYSTEM-ESCALATION` lorsque la limite, la reprise ou l’escalade est conservée dans la trace.

### Issues et exceptions

| Issue | Signification |
|---|---|
| `BLOCKED` | Une condition nécessaire manque ; l’owner et la prochaine preuve sont nommés. |
| `RETURNED` | Le run revient à une étape antérieure pour corriger un écart ou obtenir une preuve dans le même mode. |
| `RECLASSIFIED` | Le périmètre ou le risque impose un autre mode ; la `RUN_CARD` nomme le mode cible et le run successeur (`closure.reclassification`). |
| `EXPLORATORY` | Un rendu observable existe, mais une preuve requise manque encore. |
| `FAIL-ASSUMED` | Un échec connu est explicitement journalisé et diffusé dans un périmètre limité et temporaire. |
| `ESCALATED` | Une décision, un owner, un droit, une capacité ou un risque dépasse le périmètre du run. |

**Compatibilités.** Une issue non nulle interdit un verdict accepté. `LOST-IN-BUILD` interdit un verdict accepté. `PARTIALLY-HELD` interdit `ACCEPTED` ; `HELD-WITH-ACCEPTED-DIFFERENCE` est le statut d’une différence acceptée. En `DIRECTION`, un verdict accepté exige que chaque ancre soit `transformation_status: transformed`.

**Conséquence décisionnelle** (`DECISION-CHANGE`) : changée · confirmée · abandonnée (la triade) ; sinon, l’une des deux valeurs de repli : `N/A-JUSTIFIED` (aucune conséquence applicable, avec raison) · `NOT-OBSERVED` (conséquence attendue absente ; interdit `ACCEPTED`). À ne pas confondre avec `NOT-VERIFIED`, qui qualifie une preuve manquante ou un axe. Dans une `RUN_CARD`, ces valeurs sont `decision_change.outcome` : `CHANGED`, `CONFIRMED`, `ABANDONED`, `N/A-JUSTIFIED`, `NOT-OBSERVED`.

### Règle de lecture des statuts

ACTION sépare strictement : **état du run**, **issue**, **verdict V/U/A/T**, **statut de direction** et **verdict global**. Il n’existe pas de plan de « maturité » à renseigner par défaut.

> **Plans à ne pas confondre.** `A/B/C` désignent les gates de contrôle ; `V/U/A/T` désignent les axes de questions et de preuve. Ils ne sont ni interchangeables ni combinés en un nouveau statut.

Un statut de direction décrit la fidélité de la direction dans le rendu. Un verdict global décrit la possibilité d’accepter, de retourner, d’explorer ou d’escalader le run dans son périmètre. `HELD` ne produit donc pas automatiquement `ACCEPTED`.

Si une équipe doit suivre un handoff ou une archive, elle le fait dans son outil de projet sans créer un statut concurrent du run.

### Chemin minimal

`DIRECTION` classe le mode et le risque ; `ACTION` conserve la trace, obtient la preuve adaptée et clôt le run. Pour un delta local, garde la ligne de run et le contrôle proportionné. N’ajoute une route, une capture ou un contrat que si cela peut modifier la décision ou lever une incertitude déclarée.

### Principe positif de qualité

La méthode ne vise pas seulement à éviter une sortie générique. Elle prépare et construit une proposition qui peut être belle, ambitieuse, spécifique et cohérente dès le premier rendu. Avant le build, déclare la relation produit à rendre perceptible, le niveau de résolution attendu et le défaut dominant à éviter. Après le build, juge cette intention sur l’artefact réel. Un rendu one-shot peut être clôturé après la première observation si la qualité attendue est atteinte, les risques sont couverts et aucune correction ne promet un gain réel (B1b dans son scope, `ACTION/GATE-B/B1b`) ; il ne peut jamais être clôturé sans observation du rendu.


### Verdicts V/U/A/T

V/U/A/T est une **taxonomie interne de questions et de preuves**. Elle n’est pas une nomenclature normative externe.

| Axe | Couvre | Statuts autorisés |
|---|---|---|
| **V — caractère visuel** | Point de vue, hiérarchie, typographie, composition, matière et retenue. | `PASS`, `PASS-WITH-RESERVATION`, `RETURN`, `N/A-JUSTIFIED`, `NOT-VERIFIED`. |
| **U — compréhension / usage** | JTBD, architecture, parcours, action critique, contenu, états et résultats de tâche. | Même liste. |
| **A — accessibilité / conformité** | Contraste, clavier, focus, cibles, sémantique, information non chromatique, motion et technologies d’assistance selon le périmètre. | Même liste. |
| **T — robustesse technique** | Média, responsive, performance, chargement, erreur, intégration et non-régression. | Même liste. |

Le verdict global est l’un des suivants : `ACCEPTED`, `ACCEPTED-WITH-RESERVATION`, `RETURN`, `RETURN-DIRECTION`, `EXPLORATORY` ou `SYSTEM-ESCALATION`. Il nomme toujours le risque ou conflit le plus important. Aucune moyenne ne compense un axe bloquant.

### Statut de direction

| Statut | Signification |
|---|---|
| `HELD` | La direction se retrouve dans le rendu sans écart majeur non résolu. |
| `HELD-WITH-ACCEPTED-DIFFERENCE` | L’écart est explicite, utile et préserve l’axe touché autrement. |
| `PARTIALLY-HELD` | Une partie de la direction est affaiblie ou non résolue. |
| `LOST-IN-BUILD` | Le rendu ne porte plus la direction retenue. |

`HELD` signifie fidèle à la direction et approprié au contexte ; il ne signifie ni « beau », ni « préféré », ni accepté globalement, ni validé sur U, A ou T.

---
