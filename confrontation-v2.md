# Confrontation — Design Governance face aux recherches, version 2

22-10-2026. Document de travail, hors paquet. Il prolonge la [version 1](confrontation-systeme-recherches.md) du 21-10-2026 et en garde les niveaux de preuve et les verdicts.

## But

Refaire la confrontation sur le système actuel : révision `R2026-10-21.2`, commit `1920ccd` de la branche `ccr-35204e53-0om9bb`. La version 1 portait sur `c77a8bc`.

Trois questions guident ce document :
- quels écarts relevés le 21 sont fermés dans les textes et dans les outils ;
- ce que le premier run de la révision (run 7, condition C) montre de leur usage réel ;
- ce qui reste ouvert.

## Corpus

| Corpus | Apport à cette version |
|---|---|
| Recherches 1 à 3 (Exa, 21-10-2026) et notes du 20-10 | Inchangées ; constats repris de la version 1 |
| Discussion sur la mobilisation (21-10-2026) | Écart entre savoir et faire : outil nécessaire mais non appelé dans 26 à 54 % des cas, l’écart se jouant au passage à l’acte ([P] Fan et al., arXiv 2605.14038). Contexte apporté au moment utile plutôt que chargé d’avance ([D] Anthropic, *Effective context engineering for AI agents*). Connaissance de cas concrets plus utile que des règles abstraites ([R] KATE, Findings ACL 2026) |
| État de référence | 15 productions, 7 journaux (version 1) |
| Run 7, atelier de lutherie (`runs/7-lutherie/`) | Une production, son journal, sa fiche de mobilisation, la recette de caractère face au caractère attendu, et la note de l’agent sur la skill |

## Synthèse

1. **Les sept ajustements sont dans le système, à l’essai.** Les manques de la version 1 sont fermés dans les textes. Il s’agit de l’harmonie de couleur, de l’identité dans la durée, de la limite de l’auto-critique, des surfaces translucides et des familles par défaut. Restent en `PILOT` les cartes de moment, les gestes servis, le registre, le spécimen et la planche.
2. **Le savoir poussé à un moment fixe a été lu, et il a servi.** Dans le run 7, la carte « avant » a mené à :
   - l’inventaire du sujet, puis l’idée de la coupe ;
   - la séquence, puis une trame rompue ;
   - les relations de couleur, puis un fond accordé et une figure contrastée.

   Le registre, lu avant la direction, a fait écarter le fond crème. Ce sont les routes que les 7 runs précédents ne lisaient presque jamais (`SEQUENCE` 2 fois sur 7, `FRAME/COMPOSITION` 1 fois).
3. **Le savoir qui attend le bon moment n’est pas encore pris.** La carte « regard » n’a pas été ouverte malgré trois tours de correction. Les gestes ont été servis une fois, puis retirés par l’agent (`--sans-gestes`). La recette de caractère n’a pas été lancée. L’écart entre savoir et faire se déplace : il ne porte plus sur l’entrée du run, mais sur la boucle de correction.
4. **Le run a montré les limites des outils, pas celles du savoir.** Quatre défauts d’outils sont apparus et ont été corrigés le jour même : objet de preuve mesuré pendant un défilement doux, volets fermés comptés comme chevauchement, police de corps mal relevée par le registre, outils du regard absents du journal. Le défaut dominant restant, le dessin du chevalet, n’est vu par aucune recette, conformément à AUV-Bench.
5. **Aucun gain n’est encore prouvé.** Une seule production a été faite, sans condition de comparaison. L’évaluation à l’aveugle reste vide : 0 ligne remplie sur 56. Aucun des cinq tests de protocole proposés le 21 n’a été fait.

## Ce qui a changé depuis la version 1

| Constat (version 1) | Verdict le 21 | Ce que dit le système aujourd’hui | Ce que montre le run 7 | Verdict |
|---|---|---|---|---|
| Les modèles varient peu d’un brief à l’autre ; rien ne mesure la variation entre runs ([P] Rusia et al.) | Partiel | Registre des choix : polices réellement rendues, fond, accent, comparés aux runs précédents (`CFT-05`, `SAVOIR/TOOLS/CONVERGENCE`) | Lu avant la direction ; l’agent cite crème ×6 et orange ×4 et s’en écarte ; aucun choix partagé avec les 8 productions | Partiel → **aligné pour la visibilité**, non mesuré sur la diversité |
| Familles par défaut : noir à accent acide, journal à filets fins ([D] Anthropic) | Partiel | Nommées comme signaux à confirmer, datés (`[VEILLE 2026-10]`) | Citées par l’agent ; aucune reprise | **Aligné** |
| Le vocabulaire du système attirerait vers Atkinson ([D] Anthropic, critère aspirationnel) | Partiel | Observation consignée comme hypothèse ; registre et spécimen la rendent visible | Spécimen de trois voix ; Barlow Semi Condensed et Spectral, sans Atkinson | **Partiel** : hypothèse visible, non testée |
| Le numérique est séquentiel ; `SEQUENCE` lu 2 fois sur 7 ([S] Rugiet) | Aligné, peu lu | `BIBLIOTHEQUE/SEQUENCE` dans la carte « avant » | Lue ; trame en six temps, avec retour de l’action en fin de page | **Aligné et mobilisé** (1 run) |
| Fond accordé, figure contrastée ([R] Schloss et Palmer) | Partiel | « Fond accordé, figure contrastée » dans `CFT-05`, avec sources | Lue (carte « avant ») ; fond gris froid, encre bleue, vernis réservé à l’instrument | **Aligné et mobilisé** |
| Les gabarits du cercle chromatique ne prédisent pas l’harmonie ([R] O’Donovan, Tan) | Aligné sans sources | Sources citées | — | **Aligné** |
| Les tests automatiques ne savent pas évaluer la transparence ([S] Mauro) | Absent | `check_render.py` met en réserve une surface translucide sur flou d’arrière-plan | Non sollicité (aucun verre) | **Aligné** |
| Constance de forme puis liberté d’usage ; élément signature et ses états ([S] Romaniuk, Adobe) | Absent / Partiel | « Identité dans la durée » (`SAVOIR/SYSTEM`, `PILOT`) | Non sollicité (mode `DIRECTION`, une page) | **Aligné, non éprouvé** |
| Le diagnostic fin plafonne ; la révision humaine améliore ([P] AUV-Bench, Revision Matters) | En tension | « Regard humain sur la dernière finition » (`DIRECTION/DOUBLE-LOOP`, `PILOT`) ; planche | L’agent s’arrête et demande une correction nommée dans sa réponse ; il nomme un défaut qu’aucune recette ne voit | **Aligné** |
| Un designer qui corrige est plus fiable qu’un designer qui classe ([R] Wu et al., Apple) | Partiel | Planche : champ « ce que je changerais d’abord » | Planche du run 7 prête, pas encore remplie | **Aligné côté outil** ; protocole d’évaluation inchangé |
| Écart entre savoir et faire : l’outil nécessaire n’est pas appelé ([P] Fan et al. ; [D] Anthropic) | (discussion) | Cartes de moment (`--moment`), gestes servis sous les signaux des recettes, fiche qui signale une carte sautée | « Avant » et « sortie » lues ; « regard » sautée ; gestes retirés après le premier passage | **Partiel** : l’entrée du run est corrigée, la boucle ne l’est pas |

## Ce qui reste ouvert

| Constat | Verdict | Pourquoi c’est encore ouvert |
|---|---|---|
| Unicité d’un élément mesurée sur un test sans marque ; les professionnels la jugent mal ([R] Romaniuk ; [R] Brus et al.) | Absent | Aucun test externe de reconnaissance ; le test d’association proposé le 21 n’est pas fait |
| La complexité du haut de page pèse 32 % de la beauté perçue, la page entière 3 % ([R] Miniukovich et Figl) | Partiel | La recette de caractère mesure le premier écran et n’a pas été lancée au run 7. Lancée après coup face au caractère attendu, elle signale une page compressée à 390 px, là où la respiration était attendue |
| Matériaux à rôle défini : solide, verre dépoli, voile ([D] Fluent 2) | Partiel | Pas de typologie des matériaux par rôle |
| Un procédé de fabrication engendre une famille visuelle ([S] Pentagram, BFI LFF) | Partiel | Pas de notion de procédé générateur. Le run 7 en esquisse un : la coupe est générée par un script, réutilisée dans le diagnostic |
| Le mouvement se juge au ralenti, répété, interrompu ([S] Kowalski) | Partiel | « Répété puis interrompu » est écrit ; l’observation au ralenti ne l’est pas |
| Connaissance de cas concrets plutôt que de règles ([R] KATE) | Partiel | Les gestes ont une condition et une réinspection, mais aucun exemple avant/après réel |
| Carte des moyens, collections ouvertes ([S] notes du 20-10) | Non éprouvé | `SAVOIR/SOURCE` lu 0 fois sur 8 runs ; au run 7, sans photo, l’agent a dessiné et laissé un emplacement marqué sans chercher de collection ouverte |
| La critique automatique perd son utilité quand la page s’améliore ([R] CHI 2024) | Partiel | Les deux derniers passages de la recette ne relèvent plus rien de bloquant ; c’est le moment où la planche sert, mais rien ne le signale à l’agent |

## Ce que le run 7 ajoute à la confrontation

Les remarques de l’agent rejoignent des constats de recherche. Elles sont à prendre comme des indices d’une seule production, pas comme des résultats.

| Remarque de l’agent | Constat qui l’éclaire | Lecture |
|---|---|---|
| « Les marqueurs de convergence couvrent presque tout ; on justifie chaque choix contre une liste » | [D] Anthropic : une liste de clichés déplace le choix vers un autre choix fixe | Risque réel : la liste peut devenir la contrainte. Le registre, qui compare à des runs réels, est plus situé qu’une liste générale |
| « Beaucoup de lecture avant le premier pixel » | [D] Anthropic, ingénierie du contexte : la plus petite base utile, le reste au moment où il sert | Mesuré par le journal : 74 000 caractères de routes lues, en plus du noyau de 30 440 octets, dont 35 000 pour le tronc. La carte « avant » (13 500) est celle dont les conséquences sont les plus visibles |
| « La trace légère ne tient pas en six lignes avec la déclaration de l’absolu 4 » | — (cohérence interne) | Deux règles se recouvrent ; à trancher dans le système |
| « Rien pour une hypothèse structurante sans réponse possible » (quatuor ou guitare) | [S] pratique : hypothèse nommée, alternative montrée | L’agent a nommé l’hypothèse et dit ce qu’elle change ; le système ne dit pas quand montrer l’autre branche |
| « Rien pour juger la justesse métier d’un schéma » | [P] AUV-Bench ; [R] Wu et al. | Limite attendue : seul un regard humain ou métier la voit, d’où la planche |

## Propositions

### Dans le système

| N° | Ajustement | Constat qui le motive | Mesure de réussite |
|---|---|---|---|
| T1 | Quand une recette ouvre une correction (RETURN ou SIGNAL), sa sortie rappelle en une ligne `--moment regard`, au lieu d’attendre que l’agent y pense | Carte « regard » sautée malgré trois tours ; Fan et al. | Carte « regard » consultée dans les fiches des runs suivants |
| T2 | Rendre les gestes servis plus courts, un seul par signal, au lieu de trois au maximum, pour qu’ils ne soient pas retirés | `--sans-gestes` employé dès le deuxième passage | Gestes servis sans retrait ; gestes suivis d’une modification |
| T3 | Après deux passages de la recette sans RETURN ni SIGNAL nouveau, la sortie propose la planche | CHI 2024 ; AUV-Bench ; défaut restant invisible aux recettes | Planche ou demande de correction nommée au bon moment |
| T4 | Ajouter aux gestes des cas avant/après réels, tirés des runs (par exemple le titre recoupé selon le sens au run 7) | KATE | Gestes appliqués et réobservés |
| T5 | Trace légère : compter la déclaration de l’absolu 4 à part des six lignes, ou la fondre explicitement dans la ligne `MODE` | Remarque de l’agent ; lignes très longues | Traces plus courtes, sans perte de champ |
| T6 | Relire les marqueurs de convergence : les garder datés, mais servir d’abord le registre réel avant la liste générale | Anthropic ; remarque de l’agent | Choix justifiés par le produit plutôt que contre la liste |
| T7 | Faire lancer la recette de caractère quand la direction est ouverte, avec une déclaration du run | Recette non lancée ; signal de densité trouvé après coup | Caractère déclaré et confronté dans chaque run `DIRECTION` |

### Dans le protocole

1. **Remplir l’évaluation à l’aveugle** existante (56 lignes), en ajoutant la colonne « ce que je changerais d’abord ».
2. **Rejouer les briefs 1, 4 et 5 en condition C**, deux productions chacun, journal actif. C’est le seul moyen de dire si la révision améliore quelque chose.
3. **Faire le test d’association** sur les captures floutées, condition par condition (Romaniuk).
4. **Remplir la planche du run 7**, pour savoir si une correction humaine nommée change l’artefact au tour suivant.

## Limites

- Le run 7 est une seule production, sans condition de comparaison ; il décrit ce run, pas une tendance.
- L’agent du run 7 a le même modèle que celui qui a écrit les cartes de moment ; un autre modèle pourrait les lire autrement.
- Les sources marquées « agent » dans la version 1 n’ont pas été rouvertes pour cette version.
- Ce document compare des textes, des journaux et une production. Il ne juge pas la qualité visuelle des rendus : c’est le rôle de l’évaluation à l’aveugle et de la planche.

## Sources ajoutées

- Fan et al., arXiv 2605.14038, 2026 — https://arxiv.org/html/2605.14038
- Anthropic, *Effective context engineering for AI agents* — https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- KATE, Findings of ACL 2026 — https://aclanthology.org/2026.findings-acl.710.pdf

Les autres sources sont celles de la version 1.
