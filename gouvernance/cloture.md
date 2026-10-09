# Gouvernance — clôture

Le dossier de clôture, le test de sortie et la clôture de direction.

<!-- origine:ACTION.md -->
## ACTION/CLOSE-PACKAGE — paquet de clôture

Livre d’abord l’artefact ou le lien de rendu. Enregistre ensuite le paquet minimal correspondant dans la ligne de run, la `RUN_CARD`, le ticket ou le manifeste. Ce paquet est celui de la trace complète ; en trace légère (`ACTION/HANDOFF`), le run livre une proposition sans paquet de clôture. La forme courte LITE sans RUN_CARD suit `ACTION/HANDOFF` ; si une projection structurée est demandée, utilise la RUN_CARD et son validateur.

| Mode | Paquet minimal | Contrôle machine |
|---|---|---|
| **LITE** | Artefact touché, diff, risque, V/U/A/T touchés, verdict, réserve ou prochaine action, et conséquence décisionnelle (`DECISION-CHANGE`, `N/A-JUSTIFIED` ou `NOT-OBSERVED`). | Invariants communs de la `RUN_CARD` si elle existe (états, axes, verdict, preuve) ; le reste du paquet vit dans la trace. |
| **ITER** | Direction rappelée et retrouvable, diff observable, non-régression, preuve du risque touché, V/U/A/T mis à jour, verdict, risque restant, prochaine action et conséquence décisionnelle (`DECISION-CHANGE`, `N/A-JUSTIFIED` ou `NOT-OBSERVED`). | Invariants communs ; à la clôture, `decision_change`, `trace_locator` et rappel de direction (`direction.thesis`) ; le reste vit dans la trace. |
| **STANDARD** | Rendu ou artefact, hiérarchie, typographie, états pertinents, V/U/A/T, verdict, risque restant, prochaine action et conséquence décisionnelle (`DECISION-CHANGE`, `N/A-JUSTIFIED` ou `NOT-OBSERVED`). | Invariants communs ; à la clôture, `decision_change` et `trace_locator` ; le reste vit dans la trace. |
| **DIRECTION** | Artefact, direction écrite, ancre/spec, capture, trace locale des assets pertinents, écarts, revue créative, creative close, gates A/B/C, V/U/A/T, statut de direction, verdict global, owner, risque restant, prochaine preuve et conséquence décisionnelle (`DECISION-CHANGE`, `N/A-JUSTIFIED` ou `NOT-OBSERVED`). | Invariants DIRECTION et B1b (`closure.b1b`). |
| **SYSTÈME** | Décision de système, impact, consumers, owner, migration/rollback, non-régression, réserves, verdict, entrée CHANGELOG et conséquence décisionnelle (`DECISION-CHANGE`, `N/A-JUSTIFIED` ou `NOT-OBSERVED`). | `closure.system_package`. |

Un verdict vert ne certifie que ce que la liste close contrôle (voir la frontière de validation d’`ACTION/RUN_CARD`).

Un paquet incomplet ne reçoit pas de `PASS` implicite. Utilise `NOT-VERIFIED`, `EXPLORATORY`, `RETURNED`, `FAIL-ASSUMED` ou `ESCALATED` selon le cas.

Pour un run `DIRECTION`, le paquet comprend aussi un **creative close** bref : présence effectivement produite, signature ou élément spécifique, détail ou état révélant le niveau de craft, défaut dominant restant et prochaine action de polish. Dans une `RUN_CARD` structurée, ces éléments sont transportés par `creative_close.presence`, `creative_close.signature`, `creative_close.craft_detail`, `creative_close.dominant_defect` et `creative_close.next_polish_action`. `STOP — [raison]` est une valeur valide de `next_polish_action` : aucune action de polish n’est alors requise. Ce close cite un artefact ou une observation ; il ne devient ni verdict esthétique, ni score, ni preuve d’usage. Une `RUN_CARD` DIRECTION clôturée qui omet ce bloc est incomplète.

### Fraîcheur de la preuve

Chaque verdict est rattaché à l’artefact, à la version, au scope et à l’état réellement observés. Après un changement substantiel qui touche l’axe couvert, ce verdict revient à `NOT-VERIFIED` jusqu’à réinspection, nouvelle preuve ou justification explicite que la modification est hors scope. Les axes non touchés conservent leur dernière preuve valide.

Une preuve reste réutilisable lorsque l’artefact a seulement été déplacé ou relocalisé et que `TRACE-LOCATOR` permet de constater son identité et son absence de changement pertinent. Une capture, un test, une revue ou un avis portant sur une version antérieure ne peut jamais être cité comme preuve de la version livrée sans ce contrôle de fraîcheur. Dans une `RUN_CARD` acceptée, `artifact.version` est égal à `proof.provenance.artifact_version`, et `observed_at` est une date ISO ; un simple déplacement garde la même version.

### Cycle de vie des réserves

Toute réserve qui affecte la livraison conserve :

```text
OWNER
SCOPE
DATE / VERSION
IMPACT
NEXT-PROOF
REVIEW-DATE
EXIT-CONDITION
```

Cette structure s’applique à `PASS-WITH-RESERVATION`, `ACCEPTED-WITH-RESERVATION`, `REMAINING-RISK` et `FAIL-ASSUMED`. Dans une `RUN_CARD`, chaque réserve est un élément de `closure.reservations[]` portant ces sept attributs (`owner`, `scope`, `date_version`, `impact`, `next_proof`, `review_date` en date ISO, `exit_condition`), sans placeholder ; `ACCEPTED-WITH-RESERVATION` en exige au moins une. `FAIL-ASSUMED` utilise `closure.exception` (`ACTION/OVERRIDE`).

### Responsabilité, droits et confidentialité

Chaque run conserve un **owner de décision finale**, même lorsque plusieurs personnes, agents ou prestataires ont contribué à l’artefact, à la direction ou à la preuve. L’owner répond de la décision et de la prochaine action ; il ne peut pas déléguer silencieusement un risque critique au protocole.

Tout asset fourni, curaté, généré ou transformé déclare, lorsque le contexte le requiert, sa provenance, son statut d’autorisation, sa portée d’utilisation, ses restrictions et son fallback. Une provenance tracée ne vaut pas licence d’utilisation. En cas de doute sur un droit, une ressemblance, une marque, une donnée personnelle ou un contenu client, la sortie reste limitée, bloquée ou escaladée selon le risque ; elle ne devient pas acceptable par simple mention dans la trace. Dans une `RUN_CARD` `DIRECTION`, `artifact.rights_status` déclare `not_applicable`, `cleared`, `unknown` ou `restricted` ; en cas de doute (`unknown`), pas d’`ACCEPTED`.

Les données sensibles, captures internes, informations personnelles et artefacts confidentiels ne sont utilisés que dans le périmètre autorisé. Si un outil, un agent ou un export ne permet pas de garantir ce périmètre, déclare la limitation et n’envoie pas la donnée vers ce canal. `NOT-VERIFIED` décrit une preuve manquante ; il ne constitue pas une autorisation de partager un contenu sensible.

### Condition d’arrêt du polish

Le polish s’arrête lorsque le défaut dominant identifié est corrigé ou accepté par l’owner, que les risques applicables sont couverts ou explicitement réservés, et qu’une itération supplémentaire ne promet pas de modifier une relation visible, une tâche, une preuve ou une contrainte importante. Si le défaut persiste mais qu’une nouvelle action est disproportionnée, conserve la réserve avec owner, impact, prochaine preuve et condition de sortie. Ne poursuis pas le polish pour remplir un quota, ajouter des effets ou atteindre une perfection abstraite. Quand le polish s’arrête, `next_polish_action` vaut `STOP — [raison]`.

---

<!-- origine:ACTION.md -->
## ACTION/CLOSE-EXIT-CHECK — test de sortie canonique

Avant de clôturer un run, vérifie :

1. Le mode est-il celui qui protège le risque dominant ?
2. L’artefact et la décision sont-ils retrouvables ?
3. La preuve adaptée à la question a-t-elle été obtenue, ou son absence est-elle déclarée ?
4. Le scope et la limite de couverture sont-ils connus lorsque la preuve le requiert ?
5. Les V/U/A/T touchés et le risque restant sont-ils renseignés ?
6. Le statut de direction, le verdict global, l’owner et la prochaine action sont-ils persistants ?
7. La réserve, si elle existe, possède-t-elle owner, périmètre, date ou version, impact, date de revue, prochaine preuve et condition de sortie ?
8. Quelle décision concrète a changé grâce à la procédure ? Si la réponse est « aucune », la procédure est-elle réellement justifiée ?
9. Quel niveau de qualité était visé au premier rendu, et quel élément observable démontre qu’il était composé, spécifique et suffisamment résolu pour le mode ?
10. La dernière modification a-t-elle changé une relation perceptible, produit, preuve, accessibilité ou robustesse, ou seulement la justification ?

Si une réponse reste inconnue, utilise le statut approprié. Ne transforme jamais une lacune de preuve en `PASS` implicite. Une trace complète ne compense pas un artefact faible ; un premier rendu très fort ne compense pas une preuve requise absente.

### Mesure expérimentale de la méthode

Au niveau d’un pilote ou d’une série de runs, et non comme score individuel, observe le temps jusqu’au premier rendu jugeable, la part des premiers rendus nécessitant une correction structurelle, la part des corrections qui changent réellement l’artefact, les preuves encore `NOT-VERIFIED` à la clôture, les défauts récurrents par mode et la perception de qualité par plusieurs regards situés. Ces mesures servent à améliorer V1 ; elles ne créent ni verdict esthétique, ni quota d’itérations, ni obligation de variante.

<!-- origine:DIRECTION.md -->
## Clôture de direction

`ACTION/CLOSE-EXIT-CHECK` est l’unique test de sortie canonique. Avant de l’appeler, `DIRECTION` vérifie que la thèse, la conséquence observable, l’ancre utile, l’opération visuelle dominante, la preuve attendue et, lorsque nécessaire, la route d’asset restent reliées à des observations du rendu ; une non-applicabilité réelle est `N/A-JUSTIFIED`, et une preuve nécessaire non vérifiable reste `NOT-VERIFIED` ou l’issue ACTION appropriée. Pour une `RUN_CARD DIRECTION` décidée ou clôturée, ACTION conserve séparément `closure.state`, `closure.issue`, `closure.direction_status`, `closure.verdict`, `closure.limitations` et `creative_close` selon `ACTION/CLOSE-PACKAGE`.

Les gates, verdicts, exceptions, preuves exécutables et statuts restent canoniques dans `ACTION.md`. Les principes de craft, styles, contextes et intégrité restent canoniques dans `SAVOIR.md`. Les structures restent canoniques dans `BIBLIOTHEQUE.md`. Les migrations, pilotes et décisions partagées restent canoniques dans `CHANGELOG.md`.

`DIRECTION` ne ferme pas un run à la place d’`ACTION`. Il vérifie seulement que la direction déclarée est encore identifiable, que sa preuve attendue est nommée et que les limites de preuve ne sont pas dissimulées.

### Lecture instrumentée et règle de passage

Pour éviter de présenter une hypothèse de proportion comme un gain démontré, dans un run instrumenté ou audité, distingue dans la trace :

- `STARTUP-NOMINAL` — modules recommandés avant la première décision ;
- `CONDITIONAL-READ` — modules ouverts parce qu’une condition du brief ou du risque peut changer la décision ;
- `AUDIT-READ` — fichiers ouverts pour contrôler le corpus ou le protocole, sans être nécessaires au run ;
- `ACTUAL-READ` — fichiers effectivement lus dans un run instrumenté.

La chaîne de lecture est définie une seule fois : « Chaîne de lecture interne », dans la constitution du document. Dans un run instrumenté ou audité, déclare dans la trace la catégorie de lecture applicable (en trace légère, cette déclaration n’est pas demandée) ; ne compte jamais un `AUDIT-READ` comme une lecture nécessaire au run. La règle de lecture proportionnelle décrit un chemin nominal : elle ne constitue pas une mesure de temps, de volume, de charge cognitive ou de qualité. Toute affirmation de réduction doit préciser la méthode, le périmètre et la limite.

Le passage entre propriétaires reste celui de la règle de passage de `DIRECTION/CHARGE`. Pour une route partagée ou candidate à la promotion, l’ordre de décision est `DIRECTION/START` → `ACTION/RUN-SYSTEM` → `BIBLIOTHEQUE/EVOLUTION` si la route est structurelle, sinon la source normative propriétaire (`SAVOIR` pour une heuristique de jugement, `ACTION` pour un gate ou un champ de `RUN_CARD`) → `CHANGELOG`. Cet ordre ne constitue ni une promotion, ni un nouveau gate, ni une nouvelle source d’autorité.
