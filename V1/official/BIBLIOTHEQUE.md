# BIBLIOTHEQUE — Structures d’interface situées

**Design Governance V1 — expérimentation maintenue.** Cette V1 est un cadre de travail en évaluation ; elle n’est pas présentée comme une release publique stabilisée. Ses limites, preuves et conditions d’usage restent explicites. BIBLIOTHEQUE sélectionne les responsabilités structurelles — support, grille, scène, objet, micro-interface, modificateur, primitive et couche — puis les encadre par des contrats transversaux (`BIBLIOTHEQUE/CONTRACTS`, `BIBLIOTHEQUE/COMPAT`).

## Responsabilité

BIBLIOTHEQUE est le système de sélection des **structures d’interface**. Elle décrit où une surface vit, comment le regard circule, comment texte, information, média et preuve se rencontrent, et quelles unités rendent une action tangible.

**Capacité positive de BIBLIOTHEQUE.** BIBLIOTHEQUE aide à transformer une décision de direction ou de produit en structure habitable, compatible et maintenable. Elle permet de choisir, adapter ou faire évoluer le support, la grille, la scène, l’objet, la micro-interface ou la couche qui rendent une relation perceptuelle et une action réellement tangibles. Elle augmente la robustesse et la richesse des possibilités sans imposer un style ; la structure retenue doit toujours servir une décision située et pouvoir être observée dans un premier objet.

**Chemin de sélection.** Après `DIRECTION/START` et la classification du mode, du risque, du scope et de la capacité, commence par la décision que la structure doit modifier, puis vérifie la relation perceptuelle ou produit concernée, la preuve attendue, la compatibilité et le coût de maintenance. Charge seulement les niveaux de structure nécessaires ; si aucune décision ne change, l’héritage explicite ou documentaire est préférable à une sélection décorative et `N/A-JUSTIFIED` ne s’emploie que selon le contrat ACTION.

Elle ne décrit pas un goût à reproduire, ne choisit pas le mode et ne ferme pas un run. Elle ne remplace pas :

| Document | Responsabilité |
|---|---|
| `DIRECTION.md` | Mode, risque, classification, absolus, cible, capacité et routage général. |
| `ACTION.md` | Runs, méthodes, preuves exécutables, états, issues, gates, verdicts et clôture. |
| `SAVOIR.md` | Jugement, craft, styles, contexte, états spécialisés et intégrité. |
| `CHANGELOG.md` | Cycle de vie des routes, migrations, promotions, dépréciations et décisions de gouvernance. |

### Entrée prioritaire — à lire avant le catalogue

Avant de parcourir les routes détaillées, retiens ces décisions de protection :

1. **Responsabilité :** BIBLIOTHEQUE transforme une décision située en structure habitable ; elle ne choisit ni le mode, ni le style, ni le verdict de livraison.
2. **Zéro route est valide :** si la structure existante suffit, conserve-la par héritage ou comme cas documentaire, avec sa source et sa justification. `N/A-JUSTIFIED` est réservé à une non-applicabilité réelle selon ACTION. Une route n’est sélectionnée que si elle peut changer une décision d’espace, de hiérarchie, de comportement ou de preuve.
3. **Premier objet :** toute sélection ouverte doit relier une thèse structurelle, une tension et, lorsque l’écart est ouvert, une signature à un premier objet habitable, avec contenu crédible, hiérarchie, action, états et résolution proportionnée.
4. **Preuve :** distingue ce que la structure rend perceptible, ce qu’un regard expert interprète, ce qu’un contrôle technique mesure et ce qu’une personne accomplit dans une tâche. Une chaîne de routes ne constitue jamais une preuve à elle seule.
5. **Proportion :** commence par le niveau minimal qui peut changer la décision ; ajoute support, grille, scène, objet, micro, modificateur ou couche seulement lorsque leur responsabilité est active.
6. **Promotion :** une route partagée ou candidate à la durée suit `DIRECTION/START` → `ACTION/RUN-SYSTEM` → `BIBLIOTHEQUE/EVOLUTION` → `CHANGELOG`. Cette chaîne organise la décision et la preuve ; elle n’accorde aucune promotion.

Cette entrée est un **résumé de protection**, pas une nouvelle route, un nouveau gate, un nouveau statut ou un second contrat machine. Les sections détaillées et les propriétaires existants prévalent en cas de différence.

### Orientation interne et sortie de sélection

Après `DIRECTION/START`, et après `SAVOIR/STYLE` seulement si le registre d’expression peut modifier la structure, commencez par `BIBLIOTHEQUE/READ`, puis `SELECT` si une décision structurelle est ouverte. Cette instruction est interne à BIBLIOTHEQUE et ne remplace jamais le démarrage DIRECTION. La chaîne `support → grille → scène → objet → primitive` décrit des responsabilités, pas un ordre obligatoire de chargement. `READING_MAP.md` est une vue dérivée pour le déclencheur et le non-chargement.

Toute sélection ou non-sélection doit transmettre : `DECISION`, niveau ou héritage, `STRUCTURAL-SIGNATURE` si applicable, contre-indication, premier objet attendu, preuve, limite, owner et condition de sortie. Ces champs sont une projection structurelle locale vers le handoff canonique ACTION ; ils ne le remplacent pas. Le reste de la transmission suit le handoff canonique (`ACTION/HANDOFF`). Si la structure existante suffit, utilisez l’héritage ou le cas documentaire ; `N/A-JUSTIFIED` est réservé à une non-applicabilité justifiée selon ACTION. La clôture et le verdict restent chez ACTION.

**Condition d’arrêt de lecture :** arrêter lorsque la relation structurelle à modifier, la route ou l’héritage, la conséquence observable, la preuve, la limite et le propriétaire suivant sont explicites.

En run local, le contrat réduit de `BIBLIOTHEQUE/CONTRACTS` suffit ; si la structure existante suffit, conserve l’héritage ou le cas documentaire avec sa source et sa justification. `N/A-JUSTIFIED` est réservé à une non-applicabilité réelle selon ACTION. Les exigences par périmètre de contribution (pilote, partagé, durable) et les statuts de cycle de vie relèvent de `BIBLIOTHEQUE/EVOLUTION`.

<!-- noyau:début STRUCT-OU -->
> L’interface ne commence ni avec une « landing premium », ni avec une grille de cartes, ni avec une image inspirante. Elle déclare d’abord **où elle vit**, **comment le regard circule**, **quelle preuve devient tangible** et **comment la personne agit**.
<!-- noyau:fin STRUCT-OU -->

---

## BIBLIOTHEQUE/READ — responsabilités et convention de route

La chaîne canonique est une carte de responsabilités, non une séquence obligatoire :

> **support → grille → scène → objet → primitive**

Une surface peut hériter d’un niveau ou n’en sélectionner aucun si aucune décision structurelle ne change. Le **support** définit le champ spatial dans lequel vit la surface. La **grille** organise la circulation, les axes, le rythme, le foyer et la hiérarchie dans ce champ. La **scène** définit le scénario de lecture et de preuve entre promesse, contenu, média et action. L’**objet** rend une preuve, un état ou une action locale tangible. La **primitive** porte le geste accessible et la sémantique de base.

Cette chaîne décrit une responsabilité, pas un ordre de lecture rigide. Une micro-interface peut être le point de départ d’une surface dense. Un modificateur intervient seulement après la structure lorsqu’il change un comportement réel.

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

## BIBLIOTHEQUE/SELECT — choisir avant de composer

Après `DIRECTION/START` et, si un registre d’expression doit être choisi, après `SAVOIR/STYLE`, sélectionne zéro à plusieurs responsabilités selon la décision. Ne sélectionne aucune route si la structure existante suffit ; sinon choisis uniquement les niveaux qui peuvent modifier la prochaine décision : support, grille, scène, objet de preuve, objet de rythme, micro-interface si la tâche l’exige et modificateur si son comportement est réel.

Une route est refusée lorsqu’elle ne change aucune décision d’espace, de hiérarchie, de comportement ou de preuve. Elle appartient alors au style dans `SAVOIR`, au projet local ou est retirée.

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

## BIBLIOTHEQUE/CONTRACTS — contrat commun de route

Une route locale commence par un contrat réduit : décision initiale, responsabilité, contre-indication, preuve attendue et limite. C’est la seule définition du contrat réduit ; la ligne `Local` du contrat minimal par périmètre et les lignes « avant build » de `BIBLIOTHEQUE/DERIVE` y renvoient. Lorsqu’elle est suivie comme candidate, elle peut porter le statut de cycle de vie `PILOT`, distinct du niveau de contrat et des statuts de run. Après observation, renseigne `DECISION-CHANGE` ou l’issue ACTION appropriée. Le contrat complet est nécessaire, mais non suffisant, pour `ADOPTED` : la promotion exige aussi usages contrastés, gain observé ou mesuré, maintenance, compatibilité, owner, prochaine revue et décision persistée dans `CHANGELOG`.

Toute route durable déclare :

| Champ | Question |
|---|---|
| Responsabilité | Quelle décision d’espace, de lecture, de preuve ou d’action porte la route ? |
| Usage juste | Dans quel contexte la route accélère-t-elle une décision ? |
| Contre-indications | Quand la route refroidit-elle, masque-t-elle ou ralentit-elle la tâche ? |
| Preuve attendue | Quelle capture, test, état ou observation montre qu’elle aide ? |
| `PROOF-TYPE` | Perceptuelle, experte, technique, utilisateur/tâche ou combinaison ? |
| `PROOF-SCOPE` | Quelle surface, tâche, medium/runtime, viewport/device, état, données ou population est couverte ? |
| `PROOF-LIMIT` | Que ne permet pas de conclure la preuve ? |
| Contenu et états | Que se passe-t-il avec contenu long, localisation, empty, error, loading, unavailable, disabled, focus, permissions, récupération et succès partiel ? |
| Mobile | Quelle relation est recomposée, conservée ou remplacée ? |
| Accessibilité | Quels risques de sémantique, nom, clavier, focus, contraste, cibles, motion et information non chromatique sont couverts, par quelle méthode et dans quel scope ? |
| Confidentialité et permissions | Quelles données, autorisations, expositions et voies de récupération sont couvertes ? |
| Compatibilité | Quels consumers, scènes, grilles, objets, plateformes ou runtimes peuvent l’accompagner, avec quel fallback, migration et rollback ? |
| Owner | Qui décide pour le run, qui reçoit l’action suivante et qui maintient la route ? La promotion/dépréciation reste une décision `CHANGELOG`. |
| Revue | Quels usages contrastés, baseline, observation ou mesure ont été réalisés, avec quelle limite et quand la route sera-t-elle revue ? |
| `DECISION-CHANGE` | Quelle décision a changé, été confirmée ou abandonnée grâce à la route ? |
| Contribution expressive | Quelle présence, quel rythme, quelle atmosphère ou quelle signature la route rend-elle possible dans son contexte ? |
| Risque de banalisation | Comment la route peut-elle devenir interchangeable, mécanique ou décorative ? |

Les sorties de contrôle suivent ACTION : `PASS`, `PASS-WITH-RESERVATION`, `RETURN`, `N/A-JUSTIFIED` ou `NOT-VERIFIED`. Elles ne créent ni statut de route, ni état de run, ni issue, ni verdict global concurrent.

Un objet ou composant accessible en isolation doit encore être testé dans sa scène, son contenu, ses états, son viewport, ses permissions et ses interactions réels lorsque le risque le requiert. Une preuve de structure ne vaut pas automatiquement preuve de tâche, de performance ou de conformité globale.

### Calibration locale de la relation retenue

Lorsqu’une sélection ou un héritage laisse des choix de fabrication ouverts, calibre ceux qui peuvent changer la relation retenue. Cette calibration précise le contenu, la contribution expressive, les états, le mobile et la preuve du contrat existant ; elle ne crée ni formulaire, ni schéma, ni route de style supplémentaire. Les valeurs vivent dans la spec, les tokens ou le composant du projet, à côté de l’artefact. Une valeur héritée déjà adaptée reste valable.

Si la ressource reste ouverte, nomme la primitive, le pack ou le fichier réellement retenu, sa source/version et le moyen disponible pour le modifier. Relie cette ressource au levier de la table et à son observation, selon la fiche existante d’`ACTION/STRUCTURED-PROOF` ; un composant cité mais inaccessible ne devient pas une capacité acquise. Le repli conserve la responsabilité utile, sans imposer l’habillage de la bibliothèque.

| Dimension ouverte | Ce qu’il faut rendre concret dans le projet | Ce qu’il faut réinspecter |
|---|---|---|
| Support et grille | Largeur utile, axes, proportions des masses, marges et distances entre groupes ; relation recomposée au format étroit. | Silhouette, regroupement et priorité avec le vrai contenu ; éviter d’empiler mécaniquement les colonnes. |
| Objet et micro-interface | Anatomie utile, ordre valeur/contexte/action, dimensions liées au contenu, états et valeurs extrêmes. | Lecture à taille réelle, référence de la mesure, précision des données, état critique et reprise lorsqu’elle est pertinente. |
| Voix typographique | Police disponible, graisse, taille, interligne, longueur de ligne et figures numériques sur le vrai titre, le texte et les données. | Hiérarchie, caractère, wrapping et repli ; jugement par `SAVOIR/TYPE` et `SAVOIR/CRAFT/CFT-05`. |
| Image, matière et couleur | Asset retenu, point focal, traitement, occupation, rôle des couleurs et paramètres de frontière ou de lumière utiles. | Relation image/texte, raccord, contraste et effet sur l’ensemble ; juger par `SAVOIR/STYLE` et `SAVOIR/STATE`, vérifier par ACTION. |
| Comportement | Changement d’état porté par le geste, place réservée, trajectoire ou durée seulement si utiles, alternative réduite. | Début, interruption, fin, récupération et réduction dans le runtime réel ; une image fixe ne couvre pas ces observations. |

**Exemples de traduction, à adapter.** Pour une scène à deux masses, un rapport initial `3:2` peut privilégier l’objet ; le vrai titre et la lecture au format étroit peuvent imposer `1:1` ou une autre relation. Pour un groupement simple, tester une distance entre groupes supérieure à celle entre membres, puis vérifier que les unités restent perceptibles. Pour un arrondi emboîté ou un bord éclairé, utiliser les conditions de `SAVOIR/STATE`. Ces essais n’établissent aucune valeur universelle et ne sont pas des tokens partagés.

Avant le build, indique l’effet attendu du levier retenu ; après le rendu ou l’interaction, compare cet effet à ce qui est réellement observable dans le même scope. Conserve, ajuste ou retire le choix et vérifie l’ensemble. Sans observation, conserve la limite prévue par ACTION. Un paramètre inscrit dans la spec, un token ou une route nommée ne constitue pas sa réussite visuelle. Une calibration locale ne devient une règle partagée que par le parcours système et la gouvernance existants.

---

## BIBLIOTHEQUE/SUPPORT — où la surface vit

Le support est la condition spatiale qui précède les composants. Il règle air, limites, navigation et entrée d’une donnée, d’un média ou d’une fenêtre produit dans le champ.

### `SUPPORT/FREE_FIELD`

Grand champ sans châssis apparent ; scène, matière ou paysage remplissent le viewport.

**Choisir lorsque :** une promesse, une illustration ou un geste de marque doit prendre l’espace avant la preuve détaillée.

**Éviter lorsque :** comparaison dense, tâche opérationnelle ou contexte critique exigent des repères continus.

**Preuve :** foyer, circulation et zone de preuve restent lisibles sans châssis explicite. Type prioritaire : `PERCEPTUAL`, puis `USER/TASK` si l’espace porte une action.

### `SUPPORT/ARCHITECTED_FRAME`

Zone active encadrée dans un espace plus calme ; bordures, axes, lignes ou seuils rendent la construction sensible.

**Choisir lorsque :** la surface doit rendre perceptibles construction, soin, institution ou maturité produit.

**Éviter lorsque :** le JTBD exige spontanéité, intimité ou récit organique refroidi par un châssis.

**Preuve :** le cadre organise une relation d’usage ou de preuve ; il ne sert pas seulement de prestige.

### `SUPPORT/OPERATIONAL_CANVAS`

Surface continue, dense et instrumentée ; contrôles, contexte et données forment la première lecture.

**Choisir lorsque :** le travail consiste à observer, analyser, comparer, administrer ou décider.

**Éviter lorsque :** projection émotionnelle, manifeste ou pièce média unique constitue la tâche dominante.

**Preuve :** contrôles et données restent récupérables sans décor concurrent ; type `USER/TASK` lorsque la surface porte une décision.

### `SUPPORT/COLLECTION_PLINTH`

Pièces, archives ou preuves mises en scène dans un vide généreux et des proportions d’objet.

**Choisir lorsque :** collection, portfolio, cas d’usage ou média doivent être mémorisés comme pièces distinctes.

**Éviter lorsque :** les éléments doivent être comparés à grande vitesse ou manipulés avec forte densité.

**Preuve :** chaque pièce conserve identité, métadonnées et relation à l’action.

### Test de support

Si texte, données et images sont masqués, cadre, vide, axes et foyer doivent encore indiquer un parti de composition. Ce test est `PERCEPTUAL` ou `EXPERT` ; il ne prouve pas seul l’utilisabilité de la surface. Si la composition dépend de ce qui est masqué par une relation déclarée, avec un repli, la dépendance est recevable (`BIBLIOTHEQUE/GATE`, non-généricité) ; le masquage sert à diagnostiquer, pas à exiger un décor indépendant du contenu.

Le support et la scène ne sont pas le même niveau : le support est le champ spatial ; la scène est le scénario de lecture et de preuve qui y prend place.

---

## BIBLIOTHEQUE/GRID — comment le regard circule

Une grille est une infrastructure de lecture, jamais un overlay décoratif ajouté après les composants. Elle organise la circulation dans le support et donne à la scène ses axes, son rythme, son foyer et ses relations.

### `GRID/MODULAR`

Unités répétables : cellules, blocs, images, chiffres et texte s’assemblent dans une trame.

**Choisir lorsque :** collection, plans, cartes, dashboard, archive ou système avec plusieurs éléments de poids proche.

**Preuve :** les cellules créent rythme et priorité ; elles ne forment pas une galerie de boîtes équivalentes.

### `GRID/COLUMN`

Axes verticaux pour largeur de texte, média, navigation et alignements durables.

**Choisir lorsque :** lecture éditoriale, contenu dense, responsive ou guidage de plusieurs sections.

**Preuve :** éléments critiques reviennent sur des axes identifiables.

### `GRID/RADIAL`

Lignes ou panneaux convergent vers un foyer.

**Choisir lorsque :** choix, signal, communauté, produit ou action doivent devenir centre de gravité.

**Preuve :** le foyer reste perceptible sans les rayons visibles et les périphéries le renforcent.

### `GRID/HIERARCHICAL`

Tailles et positions inégales selon priorité, avec ruptures contrôlées de trame.

**Choisir lorsque :** page narrative, annonce, pièce forte ou relation promesse/artefact/preuve.

**Preuve :** l’œil trouve sujet, contexte puis détail ; chaque rupture change réellement la priorité.

### `GRID/BASELINE`

Typographie, métadonnées et blancs suivent une cadence commune.

**Choisir lorsque :** lecture, langage type et précision éditoriale portent l’identité.

**Preuve :** titres, textes et microcopie partagent un rythme sans compresser le contenu.

### `GRID/AXIAL`

Axe horizontal, vertical ou diagonal qui porte passage, orientation, énergie ou tension.

**Choisir lorsque :** le produit ou la marque raconte une progression, un déplacement ou une force.

**Preuve :** l’axe guide réellement le chemin vers l’artefact et l’action sans compromettre lecture et focus.

### Contrat de grille

Une déclaration de grille précise :

- `GRID` ;
- `UNIT` ;
- `MARGIN + GUTTER` ;
- `ANCHORS` ;
- `RHYTHM` ;
- `FOCUS` lorsque radialité, axialité ou hiérarchie le requièrent ;
- les familles `MOBILE-*`, lorsque le mobile est dans le scope ou qu’un risque responsive est réel ; sinon `N/A-JUSTIFIED` :
  - `MOBILE-PRIORITY` ;
  - `MOBILE-NEIGHBORHOOD` ;
  - `MOBILE-ACTION` ;
  - `MOBILE-STATE` ;
  - `MOBILE-CONTENT` ;
  - `MOBILE-PERFORMANCE` ;
  - `MOBILE-COVERAGE-LIMIT` ;
- fallback et condition de sortie si la relation ne survit pas au contexte.

Les valeurs comme « 12 colonnes » ou « baseline 8 » sont des points de départ adaptables, jamais des validations universelles. `MOBILE-STATE`, `MOBILE-CONTENT` et `MOBILE-PERFORMANCE` sont conditionnels au risque : renseigne-les lorsque la grille porte directement une décision d’état, de contenu ou de performance ; sinon conserve la responsabilité dans la scène, l’objet ou `SAVOIR/CONTEXT` et justifie le périmètre, le scope et la prochaine preuve.

Le mobile préserve priorité, voisinage, cadence, foyer et action plutôt que le nombre de colonnes. Une radialité peut devenir séquence, une mosaïque rail, une ligne de mesure étiquette et une hiérarchie conserver sa dominante sans uniformiser tous les éléments.

La preuve de grille distingue ce qui est établi des méthodes et statuts ACTION ; aucun niveau ne vaut `PASS` par lui-même :

| Niveau | Question |
|---|---|
| `PERCEPTUAL` | Foyer, axes, masses et rythme sont-ils reconnaissables ? |
| `EXPERT` | La circulation est-elle cohérente avec la tâche déclarée ? |
| `USER/TASK` | La personne comprend-elle ou accomplit-elle la tâche avec le résultat attendu ? |

---

## BIBLIOTHEQUE/SCENE — comment la promesse devient une surface

Une scène règle la relation entre promesse, contenu, média, preuve et action. Une scène durable déclare sa responsabilité distinctive : ce qu’elle rend possible qu’une autre scène ne rend pas.

Le support reste la condition spatiale ; la scène est le scénario de lecture et de preuve.

### `SCENE/INSTRUMENT`

Champ expressif et panneau de mesure fonctionnel au premier plan.

**Choisir lorsque :** signaux, scores, états, risques ou décisions doivent être compris comme lecture concrète.

**Éviter lorsque :** l’image ne ferait qu’habiller une carte sans donnée, statut ou geste réel.

`SCENE/INSTRUMENT` peut contenir un `OBJECT/SYSTEM_DATA_MODULE` ou une `MICRO/QUERY_HEALTH`; il ne remplace pas l’objet local de mesure.

### `SCENE/EDITORIAL_FIELD`

Espace visuel souverain, manifeste compact, repère ou navigation intégrée ; l’image ou l’illustration doit porter une relation de produit.

**Choisir lorsque :** projection émotionnelle ou culturelle précède une preuve produit ultérieure, ou lorsqu’une métaphore visuelle explique et oriente.

**Éviter lorsque :** prix, capacités ou données doivent être comparés immédiatement.

`SCENE/EDITORIAL_FIELD` est un scénario de lecture ; `SUPPORT/FREE_FIELD` est le champ spatial qui peut l’accueillir.

### `SCENE/FRAMED_PRODUCT`

Page traitée comme objet dans un châssis : marge extérieure, cadre et contenu immersif.

**Choisir lorsque :** qualité de produit, confiance ou expérience intégrée doivent être perçues avant l’explication.

**Éviter lorsque :** le châssis ne hiérarchise ni contenu ni interaction.

`SCENE/FRAMED_PRODUCT` est une relation narrative et produit ; `SUPPORT/ARCHITECTED_FRAME` est la condition spatiale encadrée.

### `SCENE/OPERATING_GRID`

Grande grille porteuse, cellules nommées, métriques, texte et module analytique.

**Choisir lorsque :** système, réseau, plateforme B2B ou opération doivent se présenter avec sérieux et lisibilité.

**Éviter lorsque :** sujet sensible, narratif ou singulier serait aplati par une grille bureaucratique.

`SUPPORT/OPERATIONAL_CANVAS` décrit le champ dense ; `SCENE/OPERATING_GRID` décrit le scénario opérationnel dans ce champ.

### `SCENE/SPLIT_PROOF`

Artefact, matière ou code d’un côté ; promesse et action de l’autre, sans faux équilibre imposé.

**Choisir lorsque :** une idée peut être prouvée par un artefact concret unique.

**Éviter lorsque :** le produit exige démonstration large ou que le split force un 50/50 artificiel.

`SCENE/SPLIT_PROOF` est une composition relationnelle ; `OBJECT/COMPARISON_SPLIT` est une unité locale de comparaison.

### `SCENE/PRODUCT_NARRATIVE`

Fenêtre applicative ou état produit qui fait progresser l’histoire.

**Choisir lorsque :** interaction réelle — assistant, analyse, cockpit, collaboration — constitue la preuve la plus forte.

**Éviter lorsque :** fenêtre générique, trop petite ou sans réponse au titre.

`SCENE/PRODUCT_NARRATIVE` est une séquence de preuve ; `OBJECT/PROOF_PRODUCT_STAGE` est une fenêtre produit réutilisable.

### Test de scène

Une scène échoue si elle conserve `titre + sous-texte + CTA + image décorative` alors que sa responsabilité exige instrument, fenêtre, grille ou preuve.

Une illustration souveraine porte une métaphore produit, une navigation ou une relation précise à la preuve ; elle ne sert pas seulement de fond.

La preuve de scène doit indiquer son type et sa limite. Une relation perceptuellement convaincante ne produit pas automatiquement une preuve de tâche.

---

## BIBLIOTHEQUE/OBJECT — quelle preuve devient tangible

Un objet donne une forme locale et réutilisable à une preuve, une sélection, une comparaison, une mémoire, un contrôle ou une action. Il possède un rôle informationnel, des slots, des contextes et des états. Il ne compose pas un écran complet.

### Routes d’objet

| Objet | Responsabilité |
|---|---|
| `OBJECT/EDITORIAL_SELECTION` | Image, titre, explication courte et action pour une sélection de catégories, cas, experts, parcours ou articles. |
| `OBJECT/COMPARISON_SPLIT` | Objet traversé par une rupture de thème, fonction, lumière ou donnée lorsque comparaison ou coexistence de modes est réelle. |
| `OBJECT/MEDIA_ARCHIVE` | Média principal, métadonnées et valeur ou repère mémorable pour archive, événement, collection ou pièce culturelle. |
| `OBJECT/SYSTEM_DATA_MODULE` | Lignes, réseaux, nœuds, coordonnées ou structure de données encodent une relation de système, flux, couche, module ou économie. |
| `OBJECT/PROOF_PRODUCT_STAGE` | Promesse en haut et fenêtre produit large comme preuve concrète ; le produit réel rassure mieux qu’un mockup isolé. |
| `OBJECT/NAV_CONTEXT_CAPSULE` | Navigation compacte dans un châssis, une scène ou une image, avec destinations, utilitaires et action. |
| `OBJECT/BRAND_GRAMMAR_PLATE` | Planche de logo, contraste, palette, matière, type et application fonctionnelle lorsque l’identité doit devenir une décision répétable. |
| `OBJECT/CONVERSION_CONTEXT_FIELD` | Promesse entourée d’artefacts de travail réellement contextualisés lorsque le monde concret du visiteur crédibilise la conversion. |
| `OBJECT/CONTROL_VALUE_TILE` | Valeur principale, statut, contexte limité et actions courtes pour solde, quota, score, capacité ou décision rapide. |

### Contrat d’objet

Chaque objet durable déclare :

| Champ | Contenu |
|---|---|
| Rôle | Preuve, sélection, comparaison, mémoire, contrôle ou action. |
| Contextes autorisés | Où l’objet aide réellement. |
| Slots | Requis, optionnels et interdits. |
| Variantes | Sémantiques : `context`, `density`, `emphasis` ; elles ne remplacent pas les états d’exécution. |
| États | Default, loading, empty, error, unavailable, disabled, focus, permissions, récupération, contenu extrême et autres pertinents ; chaque état est déclaré applicable, non applicable et justifié, ou requis. |
| Contenu | Longueur, localisation, données et confidentialité. |
| Risques | A11y, compréhension, performance, confidentialité, permissions et récupération. |
| `PROOF-TYPE` | Perceptuel, expert, technique, utilisateur/tâche ou combinaison. |
| Test | Observation, capture, scénario ou résultat attendu, avec `SCOPE`, `METHOD`, `OWNER`, `TRACE-LOCATOR` et date/version lorsque pertinents. |
| `PROOF-LIMIT` | Ce qui ne peut pas être conclu à partir de ce test. |

Les variantes de maquettage comme `green-hero-v3` ne sont pas des variantes sémantiques. Les objets très situés — campagne, domaine ou projet — restent locaux tant que leur responsabilité ne démontre pas plusieurs usages distincts.

Un objet accessible ou cohérent en isolation ne constitue pas une preuve de scène. Teste son intégration dans le support, la grille, la scène, le contenu, les états, le viewport, les permissions et les interactions réels lorsque le risque le requiert. Pour un objet partagé ou durable, ajoute `OWNER-SCOPE`, `CONSUMERS`, `MOBILE`, `A11Y`, `COMPATIBILITY`, `MIGRATION`, `ROLLBACK`, `ADOPTION-STATUS` et `NEXT-REVIEW` selon le risque.

---

## BIBLIOTHEQUE/MICRO — unités denses

Les micro-interfaces suivent la lecture :

> **identité → état → mesure ou choix → conséquence → action**

Graphiques, couleurs, textures et icônes soutiennent cette lecture mais ne portent jamais seuls un état.

Une micro-interface déclare au minimum rôle, contextes autorisés, slots requis/optionnels/interdits, variantes, états applicables, contenu/localisation/confidentialité, risques, `PROOF-TYPE`, `PROOF-LIMIT`, test, scope, owner et prochaine preuve. Elle devient partagée ou durable seulement avec contrat, consumers, compatibilité, maintenance, statut de cycle de vie et revue adaptés.

| Micro-interface | Responsabilité | Vérification principale |
|---|---|---|
| `MICRO/IDENTIFICATION_GATE` | Onboarding, identification, profil ou première étape de service. | Dans le viewport, le médium et le scope déclarés, tâche, raison, suite, erreurs, attente et voie d’accès/récupération alternative sont compréhensibles. |
| `MICRO/SETTINGS_GROUP` | Réglages et profil avec catégories de décision hétérogènes. | Regroupement selon modèle mental ; valeurs actuelles, destinations et indisponibilités visibles. |
| `MICRO/PROFILE_EVIDENCE` | Personne, compte ou agent devant inspirer confiance et conduire à une action. | Sujet, crédibilité et action compris avant attributs décoratifs. |
| `MICRO/QUERY_HEALTH` | Requête, ressource, job ou signal surveillé sans ouvrir un dashboard complet. | Nom, période, métrique, référence, source, fraîcheur/horodatage, état de chargement ou d’erreur, diagnostic et prochaine action répondent à « quoi, comparé à quoi, depuis quand, avec quel niveau de confiance, que faire ? ». |
| `MICRO/ENTITY_STATUS_RAIL` | Flotte, site, lieu ou ensemble de ressources piloté rapidement. | Entité, total de référence, éléments actifs, fraîcheur, exception, capacité et action suivante restent lisibles ; aucun statut ne dépend de la couleur seule. |
| `MICRO/ITINERARY_SEGMENTS` | Voyage, rendez-vous, livraison ou séquence logistique comparée et modifiée. | Segments, connexion, fuseau, transfert, annulation, coût/délai, conséquence de modification et informations incomplètes. |
| `MICRO/USAGE_LEDGER` | Crédits, quotas, consommation ou budget guidant une décision. | Valeur, unité, plafond, période, prévision et conséquence du dépassement. |

### Before-after

Un avant/après valide une hypothèse, non une impression de modernité. Il nomme :

```text
TASK
GROUPING
PRIORITY
REFERENCE
CONSEQUENCE
STATE
TEST
PROOF-LIMIT
```

La comparaison est valide si elle isole la décision et observe le critère déclaré. La version retenue est celle qui réduit une ambiguïté, préserve les états critiques et rend une décision plus directe sans exiger davantage d’attention : l’original s’il résout mieux (`ACTION/GATE-B/B1b`). La preuve se rattache au gate ACTION applicable et à la méthode déclarée ; lorsque la compréhension ou l’usage domine, une tâche utilisateur est requise dans le scope déclaré.

Lorsque le scope le requiert, rattache l’avant/après à `ACTION/GATE-B/B1b` : capture initiale et capture après une seule décision éditée, tâche ou lecture déclarée, variable observable, états critiques, `DECISION-CHANGE`, méthode, scope, owner, `PROOF-LIMIT` et prochaine preuve. Si aucun résultat n’est observé, utilise le statut ACTION approprié, jamais un `PASS` implicite.

Une micro-route devient durable seulement lorsqu’elle possède plusieurs usages contrastés, un contrat réutilisable, un owner de maintenance, une preuve de gain avec baseline et limite, une compatibilité, une prochaine revue et un statut de cycle de vie ; la promotion passe par `BIBLIOTHEQUE/EVOLUTION` puis `CHANGELOG`.

---

## BIBLIOTHEQUE/MODIFIER — comportements transversaux

Un modificateur n’est ni un style, ni une scène, ni un objet substitutif. Il s’ajoute après la structure lorsque son comportement change réellement lisibilité, navigation ou matérialité.

### `MODIFIER/FIELD_SWITCH`

Une sélection recompose le champ visuel, la microcopie ou l’action.

**Test :** nom, rôle, valeur, focus, état actif/inactif, conséquence et changement utile sont perceptibles et utilisables au clavier, au lecteur d’écran et à l’œil dans le scope déclaré.

### `MODIFIER/NAVIGATION_SHELL`

Navigation comme couche de contrôle dans une scène, un cadre ou une image.

**Test :** sorties, actions, focus et contraste restent lisibles dans la matrice finie de fonds, crops, thèmes, viewports et états déclarés ; le fallback est explicite.

### `MODIFIER/PRINT_FIELD`

Grain, trame, aplat, bordure ou hachure donnent un statut de matière conçue.

**Conditions :** rôle perceptuel ou sémantique, test de retrait, contraste, performance et alternative lorsque la matière est informative. La sémantique ne dépend jamais de la texture ou de la couleur seule. La matière peut être produite par CSS, SVG, typographie, masque ou procédé local ; elle ne devient pas une recette réutilisable sans preuve de gain transversal.

**Test :** la matière soutient l’identité ou la preuve sans abaisser lisibilité, accessibilité ou robustesse. Une matière reprise d’un brief à l’autre est un signal de convergence (`BIBLIOTHEQUE/SELECT`, signaux de convergence structurelle) : une question de jugement, jamais une interdiction.

---

## BIBLIOTHEQUE/COMPONENTS — couches et dépendances

| Couche | Responsabilité | Exemples |
|---|---|---|
| `LAYER/TOKENS` | Valeurs et relations durables. | Couleurs sémantiques, type, espacements, bordures, z-index, motion. |
| `LAYER/BRAND_GRAMMAR` | Expression d’identité hors métier. | Cadres, règles, repères, trames, champs matière, signatures typographiques. |
| `LAYER/PRIMITIVES` | Gestes universels et accessibilité. | Button, Link, Input, Select, Dialog, Tabs, Tooltip, Checkbox, Skeleton. |
| `LAYER/OBJECTS` | Forme stable d’une preuve ou information. | Routes `OBJECT/*` ; `MICRO/*` est un sous-type d’objet dense soumis au même contrat, pas une couche indépendante. |
| `LAYER/SCENES` | Composition, support et hiérarchie d’un écran. | Routes `SUPPORT/*`, `GRID/*`, `SCENE/*`. |
| `LAYER/TEMPLATES` | Séquence de scènes pour une intention produit. | Une route `TEMPLATE/*` si elle est nommée, avec slots, états, mobile, contre-indications, owner et preuve ; les exemples Produit, dashboard, authentification, archive et campagne restent descriptifs sinon. |

### Contrat de composant partagé

S’applique à un pattern réutilisable, à un composant critique ou à un composant partagé ; un delta local sans responsabilité critique, réutilisable ou partagée n’en porte aucune obligation ; s’il touche un composant critique ou partagé, ou devient réutilisable, il relève de ce contrat (reclasser avec `DIRECTION/START`). C’est la seule définition de la structure d’un composant : `ACTION` en garde la baseline comme preuve, la migration et le verdict ; `SAVOIR/SYSTEM` en garde le jugement (tokens, modes, interopérabilité, maintenance).

```text
INTENTION / NON-USAGE
SÉMANTIQUE / CLAVIER ET FOCUS
ANATOMIE ET SLOTS
TOKENS CONSOMMÉS ET MODES
VARIANTS UTILES
ÉTATS
RESPONSIVE
FRONTIÈRES DE COMPOSITION
BASELINE DE RENDU
SOURCE DE VÉRITÉ
OWNER
COMPATIBILITÉ
PROCHAINE REVUE
```

### Échelle de responsabilité

| Couche | Peut | Ne peut pas |
|---|---|---|
| Primitive | Porter geste accessible et sémantique de base. | Déclarer promesse produit ou identité entière. |
| Objet | Rendre preuve, état ou action locale réutilisable. | Composer une page complète ou réinventer une primitive. |
| Scène | Régler support, grille, rapport type/média/preuve et hiérarchie. | Encapsuler plusieurs pages ou contourner les états. |
| Template | Orchestrer plusieurs scènes pour une intention. | Réécrire les contrats inférieurs. |

`LAYER/BRAND_GRAMMAR` est transversal mais gouverné. Il déclare :

```text
OWNER
SCOPE
TOKENS-CONSUMED
AUTHORIZED-SIGNATURES
ADMISSIBLE-SURFACES
COUNTERINDICATIONS
REMOVAL-TEST
BLAST-RADIUS
NEXT-REVIEW
DECISION-OWNER
APPROVAL-ROUTE
LIFECYCLE-STATUS
PROOF
PROOF-LIMIT
TRACE-LOCATOR
```

Ce n’est pas un coffre de CSS décoratif ni une autorité de direction à la place de `DIRECTION`.

Le graphe de dépendance reste à sens unique :

> **templates → scenes → objects → primitives → tokens** ; `brand_grammar → tokens` avec application aux surfaces déclarées.

Une scène ne réimplémente pas l’accessibilité. Une primitive ne porte pas l’identité entière. Un objet n’importe pas une page spécifique. `BRAND_GRAMMAR` ne remonte pas vers `DIRECTION` et ne réécrit pas les contrats inférieurs.

---

## BIBLIOTHEQUE/COMPAT — combiner avec une raison

La compatibilité indique des combinaisons favorables, non des prescriptions. Chaque ligne est une hypothèse de combinaison. L’absence d’une route dans la matrice ne constitue ni une contre-indication ni un signal de moindre sécurité ; elle signifie seulement qu’aucune combinaison indicative n’est fournie ici. Elle doit être relue avec :

```text
DECISION
PROOF-TYPE / PROOF-SCOPE / PROOF-LIMIT
RISK
RESPONSIVE-RELATION
CRITICAL-STATES
EXIT-CONDITION
```

Ces labels sont des champs de lecture et non de nouvelles routes ou de nouveaux statuts. Une combinaison non listée est possible si elle possède le contrat de route applicable. Une combinaison listée ne devient jamais une recette par défaut.

| Niveau structurel — support ou scène | Grilles favorables | Unités locales — objet ou micro-interface | Condition principale |
|---|---|---|---|
| `SUPPORT/FREE_FIELD` | `GRID/HIERARCHICAL`, `GRID/RADIAL`, `GRID/BASELINE` | `OBJECT/MEDIA_ARCHIVE`, `OBJECT/EDITORIAL_SELECTION`, `OBJECT/NAV_CONTEXT_CAPSULE` | Foyer ou cadence conservé ; pas de collection égale sans raison. |
| `SUPPORT/ARCHITECTED_FRAME` | `GRID/COLUMN`, `GRID/MODULAR`, `GRID/BASELINE` | `OBJECT/PROOF_PRODUCT_STAGE`, `OBJECT/NAV_CONTEXT_CAPSULE` | Cadre renforce usage ou preuve, pas seulement prestige. |
| `SUPPORT/OPERATIONAL_CANVAS` | `GRID/COLUMN`, `GRID/MODULAR`, `GRID/BASELINE` | `OBJECT/SYSTEM_DATA_MODULE`, `OBJECT/COMPARISON_SPLIT`, `MICRO/QUERY_HEALTH` | Aucun décor ne masque les lectures de même importance. |
| `SUPPORT/COLLECTION_PLINTH` | `GRID/MODULAR`, `GRID/HIERARCHICAL`, `GRID/BASELINE` | `OBJECT/MEDIA_ARCHIVE`, `OBJECT/EDITORIAL_SELECTION` | Foyer ponctuel, comparaison encore possible. |
| `SCENE/INSTRUMENT` | `GRID/COLUMN`, `GRID/BASELINE`, `GRID/MODULAR` | `OBJECT/SYSTEM_DATA_MODULE`, `MICRO/QUERY_HEALTH`, `MICRO/ENTITY_STATUS_RAIL` | Décision et mesure avant récit d’écosystème. |
| `SCENE/EDITORIAL_FIELD` | `GRID/HIERARCHICAL`, `GRID/RADIAL`, `GRID/BASELINE` | `OBJECT/EDITORIAL_SELECTION`, `OBJECT/MEDIA_ARCHIVE`, `OBJECT/PROOF_PRODUCT_STAGE` | Image ou paysage porte une relation ; preuve produit explicite. |
| `SCENE/FRAMED_PRODUCT` | `GRID/COLUMN`, `GRID/MODULAR`, `GRID/BASELINE` | `OBJECT/PROOF_PRODUCT_STAGE`, `OBJECT/NAV_CONTEXT_CAPSULE` | Châssis renforce usage et confiance. |
| `SCENE/OPERATING_GRID` | `GRID/MODULAR`, `GRID/COLUMN`, `GRID/BASELINE` | `OBJECT/SYSTEM_DATA_MODULE`, `MICRO/QUERY_HEALTH`, `MICRO/ENTITY_STATUS_RAIL` | Ruptures réservées à action ou alerte prioritaire. |
| `SCENE/SPLIT_PROOF` | `GRID/AXIAL`, `GRID/HIERARCHICAL`, `GRID/COLUMN` | `OBJECT/SYSTEM_DATA_MODULE`, `OBJECT/PROOF_PRODUCT_STAGE` | Artefact centre de la preuve ; pas de split décoratif. |
| `SCENE/PRODUCT_NARRATIVE` | `GRID/HIERARCHICAL`, `GRID/COLUMN`, `GRID/MODULAR` | `OBJECT/PROOF_PRODUCT_STAGE`, `MICRO/PROFILE_EVIDENCE` | Fenêtre produit répond directement à la promesse. |

### Contrat de compatibilité

Toute compatibilité durable indique : relation de preuve, décision dominante, contre-indication, recomposition responsive, états critiques, scope, méthode, owner, limite et condition de sortie. Ces champs complètent `BIBLIOTHEQUE/CONTRACTS` ; ils ne le remplacent pas.

Si une combinaison ne peut pas répondre à ces champs, elle reste exploratoire ou locale au run. `COMPAT` ne constitue ni un gate ni un verdict ; les contrôles structurels sont transmis à `BIBLIOTHEQUE/GATE` et les statuts, preuves exécutables et verdicts restent ceux d’ACTION.

---

## BIBLIOTHEQUE/GATE — contrôle de module structurel complémentaire

Ce contrôle appartient au périmètre de BIBLIOTHEQUE. Il ne constitue pas un quatrième gate global : `ACTION/GATE-A`, `ACTION/GATE-B` et `ACTION/GATE-C` restent les gates canoniques du run.

Il s’agit d’un **contrôle structurel complémentaire**, pas d’une route de clôture concurrente. BIBLIOTHEQUE peut décrire le parti structurel et sa limite ; `ACTION` reste propriétaire du scope, de la méthode, de la preuve, des statuts, des issues, du verdict de livraison et de la clôture. `BIBLIOTHEQUE/GATE` ne possède ni statut ni verdict propres.

<!-- concept:PRC-01 -->
Le contrôle de module vérifie support, grille, scène, objet, états, mobile et accessibilité structurelle, pas seulement code ou conformité d’une primitive. Il vérifie également que la thèse structurelle est visible dans le premier objet habitable et que la relation déclarée reste observable lorsque le contenu, le viewport ou l’état changent. Pour une micro-interface d’identification, de santé, de permission ou de récupération, reviens à `DIRECTION/START` pour la classification et à `ACTION` pour la preuve, le scope et le verdict ; le contrat structurel seul ne suffit jamais.

| Test | Question | Type possible |
|---|---|---|
| Non-généricité | Sans image, données et nom, la structure pourrait-elle appartenir à cinquante produits ? Si oui, la structure dépend de ce qui a été retiré. Si la dépendance est porteuse (relation déclarée, fallback prévu par `DIRECTION/VISUAL_TARGET`), la conserver. Si elle est décorative, changer la relation support/grille/scène/preuve plutôt qu’ajouter du polish. Dans les deux cas, décider sur le rendu entier, la tâche et `ACTION/GATE-C`. | `PERCEPTUAL`, `EXPERT` |
| Silhouette | Après floutage, support, foyer, masses et axes restent-ils perceptibles ? | `PERCEPTUAL` |
| Grille | Éléments critiques partagent-ils un axe, rythme ou relation identifiable ? Les ruptures changent-elles une priorité ? | `PERCEPTUAL`, `EXPERT` |
| Preuve | Objet ou micro-interface répond-il à la promesse avec contenu, état et action crédibles ? | `EXPERT`, `USER/TASK` |
| Asset | Route de production, cadrage, occupation et contraste changent-ils support, scène ou preuve ? Source, droits, provenance et raison de route sont-ils tracés ? | `TECHNICAL`, `EXPERT` |
| Clarté | Tâche, référence, conséquence et action sont-elles lisibles ? | `EXPERT`, `USER/TASK` |
| États | Loading, empty, error, unavailable, disabled, succès, contenu long et données sensibles préservent-ils le rôle ? | `TECHNICAL`, `USER/TASK` |
| Mobile | Priorité, voisinage, action, état, contenu et performance sont-ils recomposés plutôt que compressés ? | `TECHNICAL`, `USER/TASK` |
| Accessibilité | Focus, clavier, contrastes, noms, alternatives et information non chromatique sont-ils présents ? | `TECHNICAL`, `USER/TASK` |
| Contexte | La structure répond-elle au public, au JTBD et au risque dominant ? | `EXPERT`, `USER/TASK` |
| `DECISION-CHANGE` | Après observation, la sélection a-t-elle changé, confirmé ou abandonné une décision, ou est-elle seulement documentée ? | Sortie de trace ACTION ; méthode et scope séparés |

BIBLIOTHEQUE/GATE reste complémentaire d’ACTION/GATE-A, B et C. BIBLIOTHEQUE vérifie le parti structurel et rend explicite la limite ; ACTION contrôle scope, méthode, preuve et verdict de livraison.

### Statut ACTION du contrôle structurel

Ce contrôle ne possède ni statut ni verdict propres. Les statuts ACTION applicables sont `PASS`, `PASS-WITH-RESERVATION`, `RETURN`, `N/A-JUSTIFIED` ou `NOT-VERIFIED`, dans le registre de gate ou de preuve approprié.

Une description dans la `RUN_CARD` peut suffire pour une relation simple et non critique. Une relation visuelle critique exige une capture annotée, un rendu ou une comparaison adaptée. Une description seule ne devient pas une preuve de rendu.

Une chaîne de routes complète sans `DECISION-CHANGE` observable est une trace documentaire, pas une preuve de structure.

La structure reçoit la route d’asset décidée par `DIRECTION` et vérifiée par `ACTION` seulement lorsqu’elle modifie support, scène, objet ou mobile. Elle ne source ni ne hiérarchise les outils. La preuve structurelle reste locale au run ; BIBLIOTHEQUE ne devient ni galerie d’assets, ni archive de références visuelles, ni corpus de goût.

---

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

## Test de sortie BIBLIOTHEQUE

Avant de clôturer une sélection, vérifie :

1. Chaque route sélectionnée change-t-elle une décision réelle ?
2. Chaque route possède-t-elle une responsabilité et une contre-indication claires ?
3. L’objet ou la micro-interface porte-t-il une preuve, un état et une action crédibles ?
4. Le type, le scope et la limite de preuve sont-ils déclarés ?
5. La recomposition mobile couvre-t-elle priorité, voisinage, action, état, contenu et performance lorsque le risque le requiert ?
6. La combinaison choisie est-elle justifiée par JTBD, preuve, risque et condition de sortie ?
7. Chaque identifiant sélectionné existe-t-il dans le catalogue canonique, ou est-il explicitement marqué local ou `PILOT` ?
8. En trace complète, la sélection structurelle et sa justification sont-elles persistées dans la `RUN_CARD` ou la trace canonique référencée par `trace_locator`, le paquet de preuve n’étant qu’une pièce jointe localisable ?
9. Les routes et identifiants respectent-ils le bon niveau : support, grille, scène, objet, micro, modificateur ou couche ?

Si une réponse reste inconnue, utilise `NOT-VERIFIED`. Si un contrôle doit être repris, utilise `RETURN`; si le périmètre reste exploratoire, utilise l’issue ACTION appropriée, par exemple `EXPLORATORY` ou `RETURNED`. Ne transforme pas une chaîne complète de routes en preuve de qualité et ne remplace pas `ACTION/CLOSE-EXIT-CHECK`.
