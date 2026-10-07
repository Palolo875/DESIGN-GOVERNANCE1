# U1b — Synthèse de l'inventaire, par couche de travail

**Base :** commit `d90869c`. **Sources :** les dix fiches U1b (01 à 10), toutes fondées sur une lecture intégrale des fichiers et, pour les affirmations testables, sur des tests reproductibles (T-01 à T-23, dossiers `U1/preuves/` et `U1b/preuves/`). Une seule vérification nouvelle : une recherche sur l'écriture des contenus (§2.6). **Aucune proposition d'ajout** : cette synthèse dit ce qui existe.

## 0. Comment lire cette synthèse

Pour chaque couche, quatre colonnes :

| Colonne | Sens |
|---|---|
| **Donné à l'agent** | Actionnable **et** toujours présent : dans le noyau (`SKILL.md`), ou exécuté par un outil |
| **Possédé, hors du chemin par défaut** | Actionnable, mais seulement dans une route que l'agent doit penser à ouvrir, ou dans un guide qu'il ne lit pas |
| **Seulement évoqué** | Orientant ou nommé, sans moyen d'exécution |
| **Manque** | Absent du paquet |

**Limite essentielle.** « Donné à l'agent » veut dire que le système **le lui donne**, pas que l'agent **le fait**. Aucune mesure n'existe sur ce que l'agent applique réellement ; le système le dit lui-même (« Efficacité : `NOT-VERIFIED` »). C'est l'objet de U2.

---

## 1. Vue d'ensemble

| Couche | Donné à l'agent | Possédé, hors chemin | Seulement évoqué | Manque |
|---|---|---|---|---|
| Brief | **Bon** | **Très riche** | Moyen | Traduction des mots de la personne au noyau |
| Direction artistique | **Bon** | **Très riche** | Moyen | Exemples visuels ; diversité vérifiée |
| Composition et structure | **Bon** | **Riche** (35 routes) | Faible | Valeurs ; implémentation ; vues de masses |
| Typographie | Moyen | Moyen | — | Valeurs ; spécimens ; police réelle observée par défaut |
| Couleur | Moyen | Moyen | — | Exemples ; contraste non textuel |
| Contenu | **Bon** (vérité) | Bon | Écriture | Contrôle outillé ; méthode d'écriture |
| Interactions | Faible | **Bon** | — | Recette au noyau ; options documentées |
| États | Faible | **Bon** | — | Observation d'un autre état par défaut |
| Assets et médias | Moyen | **Bon** | **Fort** (moyens = noms) | Ressources utilisables ; médiums hors web |
| Vérification | Moyen | **Très riche** | — | Captures ; regard extérieur ; hors web |
| Reprise | **Bon** | Bon | Moyen | Mémoire entre runs ; vue d'exécution réelle |
| Le système lui-même | — | **Bon** | — | Une seule mesure d'efficacité |

**Lecture.** Le système est **fort en jugement et en méthode**, **fort en honnêteté de la preuve**, mais **faible dès qu'il faut passer au concret** : valeurs, ressources, images, observation visuelle, médiums hors web. Et ses meilleurs outils sont **hors du chemin par défaut**.

---

## 2. Couche par couche

### 2.1 Brief : comprendre le besoin

| | Contenu | Source |
|---|---|---|
| **Donné** | Prise de brief : au plus trois demandes, en un seul échange, « par gain de plafond » (contenu réel, marque, asset principal, destination) ; chemin court par défaut | Noyau §3 ; DIRECTION l. 350 |
| **Possédé, hors chemin** | **Traduction humaine de START** : 6 questions sans jargon (que doit comprendre, ressentir, faire la personne…) | DIRECTION l. 360-371 |
| | **Vocabulaire à rendre observable** : 7 familles de mots vagues (« premium », « moderne », « intuitif ») et ce qu'il faut préciser | SAVOIR l. 737-749 |
| | FND-03 : cinq questions de cadrage et formule JTBD ; fiche d'hypothèse | SAVOIR l. 168-191 |
| | DOMAIN-FRAME : 16 variables et la règle anti-stéréotype (« un produit financier n'est pas minimaliste par défaut ») ; schéma validé | DIRECTION l. 223-250 ; fiche n°8 |
| | « Commencer » (4 questions pour la personne) ; handoff agentique (OBJECTIVE, SCOPE, AUTONOMY…) | README ; QUICKSTART l. 180-195 |
| **Évoqué** | Recherche orientée décision : la fiche de source de SAVOIR (12 rubriques) et le schéma RESEARCH_BRIEF divergent ; le schéma n'est nommé par aucune doctrine | Fiche n°8 |
| **Manque** | La traduction des mots de la personne n'est pas au noyau, alors que c'est le cœur de « exprimer son besoin sans maîtriser la mécanique » | Fiche n°3 |
| | Une contradiction sur le moment de la question : « avant de construire » (README) contre « la première proposition vaut checkpoint » (noyau) | C01, C02 |

**Bilan.** Le meilleur du brief (6 questions humaines, mots vagues, anti-stéréotype) existe déjà et il est bien écrit. Il est simplement hors du chemin par défaut.

### 2.2 Direction artistique

| | Contenu | Source |
|---|---|---|
| **Donné** | Rôle de DA senior ; « première idée = hypothèse à tester contre la convergence » ; promesse → objet de preuve → geste ; MODAL et PARTI ; test de singularité ; question de convergence (palette, police) ; marqueurs de vague datés (résumé) ; varier un axe à la fois ; plafond de fabrication ; ancre graduée | Noyau §1, §3, §5, §6 |
| **Possédé, hors chemin** | **RUN-PRIORITY et NO-GO** (vérité → direction → premier objet → finition ; « dashboard décoratif », « cartes avant le mécanisme »…) | DIRECTION l. 333-347 |
| | **Contrat positif du premier objet** : 8 dimensions, « suffisant quand… » et « retour si… » | DIRECTION l. 386-401 |
| | Creative Boot (12 décisions) ; VISUAL_TARGET (11 champs) ; DIRECTION-ATELIER (critique par verbes) | DIRECTION |
| | **REUSE-CHALLENGE** : lire l'antécédent dans les traces, jamais de mémoire ; seul mécanisme contre la répétition entre runs | DIRECTION l. 420-433 |
| | CFT-04 émotions (5 intentions, leviers, contre-indications) ; **CFT-04a** objet ou geste d'abord (« aucun ne gagne par défaut ») ; CFT-02 axes de position ; STYLE (8 profils, test de style) ; direction divergente | SAVOIR ; DIRECTION |
| | `creative_direction_set` : au moins deux directions avant de choisir, validé | Fiche n°8 |
| **Évoqué** | CFT-00 (8 dimensions de qualité) ; trois lois ; pluralité esthétique. **Trois jeux d'axes concurrents** (7 tensions, 6 positions, 6 divergences) | Fiches n°1, 2, 4 |
| **Manque** | **Aucun exemple visuel**, aucune image de référence, aucun avant/après archivé | Fiches n°1, 3 |
| | La diversité n'est vérifiée que par la forme (deux directions identiques à un point près sont acceptées, T-18) | Fiche n°8 |
| | Une vue unifiée de la méthode : elle est éclatée en 7 modules voisins | Fiche n°4 |
| **Gardes machine** | 18 marqueurs de tendance seulement sur une ligne datée (LCF-46) ; aucun « style universel » (UNI-01) | Fiche n°10 |

**Bilan.** C'est la couche la plus aboutie en méthode. Le noyau porte un premier niveau solide. Les outils de **décision** (priorités, contrat du premier objet, anti-répétition) restent en route. Le noyau ne porte qu'un côté de CFT-04a (l'objet d'abord), ce qui peut pousser vers une seule forme.

### 2.3 Composition et structure

| | Contenu | Source |
|---|---|---|
| **Donné** | Grammaire intention → tension → foyer → masse → rythme → … → retenue ; forme située (formule) ; contrôles d'alignement et de responsive (recomposer, pas comprimer) ; 6 polarités ; 7 axes de tension ; 7 signaux de convergence ; **test de trame** (« pour un SaaS : promesse, logos, trois bénéfices, tarifs, FAQ ») | Noyau §4, §5 |
| **Possédé, hors chemin** | **Catalogue de 35 routes** (4 SUPPORT, 6 GRID, 6 SCENE, 9 OBJECT, 7 MICRO, 3 MODIFIER) et 6 couches ; « choisir lorsque / éviter lorsque » | BIBLIOTHEQUE l. 324-644 |
| | **Table intention → construction** (calme dense, intimité, monumentalité… → route → premier levier → observation) | BIBLIOTHEQUE l. 164-171 |
| | Thèse structurelle et premier objet habitable ; calibration locale (quoi fixer) ; contrats de grille, d'objet ; **gate structurel** (11 tests, dont silhouette au flou) ; matrice COMPAT ; carte de hiérarchie | BIBLIOTHEQUE ; ACTION |
| **Évoqué** | Chaîne support → grille → scène → objet ; types de preuve | BIBLIOTHEQUE |
| **Manque** | **Aucune valeur de départ** (seuls exemples : « 12 colonnes », « baseline 8 », « 3:2 »), (choix assumé par DIRECTION l. 137, et non promesse non tenue) | Fiches n°1, 2 |
| | **Aucune implémentation** (squelette, composant, rendu de référence) | Fiche n°2 |
| | Aucun outil pour produire la « vue de masses » ou la « silhouette au flou » demandées | Fiches n°5, 6 |
| | Web seulement ; 35 routes SEED, aucun gain mesuré ; les 9 OBJECT tiennent en une ligne | Fiche n°2 |

**Bilan.** Le noyau donne une vraie grammaire et un test anti-banalité (la trame). Le catalogue est riche mais **textuel, sans valeurs ni code, et web seulement**.

### 2.4 Typographie

| | Contenu | Source |
|---|---|---|
| **Donné** | Critères de choix (langues, chiffres, licence, performance, fallback, ton) ; équilibre d'un titre ; comparer au moins deux voix sur le vrai titre ; plancher protégé par le validateur | Noyau §5 ; fiche n°10 |
| **Possédé, hors chemin** | Une ou deux voix expressives ; polices variables ; preuve typographique (5 axes, 4 cas) ; **partition typographique** (5 rôles × 8 colonnes) ; calibration « voix typographique » (graisse, taille, interligne, longueur de ligne sur le vrai titre) | SAVOIR l. 416-447 ; ACTION l. 671-681 ; BIBLIOTHEQUE l. 314 |
| **Évoqué** | Sources nommées (Google Fonts, Fontshare) sans recette d'intégration | SAVOIR l. 923-933 |
| **Manque** | Échelle, interlignage, longueur de ligne : **aucune valeur** | Fiche n°1 |
| | Aucune paire, aucun spécimen | Fiche n°1 |
| | **Par défaut, `check_render` bloque les polices externes** : le rendu est jugé avec la police de repli. L'option `--allow-external` existe, mais elle n'est documentée nulle part (testé : 2 → 0 requêtes bloquées) | Fiche n°6 ; C39 |

**Bilan.** Le jugement typographique est bon. Mais rien n'aide à **choisir concrètement** ni à **observer la vraie police**.

### 2.5 Couleur

| | Contenu | Source |
|---|---|---|
| **Donné** | Palette par rôles (surfaces, textes, actions, états, frontières) ; répartition neutres et accents comme décision ; question de convergence ; **contrôle de contraste du texte** par `check_render` (WCAG, rigoureux), mais seulement si l'agent lance l'outil | Noyau §5 ; fiche n°6 |
| **Possédé, hors chemin** | OKLCH ; dark mode recomposé ; gamut ; leviers de couleur dans CFT-04 ; politique de contraste (WCAG 2.2, APCA en complément) | SAVOIR l. 398-400 ; ACTION l. 988 |
| **Manque** | Aucune palette d'exemple ; **contraste non textuel** (bordures, icônes) non mesuré ; ratio d'un texte conforme non rapporté | Fiche n°1 ; C21 |

**Bilan.** Couche correcte en principes, avec le seul contrôle chiffré fiable du paquet (le contraste du texte). Rien pour aider à composer une palette.

### 2.6 Contenu

| | Contenu | Source |
|---|---|---|
| **Donné** | **Vérité de scène** : exemples marqués plutôt qu'emplacements vides ; action principale fonctionnelle avec valeur d'exemple marquée ; fonctions d'un produit fictif marquées ; données d'exemple cohérentes ; labels `TRUTH/*` ; texte sur image | Noyau §3, §5 |
| **Possédé, hors chemin** | Concepts protégés HON-01, CNT-01, EXD-01 ; architecture par tâche et vocabulaire utilisateur ; fiche claim (10 champs) | SAVOIR ; DIRECTION ; fiche n°10 |
| **Évoqué** | « Contenu honnête », contrôle manuel de GATE-A ; « voix » comme axe de position (CFT-02) | ACTION ; SAVOIR |
| **Manque** | **Aucun contrôle outillé du contenu** (marquage « exemple », chiffres cohérents, affirmations inventées) | Fiches n°5, 6 |
| | **Aucune méthode d'écriture** repérée : la microcopie et les libellés n'apparaissent que comme catégorie de correction (« fix local de libellé », « correction de microcopie ») | Recherche littérale : DIRECTION l. 168, 174 ; SAVOIR l. 633 |

**Bilan.** L'**honnêteté du contenu** est une force du noyau. L'**écriture** du contenu n'a pas de méthode propre.

### 2.7 Interactions

| | Contenu | Source |
|---|---|---|
| **Donné** | Le premier geste dans la séquence promesse → objet → geste ; le déclencheur `ACTION/UI-UX-REALITY` dans CHARGE pour une surface nouvelle | Noyau §2, §3 |
| **Possédé, hors chemin** | **UI/UX REALITY** : premier geste, feedback, contrat de production en 9 lignes ; `ui_ux_reality_pack` validé ; motion comme système d'états ; contrat de motion ; MICRO (unités denses très précises) | ACTION l. 122-140 ; SAVOIR ; BIBLIOTHEQUE |
| | **`check_render`** : parcours clavier réel, focus visible, taille des cibles, noms accessibles, mouvement réduit ; **`--click`** pour observer un autre état | Fiche n°6 |
| **Manque** | **`check_render` est absent du noyau** (0 occurrence) ; `--click` n'est documenté que dans l'aide du script | Fiche n°6 |
| | Aucun test de comportement au-delà du clavier et d'un clic | Fiche n°6 |

**Bilan.** Le paquet sait **décrire et observer** les interactions de base. Mais l'agent ne rencontre ni l'outil ni ses options sur le chemin par défaut.

### 2.8 États

| | Contenu | Source |
|---|---|---|
| **Donné** | Une ligne d'états dans le noyau ; une phrase sur la récupération après erreur | Noyau §5 |
| **Possédé, hors chemin** | Liste d'états (focus, vide, erreur, overflow, chargement, permission refusée, image absente, valeur extrême) ; **RCV-01**, recette complète de récupération ; matrice d'états d'UI/UX REALITY ; **test de résilience** (5 transformations) ; `ui_ux_reality_pack`, **dont le validateur interdit qu'un état disparaisse par omission** | SAVOIR l. 519-524 ; ACTION ; DIRECTION l. 615-625 ; fiche n°8 |
| **Manque** | Par défaut, `check_render` n'observe que l'**état initial** ; un autre état exige `--click`, non documenté | Fiche n°6 |

**Bilan.** Bonne matière sur les états, presque entièrement hors du noyau. L'observation ne montre par défaut que l'état initial.

### 2.9 Assets et médias

| | Contenu | Source |
|---|---|---|
| **Donné** | Plafond de fabrication déclaré ; **aucun faux asset** ; traitement des assets moyens (recadrage, étalonnage, duotone, grain, trame) ; calibrations par domaine (cinéma, édition, affichage…) ; carte des moyens **en résumé** | Noyau §6 |
| **Possédé, hors chemin** | **Six routes de production d'asset** (CODE-NATIVE, FOURNI, CURATÉ, GÉNÉRÉ-DIRIGÉ, HYBRIDE, SANS-ASSET) ; **fiche d'asset directeur** (exige le **moyen réellement accessible**) ; test d'utilité d'une ancre ; contre-épreuve | DIRECTION l. 479-496 ; ACTION l. 685-698 ; SAVOIR |
| | **Table par médium** (web, natif, image, identité, **print, document, présentation**, motion, son, spatial) ; 5 responsabilités de preuve hors web ; profils « scène » et « hors web » de GATE-A | SAVOIR l. 831-852 ; ACTION l. 804-809 |
| **Évoqué** | **La carte des moyens n'est qu'une liste de noms** (Google Fonts, Fontshare, Lucide, Phosphor, shadcn, Radix, Wikimedia, Unsplash, Figma) : ni statut, ni licence vérifiée, ni recette | C38 ; fiche n°1 |
| **Manque** | **Aucune ressource utilisable** directement (police, icône, image, composant) | C38 |
| | **Aucune méthode de composition hors écran** ; aucune observation outillée d'un document, d'une présentation ou d'une image | Fiches n°1, 2, 6 |
| | Les ressources externes sont bloquées par défaut dans l'observation (C39) | Fiche n°6 |

**Bilan.** L'honnêteté sur les assets est exemplaire (pas de faux, plafond déclaré, six routes). Mais la promesse de ta mission (« déboucher sur une possibilité concrète de fabrication ») **n'est pas tenue pour les moyens** : ce sont des noms, pas des moyens.

### 2.10 Vérification

| | Contenu | Source |
|---|---|---|
| **Donné** | Boucle d'édition ; table de diagnostic ; atelier B1b ; revue créative ; 6 questions ; renvoi à GATE-A par profil de surface | Noyau §7 |
| | **`check_render`** : 11 contrôles rigoureux, jamais de faux succès, 125 cas de test. Mais il n'est **pas** dans le noyau | Fiches n°6, 10 |
| **Possédé, hors chemin** | GATE-A (14 contrôles, 4 profils) ; GATE-B (relationnel, regard externe déclaré, corrections ancrées) ; **GATE-C, « geste si absent »** ; preuve visuelle (6 vues) ; **mode agent seul** (ce qu'un agent peut conclure) ; frontière de validation ; fraîcheur ; signaux de réouverture ; test de résilience ; gate structurel | ACTION ; DIRECTION ; BIBLIOTHEQUE |
| | Validateurs : honnêteté **formelle** des fiches de run (un résultat accepté exige observation, provenance, limite) | Fiche n°10 |
| **Manque** | **Aucune capture, aucune vue de masses** produite par un outil du paquet, alors qu'ACTION les exige | Fiches n°5, 6 |
| | **Aucun regard extérieur** sur le chemin par défaut : le jugement perceptuel est une auto-évaluation | Fiche n°5 |
| | Aucune vérification hors web ; captures B1b jamais vérifiées, même en profil strict (T-22) ; substance des fiches non contrôlée (C11, T-18 à T-20) ; CI sans navigateur | Fiches n°5, 8, 9, 10 |

**Bilan.** La doctrine de preuve est la plus honnête et la plus complète du système. **L'instrument de l'observation visuelle manque** : le système demande à l'agent de regarder des images qu'il ne l'aide pas à produire.

### 2.11 Reprise (continuer, corriger, reprendre plus tard)

| | Contenu | Source |
|---|---|---|
| **Donné** | La première proposition vaut checkpoint ; réponse visible en 4 rubriques (« Ce que j'ai fait, Pourquoi, Ce qui manque, La suite ») ; trace légère en 6 lignes ; boucle d'édition | Noyau §8 |
| | `read_route.py` (retrouver une route ou un terme) ; `validate_run_card.py` | Fiche n°6 |
| **Possédé, hors chemin** | Handoff (13 éléments) ; 6 suites possibles (corriger, approfondir, rouvrir…) ; « Comment poursuivre ? » pour la personne ; ITER (rappel de thèse) ; REUSE-CHALLENGE ; fraîcheur de la preuve ; réserves datées avec condition de sortie ; signaux de réouverture | ACTION ; QUICKSTART ; README ; DIRECTION |
| **Évoqué** | **Vue d'exécution dérivée** (snapshot) : décrite, « sur papier » | ACTION l. 376-399 |
| **Manque** | **Aucune mémoire entre runs par défaut** : REUSE-CHALLENGE suppose des traces antérieures que la trace légère ne garantit pas | Fiche n°4 |
| | La recherche ne connaît pas les synonymes (« trop froid » ne mène pas aux émotions), et un test fige ce choix | Fiches n°6, 10 |

**Bilan.** Le premier niveau de reprise (checkpoint, réponse claire, trace légère) est bien conçu et présent. La continuité **entre** runs repose sur des traces que rien ne garantit.

### 2.12 Le système lui-même

| | Contenu | Source |
|---|---|---|
| **Possédé** | **Règle d'évolution** (8 éléments et décision du propriétaire pour tout changement) ; cycle de vie des routes (jamais utilisé) ; règles de retrait si le coût dépasse l'apport | CHANGELOG l. 50, 54-66, 44 |
| | **Indicateurs de mesure déjà définis** (temps jusqu'au premier rendu jugeable, corrections structurelles, corrections utiles, défauts récurrents, regards multiples) et **format `evaluation_case` déjà prêt** | ACTION l. 1084 ; fiche n°8 |
| | Validateurs exemplaires ; builds reproductibles ; CI verte | Fiches n°9, 10 |
| **Manque** | **Aucune mesure n'a jamais été faite.** Chaque révision désigne la même prochaine preuve : « une réalisation complète comparée » | Fiche n°9 |
| **Coût** | Environ **220 formulations verrouillées** par les validateurs ; 6 versions du parcours, au moins 8 tables de routage, 3 jeux d'axes, 4 FAST-PATH | Fiches n°7, 10 |

---

## 3. Sept motifs transversaux

| # | Motif | Couches touchées | Preuves |
|---|---|---|---|
| **M1** | **Les meilleurs outils sont hors du chemin par défaut.** Le noyau ne compile que 4 à 15 % de chaque source. Restent en route : la traduction des mots vagues, les émotions, CFT-04a, RUN-PRIORITY, le contrat du premier objet, la table intention → construction, RCV-01, UI/UX REALITY, `check_render`… | Toutes | Fiches n°1 à 6 ; C15, C16 (charge mesurée) |
| **M2** | **Du savoir sans matière.** Pas de valeurs de départ, pas de ressources utilisables, pas d'images. Le savoir est relationnel **par choix assumé** (DIRECTION l. 137 : les valeurs chiffrées, quand il y en a, sont des points de départ ; BIBLIOTHEQUE l. 787). *Correction du 2026-10-07 : la version précédente parlait à tort de « points de départ annoncés » non tenus* | Composition, typographie, couleur, assets | Fiches n°1, 2 ; C38 |
| **M3** | **L'observation visuelle est exigée mais pas outillée.** Ni capture, ni vue de masses, ni regard extérieur ; l'outil existant n'est pas dans le noyau, a deux options cachées, et bloque les polices par défaut | Vérification, typographie, états, interactions | Fiches n°5, 6 ; C39 |
| **M4** | **Web seulement en pratique.** Les médiums hors écran ont une table de traduction, pas de méthode ni d'observation | Composition, assets, vérification | Fiches n°1, 2, 5 |
| **M5** | **L'honnêteté est contrôlée sur la forme, pas sur le fond.** Excellente doctrine, validateurs rigoureux, mais « ok » passe, et les captures citées ne sont jamais vérifiées | Vérification, reprise | C11 ; T-18 à T-22 |
| **M6** | **Redondance et verrous.** Plusieurs versions des mêmes contenus, et environ 220 formulations verrouillées : la cohérence est garantie, mais chaque simplification coûte | Système | Fiches n°7, 10 ; T-23 |
| **M7** | **Rien n'a été mesuré**, alors que les indicateurs et le format existent déjà | Système | Fiches n°5, 8, 9 |

---

## 4. Au regard de ton critère

Ton critère : « permet-il d'obtenir de **meilleures réalisations**, avec **moins d'effort total**, de **défauts évitables** et de **reprises**, tout en préservant **diversité** et **adaptation** ? »

| Dimension | Ce qui la soutient déjà | Ce qui la freine | Inconnu jusqu'à U2 |
|---|---|---|---|
| **Meilleures réalisations** | Grammaire, craft (13 gestes), test de trame, contrat du premier objet | M2 (pas de matière), M3 (pas de regard) | L'agent applique-t-il le noyau ? Ouvre-t-il les routes ? |
| **Moins d'effort total** | Chemin court, trace légère, checkpoint à la proposition | M1 et M6 : 61 à 134 Ko à lire selon le mode ; méthode éclatée | Coût réel en lecture et en temps |
| **Moins de défauts évitables** | Vérité de scène, `check_render` (contraste, clavier, débordement), UI/UX REALITY | `check_render` hors noyau ; états hors noyau ; polices bloquées | Défauts restants sur un vrai rendu |
| **Moins de reprises** | Contrat du premier objet, signaux de réouverture, gestes de GATE-C | Hors noyau ; pas de captures pour comparer | Corrections structurelles nécessaires |
| **Diversité** | MODAL et PARTI, marqueurs de vague, UNI-01, REUSE-CHALLENGE, deux directions | CFT-04a absent du noyau ; diversité vérifiée par la forme ; pas de mémoire entre runs | Deux runs du même brief divergent-ils ? (B2 du plan) |
| **Adaptation** | Anti-stéréotype de domaine, profils de surface, pluralité esthétique | Web seulement (M4) ; moyens = noms | Cas non web (B4 optionnel du plan) |

---

## 5. Ce que l'inventaire change pour le plan

Ce sont des **constats sur le plan**. Aucune décision n'est prise ici.

1. **U2 (mesure de référence) est confirmée comme la prochaine étape.** Le système l'annonce lui-même dans chaque révision (M7).
2. **U2 n'a rien à inventer pour mesurer.** Les indicateurs d'ACTION (l. 1084) et le format `evaluation_case` existent. On peut les utiliser tels quels pour consigner B1, B2 et B3.
3. **Deux hypothèses à observer en U2, plutôt qu'à supposer.**
   - **H1 :** l'agent ouvre-t-il les routes qui contiennent les meilleurs outils (M1), ou fabrique-t-il seulement avec le noyau ?
   - **H2 :** le jugement sans captures produit-il des défauts que `check_render` ou un regard extérieur auraient vus (M3) ?
4. **Les pistes qui en découleraient sont surtout des déplacements, pas des ajouts.** Exemples : faire entrer `check_render` et ses options dans le noyau, échanger des passages du noyau contre des outils de route plus utiles, donner des valeurs de départ. Elles ne seront tranchées qu'après U2, selon ta règle « pas de complexité non nécessaire ».
5. **Deux ajouts au plan sont à discuter.**
   - Chaque lot de changement respecte la **règle d'évolution** du CHANGELOG : 8 éléments et ta décision (fiche n°9).
   - Chaque lot prévoit la **mise à jour des verrous** des validateurs qu'il touche, soit environ 220 formulations (fiche n°10).
6. **Les décisions D1, D2 et D3 restent en attente.**

## 6. En une phrase

Design Governance possède **un jugement de design riche, une méthode de direction complète et une doctrine de preuve exemplaire**, appuyés par des outils et des validateurs rigoureux. Mais ce qui sert le plus à **fabriquer** (outils de décision, états, observation) est **hors du chemin par défaut**, le passage au **concret** (valeurs, ressources, images, médiums hors web, regard visuel) **manque**, et **rien n'a encore été mesuré**.
