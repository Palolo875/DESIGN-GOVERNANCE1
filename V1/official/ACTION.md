# ACTION — Pipeline de livraison & preuves

**Design Governance V1 — expérimentation maintenue.** Cette V1 est un cadre de travail en évaluation ; elle n’est pas présentée comme une release publique stabilisée. Ses limites, preuves et conditions d’usage restent explicites. ACTION transforme une direction ou une décision produit en trace de run, artefacts observables, preuves adaptées, gates proportionnés et verdicts inspectables.

## Responsabilité

`ACTION` est le propriétaire des preuves exécutables, des gates, des statuts de run, des verdicts et de la clôture. Dans un run, le chargement suit `DIRECTION/CHARGE`, seule liste de chargement. Pour lire ACTION hors run, commencez par `ACTION/STATUS` et `ACTION/PRECONDITION`, puis la route de votre mode `ACTION/RUN-<MODE>`, et chargez seulement les gates correspondant au risque déclaré. `ACTION/FAST-PATH` est une vue de formalité réduite pour un delta local ; il ne supprime ni la preuve requise ni l’honnêteté du statut.

**Capacité positive d’ACTION.** ACTION ne sert pas seulement à filtrer ou accepter un résultat : elle transforme une direction en livraison observable et améliorable. Son chemin positif est la boucle d’édition (`DIRECTION/DOUBLE-LOOP`), prolongée par la preuve et, en trace complète, par une clôture avec une limite et une prochaine preuve. Les gates protègent ce chemin ; ils ne sont pas sa finalité. La qualité du premier rendu, la lisibilité de la décision et la possibilité de reprendre le run font partie de la valeur livrée.

### Carte de lecture par mode

Cette carte est une vue de `DIRECTION/CHARGE`, pas une seconde liste : elle nomme les sections d’ACTION que la route de chaque mode appelle.

**Socle pour tous les modes :** `ACTION/STATUS` et `ACTION/PRECONDITION`, dès que le run écrit un statut, un gate ou un verdict (trace complète) ; `DIRECTION/CHARGE` reste la liste du démarrage.

| Mode | Sections d’ACTION appelées par la route |
|---|---|
| `LITE` | `ACTION/RUN-LITE` ; `ACTION/GATE-A` applicable et `ACTION/GATE-B` du risque dominant |
| `ITER` | `ACTION/RUN-ITER` ; non-régression pertinente ; `ACTION/GATE-A` applicable et `ACTION/GATE-B` du risque touché ; `ACTION/GATE-C` seulement si le craft change |
| `STANDARD` | `ACTION/RUN-STANDARD` ; `ACTION/UI-UX-REALITY` si la surface UI/UX est nouvelle ou substantiellement modifiée ; `BIBLIOTHEQUE/SELECT` si la structure est ouverte ; `ACTION/GATE-A`, `ACTION/GATE-B` ou `ACTION/GATE-C` ciblés selon le risque |
| `DIRECTION` | `ACTION/RUN-DIRECTION`, `ACTION/UI-UX-REALITY` si la surface UI/UX est nouvelle ou substantiellement modifiée, `ACTION/PIPELINE-DIRECTION`, `ACTION/VISUAL_PROOF`, `ACTION/GATE-A`, `ACTION/GATE-C` ; `ACTION/GATE-B` en trace complète (`ACTION/HANDOFF`) |
| `SYSTÈME` | `ACTION/RUN-SYSTEM`, puis `CHANGELOG` pour adoption ou migration |

Le paquet de sortie de chaque mode est défini par `ACTION/CLOSE-PACKAGE` ; `ACTION/RUN-DIRECTION` (ancrages) et `ACTION/RUN-SYSTEM` (`closure.system_package`) en précisent le détail.

Les sections `RUN_CARD`, `CLOSE-PACKAGE` et `CLOSE-EXIT-CHECK` s’ajoutent lorsque la trace est persistante ou que la clôture l’exige. `FAST-PATH` n’est pas une sixième voie : chaque occurrence de ce nom reste une vue locale du propriétaire qui l’emploie.

### ACTION/HANDOFF — sortie minimale commune

`ACTION` est propriétaire de la preuve, des gates, des statuts, des verdicts et de la clôture. Une sortie de run a deux formes, à ne pas confondre. Les façades peuvent les préparer ou les recopier, jamais les redéfinir.

1. **Handoff**, pour une reprise ou un run persistant : les éléments suivants doivent être résolubles.

```text
MODE — DECISION — RISK — SCOPE — ARTIFACT
OBSERVATION/METHOD — PROOF/TRACE-LOCATOR — LIMIT/NOT-VERIFIED
DECISION-CHANGE — NEXT-ACTION — OWNER — NEXT-PROOF — EXIT-CONDITION
```

2. **Réponse visible**, pour un humain, par défaut :

<!-- noyau:début SORTIE -->
<!-- concept:SOR-01 -->
La personne reçoit une réponse en langage produit, sans le jargon interne du système, en quatre rubriques :

```text
Ce que j’ai fait : la proposition et ses choix principaux, en une ou deux phrases.
Pourquoi : la thèse, l’alternative écartée et ce que le rendu permet de décider.
Ce qui manque pour la vraie version : contenus, assets, droits, tests ou capacités, avec le plafond atteint.
La suite : une ou deux actions proposées, et ce qu’il faut de la personne pour les engager.
```

L’agent active le système en silence : la personne donne l’objectif, le périmètre et l’autonomie ; l’agent choisit le mode, charge les sources et tient la trace. Le mode, la conséquence décisionnelle d’`ACTION/STATUS` (décision changée, confirmée ou abandonnée, `N/A-JUSTIFIED` ou `NOT-OBSERVED`), la preuve et l’owner restent dans la trace et sont exposés sur demande (« pourquoi ? », « qu’as-tu vérifié ? »). Les codes de route, de concept et de statut n’apparaissent dans la réponse visible que si la personne travaille sur le système lui-même ou les demande explicitement ; quand la trace est écrite dans le fichier livré, la réponse ne la recopie pas sauf demande explicite. Les limites de vérification qui affectent l’usage ou la décision restent visibles, même lorsque la trace est persistée. La réponse visible ne remplace jamais le handoff d’un run persistant.
<!-- noyau:fin SORTIE -->

3. **Niveau de trace**, choisi par l’agent :

<!-- noyau:début TRACE -->
<!-- concept:TRA-01 -->
**Trace légère par défaut.** Hors run persistant, partagé ou audité, la trace tient en six lignes au plus : mode ; thèse (promesse → objet de preuve → geste) ; modal, trame et parti ; plafond atteint et contenus marqués ; défaut dominant restant ; prochaine preuve. Lorsque la qualité perceptuelle est une décision du run, la ligne du défaut dominant rend la revue de présence de `SAVOIR/CRAFT/CFT-00` après la première scène : ce qui retient, ce qui reste générique et, s’il est utile, le geste concret conditionné de `SAVOIR/STATE`, avec son effet observé ou sa limite. Nomme l’objet et la modification ; distingue un geste envisagé d’un geste appliqué et réinspecté. Si aucune intervention n’est utile, indique la raison de conserver. Elle s’écrit à côté de l’artefact quand l’agent écrit des fichiers (fichier de trace ou en-tête du fichier livré) ; sinon, après la réponse visible, sous « Trace ». Les planchers s’appliquent pendant la fabrication (vérité, `ACTION/GATE-A` selon le profil de surface, boucle d’édition) ; seule leur écriture s’allège. Le run livre une **proposition** `EXPLORATORY` : ni verdict, ni acceptation, ni clôture, ni `RUN_CARD`. **Trace complète** (handoff, paquet de clôture, gates écrits et projection selon `ACTION/CLOSE-PACKAGE`, `B1b` dans son scope) si le run est persistant, partagé, audité, ou si une acceptation ou une clôture est demandée. La forme courte LITE conserve une trace complète sans RUN_CARD (`ACTION/HANDOFF`).
<!-- noyau:fin TRACE -->

**Formes.** La ligne de run de `DIRECTION` est la mémoire de lancement, sous-ensemble de lancement de ce handoff ; le handoff est la transmission ; `ACTION/CLOSE-PACKAGE` est la clôture par mode ; la `RUN_CARD` JSON est la projection persistante, selon la table de correspondance d’`ACTION/RUN_CARD`. **Forme courte LITE** (trace complète d’un `LITE` clôturé sans `RUN_CARD`, distincte de la trace légère, qui ne clôture pas) : le paquet LITE de `ACTION/CLOSE-PACKAGE` ; les autres champs du handoff sont `N/A-JUSTIFIED` par défaut, avec deux pertes déclarées (METHOD, EXIT-CONDITION) ; TRACE-LOCATOR est alors l’artefact. Une reprise par un autre agent exige OWNER et NEXT-ACTION ; sinon la forme courte reste une préparation.

Le handoff réutilise les champs existants ; il ne crée ni statut, ni gate, ni nouveau schéma. Les champs non applicables sont marqués `N/A-JUSTIFIED`. Un run persistant utilise la projection `RUN_CARD` et son validateur, sauf la forme courte LITE définie ci-dessus : sa trace complète persiste dans l’artefact selon `ACTION/CLOSE-PACKAGE`. Cette exception ne dispense ni des preuves dues ni des conditions de reprise ; une demande de projection structurée requiert la `RUN_CARD` validée. Une sortie courte qui ne fournit pas le paquet applicable reste une préparation, une clarification ou une décision non clôturée.

**Condition d’arrêt de lecture :** arrêter lorsque le mode, le risque, la route, la preuve, la limite, le propriétaire et la prochaine action sont connus. Charger un registre, une route ou un gate supplémentaire uniquement s’il peut modifier l’un de ces éléments.

### Les quatre registres à ne pas mélanger

Pour naviguer dans ACTION : la **route** dit quoi faire ; puis quatre registres, dans cet ordre : **observation**, **interprétation**, **décision**, **persistance**. La preuve réunit observation et interprétation ; elle ne se confond pas avec la décision. Ces quatre registres structurent la trace ; ils ne créent ni états ni statuts supplémentaires.

| Registre | Question | Sortie minimale |
|---|---|---|
| **Observation** | Qu’est-ce qui a été regardé, par quelle méthode, dans quel scope et quelle version ? | Artefact, méthode, scope, version, date et capacité. |
| **Interprétation** | Que montre réellement l’observation, avec quelle couverture et quelle limite ? | Relation, effet, défaut dominant, incertitude et limite. |
| **Décision** | Que fait-on maintenant et pourquoi ? | Correction, retour, acceptation, réserve, reclassification ou escalade. |
| **Persistance** | Où la décision et ses limites restent-elles inspectables ? | Trace complète selon `ACTION/HANDOFF`, projection `RUN_CARD` selon la forme de clôture, trace locator, owner, prochaine preuve et condition de sortie. |

`STATE`, `ISSUE`, verdict d’axe, statut de direction et verdict global ne sont jamais des niveaux de maturité ni des synonymes. Le JSON Schema est l’autorité de structure de la projection ; les exemples YAML et textuels restent des vues de transport ou d’explication.

**Ordre de preuve.** Vérifie d’abord le risque dominant. Pour une surface identitaire sans risque critique, vérifie que la direction `P0` et le craft visuel sont réellement tenus ; vérifie ensuite le plancher `P1` d’usage et d’accessibilité ; adapte `P2` au runtime et à la plateforme réels ; déclenche `P3` pour la robustesse, la performance, la compatibilité et le maintien lorsque le risque le requiert. En présence d’un risque critique de tâche, de santé, de sécurité, de confidentialité, de permission ou d’accessibilité, la protection critique passe avant l’optimisation visuelle. P1 est non négociable, mais aucun gate ne transforme une interface conforme en interface réussie si la décision visuelle et la tâche ne tiennent pas.

ACTION ne remplace pas :

| Document | Responsabilité |
|---|---|
| `DIRECTION.md` | Rôle, cinq absolus, classification, routage général et cadrage de capacité. |
| `SAVOIR.md` | Principes de jugement, craft, styles, contexte, outils et intégrité. |
| `BIBLIOTHEQUE.md` | Supports, grilles, scènes, objets, micro-interfaces et composants. |
| `CHANGELOG.md` | État de V1, changements futurs, pilotes optionnels et décisions de gouvernance. |

**Chargement.** Dès qu’un build, une vérification ou un changement d’état est engagé, charge ACTION au niveau requis par le mode. Le contrat court suffit en `LITE` et `ITER`. Le pipeline et les gates complets sont chargés lorsque le périmètre les déclenche. Les recettes de code, prompts, packages et intégrations de stack sont des ressources techniques ; ils ne constituent jamais une preuve à eux seuls.

### ACTION/AUTHORITY — portée d’action et reprise

Une capacité indique ce qui peut être construit ou vérifié ; elle ne constitue pas une autorisation de décider. Lorsque l’agent, l’outil ou l’équipe agit au nom d’un owner, déclare seulement si cela peut changer la décision, le risque, la persistance ou une action externe : la portée d’action autorisée, la base de cette autonomie, la condition de reprise ou d’escalade, et le rôle qui reprend la décision si nécessaire. Ces éléments restent dans la trace existante d’ACTION ; ils ne créent ni état, ni issue, ni verdict, ni gate supplémentaire.

Un checkpoint indisponible ne réduit pas silencieusement le mode. Il rend la décision exploratoire, retournée ou escaladée selon le risque, la preuve disponible et la condition de sortie. `APPROVED`, lorsqu’un transport ou une trace le mentionne, signifie seulement qu’une décision d’autorité a été autorisée dans son scope ; il ne signifie ni résultat accepté, ni preuve complète, ni clôture.

### Parcours minimal

Le parcours d’un run est celui du noyau de la skill : classer et charger (`DIRECTION/CHARGE`), prendre le brief, construire une première scène complète, boucler (`DIRECTION/DOUBLE-LOOP`), répondre et tracer (`ACTION/HANDOFF`). ACTION en porte les preuves, les gates et, en trace complète, la clôture ; ses contrats restent applicables dès que le risque ou le mode les déclenche.

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

Pour une surface UI/UX nouvelle ou substantiellement modifiée, le premier objet doit rendre observables, dans la proportion du mode et du risque : hiérarchie de contenu, premier geste, feedback, états `loading`, `empty`, `error`, `unavailable`, `disabled` et succès partiel lorsque pertinents, contenu long ou multilingue, responsive recomposé, focus et récupération. Une capture de l’état nominal ne suffit pas lorsque l’état, la tâche ou la récupération fait partie de la décision.

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

## ACTION/FAST-PATH — preuve minimale sans rituel

Pour `LITE` et les petits `ITER`, arrête le protocole après quatre réponses : décision touchée, risque dominant, preuve la moins coûteuse et conséquence de la preuve ; puis, en trace complète, clôture avec le paquet de son mode : forme courte LITE pour `LITE`, paquet `ITER` pour un `ITER` (`ACTION/CLOSE-PACKAGE`) ; en trace légère, la proposition suffit.

Si aucune décision ne peut changer, n’ajoute pas de capture, comparaison ou route uniquement pour remplir le paquet. Journalise `N/A-JUSTIFIED` lorsque la procédure ne peut rien modifier.

Reviens à un mode plus riche si le changement touche une règle partagée, l’identité, la sécurité, l’accessibilité, le comportement critique ou une décision coûteuse.

---

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

La projection canonique se trouve dans `schemas/run_card.example.json`. Utilisez-la comme exemple machine-readable et validez-la avec `python3 scripts/validate_run_card.py schemas/run_card.example.json`. ACTION ne duplique pas ici un exemple YAML partiel : la projection JSON est la source unique de l’exemple structuré, tandis que cette section précise seulement son rôle de transport.

Les valeurs `state`, `issue`, `verdict`, `gate`, `axis`, `decision_change`, `NOT-VERIFIED`, `NOT-OBSERVED` et `N/A-JUSTIFIED` ne doivent pas être fusionnées. `null` signifie qu’aucune valeur n’est déclarée dans cette projection ; il ne signifie ni réussite ni preuve absente. Seuls `closure.issue`, `closure.verdict` et `risk.critical_protection` admettent `null` ; un champ facultatif sans valeur est omis (par exemple `closure.direction_status` hors surface `DIRECTION`), et un champ requis sans valeur suit sa règle propre (par exemple des ancres vides avec une issue non nulle). La projection ne doit jamais introduire `SELF-DECLARED`, `ATLAS-PASS`, `POLISHED`, `SLOP-FREE` ou un score esthétique. La projection machine ne remplace ni la trace complète, ni l’observation, ni la clôture d’ACTION.

### Frontière de validation et de preuve

<!-- concept:HON-04 -->
La validation JSON, la validation CLI, les fixtures, la compilation, le build et l’intégrité d’une archive établissent seulement que la projection, le package ou l’artefact de distribution respecte les contrôles exécutés. Ils ne prouvent ni que l’artefact est réellement implémenté dans son runtime, ni son usage, ni son accessibilité exécutée, ni sa performance, ni sa qualité visuelle, ni la préférence humaine. Une `RUN_CARD` valide peut donc rester `NOT-VERIFIED` sur un axe ou porter une limitation substantielle.

<!-- concept:VAL-01 -->
**Ce qu’atteste une `RUN_CARD` validée :** la forme de la projection et les invariants de la liste close (états, issues, verdicts et leur temps, axes, protection critique, exception, capacité et version de la preuve, réserves, droits déclarés, ancres, conséquence décisionnelle, reclassement, paquet SYSTÈME, B1b, trace par mode). **Ce qu’elle n’atteste pas (forme seule) :** que les observations ont réellement eu lieu ; la justesse des jugements V/U/A/T ; l’étendue réelle d’un claim (tâche utilisateur, technologie d’assistance, périmètre de diffusion) ; l’identité de la personne qui autorise ; la réalité des droits, licences et données ; la fraîcheur d’une ancre, dont seule la date ISO est contrôlée ; la qualité perceptuelle. Par mode : pour `LITE`, `ITER` et `STANDARD`, la machine vérifie les invariants communs et les champs de mode nommés dans la colonne « Contrôle machine » d’`ACTION/CLOSE-PACKAGE` ; le reste du paquet vit dans la trace et n’est pas vérifié ; pour tous les modes, elle ne vérifie ni que les consumers listés sont tous les consumers réels, ni que la baseline montre ce qu’elle prétend, ni que la décision couverte par une paire équivalente est bien la même. Ces points restent à la trace, à la revue et à l’owner.

Le **profil strict** applique les mêmes exigences par mode que la validation normale. Il ajoute le rejet des placeholders et des hôtes de démonstration, et l’existence des locators locaux, résolus depuis le dossier de la carte.

Pour chaque claim important, séparer explicitement : **cible de conformité** ou décision visée ; **méthode** ; **scope et runtime observés** ; **résultat** ; **limite** ; **prochaine preuve**. Si l’un de ces éléments manque, ne l’inférer pas depuis la validation de structure : conserver le verdict, l’issue ou `NOT-VERIFIED` approprié selon le contrat existant. La projection machine transporte ces distinctions lorsqu’elle possède les champs correspondants ; les dimensions non sérialisées restent dans la trace complète, le ticket, le manifeste ou le paquet de preuve cité.

---

## ACTION/RUN — routes d’exécution

Les blocs `RUN-*` donnent l’entrée, la sortie et le contrôle minimal de chaque mode. Les sections détaillées ci-dessous sont canoniques lorsque le bloc les appelle.

### `ACTION/RUN-LITE`

**Entrée.** Système et direction retrouvables ; delta local ou fix ; décision dominante connue.

**Faire.** Écrire la ligne de run, déclarer `DECISION-INTENT`, modifier, contrôler les gates A applicables et obtenir une preuve B du risque dominant. Charger `SAVOIR` ou `BIBLIOTHEQUE` uniquement si cela peut changer le correctif. Une alternative n’est documentée que si un choix plausible peut modifier le delta ou le risque.

**Sortie.** Paquet `LITE` d’`ACTION/CLOSE-PACKAGE`. Trace légère : la proposition (`ACTION/HANDOFF`).

**Clôture.** En trace complète, passer à `DECIDED`, puis `CLOSED`. Reclassifier en `SYSTÈME` si une règle partagée est touchée, en `ITER` si la direction précédente doit être réévaluée ou en `DIRECTION` si une nouvelle décision identitaire apparaît.

### `ACTION/RUN-ITER`

**Entrée.** Direction, composants, tokens et périmètre précédent retrouvables dans la trace légère (ligne de thèse), la `RUN_CARD`, le manifeste ou le projet. Dans une `RUN_CARD`, le rappel de direction est porté par `direction.thesis` et la trace par `trace_locator`.

**Faire.** Rappeler la direction en une phrase, déclarer `DECISION-INTENT`, appliquer le delta et vérifier la non-régression pertinente : visuelle, fonctionnelle, responsive, typographique ou systémique.

**Sortie.** Paquet `ITER` d’`ACTION/CLOSE-PACKAGE`. Trace légère : la proposition (`ACTION/HANDOFF`).

**Clôture.** En trace complète, passer à `DECIDED`, puis `CLOSED`. Utiliser `RETURNED` si une preuve ou correction doit être reprise dans le même mode, `RECLASSIFIED` si l’identité, la portée ou le système sont remis en cause.

### `ACTION/RUN-STANDARD`

**Entrée.** Écran ou flow nouveau, sans charge identitaire autonome ni blast radius systémique.

**Faire.** Cadrer le JTBD et la décision dominante. Appeler `BIBLIOTHEQUE/SELECT` si support, grille, scène ou objet restent ouverts. Produire dès le premier rendu une composition jugeable : contenu crédible, hiérarchie, typographie appropriée, états pertinents, responsive applicable et détail de finition utile. Exécuter les Gates A et B ciblés. Utiliser une ancre visuelle seulement lorsqu’une direction locale, une matière, une composition ou une comparaison perceptuelle le rend utile.

**Sortie.** Paquet `STANDARD` d’`ACTION/CLOSE-PACKAGE`. Trace légère : la proposition (`ACTION/HANDOFF`).

**Clôture.** En trace complète, passer à `DECIDED`, puis `CLOSED`. Passer à `EXPLORATORY` si une preuve requise manque, à `RETURNED` si une correction doit être reprise dans le même mode ou à `DIRECTION` si la surface devient identitaire.

### `ACTION/RUN-DIRECTION`

**Entrée.** Identité, surface de marque, premier contact ou hypothèse de direction autonome.

**Faire.** Exécuter le pipeline `ACTION/PIPELINE-DIRECTION` : positions distinctes lorsque la décision est ouverte, alternative située lorsque nécessaire, ancre utile, `DIRECTION/VISUAL_TARGET`, spec, checkpoint si nécessaire, build de la première scène significative, `ACTION/VISUAL_PROOF`, capture et comparaison. La première scène significative doit être présentable par défaut : elle porte déjà la direction, la hiérarchie, la typographie, la composition, la palette, la matière ou l’asset pertinent, les composants authored nécessaires et un niveau de finition suffisant pour juger la proposition comme un objet réel plutôt qu’un wireframe générique. Les détails sans rôle produit restent exclus. Lorsque la direction est nouvelle, ambiguë ou exposée à la convergence générique, le sourcing Web ou documentaire est recommandé ; s’il soutient un claim, une tendance, une provenance ou une décision non fondée en mémoire, il devient une ancre à ouvrir, dater, borner et transformer.

**Sortie.** Paquet `DIRECTION` d’`ACTION/CLOSE-PACKAGE`. En trace légère (`ACTION/HANDOFF`), la réponse visible et la trace légère en tiennent lieu. Pour chaque ancrage mobilisé, distinguer si nécessaire son rôle de direction, de production ou de vérification, les attributs retenus et rejetés, la transformation effectuée et les limites de transfert ; une référence Web n’est ni une preuve de réussite, ni une autorisation de copie.

**Clôture.** En trace complète, passer à `DECIDED`, puis `CLOSED` lorsque l’artefact et la trace sont persistés : `CLOSED` ne dit pas que la direction est tenue (`ACTION/STATUS`). Le résultat se déclare à part : une direction tenue, preuves applicables déclarées, peut recevoir un verdict accepté ; sinon, l’issue est `RETURNED`, `EXPLORATORY`, `FAIL-ASSUMED` (échec connu) ou `ESCALATED`, avec le verdict `RETURN-DIRECTION` si la direction doit être reprise, selon la preuve et le risque.

### `ACTION/RUN-SYSTEM`

**Entrée.** Règle, token, composant, convention, dépendance ou format partagé affecté.

**Faire.** Cartographier l’impact et les consumers. Nommer la décision, l’owner, la migration, le rollback et les tests de non-régression. Consulter `CHANGELOG.md` avant adoption, pilotage ou dépréciation.

**Sortie.** Paquet `SYSTÈME` d’`ACTION/CLOSE-PACKAGE`. Trace légère : la proposition (`ACTION/HANDOFF`). Dans une `RUN_CARD` acceptée, ces éléments forment `closure.system_package` : impact, consumers, owner, migration, rollback, non-régression (claim et baseline : locator, version, état) et référence CHANGELOG.

**Clôture.** En trace complète, passer à `DECIDED`, puis `CLOSED` lorsque consumers et réserves sont traçables. Passer à `ESCALATED` si owner, droit, décision externe ou risque externe manque.

---

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

## ACTION/PIPELINE-DIRECTION — direction vérifiable

Ce pipeline s’applique au mode `DIRECTION`. Il vise une direction réellement choisie, non un catalogue de variantes.

`DIRECTION/DOUBLE-LOOP` décrit la boucle d’édition, seule description de la boucle (copiée dans le noyau). `ACTION/PIPELINE-DIRECTION` décrit son exécution livrable : préparer, construire, produire la preuve, appliquer les corrections, comparer et clôturer ou retourner. `ACTION/GATE-B/B1b` est un contrôle spécialisé déclenché dans ce pipeline lorsque son scope est actif ; ces trois niveaux ne sont pas trois boucles concurrentes.

### Boucle de qualité et branche one-shot

Pour tout run qui produit un rendu, la boucle est celle de `DIRECTION/DOUBLE-LOOP` ; ce pipeline en exécute la préparation, la preuve, puis la clôture ou le retour. Observe le rendu réel sans te laisser guider par la rationale.

La branche `one-shot` est une exécution raccourcie de cette même boucle, jamais une suppression de la boucle. Elle permet de clôturer après l’observation initiale lorsque le premier rendu atteint la qualité attendue du mode, que la direction est identifiable, que les risques applicables sont couverts et qu’aucune amélioration utile n’est probable. Si le premier rendu est faible, générique ou incomplet, la branche one-shot ne s’applique pas : corrige, retourne ou déclare honnêtement la limite. Sur une surface `DIRECTION` acceptée avec V positif, l’arrêt suppose `ACTION/GATE-B/B1b` fait ou l’un de ses deux motifs `N/A-JUSTIFIED` ; la comparaison peut confirmer la décision initiale (`confirmed`). En trace légère, la proposition reste `EXPLORATORY` et B1b ne s’applique pas.

### 1. Situer les positions

Lorsque la décision est ouverte, formule des positions distinctes sur les axes pertinents : structure, matière, voix, temporalité, densité, rapport texte/image, rythme ou émotion traduite en levier visuel.

Il n’existe aucun quota obligatoire de directions. Une position retenue et une alternative située suffisent lorsque le risque dominant et les tensions sont déjà clairs.

La projection `creative_direction_set` de `schemas/production_contracts.schema.json` est conditionnelle : elle décrit une comparaison lorsqu’une décision ouverte et une alternative plausible la rendent utile. Si elle est produite, au moins deux positions distinctes matérialisent cette comparaison ; aucun plafond de directions n’est imposé. Ce minimum de structure du contrat ne demande ni variantes ni builds supplémentaires aux autres runs. Les qualités prioritaires de CREATIVE-BOOT sont un foyer de construction distinct du nombre de positions.

### 2. Traduire l’émotion

Une émotion n’est une direction que lorsqu’elle change une décision visible : composition, contraste, densité, échelle typographique, rythme de motion, contenu, relation texte/image ou traitement matériel.

« Premium », « chaleureux » ou « dynamique » sont des intentions à traduire, non des options de design autonomes.

### 3. Développer une alternative située

Le déclenchement appartient à `DIRECTION` (« Direction divergente ») et les leviers à `SAVOIR/CRAFT/CFT-02`. En trace complète, avant le build, la trace du run (retrouvable par `trace_locator`) nomme la position retenue, l’alternative considérée, la raison de son niveau de matérialisation et la preuve attendue ; la projection JSON ne porte pas ce paquet (voir `ACTION/RUN_CARD`). En trace légère, la première proposition nomme l’alternative écartée (checkpoint, étape 7).

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
**La première proposition vaut checkpoint.** Construis la première scène, puis présente-la avec sa thèse, l’alternative écartée et ce qu’il faut décider ; la personne valide, réoriente ou arrête. Valider oriente la suite (affiner, décliner, préparer la vraie version) ; ce n’est pas une acceptation. Pour retenir la direction pour un produit réel, la personne le demande : le run passe en trace complète, avec ancre observée ou fournie, gates et verdict (absolu 2 de `DIRECTION`). Jusque-là, la proposition reste `EXPLORATORY`. Un checkpoint avant le build n’est requis que si la personne l’a demandé ou si le build engage une action irréversible ou coûteuse (publier, envoyer, payer, consommer des crédits, écraser un existant, engager l’owner). Une marque, un public ou une hypothèse nouvelle est nommée dans la proposition ; elle ne bloque pas le build.
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

---

## ACTION/STRUCTURED-PROOF — contrats de décision et leur preuve

Ces artefacts rendent les décisions inspectables. Chacun n’est dû que si son déclencheur est actif ; sinon il est `N/A-JUSTIFIED`, avec sa raison. Zéro contrat est valide lorsqu’aucun déclencheur n’est actif : aucun fichier `production_contracts` n’est alors produit ; un fichier présent en porte au moins un.

| Contrat | Déclencheur |
|---|---|
| Carte de hiérarchie | `STANDARD` ou `DIRECTION` ; tout run dont la hiérarchie peut changer la décision |
| Preuve U structurée | U dominant |
| Partition typographique | Famille, registre, langue, données ou hiérarchie typographique pouvant changer la décision |
| Fiche d’asset directeur | Asset ou absence d’asset portant une décision perceptible (`DIRECTION/VISUAL_TARGET`) |
| Contrat de composant partagé | Pattern réutilisable, composant critique ou partagé : défini dans `BIBLIOTHEQUE/COMPONENTS` |
| Motion ou scène spatiale | Motion non triviale, animation interactive, scène 3D |
| `CREATIVE_DIRECTION_SET` | `DIRECTION` à décision ouverte avec alternative plausible |
| `UI_UX_REALITY_PACK` | Surface UI/UX nouvelle ou substantiellement modifiée (`ACTION/UI-UX-REALITY`) |
| `EVALUATION_CASE` | Pilote ou série de runs (`ACTION/CLOSE-EXIT-CHECK`, mesure expérimentale) |

**Règle de phase.** Les lignes de preuve sont marquées « après observation ». Avant build, elles restent vides ou `NOT-VERIFIED`, jamais préremplies par l’attendu. Après build, la cible est conservée et l’observation s’ajoute à côté.

### Carte de hiérarchie

- **Public prioritaire :**
- **Contexte et tâche dominante :**
- **Contenu primaire :**
- **Action critique :**
- **Contenu secondaire :**
- **Contenu à la demande :**
- **Risque de mauvaise lecture :**
- **Signal visuel prévu :**
- **Preuve U attendue :**

Lorsque U est dominant, la preuve U attendue peut être structurée ainsi :

```text
USER / PROFILE
TASK
CONTEXT
SUCCESS-CRITERION
OBSERVATION / MEASURE — après observation
SATISFACTION-OR-QUALITATIVE-RETURN — après observation
LIMIT — après observation
NEXT-PROOF — après observation
```

Une capture ou une inspection experte peut formuler un risque U ; elle ne doit pas être nommée test d’utilisabilité si aucune tâche représentative n’a été exécutée avec un utilisateur ou un profil concerné.

### Partition typographique

La partition est requise lorsque famille, registre, langue, données ou hiérarchie typographique peuvent changer la décision ; licence, glyphes nécessaires et coût de chargement sont vérifiés selon `SAVOIR/TYPE`. Sinon, le système existant et la raison de sa conservation suffisent.

| Rôle | Fonction | Famille / registre | Mesure / interligne | Poids / axe | Contextes | Fallback | Justification |
|---|---|---|---|---|---|---|---|
| Fonctionnel | Corps, lecture longue |  |  |  |  |  |  |
| Éditorial | Titre, rythme, angle |  |  |  |  |  |  |
| Microcopie | Labels, métadonnées, actions |  |  |  |  |  |  |
| Donnée | Chiffres, tableaux, comparaisons |  |  |  |  |  |  |
| Signature | Usage expressif limité, si nécessaire |  |  |  |  |  |  |

La partition vérifie aussi reflow, zoom et ajustements d’espacement utilisateur : aucun rôle critique ne doit être tronqué, recouvert ou rendu illisible lorsque ces conditions sont dans le périmètre.

### Fiche d’asset directeur

- **ID et rôle dans la promesse :**
- **Route de production et statut :** `CODE-NATIVE`, `FOURNI`, `CURATÉ`, `GÉNÉRÉ-DIRIGÉ` ou `HYBRIDE` ; image, illustration, SVG, vidéo, Rive, 3D ou absence intentionnelle.
- **Raison et alternative refusée :** quelle relation devient plus lisible, crédible ou singulière avec cette route ?
- **Source, disponibilité et droits :** locator et version du fichier, pack ou bibliothèque retenus ; moyen réellement accessible et constat qui l’établit ; licence documentée, autorisation requise ou inconnu. Une ressource citée n’est pas présumée connectée.
- **Provenance et transformations :** origine, créateur, génération ou édition connue.
- **Usage et intégration :** informatif, décoratif ou mixte ; relation au type, cadrage, grade, masque, composition ou donnée ; modification précise à effectuer dans l’artefact et effet attendu ; alt, description longue ou justification décorative.
- **Desktop et mobile :** ratio, crop, focal point, zone sûre, suppression ou alternative.
- **Format, poids cible, fallback, mouvement et reduced motion :**
- **Preuve V/U/A/T (après observation) et contre-indication :** observation capable de confirmer, remplacer ou retirer la ressource ; scope, limite et réexamen après changement du fichier, du contenu voisin, du support ou des droits.

La fiche rapproche les moyens et l’intervention dans la trace existante ; elle n’ajoute aucun champ RUN_CARD. Pour un composant, rattache ces informations au contrat existant de `BIBLIOTHEQUE/COMPONENTS` ; le comportement fiable de la primitive reste distinct de la contribution expressive de son habillage.

<!-- concept:HON-08 -->
La provenance informe l’origine ; elle ne constitue pas une autorisation de réemploi. Un droit inconnu (`rights_status` : `unknown`) interdit `ACCEPTED` ; `ACCEPTED-WITH-RESERVATION` reste possible avec une réserve structurée dont le scope couvre les droits et dont la condition de sortie est leur clearance, et la diffusion attend cette clearance. Un droit non autorisé déclenche `RETURNED`, `ESCALATED` ou le statut prévu par le contexte avant diffusion. La machine ne contrôle cette exclusion que pour une `RUN_CARD` `DIRECTION`, où `artifact.rights_status` est requis ; dans les autres modes, comme pour la réserve sur les droits, le contrôle reste à la trace.

### Contrat de composant et baseline

Pour un nouveau pattern réutilisable, un composant critique ou un composant partagé, le contrat de structure est défini par `BIBLIOTHEQUE/COMPONENTS` (contrat de composant partagé). ACTION en garde la baseline comme preuve, la migration et le verdict.

Une baseline visuelle est une image versionnée d’un état réel. Elle signale un écart ; elle ne produit pas automatiquement un `PASS`. Dans un paquet SYSTÈME, la baseline de non-régression est `system_package.non_regression.baseline` : locator, version et état.

Une différence est une régression seulement si elle s’écarte de l’intention, du comportement attendu ou du contrat de compatibilité. Une différence intentionnelle doit être reliée à une décision et à une preuve ; elle ne doit pas être supprimée comme régression visuelle par défaut.

Toute différence est revue contre l’intention, l’usage, l’accessibilité et le risque de régression.

### Contrat de motion ou scène spatiale

Toute motion non triviale, animation interactive ou scène 3D porte : rôle utilisateur ou narratif, état initial, déclencheurs, transitions, interruptions, clavier/tactile, reduced motion, fallback statique, performance, contenu alternatif, capture de référence et contre-indication.

Un effet qui ne produit ni feedback, ni information, ni relation spatiale ni décision de direction est candidat à la suppression.

---

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

<!-- concept:HON-07 -->
Une capture prouve le rendu, pas l’indépendance du jugement, l’accessibilité complète ou la réussite d’une tâche. Un regard humain ou externe prouve un avis situé, pas une mesure technique. Un asset généré est une ancre possible, jamais une preuve de rendu.

---

## ACTION/GATE-A — plancher objectivable

Gate A vérifie les fautes mesurables ou observables. Exécute uniquement les contrôles applicables au composant, à l’appareil et au contexte.

### Contrat de portée

Lorsque l’accessibilité ou la conformité est dans le périmètre, déclare avant le contrôle :

```text
MEDIUM — médium réel de la surface et périmètre effectivement observé ; déclare le support applicable. Pour le Web, le médium peut rester implicite seulement si le périmètre est sans ambiguïté ; pour tout autre médium, il est explicite.
SCOPE — vues, composants, états ou chemins couverts.
CONFORMANCE-TARGET — référentiel et niveau visé, adapté au médium déclaré.
SAMPLE — échantillon représentatif ou raison de l’exhaustivité.
METHOD — AUTOMATED, MANUAL, EXPERT, USER ou combinaison, adaptée au médium.
BUDGET-UNIT — unité de budget pertinente : load/INP, lancement/frame rate/mémoire, confort motion, encre/contraste ou équivalent déclaré.
COVERAGE-LIMIT — éléments hors couverture, incluant toute preuve web indisponible.
NEXT-PROOF — preuve suivante attendue.
```

Pour le web, utilise WCAG 2.2 comme base normative actuelle lorsque le projet n’impose pas un autre référentiel applicable. Pour un autre médium, déclare le référentiel applicable dans `CONFORMANCE-TARGET` : guideline de plateforme, référentiel légal, standard émergent ou critère de lisibilité pertinent. WCAG 3.0 reste une `[VEILLE]` tant que sa recommandation et son modèle de conformance ne sont pas stabilisés. Les critères de conformité ne valident ni la direction visuelle, ni l’utilisabilité globale, ni l’adéquation du positionnement.

### Familles de méthodes

| Méthode | Couvre prioritairement | Limite |
|---|---|---|
| `AUTOMATED` | Défauts détectables par outil et règles codées. | Ne couvre pas tous les problèmes d’usage, de contexte ou d’interprétation. |
| `MANUAL` | Structure, clavier, focus, états et situations que l’outil ne comprend pas. | Dépend de la méthode et de l’expertise de l’inspecteur. |
| `EXPERT` | Interprétation, risque, cohérence et problèmes contextuels. | Ne remplace pas une tâche utilisateur. |
| `USER` | Expérience réelle et difficultés de personnes concernées. | Échantillon, tâche et contexte doivent être déclarés. |

Un `PASS` décrit la preuve obtenue par la méthode, le médium et le périmètre déclarés. Il ne devient pas un `PASS` global par glissement. Ce qui n’existe pas dans le médium est `N/A-JUSTIFIED` ; ce qui le remplace est testé. Une preuve web indisponible n’est jamais simulée : elle devient `NOT-VERIFIED` avec `NEXT-PROOF`, ou est traduite en équivalent du médium.

Pour un verdict global `ACCEPTED` ou `ACCEPTED-WITH-RESERVATION`, la `RUN_CARD` doit rattacher la preuve observée à une provenance minimale : `artifact_locator`, `artifact_version`, `method` et `observed_at`. Cette provenance établit où, sur quelle version, par quelle méthode et à quel moment l’observation a été obtenue ; elle ne prouve pas à elle seule la véracité de l’artefact, la qualité du design ou la réussite d’usage. Si la provenance ne peut pas être établie, le verdict reste non accepté.

### Adéquation des preuves

| Question | Preuve adaptée | Limite |
|---|---|---|
| Ratio, taille, token, régression mesurable | Script ou test exécuté. | Ne prouve pas l’intention visuelle. |
| Hiérarchie, composition, densité, matière | Capture, détail et comparaison. | Ne crée pas seul un juge indépendant. |
| Préférence, clarté, fidélité au contexte | Regard humain, expert ou utilisateur selon le risque. | N’est pas une mesure technique par défaut. |
| Utilisabilité réelle | Utilisateur représentatif, tâche représentative, observation et résultat. | Ne se déduit pas d’une capture ou d’un avis expert seul. |
| Hypothèse sans runtime ou observateur | Déclaration structurée. | Reste `NOT-VERIFIED` si la preuve est requise. |

### Contrôles applicables

| Contrôle | `PASS` si… | Retour ou réserve si… |
|---|---|---|
| Contraste | Les cas représentatifs sont calculés selon la politique WCAG 2.2 AA du projet lorsqu’elle s’applique. | Estimé à l’œil, sous seuil ou non calculé lorsque requis. |
| Sémantique et nom accessible | Interactifs et contenus essentiels ont une sémantique et un nom adaptés. | Rôle, nom, structure ou alternative absents. |
| Focus clavier | Interactifs atteignables avec focus visible et testé. | Navigation ou focus indisponible. |
| États pertinents | Interaction, sélection, contenu et erreurs sont vérifiés ; événement, conséquence et action suivante sont explicites. | État critique absent, implicite ou dépendant de la couleur seule. |
| Contenu honnête | Pas de faux contenu, lorem ou promesse non étayée présenté comme réel. | Contenu de remplissage trompeur. |
| Stabilité média | Dimensions, fallback et chargement évitent les déplacements pertinents. | Instabilité visible ou espace non réservé. |
| Motion réduite | L’alternative sans mouvement est implémentée et vérifiée préférence activée, dans le runtime déclaré. Sans motion : `N/A-JUSTIFIED`. | Motion imposée ou alternative absente ; alternative seulement dessinée ou annoncée : `NOT-VERIFIED`. |
| Cibles d’interaction | Taille adaptée au device et au contexte selon la politique du projet. | Cible trop petite sans alternative ni justification. |
| Information non chromatique | L’information essentielle ne dépend pas de la couleur seule. | Statut ou action incompréhensible sans couleur. |
| Focus non masqué | Le composant recevant le focus reste visible selon le contexte applicable. | Focus masqué par contenu ou interface auteur. |
| Mouvement de glisser | Une alternative existe lorsque l’action de glisser n’est pas essentielle. | Action impossible autrement sans justification. |
| Aide cohérente | L’aide répétée apparaît de façon cohérente lorsque le produit en fournit. | Aide déplacée ou incohérente dans le périmètre. |
| Saisie redondante | L’utilisateur ne doit pas ressaisir inutilement une information déjà fournie dans le même processus. | Répétition évitable sans raison. |
| Authentification accessible | Le processus n’impose pas une charge cognitive ou sensorielle évitable. | Mémoire, perception ou interaction imposée sans alternative. |

<!-- concept:GTA-01 -->
**Profils de surface.** Commence par les contrôles d’office du profil ; un contrôle hors profil devient applicable dès que la surface porte l’élément concerné (formulaire, glisser, motion, connexion). Ce que le médium ne porte pas est `N/A-JUSTIFIED`.

| Profil | Contrôles d’office | Selon le contenu |
|---|---|---|
| Page vitrine, éditoriale ou portfolio | Contraste, sémantique et nom accessible, focus clavier, information non chromatique, cibles d’interaction, contenu honnête, stabilité média. | États (formulaire, commande), motion réduite, mouvement de glisser, focus non masqué. |
| Application, formulaire ou flow | Tous les contrôles d’interface : contraste, sémantique, focus clavier et non masqué, états, cibles, information non chromatique, saisie redondante, aide cohérente, contenu honnête. | Authentification accessible (connexion), motion réduite, mouvement de glisser, stabilité média. |
| Scène, motion ou 3D | Motion réduite, contraste, information non chromatique, stabilité média, contenu honnête. | Focus clavier et cibles si la scène est interactive. |
| Hors Web (imprimé, affiche, écran fixe) | Contraste ou lisibilité d’encre, information non chromatique, contenu honnête. | Référentiel du médium, déclaré dans `CONFORMANCE-TARGET`. |

Les scripts et recettes sont des ressources versionnées. Une recette exécutée ne suffit pas à valider un résultat visuel, produit ou utilisateur. La recette `AUTOMATED` du paquet pour un rendu HTML est `scripts/check_render.py` (optionnelle, navigateur requis) : elle contrôle le débordement (de la page et des feuilles ouvertes), les erreurs de script, le contraste sur fond uni opaque, les candidats de nom tirés du DOM, la taille des cibles (exception d’espacement comprise), les arrêts clavier observés et leur changement de style au focus, la structure du document et le mouvement réduit, et produit la provenance minimale ci-dessus. Une opacité de groupe, une couleur non convertible, un fond en dégradé ou un texte SVG non mesuré deviennent une réserve, jamais `PASS`. Le candidat DOM exclut le contenu masqué ordinaire et peut utiliser les labels explicitement référencés ; sa présence ne prouve pas le nom accessible calculé et conserve une réserve. Un cas de nom non couvert conserve également une réserve. Le parcours clavier indique le périmètre actif, les candidats non atteints et la raison d’arrêt ; la borne atteinte ou une couverture inconnue conserve une réserve. Un changement de style ne prouve ni visibilité, ni contraste, ni absence de masquage du focus. Ces limites n’allègent pas les contrôles applicables du gate : approfondis la preuve si nécessaire. Sans navigateur, la recette rend `NOT-VERIFIED`. Ses comportements sont testés par `scripts/test_check_render.py` ; `--require-browser` exige les tests de pages et fait échouer leur contrôle si le navigateur est indisponible.

**Résoudre un contraste non évalué.** Pour le texte SVG, relève dans l’état et aux largeurs concernés la couleur peinte (`fill` ou `stroke`), les opacités et le fond réellement placé derrière les glyphes ; la propriété CSS `color` et le fond d’un ancêtre ne suffisent pas. Calcule le rapport sur les couleurs effectives selon les seuils de cette gate et `SAVOIR/CRAFT/CFT-05`. Sur une image, un dégradé ou des formes superposées, identifie les positions les plus défavorables dans le rendu ; une capture seule ne mesure pas le rapport. Relie le relevé, le calcul, la méthode, l’artefact, l’état, le viewport et la limite dans la preuve existante. L’agent peut produire cette mesure avec un outil adapté ; si les couleurs effectives ne sont pas établies, conserve la réserve et nomme la mesure suivante. Une preuve complémentaire résout la réserve dans le run sans modifier rétroactivement le résultat de la recette.


**Couverture de la recette.** Le contraste enregistre candidats, évaluations, exclusions et textes détectés hors couverture dans `contrast_coverage`. Valeur courante, placeholder affiché, texte natif et contenu pseudo détectés mais non calculés conservent une réserve ; une absence de mesure ne devient pas une preuve de conformité. Vérifie séparément leur couleur réellement peinte, leur fond et leur état, notamment `::placeholder`, sans publier les valeurs sensibles. Un défaut calculé ailleurs conserve `RETURN`. Ces données appartiennent à la recette, pas au schéma RUN_CARD.

Avec `--proof`, `proof_observations` sépare présence, surface, opacité CSS cumulée et intersection du rectangle avec les deux axes du viewport initial. Introuvable, masqué ou transparent : `RETURN`. Une intersection insuffisante — moins de `min(40 % de la dimension, 320 px)` sur un axe — ou une découpe non évaluée conserve une réserve : la recomposition reste à juger. Un `PASS` porte uniquement sur ces observations CSS et géométriques ; pixels, occlusion et pertinence de l’objet restent à inspecter. Une ancienne mesure sans couverture ne suffit pas.
---

## ACTION/GATE-B — jugement contextualisé et risques

Gate B compare, observe et explique les risques restants. Il ne produit pas une moyenne décorative.

### B1 — Comparaison relationnelle

En `DIRECTION`, compare le build à l’ancre utile sur les axes réellement concernés. En `STANDARD`, utilise une ancre seulement lorsqu’une direction locale, une matière, une composition ou une comparaison perceptuelle le justifie.

Pose des questions relationnelles : quel résultat conduit mieux à l’action critique, rend le rythme plus lisible, porte mieux l’intention ou maintient mieux la singularité du produit ?

Une différence significative sur un axe dominant déclenche une correction, un écart assumé ou une justification de non-transfert. Aucun nombre fixe de comparaisons ne constitue une condition de `PASS`.

### B1b — Discrimination sur capture, requise dans son scope

`B1b` est **requis par module** sur toute surface `DIRECTION` qui accepte (`ACCEPTED` ou `ACCEPTED-WITH-RESERVATION`) avec l’axe V en `PASS` ou `PASS-WITH-RESERVATION` : un V positif n’y est pas accordé sans une décision principale confrontée à une variante, ou sans l’un des deux motifs `N/A-JUSTIFIED` admis ci-dessous. Avant la clôture, il est déclenché dès que le risque V/craft est dominant dans la ligne de run ou que le verdict V visé repose sur une intention, une composition, une matière ou un traitement qui n’a pas encore été confronté à une variante. Le déclencheur porte sur le risque, la décision et le verdict déclarés ; il ne dépend pas de l’affirmation qu’une comparaison « ne changerait rien ».

La preuve minimale est une paire de captures réelles : une capture initiale, puis une capture après l’édition réversible d’une seule décision principale. La variable doit être observable : masse, vide, silhouette, lumière, densité, cohérence de rayon, définition d’état, crop, vocabulaire, preuve, couleur ou action.

#### Atelier d’édition — opération observable

<!-- noyau:début BOUCLE-ATELIER -->
Dans le scope de B1b (surface `DIRECTION` qui accepte avec l’axe V positif, en trace complète : `ACTION/GATE-B/B1b`), cet atelier est requis, sauf deux motifs `N/A-JUSTIFIED` : aucune décision principale éditable, ou une paire équivalente encore valide qui couvre la même décision. Hors de ce scope, il ne s’impose pas.

Après la première capture, effectuer une lecture légère en ignorant le texte explicatif et nommer en une phrase la catégorie, la marque et le niveau de preuve que la surface semble raconter. Nommer ensuite la décision principale qui sera mise à l’épreuve. Éditer cette décision par **retrait, réduction ou transformation** ; une décision peut coordonner plusieurs diffs, mais l’unité de compte n’est pas le nombre de changements. Ne rien ajouter pour compenser.

Conserver et comparer la capture suivante. La trace nomme le changement, sa direction, son effet et la décision qu’il confirme, modifie ou abandonne. Conserver l’original lorsqu’il résout mieux la décision est un résultat valide : la variante a alors confirmé une décision par comparaison plutôt que par déclaration.
<!-- noyau:fin BOUCLE-ATELIER -->

`N/A-JUSTIFIED` n’est recevable que si aucune décision principale éditable n’existe dans le périmètre, ou si une paire équivalente, toujours valide après le dernier changement substantiel, couvre déjà exactement la même décision. La justification lie l’artefact concerné, l’owner et la prochaine preuve. Une thèse encore incertaine, un élément producteur introuvable ou une paire qui n’autorise aucune conclusion maintiennent le run en `EXPLORATORY` ; ils ne produisent pas un `PASS` indirect.

Dans une `RUN_CARD`, B1b est `closure.b1b`. Statut `DONE` : `pair` avec `before_locator` et `after_locator` (deux captures distinctes), `decision` et `outcome` (`confirmed`, `modified` ou `abandoned` ; `modified` correspond à `CHANGED` de `decision_change`). Statut `N/A-JUSTIFIED` : `reason` prend l’une des deux seules valeurs admises, `no_editable_decision` ou `equivalent_pair_valid` (avec `pair_ref`), plus `covered_decision`, `owner` et `next_proof`. Le validateur exige `closure.b1b` pour une surface `DIRECTION` acceptée avec V en `PASS` ou `PASS-WITH-RESERVATION` ; il ne vérifie pas que la décision couverte par une paire équivalente est bien la même.

B1b n’est ni un sixième absolu, ni un score esthétique, ni un quota universel. Hors de son scope, il ne s’applique pas. Dans son scope, il ne peut être omis sans la sortie matérielle ci-dessus.

Si l’équipe accepte consciemment l’écart narratif entre la thèse déclarée et le récit implicite de la capture, ne crée pas une nouvelle `ISSUE`. Utilise le statut de direction `HELD-WITH-ACCEPTED-DIFFERENCE` et, lorsque le périmètre permet la clôture, le verdict global `ACCEPTED-WITH-RESERVATION`. La trace doit nommer : `NARRATIVE-DIFFERENCE`, `REASON`, `PRODUCT-OR-PUBLIC-CONSTRAINT`, `OWNER`, `NEXT-PROOF` et `EXIT-CONDITION`. Cette issue n’est acceptable que si l’écart est explicite, assumé, compatible avec U/A/T et révisable ; elle ne convertit pas une preuve manquante en acceptation.

En l’absence de regard indépendant, déclarer cette limite selon B3. Une B1b menée par l’auteur du rendu est une **auto-comparaison** : elle peut soutenir une correction de craft, mais ne satisfait jamais un claim de revue indépendante. Une décision identitaire importante qui requiert un contrepoint externe reste avec réserve ou prochaine preuve tant que ce regard n’existe pas.

### B2 — Familles de preuve

Ajoute une preuve de contexte lorsque le risque produit est dominant : source de l’hypothèse, niveau de confiance, coût d’erreur, owner et prochaine preuve. Une direction peut être visuellement tenue et néanmoins répondre au mauvais problème ; ce cas doit rester visible dans U et dans le risque restant.

| Famille | Axes | Preuves privilégiées | Sortie principale |
|---|---|---|---|
| Caractère et perception | Point de vue, hiérarchie, typo/contenu, craft/états, singularité/retenue. | Capture, paires, détail, regard externe. | V |
| Compréhension et produit | UX, architecture, action critique et contenu. | Carte de hiérarchie, scénario, états, test ou retour de tâche. | U |
| Système et robustesse | Couleur, accessibilité, responsive, dark, performance et motion. | Tokens, inspection, tests, capture responsive. | A/T |
| Gouvernance | Best-fit, limites, délégation et arbitrages. | Journal, recherche, compromis, escalade. | Réserve ou prochaine action |

Chaque axe jugé porte une observation factuelle. Une note sur cinq peut localiser un risque, mais aucune note globale ne remplace V/U/A/T. Une note sans observation est invalide.

### B3 — Regard externe

Un regard humain ou un autre évaluateur peut réduire l’auto-préférence. Une seconde session du même auteur est une auto-comparaison différée : elle n’est jamais un regard externe, indépendant ou aveugle. Documente la source, l’expertise ou le profil, l’artefact regardé et la limite du jugement. Une B1b exécutée par le même auteur est une auto-comparaison et ne doit jamais être étiquetée regard externe, indépendant ou aveugle.

Un regard externe fournit un contrepoint situé ; il ne garantit ni indépendance parfaite ni exhaustivité. Pour une décision importante, triangule selon le risque : plusieurs évaluateurs, plusieurs méthodes, ou inspection et observation utilisateur.

Si aucun regard externe n’est disponible, déclare l’absence, conserve la capture et la comparaison, et inscris la réserve ou la prochaine preuve. L’absence de regard indépendant ne devient jamais une validation implicite.

Lorsqu’un regard est présenté comme **indépendant**, **comparatif** ou **aveugle**, la trace conserve aussi :

```text
REVIEWER-ROLE
REVIEWER-RELATION — SAME-AUTHOR / INVOLVED-IN-RUN / UNINVOLVED-COLLABORATOR / EXTERNAL
RENDER-AUTHOR
CONFLICT — DECLARED / NONE-KNOWN
ARTEFACTS-REVIEWED
REVIEW-EXPOSURE — BLIND / CODE-EXPOSED / PROMPT-EXPOSED / MAPPING-EXPOSED / NOT-BLIND ; plusieurs expositions sont listées ensemble, sans être condensées en une valeur
MAPPING-TIMING — BEFORE / AFTER / NOT-APPLICABLE
LIMIT
```

Le label « indépendant » exige une relation `UNINVOLVED-COLLABORATOR` ou `EXTERNAL`, un reviewer qui n’est pas l’auteur du rendu, et aucun conflit déclaré. Sinon, le regard est nommé selon sa relation réelle.

Une revue non aveugle reste une preuve située utile si son exposition est déclarée. Elle ne reçoit pas le poids d’une passe aveugle. Une divulgation du mapping après l’avis peut enrichir la passe d’interprétation, mais ne réécrit pas le jugement initial.

### B4 — Corrections ancrées

Une correction de direction répond à un écart ou une critique observable. Retourne à la divergence, à l’ancre, à la spec ou au build lorsque l’écart dominant persiste, lorsque la preuve manque ou lorsque la correction locale dénature le produit.

Aucun nombre fixe d’itérations ne constitue une règle de qualité. Le run s’arrête lorsque la direction est tenue, l’écart est explicitement assumé, la preuve est impossible et statuée, ou le périmètre doit être reclassifié.

### B5 — Trace d’assets et statut de direction

Avant le verdict d’une surface `DIRECTION`, conserve dans la trace locale les éléments utiles : capacités vérifiées, ancre et références observées, attributs retenus/rejetés, direction, écarts, réserves et statut.

Si un asset est directeur, la trace relie aussi sa route de production, sa raison, son droit ou son incertitude, son traitement et l’observation de son intégration au rendu réel. Un asset techniquement disponible mais faible dans son crop final, hors récit, ou seulement « joli » reste un écart de direction, pas une preuve de finition.

### B6 — Format de sortie compact

Livre d’abord l’artefact ou le lien. Ensuite, expose le verdict adapté au mode : une ligne en `LITE`, quelques lignes en `ITER` ou `STANDARD`, et un bloc direction + risques en `DIRECTION`.

Les paires, logs, preuves et diffs vivent dans un artefact associé ou la `RUN_CARD`. Ne répète pas les mêmes valeurs en prose et en structure.

---

## ACTION/GATE-C — craft sur rendu réel

Gate C évalue la présence de décisions perceptibles et la qualité de leur résolution. Il est obligatoire en `DIRECTION`, ciblé au risque craft en `STANDARD`, limité à la zone touchée en `ITER` et `N/A-JUSTIFIED` en `LITE` lorsque le craft n’est pas concerné.

Une capture réelle est nécessaire pour un jugement C. Sans runtime ou capture, le craft reste `NOT-VERIFIED`.

Gate C décide sur le rendu à partir des observations de la revue créative et, si elle est déclenchée, de la paire B1b (`ACTION/GATE-B — B1b`) pour la décision mise à l’épreuve ; il ne refait pas une seconde revue, ni une seconde procédure de comparaison.

Chaque verdict C précise le périmètre : viewport, état, scène, contenu et élément observé. Pour une finesse insuffisante, utilise les gestes conditionnels de `SAVOIR/STATE`, puis compare les versions au même scope ; une cohérence déclarée ou un geste seulement prévu ne prouve pas la résolution. Lorsque la structure est ouverte, applique sur la même capture les tests perceptifs de `BIBLIOTHEQUE/GATE` (non-généricité, silhouette, grille) ; ils nourrissent C3 et C4 sans verdict propre.

| Critère | Présent si… | Retour ou réserve si… | Geste si absent (noyau, §) |
|---|---|---|---|
| **C1 — Stratégie de surface** | Photo, donnée, lumière, illustration, surface, trame, profondeur ou planéité assumée découle du produit. | Traitement par défaut sans relation observable. | Choisis la surface d’après ce que le produit montre (carte des moyens, §6) ; un traitement justifié par la thèse pour les assets moyens ; retire le traitement sans rôle. |
| **C2 — Typographie choisie** | Famille, système existant ou alternative est justifié ; rôles, échelle et fallback servent le contexte. | Choix par défaut non interrogé ou non calibré. | Choisis la famille pour la voix et la donnée à porter (§6) ; fixe deux ou trois rôles et une échelle contrastée ; vérifie le fallback au rendu. |
| **C3 — Composition intentionnelle** | Structure de lecture identifiable sert l’action et le rythme. | Empilement uniforme sans décision spatiale. | Recompose dans l’ordre intention → foyer → masse → rythme (§5) ; nomme le foyer et l’ordre de lecture ; romps la trame modale si elle ne sert pas la tâche (§4). |
| **C4 — Densité optique** | Espace, masses et regroupements suivent la priorité et l’usage. | Espacement uniforme qui masque les relations. | Regroupe par proximité ; redistribue masses et vides selon la priorité (masse visuelle, gestion du vide, §5) ; contrôle la silhouette à faible détail. |
| **C5 — Stratégie de profondeur applicable** | Profondeur, lumière ou planéité est cohérente avec le registre et lisible au rendu. | Ombres, bordures ou flous par défaut sans logique. `N/A-JUSTIFIED` si la planéité est intentionnelle et suffisante. | Tiens une seule logique, lumière, élévation ou planéité, sur toute la surface ; retire ombres, bordures et flous sans rôle (surface, §5). |
| **C6 — Résolution située** | Une difficulté réelle est résolue par microcopie, état, donnée, interaction, asset ou transition pertinente. | Assemblage de composants sans adaptation au cas. | Trouve la difficulté réelle du cas (attente, erreur, donnée, choix) et résous-la par microcopie, état, donnée ou interaction (forme située, §5) ; une erreur se résout jusqu’à la reprise (`SAVOIR/STATE`). |

Chaque verdict C cite l’élément concret observé. Un critère bloquant absent, ou plusieurs signaux faibles convergeant sur le même risque, déclenchent un retour. La correction revient à la direction, à la spec ou au build ; elle n’ajoute pas un effet décoratif terminal.

En trace légère, Gate C sert de contrôle de craft sur la capture, dans la boucle d’édition : un critère absent déclenche son geste, puis une nouvelle capture ; aucun verdict n’est écrit.

---

## ACTION/ANTI-SLOP — conséquence de gate

La matrice canonique motivation/construction appartient à `SAVOIR/CRAFT/CFT-01`. ACTION ne la reproduit pas : il vérifie sa conséquence sur l’artefact. Lorsqu’un motif manque de motivation, de construction ou des deux, la trace nomme l’élément observé, la relation produit/lecture manquante et la sortie : correction, retrait, réserve ou `RETURN`.

Une couleur de marque, une contrainte de contenu ou une construction technique soignée n’immunisent pas un choix contre les autres gates. Les watchlists et tendances restent des aides de jugement dans `SAVOIR/CRAFT` ou la veille ; elles ne deviennent pas des interdits universels.

---

## ACTION/OVERRIDE — FAIL-ASSUMED et péremption

### FAIL-ASSUMED

Un utilisateur peut demander une diffusion limitée malgré un échec connu lorsque le risque est documenté, assigné et re-testable. Le FAIL ne devient jamais un PASS.

Journalise :

> `FAIL-ASSUMED — [gate / axe] — [mesure ou preuve] — [date] — [risque] — [périmètre de diffusion] — [owner] — [condition de re-vérification].`

Toute exception conserve également :

```text
SCOPE
IMPACT
REVIEW-DATE
NEXT-PROOF
EXIT-CONDITION
```

Dans une `RUN_CARD`, l’exception est `closure.exception` : la structure de réserve de `ACTION/CLOSE-PACKAGE` (owner, scope, impact, date de revue, prochaine preuve, condition de sortie ; la date est celle de la carte), plus `gate_axis`, `failure_evidence` — un échec présent dans `proof.observed`, jamais un `NOT-VERIFIED` requalifié —, `requested_by` et `disposition` (`NON-DIFFUSÉ`, `DIFFUSÉ-LIMITÉ`, `RETIRÉ` ou `ESCALADÉ`). Si la protection critique du run a échoué, `FAIL-ASSUMED` n’est pas disponible sur ce risque : l’issue suit l’action déclarée par la protection.

Un `FAIL-ASSUMED` ne peut pas autoriser la mise en production d’un risque de sécurité, de dommage grave, de conformité critique ou de défaillance qui rend l’action essentielle trompeuse ou dangereuse. Ces cas passent en `ESCALATED` ou restent non livrables.

Les risques d’accessibilité, de sécurité ou de conformité à fort impact sont rappelés factuellement. Un `FAIL-ASSUMED` est re-présenté à la prochaine modification du même périmètre.

### Péremption

La péremption d’un claim, d’un outil, d’une watchlist ou d’une ressource déclenche une revue lorsque le livrable en dépend. La trace conserve type de claim ou de ressource, source, version, date de vérification, portée, limite, owner, date de revue et prochaine preuve.

La péremption ne bloque pas un fix sans rapport, mais ne peut pas être silencieusement reconduite lors d’une prochaine utilisation.

Une réserve périmée conserve owner, date de revue, impact, nouvelle preuve attendue et condition de clôture.

---

## ACTION/POLICIES — contraste et inspection

### Politique de contraste

Calcule le contraste selon WCAG 2.2 et le référentiel applicable lorsque ce référentiel s’applique au projet. Ne valide jamais le contraste à l’œil.

APCA peut être documenté comme mesure complémentaire de lisibilité ou d’exploration lorsque son contexte, sa version et sa limite sont connus. APCA ne remplace pas un critère WCAG applicable et ne crée pas seul un verdict réglementaire.

Les seuils, outils, projections réglementaires et sources évolutives sont qualifiés dans `SAVOIR/TOOLS` et la trace locale du run. ACTION porte la politique de livraison ; un fait ne mérite une décision de gouvernance que lorsqu’il devient une règle partagée.

### Inspection et ressources techniques

Une inspection externe peut compléter le jugement sur l’accessibilité, la régression visuelle, les tokens et les motifs. Choisis l’outil selon l’environnement, sa documentation, sa version et son owner. Une commande, un package ou une intégration cités dans une ressource ne sont jamais exécutés aveuglément. Trois cas :

- **script local sans dépendance nouvelle** : la trace conserve la méthode, la commande ou la version, et le résultat ;
- **outil déjà autorisé** : la trace cite la référence de l’autorisation ;
- **nouvelle dépendance** : approbation requise, et la ressource indique les sept champs ci-dessous.

Toute ressource technique maintenue indique :

- stack et version ;
- date de vérification ;
- capacité résolue ;
- fallback ;
- limites ;
- owner ;
- prochaine revue.

L’automatisation détecte une partie des défauts mesurables. Elle ne remplace ni l’inspection de rendu, ni la capture, ni le jugement contextuel, ni l’observation utilisateur lorsque le risque la requiert.

Pour les composants critiques, maintiens une baseline d’états pertinents : variant, thème, viewport, données longues, loading, empty, error et focus lorsque nécessaires. Une capture versionnée et une revue explicite peuvent fournir une preuve proportionnée lorsqu’un pipeline de stories ou de tests visuels n’existe pas.

---

## ACTION/ROUTING — prérequis de jugement et de structure

DIRECTION déclenche la classification générale. ACTION appelle ensuite les routes de `SAVOIR` et `BIBLIOTHEQUE` qui peuvent modifier la prochaine décision : elles s’ajoutent à la ligne du mode dans `DIRECTION/CHARGE` (colonne « Ajouter seulement si ») et ne forment pas une seconde liste.

| Situation | Routes ciblées |
|---|---|
| Spec `DIRECTION` | `SAVOIR/CRAFT`, `SAVOIR/TYPE` ou `SAVOIR/SOURCE` si la composition, la typographie ou l’ancrage restent ouverts, `SAVOIR/STYLE` si registre, `BIBLIOTHEQUE/SELECT` si structure ouverte. |
| Craft ou états | `SAVOIR/STATE`. |
| Couleur, contraste ou theming | `SAVOIR/CRAFT`, `SAVOIR/SYSTEM` et politique de contraste ACTION. |
| Risque critique, responsive, performance ou motion | `SAVOIR/CONTEXT`. |
| Technique ou compatibilité | `SAVOIR/TECH`. |
| Claim, outil ou tendance datée | `SAVOIR/TOOLS` et trace locale indiquant source, date, portée et limite. |
| Doute d’application ou théâtre procédural | `SAVOIR/INTEGRITY`. |
| Une famille de design peut modifier la prochaine décision | Section `DESIGN-ATLAS` de `SAVOIR.md`, puis seulement la route propriétaire utile. |
| Structure d’un écran | `BIBLIOTHEQUE/SELECT`, puis routes retenues. |
| Token, composant ou blast radius | `SAVOIR/SYSTEM` si une décision partagée change, `BIBLIOTHEQUE/COMPONENTS` si un composant change, `ACTION/RUN-SYSTEM` si partagé. |

Les anciennes références de section ne sont pas des routes quotidiennes. Leur migration est documentée dans `CHANGELOG.md`, et un nouveau run utilise uniquement les routes stables.

---

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
