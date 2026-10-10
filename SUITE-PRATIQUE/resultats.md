# Suite pratique : décisions, mouvement et mobile

10 octobre 2026. Le propriétaire reporte la comparaison avec les concurrents et l’anglais. Cette suite continue la consolidation, les lectures utiles, le choix de direction et la mise en pratique mobile. Elle ne relance pas U6.

## Pourquoi les juges ont choisi l’ancienne version

Les deux juges préfèrent F à A et E à C en facturation, mais D (nouvelle version) à B pour le vélo. Leur motif commun est la compréhension du mécanisme et du prochain geste : données et calcul visibles, « Modifier cet exemple » lié au document, bénéfices et engagement précis. Ils reconnaissent à A sa voix à empattements et son document soigné, à C sa concision. Ils n’ont pas décidé qu’une police, une couleur ou une structure devait toujours gagner.

Le [diagnostic](diagnostic/diagnostic-u6.md) relie leurs raisons aux captures et aux traces. Les six principales sources normatives examinées étaient identiques entre les paquets U6 : aucune règle utile perdue n’a été identifiée sur ce périmètre. L’effet du chargement sur l’attention reste une hypothèse. Six pages, deux briefs et deux juges ne permettent pas d’établir une supériorité générale ou une causalité.

## Ce qui change dans le système

La ligne DIRECTION distingue le cadrage avant le premier objet, les lectures pendant fabrication/observation et la formalisation à la sortie. Les contraintes critiques restent lues avant la décision protégée. L’inventaire anticipé de toutes les exclusions est remplacé par les motifs qui changent effectivement une décision, dans la trace existante.

Le savoir insiste sur le lien objet → action → conséquence et sur des alternatives plausibles de la même décision. Les méthodes techniques précisent état correct sans animation, annulation/remplacement, gestes, mouvement réduit, fallback, viewport et particularités des plateformes mobiles. Aucun mode, gate, statut ni champ de schéma n’est ajouté.

Le noyau compilé mesure **18 960 octets** (18 852 précédemment, +108), sous le plafond 46 000. Sur les 43 blocs protégés de la version précédente, **41 corps restent identiques et deux consignes de chargement changent** ; aucun bloc ajouté ou absent. Le [relevé](diagnostic/conservation-suite.json) précise son périmètre. Les nouveaux gestes restent dans le savoir chargé à la demande. Aucun gain général de qualité, variété, durée ou coût API n’est revendiqué.

## Folio : un document devenu instrument mobile

Le [prototype autonome](mobile/index.html) conserve une voix documentaire expressive. Modifier les heures change immédiatement le total ; un panneau permet de modifier les autres données ; erreurs, annulation, reprise et téléchargement local sont disponibles. Le mouvement accompagne l’état sans décider de sa validité. Les fontes et licences sont embarquées, sans dépendance externe.

Le premier passage donne **50 réussites et trois échecs** : le montant extrême déborde pendant son mouvement. Le raccord animé et le repli des textes sont corrigés ; la saisie conserve une quantité sans séparateur de milliers. Le passage final donne **53 réussites, aucun échec** dans Chromium 151, sur contextes neufs. Il couvre calcul, erreurs/correction, focus, fermetures et interruptions, contenu extrême, hauteur réduite, préférence de mouvement réduit, API et stockage absents, téléchargement et gestes tactiles émulés. Voir [parcours finaux](mobile/preuves/parcours.json), [premier passage](mobile/preuves-premier-essai/parcours.json) et [trace](mobile/trace.md).

Une paire à contenu constant compare l’entrée ample et réduite. À 390 et 320 px, seule l’entrée réduite conserve le total dans le premier viewport ; à 1440 px, les deux le conservent. Le coordinateur retient l’entrée réduite pour la tâche, avec une présence éditoriale moindre. Ce choix est explicité après inspection des captures 390 px ; aucun jugement aveugle ou test utilisateur n’est revendiqué. La comparaison porte sur la masse de l’entrée, pas sur deux architectures produit complètes. Voir la [galerie](galerie.html) et les [mesures](mobile/preuves/comparaison/comparaison.json).

Les Gate A sur quatre largeurs ne détectent aucun échec, avec les réserves conservées de leur recette. Le complément vérifie les champs réellement construits : texte 12,88:1, bordure 3,34:1, focus 6,31:1 ; huit cibles de l’éditeur au moins égales à 44 pixels CSS. Les noms/roles sont contrôlés. Ce périmètre ne certifie pas une accessibilité exhaustive. La [projection RUN_CARD](mobile/run-card.json) passe le profil strict et conserve une clôture exploratoire, sans identité réelle acceptée.

## Vérification et intégration

Produit : [`3b79b3a10d2344a52db76f6e6239cf0a91c056c7`](https://github.com/Palolo875/DESIGN-GOVERNANCE1/tree/3b79b3a10d2344a52db76f6e6239cf0a91c056c7), révision `R2026-10-10-PRATIQUE`. `validate_all.py --require-browser` donne **FULL VALIDATION PASSED**, code 0. Lecteur : 84 cas ; budget/activation : 18 ; audit : 68 ; préparation : 9 ; rendu : A 55, C 51, B 33. GitHub : 108 fichiers ; Local : 103. Deux constructions sont comparées et les archives sont reproductibles ; leurs [empreintes](validation/archives.json) sont conservées.

Les premiers essais de validation sont joints séparément : révision de connexions non actualisée, assertion du lecteur confondant texte en gras d’une cellule et début de ligne de mode, puis navigateur bloquant `file://` faute d’activation du mode HTTP déjà prévu dans l’environnement. Les deux corrections de source et l’environnement HTTP explicite conservent les protections. La RUN_CARD mobile a reçu la date de revue exigée par son schéma, puis passe le profil strict.

CI [52](https://github.com/Palolo875/DESIGN-GOVERNANCE1/actions/runs/38079276592) et [53](https://github.com/Palolo875/DESIGN-GOVERNANCE1/actions/runs/38079280463) réussies sur `3b79b3a10d2344a52db76f6e6239cf0a91c056c7`. La PR 1 est fusionnée ; `main` (`4e1f9cc`) possède exactement le même arbre que le commit testé. Voir [la livraison](livraison.md).

## Ce qui reste ouvert

Le Web mobile émulé ne démontre pas le comportement du clavier logiciel, Safari, des gestes système, d’un lecteur d’écran ou la fluidité sur téléphone physique. Le prototype est illustratif et n’assure pas la conformité comptable. Le prochain pas utile est une tâche observée avec un indépendant représentatif et un contrôle matériel ; ajouter de la décoration maintenant ne résout pas ces limites.

La décision esthétique du propriétaire, les jetons API, la charge cognitive et les cibles initiales de lecture restent ouverts. La comparaison concurrentielle et l’anglais sont reportés. Les originaux U6 sont conservés : leurs 1 344 empreintes ont été vérifiées inchangées avant la livraison de cette suite.
