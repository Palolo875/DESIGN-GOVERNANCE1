# Formes — choisir une structure

Lire une structure, diverger, sélectionner et dériver avant de composer.

<!-- origine:BIBLIOTHEQUE.md -->
## BIBLIOTHEQUE/READ — responsabilités et convention de route

La chaîne canonique est une carte de responsabilités, non une séquence obligatoire :

> **support → grille → scène → objet → primitive**

Une surface peut hériter d’un niveau ou n’en sélectionner aucun si aucune décision structurelle ne change. Le **support** définit le champ spatial dans lequel vit la surface. La **grille** organise la circulation, les axes, le rythme, le foyer et la hiérarchie dans ce champ. La **scène** définit le scénario de lecture et de preuve entre promesse, contenu, média et action. L’**objet** rend une preuve, un état ou une action locale tangible. La **primitive** porte le geste accessible et la sémantique de base.

Sur une page de plusieurs sections, la **séquence** ordonne les scènes, leur rythme et leur fin (`BIBLIOTHEQUE/SEQUENCE`). Cette chaîne décrit une responsabilité, pas un ordre de lecture rigide. Une micro-interface peut être le point de départ d’une surface dense. Un modificateur intervient seulement après la structure lorsqu’il change un comportement réel.

Une structure peut porter une scène naturelle, éditoriale, technique, tactile ou expressive ; elle ne se limite pas à un dashboard ou à une grille de cards. Lorsque la décision le justifie, l’objet visible peut être un composant authored : sa silhouette, son contenu, sa hiérarchie, sa matière et son comportement sont composés pour le produit. Cela ne rend pas les primitives critiques inhabituelles par obligation ; leur sémantique, leur accessibilité, leur feedback et leur comportement restent prioritaires.

### Lecture expressive de la structure

<!-- noyau:début STRUCT-EXPRESSION -->
Une structure ne choisit pas seule le goût, mais elle ouvre ou ferme des possibilités de présence. Lorsqu’une décision esthétique est active, décris aussi le caractère perceptuel que la structure doit favoriser : **calme ou tension, intimité ou monumentalité, précision ou spontanéité, continuité ou rupture, collection ou instrument, retenue ou intensité**. Ces termes ne sont pas des styles à appliquer ; ils doivent être traduits par des relations observables de masse, de rythme, de matière, de typographie, de lumière, de contenu ou de comportement.
<!-- noyau:fin STRUCT-EXPRESSION -->

Une sélection structurelle est créativement utile lorsqu’elle améliore au moins une relation entre le produit et le regard : foyer, cadence, révélation, profondeur, voisinage, contraste, mémoire, geste ou preuve. Une structure peut donc être retenue pour sa contribution perceptuelle, à condition de nommer la décision, la contre-indication et la condition de sortie. La beauté ne justifie pas une structure qui masque la tâche, mais la tâche n’épuise pas toute la valeur d’une structure lorsque la présence, la voix ou l’expérience du regard sont elles-mêmes des décisions du run.

### BIBLIOTHEQUE/TENSION — diverger avant de sélectionner

<!-- noyau:début STRUCT-TENSION -->
Lorsqu’une décision structurelle ou créative est ouverte, déclare un ou deux axes de tension observables avant de choisir une route. Ces axes ne sont ni des styles, ni des scores, ni des verdicts ; ils décrivent la relation que la composition doit rendre perceptible.

```text
DENSITY: respiration ↔ compression
FOCUS: unique ↔ distribué
PROOF-POSITION: intégrée ↔ latérale ↔ textuelle
TEMPORALITY: immédiate ↔ séquencée
FIELD-MATERIAL: plan ↔ image ↔ typographie
NAVIGATION: guidée ↔ exploratoire
ACTION: centrale ↔ contextuelle
```
<!-- noyau:fin STRUCT-TENSION -->

La route devient une conséquence de cette tension, de la tâche, du contenu réel, du mécanisme de preuve et du risque ; elle ne constitue pas la direction créative à elle seule. Une tension est retenue seulement si son pôle choisi change une décision d’espace, de hiérarchie, de comportement, de preuve ou de mémoire et peut être observé dans le premier objet. Si aucun axe ne peut modifier la prochaine décision, conserve l’héritage ou justifie `N/A-JUSTIFIED`.

La trace persiste `TENSION-AXES`, `SELECTED-POLE`, `DECISION-IMPACT`, `OWNER`, `SCOPE`, `NEXT-OBSERVATION` et `EXIT-CONDITION`. Pour un axe à trois pôles comme `PROOF-POSITION`, le pôle retenu et sa conséquence doivent être explicites. Une absence de tension structurelle relève d’un héritage ou d’un cas documentaire ; elle ne devient `N/A-JUSTIFIED` que si un contrôle ou une preuve est réellement non applicable selon ACTION.

### BIBLIOTHEQUE/SIGNATURE — rendre l’écart vérifiable

Toute sélection ouverte en mode `DIRECTION`, ou toute dérivation destinée à produire un écart perceptible, nomme une signature structurelle :

```text
STRUCTURAL-SIGNATURE: relation rendue possible par la structure choisie
PREVIOUS-LIMIT: limite de l’héritage ou de la structure précédente
OBSERVABLE-CONSEQUENCE: manifestation attendue dans le premier objet
EXIT-CONDITION: observation qui impose l’abandon ou la recomposition
```

La signature ne signifie pas nouveauté forcée. Elle peut être une relation de foyer, de voisinage, de révélation, de temporalité, de preuve, de geste ou de retenue qui sert mieux le produit et le public. Si aucune différence structurelle utile ne peut être nommée, la sélection est documentaire ou héritée ; elle ne doit pas être présentée comme une nouvelle direction.

### Thèse structurelle et premier objet habitable

Toute sélection ouverte doit formuler une **thèse structurelle** : quelle relation perceptuelle et produit la combinaison rend-elle possible, et comment cette relation sera-t-elle visible dans le premier objet ? La réponse doit relier au moins une décision de support, grille, scène ou objet à un foyer, une masse, une cadence, une révélation, une profondeur, un geste ou une preuve.

Sépare les objets de trace : `STRUCTURAL-THESIS` décrit la relation recherchée ; `STRUCTURAL-SIGNATURE` décrit l’écart et la limite antérieure ; `OBSERVABLE-CONSEQUENCE` est l’assertion testable commune aux deux ; `FIRST-OBJECT` est l’artefact où elle doit apparaître. `EXIT-CONDITION` décide de maintenir, modifier ou abandonner la direction. La conséquence observée doit être cohérente avec la thèse et la signature, pas seulement déclarée dans deux champs.

Le premier objet doit être **habitable** : complet assez pour être regardé, comparé et jugé dans son contexte, avec contenu crédible, hiérarchie, action, états pertinents et niveau de résolution proportionné au mode. Une route ne peut pas être considérée comme réussie parce qu’elle est nommée dans la trace, ni parce qu’un schéma vide respecte ses slots.

La structure n’est pas tenue lorsqu’elle ne fonctionne qu’avec un contenu idéal, une image absente, un viewport unique ou une justification textuelle. Lorsque l’ambition visuelle est ouverte, le premier objet doit déjà posséder une composition, une spécificité et une présence suffisantes pour permettre une observation réelle ; la correction vient ensuite si une relation dominante peut être améliorée.

### Préfixes canoniques

| Préfixe | Responsabilité |
|---|---|
| `SUPPORT/<NAME>` | Champ, cadre ou niveau de densité où vit la surface. |
| `GRID/<NAME>` | Axes, rythme, foyer et hiérarchie qui organisent la lecture dans le support. |
| `SCENE/<NAME>` | Scénario reliant promesse, contenu, média, preuve et action. |
| `OBJECT/<NAME>` | Preuve, sélection, comparaison, mémoire, contrôle ou action locale. |
| `MICRO/<NAME>` | Unité dense portant un contrat de lecture, d’état, de conséquence et d’action. |
| `MODIFIER/<NAME>` | Comportement transversal ajouté après la structure. |
| `LAYER/PRIMITIVES` | Couche canonique des primitives accessibles et sémantiques ; les primitives nommées restent sélectionnées par les contrats d’objet ou de couche. |
| `LAYER/<NAME>` | Couche de composants et de dépendance. |

Un nom de domaine, un nom de campagne ou un nom de variante locale ne devient pas une route canonique par défaut.

**Lire un identifiant de structure.** `scripts/read_route.py GRID/HIERARCHICAL` et `scripts/read_route.py BIBLIOTHEQUE/GRID/HIERARCHICAL` ouvrent le titre documenté. Quand l’identifiant est une ligne de table, par exemple `MICRO/USAGE_LEDGER`, le lecteur ouvre sa section porteuse `BIBLIOTHEQUE/MICRO` ; il ne fabrique pas de sous-route. Les identifiants absents ou ambigus sont refusés. Ces raccourcis de lecture conservent les propriétaires et les responsabilités existants.

### Types de preuve

Toute route peut indiquer le type de preuve attendu :

| Type | Ce qu’il établit | Ce qu’il n’établit pas seul |
|---|---|---|
| `PERCEPTUAL` | Foyer, axes, masses, rythme, silhouette, contraste ou relation visible. | Utilisabilité réelle ou réussite de tâche. |
| `EXPERT` | Cohérence interprétée par un regard compétent dans le contexte déclaré. | Vérité universelle ou validation utilisateur. |
| `TECHNICAL` | Structure, responsive, performance, compatibilité ou contrôle mesuré. | Qualité de direction ou compréhension globale. |
| `USER/TASK` | Compréhension, réussite, erreur, effort ou satisfaction dans une tâche déclarée. | Conformité technique complète ou validité dans tous les contextes. |

Une route peut exiger plusieurs types. Une preuve perceptuelle ou experte ne devient pas une preuve d’utilisabilité par changement de vocabulaire.

La typologie BIBLIOTHEQUE décrit **ce qui est prouvé**. Les méthodes ACTION — `AUTOMATED`, `MANUAL`, `EXPERT`, `USER` ou combinaison — décrivent **comment la preuve est obtenue**. Correspondance indicative : `PERCEPTUAL` peut s’appuyer sur capture ou comparaison ; `TECHNICAL` sur script ou inspection ; `USER/TASK` sur observation d’une tâche utilisateur. Une preuve peut combiner plusieurs types et plusieurs méthodes ; aucune correspondance ne constitue un mapping automatique de verdict. `EXPERT` comme type de preuve ne doit pas être confondu avec `METHOD: EXPERT` ; le premier qualifie ce qui est établi, le second la manière dont le regard est obtenu.

---

<!-- origine:BIBLIOTHEQUE.md -->
## BIBLIOTHEQUE/SELECT — choisir avant de composer

Après `DIRECTION/START` et, si un registre d’expression doit être choisi, après `SAVOIR/STYLE`, sélectionne zéro à plusieurs responsabilités selon la décision. Ne sélectionne aucune route si la structure existante suffit ; sinon choisis uniquement les niveaux qui peuvent modifier la prochaine décision : support, grille, scène, objet de preuve, objet de rythme, micro-interface si la tâche l’exige et modificateur si son comportement est réel.

Une route est refusée lorsqu’elle ne change aucune décision d’espace, de hiérarchie, de comportement ou de preuve. Elle appartient alors au style dans `SAVOIR`, au projet local ou est retirée. La chaîne de responsabilités (support, grille, scène, objet) est décrite dans `BIBLIOTHEQUE/READ` ; pour combiner deux routes avec une raison, `BIBLIOTHEQUE/COMPAT`.

**Filtre avant catalogue.** Avant de lire une table de routes, réponds : quelle décision doit changer, quel niveau minimal peut la changer, quel premier objet rendra la relation observable et quelle preuve fera sortir la route ? Si ces réponses ne sont pas nommées, ne descends pas dans le catalogue ; reviens à `DIRECTION/START`, conserve l’existant ou pose une clarification ciblée.

### Traduire une intention en construction

<!-- noyau:début STRUCT-ACTIVATION -->
**Activer la bibliothèque.** Pour une relation visuelle ouverte, relie **intention → niveau structurel → levier concret → effet à observer**. « Calme » ou le nom d’une scène ne suffit pas : nomme ce qui change dans l’espace, le rythme, le cadrage, la mesure ou le comportement. Si le levier reste indéterminé, lis la traduction de `BIBLIOTHEQUE/SELECT`, puis seulement la route utile. Pour spécifier ou construire un objet sélectionné, utilise la calibration locale de `BIBLIOTHEQUE/CONTRACTS` si ses proportions, tokens ou états ne sont pas déjà définis dans une source pertinente du projet. Une structure héritée peut être calibrée sans nouvelle sélection ; nomme sa source retrouvable, sinon présente-la comme hypothèse nouvelle. Réemploie la trace existante ; distingue l’effet attendu de l’effet observé. Une relation déjà résolue ne déclenche aucune lecture supplémentaire.
<!-- noyau:fin STRUCT-ACTIVATION -->

Les correspondances suivantes sont des hypothèses de construction. Le contenu, le public, le médium et le risque peuvent appeler un autre levier ou une dérivation locale (`BIBLIOTHEQUE/DERIVE`). Une qualité n’impose ni palette, ni police, ni route. Lis seulement la ligne qui peut faire avancer la décision.

| Relation recherchée | Responsabilité à examiner | Premier levier concret | Observation et condition de reprise |
|---|---|---|---|
| Calme avec plusieurs informations nécessaires | `GRID/HIERARCHICAL` ou `GRID/COLUMN` | Séparer les groupes par leur distance ; réserver la plus forte masse à la priorité ; garder les informations utiles. | À faible détail puis à taille réelle, les groupes et la priorité restent perceptibles. Reprendre si le vide disloque un groupe ou éloigne sa conséquence. |
| Intimité ou présence d’un sujet réel | `OBJECT/MEDIA_ARCHIVE` ou `OBJECT/PROOF_PRODUCT_STAGE` | Régler distance du sujet, point focal, occupation de l’image et voisinage du texte sur l’asset disponible. | Inspecter sujet, contexte, texte et recomposition au format étroit. Reprendre si le cadrage détruit le contexte ou si l’asset contredit la promesse. |
| Précision d’une valeur ou comparaison | `OBJECT/CONTROL_VALUE_TILE`, `MICRO/USAGE_LEDGER` ou `GRID/BASELINE` | Lier valeur, unité, période et conséquence ; aligner les éléments comparables ; régler la longueur d’une graduation à la donnée réelle. | Tester variation des valeurs, unité, signe et contenu long. Reprendre si un repère est inexact ou si une valeur perd sa référence ; la régularité visuelle seule ne suffit pas. |
| Intensité ou monumentalité | `GRID/HIERARCHICAL` ou `SCENE/EDITORIAL_FIELD` | Donner à une masse typographique ou picturale une échelle dominante, puis régler le contraste et la place des informations secondaires. | Lire l’ensemble et les informations pratiques au format final. Réduire ou recomposer si l’intensité efface la compréhension ou multiplie les foyers. |
| Continuité, révélation ou rupture de rythme | `SCENE/PRODUCT_NARRATIVE` ou `GRID/AXIAL` | Séquencer une transformation réelle, conserver un repère commun ou déplacer une priorité à un moment précis. | Observer la séquence et son état final ; avec mouvement, jouer aussi l’interruption et la version réduite. Reprendre si la rupture ne change rien de perceptible ou fait perdre le repère. |
| Collection de pièces distinctes | `SUPPORT/COLLECTION_PLINTH` ou `OBJECT/EDITORIAL_SELECTION` | Rendre la sélection et les différences de priorité sensibles par l’échelle, l’ordre, le voisinage ou la cadence. | Comparer mémoire des pièces et accès à la sélection. Recomposer si le rythme ralentit une comparaison rapide requise par la tâche. |

La qualité expressive relève du jugement de SAVOIR ; cette table rend son hypothèse construisible. Une sélection peut résoudre le foyer tout en restant froide, générique ou mal finie : réinspecte aussi les qualités prioritaires du premier objet. Une contre-indication demande un choix situé ; elle n’interdit pas un registre expressif.

### BIBLIOTHEQUE/AVANT-SELECTION — vérifier avant de sélectionner

Pour un delta local, réponds avant toute sélection aux quatre questions d’`ACTION/FAST-PATH`, en nommant la relation qui change. Si aucune décision ne change, conserve la structure existante et inscris l’héritage ou le cas documentaire ; utilise `N/A-JUSTIFIED` seulement si le contrôle ou la décision est réellement non applicable dans le scope déclaré, avec justification ACTION, owner et prochaine preuve.

`N/A-JUSTIFIED` n’est pas une sortie de confort. Elle n’est valable que lorsque le contrôle ou la décision principale est réellement non applicable dans le scope déclaré, ou lorsqu’une paire équivalente reste valide après le dernier changement substantiel, avec artefact, owner et `NEXT-PROOF` selon ACTION. Paire équivalente : seulement lorsque B1b est déclenché et que la paire couvre exactement la même décision — voir `ACTION/GATE-B/B1b`. Un héritage documentaire sans contrôle applicable doit être marqué comme tel dans la trace, sans transformer l’absence de changement en verdict.

### Question de sélection

| Décision | Question |
|---|---|
| Support | Quel champ, cadre ou niveau de densité donne sa place à la surface ? |
| Grille | Quels axes, rythme, foyer ou relations organisent le regard ? |
| Scène | Comment promesse, contenu, média, preuve et action se rencontrent-ils ? |
| Objet de preuve | Quel objet rend la promesse crédible ? |
| Objet de rythme | Quel objet règle sélection, comparaison, mémoire ou récit ? |
| Micro-interface | Quelle unité dense demande un contrat d’état, de conséquence et d’action ? |
| Modificateur | Quel comportement transversal est nécessaire et vérifiable ? |

> **Objet de rythme.** « Objet de rythme » est un rôle, non un préfixe canonique. Il est tenu par une route `OBJECT/*` qui règle sélection, comparaison, mémoire ou récit, par exemple `OBJECT/EDITORIAL_SELECTION`, `OBJECT/MEDIA_ARCHIVE` ou `OBJECT/COMPARISON_SPLIT`. Si aucune route existante ne porte ce rôle, la sélection peut omettre l’objet de rythme et justifier `N/A-JUSTIFIED`.

### Sélection par mode

| Mode | Sélection suffisante | Limite utile |
|---|---|---|
| **LITE** | Aucune, sauf si le delta modifie réellement une relation de structure. | Préserver la structure existante. |
| **ITER** | Aucune, ou la seule route effectivement modifiée. | Ne pas redéfinir la structure pour un delta local. |
| **STANDARD** | Une décision structurante : `GRID`, `SCENE`, `OBJECT` ou `MICRO`. | Ajouter `SUPPORT` seulement si le champ est ouvert. |
| **DIRECTION** | Évaluer `SUPPORT`, `GRID`, `SCENE` et objet de preuve, puis ne retenir que les niveaux qui changent la décision ; déclarer l’héritage des autres. | `MICRO` seulement si une tâche opérationnelle existe. |
| **SYSTÈME** | La couche réellement affectée — par exemple `LAYER/PRIMITIVES`, `LAYER/OBJECTS`, `LAYER/SCENES` ou `LAYER/TOKENS` — avec le contrat de la couche, du token, du composant, de la scène ou de l’objet affecté. | Une scène ou un style n’est pas une décision système sans blast radius démontré. |

En trace complète, la sélection structurelle est persistée dans la `RUN_CARD` ou la trace canonique du run référencée par `trace_locator`, avec `MODE`, `DECISION`, `RISK`, `SCOPE`, `ARTIFACT`, `OBSERVATION/METHOD`, `PROOF/TRACE-LOCATOR`, `LIMIT/NOT-VERIFIED`, `DECISION-CHANGE`, `NEXT-ACTION`, `OWNER`, `NEXT-PROOF` et `EXIT-CONDITION`. Les identifiants de routes peuvent être rappelés dans `sources` ou dans le paquet de preuve ; BIBLIOTHEQUE ne crée pas de champ machine concurrent et respecte `MODE / STATE / ISSUE / VERDICT` d’ACTION.

### One-shot et boucle structurelle

Le `one-shot` suit la branche one-shot d’`ACTION/PIPELINE-DIRECTION`. Après sélection, il ne ferme que si la thèse structurelle, la composition, la spécificité, les états et les risques applicables tiennent déjà ; si une relation dominante échoue, retourne ou corrige, sans seconde version décorative.

La boucle structurelle est la boucle d’édition de `DIRECTION/DOUBLE-LOOP` appliquée à la structure : toute correction change une relation de foyer, de rythme, de hiérarchie, de preuve, de comportement ou de robustesse ; une route supplémentaire ou une variante nominale ne constitue pas une amélioration.

### Garde-fou de dérivation

Lorsqu’une forme locale doit être inventée, ne crée pas immédiatement une route. Charge `SAVOIR/CRAFT`, puis dérive la forme de la tâche, de la donnée, de l’état, de la conséquence, de la densité et de la preuve attendue.

Une matière, une métaphore ou un phénomène n’est retenu que s’il modifie une de ces relations et survit aux états, à l’accessibilité, à la performance et au test de retrait. La forme reste locale jusqu’à ce que plusieurs usages contrastés prouvent qu’une route durable réduit une décision ou une erreur sans homogénéiser les rendus.

`PRINT_FIELD` désigne ici une matière imprimée ou générée par code — CSS, SVG, masque, trame ou procédé local — et son nom historique ne limite pas le médium.

### BIBLIOTHEQUE/DERIVE — inventer sans fabriquer un menu

Lorsqu’aucune route existante ne rend suffisamment bien la décision, dérive une forme locale à partir d’une responsabilité existante avant d’envisager toute promotion. La dérivation déclare ses lignes par phase ; les huit premières forment le contrat réduit de `BIBLIOTHEQUE/CONTRACTS` :

```text
[Avant build — contrat réduit]
BASE-ROUTE: route ou héritage de départ (décision initiale)
PRODUCT-CONSTRAINT: contrainte réelle qui rend l’héritage insuffisant (décision initiale)
CHANGED-LEVER: foyer, rythme, preuve, voisinage, temporalité, responsive ou action (décision initiale)
PRESERVED-RESPONSIBILITY: responsabilité conservée
NEW-COUNTERINDICATION: situation où la dérivation devient nuisible
FIRST-OBJECT: objet réel dans lequel la dérivation sera observée (preuve attendue)
OBSERVABLE-CONSEQUENCE: conséquence testable (preuve attendue)
PREVIOUS-LIMIT: limite de l’héritage
[Si le risque l’active]
STRUCTURAL-SIGNATURE: écart ouvert et limite antérieure
A11Y / PERFORMANCE: bases, budget, méthode et limite
[Après observation]
SCOPE: medium, viewport, état, contenu et surface
CONTENT / STATES: données et états effectivement couverts
PROOF-TYPE / PROOF-LIMIT: ce qui est établi et ce qui reste non prouvé
EXIT-CONDITION: résultat qui maintient, modifie ou abandonne
OWNER / NEXT-PROOF: owner hérité de la ligne de run sauf changement ; prochaine vérification
[Promotion : table complète de BIBLIOTHEQUE/CONTRACTS, par BIBLIOTHEQUE/EVOLUTION]
```

Un essai local à faible risque démarre avec les huit lignes « avant build ». Un risque actif (erreur, contenu long, accessibilité, performance) rappelle ses lignes sans attendre la promotion.

Une dérivation modifie d’abord un seul levier principal, puis vérifie la responsabilité, la contre-indication, le contenu, les états, le responsive, l’accessibilité, la performance et la preuve attendue. Elle reste locale tant que plusieurs usages contrastés ne démontrent pas une responsabilité stable et un gain réel. Si elle devient candidate, son statut et sa promotion passent par `BIBLIOTHEQUE/EVOLUTION`, puis `CHANGELOG` ; aucun usage répété ne constitue une promotion silencieuse. Ne crée pas de route canonique nommée d’après une tendance ou une peau — par exemple `SCENE/BENTO`, `SCENE/GLASS_HERO` ou `SCENE/EDITORIAL_PREMIUM` — lorsque le nom ne décrit ni une responsabilité structurelle ni une preuve distinctive.

### Signaux de convergence structurelle

<!-- noyau:début STRUCT-SIGNAUX -->
Les compositions suivantes sont des signaux d’enquête, pas des interdits stylistiques :

| Signal | Question de reprise |
|---|---|
| Trois cartes égales sous un titre centré | Quelle hiérarchie ou quel objet dominant la décision exige-t-elle réellement ? |
| Hero image avec double CTA générique | Quelle preuve, quel geste ou quelle conséquence l’image et les CTA remplacent-ils ? |
| Split 50/50 promesse / screenshot sans mécanisme | Quelle relation entre artefact, état et action doit être rendue visible ? |
| Plinthe de logos avant l’objet de preuve | Quelle preuve située est remplacée par un signal de réputation ? |
| Screenshot produit décoratif sans état ni geste | Quel comportement ou quel résultat de tâche le produit doit-il démontrer ? |
| Grille répétitive sans différence de priorité | Quelle rupture doit changer la lecture, la comparaison ou l’action ? |
| Grain, trame d’impression ou texture repris d’un brief à l’autre | Quelle matière la thèse de ce produit appelle-t-elle, et que perd la page si on la retire (`MODIFIER/PRINT_FIELD`, test de retrait) ? |

<!-- concept:TRM-01 -->
**Test de trame.** Chaque brief a aussi sa trame modale : l’ordre de sections que n’importe quelle IA produirait pour lui (pour un SaaS : promesse, logos, trois bénéfices, tarifs, FAQ). Avant de fixer la structure, écris-la en une ligne, puis romps-la ou garde-la en le justifiant par ce que la personne doit voir, comprendre ou faire d’abord. Rompre, c’est changer l’ordre, le foyer ou l’objet qui organise la page ; renommer ou restyler les sections ne suffit pas.

Un signal de convergence déclenche une reformulation de la tension, de la signature ou de l’objet ; il ne justifie pas l’ajout mécanique d’une nouvelle scène. La diversité crédible vient de la relation entre contenu réel, mécanisme de preuve, geste, contrainte et structure, et non d’un changement de nom ou de peau.
<!-- noyau:fin STRUCT-SIGNAUX -->

---
