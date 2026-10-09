# Fiche — V1/official/SAVOIR.md

Fichier lu en entier (1 071 lignes, 123 075 octets, 118 404 caractères), en six morceaux. Les numéros de ligne sont ceux du fichier au commit `9681d4e`. Rien n'a été modifié dans le dépôt.

## Identité

- **Rôle actuel.** Source normative du jugement de design : fondations, craft, typographie, couleur, états, sourcing, styles, contexte, technique, intégrité. Le fichier mêle aussi, dans le même flux, des règles de gouvernance (preuves, statuts, traces) sans les séparer du savoir (`SAVOIR.md:5-32`, `:34-82`, `:1035-1071`).
- **Public réel.** L'agent et le mainteneur du système. Le texte renvoie sans cesse à `ACTION`, `DIRECTION`, `NOT-VERIFIED`, `NEXT-PROOF`, etc. Un designer humain ne peut pas le lire comme un livre sans connaître ces codes.
- **Public visé par la charte.** Designer d'abord (« savoir parcourable par sujet, qui explique le pourquoi, utilisable sans agent »), agent ensuite (« renvois précis, aucune lecture inutile »), équipe. Ce fichier est le cœur du savoir (charte, section 2).
- **Mesures (mesures.md).**
  - 118 404 caractères, 16 760 mots, 616 phrases.
  - Titres : {1 : 13 ; 2 : 19 ; 3 : 40}.
  - Plus grosse section : « Vocabulaire perceptuel », 8 447 caractères.
  - Codes : 30 pour 1000 mots, soit 495 codes (127 routes, 98 composés, 259 capitales, 11 numéros).
  - Non vérifié : 11. Vestiges : 0.
  - Phrases : moyenne 19,3 mots, p90 33, 5 % de plus de 40 mots.
  - Répétitions : 18 fenêtres SAVOIR↔SAVOIR (lignes 923 et 928) ; 18 fenêtres avec ACTION, BIBLIOTHEQUE et DIRECTION (ligne 3) ; 8 avec ACTION et DIRECTION (ligne 545) ; 3 avec DIRECTION (ligne 30).
- **Mesures complémentaires (calculées pour cette fiche).**
  - 18 blocs `noyau` couvrent 16 408 caractères, soit 13,9 % du fichier.
  - Le préambule (lignes 1 à 84) pèse 8 057 caractères avant la première ligne de design.
  - Poids des chapitres H1 : CRAFT 23 013 ; STYLE 15 184 ; STATE 13 177 ; FRAME 11 291 ; TOOLS 9 435 ; INTEGRITY 5 506 (plus 2 785 de « Règles d'or » et « Méthodologie ») ; SOURCE 7 701 ; ATLAS 7 351 ; TECH 6 580 ; TYPE 3 323 ; CONTEXT 3 012 ; SYSTEM 1 963.
  - Estimation à la lecture, à vérifier : un tiers environ du texte (≈ 39 000 caractères) relève de la gouvernance (preuves, fiches, statuts, délégation) et non du savoir de design.

## Verdicts de la grille

| Critère | Verdict | Preuve |
|---|---|---|
| F1 Rôle | à corriger | Les lignes 1 à 3 annoncent « jugement de design : craft, style, contenu, contexte, technique, sources, intégrité » mais le fichier porte aussi un module de preuve et de trace (`:30`, `:586`, `:857-873`, `:975-1031`). Plusieurs rôles : livre de savoir, carte de routage, contrat de preuve. La bannière « V1 expérimentation maintenue » (`:3`) est copiée dans 4 fichiers. |
| F2 Public | à corriger | Aucune ligne ne dit pour qui est le fichier. Le préambule s'adresse à l'agent (`:11`, `:28-32`, `:38-40`). Le contenu (CFT-00 à CFT-05, TYPE, vocabulaire de gestes) intéresse un designer, mais il est enrobé de codes de run. |
| F3 Structure | à corriger | Trois niveaux au plus : conforme. Mais 13 titres de niveau 1 : le titre du document (`:1`) et 12 chapitres, au même niveau. `SAVOIR/READ` (`:34`) et `SAVOIR/ROUTING` (`:66`) sont des routes au niveau 2, alors que `SAVOIR/FRAME` (`:86`) est au niveau 1. `SAVOIR/JUGEMENT-COURT` est au niveau 3 (`:42`). Les sections CFT sont au niveau 2 sous CRAFT, les « Règles d'or » (`:1035`) et la « Méthodologie » (`:1050`) sont au niveau 2 donc rattachées par erreur à INTEGRITY alors qu'elles concernent tout le fichier. Le modèle des titres varie : `SAVOIR/X — …`, `FND-01 — …`, `CFT-04a — …`, titres nus (`:468`). |
| F4 Une seule fois | à corriger | Voir défauts D6 à D9 : 18 fenêtres identiques `:923`/`:928`, et le même test « quelle décision a changé » redit 7 fois (`:112`, `:247`, `:602`, `:648`, `:748`, `:973`, `:1003`). |
| F5 Langue | bloquant pour un lecteur humain | 30 codes pour 1000 mots. Le préambule monte à 62-75 (`:5-32`) et la table de routage à 196 (`:66`). Termes employés avant toute définition : `JTBD` (`:96`, défini `:176`), `slop` (`:122`, défini `:245`), `DECISION-MODIFIED` et `WHEN-USEFUL` (`:247`, définis `:648`), `MODAL` (`:923`, jamais défini ici), `blast radius` (`:772`), axes `V/U/A/T` (`:167`), `P0` à `P3` (`:840`), `same-energy` (`:965`). |
| F8 Longueur | à corriger | Sections de 8 000 caractères ou plus : « Vocabulaire perceptuel » (8 447) et « Goût, références et tendances » (8 201). Chapitres H1 de 13 000 à 23 000 caractères (CRAFT, STYLE, STATE) sans sous-niveau intermédiaire. Une route chargée par l'agent coûte jusqu'à 23 000 caractères. |
| F9 Limites | à corriger | 11 mesures « non vérifié », mais le même avertissement revient 21 fois sous la forme « ne prouve pas / ne remplace pas » (`:9`, `:288`, `:393`, `:483`, `:518`, `:555`, `:588`, `:632`, `:820`, `:849-853`, `:965`…). Les cinq lignes `:849-853` répètent le même schéma « X ne prouve pas Y » pour cinq médiums. |
| F10 Exemples | à corriger | Valeurs et gabarits recopiables, voir la section « Ce qui fige » (CSS `1 px`, formule de rayon, 8 profils fermés, noms de produits). Les tendances sont bien datées `[VEILLE]` (`:928-931`, `:940`), ce qui est conforme. |
| F11 Vestiges | à corriger (léger) | Mesure : 0. À la lecture : renvoi à un état passé « Les anciens identifiants de section sont documentés dans la table de migration de `CHANGELOG.md` » (`:64`) ; consigne de maintenance dans le contenu (« toute évolution de ses cas… se fait ici », `:262`) ; phrase résiduelle d'une déduplication passée (« sa seule définition », `:233`). |

## Sections

Familles : design, produit, gouvernance, méta. Les dispositions sont des propositions, non des décisions.

| Section (ligne) | Ce qu'elle apporte | Famille | Public | Observation principale | Disposition proposée |
|---|---|---|---|---|---|
| Titre, bannière V1 (`:1-3`) | Identité et statut du document. | méta | tous | Bannière recopiée dans 4 fichiers. | Garder le titre ; retirer la bannière d'ici (une seule fois, dans README). |
| Responsabilité (`:5-22`) | Dit ce que SAVOIR est, et ce qu'il ne remplace pas (table de 4 documents). | méta | agent, mainteneur | Dense en codes (75/1000). Table de partage des rôles présente aussi dans les autres fichiers. | Réécrire (forme) en préface de 5 lignes pour un humain ; déplacer la table de partage vers la carte du système. |
| Orientation interne et sortie vers ACTION (`:26-32`) | Dit comment SAVOIR passe la main à ACTION, valeurs de repli. | gouvernance | agent | Recoupe DIRECTION:268 (3 fenêtres). | Déplacer vers la partie gouvernance (module de preuve) ; garder un renvoi. |
| SAVOIR/READ (`:34-46`) et JUGEMENT-COURT | Règle de chargement : zéro à deux routes ; fast path. | méta | agent | Dupliqué par la skill et par `DIRECTION/CHARGE`. Phrase de `:40` de 140 mots environ, verrouillée par `validate_structure.py`. | Déplacer vers le module agent / skill ; garder une phrase de renvoi. |
| Niveaux d'autorité (`:48-62`) | Table des 7 tags (`[DURABLE]`, `[MÉTHODE]`…), leur sens et leur usage. | méta | agent, designer | Utile aux deux publics ; c'est la légende du fichier. Cité par `validate_reading_map.py` (LCF-29). | Garder ; placer en annexe de lecture, après le préambule. |
| SAVOIR/ROUTING (`:66-82`) | Table question vers route principale vers renvoi. | méta | agent | Carte de routage de 11 routes ; DESIGN-ATLAS n'y figure pas. 196 codes/1000. Doublon partiel avec READING_MAP. | Fusionner avec la carte des routes (READING_MAP) ; le fichier garde une table des matières lisible. |
| FRAME / FND-01 principe fondateur (`:86-154`) | Trois lois (intention, retenue, cohérence), premium, singularité, grammaire de composition, pluralité. | design | designer, agent | Le meilleur du fichier. Pluralité (`:146-154`) corrige bien le biais de retenue. Blocs COMP-SINGULARITE et COMP-GRAMMAIRE dans le noyau. | Garder ; tête du livre pour le designer. |
| FRAME / FND-02 compromis (`:156-167`) | Format de décision en 4 lignes. | design | designer, agent | Gabarit fixe de 4 lignes ; renvoie aux axes `V/U/A/T` non définis ici. | Garder ; définir ou retirer les axes. |
| FRAME / FND-03 cadrage et preuve de contexte (`:169-196`) | Questions de cadrage (Qui, Pourquoi, Quelle décision, Quelle preuve, Contraintes). | design (partie) + gouvernance | tous | La table de cadrage (`:173-179`) est du design ; la table de champs d'hypothèse (`:183-190`) est de la gouvernance. | Scinder : cadrage vers design, champs d'hypothèse vers gouvernance. |
| CRAFT / premier rendu (`:202-214`) | Trois moments de qualité ; niveaux Correction, Précision, Intention. | design | agent, designer | Phrase orpheline `:202` (« Dans V1, le polish structurel… ») ; `:212` est une mention de maintenance. | Réécrire (forme) ; retirer les deux phrases méta. |
| CRAFT / CFT-00 qualité créative (`:216-247`) | Huit dimensions de critique ; revue de qualité créative ; définition d'AI slop. | design | tous | Définit « premium » une deuxième fois (`:233`), avec un renvoi défensif. Bloc BOUCLE-REVUE (`:237`). | Garder ; supprimer la redéfinition de premium (`:233`). |
| CRAFT / CFT-01 motivation et construction (`:249-290`) | Matrice 2×2 du slop, forme située, idée par rapprochement. | design | tous | Source canonique déclarée (`:262`). Bloc COMP-FORME. | Garder ; retirer la note de maintenance. |
| CRAFT / CFT-02 registres (`:292-321`) | Six axes de direction, alternative située, un axe à la fois. | design | designer, agent | Bloc BOUCLE-AXE. Recoupe `DIRECTION` (ALT-01) et les dials de STYLE. | Garder ; rapprocher des dials. |
| CRAFT / CFT-03 composition (`:323-354`) | Contrôles, texte sur image, mot et image, champ calme, franchissement, harmonie. | design | designer, agent | Recettes précises (`:340-344`), non étiquetées comme tendance. Blocs COMP-CONTROLES et COMP-TEXTE-IMAGE. | Garder ; étiqueter les gestes de `:340-344` comme exemples. |
| CRAFT / CFT-04 et CFT-04a émotion et premier contact (`:356-393`) | Intentions émotionnelles, hero objet ou geste. | design | designer | Table émotion vers leviers (`:368-374`). Cite des géométries de hero (`:384`). | Garder. |
| CRAFT / CFT-05 couleur (`:395-415`) | Palette par rôles, question de convergence, couleur située, OKLCH, dark mode. | design | designer, agent | Trois blocs du noyau (COULEUR, CONVERGENCE). Aucune règle chiffrée : bon. | Garder. |
| TYPE (`:419-460`) | Choix typographique, variable, équilibre d'un titre, preuve typographique. | design | designer | Court (3 323 caractères) pour un sujet central. Le gabarit `FORM-LEGIBILITY…` (`:444-451`) est de la preuve. | Garder ; déplacer le gabarit de preuve vers la gouvernance. |
| STATE / Jugement visuel situé (`:466-497`) | Six lentilles de jugement ; trois niveaux. | design | designer, agent | Redit les trois niveaux déjà donnés en `:208`. | Fusionner avec CRAFT / premier rendu. |
| STATE / Vocabulaire perceptuel (`:499-526`) | Table de 12 gestes concrets : signal, geste, condition, réinspection. | design | agent, designer | Plus grosse section (8 447). Entièrement dans le noyau (7 883). Le nom « STATE » ne dit pas « gestes de finition ». Phrase orpheline `:526`. | Garder ; renommer la route (voir D3) ; rattacher la phrase `:526`. |
| STATE / États pertinents, récupération (`:528-535`) | États nécessaires, accessibilité de base, récupération après erreur. | produit | tous | Le contenu produit (états, erreurs) est mêlé aux renvois Gate A et Gate C. | Garder ; lien vers la partie produit. |
| SOURCE (`:539-602`) | Ancre, utilité de l'ancre, recherche orientée décision, fiche de source, curation. | design + gouvernance | agent | La fiche de 12 champs (`:571-584`) et la projection machine (`:586`) sont de la gouvernance. Recoupe `ANCHOR-GENERATED` d'ACTION et DIRECTION (`:545`). Blocs MOY-CALIBRATION. | Scinder : sourcing visuel (design) ; fiche et projection (gouvernance). |
| DESIGN-ATLAS (`:606-650`) | Six familles de choix, cartographie, rôles d'asset, médiums, test de sélection. | design + méta | agent | Table de routage bis (`:610-617`). Test de sélection en 7 champs (`:648`). Bloc MOY-ASSETS verrouillé dans cette section (LCF-49). | Garder ; déplacer le test de sélection vers la gouvernance ; laisser MOY-ASSETS en place. |
| STYLE (`:654-768`) | Règle de sélection, taxonomie, 8 profils, usage, 9 dials, ponctuation, anti-slop procédural, vocabulaire à rendre observable. | design + méta | agent, designer | 15 184 caractères. Mélange le style (`:660-736`) et trois sujets sans lien (`:738-766`). | Scinder : style (profils, dials) ; déplacer ponctuation, anti-slop procédural et vocabulaire à rendre observable vers CRAFT ou INTEGRITY. |
| SYSTEM (`:770-784`) | Tokens primitifs et sémantiques, formats, stack. | produit / design | équipe | Court, clair, mais très renvoyé (`DIRECTION/START`, `ACTION/RUN-SYSTEM`). | Garder. |
| CONTEXT (`:788-820`) | Contextes à fort enjeu, responsive, motion, espace. | produit | tous | Court pour l'accessibilité (une phrase `:792`). Rien de chiffré. | Garder ; étoffer à part si le propriétaire veut un livre de référence (décision de fond, hors rangement). |
| TECH (`:824-873`) | Preuve par technique, P0 à P3, médiums non web, cinq responsabilités de preuve. | gouvernance + produit | agent, équipe | 5 116 caractères de contrat de preuve par médium. Phrase de `:867` de plus de 100 mots. | Déplacer vers la gouvernance (preuve par médium) ; garder les points de production par médium en design. |
| TOOLS / Claims externes (`:879-907`) | Gabarit de claim (10 champs), promotion. | gouvernance | agent, équipe | Pure gouvernance. | Déplacer vers la gouvernance. |
| TOOLS / Goût, références, tendances, CONVERGENCE, MOYENS (`:909-965`) | Goût, ancrages, observations datées, carte des moyens, niveaux (veille, principe, style, technique). | design + veille | agent | Les paragraphes `:954-965` (tendance, niveaux, same-energy) sont rangés sous `### MOYENS`, hors sujet. Pointeurs du noyau (`:921-924`, `:933-936`) en tête de leurs textes complets. Marqueurs `[VEILLE]` verrouillés (LCF-46/48/50). | Garder ; rattacher `:954-965` à « Goût » ; séparer pointeur et texte (voir D7). |
| INTEGRITY (`:969-1031`) | Test de non-récitation, modes d'échec, contrôle d'intégrité, limites, délégation, faux asset. | gouvernance | agent, équipe | Seule la phrase VER-FAUX-ASSET (`:1022`) est du design. | Déplacer vers la gouvernance ; garder VER-FAUX-ASSET dans le savoir ou dans la vérité du rendu. |
| Règles d'or (`:1035-1046`) | Huit règles de lecture rapide. | méta | agent, débutant | Résumé placé à la fin, rattaché par erreur à INTEGRITY. | Déplacer en tête de document (c'est le résumé du livre) ; réécrire (forme). |
| Méthodologie studio (`:1050-1071`) | Étapes, repasse (BOUCLE-REPASSE), phrase de clôture. | design + méta | agent | Liste d'étapes qui recopie le chemin d'un run. | Fusionner avec la boucle d'édition ; garder BOUCLE-REPASSE. |

## Défauts

| n° | Type | Gravité | Preuve | Proposition |
|---|---|---|---|---|
| D1 | structure | important | 13 titres de niveau 1 : titre du document `:1` et 12 chapitres `:86`, `:200`, `:419`, `:464`, `:539`, `:606`, `:654`, `:770`, `:788`, `:824`, `:877`, `:969`. Deux routes au niveau 2 (`:34`, `:66`). | Un seul niveau 1 (le titre). Chapitres au niveau 2, sections au niveau 3. Attention : `read_route.py:41` accepte tout niveau (`^#+`), mais `validate_reading_map.py:561` cherche le texte `# SAVOIR/DESIGN-ATLAS` avec un seul dièse. |
| D2 | structure | important | `## Règles d'or` (`:1035`) et `## Méthodologie studio` (`:1050`) tombent sous `# SAVOIR/INTEGRITY`. Sections orphelines : `:202`, `:526`, `:954-965` sous `### MOYENS`. | Replacer ces blocs à leur place logique. |
| D3 | structure | important | La route `SAVOIR/STATE` (`:464`) est nommée « craft, composants et états » mais porte les 12 gestes de finition (7 883 caractères). L'agent la trouve via « Cohérence de rayon » (contrôle `validate_all.py:131`). Le chapitre STYLE (`:738-766`) contient trois sujets étrangers au style. | Renommer ou scinder après décision ; garder l'alias pour les contrôles. |
| D4 | langue | important | Titres de chapitre en forme de code : `SAVOIR/FRAME`, `FND-01`, `CFT-04a`. 495 codes, 30/1000 mots. Préambule à 62-75/1000 (`:5-32`). | Titres lisibles par un humain ; localisateur en deuxième ligne ou alias. Définir chaque terme à sa première apparition (liste dans F5). |
| D5 | coût de lecture | important | 8 057 caractères avant le premier contenu de design (`:1-84`) : responsabilités, orientation, chemin minimal, tags, table de routage. | Placer le préambule agent dans un module séparé ; ouvrir le fichier par une page « ce que ce livre enseigne » et la table des matières. |
| D6 | répétition | important | Test « quelle décision a changé / si cette ligne est fausse ou absente » : `:112`, `:247`, `:602`, `:648`, `:748`, `:973`, `:1003`. Idée « théâtre procédural / slop procédural / récitation » : `:266`, `:744-750`, `:971-973`, `:977`, `:1004`. | Une seule formulation, dans INTEGRITY ; renvoi partout ailleurs. |
| D7 | répétition | important | Mesure : 18 fenêtres SAVOIR↔SAVOIR. Pointeur du noyau `:923` redit presque mot pour mot `:928` ; `:935` redit `:940`. Cause : le bloc `noyau` est un pointeur, le texte complet vient juste après. | Garder le pointeur seulement dans la skill (ou le générer depuis la section) ; supprimer la copie dans SAVOIR. Voir les contrôles verrouillés (LCF-46/48/50). |
| D8 | répétition | mineur | « Premium » défini en `:102-106`, redéfini en `:233`, déconstruit en `:373` et `:758`. Singularité testée en `:116`, `:479`, `:226-227`. Trois niveaux (Correction, Précision, Intention) en `:208` et `:485-491`. | Une définition, des renvois. |
| D9 | répétition | mineur | Avertissement « une capture / un outil ne prouve pas » : 21 occurrences (voir F9). | Une règle générale dans INTEGRITY ; garder seulement la limite propre à chaque médium. |
| D10 | langue | important | Termes d'ACTION imposés dans le savoir : `NOT-VERIFIED`, `N/A-JUSTIFIED`, `NEXT-PROOF`, `DECISION-CHANGE`, `FAIL-ASSUMED`, `CONFORMANCE-TARGET` (`:30`, `:56`, `:588`, `:648`, `:861-871`, `:1012`). | Dans le livre de design, dire « non vérifié » en clair ; réserver les codes à la partie gouvernance. |
| D11 | risque | important | Huit gabarits de champs : cadrage (`:183-190`), compromis (`:162-165`), preuve typo (`:444-451`), fiche de source (`:571-584`), profil (`:666-671`), test de sélection (`:648`), claim (`:883-894`), délégation (`:1018`). Le fichier met en garde contre ce risque (`:744-750`). | Réduire aux champs qui changent une décision ; déplacer le reste vers la gouvernance. |
| D12 | convergence | important | Voir section suivante : formule `rayon intérieur = max(0, rayon extérieur − inset)`, `1 px CSS`, 8 profils nommés, listes de polices et d'outils. | Étiqueter comme exemples, dire « choisis la valeur par la capture », réduire les listes. |
| D13 | obsolète / vestige | mineur | `:64` (table de migration du CHANGELOG), `:233` (« sa seule définition »), `:212` et `:262` (consignes de maintenance dans le contenu). | Retirer ou déplacer vers le fichier de maintenance. |
| D14 | structure | mineur | La route DESIGN-ATLAS n'apparaît pas dans la table `SAVOIR/ROUTING` (`:70-82`), alors qu'elle a sa propre section (`:606`). | Ajouter ou expliquer. |
| D15 | langue | mineur | Phrases de plus de 40 mots (5 %) : `:40`, `:608`, `:648`, `:867`. | Réécrire (forme) en deux ou trois phrases. |
| D16 | visuel | mineur | Marqueurs `<!-- concept:… -->` et `<!-- noyau:… -->` visibles dans le texte brut (18 blocs, `:116` à `:1065`) ; une ligne vide avant la balise de fin coupe un tableau (`:141-142`). | Sans effet au rendu ; à garder tant que `build_core.py` en dépend. |

## Savoir à protéger

- Trois lois du jugement : intention avant décoration, retenue avant accumulation, cohérence avant créativité locale (`:88-100`).
- Premium comme heuristique, pas comme style (`:102-106`).
- Quatre mouvements : comprendre, ouvrir, converger, prouver (`:108-112`).
- Singularité sans rejet des conventions ; test du logo retiré ; recipe-slop (`:114-126`) — bloc COMP-SINGULARITE.
- Grammaire positive de composition en 10 temps et sa table (`:128-144`) — COMP-GRAMMAIRE.
- Pluralité esthétique et goût situé ; trois questions de revue (`:146-154`).
- Format de compromis en 4 lignes (`:156-167`).
- Cadrage : 5 questions, JTBD, hypothèses par nature (`:169-196`).
- Polish structurel et polish expressif (`:202`, `:214`) ; trois moments de qualité (`:204-210`).
- CFT-00 : huit dimensions de qualité créative (`:216-233`) ; revue de qualité créative (`:235-239`, BOUCLE-REVUE) ; composant authored ; définition d'AI slop (`:241-247`).
- CFT-01 : matrice motivation x construction (`:249-266`) ; idée par rapprochement (`:268`) ; forme située (`:270-290`, COMP-FORME).
- CFT-02 : six axes de direction ; alternative située ; un axe à la fois (`:292-321`, BOUCLE-AXE).
- CFT-03 : contrôles de composition (`:323-333`, COMP-CONTROLES) ; texte sur image (`:335-338`, COMP-TEXTE-IMAGE, TXI-01) ; mot et image, champ calme, franchissement (`:340-344`) ; cohérence et harmonie (`:346-354`).
- CFT-04 et CFT-04a : émotion, premier contact objet ou geste (`:356-393`).
- CFT-05 : couleur par rôles, convergence, couleur située, OKLCH, dark mode (`:395-415`, COMP-COULEUR, COMP-CONVERGENCE).
- TYPE : choix typographique, variable, signature (`:419-433`, COMP-TYPO) ; équilibre d'un titre (`:435-438`, COMP-TITRE, TIT-01) ; preuve typographique (`:440-460`).
- STATE : six lentilles de jugement (`:468-483`) ; trois niveaux (`:485-497`) ; 12 gestes de finition (`:499-526`, COMP-VOCABULAIRE, FIN-01) ; états nécessaires (`:528-532`) ; récupération après erreur (`:534-535`, RCV-01).
- SOURCE : ancre et ses voies (`:541-545`) ; test d'utilité (`:547-559`) ; lot d'assets et registre d'illustration (`:561-563`) ; recherche orientée décision et fiche de source (`:565-590`) ; calibration (`:596-598`, MOY-CALIBRATION) ; contre-épreuve (`:600-602`).
- DESIGN-ATLAS : six familles (`:610-617`) ; cartographie (`:619-632`) ; traitement des assets moyens (`:634-636`, MOY-ASSETS) ; rôles d'asset (`:638-640`) ; médiums (`:642-644`) ; test de sélection et frontière maintenance/design (`:646-650`).
- STYLE : règle de sélection (`:660-679`) ; taxonomie (`:681-695`) ; 8 profils (`:697-706`) ; test de style (`:708-712`) ; 9 dials (`:714-730`) ; styles multi-médias (`:732-736`) ; ponctuation et cadratin (`:738-742`) ; anti-slop procédural (`:744-750`) ; vocabulaire à rendre observable (`:752-766`).
- SYSTEM : tokens, interopérabilité, stack existante (`:772-784`).
- CONTEXT : contextes à fort enjeu, responsive, motion, espace (`:792-820`).
- TECH : preuve par technique (`:826-836`) ; P0 à P3 (`:838-840`) ; production et observation par médium (`:842-855`) ; cinq responsabilités de preuve (`:857-873`).
- TOOLS : claims (`:879-907`) ; goût (`:911-917`) ; veille, vagues, écran d'accueil, signaux de page (`:919-931`, COMP-VAGUES, ANT-01, `[VEILLE]` verrouillés) ; carte des moyens (`:933-952`, MOY-CARTE, MOY-01) ; niveaux signal, principe, style, technique (`:954-965`).
- INTEGRITY : non-récitation (`:971-973`) ; modes d'échec et huit questions (`:975-1004`) ; contrôle d'intégrité (`:1006-1012`) ; limites et délégation (`:1014-1031`) ; faux asset (`:1020-1025`, VER-FAUX-ASSET, HON-02).
- Niveaux d'autorité : sept tags (`:48-62`) ; chemin minimal (`:40`) ; règles d'or (`:1035-1046`) ; repasse (`:1063-1071`, BOUCLE-REPASSE).

### Blocs `noyau` copiés dans la skill

18 blocs, 16 408 caractères. Source normative ici ; la copie dans `skills/design-governance-practice/SKILL.md` est générée par `scripts/build_core.py` (jamais modifiée à la main, comparée par `validate_structure.py`).

| Bloc | Lignes | Caractères | Section d'origine |
|---|---|---|---|
| COMP-SINGULARITE | 116-118 | 254 | FRAME |
| COMP-GRAMMAIRE | 130-142 | 1 003 | FRAME |
| BOUCLE-REVUE | 237-239 | 921 | CFT-00 |
| COMP-FORME | 274-278 | 378 | CFT-01 |
| BOUCLE-AXE | 309-317 | 496 | CFT-02 |
| COMP-CONTROLES | 329-331 | 287 | CFT-03 |
| COMP-TEXTE-IMAGE (TXI-01) | 335-338 | 504 | CFT-03 |
| COMP-COULEUR | 397-399 | 512 | CFT-05 |
| COMP-CONVERGENCE | 401-403 | 631 | CFT-05 |
| COMP-TYPO | 421-423 | 207 | TYPE |
| COMP-TITRE (TIT-01) | 435-438 | 925 | TYPE |
| COMP-VOCABULAIRE (FIN-01) | 503-524 | 7 883 | STATE |
| MOY-CALIBRATION | 596-598 | 387 | SOURCE |
| MOY-ASSETS | 634-636 | 547 | DESIGN-ATLAS |
| COMP-VAGUES (ANT-01) | 921-924 | 402 | TOOLS |
| MOY-CARTE (MOY-01) | 933-936 | 375 | TOOLS |
| VER-FAUX-ASSET (HON-02) | 1020-1023 | 308 | INTEGRITY |
| BOUCLE-REPASSE | 1063-1065 | 388 | Méthodologie |

Deux de ces blocs (COMP-VAGUES, MOY-CARTE) sont des pointeurs qui précèdent le texte complet, d'où les 18 fenêtres répétées. Déplacer ou renommer un bloc exige de relancer `build_core.py` ; le plafond de la skill est de 46 000 octets, et COMP-VOCABULAIRE seul en occupe près de 18 % (7 883 sur 42 978).

## Ce qui fige ou pousse à la convergence

- **Gestes chiffrés dans le noyau lu à chaque run.**
  - `rayon intérieur = max(0, rayon extérieur − inset)` (`:509`).
  - Liseré clair de **1 px CSS** sur le bord supérieur avec ombre opposée atténuée (`:513`).
  - Décalage de **1 px CSS** pour l'alignement optique (`:519`).
  - `font-variant-numeric: tabular-nums` (`:514`).
  - `text-wrap: balance` (`:437`).
  - Les conditions « si… » et « tester » atténuent le risque. Le liseré supérieur clair est pourtant une signature courante de surfaces génériques ; un agent qui « utilise une ligne de la table » l'appliquera souvent. Risque réel, mais fréquence à vérifier.
- **Profils fermés** (`:697-706`). Huit profils nommés (`STYLE/RAW_BRUTALISM`, `EDITORIAL_PRECISION`, `PICTORIAL_UTILITY`, `QUIET_SYSTEM`, `MAXIMAL_EXPRESSION`, `DIGITAL_MEMORY`, `TACTILE_VOLUME`, `COLLAGE_ASSEMBLY`), chacun avec une colonne « Expression possible » concrète. Le texte dit « borné et non exhaustif » (`:677`) mais le catalogue reste le plus petit ensemble à portée de l'agent.
- **Tension interne.** `DIGITAL_MEMORY` recommande « pixel, raster, scanline, néon » (`:704`) alors que la vague 3 les classe en marqueurs de convergence (`:928`, « dithering, logos pixel, ASCII »). `EDITORIAL_PRECISION` (`:700`) rejoint la vague 2 (serif de caractère, crème). La veille et le catalogue se contredisent sur des choix à éviter ou à prendre.
- **Dials et axes** (`:296-303`, `:718-728`). Neuf dials et six axes à pôles fixes : cadre utile, mais chaque run les parcourt avec les mêmes mots.
- **Listes de références imposées.**
  - Voix typographiques à comparer : « grotesque, serif, mécane, manuscrite ou vernaculaire du lieu » (`:402`).
  - Listes à éviter : « neutres et un seul accent, sombre et doré, dégradé froid » (`:402`) ; amorçage par la négative.
  - Hero : « trois cards égales, split hero, feuillet » (`:384`).
  - Médiums : liste fermée de 11 (`:644`).
- **Outils nommés** (`:941-948`) : Google Fonts, Fontshare, Lucide, Phosphor, shadcn, Radix, Wikimedia Commons, Unsplash. Datés `[VEILLE 2026-09]` donc conformes à la charte, mais ce sont des choix par défaut déguisés ; shadcn et Radix sont eux-mêmes une source de convergence de pages.
- **Recettes de composition non datées** (`:340-344`) : un sujet passe devant le mot, l'image remplit les lettres, objet minuscule contre titre immense, repères aux coins. Précises, actuelles, sans étiquette de tendance : l'agent peut les recopier telles quelles.
- **Détails de veille issus de runs internes** (`:928`) : « Archivo », « fournées du jour », « facture tamponnée », « bleu Klein ». Utiles pour détecter la convergence, mais à relire avec prudence : ils nomment des sorties précises que l'agent verra (route chargée à la demande, hors noyau).
- **Biais de retenue.** « Retenue avant accumulation » (`:97`), « Retire avant d'ajouter » (`:1041`), « Deux ou trois couleurs tenues valent souvent mieux » (`:407`), retenue comme dimension (`:231`). Contrebalancé par `:148` et `:398` ; l'équilibre est à vérifier sur des sorties.
- **Gabarits de champs** (voir D11) : remplissage mécanique, ce que le texte appelle lui-même « slop procédural » (`:744-750`).

## Dépendances et risques de déplacement

- **Cité par.**
  - Sources : READING_MAP (65 renvois `SAVOIR/…`), DIRECTION (49), ACTION (26), BIBLIOTHEQUE (12), CHANGELOG (10), QUICKSTART (3), GLOSSAIRE (2), `machine_projection.md` (1).
  - Skill : `SKILL.md` appelle `SAVOIR/READ`, `SAVOIR/ROUTING`, `SAVOIR/STATE`, `SAVOIR/CRAFT/CFT-00`, `SAVOIR/TOOLS/CONVERGENCE` et `MOYENS`.
- **Cite.** ACTION (GATE-A, GATE-B/B3, GATE-C, STATUS, POLICIES, PIPELINE-DIRECTION, STRUCTURED-PROOF, ANTI-SLOP, RUN-SYSTEM, OVERRIDE, HANDOFF), DIRECTION (START, CHARGE, CREATIVE-BOOT, VISUAL_TARGET, DOMAIN-FRAME, DOUBLE-LOOP), BIBLIOTHEQUE (SELECT, CONTRACTS, COMPONENTS), `schemas/research_brief.schema.json`, `scripts/validate_contracts.py`, `scripts/check_render.py`.
- **Contrôles qui verrouillent le texte.**
  - `validate_structure.py` : registre de concepts protégés dans SAVOIR (HON-02, ANT-01, MOY-01, TIT-01, TXI-01, RCV-01, FIN-01), 14 phrases verrouillées, motif retiré « Chemin minimal. Décide d'abord » (`:250`) et « Le parcours est : `DIRECTION/START → SAVOIR/FRAME` » (`:276`).
  - `validate_reading_map.py` : 9 phrases ; LCF-33 (ligne « Toute ressource de stack »), LCF-46 (marqueurs de vague seulement dans les lignes `[VEILLE 20…]` de SAVOIR), LCF-48 (carte des moyens), LCF-49 (`# SAVOIR/DESIGN-ATLAS` jusqu'à `# SAVOIR/STYLE`, qui exige « Traitement des assets moyens »), LCF-50 (« Vague 3 : »).
  - `validate_all.py` : 4 phrases ; findabilité de « Cohérence de rayon » vers `SAVOIR/STATE` (`:131`) ; mutation de la skill (`:76`).
  - `validate_design_governance.py` : 2 phrases. `test_audit_regressions.py` : 2 phrases, plus les localisateurs `TOOLS/CONVERGENCE` et `TOOLS/MOYENS` (`:194-204`). `test_read_route.py` ouvre SAVOIR (`CFT-05`). `build_core.py` ouvre SAVOIR et compare la copie de la skill.
- **Ce qui casserait.**
  - Renommer un titre `SAVOIR/…` : `read_route.py` (regex `HEADING_LOCATOR`, `:41`), les 65 renvois de READING_MAP, la skill.
  - Changer le niveau des titres `# SAVOIR/DESIGN-ATLAS` ou `# SAVOIR/STYLE` : LCF-49.
  - Déplacer MOY-ASSETS hors de DESIGN-ATLAS : LCF-49.
  - Faire commencer d'autres lignes que `[VEILLE 20…` pour les marqueurs de vague : LCF-46.
  - Modifier un bloc `noyau` sans relancer `build_core.py` : écart détecté par `validate_structure.py`.
- **Règle de prudence.** Aucune de ces contraintes n'interdit le rangement (phase 2), mais elle exige que les contrôles soient adaptés dans le même lot. À traiter avec la phase 5 pour ce qui touche au chargement.

## Synthèse

- C'est le cœur du savoir : le fond est dense et de qualité (grammaire de composition, pluralité, 12 gestes, couleur et type sans valeurs imposées). Rien à retirer sur le fond ; tout est à protéger.
- La forme dessert le designer : 8 000 caractères de routage et de codes avant la première ligne de design, 13 titres de niveau 1 inégaux, des chapitres codés (`SAVOIR/FRAME`, `CFT-04a`), et un tiers environ de contenu de gouvernance mêlé au savoir (preuves, champs, délégation, claims).
- Les répétitions internes viennent surtout du mécanisme du noyau (pointeur + texte complet, 18 fenêtres) et de trois idées redites 5 à 7 fois (test « quelle décision a changé », premium, « une capture ne prouve pas »).
- Risque de convergence modéré : valeurs CSS dans le noyau (liseré 1 px, formule de rayon), catalogue fermé de 8 profils en tension avec la veille, listes d'outils nommés, recettes de composition non datées.
- Déplacer exige d'adapter les contrôles de `validate_structure.py`, `validate_reading_map.py` (LCF-46/48/49/50) et `read_route.py`, ainsi que la copie générée dans la skill.
