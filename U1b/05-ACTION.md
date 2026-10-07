# U1b — Fiche d'inventaire n°5 : `V1/official/ACTION.md`

**Base :** commit `d90869c`. **Lecture :** intégrale (lignes 1 à 1084), faite le 7 octobre pendant l'unité U1 et reprise ici sous l'angle de l'inventaire ; tailles des sections mesurées par script. **Angle :** ce que le fichier permet d'**observer, prouver, transmettre et reprendre**.

## 1. Identité

| Élément | Valeur |
|---|---|
| Taille | 120 008 o, 1 084 lignes, 24 tables, 12 gabarits |
| Part compilée dans le noyau | 4 blocs, 5,1 Ko (SORTIE, TRACE, CHECKPOINT, BOUCLE-ATELIER) : 4 % du fichier, 12 % du noyau |
| Concepts protégés | 10 (dont les cinq HON- sur l'honnêteté de la preuve, VAL-01, GTA-01) |

## 2. Rôle

- **Déclaré** (l. 7-9) : propriétaire des preuves, gates, statuts, verdicts et de la clôture ; « transforme une direction en livraison observable et améliorable ».
- **Réel :** trois choses dans un même fichier :
  1. une **doctrine de la preuve** : ce qui prouve quoi, et ce qui ne prouve pas ;
  2. un **contrat de sérialisation** : la carte de run et sa validation ;
  3. une **méthode d'exécution** : routes par mode, pipeline de direction, contrats de preuve structurés, gates.

## 3. Répartition du volume (mesurée)

| Partie | Taille |
|---|---|
| Sortie et vocabulaire (HANDOFF, registres, AUTHORITY, STATUS, PRECONDITION, FAST-PATH) | ≈ 24 Ko |
| Carte de run (champs, correspondance, capacités, mode agent seul, snapshot, projection, frontière de validation) | ≈ 18,7 Ko |
| Routes par mode et paquet de clôture | ≈ 11,8 Ko |
| Pipeline de direction, preuves structurées, preuve visuelle | ≈ 22 Ko |
| Gates A, B, C et anti-slop | ≈ 28 Ko |
| Override, politiques, routage, maintenance, test de sortie | ≈ 10 Ko |

## 4. Ce qu'il possède

Niveaux : **A** actionnable · **O** orientant. Accès : **Noyau** ou **Route**.

### Répondre et transmettre

| Élément | Lignes | Concr. | Accès |
|---|---|---|---|
| Réponse visible en 4 rubriques ; système activé en silence | 45-54 | A | **Noyau** |
| Trace légère (6 lignes) et trace complète ; où l'écrire | 61 | A | **Noyau** |
| Handoff pour une reprise (13 éléments) ; forme courte LITE | 35-66 | A (gabarit) | Route |
| La première proposition vaut checkpoint ; un checkpoint avant le build seulement si demandé ou si l'action est irréversible ou coûteuse | 599 | A | **Noyau** |
| Portée d'action et reprise (AUTHORITY) : une capacité n'est pas une autorisation | 98-100 | O | Route |

### Viser la qualité dès le premier rendu

| Élément | Lignes | Concr. | Accès |
|---|---|---|---|
| **Qualité initiale attendue par mode** (LITE, ITER, STANDARD, DIRECTION, SYSTÈME) | 110-118 | A | Route |
| **UI/UX REALITY** : ce que le premier objet doit rendre observable (premier geste, feedback, états loading, empty, error, unavailable, disabled, succès partiel, contenu long, responsive, focus, récupération) et un contrat de production en 9 lignes (modèle de contenu, tâche, geste, états critiques, relation responsive, base d'accessibilité, robustesse, scope attendu et observé) | 122-140 | **A** | Route |

### Organiser la preuve

| Élément | Lignes | Concr. | Accès |
|---|---|---|---|
| Quatre registres : observation → interprétation → décision → persistance | 72-81 | O | Route |
| Ordre de preuve P0 → P3 ; la protection critique passe avant le visuel | 83 | O | Route |
| Vocabulaire des statuts : 7 états, 6 issues, 6 verdicts, 4 statuts de direction, 4 axes V/U/A/T, triade de la conséquence décisionnelle | 146-222 | A (registres fermés) | Route (une partie au noyau) |
| Contrat minimal par mode | 230-239 | A | Route |
| Trace post-build d'EXTERNAL-START : décision changée, **omission évitée**, limite restante | 259-267 | A | Route |
| **Mode agent seul et preuve dégradée** : ce qu'un agent peut et ne peut pas conclure selon ses capacités (avec ou sans capture, sans regard externe, sur risque critique) | 363-372 | **A** | Route |
| Profil de capacités (disponible, indisponible, non requis) et sa base | 352-358 | A | Route |
| Vue d'exécution dérivée (snapshot), qui sait rapprocher connexions, passages propriétaires et trace pour une reprise | 376-399 | O, sur papier | Route |
| **Frontière de validation** : ce qu'une carte validée atteste, et ce qu'elle n'atteste pas | 412-419 | A | Route |
| Fraîcheur de la preuve (un verdict redevient `NOT-VERIFIED` après un changement substantiel) ; cycle de vie des réserves (7 attributs) | 497-517 | A | Route |
| Droits et confidentialité (droit inconnu = pas d'`ACCEPTED` ; ne pas envoyer de données sensibles vers un canal non garanti) | 521-525 | A | Route |
| Condition d'arrêt du polish (`STOP — raison`) | 529 | A | Route |

### Exécuter

| Élément | Lignes | Concr. | Accès |
|---|---|---|---|
| Routes RUN-LITE, ITER, STANDARD, DIRECTION, SYSTEM : entrée, à faire, sortie, clôture | 427-475 | A | Route |
| Paquet de clôture par mode et ce que la machine contrôle | 483-495 | A | Route |
| **Pipeline de direction en 8 étapes** : positions, émotion, alternative, spec, sourcing, sélection contre la facilité, écriture de la direction, vérification du rendu ; comparaison spec contre rendu (`CORRECTED`, `ACCEPTED-DIFFERENCE`, `REMAINING-RISK`) | 533-606 | A | Route |
| Passe créative : 4 questions de clôture (présence, signature, détail de craft, défaut restant) ; niveaux Correction, Précision, Intention | 608-620 | A | Route |

### Contrats de preuve structurés

| Élément | Lignes | Concr. | Accès |
|---|---|---|---|
| Table des déclencheurs (quel contrat est dû, quand) ; « zéro contrat est valide » | 626-640 | A | Route |
| **Carte de hiérarchie** (9 champs) ; preuve d'usage structurée (utilisateur, tâche, contexte, critère) | 644-667 | A (gabarit) | Route |
| **Partition typographique** (5 rôles × 8 colonnes) | 671-681 | A (gabarit) | Route |
| **Fiche d'asset directeur** : route, raison, source et **moyen réellement accessible**, provenance, usage et intégration, desktop et mobile, format et fallback, preuve | 685-698 | **A** | Route |
| Contrat de composant et baseline ; contrat de motion ou scène 3D | 702-714 | A | Route |

### Observer

| Élément | Lignes | Concr. | Accès |
|---|---|---|---|
| **Preuve visuelle** : 6 vues attendues (capture desktop entière, mobile entière, détail, **vue de masses**, état significatif, comparaison des écarts), avec la conséquence si elle manque | 718-734 | A | Route |
| **GATE-A** : contrat de portée (8 lignes), 4 familles de méthodes, adéquation preuve et question, **14 contrôles** fondés sur WCAG 2.2 AA, **4 profils de surface** (vitrine, application, scène, hors web) qui disent quels contrôles sont dus d'office | 738-818 | **A** | Route (le noyau dit « GATE-A selon le profil de surface ») |
| Documentation de la recette `check_render` (ce qu'elle contrôle, ses réserves, sa couverture) | 811-818 | A | Route |
| **GATE-B** : comparaison relationnelle (B1), discrimination sur capture avec atelier (B1b), familles de preuve (B2), regard externe et déclaration de la relation du relecteur (B3), corrections ancrées (B4), trace d'assets (B5), format de sortie (B6) | 821-913 | A | Route (sous-routes lisibles) |
| **GATE-C** : 6 critères de craft (surface, typographie, composition, densité, profondeur, résolution située), chacun avec le **geste à faire s'il manque**, relié au noyau | 917-938 | **A** | Route |
| Politique de contraste (WCAG 2.2 ; APCA en complément) ; règles pour les outils et nouvelles dépendances (7 champs) | 988-1016 | A | Route |

### Clore et mesurer

| Élément | Lignes | Concr. | Accès |
|---|---|---|---|
| FAIL-ASSUMED (échec connu, diffusion limitée) ; péremption des claims et ressources | 952-982 | A | Route |
| Test de sortie en 10 questions, dont « quelle décision a changé grâce à la procédure ? » | 1067-1080 | A | Route |
| **Mesure expérimentale de la méthode** : temps jusqu'au premier rendu jugeable, part des premiers rendus nécessitant une correction structurelle, part des corrections qui changent l'artefact, preuves encore `NOT-VERIFIED` à la clôture, défauts récurrents par mode, perception par plusieurs regards | 1084 | **A** | Route |
| Recette documentaire (11 contrôles de maintenance du corpus) | 1043-1061 | A (gouvernance) | Route |

## 5. Ce que le fichier ne possède pas

1. **Aucun outil pour produire les vues qu'il exige.** La preuve visuelle demande une capture desktop entière, une mobile, une vue de masses, et GATE-C exige « une capture réelle ». La seule recette du paquet (`check_render`) **ne produit aucune capture**. Elle contrôle le DOM et la géométrie (vérifié, fiche n°3 et U1). Les captures dépendent donc entièrement des outils de l'agent.
2. **Aucun regard extérieur sur le chemin par défaut.** B3 décrit très bien comment déclarer un relecteur, mais aucun dispositif n'en fournit un. En trace légère, tout le jugement perceptuel est une auto-évaluation (GATE-C sans verdict écrit, l. 938).
3. **Aucune observation outillée hors web** : les profils « scène » et « hors web » de GATE-A existent, mais aucune recette ne les exécute.
4. **Aucun contrôle de contenu** (marquage « exemple », cohérence des chiffres, affirmations inventées). « Contenu honnête » est un contrôle de GATE-A, mais il reste manuel.

## 6. Potentiel présent mais peu exploité

| Élément | Pourquoi il compte au regard de la mission | Accès actuel |
|---|---|---|
| **Mesure expérimentale** (l. 1084) | Le système définit **déjà** ses propres indicateurs d'évaluation, très proches de votre critère : temps jusqu'au premier rendu, corrections structurelles, corrections utiles, défauts récurrents. Ils n'ont jamais été mesurés. | Route |
| **Qualité initiale par mode** et **UI/UX REALITY** (l. 110-140) | Ce qu'un premier rendu doit déjà contenir selon le type de demande : une checklist de fabrication, pas de preuve | Route |
| **Profils de surface de GATE-A** (l. 804-809) | Disent en 4 lignes quels contrôles d'accessibilité sont dus pour une vitrine, une application, une scène ou un support hors web | Route ; le noyau y renvoie |
| **GATE-C, geste si absent** (l. 927-934) | Le meilleur pont entre un défaut observé et un geste du noyau | Route |
| **Mode agent seul** (l. 363-372) | Dit honnêtement ce qu'un agent sans capture ou sans relecteur peut conclure : la base d'une réponse honnête | Route |
| **Fiche d'asset directeur** (l. 685-698) | Seul endroit qui exige de nommer le **moyen réellement accessible** et le constat qui l'établit (lien avec C38) | Route |
| **Trace post-build : « omission évitée »** (l. 259-267) | Une mesure simple de l'utilité du cadrage | Route |

## 7. Connexions

- **Vers DIRECTION :** START (classement), CHARGE (chargement), VISUAL_TARGET (cible et ancres), DOUBLE-LOOP (boucle), absolus.
- **Vers SAVOIR :** CFT-00 (revue créative), CFT-01 (matrice anti-slop), CFT-02 (alternative), STATE (gestes), TYPE, CONTEXT, TECH, TOOLS, INTEGRITY.
- **Vers BIBLIOTHEQUE :** SELECT, COMPONENTS (contrat de composant), GATE (tests structurels, l. 925).
- **Vers les schémas et scripts :** `run_card.schema.json`, `production_contracts.schema.json`, `validate_run_card.py`, `check_render.py`.
- **Vers le noyau :** GATE-C renvoie aux paragraphes du noyau (§4 à §6), dont un renvoi faux (C12).

## 8. Observations faites en passant (à verser au registre)

| Observation | Lignes | Lien |
|---|---|---|
| La preuve visuelle exige des captures (dont une « vue de masses ») qu'aucun outil du paquet ne produit | 724-731 | Nouveau, relié à l'idée des vues de perception |
| Seconde table de routage vers SAVOIR et BIBLIOTHEQUE (`ACTION/ROUTING`), en plus de CHARGE et de la carte de lecture d'ACTION | 1024-1035 | Lié à C13 |
| Les indicateurs de la mesure expérimentale recoupent ceux du plan U2 : ils peuvent servir de base sans rien inventer | 1084 | Pour U2 |
| La dépendance au chemin de l'agent (captures, relecteur, navigateur) n'est déclarée que dans « mode agent seul » | 363-372 | Lien avec la fiche n°3 (accès) |

## 9. En une phrase

ACTION possède **la doctrine de preuve la plus honnête du système** (ce qui prouve quoi, ce qu'un agent seul peut conclure) et **des outils d'exécution très concrets** : qualité initiale par mode, UI/UX REALITY, profils de surface, gestes de GATE-C, fiche d'asset, et même ses propres indicateurs de mesure. Mais il **exige des observations visuelles qu'aucun outil du paquet ne produit**, il n'offre aucun regard extérieur sur le chemin par défaut, et presque tout reste hors du noyau.
