# Maintenance — évolution

Comment une modification du système est recettée, comment une route naît, change ou disparaît.

<!-- origine:ACTION.md -->
## ACTION/MAINTENANCE — recette documentaire

Tout cycle qui modifie ACTION ou un contrat connexe se clôt par une recette avant adoption.

| Contrôle | Preuve attendue |
|---|---|
| Fichiers et renvois | Chaque fichier et route référencés existent et portent la bonne portée. |
| Statuts | Les états, issues, verdicts et statuts de direction appartiennent aux registres canoniques ; aucun plan de maturité concurrent n’est ajouté. |
| Scopes | Chaque obligation précise son mode, contexte ou niveau de proportionnalité. |
| Exemples | Aucun exemple ne propage un statut ou une règle dépréciée. |
| Claims datés | Source, version/date, portée, limite et prochaine preuve sont renseignées dans la trace locale quand le run en dépend. |
| Routage | Chaque signal a une route principale ; les miroirs sont dérivés explicitement. |
| Quotas artificiels | Aucun quota de variantes, retraits, comparaisons, itérations ou appels ne gouverne la qualité. |
| Échappatoire théâtrale | Chaque mécanisme est testé contre sa manière la plus facile d’être satisfait sans intention. |
| Run réel | Une modification substantielle est exercée sur un run réel avant adoption élargie. |
| Ownership | Owner du changement, statut d’adoption et prochaine revue sont nommés. |
| Réserves | Owner, périmètre, date ou version, impact, date de revue, prochaine preuve et condition de sortie sont persistants. |

La recette peut être automatisée pour les fichiers, routes, statuts et renvois. Elle doit rester humaine pour le scope, l’intention, l’échappatoire théâtrale, la proportionnalité et le jugement du risque.

Une contradiction non résolue devient un risque explicite, jamais une règle silencieusement concurrente.

---

<!-- origine:BIBLIOTHEQUE.md -->
## BIBLIOTHEQUE/EVOLUTION — promotion et dépréciation

BIBLIOTHEQUE est stable dans ses responsabilités, mais pilotée dans ses routes. Une route devient durable après plusieurs usages contrastés documentés, lorsque sa responsabilité reste stable, son contrat est complet, sa maintenance est assumée, ses rendus ne s’homogénéisent pas et un gain réel est observé ou mesuré avec baseline, contexte et limite. Elle doit également démontrer qu’elle permet des premiers objets composés, spécifiques et crédibles dans ces contextes, et pas seulement des structures conformes ou jolies dans un screenshot.

**Mesure de lecture.** Pour mesurer ce qu’un run instrumenté lit dans les routes structurelles, les catégories de `DIRECTION` (« Lecture instrumentée et règle de passage ») s’appliquent ; un run ordinaire ne les déclare pas.

### Contrat minimal par périmètre de contribution et statut de route

| Niveau | Minimum attendu | Ne pas exiger par défaut |
|---|---|---|
| Local | Contrat réduit (`BIBLIOTHEQUE/CONTRACTS`) ; héritage ou cas documentaire si la structure suffit, avec source et justification ; `N/A-JUSTIFIED` seulement si réellement non applicable selon ACTION. | Contrat complet de promotion. |
| Route au statut `PILOT` | Contrat réduit, contre-indication, preuve, `DECISION-CHANGE` et périmètre déclaré. | Adoption ou compatibilité générale. |
| Partagé | Contrat complet, consumers, owner, compatibilité, états, mobile, accessibilité, migration et rollback selon le risque. | Promotion silencieuse. |
| Durable | Usages contrastés, baseline, observation ou mesure de gain, maintenance, owner et prochaine revue. | Validation par beauté, fréquence ou screenshot unique. |

`SEED`, `PILOT`, `ADOPTED`, `DEPRECATED` et `ABANDONED` sont des statuts de cycle de vie `CHANGELOG`, jamais des modes, niveaux de structure, états, issues ou verdicts `ACTION`. `OWNER` désigne le responsable de la décision et de sa prochaine preuve ; `NEXT-OWNER` désigne le destinataire de l’action suivante ; l’owner de maintenance d’une route partagée reste distinct et se conserve dans le contrat d’évolution.

### Contrat de gain réel

Le gain réel ne doit pas être déclaré sans :

```text
TASK / DECISION
BASELINE
OBSERVATION OR MEASURE
CONTEXT
LIMIT
OWNER
NEXT-REVIEW
```

Il peut s’agir d’une réduction d’erreur, d’une décision plus directe, d’un temps de décision réduit, d’une diminution de réassemblage ou d’une maintenance plus fiable. La nature du gain et la limite de l’observation sont toujours nommées.

| Critère | Preuve attendue |
|---|---|
| Usages contrastés | Plusieurs usages distincts, documentés dans des runs et non une répétition du même cas. |
| Responsabilité claire | La route réduit une décision identifiable. |
| Contrat complet | Usage, contre-indication, preuve, états, mobile, a11y, owner et revue. |
| Gain réel | Tâche/baseline/observation ou mesure/contexte/limite. |
| Non-homogénéisation | Les rendus restent situés malgré la route commune. |
| Maintenance | Owner et prochaine revue nommés. |

Une route peut être `SEED`, `PILOT`, `ADOPTED`, `DEPRECATED` ou `ABANDONED` dans la gouvernance du `CHANGELOG`. Ces statuts ne sont pas des verdicts d’écran, des issues de run ou des statuts de gate.

### Contribution et retour d’usage

Une proposition de route commence par ce qui existe déjà : vérifier les routes compatibles, les discussions ou les usages documentés, puis expliquer la décision que la nouvelle combinaison permet de mieux prendre. Une contribution n’est promue que si ses usages, sa contre-indication, sa preuve, son owner, son coût de maintenance et sa prochaine revue sont lisibles. Les retours d’équipe, d’usagers ou de production peuvent corriger le contrat ; ils ne remplacent pas l’observation du run ni ne créent un gate supplémentaire.

Le niveau de contribution reste proportionné au risque : un run local peut conserver une trace courte ; une route partagée exige un contrat et une preuve de gain ; une promotion ou une dépréciation relève de `CHANGELOG`. Ne pas transformer la recherche de feedback, la revue communautaire ou le nombre de réutilisations en quota ou en verdict automatique.

**Chaîne de promotion et de gouvernance.** Lorsqu’une route devient partagée ou candidate à une durée canonique, `DIRECTION/START` classe le risque et le blast radius ; `ACTION/RUN-SYSTEM` prépare l’impact, les consumers, l’owner, la preuve, la compatibilité, la migration et le rollback ; `BIBLIOTHEQUE/EVOLUTION` examine les usages contrastés, le gain réel, la non-homogénéisation et la maintenance ; `CHANGELOG` persiste uniquement la décision de cycle de vie autorisée. Une route locale ou exploratoire ne doit pas ouvrir cette chaîne complète sans raison.

Un style reste dans `SAVOIR/STYLE`. Une image, un site, une capture ou un asset reste local à la `RUN_CARD` ou à l’artefact de projet déjà disponible. Une route locale ne devient pas canonique simplement parce qu’elle est jolie ou fréquemment demandée.

Les anciens aliases `REFERENCES/QUERY`, `REFERENCES/SOURCE`, `REFERENCES/ASSET`, `REFERENCES/MEMORY` et `REFERENCES/CORPUS` sont `DEPRECATED` et ne doivent pas apparaître dans un nouveau run. Leur mapping est défini dans la section « Migration des anciens aliases » de `CHANGELOG.md`, pas dans les instructions actives.

<!-- origine:CHANGELOG.md -->
## Cycle de vie des routes

Les statuts de route décrivent la maintenance d’une route candidate ou canonique. Ils ne sont pas des verdicts de design.

| Statut | Sens | Transition autorisée |
|---|---|---|
| `SEED` | Route du seed V1, canonique par construction, sans gain mesuré. | `ADOPTED` (contrat de gain réel satisfait, `BIBLIOTHEQUE/EVOLUTION`) ou `DEPRECATED`. |
| `PILOT` | Route locale ou candidate testée dans un périmètre déclaré. | `ADOPTED` ou `ABANDONED` ; `DEPRECATED` lorsque la route a des consumers. |
| `ADOPTED` | Route canonique dont le contrat, la maintenance et le gain sont acceptés. | `DEPRECATED`. |
| `DEPRECATED` | Route conservée pour migration ou compatibilité ; elle ne doit pas être choisie dans un nouveau run. Aucun nouvel usage ; migration par `ACTION/RUN-SYSTEM` (paquet SYSTÈME). | `ABANDONED` après migration. |
| `ABANDONED` | Route qui n’est plus maintenue ni proposée. | Aucune transition silencieuse. |

Les routes présentes dans le seed de la V1 ont le statut `SEED` : canoniques, sans gain mesuré. `ADOPTED` exige le contrat de gain réel (`BIBLIOTHEQUE/EVOLUTION`). Une route peut être dépréciée depuis tout état publié ou utilisé (`SEED`, `PILOT` avec consumers, `ADOPTED`) ; une dépréciation interdit les nouveaux usages, exige une migration et ne revendique aucun gain. Toute nouvelle route ou promotion doit indiquer son problème, sa décision, son owner, son contrat, sa preuve, sa limite, sa compatibilité et sa prochaine revue.

<!-- origine:CHANGELOG.md -->
## Migration des anciens aliases

Les aliases suivants, issus des brouillons antérieurs à V1, ne sont pas des routes actives. Ils sont reclassés selon ce qu’ils établissent réellement ; l’ancien identifiant peut être conservé dans une trace de compatibilité.

| Alias | Reclassification retenue |
|---|---|
| `REFERENCES/QUERY` | `SAVOIR/TOOLS` pour une recherche ou un claim à vérifier. |
| `REFERENCES/SOURCE` | `SAVOIR/SOURCE` pour une ancre ou une référence observée. |
| `REFERENCES/ASSET` | `DIRECTION/VISUAL_TARGET` pour la route et le rôle de production ; `SAVOIR/SOURCE` pour provenance et limite. |
| `REFERENCES/MEMORY` | `TRACE-LOCATOR` et artefact local ; une mémoire ne devient pas une source normative. |
| `REFERENCES/CORPUS` | Le propriétaire normatif réellement concerné ; `CHANGELOG` seulement si le contenu modifie le package. |

Une reclassification ambiguë reste `NOT-VERIFIED` ou `EXPLORATORY` jusqu’à ce que son propriétaire et sa portée soient établis.
