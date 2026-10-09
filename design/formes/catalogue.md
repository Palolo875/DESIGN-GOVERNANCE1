# Formes — catalogue

Supports, grilles, scènes, séquence, objets, micro-unités, modificateurs, composants et compatibilités.

<!-- origine:BIBLIOTHEQUE.md -->
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

<!-- origine:BIBLIOTHEQUE.md -->
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

<!-- origine:BIBLIOTHEQUE.md -->
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

<!-- origine:BIBLIOTHEQUE.md -->
## BIBLIOTHEQUE/SEQUENCE — comment la page s’enchaîne

Une page de plusieurs sections est une séquence de scènes. La scène règle chaque moment ; la séquence règle leur ordre, leur rythme et leur fin. Une surface d’un seul écran n’en a pas besoin.

**Question de séquence.** Que fait avancer chaque section : comprendre, croire, choisir ou agir ? Une section qui ne fait rien avancer se fond dans une autre ou disparaît.

| Opération | Choisir lorsque | Éviter lorsque | Preuve |
|---|---|---|---|
| **Arc** : entrée, développement, moment fort, fin | la page porte une décision d’une section à l’autre | la surface sert une tâche unique et répétée (outil, tableau de bord) | la page entière réduite montre un foyer par section et un moment plus fort que les autres |
| **Série** : constantes (repères, numérotation, bande basse, place du titre) et variables (position, échelle, côté de l’objet) | plusieurs sections de même nature se suivent | la variation ferait perdre un repère nécessaire à la comparaison | deux sections voisines diffèrent par une variable déclarée et partagent les constantes |
| **Moment de champ** : une section en grand, portée par une seule opération | la thèse gagne à être vue en grand une fois dans la page | contexte critique ou tâche urgente | la section se résume en une phrase et n’a qu’un foyer |
| **Transition** : le passage d’une section à la suivante a une forme | le bord vient d’une forme que le produit ou le domaine porte déjà | le bord est décoratif ou repris d’un gabarit | retirer la transition affaiblit la lecture, pas seulement l’ornement |
| **Fil** : un motif ou un objet revient et relie l’entrée au reste | un objet du produit peut changer d’état d’une section à l’autre | le motif n’a aucun lien avec le produit | le motif change d’état ou de rôle entre ses apparitions |
| **Fin** : une dernière scène (phrase de clôture, action), puis un colophon (marque, navigation, mentions) | la page a plusieurs sections | la surface est une vue d’application sans fin de lecture | la fin reprend la thèse de l’entrée ; le pied de page n’est pas qu’une liste de liens |

**Trame sur toute la page.** Le test de trame de `BIBLIOTHEQUE/SELECT` s’applique au milieu et au bas de la page, pas seulement au premier écran : une page qui rompt la trame en haut puis empile des sections de même poids, des cartes, des tarifs et des questions y retombe. Écris la séquence en une ligne avant le build, puis vérifie-la sur la page entière réduite.

**Cartes.** Une carte marque un objet séparable : à comparer, choisir ou collectionner. Pour des fonctionnalités ou des arguments, préfère une liste, un texte, un objet unique ou des onglets qui montrent une fonctionnalité à la fois avec sa vraie vue produit et ses états.

### Structure mobile

Sur petit écran, la séquence se recompose au lieu de se comprimer (`SAVOIR/CONTEXT`). Pour une interface, une décision par écran : un champ, un choix ou une action, l’action principale dans la zone du pouce ; une feuille posée sur le contexte garde l’objet visible au-dessus. Une relation entre plans (mot devant ou dans l’image, élément qui chevauche deux sections) se recompose aussi : vérifie sur capture mobile qu’elle ne coupe ni le texte ni l’objet.

---

<!-- origine:BIBLIOTHEQUE.md -->
## BIBLIOTHEQUE/OBJECT — quelle preuve devient tangible

Un objet donne une forme locale et réutilisable à une preuve, une sélection, une comparaison, une mémoire, un contrôle ou une action. Il possède un rôle informationnel, des slots, des contextes et des états. Il ne compose pas un écran complet.

**Objet du métier.** Un document ou un instrument que le domaine utilise déjà (formulaire, ticket, carnet, relevé, cadran, règle graduée) peut donner sa forme à l’objet de preuve ou le gabarit d’une section. Choisis-le s’il rend le mécanisme plus clair ; écarte-le s’il n’est qu’un décor ou s’il imite un document officiel au point de tromper.

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

<!-- origine:BIBLIOTHEQUE.md -->
## BIBLIOTHEQUE/MICRO — unités denses

Les micro-interfaces suivent la lecture :

> **identité → état → mesure ou choix → conséquence → action**

Graphiques, couleurs, textures et icônes soutiennent cette lecture mais ne portent jamais seuls un état.

Un graphique écrit sa conclusion au lieu de la laisser au lecteur, et montre son repère : objectif, seuil, plafond ou période de comparaison. La couleur d’une variation suit le sens de la mesure, pas son signe : une baisse peut être une bonne nouvelle, pour un délai ou un coût ; le statut est aussi écrit.

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

<!-- origine:BIBLIOTHEQUE.md -->
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

<!-- origine:BIBLIOTHEQUE.md -->
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

<!-- origine:BIBLIOTHEQUE.md -->
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
