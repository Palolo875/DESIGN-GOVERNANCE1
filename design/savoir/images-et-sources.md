# Savoir — images et sources

Ancre, sourcing visuel et familles visuelles.

<!-- origine:SAVOIR.md -->
# SAVOIR/SOURCE — ancre et sourcing visuel

[REQUIS PAR LE MODULE — surface `DIRECTION`] Regarder n’est pas lire une légende. Une description textuelle peut expliquer un principe ; elle ne transmet pas seule masse, lumière, trame, densité ou rapport image/texte.

Utilise les voies `ANCHOR-GENERATED` / `ANCHOR-OBSERVED` / `ANCHOR-PROVIDED` définies par `DIRECTION/VISUAL_TARGET` et exécutées dans `ACTION/PIPELINE-DIRECTION` seulement si une ancre peut modifier la décision et si sa limite sera déclarée. Pour une surface identitaire, l’ancre suit l’absolu 2 de `DIRECTION` : exploration possible sans ancre, limite déclarée ; acceptation avec une ancre, observée ou fournie pour un produit réel ; si elle manque, les axes concernés restent `NOT-VERIFIED` et le run suit l’issue ACTION appropriée (`ACTION/PIPELINE-DIRECTION`). Hors surface identitaire, justifie la non-applicabilité. Termine par une spec visuelle exploitable. Une image générée peut matérialiser une direction ; une référence observée peut calibrer une résolution ; une ancre fournie peut exprimer une intention ou un actif réel.

`ANCHOR-GENERATED` est une **hypothèse visuelle générée**, utile pour explorer une direction et comparer une possibilité, mais elle ne fait pas autorité par défaut dans `SAVOIR/SOURCE`. Elle ne constitue ni une calibration externe suffisante, ni une preuve de qualité ou d’usage, et ne calibre pas seule un principe durable, un niveau de craft ou une résolution de détail. Lorsque l’enjeu identitaire est élevé, accompagne-la d’une référence observée, d’une contrainte réelle ou d’une réserve explicite sur l’absence de calibration externe ; une revue indépendante est un contrepoint (`ACTION/GATE-B`, B3), pas une calibration. Cette limite concerne l’autorité de la source, pas la valeur exploratoire de l’hypothèse.

### Test d’utilité de l’ancre

Une ancre est utile si elle fournit :

1. une décision structurelle ou perceptuelle qu’elle change réellement ;
2. une contre-indication identifiable ;
3. des attributs retenus, rejetés et non transférables.

Une image jolie mais sans conséquence de décision est décorative et ne suffit pas. Une ancre ne prouve ni qualité finale, ni utilisabilité, ni droit de réemploi.

Les galeries de composants, templates et bibliothèques sont utiles pour observer conventions, états et accessibilité. Elles ne suffisent pas à fournir matière, direction ou singularité. Cherche hors écran lorsqu’une affiche, une signalétique, un packaging, une photo, une édition ou une architecture apporte une contrainte de composition utile.

Les pièges sont : prompts qui convergent, image créée puis ignorée, image générée utilisée comme asset final sans décision de droits, rôle et fidélité, résultat de recherche choisi seulement parce qu’il est thématique, ou asset isolément séduisant qui détruit la lecture une fois intégré.

**Lot d’assets.** Plusieurs images d’une même page forment un lot : elles partagent un traitement (recadrage, étalonnage, grain, bichromie ou trait) qui les fait tenir ensemble même quand leurs sources diffèrent. Chaque image du lot dit quelque chose du produit, de son usage ou de son public, pas seulement du thème ; une image qui échoue à ce test est retirée, pas compensée.

**Registre d’illustration.** Le même outil peut paraître professionnel ou enfantin selon le trait, la palette et la finition. Choisis le registre pour la personne qui décide, souvent un adulte même quand le produit s’adresse à des enfants, et vérifie-le sur capture.

### Recherche orientée décision — chercher loin seulement quand cela change le résultat

Lorsque le `DOMAIN-FRAME`, le risque ou l’ambition déclenche une recherche, ne collecte pas des liens pour décorer la trace. Recherche ce qui peut modifier une décision : conventions du domaine, modèles mentaux, terminologie, contraintes réglementaires ou d’accessibilité, références culturelles, comportements concurrents, systèmes existants, matériaux, images, données ou mécanismes de preuve.

Chaque source retenue porte une fiche minimale :

```text
SOURCE: origine, date et portée
ROLE: direction, production ou vérification
STATUS: vérifié dans ce run, connaissance non revérifiée ou source utilisateur non revérifiée
WHAT-WAS-OBSERVED: observation réellement faite
WHAT-WAS-RETAINED: relation retenue
WHAT-WAS-REJECTED: motif, surface ou hypothèse écarté
HOW-TRANSFORMED: traduction propre au produit et au contexte
DECISION-CHANGED: décision que la source a modifiée, confirmée ou abandonnée
LIMIT: ce que la source ne permet pas d’affirmer
TRACE-LOCATOR: où réinspecter la source, l’observation et l’artefact
OWNER / NEXT-PROOF: responsable et prochaine vérification
RIGHTS / UNCERTAINTY: droits, autorisation ou inconnue lorsque l’asset ou le claim le requiert
```

**Projection machine, facultative.** Quand une recherche doit être contrôlée par machine, `RESEARCH_BRIEF` (`gouvernance/schemas/research_brief.schema.json`, validé par `gouvernance/outils/validate_contracts.py`) la porte : question, décision à risque, profondeur, classes de sources, incertitude avant et après, condition d’arrêt, puis une entrée par source qui reprend cette fiche. `ROLE` et `OWNER / NEXT-PROOF` n’y ont pas de champ et restent dans la trace. Ce schéma n’est jamais exigé pour faire une recherche.

Une recherche de domaine et une recherche de calibration visuelle peuvent se compléter, mais elles ne se substituent pas l’une à l’autre. Une source de tendance ne prouve pas l’usage ; une référence visuelle ne prouve pas les droits ; une convention concurrente ne devient pas une vérité produit ; un résultat généré ne devient pas une observation externe. Lorsque la recherche ne peut modifier aucune décision, déclare `N/A-JUSTIFIED` et n’approfondis pas par réflexe ; une recherche faite qui confirme la décision est une confirmation (`ACTION/STATUS`), pas un `N/A-JUSTIFIED`.

La profondeur de recherche augmente par déclencheur : confiance ou erreur coûteuse, public ou JTBD incertain, contexte culturel sensible, convention inconnue, matériau ou asset directeur à calibrer, ou écart créatif qui ne peut être défendu par le seul jugement interne. La recherche doit ensuite revenir dans le premier objet, la structure, le contenu, le geste ou la preuve ; sinon elle reste une archive et non un levier de production.

### Curer, produire et intégrer

Le point de départ n’est pas « quelle image produire ? », mais « quelle relation manque à la promesse, à la preuve ou à l’action ? ».

<!-- noyau:début MOY-CALIBRATION -->
Cherche des calibrations dans les domaines qui peuvent changer cette relation — cinéma pour lumière et séquence, édition pour rythme et crop, affichage pour échelle et distance, architecture pour masse, photographie pour focalisation, packaging pour matière, signalétique pour orientation, arts vivants pour mouvement — sans transformer une référence culturelle en décor interchangeable.
<!-- noyau:fin MOY-CALIBRATION -->

Choisis ensuite une route de production déclarée dans `DIRECTION/VISUAL_TARGET`. Une génération réussie ne se mesure pas à son réalisme intrinsèque : elle doit répondre au cadrage, au plan de lecture, au rôle du type, au contraste, au mouvement éventuel, au crop mobile et au niveau de preuve requis.

Avant de retenir un asset directeur, formule une contre-épreuve proportionnée : quel rendu code-native, asset retiré, crop alternatif ou autre médium ferait mieux apparaître la même relation ? Persiste dans la trace la contre-épreuve, la décision qu’elle pourrait modifier, son résultat et l’alternative refusée. Ne produis cette contre-épreuve que si elle peut réellement modifier la décision ; sinon, conserve la justification de non-applicabilité prévue par ACTION et avance.

---

<!-- origine:SAVOIR.md -->
# SAVOIR/DESIGN-ATLAS — familles et responsabilités

`DESIGN-ATLAS` est la section atlas de `SAVOIR.md` : un index de jugement, pas un catalogue de recettes. Commence par la décision et le risque ; si aucune famille ne peut modifier la prochaine décision, ne charge pas l’atlas. Il aide à nommer la famille d’un choix avant de charger la route spécialisée. Il ne choisit ni le mode, ni le JTBD, ni une esthétique par défaut. Il ne peut jamais réduire un mode, un niveau de preuve ou une protection déjà imposée par `DIRECTION/START` ou par un risque critique ; s’il révèle un risque supérieur, retourne à `DIRECTION/START` pour mettre à jour `MODE`, `RISK` et `SCOPE`, puis laisse ACTION recalculer owner, preuve, gates et prochaine action avant toute reprise.

| Famille | Responsabilité | Route approfondie | Question de sélection |
|---|---|---|---|
| **Médium** | Traduire la décision dans l’environnement réel. | `SAVOIR/CONTEXT`, `SAVOIR/TECH` | Quels appareils, supports, inputs, budgets et idiomes peuvent changer le résultat ? |
| **Style / registre** | Donner une manière située d’exprimer une décision. | `SAVOIR/STYLE`, `SAVOIR/CRAFT` | Quelle relation de type, matière, densité ou rythme doit être différente ici ? |
| **Technique** | Modifier une relation visuelle, informationnelle ou de production. | `SAVOIR/CRAFT`, `SAVOIR/TYPE`, `SAVOIR/TECH` | Quelle décision la technique rend-elle plus claire, plus crédible ou plus robuste ? |
| **Effet** | Produire une conséquence perceptive, comportementale, narrative, spatiale, identitaire ou informative. | `SAVOIR/CRAFT`, `SAVOIR/CONTEXT` | Que comprendra, fera, ressentira ou localisera la personne grâce à cet effet ? |
| **Asset / média** | Rendre tangible une preuve, une identité, un contenu, un contexte ou une atmosphère. | `DIRECTION/VISUAL_TARGET` pour le rôle et la route de production ; `SAVOIR/SOURCE` pour provenance, droits et transformation ; `ACTION` pour intégration, fallback, preuve et clôture. | Quel rôle porte l’asset, et que se passe-t-il s’il est absent, recadré ou remplacé ? |
| **Structure / composant** | Organiser l’espace, la lecture, l’état, la donnée ou l’action. | `BIBLIOTHEQUE/SELECT` si la structure est ouverte ; `BIBLIOTHEQUE/COMPONENTS` et `ACTION/RUN-SYSTEM` si le composant ou le blast radius est partagé, avec `SAVOIR/SYSTEM` pour le jugement du système partagé ; `ACTION` pour preuve et clôture. | Quelle unité rend la décision et les états plus directs ? |

### Cartographie non exhaustive

Les familles ci-dessous orientent la recherche ; elles ne sont ni des quotas, ni des tags obligatoires, ni des styles prêts à appliquer.

| Relation à améliorer | Techniques possibles | Effets possibles |
|---|---|---|
| Hiérarchie et orientation | Échelle, contraste, espace négatif, groupement, grille, alignement, rythme | Perceptif, informationnel, comportemental |
| Matière et contexte | Photographie, illustration, texture, trame, couleur, lumière, matériau code-native | Identitaire, atmosphérique, spatial |
| Preuve et compréhension | Donnée, diagramme, comparaison, vue produit, annotation, séquence, avant/après | Informationnel, comportemental, narratif |
| Rythme et feedback | Transition, motion d’état, progressive disclosure, scroll, réaction, son | Comportemental, narratif, perceptif |
| Profondeur et espace | Couches, masque, blur, ombre, perspective, 3D, parallax | Spatial, perceptif, identitaire |
| Voix et reconnaissance | Typographie, microcopie, couleur sémantique, marque, motif, langage | Identitaire, informationnel, narratif |

Un effet est retenu seulement s’il modifie une relation observable. Une ombre, un blur, un gradient, une texture, une animation ou une transition peuvent être légitimes, mais leur présence seule ne prouve rien. `DÉCORATIF-SANS-CONSEQUENCE` est une catégorie de retrait, jamais une technique à promouvoir.

<!-- noyau:début MOY-ASSETS -->
**Traitement des assets moyens.** Quand les assets disponibles sont moyens (photos de téléphone, banque d’images), choisis le traitement que justifie la thèse — recadrage, étalonnage, duotone, grain ou trame — plutôt que de les poser bruts ou de les remplacer par un dessin. Un traitement commun peut unifier une série disparate ; plusieurs traitements se justifient si leurs rôles sont distincts et lisibles. Vérifie sur capture la relation entre les images et la composition. Le traitement ne masque ni un droit inconnu, ni une image hors sujet.
<!-- noyau:fin MOY-ASSETS -->

### Rôles d’asset

Un asset peut servir de **preuve produit**, **contenu**, **identité**, **orientation**, **contexte**, **atmosphère**, **matière**, **signal d’état**, **donnée**, **média temporel** ou **modèle spatial**. Son rôle doit être observable dans la scène. `DIRECTION/VISUAL_TARGET` possède le rôle et la route de production ; `SAVOIR/SOURCE` possède la provenance, la transformation et la contre-indication ; `ACTION` observe l’intégration, le fallback, le scope, les droits selon le contrat du run, le statut et la clôture.

### Portée par médium

Les médiums usuels sont le **Web**, le **mobile natif**, le **desktop natif**, le **print et l’édition**, la **signalétique**, l’**espace et l’exposition**, la **vidéo et le motion**, le **jeu**, la **3D/spatial**, le **service** et l’**embarqué**. Cette liste est un index, pas une promesse d’exhaustivité. `SAVOIR/CONTEXT` définit les contraintes et les questions de robustesse ; ACTION conserve pour le scope retenu le rendu observable, les idiomes d’interaction, le référentiel applicable, l’unité de budget, la méthode, le résultat et la limite de preuve. Ces éléments sont des slots regroupables ; ils ne constituent pas cinq livrables obligatoires.

### Test de sélection et de non-recyclage

Après classification, décision et risque, et avant de charger une famille, évalue dans la trace existante : `DECISION-MODIFIED` — décision que la famille pourrait modifier ; `WHEN-USEFUL` — condition située où elle peut aider ; `COUNTERINDICATION` — cas où elle nuirait ; `MEDIUM-SCOPE` — médium et surface concernés ; `PROOF-LIMIT` — ce qui restera non prouvé. Si `DECISION-MODIFIED` ne peut pas être renseigné honnêtement, ne charge pas la famille. Ces champs préparent la sélection ; ils ne remplacent pas la trace canonique d’ACTION. Après observation, inscris `DECISION-CHANGE` si une décision a effectivement changé, été confirmée ou abandonnée ; sinon utilise `N/A-JUSTIFIED` ou `NOT-OBSERVED` selon le contrat d’ACTION. `WHY-NOW` et `REUSE-CHALLENGE` sont requis surtout lorsqu’une famille ou un profil provient d’un run précédent. Si la famille ne peut modifier aucune décision, ne la charge pas. L’absence de style, de technique, d’effet, d’asset ou de composant est une sortie valide.

**Frontière maintenance/design.** Une correction de microcopie, traduction, overflow, wrapping, contraste, focus, nom accessible ou état dans un composant existant reste une maintenance locale ; elle ne devient pas automatiquement une décision de style, de technique, d’effet, d’asset ou de structure. Si aucune famille n’est applicable, ne renseigne pas de famille et conserve la décision dans la trace ACTION ; n’utilise `N/A-JUSTIFIED` que si sa condition canonique est satisfaite. Ne transforme pas la phrase « rendre le libellé lisible » en profil typographique, ni « vérifier le contraste » en effet visuel.

---
