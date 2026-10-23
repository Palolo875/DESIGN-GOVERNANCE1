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

Au lancement, la `RUN_CARD` contient la décision dominante de la ligne `RUN` (`DIRECTION/START`) :

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

### Raccord de trace pour `SAVOIR/DESIGN-ATLAS`

Lorsque `SAVOIR/DESIGN-ATLAS` est chargée, ses champs de présélection restent des éléments locaux de décision et ne remplacent pas la `RUN_CARD`. Elle n’est appelée qu’après classification, décision et risque ; si aucune famille ne peut modifier la prochaine décision, elle n’est pas chargée. Avant le build, `DECISION-MODIFIED`, `WHEN-USEFUL`, `COUNTERINDICATION`, `MEDIUM-SCOPE` et `PROOF-LIMIT` décrivent une hypothèse de sélection, non une observation indépendante. Une rationale, une cible visuelle, une ancre, une référence ou la présence d’un asset ou d’un composant ne prouve ni l’implémentation, ni l’utilité, ni la qualité, ni l’accessibilité, ni l’efficacité.

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

**Mobiliser une relation ouverte.** La vue peut rapprocher les connexions situées de `sections/READING_MAP.md`, les passages propriétaires et les informations de la trace hors JSON : promesse, silhouette, cadrage, moyens de fabrication, héritage et portée d’autorité. Réemploie les champs existants pour rendre explicites effet recherché, levier concret, source/version et moyens, condition de reprise et observation attendue. Ne crée ni trace par ressource ni obligation de snapshot. Les lectures et protections dues selon DIRECTION restent applicables même si une suggestion facultative n’est pas affichée.

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

Le **profil strict** applique les mêmes exigences par mode que la validation normale. Il ajoute le rejet des placeholders (y compris `?` ou `inconnu` à la place d’un locator) et des hôtes de démonstration, et l’existence des locators locaux — artefact, trace et, si la paire B1b est faite, ses deux captures —, résolus depuis le dossier de la carte. Un fragment ou une requête (`exemple: page.html#hero`, `exemple: page.html?state=empty`) désigne une section ou un état : seul le fichier est contrôlé, pas la section ni l’état.

Pour chaque claim important, séparer explicitement : **cible de conformité** ou décision visée ; **méthode** ; **scope et runtime observés** ; **résultat** ; **limite** ; **prochaine preuve**. Si l’un de ces éléments manque, ne l’inférer pas depuis la validation de structure : conserver le verdict, l’issue ou `NOT-VERIFIED` approprié selon le contrat existant. La projection machine transporte ces distinctions lorsqu’elle possède les champs correspondants ; les dimensions non sérialisées restent dans la trace complète, le ticket, le manifeste ou le paquet de preuve cité.

---

<!-- origine:ACTION.md -->
## ACTION/PIPELINE-DIRECTION — direction vérifiable

Ce pipeline s’applique au mode `DIRECTION`. Il vise une direction réellement choisie, non un catalogue de variantes.

`DIRECTION/DOUBLE-LOOP` décrit la boucle d’édition, seule description de la boucle (copiée dans le noyau). `ACTION/PIPELINE-DIRECTION` décrit son exécution livrable : préparer, construire, produire la preuve, appliquer les corrections, comparer et clôturer ou retourner. `ACTION/GATE-B/B1b` est un contrôle spécialisé déclenché dans ce pipeline lorsque son scope est actif ; ces trois niveaux ne sont pas trois boucles concurrentes.

### Boucle de qualité et branche one-shot

Pour tout run qui produit un rendu, la boucle est celle de `DIRECTION/DOUBLE-LOOP` ; ce pipeline en exécute la préparation, la preuve, puis la clôture ou le retour. Observe le rendu réel sans te laisser guider par la rationale.

La branche `one-shot` est une exécution raccourcie de cette même boucle, jamais une suppression de la boucle. Elle permet de clôturer après l’observation initiale lorsque le premier rendu atteint la qualité attendue du mode, que la direction est identifiable, que les risques applicables sont couverts et qu’aucune amélioration utile n’est probable. Si le premier rendu est faible, générique ou incomplet, la branche one-shot ne s’applique pas : corrige, retourne ou déclare honnêtement la limite. Sur une surface `DIRECTION` acceptée avec V positif, l’arrêt suppose `ACTION/GATE-B/B1b` fait ou l’un de ses deux motifs `N/A-JUSTIFIED` ; la comparaison peut confirmer la décision initiale (`confirmed`). En trace légère, la proposition reste `EXPLORATORY` et B1b ne s’applique pas.

### 1. Situer les positions

Lorsque la décision est ouverte, formule des positions distinctes sur les axes pertinents de `SAVOIR/CRAFT/CFT-02`, l’émotion traduite en levier visuel ; pour la structure, sur les axes de tension de `BIBLIOTHEQUE/TENSION`.

Il n’existe aucun quota obligatoire de directions. Une position retenue et une alternative située suffisent lorsque le risque dominant et les tensions sont déjà clairs.

La projection `creative_direction_set` de `gouvernance/schemas/production_contracts.schema.json` est conditionnelle : elle décrit une comparaison lorsqu’une décision ouverte et une alternative plausible la rendent utile. Si elle est produite, au moins deux positions distinctes matérialisent cette comparaison ; aucun plafond de directions n’est imposé. Ce minimum de structure du contrat ne demande ni variantes ni builds supplémentaires aux autres runs. Les qualités prioritaires de CREATIVE-BOOT sont un foyer de construction distinct du nombre de positions.

### 2. Traduire l’émotion

Une émotion n’est une direction que lorsqu’elle change une décision visible : composition, contraste, densité, échelle typographique, rythme de motion, contenu, relation texte/image ou traitement matériel.

« Premium », « chaleureux » ou « dynamique » sont des intentions à traduire, non des options de design autonomes.

### 3. Développer une alternative située

Le déclenchement appartient à `DIRECTION/DIVERGENCE` et les leviers à `SAVOIR/CRAFT/CFT-02`. En trace complète, avant le build, la trace du run (retrouvable par `trace_locator`) nomme la position retenue, l’alternative considérée, la raison de son niveau de matérialisation et la preuve attendue ; la projection JSON ne porte pas ce paquet (voir `ACTION/RUN_CARD`). En trace légère, la première proposition nomme l’alternative écartée (checkpoint, étape 7).

Matérialise l’alternative seulement au niveau nécessaire pour comparer la décision : phrase, schéma, cible ou rendu. Ne construis pas une variante qui ne peut modifier aucune décision. Si aucune alternative située ne change raisonnablement le choix, note cette condition et passe à la spec après avoir nommé la raison.

### 4. Produire la spec visuelle

Une spec visuelle synthétique existe avant le premier code ou rendu d’une surface `DIRECTION`. La définition des voies `ANCHOR-GENERATED`, `ANCHOR-OBSERVED` et `ANCHOR-PROVIDED` appartient à `DIRECTION/VISUAL_TARGET` ; ACTION en conserve seulement la trace opératoire : type et identifiant de l’ancre, cible ou hypothèse, attributs observés, éléments retenus et rejetés, contre-indications, limites de transfert et preuve attendue.

`ANCHOR-GENERATED` reste une hypothèse visuelle comparable, non une calibration externe suffisante par défaut. Lorsque l’enjeu identitaire est élevé, accompagne-la d’une référence observée, d’une contrainte réelle ou d’une réserve explicite sur l’absence de calibration externe.

La spec décrit uniquement les décisions utiles : structure, hiérarchie, relation texte/preuve, traitement perceptible, typographie lorsque pertinente, contenu réel, actions, états, contre-indications et palette lorsque la couleur porte une décision.

Une ancre est utile seulement si elle apporte une décision structurelle ou perceptuelle, une contre-indication et une liste d’attributs retenus, rejetés et non transférables.

Sans ancre utile et spec exploitable, les axes concernés sont `NOT-VERIFIED`. Le run devient `RETURNED`, `EXPLORATORY` ou `ESCALATED` selon le périmètre ; `FAIL-ASSUMED` ne vaut que pour un échec connu (`ACTION/OVERRIDE`), jamais pour une ancre absente.

Dans une `RUN_CARD`, chaque ancre porte son `type` (`generated`, `observed` ou `provided`) et une date ISO ; `direction.identity_stake` déclare l’enjeu identitaire (`high` ou `normal`). Lorsque l’enjeu est élevé, que toutes les ancres sont générées et que la direction est tenue, `direction.calibration` nomme sa base : `real_constraint`, ou `generated_only_reserved`, qui interdit `ACCEPTED`. Une revue indépendante n’est pas une base de calibration. Une ancre manquante se sérialise par l’issue — ancres vides, issue non nulle, aucun verdict accepté —, jamais par une ancre inventée.

### 5. Sourcer et tracer

Trace dans la `RUN_CARD` ou le manifeste les références, requêtes, images ou assets réellement observés, avec leur rôle et leur statut. `BIBLIOTHEQUE.md` fournit des structures de décision ; il ne devient ni ancre visuelle, ni source d’asset, ni preuve de comparaison.

Pour toute recherche substantielle, distingue : `VERIFIED-THIS-RUN`, `MODEL-KNOWLEDGE-NOT-RECHECKED` et `USER-SOURCED-NOT-RECHECKED`. Les claims mesurés, datés, réglementaires ou dépendants d’un outil portent source, date, portée et limite dans la trace locale du run ; ils ne deviennent partagés qu’après décision de gouvernance.

Pour un asset directeur, trace aussi la route `CODE-NATIVE`, `FOURNI`, `CURATÉ`, `GÉNÉRÉ-DIRIGÉ` ou `HYBRIDE`, sa raison, son traitement prévu, ses droits ou incertitudes et l’alternative refusée. Une requête ou un prompt ne prouve pas qu’un asset est adéquat : observe l’asset à son ratio, son crop, son contraste et son voisinage de texte réels.

### 6. Sélectionner contre la facilité

Si plusieurs solutions restent plausibles, nomme ce qui distingue le choix retenu. Si la solution est la plus simple à implémenter, défends-la par le JTBD, le risque, les droits, la performance, la maintenance ou une contrainte réelle.

> La faisabilité immédiate n’est pas une preuve d’appropriation.

### 7. Écrire la direction et demander une décision si nécessaire

Écris la direction retenue en une phrase : position, intention, décision dominante et contrainte servie. Compare-la à l’alternative située et formule l’avantage vérifiable du choix.

<!-- noyau:début CHECKPOINT -->
<!-- concept:CHK-01 -->
**La première proposition vaut checkpoint.** Quand la demande appelle une fabrication, construis la première scène, puis présente-la avec sa thèse, l’alternative écartée lorsqu’un autre choix plausible pouvait changer la décision, et ce qu’il faut décider ; la personne valide, réoriente ou arrête. Une demande de jugement, d’explication ou d’analyse d’un existant se conclut par ce jugement : elle n’impose ni scène nouvelle, ni variante, ni brief. Valider oriente la suite (affiner, décliner, préparer la vraie version) ; ce n’est pas une acceptation. Pour retenir la direction pour un produit réel, la personne le demande : le run passe en trace complète, avec ancre observée ou fournie, gates et verdict (absolu 2 de `DIRECTION`). Jusque-là, la proposition reste `EXPLORATORY`. Un checkpoint avant le build n’est requis que si la personne l’a demandé ou si le build engage une action irréversible ou coûteuse (publier, envoyer, payer, consommer des crédits, écraser un existant, engager l’owner, la personne responsable de la décision). Une marque, un public ou une hypothèse nouvelle est nommée dans la proposition ; elle ne bloque pas le build.
<!-- noyau:fin CHECKPOINT -->

Si un checkpoint préalable est requis et que l’autorisation manque, n’engage pas le build : applique `ACTION/AUTHORITY` (exploratoire, retourné ou escaladé). L’absence de regard externe est une autre question : déclare-la et compense-la par capture, comparaison, réserve et prochaine preuve ; cette compensation n’autorise rien.

### 8. Vérifier le rendu réel

Après le build, capture le rendu et compare-le à la spec. Pour chaque écart significatif, nomme l’observation, la cause probable, l’effet sur la tâche ou la direction et l’issue : `CORRECTED`, `ACCEPTED-DIFFERENCE` ou `REMAINING-RISK`. Ces valeurs sont des résultats locaux de comparaison, pas des statuts : `CORRECTED` se traduit par une conséquence décisionnelle `CHANGED` avec la nouvelle preuve ; `ACCEPTED-DIFFERENCE`, par `HELD-WITH-ACCEPTED-DIFFERENCE` et une réserve ; `REMAINING-RISK`, par une réserve. Inspecte en priorité la structure, la hiérarchie, la typographie, la composition, la spécificité, la qualité des assets, les composants authored, les états et la cohérence de finition ; ne corrige pas un défaut structurel par un effet décoratif terminal.

### Passe créative et polish

Lorsque la qualité perceptuelle est une décision du run, effectue après la première scène la revue créative définie par `SAVOIR/CRAFT/CFT-00` (Creative Quality Review), puis une repasse ciblée avant la clôture. ACTION en fixe le moment et la trace ; la revue ne produit ni score esthétique ni statut concurrent. Elle vérifie aussi si le premier rendu atteignait déjà la qualité attendue du mode, ou si la boucle est en train de réparer une préparation insuffisante.

La repasse examine les rapports entre masses, vides, échelles, rythme, typographie, matière, lumière ou profondeur, contenu, objet de preuve, états, responsive, transitions et détails de finition. Elle corrige d’abord le défaut dominant avec l’activation de `SAVOIR/STATE` ; la trace existante relie observation initiale, geste appliqué, condition, effet réinspecté et décision de conserver, ajuster ou retirer. Une capacité manquante reste une limite de preuve, pas un effet observé. Ajouter des effets, des variantes ou des assets sans améliorer une relation observable ne constitue pas une passe de polish.

Pour un run `DIRECTION`, la clôture créative doit pouvoir répondre à quatre questions : **quelle présence est effectivement produite, quelle signature rend la proposition spécifique, quel détail ou état montre le niveau de craft, et quel défaut reste prioritaire ?** Les réponses citent le rendu ou un objet inspectable et restent distinctes des preuves d’usage, d’accessibilité et de robustesse.

La comparaison vérifie notamment silhouette, opération dominante, matière/asset, typographie, objet de preuve, états et retenue. « Plus beau », « plus premium » ou « ressemble à la référence » ne sont pas des observations suffisantes.

Lorsque le risque visuel ou identitaire le requiert, la preuve doit être représentative de l’artefact construit et de son scope : elle montre, selon la décision, hiérarchie, composition, typographie, matière, spécificité, cohérence, retenue, états et résolution réelle. Une capture idéale ne masque pas un état, un viewport, un contenu ou un comportement non inspecté. La trace peut qualifier le niveau de craft observé — `Correction`, `Précision` ou `Intention` — mais cette qualification reste une lentille locale de jugement ; elle ne devient ni un score esthétique, ni un verdict global, ni un statut de direction. Une qualité visuelle observée ne prouve pas à elle seule la fidélité de la direction, la réussite d’usage, l’accessibilité ou la robustesse technique.

Retourne à la direction, à l’ancre, à la spec ou au build lorsque l’écart dominant persiste, lorsque la preuve manque ou lorsqu’une correction locale ne change plus réellement le résultat. Aucun nombre fixe d’itérations n’est requis.
