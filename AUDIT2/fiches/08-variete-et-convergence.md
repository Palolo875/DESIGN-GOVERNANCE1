# Fiche 08 — Variété et convergence

Audit en lecture seule. Question : où le système pousse-t-il à la variété et à la spécificité (principe 3 de la charte), et où pousse-t-il à des résultats qui se ressemblent d'une demande à l'autre ?

## 0. Matériau, conventions et limites

**Pages lues (valeurs CSS et structure HTML, pas de comparaison de pixels).** Les chemins `U5/…` et `U3/…` sont relatifs à `…/scratchpad/wt-refonte/`.

| Brief | Avec le système | Sans le système (témoin) |
|---|---|---|
| B2, landing page d'un SaaS de facturation | N1, N2, N4 (U5) ; R2 « V », R4 « X » (U3) | R1, R3 (U3) |
| B3, site d'une école de natation pour enfants | N3, N5 (U5) ; R6 « K » (U3) | R5 (U3) |

R7 (retouche de contraste, 1 968 octets) est exclue : ce n'est pas une page conçue.

**Version du système.** U3 a tourné sur `01be58d`. U5 a tourné sur `9f921c1`, qui contient les paris P1 (marquage proportionné) et P3 (premier regard), retirés ensuite par `e0e830c`. Les citations `fichier:ligne` du système visent le dépôt actuel (`9681d4e`).
- `SKILL.md`, `DIRECTION.md`, `ACTION.md`, `examples.md` et les passages de `BIBLIOTHEQUE.md` cités ici portent les mêmes numéros de ligne à la base des runs.
- Pour `SAVOIR.md`, la ligne de la base des runs est plus basse. Correspondance actuel → base : 275→273 ; 310→308 ; 402→394 ; 422→412 ; 425→415 ; 437→427 ; 514→504 ; 662→648 ; 677→663 ; 744→730 ; 923→909 ; 928→914 ; 971→955.
- Les passages ajoutés après les runs sont signalés « postérieur aux runs ». Aucune page ne peut en avoir subi l'effet : `BIBLIOTHEQUE.md:553`, `:555`, `:567`, `SAVOIR.md:407`, `:931`.

**Limites de cette fiche.**
- Un seul run par condition et par demande. Les comptes décrivent, ils ne prouvent pas.
- Je n'ai pas regardé les rendus. Les traits visuels sont lus dans le CSS et le HTML.
- Ce que les agents disent avoir choisi vient de leurs traces (`U5/journaux/N4-trace.md`, `N5-TRACE.md`, commentaires de tête des pages, `U*/reponses/`). Je ne l'ai pas revérifié.
- Les journaux `U3/journaux/R*.md` et `U5/journaux/N1-N3.md` sont des listes d'appels, pas des raisonnements. Pour R1, R3 et R5 (sans système), il n'y a pas de trace de raisonnement, seulement la réponse finale.
- `U3/releves.md` ne donne pas le nombre de mentions « exemple » visibles de R6.
- Je n'ai aucune mesure d'un modèle livré à lui-même au-delà des trois pages « sans ».

**Précision sur un relevé existant.** `U5/releves.md` (note de convergence) décrit N1, N2 et N4 comme « crème, vert sombre, titre à empattements ». Le CSS nuance : le fond est vert-gris, pas crème (N1 `#EDF1EA`, teinte 94° ; N2 `#f2f4f2` ; N4 `#F5F6F1`), et le titre de N1 est une grotesque (`U5/pages/N1-B2-paris.html:47`, Schibsted Grotesk), pas une slab.

---

## 1. Ce que les pages ont en commun

Légende de la colonne « Origine » :
- **S** : le trait est dicté ou fortement suggéré par une phrase du système (voir sections 3 et 4).
- **P** : le trait apparaît aussi dans les pages sans système, donc probablement un réflexe du modèle.
- **?** : à vérifier.

### 1.1 Entre les pages du brief B2 (facturation), avec système : N1, N2, N4, R2, R4

| Trait | Pages | Preuve | Origine |
|---|---|---|---|
| Titre en slab « Zilla Slab » | N2, N4, R2, R4 (4/5 ; 6 paires sur 10) | `N2:38`, `N4:34`, `R2:41`, `R4:34` : `--display`/`--serif:"Zilla Slab","Rockwell",…`. N1 fait exception (`N1:47`, Schibsted Grotesk 800). « Zilla » est absent des sources du système. | S probable (voir 4.2) |
| Le mot « mécane » dans la justification | N2, N4, R2, R4 | « titre en mécane (Zilla Slab…) » : `N2:3` et suivantes (commentaire de tête), `R4:3` et suivantes, `R2` (commentaire de tête), `U5/journaux/N4-trace.md:38,45`. Le mot n'existe dans le système qu'à `SKILL.md:161` et `SAVOIR.md:402`. | S |
| Fond blanc teinté de vert-gris | 5/5 | `--paper`/`--bg` : N1 `#EDF1EA`, N2 `#f2f4f2`, N4 `#F5F6F1`, R2 `#F4F7F2`, R4 `#F3F4F1`. Teinte 72–120°, clarté 93–96 %. ΔE76 entre les 10 paires : 0,6 à 3,0. Les deux pages sans système ont un fond crème (R1 `#f6f3ec` teinte 42° ; R3 `#F5F2EA` teinte 44°). | S probable (4.3) |
| Encre très sombre à reflet vert | N1, N2, N4, R2 (4/5) | `#122019`, `#14211d`, `#14211B`, `#13211A` : ΔE76 de 0,5 à 2,4 entre elles. R4 `#15191E` s'en écarte (teinte 213°, ΔE 8,6 à 10,7). | S probable (4.3) |
| Rouge de retard, vert « payé », ocre d'attente quasi identiques | 5/5 pour le rouge, 4/5 pour l'ocre | Rouge : `#AE3418`, `#b0261d`, `#B42318`, `#A8321A`, `#B42318` (teinte 4–11°). Vert : `#1D6646`, `#17703f`, `#1D6B45`, `#0D6A46` (teinte 147–157°). Ocre : `#7E5300`, `#965200`, `#7A5200`, `#8A5600` (teinte 33–40°). | S/P ? |
| « La couleur sert seulement aux statuts ; l'action est à l'encre » | N1, N2, R2, R4, et N4 en partie | `N1:33` « statuts — la couleur ne sert qu'à eux » ; `N2:31` « statuts : seule couleur de la page » ; `U3/reponses/R4.md:21` ; `U3/reponses/R2.md:11`. N4 : action en vert `#0F5B3C` (`U5/journaux/N4-trace.md:39`), seule exception. | S (4.4) |
| Objet d'ouverture = suivi du cycle de vie d'une facture | 5/5 | N1 fiche de suivi (`N1:373`), N2 registre d'octobre, N4 échéancier (`N4:302`), R2 « Encours » et trajet, R4 curseur J0→J+40 (`R4:363`). Les témoins R1 et R3 ouvrent sur une facture-document avec tampon. | S (3.1) puis (4.5) |
| Même thèse mot pour mot | N1 et R2 | `N1:362` « Une facture n'est finie que lorsqu'elle est encaissée. » ; `R2:318` « … lorsqu'elle est payée. ». Deux runs indépendants, deux jours d'écart. Absent des sources. | ? |
| Formules de promesse sur « suivie jusqu'au paiement » | 5/5 | Titres de page : N1 « suivie jusqu'à l'encaissement », R2 « suivie jusqu'au paiement », R4 « suivie jusqu'au virement » ; h1 N2 `:317` « de l'envoi au virement », N4 `:289` « relance jusqu'au paiement ». | ? |
| Noms du produit dans un même champ lexical | 5/5 | Échéance, Encaisse, Souche, Quittance, Quitus. « Échéance » est aussi le nom du témoin sans système R3 (`R3:6`, `N1:14`). Quittance et Quitus partagent leur racine. | P ? |
| Pas de plinthe de logos, pas de témoignages, pas de trois cartes de bénéfices | 5/5 | Traces : `U5/journaux/N4-trace.md:15` ; `N1` (commentaire de tête, ligne « Parti ») ; `R4` (commentaire de tête). | S (3.1) |
| Fin de page : tarifs puis conversion, parfois FAQ | 5/5 | N1 `tarifs`→`compte` ; N2 `tarifs`→`essai` ; N4 `tarif` avec formulaire ; R2 `tarifs`→`questions`→`essai` ; R4 `tarifs`→`questions`→bandeau final. | S (4.6) |
| Section « réforme » dédiée | N1, N2, R2 (3/5) | `N1 #calendrier`, `N2 #reforme`, `R2 #reforme`. | P (même 8 octobre 2026) |
| Tarif à deux ou trois formules, mêmes montants | N1 et R2 : 12 € puis 39 € ; N2 et R4 : 9 € puis 29 € ; N4 : un seul tarif à 19 € | `N1:509` « 12 € HT / mois » ; `R2:476` « Solo 12 € » ; témoins `R1:504` « 12 € » et `R3` « 29 € ». « jusqu'à 5 utilisateurs » : N1, N2, R2, R4. | P |
| Numéro de facture `F-2026-0142` | N1, N4, R4 (et R1, R3 sans système) | `N4:302`, `R4:363`, `R1:340`, `R3:428`. Absent des sources. | P |
| Essai gratuit de 30 jours | 5/5 (R1 sans système : 30 j ; R3 : 14 j) | Voir le tarif de chaque page. | P |

### 1.2 Entre les pages du brief B3 (natation), avec système : N3, N5, R6

| Trait | Pages | Preuve | Origine |
|---|---|---|---|
| Titre en Barlow Condensed | 3/3 ; Barlow en texte pour N5 et R6 | `N3:39`, `N5:48`, `R6:40` (`--display:"Barlow Condensed","Arial Narrow",…`). Absent des sources. Le témoin R5 prend Fredoka et Nunito (`R5:33`). | S probable (4.2) |
| Fond « carrelage » : même nom de variable, même teinte | 3/3 | `--tile:#F2F6F6` (`N3:22`), `#f1f6f5` (`N5:19`), `#F2F7F7` (`R6:22`). Teinte 168–180°, clarté 95–96 %. ΔE76 de 0,4 à 0,6. Le témoin R5 est `--sand:#FFF9F0`, ΔE 5,8 à 6,1. | S probable (4.3) |
| Encre bleu nuit | 3/3 | `#0D2B3A` (`N3:26`), `#0d2a3a` (`N5:24`), `#0C2B45` (`R6:26`). N3 et N5 : ΔE 1,0. | ? |
| Jaune ≈ teinte 45° et rouge ≈ teinte 5° en couleurs d'appoint | 3/3 | Jaune `#F3C232`, `#f5c22e`, `#F5C33B` ; rouge `#BF2E26`, `#d23b26`, `#D8402F`. | ? |
| Même concept : groupes par profondeur, coupe ou profil du bassin, questionnaire de placement | 3/3 | `N3:317-318` « Chaque enfant a sa profondeur… groupes… rangés par profondeur » ; `N5:332` ; `R6:318` « Chaque enfant nage à sa profondeur. » Le témoin R5 range par âge (« Un groupe pour chaque âge ») avec un dessin d'enfant. | S (3.1) puis (4.5) |
| Même titre ou presque | N3 et R6 ; N5 et R6 | « Chaque enfant a sa profondeur. » / « Chaque enfant nage à sa profondeur. » ; N5 « Du petit bain au grand bain… » et R6 `h2` « Du petit bain au grand bain, un bonnet par profondeur. » | ? |
| Même justification de la police | N3 et R6 | Les deux traces écrivent « voix signalétique de piscine (Barlow Condensed… » ; N5 : « signalétique ». Cela reprend « vernaculaire du lieu » de `SKILL.md:161`. | S |
| Enchaînement en cinq temps | 3/3 | Objet de placement en hero → le bassin ou les groupes → séance de 45 minutes → tarifs ou inscription → pratique ou questions : N3 `groupes/horaires/seance/tarifs/essai` ; N5 `paliers/seance/tarifs/pratique` ; R6 `bassin/seance/inscription/questions`. | S/P (4.6) |
| Valeurs de contenu | N3, N5, R6 (+ R5 pour 45 min et 6 max) | « 45 minutes » (`N3:427`, `N5:381`, `R6` en-tête) ; « six enfants au plus » (`N3:318`) ; « 4 à 12 ans » ; « séance d'essai ». | P |
| Message d'erreur téléphone identique | N3 et R6 (N5 presque) | `N3:534` et `R6:464` : « Ce numéro semble incomplet : 10 chiffres, par exemple 06 12 34 56 78. » ; `N5:488` : « …il faut 10 chiffres, commençant par 0. » Absent des sources. | ? |
| État « Complet » / liste d'attente | 3/3 | `N5:617`, `R6:502`, `N3` (en-tête). | S (ACTION.md:114) |

### 1.3 Entre les deux briefs : toutes les pages avec système (8)

| Trait | Pages | Preuve | Origine |
|---|---|---|---|
| Blanc teinté (et non blanc pur, ni crème) + encre très sombre teintée | 8/8 | Fonds de 1.1 et 1.2. Encres à clarté 10–16 %. | S probable |
| `text-wrap:balance` sur les titres | 8/8 (témoins : R3 seul) | Chaque page en contient 2 à 5. Recommandé par `SKILL.md:131` et `SAVOIR.md:437`. | S |
| `font-variant-numeric:tabular-nums` | 8/8 (témoins : R3, R5) | `SKILL.md:146`, `SAVOIR.md:514`. | S |
| Pas de thème sombre | 8/8 (témoins : R1 et R3 en ont un) | 0 occurrence de `prefers-color-scheme`. R2 dit « Thème sombre non fait » (`R2:9`). | ? |
| Rayon concentrique (`rayon intérieur = extérieur − inset`) | au moins N1 | `N1:52` : `--r-inner:8px; /* 14 − 6 d'inset */` ; formule de `SKILL.md:141`. Non cherché sur les autres pages. | S |
| Rayon 14 px | N1, N3, N5, R4, R6 (5/8) (aussi R1 et R3) | `--r-sheet`/`--radius`/`--r:14px`. | P |
| Corps 17 px (R6 : 18 px ; R4 : 1 rem) | 6/8 (aussi R1, R3, R5) | `font-size:17px`. | P |
| `h1` : `clamp(…, 6.4vw, …)` | N2, N3, N4, N5 (4/8) (aussi R5) | `N2:70`, `N3:83`, `N4:65`, `N5:90`, `R5:83`. | P |
| Objet de preuve codé et manipulable, au premier écran | 8/8 | Voir 1.1 et 1.2. | S (3.1) |
| Page courte : 4 à 6 blocs (contre 7 à 8 sections sur les témoins) | 8/8 | Comptage des `<section>` ; `U3/pages/R1`, `R3`, `R5` ont 7 ou 8 sections. | ? |
| Beaucoup de mentions « exemple » visibles | 7 pages relevées | `U5/releves.md` : N1 11, N2 12, N3 13, N4 9, N5 13 ; V 15, X 16 (U3). R6 non relevé. Formules répétées : « nom d'exemple » (`N5:314`, `R4:330`), « Tarifs d'exemple, à remplacer/confirmer », « données fictives » (N1, N2, R4). | S (4.7) |
| Trace légère en commentaire de tête, mêmes rubriques (mode, thèse, modal/trame/parti, plafond, défaut restant, prochaine preuve) | 7/8 avec rubriques ; N5 renvoie à un fichier | `N1:3`, `N2:3`, `N3:3`, `R2:3`, `R4:3`, `R6:3` ; N4 en résumé abrégé (`N4:12`) ; N5 renvoie à `TRACE.md` (`N5:9`). Format de `SKILL.md:215`. | S |

---

## 2. Ce qui les distingue

**Entre les pages B2 avec système.**
- **Objet d'ouverture.** Cinq objets de la même famille, de nature différente :
  - fiche à quatre scénarios, avec l'opposition « rejetée ou refusée » (N1) ;
  - registre mensuel avec totaux (N2) ;
  - échéancier gradué au jour, avec choix du délai 30/45/60 j (N4) ;
  - encours manipulable avec bouton « Relancer » (R2) ;
  - curseur de J0 à J+40 (R4).
- **Sections propres.** `#rejet-refus` (N1), « Avant l'envoi, Souche relit la facture » (N4, `#mentions`), « Quand l'échéance passe, la relance part » (N2), « La loi change le tuyau » (R2).
- **Modèle de prix.** Un tarif unique illimité à 19 € (N4), deux formules (N1, R2, R4), trois formules avec « sur devis » (N2).
- **Voix de texte.** Cinq familles pour cinq pages : Hanken Grotesk (N1), IBM Plex Sans (N2 et R2), Instrument Sans (N4), Public Sans (R4). Dans N1, le titre est une grotesque à 800 de graisse et −0,035 em (`N1:110`), seule page sans slab.
- **Couleur d'action et d'attente.** Action en vert dans N4 (`#0F5B3C`), à l'encre dans les quatre autres. L'attente est en bleu franc dans N2 (`--wait:#2457a0`), en bleu sombre dans N1 (`--st-flow:#2C5878`), en gris-bleu désaturé dans R4 (`--wait:#4F6288`), seule page à l'encre bleu-gris (`#15191E`).
- **Ton du titre.** Phrases-thèses (N1, R2, N2) ou deux phrases en parallèle (N4, R4).

**Entre les pages B3 avec système.**
- **Modèle de groupe.** Cinq groupes de 0,80 m à 2,20 m (N3), cinq paliers avec tarif par palier (N5), quatre groupes à bonnets jaune, vert, orange, rouge (R6).
- **Signes propres.**
  - N3 : chiffres de profondeur en rouge sur le panneau.
  - N5 : « ligne d'eau » à flotteurs rouges et blancs, sélection par une « frite » jaune.
  - R6 : bonnets de quatre couleurs, température 30 °C.
- **Police de texte.** Figtree (N3), Barlow (N5, R6).
- **Dispositif de placement.** Cinq phrases d'aisance plus un âge (N3), un âge plus des radios (N5), un stepper plus trois questions oui/non (R6).
- **Noms.** Les Petites Longueurs, Ligne d'eau, Clapotis ; lieux Paris 11e / Lyon 7e.

**Entre avec et sans système (brief B2).**
- Les deux témoins R1 et R3 convergent entre eux sur tout le concept : même titre à une variante près (« Facturez en deux minutes. Soyez payé sans relancer / courir après. »), même facture tamponnée « PAYÉE », même fond crème et titre à empattements, même numéro de facture, mêmes 12 € et 29 € (`U3/releves.md`, note « Diversité B2 »).
- Les cinq pages avec système écartent ce concept (aucune facture tamponnée) mais convergent entre elles autour d'un autre (section 1.1).
- Sur le brief B3, le témoin R5 (enfant dessiné, Fredoka, sable et corail) n'a aucun des traits de 1.2.

**Entre les deux briefs.** Les marqueurs d'identité diffèrent nettement :
- slab contre condensée ;
- vert-gris contre bleu-vert ;
- tracker temporel contre coupe de bassin ;
- tarifs en jours contre séance de 45 minutes.

Ce qui se retrouve d'un brief à l'autre, ce sont l'échafaudage (1.3) et les gestes de finition, pas les signes d'identité.

---

## 3. Passages du système qui favorisent la variété

Chaque ligne indique l'effet observé dans les pages, quand il y en a un.

### 3.1 Mécanismes qui ont écarté le concept modal (effet constaté)

| Passage | Ce qu'il fait | Effet constaté |
|---|---|---|
| `V1/official/DIRECTION.md:204-205` (MODAL / PARTI du Creative Boot) | Oblige à nommer ce que « n'importe quelle IA produirait » puis à garder ou s'écarter en justifiant. | Les 8 pages avec système ont une ligne « Modal / trame / parti » dans leur trace, et aucune ne reprend la facture tamponnée, la photo d'enfant souriant ni les trois cartes. `U5/reponses/N4.md:9` : « Effet décisif. Le repère de convergence … signale la « facture tamponnée » … Je l'ai écarté. » |
| `skills/design-governance-practice/SKILL.md:49` (situation, tension, geste, objet de preuve, position/exclusion, contre-choix situé ; chaîne promesse → objet de preuve → geste ; « L'objet passe avant les listes de bénéfices ») | Remplace la liste de bénéfices par un objet de preuve codé. | 8/8 pages ouvrent sur un objet codé et manipulable. Deux concepts différents sur les deux runs B2 de U3 (`U3/resultats.md`, « Convergence »). |
| `SKILL.md:73` et `SKILL.md:95-103` (pas de « landing premium » ; table des signaux ; test de trame) ; `V1/official/BIBLIOTHEQUE.md:251-267` | Nomme les compositions à interroger et demande d'écrire la trame modale en une ligne avant de la rompre. | Aucun logo-plinthe, aucun témoignage, peu de grilles de trois cartes (grilles à trois colonnes : N2 1, N3 2, N5 3, R6 1 ; N1, N4, R2, R4 aucune). |
| `V1/official/SAVOIR.md:923` et `:928` (marqueurs de vague datés) ; `SKILL.md:163` | Fournit des exemples datés de ce qu'est le modal, « jamais pour interdire ». | Les agents s'en servent comme repère : `U5/journaux/N4-trace.md:14`, `N2:3` (commentaire de tête). Voir aussi 4.1 : effet de liste noire. |
| `SKILL.md:161` / `SAVOIR.md:402` (question de convergence ; comparer au moins deux voix sur le vrai titre) | Force une comparaison typographique sur le vrai texte. | Comparaison de deux à quatre voix déclarée dans les 8 pages (`U5/journaux/N4-trace.md:38`, `N5-TRACE.md:82`, `N1:3`, `N2:3`, `R4:3`, `R6:3`, `U5/reponses/N3.md:30`, `U3/reponses/R2.md:11`). |
| `V1/official/DIRECTION.md:516-518` (position et exclusion ; contre-choix situé) | Fait écrire ce qui est refusé et pourquoi, plus l'alternative meilleure sous une autre contrainte. | N4 : exclusion « facture tamponnée, faux dashboard » ; contre-choix « éditeur de facture en direct » (`U5/journaux/N4-trace.md:63`). N5 : exclusion « enfant-mascotte et photo d'ambiance » (`N5-TRACE.md:80`). |

### 3.2 Mécanismes de spécificité de fond et de contenu

| Passage | Effet constaté |
|---|---|
| `SKILL.md:121-123` et `SAVOIR.md:117-122` (test de singularité ; « Forme située = tâche + donnée ou objet métier + état et conséquence + densité de lecture… ») | Contenus propres au métier : statuts déposée/rejetée/refusée/encaissée et jours ouvrés (N1, N4), profondeurs à l'échelle, groupes, créneaux (N3, N5, R6). Les juges donnent « spécificité » à « avec » dans 20 jugements sur 20 (`U3/resultats.md`). |
| `SKILL.md:47` (contenu plausible marqué comme exemple plutôt que des emplacements vides) | Pages lisibles comme pages (prix, horaires, adresse), au prix du marquage répété (4.7). |
| `V1/official/ACTION.md:114` (états `loading`, `empty`, `error`, `unavailable`, succès partiel) | États dessinés dans les 8 pages : refus corrigeable, erreur de formulaire, « Complet ». Ce n'est pas un défaut : c'est de la qualité qui se retrouve partout. |
| `SKILL.md:192` et `SAVOIR.md:310` (« un axe situé à la fois ») ; `V1/official/SAVOIR.md:292-321` (axes de CFT-02) ; `V1/official/DIRECTION.md:746-757` | Prévoient des alternatives situées. Dans les runs, l'alternative n'est qu'une phrase écartée (N1 : « composeur de facture interactif » ; N2 : « page centrée sur la réforme » ; R2 : « page autour de la conformité »). Elle ne produit pas de variante rendue. |
| `V1/official/DIRECTION.md:807-821` (« Convergence de genre ≠ slop » ; « Les listes ne sont pas un canon ») ; `V1/official/SAVOIR.md:425`, `:662`, `:677` (« Aucun profil n'est choisi par défaut » ; catalogue « borné et non exhaustif ») | Garde-fous contre l'application mécanique d'une liste. Effet non constaté : seuls N4 et N5 ont ouvert `SAVOIR/STYLE`, et ils ont choisi des profils différents (QUIET_SYSTEM + EDITORIAL_PRECISION ; PICTORIAL_UTILITY). |
| `V1/official/DIRECTION.md:411-426` (REUSE-CHALLENGE : relever teinte, paire typographique, ossature, objet de preuve des runs précédents) | Mécanisme prévu pour la variété d'une demande à l'autre. **Sans effet dans ces mesures** : chaque run est dans un contexte neuf, donc `LIMIT` (`R2:9`, `U5/journaux/N4-trace.md:56`, `N5-TRACE.md:67`). |

---

## 4. Passages qui favorisent la convergence

### 4.1 La liste datée des marqueurs de vague sert de liste noire (et la mesure B2 s'y appuie)

- **Passage.** `V1/official/SAVOIR.md:928` énumère la vague 1 (violet, Inter, halos), la vague 2 (beige ou crème, brun, serif de caractère, orange rouille), la vague 3, des « Signaux à confirmer » (« grotesque large ou condensée (Archivo) sur fond blanc neutre avec un seul accent vif ») et « même objet central par brief (fournées du jour ; facture tamponnée) ». `SKILL.md:163` y renvoie. `DIRECTION.md:204` définit MODAL par ces marqueurs (« se nomme avec les marqueurs de vague datés »).
- **Lien avec les pages.**
  - Les traces B2 recopient la liste : `N2:3` « violet/Inter ou crème/serif ; facture tamponnée ; grotesque sur blanc + accent unique » ; `R4:3` « crème/serif ou blanc/grotesque/accent unique » ; `U5/journaux/N4-trace.md:14` ; `R2:3`.
  - Elles écartent exactement ces éléments et se retrouvent sur l'option voisine non listée : fond vert-gris au lieu de crème, slab au lieu de serif de caractère ou de grotesque, couleur réservée aux statuts au lieu d'un accent unique.
  - `U5/journaux/N4-trace.md:38` : « Zilla Slab … hors marqueurs de vague ».
  - `U5/journaux/N5-TRACE.md:82` constate que sa police correspond au signal listé (« grotesque condensée sur blanc + un accent ») et garde le choix en justifiant l'écart par « fond carrelage et palette codée multicolore, non par la police ».
- **Risque de biais de mesure.** L'entrée « facture tamponnée » (`SAVOIR.md:928`, datée du 30-09-2026) décrit « un brief » sans le nommer. Si c'est le brief B2, l'évitement observé sur B2 est favorisé par un repère que B3 n'a pas. Je n'ai pas cette information : à vérifier.
- **Postérieur aux runs.** `SAVOIR.md:931` (« Signaux de page ») a été construit à partir de « formules relevées dans les runs internes de mesure ». Elle ajoute une famille à la liste noire (slogan en deux temps, pastille en capitales, etc.). Les deux phrases en parallèle se retrouvent dans N4 (`N4:289`), R4 (`R4:345`) et dans les témoins R1 et R3.

### 4.2 Une liste d'exemples de voix typographiques où chaque domaine trouve « sa » police

- **Passage.** `SKILL.md:161` / `SAVOIR.md:402` : « compare au moins deux voix typographiques distinctes (par exemple grotesque, serif, mécane, manuscrite ou vernaculaire du lieu) ». Le mot « mécane » n'apparaît nulle part ailleurs dans le système.
- **Lien avec les pages.** Le brief de facturation prend « mécane » (4/5 pages avec Zilla Slab, le mot repris dans 4 traces) ; le brief natation prend « vernaculaire du lieu », rendu par « voix signalétique de piscine » (N3 et R6 à l'identique, N5 « signalétique »), en Barlow Condensed dans 3 pages sur 3.
- **Les alternatives comparées reviennent d'un run à l'autre.**
  - N4 : Schibsted Grotesk, Zilla Slab, Newsreader, Instrument Sans.
  - N5 : Barlow Condensed, Fraunces, Baloo 2, Rubik.
  - R6 : Barlow Condensed comparée à Fredoka, Barlow, Bricolage.
  - N1 : Schibsted Grotesk comparée à Newsreader et Spectral. N2 : Zilla Slab comparée à Hanken Grotesk.
  - Dans N4 et N5, l'agent étiquette lui-même les candidats serif et arrondi comme « vague 2 » ou « modal » (`N4-trace.md:38`, `N5-TRACE.md:82`). Cela laisse gagner la voix du domaine.
- **Mitigation du texte.** `SKILL.md:161` précise : « La question ne prescrit aucun écart : un choix convergent justifié reste valide. » Les agents justifient par le domaine (« voix de registre/formulaire », « signalétique »). Ce motif vaut pour toute autre demande du même domaine : il ne distingue pas la demande.

### 4.3 Fond « blanc chaud, froid ou neutre » et palette par rôles

- **Passage.** `SKILL.md:159` / `SAVOIR.md:398` (palette par rôles : surfaces, textes, actions, états, frontières ; « une structure neutre à accent … recevable ») ; `SKILL.md:147` (ligne « Accent » : distinguer action et statut ; « ne pas réduire à un accent unique par réflexe ») ; `SKILL.md:161` cite « neutres et un seul accent » comme palette modale.
- **Lien avec les pages.** Les 8 pages ont des noms de variables comparables (`--paper`/`--tile`, `--ink`, `--ink-2`, `--rule`, statuts en paires `…-bg`), un fond teinté en deux familles (vert-gris, bleu-vert) et une encre quasi noire teintée. La règle « une couleur sémantique n'est pas une décoration » conduit 4 pages sur 5 du brief B2 à « couleur = statuts, action à l'encre » (1.1).
- **Postérieur aux runs.** `SAVOIR.md:407` (« Le fond aussi est une décision : un blanc chaud, froid ou neutre donne le ton avant le reste ; nomme sa température et sa raison. Deux ou trois couleurs tenues valent souvent mieux qu'une palette complète ») : à surveiller. Cette phrase a la forme de ce qui a déjà produit les fonds teintés. Effet non mesuré.

### 4.4 Gestes de finition identiques d'une page à l'autre

- **Passages.** `SKILL.md:131` / `SAVOIR.md:437` (`text-wrap: balance`) ; `SKILL.md:146` / `SAVOIR.md:514` (`tabular-nums`) ; `SKILL.md:141` (formule du rayon intérieur). Ils sont donnés avec leur valeur CSS.
- **Lien.** 8/8 pages portent `text-wrap:balance` et `tabular-nums` ; N1 écrit la formule du rayon en commentaire.
- **Portée.** C'est du métier, pas de l'identité. Mais cela contribue au « grain » commun : titres à interligne 0,92–1,06 et approche serrée (`N3:83`, `N5:90`, `R6`, `N4:65`).

### 4.5 « Forme située » et « objet du métier » : l'objet le plus évident du domaine

- **Passages.**
  - `SKILL.md:49` (« promesse → objet de preuve → geste ; … de préférence codé ») ;
  - `SKILL.md:123` (« objet métier ») ;
  - `V1/official/BIBLIOTHEQUE.md:170` (la ligne « Continuité, révélation ou rupture de rythme » renvoie à `SCENE/PRODUCT_NARRATIVE` ou `GRID/AXIAL`) ;
  - postérieur aux runs : `BIBLIOTHEQUE.md:567` (« Objet du métier … formulaire, ticket, carnet, relevé, cadran, règle graduée »).
- **Lien.**
  - Sur un brief vague, la « situation » disponible est celle du domaine. B2 donne cinq variantes du suivi d'une facture. B3 donne trois fois « profondeur → groupe → questionnaire ». Les réponses sont différentes entre B2 et B3, mais proches d'un run à l'autre sur le même brief.
  - Quatre pages B2 sur cinq ont un axe de temps (trajet, échéancier, curseur, calendrier). C'est compatible avec la ligne `BIBLIOTHEQUE.md:170` (à vérifier : N4 cite `GRID/AXIAL` ; N1 a ouvert `SCENE/PRODUCT_NARRATIVE` selon `U5/releves.md`).
  - La ligne `BIBLIOTHEQUE.md:567` n'existait pas lors des runs ; les noms « Relevé », « Souche », « Quittance » viennent donc d'ailleurs. Elle peut renforcer l'effet.

### 4.6 La trame du bas de page est tolérée par le système

- **Passages.**
  - `SKILL.md:103` / `BIBLIOTHEQUE.md:267` : le test de trame donne comme trame modale d'un SaaS « promesse, logos, trois bénéfices, tarifs, FAQ ». On retire logos et bénéfices ; tarifs et FAQ restent.
  - `V1/official/DIRECTION.md:809-811` : « Une structure conventionnelle peut être la bonne réponse. »
- **Lien.**
  - Les agents le disent eux-mêmes : « trame tarifs+questions conservée (nécessaire à la décision d'achat) » (`R2:3`) ; « tarifs en deux cartes et FAQ (trame gardée, faible enjeu) » (`R4:3`) ; « bloc tarif + formulaire … reste générique » (`U5/journaux/N4-trace.md:47`) ; « sections tarifs et infos pratiques (cartes) — convention de genre gardée volontairement » (`N5-TRACE.md:135`) ; « rangée de tarifs en 3 colonnes » encore générique (`R6:3`).
  - Les juges le voient aussi : `U5/jugement/resultats/sonnet-J01.json` (« finit sur une FAQ et un tableau de tarifs plus interchangeables »), `sonnet-J17.json` (« tableau, tarifs et formulaire est plus interchangeable »).
- **Postérieur aux runs.** `BIBLIOTHEQUE.md:553` (« Trame sur toute la page ») et `:555` (« Cartes ») visent exactement ce défaut. Effet non mesuré.

### 4.7 Marquage « exemple » : un texte et des exemples qui fixent la formule

- **Passages.** `SKILL.md:47` : « Le marquage est discret dans l'interface (« exemple », « à confirmer ») ». `skills/design-governance-practice/references/examples.md:38` (« le bouton « Appeler l'atelier » fonctionne avec un numéro d'exemple ») et `:46` (« tarifs, horaires et numéro marqués « exemple » »).
- **Lien.** Entre 9 et 16 mentions visibles par page (`U5/releves.md`), avec des formules qui se répètent d'une page à l'autre : « (nom d'exemple) », « Tarifs d'exemple, à remplacer », « données fictives ». Les juges récompensent le marquage ; le propriétaire le trouve encombrant (`U5/resultats.md`, « Limites » ; `U3/resultats.md`, « Lecture » 2). Le pari P1 (marquage proportionné) a été retiré avec P3, mais N1–N5 portaient encore 9 à 13 mentions.

### 4.8 Ce que le système ne contrôle pas : valeurs par défaut du modèle

- **Observé aussi sans système.** `F-2026-0142` (R1, R3), 12 € puis 29 €, « 30 jours d'essai », corps 17 px, `h1` à 6,4 vw (R5), « 45 min » et « 6 enfants max » (R5), rayon 14 px.
- **Passage proche.** `SKILL.md:51` (« données d'exemple cohérentes entre elles ») ne demande de dériver les valeurs de rien de propre à la demande.

---

## 5. Hypothèses sur les causes de la convergence

| N° | Hypothèse | Statut | Éléments |
|---|---|---|---|
| H1 | La liste de marqueurs de vague agit comme une liste noire : les agents l'évitent et se rabattent sur l'option voisine non listée. La convergence est déplacée (crème/serif → vert-gris/slab), pas supprimée. | **probable** | 4.1 ; `N2:3`, `R4:3`, `N4-trace.md:38`, `N5-TRACE.md:82`. Le décalage des teintes (42–44° sans, 72–120° avec) est mesuré. |
| H2 | L'exemple nommé « mécane » dans la question de convergence est le canal direct de la slab sur B2 ; « vernaculaire du lieu » est celui de la signalétique sur B3. | **probable** | 4.2 : mot repris dans 4 traces sur 5 ; absent du reste du système ; Zilla Slab et Barlow Condensed absents des sources. Il manque un run B2 sans ce mot pour trancher. |
| H3 | Sur un brief vague, la seule « situation » que l'agent peut lire est celle du domaine. La chaîne promesse → objet → geste conduit donc à l'objet le plus évident du domaine, d'où une variété entre briefs (B2 ≠ B3) mais pas entre runs d'un même brief. | **probable** | 4.5 ; 5/5 et 3/3. Pas de page à brief détaillé pour comparer : **à vérifier** avec un brief riche. |
| H4 | La règle « palette par rôles, couleur sémantique non décorative, retenue » fabrique un fond teinté quasi neutre, une encre quasi noire et une couleur réservée aux statuts. | **probable** | 4.3 ; 1.1 ; mesure des ΔE. Le lien causal exact n'est pas démontré : les sources ne citent aucune valeur. |
| H5 | Le défaut ne vient pas d'un manque d'activation : les runs « plafond » (N4, N5) convergent autant que les runs par défaut. | **probable** | N4 partage Zilla Slab et l'encre `#14211B` avec R2 (ΔE 0,9) ; N5 partage Barlow Condensed, le fond et le concept avec R6. `U5/resultats.md` diagnostique un problème d'activation pour la qualité, pas pour la variété. |
| H6 | Le bas de page revient à la trame modale parce que le test de trame est formulé sur le premier écran, que la trame d'exemple est nommée (« promesse, logos, trois bénéfices, tarifs, FAQ ») et que la convention de genre est explicitement tolérée. | **probable** | 4.6 ; autodiagnostics des agents ; jugements `sonnet-J01`, `sonnet-J17`. Le correctif `BIBLIOTHEQUE.md:553` existe mais n'est pas mesuré. |
| H7 | Le marquage « exemple » fige des formules de micro-copie parce que le texte et `examples.md` donnent les mots à employer. | **probable** pour la formule, **à vérifier** pour le coût de lecture | 4.7 ; 9 à 16 mentions. |
| H8 | Les contenus par défaut (numéro de facture, tarifs, durée de séance, effectifs, message d'erreur) viennent des habitudes du modèle ; le système ne les contrôle pas. | **probable** | 4.8 : mêmes valeurs dans R1, R3 sans système. Pour le message d'erreur téléphone, absent des témoins : **à vérifier** (comportement conditionné par `ACTION.md:114` ?). |
| H9 | Chaque run est dans un contexte neuf : REUSE-CHALLENGE (`DIRECTION.md:411-426`) conclut `LIMIT` à chaque fois. Le système n'a aucun moyen de rendre une demande différente d'une autre demande indépendante. | **probable** (pour cette mesure) | `R2:9`, `N4-trace.md:56`, `N5-TRACE.md:67`. Hors mesure, en usage réel dans un même projet : **à vérifier**. |
| H10 | L'exigence « au moins deux voix comparées » est remplie avec des candidats toujours semblables, donc la comparaison ne diversifie pas le résultat. | **à vérifier** | Candidats récurrents (4.2) ; seules sept comparaisons lues. |
| H11 | L'entrée « facture tamponnée » du repère de convergence a été relevée sur le brief de test lui-même ; la mesure B2 mesure alors l'adaptation du système à ses propres tests. | **à vérifier** | 4.1 ; `SAVOIR.md:928` ne nomme pas le brief. |
| H12 | Les 8 pages sans thème sombre, plus courtes (4 à 6 blocs contre 7 à 8) viennent de l'économie d'effort du chemin proportionné, pas d'une règle. | **à vérifier** | `R2:9` « Thème sombre non fait » ; un seul témoin de la raison. |
| H13 | Une liste qui s'allonge (`SAVOIR.md:931`, signaux de page) renforce l'effet de liste noire (H1) au lieu de le réduire. | **à vérifier** | Postérieur aux runs ; aucune mesure après son ajout. |

---

## 6. Pistes de correction pour la phase 5

Pistes seulement, sans exemple visuel ni valeur. Chacune se rattache à un défaut constaté ci-dessus, conformément à la charte (section 5 : pas de règle sans défaut constaté ; pas d'exemple qui fige).

1. **Nommer l'effet de relocalisation dans le repère de convergence** (H1, H13). Ajouter un énoncé daté qui constate que l'évitement d'un marqueur mène souvent à l'option voisine, et formuler la question de convergence sur le *chemin* de choix (« pourquoi ce choix, et que seriez-vous passé à choisir si le marqueur évité n'existait pas ? ») plutôt que sur l'écart à une liste. Éviter d'étendre la liste à chaque mesure.
2. **Retirer ou remplacer la liste d'exemples de voix par un critère de provenance** (H2, H10). Au lieu de nommer des familles (dont le mot « mécane »), demander de dire de *quelle source de légitimité* vient chaque voix comparée (le métier, le public, la scène, la matière, l'époque) et de comparer des voix de sources différentes. Le sens de `SKILL.md:161` est conservé ; le canal direct disparaît.
3. **Exiger un critère de justification propre à la demande** (H3, H9). Une justification qui vaut pour tout le domaine (« signalétique de piscine ») ne distingue pas la demande. Piste : faire écrire ce que le choix doit à *cette* demande (client, lieu, contraintes, hypothèse nommée) et non au domaine. Sur un brief vague, cela revient à demander d'abord une hypothèse de situation concrète, nommée comme telle dans la proposition, qui guide au moins une décision d'identité. Elle ne doit pas être tirée au hasard (charte, principe 3).
4. **Faire porter le test de trame sur la page entière dans le chemin par défaut** (H6). `BIBLIOTHEQUE/SEQUENCE` existe (postérieur aux runs) : vérifier qu'elle est chargée sur le chemin DIRECTION, retirer du texte du test la trame d'exemple nommée si elle sert de gabarit au bas de page, et reformuler « Une structure conventionnelle peut être la bonne réponse » (`DIRECTION.md:809`) pour que la convention de genre soit une décision justifiée par section, non un défaut par omission.
5. **Séparer « finition partagée » et « identité qui doit varier » dans la grille de résultat** (H4, 4.4). Les gestes dont la valeur CSS est donnée (équilibre de titre, chiffres tabulaires, rayon) sont communs par nature. La grille de résultat de la phase 5 devrait mesurer la convergence sur les seuls marqueurs d'identité : famille du titre, teinte du fond et de l'encre, objet d'ouverture, ordre des sections, formule du titre.
6. **Mesurer la variété comme une propriété du dispositif d'essai, pas seulement du système** (H5, H8, H11).
   - Plusieurs runs par brief et au moins trois briefs de nature différente, dont un brief riche et un brief absent de toute liste du système.
   - Une condition témoin « sans système » par brief.
   - Une distance par paire de runs sur les marqueurs de piste 5.
   - Ne pas conclure sur un brief dont la trame est nommée dans les sources (cas B2, H11).
7. **Rendre explicite que les valeurs d'exemple doivent venir de la demande** (H8). Relier `SKILL.md:51` (cohérence des données) à une exigence de provenance : montants, durées, effectifs et identifiants tirés de la situation hypothétique, et non du premier ordre de grandeur disponible. Une seule phrase au bon endroit, si la mesure confirme le défaut sur un brief où les témoins diffèrent.
8. **Réexaminer le texte de marquage** (H7). Dire le principe (une mention globale discrète et des mentions locales là où une valeur peut être prise pour vraie) sans fournir de formule type dans `SKILL.md:47` ni dans `examples.md:38,46`. Le résultat du pari P1 (retiré) est à relire avant de décider.
9. **Variété d'une demande à l'autre dans un même projet** (H9). REUSE-CHALLENGE ne peut fonctionner que si une trace des runs précédents est lisible. À examiner si le but est la variété entre demandes d'un même projet ; hors de portée pour des demandes indépendantes, où seul le contenu de la demande peut différencier.
10. **Surveiller les ajouts postérieurs aux runs** (4.3, 4.5, 4.7). `SAVOIR.md:407` (fond « blanc chaud, froid ou neutre »), `BIBLIOTHEQUE.md:567` (liste d'objets du métier) et `SAVOIR.md:931` ont la forme de listes ou de formules recopiables. Les inclure dans la mesure de la phase 5 avant de les déclarer sans effet.

---

## Annexe — données manquantes

- Aucune comparaison visuelle des rendus.
- Pas de nombre de mentions « exemple » pour R6.
- Pas de raisonnement pour R1, R3, R5 (sans système) au-delà de leurs réponses finales.
- Pas de run à brief riche, donc pas de mesure de la variété quand la demande contient déjà des spécificités.
- Pas de run B2 ou B3 avec une version du système sans le mot « mécane », ni sans l'entrée « facture tamponnée ».
- Pas de lecture de `SAVOIR/TOOLS/CONVERGENCE` par les runs par défaut vérifiée page par page : `U5/releves.md` ne la liste pas pour N1, alors que sa trace cite « marqueur de convergence 30-09-2026 » ; la voie de chargement n'est pas établie.
