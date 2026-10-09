# Gouvernance — conditions et fiche de travail

Ce qu’il faut établir avant d’agir, et la fiche qui garde la trace d’un travail.

<!-- origine:ACTION.md -->
## ACTION/PRECONDITION — mode, capacité et preuve

Le mode est classé dans `DIRECTION/START`. Le type de tâche et son blast radius déterminent le mode ; les capacités disponibles déterminent la voie de preuve, le statut de vérification et la possibilité de livrer. Une capacité absente ne rétrograde jamais silencieusement une tâche `DIRECTION`.

| Mode | Contrat ACTION minimal |
|---|---|
| **LITE** | Intention, artefact touché, gates A applicables, `Gate B` du risque dominant, axes `V/U/A/T` concernés et réserve ou prochaine action. |
| **ITER** | Direction retrouvable, diff, non-régression du périmètre, Gate A applicable, Gate B du risque touché et Gate C seulement si le craft change. |
| **STANDARD** | JTBD, arbitrage, hiérarchie, typographie, états pertinents, Gates A et B ciblés ; ancre ou asset seulement si le risque le requiert. |
| **DIRECTION** | Alternative située lorsque nécessaire, ancre utile, cible, build, capture, comparaison, gates A/B/C, trace locale des assets pertinents, statut de direction et V/U/A/T. |
| **SYSTÈME** | Impact, consumers, décision, owner, migration, rollback, non-régression et entrée CHANGELOG (dans une `RUN_CARD` acceptée : `closure.system_package`). |

<!-- concept:HON-06 -->
Un gate non applicable est `N/A-JUSTIFIED`. Un gate nécessaire mais non vérifiable est `NOT-VERIFIED`, jamais `PASS` par défaut.

### Contrat de décision et de preuve

Au lancement, la `RUN_CARD` contient :

```text
DECISION-INTENT — décision que la procédure doit permettre de trancher.
```

Après une observation qui modifie, confirme ou abandonne effectivement une décision, la trace contient :

```text
DECISION-CHANGE — décision effectivement changée, confirmée ou abandonnée grâce au run.
```

Si aucune décision ne change, la clôture utilise `N/A-JUSTIFIED` lorsque cela est justifié, avec la raison et la prochaine preuve éventuelle ; `NOT-OBSERVED` lorsqu’une conséquence attendue n’a pas été observée. Ne déclare jamais un changement avant qu’une observation ne l’ait rendu réel. Dans une `RUN_CARD`, `DECISION-CHANGE` devient `decision_change`, dont `outcome` porte la triade et les deux valeurs de repli d’`ACTION/STATUS` ; `N/A-JUSTIFIED` y exige `reason`. `DECISION-CHANGE` et le creative close sont des champs « après observation » : ils restent absents tant que le run n’a pas atteint `CHECKING`.

### Trace post-build de `DIRECTION/EXTERNAL-START`

Lorsque `DIRECTION/EXTERNAL-START` a été activée, conserve après le premier artefact ou la première capture, dans la trace existante et sans créer de nouveau statut :

```text
DECISION-CHANGE — ce que le démarrage a effectivement changé, confirmé ou abandonné.
OMISSION-AVOIDED — omission concrète évitée, ou NOT-OBSERVED.
REMAINING-LIMIT — limite persistante après le premier artefact.
```

Ces trois lignes ne sont pas un gate supplémentaire. Elles vérifient que la vue de démarrage a changé une décision, rendu une omission visible ou exposé une limite. Si aucune conséquence n’est obtenue, utilise `N/A-JUSTIFIED` ou `NOT-OBSERVED` dans la trace existante ; ne transforme pas le préflight en rituel.

### Raccord de trace pour la section `DESIGN-ATLAS` de `SAVOIR.md`

Lorsque la section `DESIGN-ATLAS` de `SAVOIR.md` est chargée, ses champs de présélection restent des éléments locaux de décision et ne remplacent pas la `RUN_CARD`. Elle n’est appelée qu’après classification, décision et risque ; si aucune famille ne peut modifier la prochaine décision, elle n’est pas chargée. Avant le build, `DECISION-MODIFIED`, `WHEN-USEFUL`, `COUNTERINDICATION`, `MEDIUM-SCOPE` et `PROOF-LIMIT` décrivent une hypothèse de sélection, non une observation indépendante. Une rationale, une cible visuelle, une ancre, une référence ou la présence d’un asset ou d’un composant ne prouve ni l’implémentation, ni l’utilité, ni la qualité, ni l’accessibilité, ni l’efficacité.

Après observation, la sortie canonique est `DECISION-CHANGE` si la décision a effectivement changé, été confirmée ou abandonnée ; sinon, utilise `N/A-JUSTIFIED` lorsqu’aucune conséquence n’était applicable ou `NOT-OBSERVED` lorsqu’une conséquence attendue n’a pas été observée. Seul un résultat observé dans le scope déclaré peut alimenter `DECISION-CHANGE` et un verdict. Le polish visuel peut soutenir une revue perceptuelle, mais ne devient pas une preuve de tâche, d’usage, de performance ou d’accessibilité exécutée. `WHY-NOW` et `REUSE-CHALLENGE` sont ajoutés lorsque la famille ou le profil est repris d’un run précédent. Aucun de ces éléments ne crée un nouveau mode, gate, statut, score ou formulaire.

Pour réduire le slop procédural, préfère une proposition principale et une alternative située seulement lorsqu’elle peut changer une décision. Produis ou conserve un détail, un asset, une variante ou une rationale seulement si sa conséquence sur l’artefact, la preuve, la limite ou la prochaine action est identifiable.

---

<!-- origine:ACTION.md -->
## ACTION/RUN_CARD — carte de run minimale

La `RUN_CARD` est un format local extensible, non un document canonique séparé. Elle peut vivre dans un ticket, un manifeste, un espace de travail ou un fichier local.

Quel que soit son support, elle conserve au minimum :

| Champ | Contenu |
|---|---|
| `ID` | Identifiant du run. |
| `OWNER` | Responsable de la décision, de la reprise ou de l’escalade. |
| `DATE / VERSION` | Date, version et contexte de preuve. |
| `MODE` | Route de run classée par `DIRECTION/START`. |
| `STATE` | `INTAKE`, `CLASSIFIED`, `SPECCED`, `BUILDING`, `CHECKING`, `DECIDED` ou `CLOSED`. |
| `ISSUE` | `BLOCKED`, `RETURNED`, `RECLASSIFIED`, `EXPLORATORY`, `FAIL-ASSUMED` ou `ESCALATED`, si applicable ; `null` si aucune issue n’est déclarée. |
| `VERDICT` | Verdict global uniquement dans la projection `RUN_CARD` : `ACCEPTED`, `ACCEPTED-WITH-RESERVATION`, `RETURN`, `RETURN-DIRECTION`, `EXPLORATORY` ou `SYSTEM-ESCALATION`. Les verdicts V/U/A/T restent dans leur registre d’axes ; une carte qui accepte les sérialise dans `closure.axes`, jamais dans ce champ. |
| `DIRECTION-STATUS` | Statut de fidélité de la direction : `HELD`, `HELD-WITH-ACCEPTED-DIFFERENCE`, `PARTIALLY-HELD` ou `LOST-IN-BUILD`, si applicable. |
| `DECISION` | Décision dominante à prendre ou à vérifier. |
| `DECISION-INTENT` | Décision que la procédure doit permettre de trancher. |
| `DECISION-CHANGE` | Décision effectivement changée, confirmée ou abandonnée ; sinon l’une des valeurs de repli d’`ACTION/STATUS` : `N/A-JUSTIFIED` si aucune conséquence n’était applicable (avec la raison), `NOT-OBSERVED` si une conséquence attendue n’a pas été observée (interdit `ACCEPTED`). |
| `RISK` | Risque principal et impact potentiel ; projection : `risk.level` et `risk.statement`. |
| `ARTIFACT` | Lien vers rendu, code, capture, test ou diff. |
| `TRACE-LOCATOR` | URL, chemin, ticket, commit ou identifiant qui rend la trace et ses artefacts réinspectables. Requis en `STANDARD`, `DIRECTION`, `SYSTÈME` et `ITER` (toute `RUN_CARD` sérialisée ; un `ITER` éphémère reste en mémoire locale, sans `RUN_CARD`) ; en `LITE`, l’artefact localement évident peut servir de locator. |
| `NEXT-PROOF` | Preuve suivante attendue. |

Dans la projection JSON contrôlable, les noms composés sont sérialisés en `snake_case` : `DATE / VERSION` devient `date_version`, `DIRECTION-STATUS` devient `direction_status`, `TRACE-LOCATOR` devient `trace_locator`, `NEXT-PROOF` devient `next_proof` et `CAPABILITY-PROFILE` devient `capability_profile`. Cette sérialisation ne change pas la signification canonique des champs.

**Protection critique.** Un risque `critical` porte une protection : contrôle, owner, scope, action en cas d’échec (`RETURNED`, `BLOCKED` ou `ESCALATED`), locator de preuve et **résultat** (`PASS`, `FAIL` ou `NOT-VERIFIED`). Une vérification absente n’est jamais rédigée comme accomplie : sans résultat observé, le résultat est `NOT-VERIFIED`, qui interdit `ACCEPTED`. En cas d’échec, l’issue suit l’action déclarée et aucun verdict n’est accepté. Un risque critique que le changement touche exclut `LITE` et `ITER` (`DIRECTION/START`, « Protection de niveau ») ; un delta démontré strictement local et sans effet sur ce risque ne le déclare pas comme risque du run.

**Table de correspondance.** La projection imbrique les champs de run sous `run_card` et regroupe la clôture sous `closure`. La colonne Phase dit quand un champ est renseigné : `avant build`, `après observation` ou `clôture`. Cette table est descriptive : le schéma livré et le validateur restent les autorités de structure et de contrôle.

| Champ canonique | Phase | Projection `RUN_CARD` | Sinon |
|---|---|---|---|
| MODE, DECISION, DECISION-INTENT, OWNER, ID, DATE / VERSION | avant build | `mode`, `decision`, `decision_intent`, `owner`, `id`, `date_version` | — |
| RISK (risque principal et impact potentiel) | avant build | `risk.level`, `risk.statement` ; protection critique : `risk.critical_protection` | — |
| AUTHORITY (portée, base, condition de reprise, décideur) | avant build | `owner` = décideur | portée, base et reprise : **trace**. Un reviewer (B3) n’est jamais le décideur par défaut |
| SCOPE, ARTIFACT | avant build, puis clôture | `artifact.scope`, `artifact.locator`, `artifact.version` | — |
| OBSERVATION | après observation | `proof.observed` | — |
| METHOD | après observation | `proof.provenance.method` (+ `capability`, `observed_at`) | — |
| PROOF / TRACE-LOCATOR | clôture | `trace_locator` | preuve détaillée : trace |
| LIMIT / NOT-VERIFIED | clôture | `closure.limitations`, `proof.not_verified` ; axes : `closure.axes` | — |
| STATE, ISSUE, VERDICT, DIRECTION-STATUS | chaque transition | `closure.state`, `.issue`, `.verdict`, `.direction_status` ; reclassement : `closure.reclassification` ; exception : `closure.exception` | — |
| DECISION-CHANGE | après observation | `decision_change` (`outcome`, `value`, `evidence` ; `reason` exigé si `N/A-JUSTIFIED`, non exigé si `NOT-OBSERVED`) | — |
| NEXT-PROOF | clôture | `next_proof` | — |
| NEXT-ACTION | clôture | DIRECTION : `creative_close.next_polish_action` ; sinon `next_proof` lorsque l’action suivante est une preuve | **hors projection : trace** |
| EXIT-CONDITION | clôture | `closure.reservations[].exit_condition` lorsqu’une réserve existe | **hors projection : trace** |
| VISUAL_TARGET : thèse, modal / parti | avant build | `direction.thesis`, `.anti_direction` (le modal nommé et le parti) | — |
| Direction qualifiée : premier objet (`DIRECTION/FIRST-OBJECT`), contrainte (`CONSTRAINT` de `DIRECTION/START`) ; surfaces couvertes par la direction (facultatif ; distinct d’`artifact.scope`, scope observé de l’artefact) | avant build | `direction.first_object`, `.constraint`, `.scope` | — |
| VISUAL_TARGET : ancre | avant build | `anchors[]` (dont `type` et `date`) | — |
| VISUAL_TARGET : objet de preuve | avant build → après observation | `next_proof` avant, `proof.observed` après | — |
| VISUAL_TARGET : matière / asset | avant build | droits : `artifact.rights_status` | route, cadrage, fallback : **trace** |
| VISUAL_TARGET : conséquence observable, silhouette, relations de plans, opération visuelle dominante, typographie, résolution initiale | avant build | — | **hors projection : trace** |
| Enjeu identitaire, calibration | avant build, puis clôture | `direction.identity_stake`, `direction.calibration` | — |
| Paquet d’alternative (`DIRECTION/VISUAL_TARGET`) | avant build | — | **hors projection : trace** |
| Creative close, B1b, paquet SYSTÈME, profil de style | clôture | `creative_close.*`, `closure.b1b`, `closure.system_package`, `profile_decision` | — |
| Sources, statut de source | avant build | `sources[]` (section canonique ou locator) | statut vérifié / non revu : **trace** |
| Manifeste externe | clôture | résolu par `trace_locator` | — |

**Règle.** Un champ hors projection n’est jamais glissé dans un champ voisin non prévu par cette table (par exemple NEXT-ACTION dans `limitations`) ; il reste dans la trace, que `trace_locator` rend retrouvable.

`STATUS` peut rester lisible comme alias d’archive ou d’affichage pour compatibilité avec des traces existantes. Il est interdit dans une nouvelle `RUN_CARD` comme champ unificateur : les nouveaux runs utilisent séparément `STATE`, `ISSUE`, `VERDICT` et `DIRECTION-STATUS`. Aucun alias ne remplace cette séparation.

### Profil de capacités

Quand une conclusion dépend d’un moyen d’observation, la `RUN_CARD` ajoute un `CAPABILITY-PROFILE` concis : **disponible**, **indisponible** ou **non requis**. Déclare seulement les capacités pertinentes au risque : artefact textuel, inspection DOM/CSS, navigateur/capture, calcul de contraste, clavier/AT, participant/tâche, runtime/données réelles. Toute capacité qui soutient un claim ajoute sa `BASIS` : résultat d’outil, environnement attesté, source utilisateur ou déclaration non attestée. Le profil décrit l’**observation** ; ce que le run peut **fabriquer** relève du bilan `FABRICATION` de `DIRECTION/CREATIVE-BOOT`, en trace.

Dans la `RUN_CARD`, chaque `basis` est typée : `capability`, `kind` (`tool_result`, `attested_environment`, `user_source` ou `unattested_declaration`) et `detail`. Pour un verdict accepté, `proof.provenance.capability` nomme la capacité qui soutient l’observation : elle figure parmi les capacités disponibles, et sa basis n’est pas une déclaration non attestée.

Une même capacité ne figure que dans une des catégories `available`, `unavailable` ou `not_required`. Le validateur refuse leur intersection, après retrait des espaces périphériques, quel que soit l’état du run. Ce contrôle porte sur le même libellé ; il ne reconnaît pas les synonymes et n’atteste pas la disponibilité réelle.

Ce profil n’est ni un score, ni un gate, ni une preuve. Il sert à empêcher qu’une vérification absente soit rédigée comme accomplie. Une `BASIS` déclarative ne vaut pas attestation ; elle interdit seulement de présenter la capacité comme observée. Une capacité indisponible conduit à la preuve disponible la plus faible ou à `NOT-VERIFIED`; elle ne réduit jamais silencieusement le mode, le risque ou le verdict requis.

### Mode agent seul et preuve dégradée

<!-- concept:HON-05 -->
Lorsque le run est exécuté par un agent sans regard indépendant, sans capture réelle ou sans runtime vérifiable, applique les limites suivantes. Ce mode ne constitue ni un nouveau mode de run, ni une permission de réduire le niveau de protection ; il rend seulement explicite le niveau de conclusion atteignable avec les capacités présentes.

| Capacité disponible | Ce que l’agent peut faire | Ce qu’il ne peut pas conclure seul |
|---|---|---|
| Runtime et capture réels, sans second regard | Construire, capturer, comparer et corriger l’artefact ; documenter une auto-comparaison. | Une revue indépendante, aveugle ou externe ; une calibration complète d’une décision identitaire importante. |
| Pas de capture ou de runtime réel | Formuler une hypothèse, préparer l’artefact et déclarer la preuve attendue. | Une qualité perceptuelle observée, un `PASS` de rendu ou une preuve de comportement non exécuté. |
| Pas de regard externe lorsque B3 est dans le scope | Conserver la capture, la comparaison, la limite, la réserve et la prochaine preuve. | Étiqueter l’auto-comparaison comme regard indépendant, comparatif ou aveugle. |
| Capacité manquante sur un risque critique | Déclarer la limite, nommer l’owner et préparer `NEXT-PROOF`. | Rétrograder silencieusement le mode, le risque ou le verdict requis. |

Une auto-comparaison B1b peut soutenir une correction de craft, mais elle ne satisfait jamais un claim de revue indépendante. Si une preuve obligatoire manque, le run reste `NOT-VERIFIED` sur l’axe concerné et adopte l’issue ou le verdict approprié — notamment `EXPLORATORY`, `RETURN-DIRECTION`, `ACCEPTED-WITH-RESERVATION` ou `ESCALATED` — selon le périmètre et le risque. `ACCEPTED` n’est pas disponible lorsque la preuve obligatoire manque.

### Vue d’exécution dérivée

Une `EXECUTION-SNAPSHOT` peut être construite pour démarrer, déléguer ou reprendre un run. C’est une vue locale et éphémère de la trace existante et des sections canoniques ; elle s’appuie sur la `RUN_CARD` lorsque ce format est requis. Elle ne remplace ni ACTION, ni les sources qu’elle cite. Elle expire lorsqu’un mode, un risque, une capacité, un artefact ou une source pertinente change.

```text
RUN-ID — identifiant du run
SOURCE-VERSION / ARTIFACT-VERSION — version des sources chargées et de l’artefact
GENERATED-AT — instant de génération de la snapshot
MODE — valeur classée par DIRECTION/START
DECISION / RISK — choix à trancher et coût d’erreur
SOURCES — sections canoniques réellement nécessaires
CAPABILITIES — disponible / indisponible / non requis
CAPABILITY-BASIS — résultat d’outil / environnement attesté / source utilisateur / déclaration non attestée, si une capacité soutient un claim
FACTS — artefacts et observations déjà fournis
AXES — V / U / A / T dans le scope de preuve actuel
LIMIT — ce que la trace ne permet pas d’affirmer
TRACE-LOCATOR / NEXT-PROOF — reprise et prochaine vérification
```

Une snapshot est ainsi datable. Elle ne crée aucun statut, owner, route ou claim. Pour une décision ouverte, elle conserve les alternatives et organise la preuve suivante ; elle ne choisit pas une variante sans artefact applicable.

**Mobiliser une relation ouverte.** La vue peut rapprocher les connexions situées de `READING_MAP.md`, les passages propriétaires et les informations de la trace hors JSON : promesse, silhouette, cadrage, moyens de fabrication, héritage et portée d’autorité. Réemploie les champs existants pour rendre explicites effet recherché, levier concret, source/version et moyens, condition de reprise et observation attendue. Ne crée ni trace par ressource ni obligation de snapshot. Les lectures et protections dues selon DIRECTION restent applicables même si une suggestion facultative n’est pas affichée.

Avant construction, conserve l’effet comme attendu. Une condition inconnue appelle un approfondissement proportionné si elle peut changer la décision, ou une hypothèse explicite autorisée dans ce scope ; elle ne vaut ni non-applicabilité ni question systématique. Après observation, indique l’effet réellement visible et sa limite. Un défaut proposé sans observation reste une hypothèse. Distingue les moyens de fabrication, les capacités d’observation attestées et l’autorité d’action.

Lors d’une reprise, réexamine les contributions touchées par un changement de contexte, contenu, source/version, destination, moyens ou artefact, ainsi que la preuve qui en dépend. La validité d’une preuve antérieure ne se déduit pas de sa présence. Arrête l’approfondissement lorsque la prochaine décision, le levier, la limite et l’observation sont explicites ; aucun quota de connexions ou score esthétique n’est créé.

### Projection machine-readable optionnelle

Pour un agent ou un script, la `RUN_CARD` ou l’`EXECUTION-SNAPSHOT` peut être représentée en YAML. Cette projection est une vue de transport lisible ; elle ne crée aucun contrat, statut, route, gate, axe ou owner supplémentaire. `ACTION` reste la seule source d’autorité et les champs doivent conserver leurs significations canoniques.

La projection canonique se trouve dans `gouvernance/schemas/run_card.example.json`. Utilisez-la comme exemple machine-readable et validez-la avec `python3 gouvernance/outils/validate_run_card.py gouvernance/schemas/run_card.example.json`. ACTION ne duplique pas ici un exemple YAML partiel : la projection JSON est la source unique de l’exemple structuré, tandis que cette section précise seulement son rôle de transport.

Les valeurs `state`, `issue`, `verdict`, `gate`, `axis`, `decision_change`, `NOT-VERIFIED`, `NOT-OBSERVED` et `N/A-JUSTIFIED` ne doivent pas être fusionnées. `null` signifie qu’aucune valeur n’est déclarée dans cette projection ; il ne signifie ni réussite ni preuve absente. Seuls `closure.issue`, `closure.verdict` et `risk.critical_protection` admettent `null` ; un champ facultatif sans valeur est omis (par exemple `closure.direction_status` hors surface `DIRECTION`), et un champ requis sans valeur suit sa règle propre (par exemple des ancres vides avec une issue non nulle). La projection ne doit jamais introduire `SELF-DECLARED`, `ATLAS-PASS`, `POLISHED`, `SLOP-FREE` ou un score esthétique. La projection machine ne remplace ni la trace complète, ni l’observation, ni la clôture d’ACTION.

### Frontière de validation et de preuve

<!-- concept:HON-04 -->
La validation JSON, la validation CLI, les fixtures, la compilation, le build et l’intégrité d’une archive établissent seulement que la projection, le package ou l’artefact de distribution respecte les contrôles exécutés. Ils ne prouvent ni que l’artefact est réellement implémenté dans son runtime, ni son usage, ni son accessibilité exécutée, ni sa performance, ni sa qualité visuelle, ni la préférence humaine. Une `RUN_CARD` valide peut donc rester `NOT-VERIFIED` sur un axe ou porter une limitation substantielle.

<!-- concept:VAL-01 -->
**Ce qu’atteste une `RUN_CARD` validée :** la forme de la projection et les invariants de la liste close (états, issues, verdicts et leur temps, axes, protection critique, exception, capacité et version de la preuve, réserves, droits déclarés, ancres, conséquence décisionnelle, reclassement, paquet SYSTÈME, B1b, trace par mode). **Ce qu’elle n’atteste pas (forme seule) :** que les observations ont réellement eu lieu ; la justesse des jugements V/U/A/T ; l’étendue réelle d’un claim (tâche utilisateur, technologie d’assistance, périmètre de diffusion) ; l’identité de la personne qui autorise ; la réalité des droits, licences et données ; la fraîcheur d’une ancre, dont seule la date ISO est contrôlée ; la qualité perceptuelle. Par mode : pour `LITE`, `ITER` et `STANDARD`, la machine vérifie les invariants communs et les champs de mode nommés dans la colonne « Contrôle machine » d’`ACTION/CLOSE-PACKAGE` ; le reste du paquet vit dans la trace et n’est pas vérifié ; pour tous les modes, elle ne vérifie ni que les consumers listés sont tous les consumers réels, ni que la baseline montre ce qu’elle prétend, ni que la décision couverte par une paire équivalente est bien la même. Ces points restent à la trace, à la revue et à l’owner.

Le **profil strict** applique les mêmes exigences par mode que la validation normale. Il ajoute le rejet des placeholders et des hôtes de démonstration, et l’existence des locators locaux — artefact, trace et, si la paire B1b est faite, ses deux captures —, résolus depuis le dossier de la carte.

Pour chaque claim important, séparer explicitement : **cible de conformité** ou décision visée ; **méthode** ; **scope et runtime observés** ; **résultat** ; **limite** ; **prochaine preuve**. Si l’un de ces éléments manque, ne l’inférer pas depuis la validation de structure : conserver le verdict, l’issue ou `NOT-VERIFIED` approprié selon le contrat existant. La projection machine transporte ces distinctions lorsqu’elle possède les champs correspondants ; les dimensions non sérialisées restent dans la trace complète, le ticket, le manifeste ou le paquet de preuve cité.

---
