# Audit du système — structure, navigation, usage, trouvabilité, organisation, hiérarchie, charge cognitive

Date : 2026-10-08. Base : branche `claude/repo-analysis-g87gag`, commit `7d8721c`. Aucun run : mesures sur les sources, le lecteur `read_route.py` et les transcriptions des 9 runs « avec système » déjà faits (U3 : R2, R4, R6, R7 ; U5 : N1 à N5). Outils et données : `AUDIT/outils/`, `AUDIT/donnees/`.

## Résumé

Le savoir est là ; c'est son **accès** qui pêche.

1. **Trouvabilité faible.** Sur 40 besoins réels formulés comme un agent les chercherait (121 termes), 60 % des termes mènent à une route attendue ; 8 besoins sur 40 seulement sont trouvés quel que soit le mot employé. Les termes anglais échouent dans environ deux cas sur trois ; plusieurs formulations naturelles ne donnent rien (« premier écran », « lecteur d'écran », « enfant », « pricing », « shadow »).
2. **Bruit.** Les mots génériques renvoient 20 à 32 routes, la bonne arrivant au 10e ou au 20e rang (« hiérarchie » : 32 routes, rang 19).
3. **Usage réel étroit.** Sur le chemin par défaut, les agents ont lu presque exclusivement la ligne « Charger d'abord » de leur mode ; aucune route de structure de la BIBLIOTHEQUE et aucune de SAVOIR STYLE, STATE, SOURCE, FRAME ou INTEGRITY n'a été ouverte. 24 routes sur 70 n'ont été lues par aucun run. La recherche n'a servi que 7 fois en 9 runs.
4. **Navigation globalement solide**, avec des îlots : 44 routes sont citées dans le noyau, les autres à deux renvois au plus, sauf une poignée sans aucun renvoi entrant.
5. **Charge d'entrée lourde.** En mode DIRECTION, l'agent charge environ 66 000 caractères de routes plus 43 000 de noyau avant toute route conditionnelle (environ 30 000 jetons) ; phrases longues (noyau : 24,7 mots par phrase en moyenne, 43 au 90e centile) ; une centaine de codes en capitales.

Recommandation : **ne pas déplacer le contenu**, améliorer la couche d'accès (lecteur, sommaire, alias, carte des sujets), puis alléger l'entrée.

## 1. Inventaire et organisation

- 5 sources normatives (DIRECTION 105 k, ACTION 121 k, SAVOIR 119 k, BIBLIOTHEQUE 76 k caractères, CHANGELOG) ; guides humains : README 2 k, QUICKSTART 26 k, GLOSSAIRE 14 k, READING_MAP 29 k.
- **70 routes** de premier niveau (DIRECTION 11, ACTION 27, SAVOIR 15, BIBLIOTHEQUE 17). Taille servie médiane 3 600 caractères ; les plus grosses : `SAVOIR/CRAFT` 21 k, `ACTION/RUN_CARD` 18 k, `SAVOIR/STYLE` 15 k, `SAVOIR/STATE` 13 k, `ACTION/PIPELINE-DIRECTION` 12 k, `ACTION/GATE-A` 12 k.
- La table de chargement nomme **37 routes sur 70** ; les 33 autres ne s'atteignent que par renvoi ou recherche.
- **Un propriétaire par concept** est tenu là où il est balisé (26 concepts balisés, aucun en double). Mais les **sujets** sont très dispersés : « capture » et « hiérarchie » apparaissent dans 32 routes, « contraste » 29, « performance » 27, « typographie » et « cible » 26, « mobile » 20. Un agent qui cherche « le » propriétaire d'un sujet ne le distingue pas des mentions secondaires.

## 2. Navigation

- Profondeur depuis le noyau (renvois explicites, formes courtes `SUPPORT/…` comprises) : 44 routes à un pas, une dizaine à deux, deux à trois (`ACTION/POLICIES`, `ACTION/CLOSE-EXIT-CHECK`).
- **Sans aucun renvoi entrant** depuis une autre route : `DIRECTION/SERVICE-BOUNDARY`, `ACTION/PRECONDITION`, `ACTION/MAINTENANCE`, `ACTION/RUN`, `SAVOIR/READ`, `SAVOIR/ROUTING`, `BIBLIOTHEQUE/READ`, `BIBLIOTHEQUE/COMPAT` (les routes de structure SUPPORT, SCENE, OBJECT, MODIFIER sont atteintes par leurs identifiants courts depuis `BIBLIOTHEQUE/SELECT`). Certaines sont des têtes de lecture pour humains ; les autres sont des îlots.
- **Le lecteur ne liste pas les routes.** Aucune option ne montre ce qui existe ; N5 a tenté `--liste` en plein run (option inexistante). La table « Locators principaux » de READING_MAP n'en contient que 25, et l'agent n'interroge READING_MAP que par `--connexions`.
- **Le lecteur plante quand sa sortie est coupée** (`| head` : BrokenPipeError). 17 lectures tronquées par `head`, `sed` ou `cut` dans les transcriptions.

## 3. Usage réel (9 runs avec système)

| Groupe de routes | Runs par défaut (7) | Runs plafond (2) |
|---|---|---|
| Ligne « Charger d'abord » DIRECTION (EXTERNAL-START, CREATIVE-BOOT, VISUAL_TARGET, FIRST-OBJECT, FIRST-RENDER, UI-UX-REALITY, RUN-DIRECTION, PIPELINE, VISUAL_PROOF, GATE-A, GATE-C) | 6 à 7 sur 7 | 2 sur 2 |
| `SAVOIR/TOOLS` (cité dans le noyau, non chargé) | 6 sur 7 | 2 |
| Routes de structure BIBLIOTHEQUE (SUPPORT, GRID, SCENE, OBJECT, MICRO, TENSION, SIGNATURE, CONTRACTS) | 0 | 1 à 2 |
| SAVOIR STYLE, STATE, SOURCE, FRAME, INTEGRITY, TYPE | 0 | 2 |
| `DIRECTION/DIRECTION-ATELIER`, `DOUBLE-LOOP` | 1 et 0 | 2 et 2 |

Lecture : **le noyau et la ligne « Charger d'abord » font le travail ; la colonne conditionnelle n'est presque jamais ouverte**. Une route citée dans le noyau (TOOLS) est lue même sans être chargée. La correction U6 (trancher chaque route conditionnelle, TYPE chargé d'abord) vise ce point, sans mesure à ce jour.

Recherche : 7 appels à `--trouver` en 9 runs (« PRODUCT_NARRATIVE », « tabular », « cible », « enfant », « mineur », « fort enjeu », « Direction divergente ») ; « enfant » et « mineur » n'ont rien trouvé.

## 4. Trouvabilité

Protocole : 40 besoins, 2 à 4 termes chacun (français, anglais, synonymes), succès si `--trouver` renvoie une route attendue. Données : `donnees/trouvabilite.json`.

- Termes : **73 sur 121** trouvent une route attendue.
- Besoins : 37 sur 40 trouvés par au moins un terme ; **8 sur 40** par tous leurs termes.
- **Échecs d'anglais** : shadow, spacing, chart, pricing, keyboard, screen reader, trend, hierarchy, testimonial, target size, screenshot, cards, above the fold.
- **Échecs de vocabulaire français** : « premier écran » (le système dit « premier contact » ou « premier regard »), « lecteur d'écran », « mode sombre » (le système dit « dark mode »), « désactivé » (« disabled »), « texte sur photo », « banque d'images », « preuve sociale », « rédaction », « enfant », « mineur », « données personnelles ».
- **Bruit et rang** : contraste rang 10 sur 29 routes ; typographie 16 sur 26 ; hiérarchie 19 sur 32 ; composant 23 sur 31.
- Recherche **littérale à un seul terme** : pas de synonymes, pas de recherche à plusieurs mots indépendants, pas de classement.

## 5. Hiérarchie et nommage

- **Niveaux de titre incohérents** pour une même notion de route : SAVOIR place 12 routes en titre de niveau 1 ; les autres sources en niveau 2 ou 3.
- **Nommage mixte** : 64 noms de routes sur 70 sont anglais dans un système rédigé en français ; trois utilisent le souligné (`VISUAL_TARGET`, `RUN_CARD`, `VISUAL_PROOF`), les autres le tiret ; quelques noms mêlent les deux langues (`DIRECTION-ATELIER`, `JUGEMENT-COURT`, `PIPELINE-DIRECTION`).
- Les sous-routes (`SAVOIR/CRAFT/CFT-05`, `ACTION/GATE-B/B1b`, `SUPPORT/FREE_FIELD`) suivent trois mécanismes de résolution différents ; elles sont lisibles mais pas listables.

## 6. Charge cognitive

- **Entrée du mode DIRECTION** : environ 66 000 caractères de routes « Charger d'abord » plus 43 000 de noyau, soit environ 30 000 jetons avant toute route conditionnelle ; en trace complète, Gate B, RUN_CARD et CLOSE-PACKAGE ajoutent environ 35 000 caractères.
- **Phrases longues** : 21 à 23 mots en moyenne dans les sources, 24,7 dans le noyau ; un dixième des phrases du noyau dépasse 43 mots.
- **Vocabulaire codé** : une centaine de codes et statuts en capitales (hors locators) dans les sources ; 233 jetons codés en comptant les locators. Le glossaire en couvre 16.
- **Tags** : 18 « [REQUIS PAR LE MODULE] », 10 « [MÉTHODE] ».

## 7. Recommandations (sans run), par gain et par risque

| # | Action | Gain attendu | Risque | Coût |
|---|---|---|---|---|
| 1 | **Lecteur** : sortie silencieuse sur tube fermé ; option `--sommaire` (70 routes, rôle en une ligne, taille, sous-sections) et `--sommaire LOCATOR` (table des matières d'une route, sous-locators lisibles) | L'agent voit ce qui existe avant de choisir | Faible (outil dérivé, testable) | Faible |
| 2 | **Recherche** : alias français et anglais (premier écran → premier contact, désactivé → disabled, shadow → ombre…), recherche à plusieurs mots, résultats groupés par route et classés (titre, noyau, nombre de lignes), 8 premières routes puis « voir tout » | Trouvabilité mesurable : rejouer le test des 40 besoins | Faible ; l'alias ne crée pas de savoir | Moyen |
| 3 | **Carte des sujets** dérivée : pour les sujets dispersés (capture, hiérarchie, contraste, typographie, mobile…), propriétaire puis routes secondaires ; servie par le lecteur | Fin du « 32 routes pour un mot » | Faible si dérivée et vérifiée par un validateur | Moyen |
| 4 | **Îlots** : relier ou déclarer « lecture humaine » les routes sans renvoi entrant | Navigation complète | Faible | Faible |
| 5 | **Entrée allégée** : pour chaque route de « Charger d'abord » en DIRECTION, un « en bref » de trois lignes en tête (ce qu'elle tranche, ce qu'elle produit, quand s'arrêter) ; raccourcir les phrases les plus longues du noyau | Moins de charge, lecture plus sûre | Moyen (fidélité des résumés, verrous) | Moyen |
| 6 | **Nommage et niveaux** : alias français plutôt que renommage ; harmoniser les niveaux de titre de SAVOIR seulement si les verrous le permettent | Lisibilité | Élevé si renommage (locators cités partout) | Élevé |
| 7 | **Carte visuelle du système** pour les humains : qui décide de quoi (DIRECTION mode, ACTION preuve, SAVOIR jugement, BIBLIOTHEQUE structure), et où lire selon la décision | Compréhension d'ensemble | Faible (document dérivé) | Faible |

Ordre proposé : 1, 2, 4 (outil), puis 3 et 7 (cartes dérivées), puis 5 ; 6 seulement si un besoin réel apparaît. Chaque étape se mesure sans run : test de trouvabilité rejoué, routes atteignables, taille d'entrée.

## Limites

Test de trouvabilité construit par l'auditeur (besoins et routes attendues choisis à la main) ; usage observé sur 9 runs seulement ; profondeur calculée sur les renvois explicites ; la charge cognitive est approchée par des tailles et des longueurs de phrase, pas mesurée sur un lecteur.

## Suivi — étapes 1 et 2 appliquées (commit `928d006`)

Lecteur : `--sommaire` et `--sommaire LOCATOR`, recherche par mots entiers et alias, correspondance partielle puis mots séparés, routes classées (8 premières, `--tout`), fin silencieuse sur sortie coupée. `find()` reste littéral.

| Mesure (40 besoins, 121 termes) | Avant | Après (8 premières routes) | Après (`--tout`) |
|---|---|---|---|
| Termes menant à une route attendue | 73 | 98 | 101 |
| Besoins trouvés par tous leurs termes | 8 | 26 | 28 |
| Rang médian de la route attendue | 4 | 1 | 1 |
| Route attendue aux rangs 1 à 3 | 34 termes | 85 termes | 85 termes |

Réserve : les alias ont été construits à partir des échecs de ce test ; le gain sur d'autres formulations n'est pas mesuré. Un second jeu de besoins, écrit sans regarder les alias, donnerait une mesure indépendante.

Échecs restants : surtout des sujets absents du système (enfant, mineur), des mots trop vagues (« vide », « chargé », « poids ») et quelques routes attendues mal choisies par l'auditeur.

## Suivi — étapes 3 et 4 appliquées

- **Îlots (commit `32c71aa`)** : cinq renvois depuis les propriétaires naturels (START → SERVICE-BOUNDARY ; ACTION/RUN → PRECONDITION ; RUN-SYSTEM → MAINTENANCE ; SELECT → BIBLIOTHEQUE/READ et COMPAT ; noyau → SAVOIR/READ et SAVOIR/ROUTING). Résultat : 70 routes sur 70 atteignables depuis le noyau en trois renvois au plus (46, 19, 5) ; seule ACTION/RUN, conteneur des blocs RUN-*, reste sans renvoi entrant.
- **Carte des sujets (commit `8d1c441`)** : section dérivée de READING_MAP, 16 sujets avec propriétaire et renvois ; affichée en tête de `--trouver` ; contrôle SUJ-01 (chaque route citée se résout et traite le sujet).
- **Carte visuelle** : page générée depuis les sources (`AUDIT/outils/donnees_carte.py`, `construire_carte.py`, gabarit dans `CARTE/`), publiée en page privée. Reconstruire après un changement des sources : extraire les données, puis injecter dans le gabarit.

## Suivi — étape 5 appliquée (commit `39ea7a6`)

La mesure a changé le plan. L'« en bref » de trois lignes en tête des routes chargées d'office aurait ajouté environ 5 000 caractères de texte normatif à tenir fidèle, sans rien retirer : il n'est pas fait.

- **Repli des blocs du noyau** à la lecture d'une route : chaque bloc déjà chargé avec la skill devient une ligne de renvoi qui nomme sa section ; `--complet` affiche tout ; `--trouver` marque ces passages « (noyau) ». Gain : mode DIRECTION, trace légère, 69 354 → 62 961 caractères (−9 %) ; trace complète −7 % ; les 70 routes −9 %.
- **Noyau** : trois paragraphes réécrits en phrases plus courtes, contenu inchangé. Effet global faible (24,7 → 24,6 mots par phrase en moyenne).
- **Carte visuelle** : distingue désormais les routes de trace complète (HANDOFF, GATE-B, RUN_CARD, CLOSE-PACKAGE). En DIRECTION : 14 routes d'abord (79 k, START et CHARGE compris), 4 en trace complète (+40 k), 11 si décision.

Limite : la charge d'entrée reste élevée. La réduire vraiment demanderait de retirer ou de déplacer du texte normatif, ce que l'audit déconseille sans mesure de production : les runs plafond, qui lisaient trois fois plus, ont été préférés.
