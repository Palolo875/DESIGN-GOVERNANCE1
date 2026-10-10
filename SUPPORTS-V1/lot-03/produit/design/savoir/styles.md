# Savoir — styles

Profils de style contrôlés et réglages.

<!-- origine:SAVOIR.md -->
# SAVOIR/STYLE — profils contrôlés et dials

Un profil de style règle une manière d’exprimer une décision : rapport au type, matière, densité, contraste et mouvement. Il ne choisit ni JTBD, ni support, ni grille, ni scène.

Le parcours est : `DIRECTION/START → SAVOIR/FRAME si le cadrage est à éclaircir → SAVOIR/STYLE si nécessaire → ACTION/RUN-*`. Ajoute `BIBLIOTHEQUE/SELECT` uniquement lorsque la structure d’écran ou la combinaison de routes est ouverte ; si la structure existante suffit, justifie le non-chargement dans la trace.

### Règle de sélection

Un profil est retenu seulement s’il modifie une décision que le run doit réellement prendre et soutient le public, la tâche, le positionnement ou le contexte. Aucun profil n’est choisi par défaut.

La `RUN_CARD` ou la trace locale note, sans créer de nouveau schéma :

```text
PROFILE-DECISION — décision réellement modifiée.
DIALS — dials relevés, abaissés ou inchangés.
COUNTERINDICATION — situation où le profil devient nuisible.
EVIDENCE — capture, observation ou preuve montrant son effet.
```

`PROFILE-DECISION` se lit en deux temps : le profil retenu, qui est une intention (vers `DECISION-INTENT`), puis l’effet constaté après capture (vers `DECISION-CHANGE`). Ces libellés se mappent aux champs canoniques d’ACTION : `PROFILE-DECISION` vers `DECISION-INTENT` puis `DECISION-CHANGE`, `DIALS` vers la décision perceptuelle et son scope, `COUNTERINDICATION` vers `RISK` et `LIMIT`, et `EVIDENCE` vers `PROOF/TRACE-LOCATOR` avec méthode, résultat, owner et `NEXT-PROOF`. Ils ne sont ni des états de run, ni des issues, ni des verdicts.

Un profil est refusé lorsqu’il sert de raccourci pour un genre, un ensemble de composants, une esthétique « premium » ou une collection de motifs. Les profils ci-dessous sont des profils internes d’expression ; ils ne sont ni des catégories scientifiques, ni des packs de composants, ni des styles prêts à appliquer.

Le catalogue est **borné et non exhaustif** : l’absence d’un profil ne justifie ni d’en choisir un par confort, ni d’en inventer un nouveau pour chaque brief. Un profil peut être réutilisé seulement si la décision, le public, le contexte et la relation produit restent suffisamment comparables ; la trace doit alors dire `WHY-NOW`, ce qui reste identique et ce qui change. Une répétition due à la disponibilité d’un profil ou à la réussite d’un run précédent n’est pas une décision située. Lorsqu’un profil précédent est disponible, `REUSE-CHALLENGE` s’applique aussi au style, et l’absence de profil reste une sortie valide.

Un profil observé dans une référence réelle, découvert par recherche ou construit pour la décision peut être préféré aux profils internes ci-dessus lorsqu’il sert mieux le JTBD, le public ou le contexte. Il suit la même discipline : intention, axes d’expression, contre-indication, transformation de la référence et `PROFILE-DECISION` dans la trace. Le catalogue interne n’est ni exhaustif ni prioritaire par défaut ; une référence n’est jamais une recette, un profil externe n’est jamais une autorisation de copier une marque, une interface, un asset ou un composant tel quel.

### Taxonomie transversale

Les profils ne sont pas tous du même type. Avant de choisir un profil, distingue sa dimension principale et les dimensions qu’il influence réellement :

| Dimension | Exemples | Question de décision |
|---|---|---|
| Composition | `EDITORIAL_PRECISION`, Swiss, modulaire, radial, asymétrique | Comment le regard circule-t-il et où se situe le foyer ? |
| Matière et rendu | `RAW_BRUTALISM`, `TACTILE_VOLUME`, imprimé, plat, métallique | Quelle matérialité ou quel degré de planéité sert le produit ? |
| Représentation | `PICTORIAL_UTILITY`, pixel art, collage, vectoriel, photographie, 3D | Que rend visible ou compréhensible le mode de représentation ? |
| Époque et culture | rétro, Y2K, cyberpunk, moderniste, vernaculaire | Quelle mémoire ou relation culturelle est activée, pour quel public ? |
| Densité et énergie | minimaliste, maximaliste, silencieuse, énergique, contemplative | Quelle quantité de signal et de variation la tâche peut-elle porter ? |
| Interaction et temps | instrumentale, ludique, cinétique, réactive, séquentielle | Que change le geste, la transition ou le temps dans la compréhension ? |
| Voix et comportement | populaire, institutionnelle, expérimentale, chaleureuse, radicale | Quelle relation la surface établit-elle avec la personne ? |

Ces dimensions peuvent être combinées, mais leur combinaison doit produire une thèse. `Y2K`, `cyberpunk`, `rétro`, `pop art`, `Swiss` ou `brutalisme` peuvent être des références culturelles, des influences ou des dials ; ils ne sont pas automatiquement des profils canoniques ni des prescriptions de surface.

| Profil | Intention | Expression possible | Contre-indications |
|---|---|---|---|
| `STYLE/RAW_BRUTALISM` | Rendre une position, contrainte ou matière impossible à ignorer. | Structure tendue, type frontal mais lisible, matière franche, contraste net, densité concentrée. | Contexte critique, première fois, données sensibles ou friction qui masque état/action. Ne jamais imiter un défaut d’accessibilité. |
| `STYLE/EDITORIAL_PRECISION` | Donner au langage, au rythme et à la sélection le poids principal. | Baseline, colonnes, blancs calibrés, hiérarchie typo, métadonnées précises, densité séquencée. | Dashboard temps réel, comparaison très rapide ou données dominantes. Éviter la préciosité. |
| `STYLE/PICTORIAL_UTILITY` | Transformer image, illustration ou scène en explication ou repère. | Composition autour d’un artefact, type sobre, matière visuelle porteuse d’une relation produit. | Image sans fonction explicative, droits/provenance/alternative/performance non maîtrisés. |
| `STYLE/QUIET_SYSTEM` | Rendre un système fiable, calme et opérable sans neutralité vide. | Colonnes, baseline, modules réglés, type rationnel, matière réduite à des seuils et états utiles. | Campagne, manifeste ou objet de collection à présence émotionnelle autonome. |
| `STYLE/MAXIMAL_EXPRESSION` | Donner à l’abondance, à l’énergie ou à la pluralité une hiérarchie lisible et mémorable. | Contrastes de masse, couleurs ou matières coordonnées, rythme dense, superposition maîtrisée, contenu riche et points de repos. | Tâche urgente, surcharge cognitive, statut critique ambigu ou public non préparé. |
| `STYLE/DIGITAL_MEMORY` | Transformer une mémoire numérique ou une culture d’écran en relation utile au produit. | Pixel, raster, scanline, interface rétro, signal, néon ou artefact de compression soumis à une hiérarchie actuelle. | Nostalgie plaquée, cliché cyberpunk, faible lisibilité, motion agressive ou performance non maîtrisée. |
| `STYLE/TACTILE_VOLUME` | Donner chaleur, proximité et matérialité à une interaction ou une identité. | Volume doux, ombres calibrées, surface tactile, objets authored, feedback physique et profondeur mesurée. | Contraste faible, affordance ambiguë, interface dense, donnée critique ou poids de rendu excessif. |
| `STYLE/COLLAGE_ASSEMBLY` | Rendre visibles l’archive, la pluralité, la tension ou l’assemblage de sources. | Fragments, découpes, superpositions, échelles disjointes, annotations et provenance intégrées à la composition. | Provenance ou droits incertains, hiérarchie confuse, lecture linéaire indispensable ou collage purement décoratif. |

### Usage et test

BIBLIOTHEQUE fournit l’architecture, pas l’habillage. Un même objet ou une même scène peut recevoir des expressions différentes sans changer sa responsabilité de preuve.

> **Test de style.** Masque les couleurs de marque, l’image et le logo. Si hiérarchie, type, densité et matière ne traduisent plus une différence substantielle, le profil dépend du médium masqué. Il est légitime si ce médium porte une relation déclarée et dispose d’un fallback. Sinon, il n’y avait pas de profil choisi, seulement une étiquette.

### Dials

[À ADAPTER] Les dials sont des relations perceptuelles qualitatives, non des recettes de layout, des valeurs machine ou des scores. Un dial peut rester inchangé si aucune décision du run ne le concerne ; sa position, sa contre-indication, son médium, son scope et sa conséquence observable doivent être formulés sans fabriquer de seuil esthétique.

| Dial | Pôle bas | Pôle haut | Vérification |
|---|---|---|---|
| Variance | Prévisibilité, répétition, repères stables. | Surprise, contraste et rupture justifiée. | La variation aide-t-elle le parcours ? |
| Motion | Continuité minimale, feedback discret. | Expressivité au service du repérage, de la causalité ou de la matière. | La motion améliore-t-elle la compréhension ? |
| Densité | Respiration et focalisation. | Information utile par viewport et accès rapide. | La densité reflète-t-elle une décision réelle ? |
| Contraste | Différence contenue, transitions douces et hiérarchie calme. | Seuils nets, opposition et signal prioritaire. | Le contraste clarifie-t-il sans écraser les états ou la lecture ? |
| Matérialité | Planéité, abstraction et économie de surface. | Texture, volume ou présence tactile. | La matière porte-t-elle une relation ou seulement une décoration ? |
| Voix typographique | Neutralité fonctionnelle et continuité. | Personnalité, rythme éditorial ou expressivité contrôlée. | La voix survit-elle à la locale, au contenu long et au reflow ? |
| Formalité | Proximité, spontanéité et adresse directe. | Institution, précision et distance maîtrisée. | Le registre correspond-il au contexte de confiance et au public ? |
| Intensité émotionnelle | Retenue, calme et juste distance. | Énergie, chaleur ou impact immédiat. | L’intensité sert-elle la relation sans masquer la tâche ? |
| Originalité | Convention appropriée et repères familiers. | Écart structurel ou expressif défendu. | L’écart produit-il une compréhension, une mémoire ou une valeur située ? |

Aucun dial ne neutralise une exigence d’accessibilité, de contexte critique, de preuve ou de direction retenue. Les dials sont des hypothèses de jugement de SAVOIR ; ACTION vérifie leurs conséquences avec ses méthodes, gates, statuts et verdicts. Ils sont choisis après `DOMAIN-FRAME` et `CREATIVE-BOOT`, seulement s’ils changent une décision ; une position extrême est une décision à défendre, non un style à démontrer. La position retenue, l’alternative ou l’absence justifiée, la contre-indication et la conséquence observable doivent pouvoir être reliées au premier objet.

### Styles visuels, culturels et multi-médias

Un profil peut s’exprimer dans le graphique, l’interface, l’image, le mouvement, le son, l’espace ou la matière, selon le médium. Le nom du profil ne fixe donc pas une technique. `STYLE/DIGITAL_MEMORY` peut conduire à une typographie, une animation, un son, une texture ou une logique de navigation ; `STYLE/TACTILE_VOLUME` peut concerner une illustration, une interaction, une scène 3D ou un feedback haptique. Toute traduction doit déclarer le médium, les capacités disponibles, les contraintes de production et la preuve adaptée.

Le style est une hypothèse de direction, jamais un raccourci de secteur. Ne déduis pas qu’une marque culturelle doit être maximaliste, qu’un outil financier doit être minimaliste ou qu’un produit technique doit être cyberpunk. Le produit, le JTBD, le public, la donnée, la culture et la contrainte déterminent si une expression est pertinente.

### Ponctuation située : le tiret cadratin n’est pas une signature

Le tiret cadratin (`—`) n’est ni interdit ni recommandé par défaut. Utilise-le lorsqu’il exprime réellement une rupture, une apposition, une relation éditoriale ou une voix locale compatible avec la langue et le support. Dans une instruction, une microcopie, un label ou une trace, préfère la ponctuation qui rend la relation la plus précise : point pour séparer deux décisions, deux-points pour introduire une explication, virgule pour une incise courte, point-virgule pour deux propositions étroitement liées, ou aucune ponctuation si le label doit rester compact.

Un emploi répétitif du cadratin pour donner un rythme « premium », relier artificiellement des clauses, remplacer une relation logique non formulée ou produire une cadence reconnaissable est un signal de **slop stylistique**. Plusieurs cadratins rapprochés ne constituent pas une violation automatique ; ils déclenchent une relecture : le sens, la locale, le reflow, la lecture assistée et la densité de l’interface doivent rester meilleurs avec la ponctuation choisie. Le style doit être identifiable par une décision de contenu, de structure ou de typographie, jamais par une marque de ponctuation répétée.

### Test anti-slop procédural

> **Slop procédural :** trace ou procédure qui respecte la forme attendue sans produire de décision modifiée, d’observation inspectable, de preuve adaptée, de limite explicite ou de prochaine action utile.

Avant de conserver une étape, un tag, un profil ou une formulation, demande : **qu’est-ce qui change si cette ligne est vraie, fausse ou absente ?** Si rien ne change, supprime-la, regroupe-la dans la source propriétaire ou utilise `N/A-JUSTIFIED`. Une procédure qui exige de nommer une décision sans jamais la trancher, qui charge tous les profils, qui répète les mêmes adjectifs ou qui produit seulement des statuts rassurants est du slop procédural, même si sa trace est complète.

Le terme « slop » reste un diagnostic de mécanisme, pas un verdict esthétique. Décris toujours le symptôme observable : répétition de famille visuelle, profil choisi sans décision, claim non vérifié, champ sans effet, jargon non actionnable ou preuve recyclée.

### Vocabulaire à rendre observable

Les termes ci-dessous ne sont pas interdits comme citations, hypothèses ou langage de marque. Ils sont insuffisants comme décision seuls. Lorsqu’ils apparaissent dans une justification, ajoute leur conséquence perceptible, comportementale ou technique et leur contre-indication.

| Terme faible seul | À préciser par | À éviter comme preuve de |
|---|---|---|
| « premium », « luxe », « haut de gamme » | proportion, matière, rareté, prix, public, tâche et signal observé | qualité universelle ou statut automatique |
| « moderne », « contemporain », « actuel » | contraste avec une convention datée, public, usage ou contrainte réelle | nouveauté ou pertinence par défaut |
| « beau », « élégant », « propre » | relation de forme, hiérarchie, rythme, lisibilité ou défaut retiré | direction ou efficacité |
| « original », « créatif », « audacieux » | position choisie, parti (écart au modal), risque assumé et différence perceptible | divergence simplement décorative |
| « intuitif », « simple », « fluide », « seamless » | tâche, étape, état, effort, erreur et preuve d’usage | utilisabilité sans observation |
| « cohérent », « harmonieux », « aligné » | relation précise entre éléments, règle de système et exception | approbation globale non vérifiable |
| « immersif », « impactant », « émotionnel » | effet attendu, contexte, durée, risque de surcharge et preuve située | effet garanti sur tout public |

Cette table ne remplace pas le jugement de contexte. Elle empêche seulement le vocabulaire d’acquitter une décision qu’aucun objet, changement ou test ne soutient.

---
