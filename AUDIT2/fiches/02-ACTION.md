# Fiche — V1/official/ACTION.md

Lecture complète faite (1 078 lignes, en 6 morceaux). Les lignes citées sont celles de `V1/official/ACTION.md` sauf mention contraire. Les parts « produit / gouvernance » en caractères sont des estimations à la main, à confirmer par script.

## Identité

- **Rôle actuel.** Source normative des « preuves exécutables, gates, statuts de run, verdicts et clôture » (l. 7). Elle mêle, sous un seul titre « Pipeline de livraison & preuves » (l. 1), le plancher de qualité du produit (premier rendu, UI/UX, accessibilité, craft, preuve visuelle) et la machinerie formelle (RUN_CARD, états, verdicts, réserves, override, recette de maintenance).
- **Public réel.** Agent, et auditeur. Le README envoie aussi « Reviewer ou lead » ici (README.md:53). Aucune entrée pour le débutant, le designer ou l'équipe.
- **Public visé par la charte.** Agent (chemins courts) et équipe (module de gouvernance). Le contenu « produit » devrait aussi servir le designer.
- **Mesures** (mesures.md) : 116 983 caractères, 659 phrases (moyenne 18,0 ; p90 30 ; 4 % de plus de 40 mots). Titres : 1 / 20 / 61 / 1 (un titre de niveau 4, l. 833). 830 codes, soit 51 pour 1 000 mots. 29 « non vérifié ». 1 vestige signalé (faux positif : « ne porte plus » l. 212, voir D13). Plus grosses sections : `RUN_CARD` 18 178, `PIPELINE-DIRECTION` 12 213, `GATE-A` 11 935, `Responsabilité` 11 397, `GATE-B` 10 125.
- **Partage estimé produit / gouvernance (détail plus bas).** Environ 35 à 40 % produit ou design (≈ 42 000 caractères) ; environ 60 % gouvernance ou méta (≈ 72 000 caractères). Le plancher produit est éparpillé dans 9 sections, dont une (`GATE-A`) est étiquetée « gouvernance » par `chemins.json`.

## Verdicts de la grille

| Critère | Verdict | Preuve |
|---|---|---|
| F1 Rôle | à corriger | Trois rôles sous un titre : preuves/gouvernance (l. 7), qualité produit (l. 98-134, 911-933), méta (l. 1014-1055, 1076). La phrase de rôle (l. 3) annonce « trace de run, artefacts, preuves, gates, verdicts » et ne dit pas que le fichier porte le plancher de qualité du rendu. |
| F2 Public | à corriger | Aucune ligne de public. Le fichier est écrit pour l'agent (« charge », « arrête ») mais README.md:53 y envoie un lecteur humain. Seul le bloc SORTIE (l. 35-47) parle à une personne, et il contient lui-même des codes (D6). |
| F3 Structure | à corriger | Niveau 4 à la l. 833 (max autorisé : 3). Titres de section = codes (`ACTION/GATE-A — plancher objectivable`), sans modèle commun : certaines H2 sont des routes, d'autres des contrats, d'autres des méthodes. Deux sections dépassent 10 000 caractères et deux autres 11 000 (`RUN_CARD` 18 178 ; `Responsabilité` 11 397 mêle 5 sujets). `ACTION/ANTI-SLOP` (l. 936) est un pointeur. |
| F4 Une seule fois | à corriger | Voir D3 à D8 : cinq énoncés de « quand arrêter la lecture / chemin minimal » (l. 15, 60, 94-96, 183-185, 271-277) ; la qualité du premier rendu dite quatre fois (l. 9, 98-110, 187-189, 1071) ; 22 fenêtres communes avec DIRECTION (l. 75, 277 ↔ DIRECTION.md:108, 172) ; « aucun nombre fixe d'itérations » trois fois (l. 612, 895, 1047) ; `ANCHOR-GENERATED` redit (l. 561 ↔ DIRECTION.md:656 ↔ SAVOIR.md:545). |
| F5 Langue | à corriger | 830 codes (142 routes, 283 jetons composés, 387 mots en capitales, 18 sous-gates). Pas défini à la première apparition : `RUN_CARD`, `TRACE-LOCATOR`, `N/A-JUSTIFIED`, `NOT-VERIFIED`, `blast radius` (l. 1029), `P0`-`P3` (l. 75), `JTBD` (l. 226, 443). Collision de lettres A/B/C (gates) et V/U/A/T (axes), avertie à la l. 177. Bloquant pour le public « équipe » tant que README.md:53 l'y envoie ; acceptable pour l'agent. |
| F8 Longueur | à corriger | 116 983 caractères. Chemin LITE : `RUN-LITE` 890 + `FAST-PATH` 1 221 + `GATE-A` 12 016 + `B2` 1 271 + `B6` 475 ≈ 15 900 caractères pour une petite correction (chemins.json). Sections de référence non lisibles seules : `RUN_CARD` (table de 26 lignes l. 311-336). |
| F9 Limites | à corriger | 29 « non vérifié ». La règle « une vérification absente n'est jamais un PASS » est redite l. 231, 350, 364, 404, 485, 762, 774, 915, 1074. Les limites de la recette `check_render` sont dites à nouveau l. 725, 805, 810-812. |
| F10 Exemples | conforme (vigilance) | Aucune valeur de couleur, police, ni code type. Quelques gabarits risquent d'être recopiés : voir « Ce qui fige ». |
| F11 Vestiges | à corriger (mineur) | Bandeau « expérimentation maintenue » (l. 3), verrouillé par `validate_design_governance.py` (`check_experimental_position`). `STATUS` « alias d'archive » (l. 340). « Les anciennes références de section ne sont pas des routes quotidiennes » (l. 1031). `ACTION/ANTI-SLOP` réduit à un pointeur vers `SAVOIR/CRAFT/CFT-01` (l. 938). |

## Sections

Famille : design / produit / gouvernance / méta. Pour les sections mixtes, la répartition par sous-section est dans le tableau suivant.

| Section (ligne) | Ce qu'elle apporte | Famille | Public | Observation principale | Disposition proposée |
|---|---|---|---|---|---|
| Intro (l. 3) | Rôle du fichier + bandeau « expérimentation maintenue ». | méta | tous | Bandeau d'état verrouillé par un contrôle ; rôle incomplet (F1). | réécrire (forme) : rôle en deux phrases ; bandeau à déplacer vers la fiche de version, après décision sur le contrôle |
| Responsabilité (l. 5-96) | Rôle, cartes de lecture, sortie/trace, registres, autorité. | mixte, voir sous-sections | agent | Cinq sujets, 11 397 caractères. Contient 3 des 4 blocs `noyau`. | scinder (voir sous-sections) |
| FIRST-RENDER (l. 98-110) | Cible de qualité du premier rendu, par mode. | produit | agent, designer | Cœur de « beau et pro » (charte principe 3). Redit en l. 9, 187, 1071. | garder dans le chemin de design (module « qualité du rendu ») ; fusionner `Principe positif de qualité` (l. 187-189) |
| UI-UX-REALITY (l. 112-134) | Construire interface et tâche ensemble : états, responsive, accessibilité, robustesse. | produit | agent, designer | Utile et court. Le « contrat de production » en 9 champs majuscules (l. 118-128) est un gabarit, et mentionne `OBSERVED/NOT-VERIFIED` (gouvernance). | garder, produit ; réécrire (forme) : champs en langage clair, vocabulaire de preuve laissé au module |
| STATUS (l. 138-214) | États du run, issues, verdicts V/U/A/T, statut de direction. | gouvernance | équipe, audit | 6 596 caractères, 72 codes /1000 mots. Une exception produit : `Principe positif de qualité` (l. 187-189). V/U/A/T (l. 192-203) est le seul lien entre axes de jugement et gouvernance. | déplacer vers le module de gouvernance ; le contenu de V/U/A/T (quoi juger) a un équivalent produit à garder (voir sous-sections) |
| PRECONDITION (l. 218-267) | Contrat minimal par mode ; `DECISION-INTENT/CHANGE` ; traces post-build ; raccord `DESIGN-ATLAS`. | gouvernance | agent, équipe | Table des modes (l. 222-228) redit DIRECTION/CHARGE. La phrase « un gate non applicable est N/A-JUSTIFIED » (l. 231) est verrouillée (HON-06). Sous-sections l. 249-265 = rituels de trace. | déplacer vers le module ; fusionner la table des modes avec RUN-* |
| FAST-PATH (l. 271-277) | Preuve minimale pour LITE/petit ITER. | gouvernance (allègement) | agent | Utile pour la charte (effort proportionné) mais répète `RUN-LITE` et `Chemin minimal`. Citée par 8 renvois externes, verrouillée par `check_reading_contract` (« sixième voie », l. 19). | fusionner avec `RUN-LITE`/`RUN-ITER` ; garder la règle « un fix local de contraste, libellé, focus ou wrapping reste LITE » (l. 277) dans le chemin de design |
| RUN_CARD (l. 281-411) | Format de la carte de run, profil de capacités, agent seul, snapshot, projection, frontière de validation. | gouvernance | équipe, outil | 18 178 caractères (15,5 % du fichier). Un seul bloc produit : `Mode agent seul et preuve dégradée` (l. 352-364). Table de correspondance l. 311-336 verrouillée par `validate_run_card.py` et les schémas. | déplacer vers le module de gouvernance en bloc ; extraire l. 352-364 (voir sous-sections) |
| RUN (l. 415-467) | Entrée / faire / sortie / clôture par mode (LITE, ITER, STANDARD, DIRECTION, SYSTÈME). | mixte | agent | Les « Faire » (l. 423, 433, 443, 453, 463) disent comment fabriquer ; les « Clôture » disent comment passer d'état. | scinder : « Faire » vers le chemin de design ; « Entrée/Sortie/Clôture » vers le module |
| CLOSE-PACKAGE (l. 471-521) | Paquet de clôture par mode, fraîcheur, réserves, droits, arrêt du polish. | gouvernance, sauf deux sous-sections | équipe | Table l. 475-481 verrouillée (machine). `Condition d'arrêt du polish` (l. 519-521) et `Responsabilité, droits et confidentialité` (l. 511-517) ont une valeur produit/risque. | déplacer vers le module ; extraire polish et droits (voir sous-sections) |
| PIPELINE-DIRECTION (l. 525-612) | Huit étapes d'une direction vérifiable, puis passe créative et polish. | mixte, plutôt design | agent | 12 213 caractères. Étapes 1-3, 6, 8 et `Passe créative et polish` = savoir de conduite du design ; 4-5, 7 et l. 529-535 = traçabilité et statuts. Contient le bloc `CHECKPOINT`. | scinder (voir sous-sections) |
| STRUCTURED-PROOF (l. 616-706) | Contrats : hiérarchie, partition typographique, asset directeur, composant/baseline, motion. | mixte, plutôt produit/design | agent, designer | Les contrats sont de bons guides de décision ; la table de déclencheurs (l. 620-630) et la « règle de phase » (l. 632) sont de la gouvernance. Schéma `production_contracts` verrouille 3 noms. | scinder : gabarits vers la bibliothèque de fabrication, déclencheurs vers le module |
| VISUAL_PROOF (l. 710-728) | Quelles captures produire et quoi en conclure. | produit | agent | Contient la vérification du rendu réel sur ordinateur et mobile (charte §4). Mêle `V/U/T NOT-VERIFIED` (gouvernance). Verrouillée par HON-07 (l. 727). | garder dans le chemin de design ; réécrire (forme) : colonne « si absente » en langage clair |
| GATE-A (l. 732-813) | Plancher objectivable : accessibilité, contraste, focus, cibles, états, honnêteté, motion réduite ; recette `check_render`. | produit (≈ 80 %) | agent, designer | Étiqueté « gouvernance » par chemins.json mais c'est le plancher de qualité R5-R7 de la grille résultat. 14 contrôles WCAG 2.2. Chargé dès LITE. | garder dans le chemin de design (module « plancher produit ») ; seul `Contrat de portée` et `Familles de méthodes` partent au module |
| GATE-B (l. 815-908) | Jugement contextualisé : comparaison, B1b (édition sur capture), familles de preuve, regard externe, corrections, trace d'assets, format de sortie. | mixte | agent, équipe | B1/B1b atelier/B4 = méthode de design ; B2 table « Gouvernance », B3, B5, B6 = formalités. Contient le bloc `BOUCLE-ATELIER`. | scinder (voir sous-sections) |
| GATE-C (l. 911-932) | Six critères de craft sur rendu réel, avec gestes de correction. | design/produit | agent, designer | C1-C6 = vrai savoir de craft avec geste de sortie (colonne de droite). Gouvernance minimale (verdict C). | garder dans le chemin de design ; fusionner `ANTI-SLOP` |
| ANTI-SLOP (l. 936-940) | Conséquence d'une matrice de `SAVOIR/CRAFT/CFT-01`. | design (pointeur) | agent | 678 caractères, ne reproduit rien (l. 938). Les deux phrases utiles : « une couleur de marque ou une construction soignée n'immunisent pas » et « watchlists = aides, pas interdits ». | fusionner avec GATE-C |
| OVERRIDE (l. 944-976) | `FAIL-ASSUMED` (échec connu diffusé) et péremption. | gouvernance | équipe | Utile en équipe/audit, hors du chemin de design. | déplacer vers le module de gouvernance |
| POLICIES (l. 980-1010) | Politique de contraste ; inspection et ressources techniques. | produit (contraste) + gouvernance (ressources) | agent | « Ne valide jamais le contraste à l'œil » (l. 984) est une règle produit de base ; les sept champs de ressource (l. 998-1006) sont de la maintenance. | scinder : contraste vers le plancher produit (fusion avec GATE-A) ; ressources vers le module |
| ROUTING (l. 1014-1031) | Routes `SAVOIR`/`BIBLIOTHEQUE` à ajouter selon la situation. | méta (routage) | agent | Dit « ne forme pas une seconde liste » (l. 1016) mais en forme une ; 27 codes /1000 mots. | fusionner avec `DIRECTION/CHARGE` (liste unique) |
| MAINTENANCE (l. 1035-1055) | Recette documentaire en 11 contrôles quand on modifie ACTION. | méta | mainteneur | Concerne le système, pas un run. | déplacer vers la doc de maintenance du système |
| CLOSE-EXIT-CHECK (l. 1059-1078) | Dix questions avant de clôturer ; mesure expérimentale. | gouvernance + méta | équipe, pilote | Q9 et Q10 (l. 1071-1072) = questions de qualité produit à garder. `Mesure expérimentale` = méta. | scinder : Q9-Q10 vers le chemin de design ; Q1-Q8 vers le module ; mesure vers la doc de maintenance |

### Sous-sections des sections mixtes : produit ou gouvernance

| Sous-section (ligne) | Caractères | Famille | À garder dans le chemin de design ? |
|---|---:|---|---|
| Responsabilité : rôle et « capacité positive » (l. 7-9) | ≈ 1 400 | méta | Réécrire. La phrase « la qualité du premier rendu, la lisibilité de la décision et la possibilité de reprendre le run font partie de la valeur livrée » (l. 9) est de la charte, pas de la gouvernance. |
| Carte de lecture par mode (l. 11-19) | 876 | méta | Non : la liste de chargement est dans `DIRECTION/CHARGE` ; cette sous-section dit qu'elle ne la répète pas (l. 13). Retirer ou fusionner. |
| HANDOFF — Réponse visible, bloc `SORTIE` (l. 33-47) | ≈ 2 000 | produit (communication) | **Oui.** Réponse en quatre rubriques en langage produit. Bloc `noyau` copié dans la skill. |
| HANDOFF — Handoff persistant (l. 25-31, 56-58, 60) | ≈ 3 000 | gouvernance | Non : module. |
| HANDOFF — Niveau de trace, bloc `TRACE` (l. 49-54) | ≈ 1 900 | mixte | **Oui pour la trace légère** (six lignes, `EXPLORATORY`) ; la partie « trace complète » (l. 53, fin) vers le module. Bloc `noyau` copié dans la skill. |
| Quatre registres (l. 62-86) | 2 998 | gouvernance | Non. Mais « ordre de preuve » (l. 75, `P0` direction/craft, `P1` plancher, `P2`, `P3`) est une règle de priorité produit : à garder. La table « ACTION ne remplace pas » (l. 77-84) est un vestige de partage de rôles (F11). |
| AUTHORITY (l. 88-92) | 993 | gouvernance | Non. |
| Parcours minimal (l. 94-96) | 401 | méta | Retirer (renvoi circulaire vers le noyau de la skill, qui est compilé à partir de ce fichier). |
| UI-UX-REALITY (l. 112-134) | 2 563 | produit | Oui. |
| STATUS : États du run, Issues, Règle de lecture, Chemin minimal (l. 142-185) | ≈ 5 100 | gouvernance | Non. Le `Chemin minimal` (l. 183-185) est un doublon. |
| STATUS : Principe positif de qualité (l. 187-189) | 682 | produit | Oui, fusionner avec FIRST-RENDER. Contient la règle « jamais clôturé sans observation du rendu ». |
| STATUS : Verdicts V/U/A/T (l. 192-203) | 1 080 | mixte | V, U, A, T sont quatre questions de qualité du produit (caractère, usage, accessibilité, robustesse) ; la liste de statuts autorisés est de la gouvernance. Garder les quatre questions dans le chemin de design. |
| STATUS : Statut de direction (l. 205-214) | 558 | gouvernance | Non. Garder la phrase « `HELD` ne signifie ni beau ni accepté » (l. 214) dans le module. |
| PRECONDITION : table des modes (l. 220-231) | ≈ 1 500 | gouvernance | Non. |
| PRECONDITION : Contrat de décision, post-build `EXTERNAL-START`, raccord `DESIGN-ATLAS` (l. 233-267) | ≈ 3 500 | gouvernance | Non. Une phrase à sauver : « produis ou conserve un détail, un asset, une variante ou une rationale seulement si sa conséquence est identifiable » (l. 267). |
| RUN_CARD : champs et table de correspondance (l. 283-340) | ≈ 8 300 | gouvernance | Non. |
| RUN_CARD : Profil de capacités (l. 342-350) | 1 776 | mixte | Idée à garder : « dire ce qu'on n'a pas pu observer » (charte principe 7). Le format est du module. |
| RUN_CARD : Mode agent seul et preuve dégradée (l. 352-364) | 1 822 | produit/honnêteté | **Oui.** Dit ce qu'un agent sans navigateur peut et ne peut pas conclure. Table l. 357-362 ; marqueur HON-05. |
| RUN_CARD : Vue d'exécution dérivée, Projection machine, Frontière de validation (l. 366-411) | ≈ 7 200 | gouvernance | Non. HON-04 et VAL-01 verrouillent le texte (l. 403-407). |
| RUN-LITE, ITER, STANDARD, DIRECTION, SYSTÈME : « Faire » (l. 423, 433, 443, 453, 463) | ≈ 1 300 | produit/design | Oui. « Produire dès le premier rendu une composition jugeable » (l. 443) ; « première scène présentable par défaut » (l. 453). |
| RUN-* : Entrée, Sortie, Clôture | ≈ 4 500 | gouvernance | Non. |
| CLOSE-PACKAGE : table, fraîcheur, réserves (l. 473-509) | ≈ 4 700 | gouvernance | Non. Fraîcheur de la preuve (l. 489-493) : idée utile (« une capture d'une version antérieure n'est pas une preuve de la version livrée »), à garder en une phrase. |
| CLOSE-PACKAGE : creative close (l. 487) | ≈ 800 | mixte | Les quatre questions (présence, signature, détail de craft, défaut dominant) sont du savoir de craft ; leur champ de schéma est de la gouvernance. |
| CLOSE-PACKAGE : Responsabilité, droits, confidentialité (l. 511-517) | 1 398 | produit/risque | **Oui, en version courte** : droits des assets, données sensibles, pas d'envoi vers un canal non sûr. Marqueur HON-08 est à la l. 689. |
| CLOSE-PACKAGE : Condition d'arrêt du polish (l. 519-521) | 665 | produit | **Oui.** Évite le polish sans fin. |
| PIPELINE : intro, boucle de qualité et branche one-shot (l. 527-535) | ≈ 1 700 | gouvernance | Non, sauf la règle « le one-shot ne s'applique pas si le premier rendu est faible » (l. 535). |
| PIPELINE 1 Situer les positions, 2 Traduire l'émotion, 3 Alternative située, 6 Contre la facilité (l. 537-555, 579-583) | ≈ 2 500 | design | **Oui.** « Premium/chaleureux/dynamique sont des intentions à traduire » (l. 549) ; « la faisabilité immédiate n'est pas une preuve d'appropriation » (l. 583). Les phrases sur la `trace_locator` et la projection JSON (l. 543, 553) vont au module. |
| PIPELINE 4 Spec visuelle, 5 Sourcer et tracer (l. 557-577) | ≈ 3 000 | mixte | Spec : garder la liste des décisions utiles (l. 563) et la définition d'une ancre utile (l. 565). Les phrases sur `RUN_CARD`, `identity_stake`, `calibration` (l. 569) et `VERIFIED-THIS-RUN` (l. 575) vont au module. |
| PIPELINE 7 Écrire la direction, bloc `CHECKPOINT` (l. 585-594) | 1 523 | mixte | **Oui pour le bloc** (l. 589-592 : la première proposition vaut checkpoint ; décisions irréversibles). Les l. 594 (renvoi `AUTHORITY`) vers le module. |
| PIPELINE 8 Vérifier le rendu réel (l. 596-598) | 798 | produit | **Oui.** « Ne corrige pas un défaut structurel par un effet décoratif terminal ». Les valeurs `CORRECTED/ACCEPTED-DIFFERENCE/REMAINING-RISK` avec leurs traductions de statut vont au module. |
| PIPELINE Passe créative et polish (l. 600-612) | 2 752 | design/produit | **Oui.** Revue créative, repasse ciblée, niveaux `Correction/Précision/Intention`, « aucune itération fixe ». |
| STRUCTURED-PROOF : Carte de hiérarchie, Partition typographique, Fiche d'asset, Motion (l. 634-706) | ≈ 5 200 | produit/design | Oui (champs en langage clair) : listes de questions de décision utiles. Marqueur HON-08 (l. 689) à traiter à part. |
| STRUCTURED-PROOF : table de déclencheurs, règle de phase, contrat de composant/baseline (l. 618-632, 692-700) | ≈ 1 800 | gouvernance | Table et règle : module. Baseline : « une différence intentionnelle n'est pas une régression » (l. 698) à garder en produit. |
| GATE-A : Contrat de portée (l. 736-751) | 1 438 | gouvernance | Module. Idée à garder : WCAG 2.2 comme base par défaut (l. 751). |
| GATE-A : Familles de méthodes, provenance minimale, Adéquation des preuves (l. 753-774) | ≈ 3 000 | gouvernance | Module. La table « Adéquation » (l. 768-774) a un équivalent utile court : « une capture ne prouve pas l'utilisabilité ». |
| GATE-A : Contrôles applicables et profils de surface (l. 776-803) | ≈ 8 100 | produit | **Oui.** Les 14 contrôles, plus la table de profils (GTA-01, l. 795). |
| GATE-A : recette `check_render`, résoudre un contraste, couverture (l. 805-812) | ≈ 4 000 | produit (outil) | Oui, mais à mettre dans la fiche de l'outil. Texte très dense : un seul paragraphe de 3 500 caractères (l. 805). |
| GATE-B : B1 comparaison relationnelle (l. 819-825) | 655 | design | Oui. |
| GATE-B : B1b et atelier d'édition (l. 827-851) | 4 750 | mixte | **Atelier** (l. 835-841, bloc `BOUCLE-ATELIER`) : oui, c'est la méthode. Le reste (l. 829, 843-849 : `closure.b1b`, `closure.b1b.reason`, `NARRATIVE-DIFFERENCE`) : module. Un titre de niveau 4 (l. 833). |
| GATE-B : B2 Familles de preuve (l. 853-864) | 1 176 | gouvernance | Module. La famille « Gouvernance » (l. 862) y est nommée comme axe, ce qui montre le mélange. « Une note sur cinq » (l. 864) : échelle jamais définie (à vérifier). |
| GATE-B : B3 Regard externe (l. 866-889) | 1 908 | gouvernance | Module. Idée à garder : « une seconde session du même auteur n'est pas un regard externe » (l. 868). |
| GATE-B : B4 Corrections ancrées (l. 891-895) | 501 | design | Oui, fusionner avec la passe créative. |
| GATE-B : B5, B6 (l. 897-907) | ≈ 970 | gouvernance | Module. |
| POLICIES : Politique de contraste (l. 982-988) | 676 | produit | Oui, fusionner avec GATE-A. |
| POLICIES : Inspection et ressources (l. 990-1010) | 1 361 | mixte | Idée produit : « une baseline d'états pertinents pour les composants critiques » (l. 1010). Sept champs de ressource : module. |

## Défauts

| n° | Type | Gravité | Preuve | Proposition |
|---|---|---|---|---|
| D1 | structure / convergence | bloquant | Le plancher de qualité du produit (premier rendu, UI/UX, accessibilité, craft, preuve visuelle) est dans ce fichier de gouvernance, entre `STATUS` et `OVERRIDE`. Le chemin de design charge ACTION pour lire ces règles : `chemins.json` liste `FIRST-RENDER`, `UI-UX-REALITY`, `VISUAL_PROOF`, `GATE-A`, `GATE-C` dans les chemins DIRECTION. Le critère S9 (gouvernance séparable) échoue de ce fait. | Scinder en deux : « qualité du rendu » (chemin de design) et « module de gouvernance » (facultatif). Voir synthèse. |
| D2 | structure | important | `GATE-A` est classée « gouvernance » par `chemins.json` (« ACTION/GATE-A, 12016, gouvernance »), alors que ≈ 80 % de son contenu (contrôles, profils, recette de rendu, contraste) est du plancher produit. Elle est chargée dès LITE. | Reclasser dans `mesures`/`chemins` après le partage ; ne laisser au module que `Contrat de portée`, `Familles de méthodes`, `Adéquation`. |
| D3 | répétition | important | Cinq énoncés de « charger peu et s'arrêter » : l. 15 (socle), l. 60 (condition d'arrêt de lecture), l. 94-96 (parcours minimal), l. 183-185 (chemin minimal), l. 271-277 (FAST-PATH), plus l. 86 (Chargement). | Un seul énoncé, dans le chemin court ; fusionner `FAST-PATH` avec `RUN-LITE`. |
| D4 | répétition | important | La qualité du premier rendu est posée l. 9, 98-110, 187-189, 443, 453, 1071. | Garder `FIRST-RENDER` ; fusionner 187-189 ; les autres deviennent des renvois d'une ligne. |
| D5 | répétition | important | « Pas de PASS par défaut / NOT-VERIFIED » : l. 231, 350, 364, 404, 485, 762, 774, 915, 1074 (9 fois). | Dire la règle une fois, dans le module ; dans le chemin de design, une phrase « si tu n'as pas pu le vérifier, dis-le ». |
| D6 | langue | important | Le bloc `SORTIE`, censé être « sans le jargon interne » (l. 37), cite dans la même phrase `ACTION/STATUS`, `N/A-JUSTIFIED`, `NOT-OBSERVED` (l. 46). Ce bloc est copié dans la skill. | Réécrire (forme) le paragraphe l. 46 sans codes, après accord ; toucher `build_core.py`/concept SOR-01 en phase 5 seulement. |
| D7 | structure | important | Deuxième liste de chargement : `ACTION/ROUTING` (l. 1014-1031) alors que `DIRECTION/CHARGE` est « la seule du corpus » (l. 7, 13). | Fusionner dans `DIRECTION/CHARGE` (colonne « Ajouter seulement si »). |
| D8 | répétition | mineur | `ANCHOR-GENERATED` (l. 561) ↔ DIRECTION.md:656 ↔ SAVOIR.md:545 ; « aucun nombre fixe d'itérations » (l. 612, 895, 1047) ; P0-P3 (l. 75 ↔ DIRECTION.md:108) ; « reviens à un mode plus riche » (l. 277 ↔ DIRECTION.md:172). | Un propriétaire, deux renvois. |
| D9 | coût de lecture | important | Chemin LITE ≈ 15 900 caractères d'ACTION (chemins.json) dont 12 016 pour `GATE-A` ; le chemin DIRECTION trace complète charge en plus `RUN_CARD` 18 215 + `CLOSE-PACKAGE` 6 953 + `GATE-B` 9 140. | Après le partage, le chemin de design charge le plancher produit seul (≈ 14 000 caractères pour tout), le module reste à la demande. |
| D10 | structure | mineur | Titre de niveau 4 (`#### Atelier d'édition`, l. 833). | Passer en niveau 3 ou fusionner avec B1b. |
| D11 | structure | mineur | `ACTION/ANTI-SLOP` (l. 936-940) est un pointeur de 678 caractères. | Fusionner avec GATE-C. |
| D12 | structure | mineur | La table des documents « ACTION ne remplace pas » (l. 77-84) ressemble à la table de rôles que README.md:114 et le glossaire portent déjà. | Retirer la table, garder le renvoi. |
| D13 | obsolète | mineur | Bandeau « expérimentation maintenue » (l. 3) ; mesure « vestige » `ne porte plus` (l. 212) est un faux positif (« le rendu ne porte plus la direction retenue » = statut `LOST-IN-BUILD`). | Bandeau : décision de version (hors ce fichier). Corriger le motif du script de mesures. |
| D14 | langue | important | Collision de lettres : Gate A/B/C contre axes V/U/A/T (avertissement l. 177) ; sous-gates `B1b`, `C1`-`C6`, `HON-xx`, `P0`-`P3` ; `JTBD`, `blast radius` non définis. | Noms parlants pour le chemin de design (ex. « plancher produit », « craft ») ; codes gardés dans le module. |
| D15 | risque | important | `check_action_projection_source` (validate_design_governance.py:200-215) interdit tout bloc ```yaml/json dans ACTION et exige la citation de `schemas/run_card.example.json` ; si RUN_CARD part dans le module, ce contrôle doit suivre. | Déplacer le contrôle avec la section ; ne pas casser l'invariant. |
| D16 | coût de lecture | mineur | Paragraphe unique de 3 500 caractères sur la recette `check_render` (l. 805). | Découper en liste (comportement, options, limites). |
| D17 | convergence | mineur | Voir section « Ce qui fige ». | Garder les gabarits comme listes de questions, pas comme tableaux à remplir. |
| D18 | structure | mineur | Titre du fichier « Pipeline de livraison & preuves » (l. 1) ne désigne ni la qualité produit ni la maintenance. | Après la scission, deux titres clairs. |

## Savoir à protéger

Chaque ligne : unité de savoir, plage de lignes, famille.

**Produit et design (à garder dans le chemin de design)**
- Premier rendu composé, crédible, spécifique, « pas une ébauche à rendre présentable plus tard » ; table par mode : l. 98-110 (produit).
- Contrat UI/UX : contenu, tâche, premier geste, états `loading/empty/error/…`, responsive recomposé, accessibilité, robustesse ; l'état qui ouvre la page est rempli : l. 112-132 (produit).
- Principe positif de qualité ; jamais clôturé sans observation du rendu : l. 187-189 (produit).
- Les quatre questions V/U/A/T (caractère, usage, accessibilité, robustesse) : l. 192-203 (produit).
- Ordre de preuve P0-P3 : le craft visuel avant le plancher, la protection critique avant l'optimisation ; P1 non négociable : l. 75 (produit).
- Un fix local de contraste, libellé, focus ou wrapping reste LITE : l. 277 (produit).
- Mode agent seul : ce qu'on peut et ne peut pas conclure sans navigateur ou regard externe : l. 352-364 (honnêteté, HON-05).
- Réponse visible en quatre rubriques, sans jargon : l. 35-47 (bloc SORTIE, SOR-01).
- Trace légère de six lignes ; la proposition reste `EXPLORATORY` : l. 51-54 (bloc TRACE, TRA-01).
- La première proposition vaut checkpoint ; action irréversible = accord préalable : l. 589-592 (bloc CHECKPOINT, CHK-01).
- Atelier d'édition : lecture légère de la capture, éditer une décision par retrait/réduction/transformation, garder l'original est un résultat valide : l. 835-841 (bloc BOUCLE-ATELIER).
- Positions distinctes, émotion à traduire en levier visuel, alternative située, ne pas construire de variante inutile : l. 537-555 (design).
- Faisabilité n'est pas appropriation : l. 579-583 (design).
- Spec visuelle : décisions utiles seulement ; ancre utile = décision + contre-indication + attributs retenus/rejetés/non transférables : l. 557-565 (design).
- Observer l'asset à son ratio, crop, contraste, voisinage réels : l. 577 (produit).
- Vérifier le rendu réel contre la spec ; pas de défaut structurel corrigé par un effet décoratif : l. 596-598 (produit).
- Passe créative : revue `CFT-00`, repasse sur masses, vides, échelles, rythme ; effets sans relation observable ne sont pas du polish : l. 600-612 (design).
- Quatre questions du creative close (présence, signature, détail de craft, défaut dominant) : l. 487, 606 (design).
- Niveaux de craft `Correction/Précision/Intention` (lentille locale, pas un score) : l. 610 (design).
- Condition d'arrêt du polish ; `STOP — [raison]` : l. 519-521 (produit).
- Droits, provenance ≠ licence ; données sensibles non envoyées vers un canal non garanti : l. 511-517, 690 (HON-08) (risque).
- Contrats de décision utiles : hiérarchie, partition typographique, fiche d'asset directeur, motion/3D, baseline ; différence intentionnelle ≠ régression : l. 634-706 (design/produit).
- Captures : desktop, mobile (390/768/1440), détail, masses, états ; « une capture prouve le rendu, pas la tâche » ; asset généré = ancre, pas preuve : l. 716-728 (HON-07).
- Gate A, 14 contrôles + profils de surface : l. 776-803 (GTA-01) ; référence WCAG 2.2, WCAG 3.0 en veille : l. 751 ; contraste calculé jamais à l'œil, APCA complémentaire : l. 984-986.
- Recette `check_render` : comportement, options, limites (rien n'est `PASS` si non mesuré) ; contraste SVG, couverture, `--proof` : l. 805-812 (outil).
- Gate B : comparaison relationnelle (B1) l. 819-825 ; corrections ancrées (B4) l. 891-895.
- Gate C : six critères avec geste de correction ; verdict C cite un élément concret ; correction retourne à la direction, pas à un décor : l. 911-932.
- Anti-slop : couleur de marque ou construction soignée n'immunisent pas ; watchlists = aides : l. 940.
- Questions de clôture sur la qualité visée au premier rendu et sur ce qui a vraiment changé : l. 1071-1072 (Q9, Q10).

**Gouvernance (à garder, dans le module)**
- États du run (7), issues (6), verdicts globaux, statuts de direction, compatibilités : l. 142-214.
- Table des paquets minimaux par mode et contrôle machine : l. 222-228, 475-481.
- `DECISION-INTENT` / `DECISION-CHANGE` et valeurs de repli `N/A-JUSTIFIED`, `NOT-OBSERVED` : l. 171, 233-247, 249-259.
- Raccord de trace `DESIGN-ATLAS` : l. 261-265.
- Handoff persistant et forme courte LITE : l. 25-31, 56-58.
- Quatre registres observation / interprétation / décision / persistance : l. 62-73.
- Autorité de reprise, `APPROVED` ≠ accepté : l. 88-92.
- `RUN_CARD` : champs, protection critique, table de correspondance, `STATUS` interdit comme champ unificateur : l. 283-340.
- Profil de capacités et `basis` typée : l. 342-350.
- Vue d'exécution dérivée (`EXECUTION-SNAPSHOT`) : l. 366-391 ; projection machine : l. 393-399.
- Frontière de validation (HON-04) et ce qu'atteste une RUN_CARD (VAL-01) : l. 401-411.
- Routes de run : entrées/sorties/clôtures par mode : l. 419-467.
- Fraîcheur de la preuve ; cycle de vie des réserves à sept champs : l. 489-509.
- Owner de décision finale : l. 513.
- Contrats structurés : table de déclencheurs, règle de phase : l. 618-632.
- Contrat de portée, familles de méthodes, provenance minimale des verdicts acceptés : l. 736-764.
- B1b : champs `closure.b1b`, deux seuls motifs `N/A-JUSTIFIED`, `NARRATIVE-DIFFERENCE` : l. 827-849.
- B2 familles de preuve ; B3 regard externe et ses neuf champs ; B5 ; B6 : l. 853-907.
- `FAIL-ASSUMED` : journal, champs `closure.exception`, interdits de sécurité ; péremption : l. 944-976.
- Ressources techniques : sept champs, trois cas d'outil : l. 990-1006.
- Routage des prérequis (si conservé) : l. 1014-1031.
- Recette de maintenance en 11 contrôles ; mesure expérimentale : l. 1035-1055, 1076-1078.

## Ce qui fige ou pousse à la convergence

- **Tableau « Partition typographique »** (l. 665-671) : cinq rôles fixes (Fonctionnel, Éditorial, Microcopie, Donnée, Signature), colonnes pré-remplies. Risque : l'agent remplit toujours les cinq rôles. À présenter comme question, pas comme tableau.
- **Carte de hiérarchie** (l. 636-644) : neuf champs imposés, y compris sur des demandes où la hiérarchie n'est pas en jeu. Déclencheur déjà limité (l. 622), mais le gabarit invite au remplissage.
- **Largeurs par défaut 390, 768, 1440** (l. 725, 805) : réglage de l'outil. Risque faible, mais l'agent peut ne jamais tester d'autres tailles (mobile étroit, très large). À noter comme défaut, pas comme règle.
- **Table des états attendus** (`loading, empty, error, unavailable, disabled, succès partiel`, l. 114) : bonne liste de contrôle, mais l'agent peut en faire un jeu complet par défaut sur chaque écran. Le texte dit « lorsque pertinents » : à garder en tête de liste.
- **Quatre réponses du creative close** (l. 487, 606) et **six critères C1-C6** (l. 921-928) : même grille à chaque run, mêmes mots. Peut produire des justifications uniformes. À vérifier à l'usage (hors sujet de rangement).
- **Gabarit de réponse visible** (l. 39-44, « Ce que j'ai fait / Pourquoi / Ce qui manque / La suite ») : fixe la forme de toute réponse. Intentionnel (SOR-01), à garder tel quel.
- Aucune valeur de couleur, police, taille en pixels de mise en page ni code type n'a été relevée.

## Dépendances et risques de déplacement

- **Blocs `noyau` copiés dans la skill** (par `scripts/build_core.py`, lignes 54, 57-58 ; copie dans `skills/design-governance-practice/SKILL.md`, section générée l. 12-216) :
  - `SORTIE` : l. 35-47 de ACTION, dans « 10. Proposition, sortie et trace » (SKILL.md:200).
  - `TRACE` : l. 51-54, même section.
  - `CHECKPOINT` : l. 589-592, même section.
  - `BOUCLE-ATELIER` : l. 835-841, dans « 9. Boucle d'édition » (SKILL.md:165).
  - Déplacer un de ces blocs impose de mettre à jour le tuple de `build_core.py:54-58` et le budget de la skill (`test_core_budget.py`) ; à faire en phase 5, pas avant. Deux de ces blocs renvoient à des sections qui partent au module : `TRACE` cite `RUN_CARD`, `B1b`, `ACTION/HANDOFF` ; `BOUCLE-ATELIER` cite `ACTION/GATE-B/B1b` et la « trace complète » ; `CHECKPOINT` cite « absolu 2 de `DIRECTION` » et « gates et verdict ». Sans réécriture, le noyau de design dépend du module de gouvernance.
- **Marqueurs `concept:` verrouillés par `validate_structure.py:59-79`** : `SOR-01` (l. 36), `TRA-01` (l. 52), `HON-06` (l. 230), `HON-05` (l. 354), `HON-04` (l. 403), `VAL-01` (l. 406), `CHK-01` (l. 590), `HON-08` (l. 689), `HON-07` (l. 727), `GTA-01` (l. 795). Chaque marqueur est attaché à un fichier (`ACTION.md`) : un déplacement exige de changer le fichier attendu. Texte VAL-01 aussi protégé en `validate_structure.py:113` (phrase « Ce qu'atteste une `RUN_CARD` validée » : `{ACTION.md, CHANGELOG.md}`).
- **Aiguille de ligne `ROW_NEEDLES`** (validate_structure.py:728) : la ligne `| Token, composant ou blast radius |` doit contenir « si un composant change » (ACTION.md, l. 1029). Si `ROUTING` fusionne dans `DIRECTION/CHARGE`, ce contrôle doit suivre.
- **Contrôles de lecture** (validate_design_governance.py:201-283) : `check_action_projection_source` (pas de bloc yaml/json, citation du JSON canonique, l. 397) ; `check_reading_contract` (modes en backticks, « Carte de lecture par mode » l. 11, `RUN_CARD`, `FAST-PATH` + « sixième voie » l. 19) ; `check_experimental_position` (bandeau l. 3 et sa négation). Le retrait de la carte de lecture (disposition proposée) casse le deuxième.
- **Lecteur de routes** : `read_route.py` / `chemins.json` s'appuient sur les identifiants `ACTION/RUN-LITE`, `ACTION/GATE-A`, `ACTION/GATE-B/B2`, `ACTION/GATE-B/B6`, etc. ; `test_read_route.py:102` supprime ACTION.md pour tester l'erreur. Renommer ou scinder une section change les routes.
- **Qui cite ACTION** (nombre de renvois hors ACTION, hors fixtures) : `ACTION/RUN-*` 46, `GATE-A` 28, `HANDOFF` 24, `GATE-B` 22, `CLOSE-PACKAGE` 18, `RUN_CARD` 14, `UI-UX-REALITY` 13, `PIPELINE-DIRECTION` 11, `STATUS` 11, `OVERRIDE` 9, `GATE-C` 9, `FAST-PATH` 8, `STRUCTURED-PROOF` 7, `CLOSE-EXIT-CHECK` 6, `FIRST-RENDER` 5, `VISUAL_PROOF` 4, `POLICIES` 4, `ROUTING` 4, `AUTHORITY` 3, `ANTI-SLOP` 3, `PRECONDITION` 1, `MAINTENANCE` 0. Ils viennent de DIRECTION, SAVOIR, BIBLIOTHEQUE, READING_MAP, QUICKSTART, GLOSSAIRE, la skill et ses références ; plus 24 fixtures de `schemas/fixtures/` et `run_card.example.json`.
- **Ce qu'ACTION cite** : `DIRECTION/CHARGE`, `DIRECTION/START`, `DIRECTION/DOUBLE-LOOP`, `DIRECTION/VISUAL_TARGET`, `DIRECTION/EXTERNAL-START`, `DIRECTION/CREATIVE-BOOT`, `SAVOIR/CRAFT/CFT-00`, `CFT-01`, `CFT-02`, `CFT-05`, `SAVOIR/STATE`, `SAVOIR/TYPE`, `SAVOIR/TOOLS`, `SAVOIR/CONTEXT`, `SAVOIR/TECH`, `SAVOIR/INTEGRITY`, `BIBLIOTHEQUE/SELECT`, `BIBLIOTHEQUE/COMPONENTS`, `BIBLIOTHEQUE/GATE`, `CHANGELOG.md`, `READING_MAP.md`, `schemas/run_card.example.json`, `schemas/production_contracts.schema.json`, `scripts/validate_run_card.py`, `scripts/check_render.py`, `scripts/test_check_render.py`.
- **Machine liée à la RUN_CARD** : `validate_run_card.py` (1 085 lignes, 18 phrases verrouillées), `run_card.schema.json`, 24 fixtures. Si le module de gouvernance devient facultatif, ces scripts et schémas suivent la section RUN_CARD et ne doivent pas être appelés par le chemin de design.
- **Risque propre à la scission** : `STATUS`, `RUN_CARD` et `CLOSE-PACKAGE` se renvoient en boucle ; les couper sans carte de correspondance fait perdre des liens (F13). Une table de correspondance ligne à ligne est nécessaire avant tout déplacement.

## Synthèse

- ACTION est à ≈ 60 % de la gouvernance (états, RUN_CARD, clôture, override, maintenance) et à ≈ 40 % le vrai plancher « pro » du produit : premier rendu, UI/UX, accessibilité (14 contrôles), preuves visuelles, craft Gate C, passe créative, polish. Ce plancher est aujourd'hui noyé dans un fichier de gouvernance, et le chemin de design ne peut pas le lire sans ouvrir le reste (D1, S9).
- Proposition : extraire un module « qualité du rendu » (FIRST-RENDER, UI-UX-REALITY, VISUAL_PROOF, GATE-A contrôles et profils, GATE-C, passe créative et polish, étapes 1-3, 6, 8 du pipeline, arrêt du polish, droits, mode agent seul, atelier, checkpoint, SORTIE et TRACE légère, Q9-Q10) dans le chemin de design ; et un module de gouvernance facultatif (STATUS, PRECONDITION, RUN_CARD, RUN, CLOSE-PACKAGE, OVERRIDE, B1b formel, B2-B3, B5-B6, MAINTENANCE).
- Trois pièges à traiter avant tout déplacement : les quatre blocs `noyau` renvoient à des sections du module (le noyau de design dépend alors de la gouvernance) ; dix marqueurs `concept:` et trois contrôles de lecture verrouillent des phrases d'ACTION ; `GATE-A` est classée « gouvernance » à tort.
- Doublons à fusionner d'abord, sans changer le fond : cinq énoncés de chemin minimal, quatre énoncés de qualité du premier rendu, neuf énoncés de « pas de PASS par défaut », `ROUTING` face à `DIRECTION/CHARGE`, `ANTI-SLOP` dans `GATE-C`.
