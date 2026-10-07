# U1b — Fiche d'inventaire n°2 : `V1/official/BIBLIOTHEQUE.md`

**Base :** commit `d90869c`. **Lecture :** intégrale, lignes 1 à 861. **Angle :** ce que le fichier possède et permet de fabriquer. Pas de propositions d'ajout.

## 1. Identité

| Élément | Valeur |
|---|---|
| Taille | 76 460 o, 861 lignes |
| Part compilée dans le noyau | 5 blocs, 4,3 Ko (STRUCT-OU, EXPRESSION, TENSION, ACTIVATION, SIGNAUX) : 6 % du fichier, 10 % du noyau |
| Concepts protégés | 2 (TRM-01 test de trame, PRC-01 contrôle structurel) |
| Catalogue réel | **35 routes** et 6 couches (détail en section 3) |
| Statut des routes | Toutes `SEED`, « canoniques, sans gain mesuré » (`CHANGELOG.md:66`) |

## 2. Rôle

- **Déclaré** (l. 7-9) : système de sélection des **structures d'interface** ; transformer une décision de direction en « structure habitable ».
- **Réel :** trois choses dans un même fichier :
  - une **méthode** de structure : tension, signature, thèse, traduction d'une intention en levier (l. 51-320, environ 39 Ko) ;
  - un **catalogue** de 35 routes nommées (l. 324-644, environ 19 Ko) ;
  - une **gouvernance** du catalogue : composants, compatibilité, gate structurel, évolution (l. 648-861, environ 18 Ko).

## 3. Le catalogue, détaillé

| Niveau | Routes | Ce que chaque entrée contient | Concrétude |
|---|---|---|---|
| **SUPPORT** (où la surface vit) | 4 : FREE_FIELD, ARCHITECTED_FRAME, OPERATIONAL_CANVAS, COLLECTION_PLINTH | Description, « Choisir lorsque », « Éviter lorsque », « Preuve » | O (bien cadrées) |
| **GRID** (comment le regard circule) | 6 : MODULAR, COLUMN, RADIAL, HIERARCHICAL, BASELINE, AXIAL | Description, « Choisir lorsque », « Preuve » ; **pas d'« Éviter lorsque »** | O |
| **SCENE** (comment la promesse devient surface) | 6 : INSTRUMENT, EDITORIAL_FIELD, FRAMED_PRODUCT, OPERATING_GRID, SPLIT_PROOF, PRODUCT_NARRATIVE (BENTO, GLASS_HERO et EDITORIAL_PREMIUM sont cités comme noms **à ne pas créer**, l. 249) | Description, choisir, éviter, et la distinction avec le support voisin | O |
| **OBJECT** (quelle preuve devient tangible) | 9 : EDITORIAL_SELECTION, COMPARISON_SPLIT, MEDIA_ARCHIVE, SYSTEM_DATA_MODULE, PROOF_PRODUCT_STAGE, NAV_CONTEXT_CAPSULE, BRAND_GRAMMAR_PLATE, CONVERSION_CONTEXT_FIELD, CONTROL_VALUE_TILE | **Une seule ligne de responsabilité**, sans choisir, éviter ni états | O, mince |
| **MICRO** (unités denses) | 7 : IDENTIFICATION_GATE, SETTINGS_GROUP, PROFILE_EVIDENCE, QUERY_HEALTH, ENTITY_STATUS_RAIL, ITINERARY_SEGMENTS, USAGE_LEDGER | Responsabilité **et vérification principale**, souvent très précise (QUERY_HEALTH : « quoi, comparé à quoi, depuis quand, avec quelle confiance, que faire ? ») | **A** |
| **MODIFIER** | 3 : FIELD_SWITCH, NAVIGATION_SHELL, PRINT_FIELD | Test ou conditions | A |
| **LAYER** | 6 : TOKENS, BRAND_GRAMMAR, PRIMITIVES, OBJECTS, SCENES, TEMPLATES | Responsabilité et exemples | O |

**Chaque route est une description en texte.** Aucune ne contient de code, de squelette HTML ou CSS, de valeurs, de schéma ni d'image. Le fichier l'assume : « BIBLIOTHEQUE ne devient ni galerie d'assets, ni archive de références visuelles, ni corpus de goût » (l. 787).

## 4. Ce qu'il possède en dehors du catalogue

Niveaux de concrétude : **A** actionnable · **O** orientant · **N** seulement nommé.

| Élément | Lignes | Concr. | Accès |
|---|---|---|---|
| « L'interface déclare d'abord où elle vit, comment le regard circule, quelle preuve devient tangible, comment la personne agit » | 46 | A | **Noyau** |
| Chaîne de responsabilités support → grille → scène → objet → primitive (une carte, pas un ordre) | 55-61 | O | Route |
| Six polarités perceptuelles (calme ou tension, intimité ou monumentalité…) | 66 | O | **Noyau** |
| **7 axes de tension** (DENSITY, FOCUS, PROOF-POSITION, TEMPORALITY, FIELD-MATERIAL, NAVIGATION, ACTION) | 76-84 | A | **Noyau** |
| Signature structurelle (4 champs) | 95-102 | A (gabarit) | Route |
| **Thèse structurelle et « premier objet habitable »** | 104-112 | A | **Route seulement** |
| Types de preuve (PERCEPTUAL, EXPERT, TECHNICAL, USER/TASK) et leur différence avec les méthodes d'ACTION | 133-144 | O | Route |
| Filtre avant catalogue (4 questions) | 154 | A | Route |
| **Table « Traduire une intention en construction »** : 6 relations (calme dense, intimité, précision d'une valeur, monumentalité, rythme, collection) → route → premier levier concret → observation | 164-171 | **A** | Route (l'activation qui y renvoie est au noyau) |
| Question de sélection par niveau ; sélection par mode (LITE et ITER : aucune route) | 183-203 | A | Route |
| Dérivation d'une forme locale (gabarit de 15 lignes, dont 8 avant build) | 223-249 | A (gabarit) | Route |
| **Signaux de convergence** (7) et **test de trame** (« pour un SaaS : promesse, logos, trois bénéfices, tarifs, FAQ ») | 254-269 | A | **Noyau** |
| Contrat de route (18 champs) | 278-298 | A (gabarit) | Route |
| **Calibration locale** : ce qu'il faut rendre concret par dimension (support et grille, objet, voix typographique, image et couleur, comportement) | 310-318 | A, sans valeurs | Route |
| Contrat de grille (UNIT, MARGIN + GUTTER, ANCHORS, RHYTHM, familles MOBILE-*) | 430-450 | A (gabarit) | Route |
| Contrat d'objet, avant/après (8 champs), contrat de composant partagé (13 champs), contrat BRAND_GRAMMAR (15 champs) | 558-706 | A (gabarits) | Route |
| Graphe de dépendance templates → scènes → objets → primitives → tokens | 712 | O | Route |
| Matrice COMPAT (10 supports ou scènes × 3 grilles et objets favorables) | 733-744 | O | Route |
| Gate structurel : 11 tests (non-généricité, silhouette au flou, grille, preuve, asset, clarté, états, mobile, accessibilité, contexte, conséquence) | 763-775 | A | Route |
| Évolution et contrat de gain réel | 793-845 | — (gouvernance) | Route |

## 5. Ce que le fichier ne possède pas

1. **Presque aucune valeur de départ.** Les seuls chiffres sont des exemples « à adapter » : « 12 colonnes », « baseline 8 » (l. 448), un rapport `3:2` (l. 318). La calibration dit **quoi** rendre concret (largeur utile, marges, interligne, longueur de ligne…) mais renvoie les valeurs « à la spec, aux tokens ou au composant du projet » (l. 306). **Les points de départ chiffrés annoncés par DIRECTION n'existent donc ni dans SAVOIR ni dans BIBLIOTHEQUE.**
2. **Aucune implémentation.** Pas de squelette, de composant, de snippet ni de rendu de référence (choix assumé, l. 787).
3. **Aucune preuve d'efficacité.** Les 35 routes sont `SEED`.
4. **Une portée centrée sur le web et l'application.** Toutes les routes décrivent des interfaces : landing, dashboard, réglages, quotas, itinéraires. Rien pour un document, une présentation, une affiche ou une identité, à part `OBJECT/BRAND_GRAMMAR_PLATE` (une planche d'identité) et `MODIFIER/PRINT_FIELD`, qui désigne une texture et non le print.
5. **Les objets sont décrits en une ligne**, sans états ni contre-indication, alors que le contrat d'objet (l. 558-571) exige ces champs pour un objet durable.

## 6. Potentiel présent mais peu exploité

| Élément | Pourquoi il compte au regard de la mission | Accès actuel |
|---|---|---|
| **Table intention → construction** (l. 164-171) | C'est exactement le pont « une intention (calme, intimité, monumentalité) → un levier concret → ce qu'il faut regarder » que la mission demande. | Route ; le noyau y renvoie |
| **Thèse structurelle et premier objet habitable** (l. 104-112) | Relie la structure au rendu ; définit ce qu'est un premier objet « jugeable ». | Route seulement |
| **Les MICRO** (l. 589-597) | Les entrées les plus concrètes du catalogue : chacune dit ce qui doit être lisible. Immédiatement utiles pour des interfaces denses. | Route |
| **Gate structurel** (l. 763-775) | 11 tests rapides, dont « silhouette au flou » et « non-généricité » : les vues que l'agent devrait produire (voir l'idée des vues de perception). | Route ; GATE-C y renvoie |
| **Calibration locale** (l. 310-318) | La liste de ce qu'il faut fixer pour fabriquer. Ce qui manque, ce sont les valeurs. | Route |

## 7. Connexions

- **Vers DIRECTION :** START (classement), VISUAL_TARGET (routes d'asset, l. 787), la chaîne de promotion (l. 31, 841).
- **Vers SAVOIR :** STYLE (l. 37, 150), CRAFT (dérivation, l. 215), STATE et TYPE (calibration, l. 314-315), SYSTEM (composants).
- **Vers ACTION :** HANDOFF (l. 39), GATE-A, B et C (l. 756), B1b (avant/après, l. 616), STRUCTURED-PROOF (l. 308), RUN-SYSTEM.
- **Vers CHANGELOG :** statuts SEED à ABANDONED, migration des anciens alias (l. 845).
- **Vers les outils :** `read_route.py` résout les identifiants structurels (l. 129).

## 8. Observations faites en passant (à verser au registre)

| Observation | Lignes | Lien |
|---|---|---|
| Un **quatrième** bloc FAST-PATH (`BIBLIOTHEQUE/FAST-PATH`) | 175-179 | Étend C22 |
| **Trois jeux d'axes différents** pour la même idée : 7 axes de tension ici, 6 axes de position dans SAVOIR (CFT-02), 6 axes de divergence dans DIRECTION (l. 766-773) | 76-84 | Grilles parallèles (C37) |
| Les GRID n'ont pas d'« Éviter lorsque », contrairement aux SUPPORT et aux SCENE | 380-426 | Asymétrie du catalogue |
| Les tests « par retrait » se multiplient : test de support (masquer texte, données, images, l. 370), test de scène (l. 530), non-généricité (l. 765), silhouette (l. 766) ; s'y ajoutent le test de style et le test de singularité de SAVOIR | — | Confirme l'analyse externe |
| Les 6 avertissements « `N/A-JUSTIFIED` n'est pas une sortie de confort » sont en fait **1 phrase littérale** (l. 179) et des formulations proches répétées (l. 11, 27, 39, 43, 87, 89) | — | Corrige l'analyse externe |

## 9. En une phrase

BIBLIOTHEQUE possède une **bonne méthode pour passer d'une intention à une structure** (tensions, traduction en leviers, test de trame, tests structurels) et un **catalogue de 35 structures d'interface bien délimitées** (quand choisir, quand éviter), mais **uniquement en texte**, sans valeurs, sans implémentation, sans preuve d'efficacité, et pour le web seulement. La moitié de sa méthode la plus utile n'est visible que si l'agent charge la route.
