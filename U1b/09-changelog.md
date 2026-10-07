# U1b — Fiche d'inventaire n°9 : le CHANGELOG et les notes de version

**Base :** commit `d90869c`. **Lecture intégrale :** `V1/official/CHANGELOG.md` (86 lignes, 16 Ko) et `RELEASE_NOTES.md` (140 lignes, 16 Ko), plus le workflow CI `.github/workflows/validate.yml`, qu'ils citent. **Vérifié :** les affirmations chiffrées et techniques, contre le paquet réel et par trois petits tests (T-21a à T-21c) ; le résultat du run CI déclenché par notre commit. **Angle :** ce que ces fichiers établissent, ce qu'ils promettent, et ce qu'ils disent eux-mêmes de la suite.

## 1. Identité

| Fichier | Statut | Lecteur visé | Consommé par un script ? |
|---|---|---|---|
| `CHANGELOG.md` | **Source normative** (une des cinq) : version, cycle de vie des routes, migration | Mainteneur, auditeur | **Oui** : `read_route.py --connexions` refuse l'index de READING_MAP si sa révision diffère de celle du CHANGELOG (`R2026-10-04-AUDIT2-FIXES`, identique dans README, READING_MAP l. 80 et RELEASE_NOTES) |
| `RELEASE_NOTES.md` | Dérivé, à la racine | Personne qui découvre la version | Non |

## 2. Ce qu'ils possèdent

### CHANGELOG

| Élément | Lignes | Concr. | Valeur au regard de la mission |
|---|---|---|---|
| En-tête : version V1.0.0 du 2026-10-01, statut expérimental, usage en pilote supervisé | 1-8 | O | Honnêteté sur la maturité |
| Résumé de V1.0.0 en 15 points (sources, noyau, direction, trace graduée, vérité du contenu, ancre graduée, interfaces, entrées, projection machine, contrôles, budget, recherche, préparation, recette de rendu, efficacité) | 12-28 | O | **La meilleure vue d'ensemble du système en une page** |
| Quatre décisions de révision (audit 2, audit 1, mobilisation, activation). Chacune nomme un périmètre, des consommateurs, la compatibilité, le mainteneur, les régressions, les limites, la revue suivante et la procédure de retour | 32-44 | A (pour le mainteneur) | Traçabilité complète des changements. Très dense : un seul paragraphe va jusqu'à environ 1 400 caractères |
| **Règle d'évolution** : toute évolution nomme une source normative unique, un propriétaire, un périmètre, la compatibilité, la preuve attendue, la limite, la prochaine revue et la procédure de retour ; elle ne devient règle transversale qu'après décision explicite du propriétaire | 50 | **A** | **La procédure de changement du système lui-même.** Elle s'applique à notre refonte |
| Cycle de vie des routes : `SEED` → `PILOT` → `ADOPTED` → `DEPRECATED` → `ABANDONED`. `ADOPTED` exige le contrat de gain réel de `BIBLIOTHEQUE/EVOLUTION` | 54-66 | A | **Le seul mécanisme prévu pour faire mûrir la bibliothèque.** Il n'a jamais servi : les 35 routes sont SEED (fiche n°2) |
| Migration de 5 anciens alias `REFERENCES/*` | 68-80 | A | Héritage ; le validateur vérifie qu'ils ne réapparaissent pas comme routes actives (`validate_design_governance.py:259`) |
| Limites : une validation ne remplace ni l'observation d'un rendu, ni un test utilisateur, ni une mesure | 82-86 | O | Honnêteté |

### RELEASE_NOTES

| Élément | Lignes | Concr. | Valeur |
|---|---|---|---|
| Révision AUDIT2 : corrections F07 à F10, mesures, compatibilité | 7-17 | O | Détail technique |
| Révision AUDIT : F01 à F06, puis capacités de mobilisation et d'activation conservées | 19-59 | O | Historique condensé |
| Présentation, points clés, contenu, parcours (personne, agent, opérateur) | 61-99 | O | Redite du README et du CHANGELOG ; **sixième version du parcours principal** (l. 93-97) |
| **« Ce que le validateur atteste »** : la forme et les invariants, mais ni que les observations ont eu lieu, ni la justesse des jugements, ni les droits, ni la qualité perceptuelle | 121-132 | O | **La formulation la plus claire de la frontière des validateurs** dans tout le paquet |
| Limites déclarées : efficacité non vérifiée, convergence non garantie, coût du run non mesuré, macOS et Windows non observés, placeholders non filtrés dans les champs libres | 134-140 | O | Honnêteté |

## 3. Vérification des affirmations

| Affirmation | Où | Vérification | Résultat |
|---|---|---|---|
| Noyau de 43 201 octets sur un budget de 46 000 | RN l. 13 | `wc -c SKILL.md` | **Exact** |
| 42 blocs dans le noyau | CL l. 34 | Balises `noyau:début` distinctes | **Exact** |
| 69 fichiers GitHub, 63 Local | CL l. 38 ; RN l. 15 | Distributions construites en U1 | **Exact** |
| Deux sous-locators de `SAVOIR/TOOLS` | CL l. 34 | `TOOLS/CONVERGENCE` et `TOOLS/MOYENS` | **Exact** |
| Prise de brief : au plus trois demandes | CL l. 16 | DIRECTION l. 350 | **Exact** |
| Marqueurs `[VEILLE 2026-09]` | CL l. 16 | Présents dans SAVOIR (3) et le noyau (1) | **Exact** |
| Options `--log` et `--journal` équivalentes | CL l. 26 | `preparer_livraison.py` l. 165 | **Exact** |
| Clés `contrast_coverage`, `proof_observations`, `keyboard_coverage` | RN l. 15 | `check_render.py` | **Exact** |
| Le profil strict refuse `example.com/org/net` et `.invalid` | RN l. 11 | `validate_run_card.py` l. 602 | **Exact** |
| `maxItems: 3` retiré, minimum de 2 directions | CL l. 42 | Schéma (fiche n°8) | **Exact** |
| Vocabulaire de `SAVOIR/STATE` compilé dans la skill | RN l. 55 | « Cohérence de rayon » présent dans `SKILL.md` | **Exact** |
| Une capacité ne peut pas être à la fois disponible et indisponible ; la comparaison ignore seulement les espaces en bordure | RN l. 45, 47 | T-21a : même libellé → refusé ; T-21b : espaces autour → refusé ; T-21c : majuscule initiale → **accepté** | **Exact, limite comprise** : la casse n'est pas normalisée, comme annoncé |
| CI : « exécution NOT-VERIFIED » | RN l. 119 | Run 37603355045 sur notre commit `d90869c` | **Désormais vérifié : succès** (45 s). Mais le workflow n'installe ni Playwright ni Chromium : les 26 cas navigateur y restent non vérifiés. Le vert de la CI ne couvre donc pas `check_render` dans un vrai navigateur |
| Six parcours simulés, « rendus vectoriels », rapport de correction, historique | RN l. 43 ; CL l. 36, 52 | — | **Invérifiable** : tout est déclaré « hors distribution » |

Aucune affirmation vérifiable n'a été trouvée fausse.

## 4. Ce que le système dit lui-même de sa suite

Chaque révision se termine par sa « prochaine revue ». Toutes renvoient au même manque :

| Révision | Prochaine revue annoncée |
|---|---|
| Audit 2 | « observations spécialisées dans des travaux réels » |
| Audit 1 | « observer les cas de navigateur » |
| Mobilisation | « usage situé […] avec effet attendu, observation et coût retrouvables » |
| Activation | « **une réalisation complète comparée**, avec relation attendue, rendu, correction et limites retrouvables » |
| RELEASE_NOTES l. 37 | « La prochaine preuve attendue est **une réalisation complète avec comparaison des effets attendus et observés** » |

Et la ligne « Efficacité : `NOT-VERIFIED` » figure dans les deux fichiers. **Le système désigne donc lui-même la mesure de référence (U2) comme sa prochaine étape**, et il ne l'a jamais faite.

Deux règles de retour vont aussi dans le sens de ta demande de simplicité. La révision d'activation prévoit de retirer son relais « si [son] coût ou [son] caractère prescriptif dépasse [sa] contribution observable ». La révision audit 2 traite ressources et médiums « sans nouveau registre obligatoire ni installation ». Retirer est donc prévu par le système, pas seulement ajouter.

## 5. Ce qu'ils ne possèdent pas

1. **Aucun résultat d'usage.** Ni rendu, ni comparaison, ni mesure de qualité ou de coût. Les preuves des révisions passées sont hors distribution.
2. **Aucune entrée lisible pour une personne non technique** dans le CHANGELOG. Les décisions sont écrites pour un auditeur (F07, R01, LCF-51…) en paragraphes très longs.
3. **Aucune route n'a jamais changé de statut**, alors que le cycle de vie existe.

## 6. Observations à verser au registre

| Observation | Preuve | Lien |
|---|---|---|
| Toutes les affirmations vérifiables des notes sont exactes | §3 | Fiabilité documentaire confirmée |
| CI verte sur `d90869c`, mais sans navigateur : `check_render` n'y est pas exercé en vrai | Run 37603355045 ; `validate.yml` | Nouveau ; à mentionner si on s'appuie sur la CI en U8 |
| La règle d'évolution (l. 50) impose 8 éléments et une décision du propriétaire pour chaque changement. Le plan (U8) prévoit de mettre à jour CHANGELOG et RELEASE_NOTES, mais ne demande pas encore ces 8 éléments pour chaque lot | CHANGELOG l. 50 ; plan l. 169 | **À intégrer au plan** (à discuter) |
| Le système annonce lui-même « une réalisation complète comparée » comme prochaine preuve | §4 | Confirme la priorité de U2 |
| Le cycle de vie des routes n'a jamais servi | CHANGELOG l. 54-66 ; 35 routes SEED | Fiche n°2 |
| RELEASE_NOTES ajoute une sixième version du parcours principal | RN l. 93-97 | Correction de la fiche n°7 (5 → au moins 6) |
| Les preuves des révisions passées sont hors distribution | CL l. 36, 52 ; RN l. 43 | Invérifiable |

## 7. En une phrase

Le CHANGELOG et les notes de version sont **exacts sur tout ce qu'on peut vérifier** et **honnêtes sur leurs limites**. Ils possèdent une **procédure de changement rigoureuse** et un **cycle de vie des routes** qui n'a jamais servi. Surtout, chaque révision désigne la même prochaine étape : **une réalisation complète comparée, qui n'a jamais été faite**.
