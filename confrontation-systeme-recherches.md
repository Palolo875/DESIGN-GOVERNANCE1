# Confrontation — Design Governance face aux recherches

Version 1 · 21-10-2026. Document de travail, hors paquet. Il sert les étapes 5 à 7 du plan de suivi (`plan-de-suivi-outil-esthetique.md`).

## But

Confronter ce que dit le système (révision de `main` au commit `c77a8bc`) à ce que disent les recherches récentes sur la qualité visuelle des interfaces, pour savoir **ce que le système sait**, **ce qu’il fait réellement pendant un run**, et **ce qui lui manque pour conduire à une interface d’une haute qualité visuelle, avec une vraie direction artistique**.

Cinq dimensions sont examinées : composition et harmonie ; surface et matière ; identité et direction artistique ; craft et finition ; moyens de production. Deux sujets transverses s’y ajoutent : l’uniformisation produite par les modèles, et la capacité d’un agent à juger puis corriger son propre rendu.

## Corpus confronté

| Corpus | Contenu | Statut de vérification |
|---|---|---|
| Recherche 1 (Exa, agent, 21-10-2026) | Uniformisation du design produit par IA : mesures, causes, remèdes, tests du générique | Sources principales ouvertes et lues : Design Creativity Bench, Interrogating Design Homogenization, documentation d’Anthropic |
| Recherche 2 (Exa, agent, 21-10-2026) | Qualité perçue, direction artistique, composition, craft, écart de l’IA | AUV-Bench, Miniukovich et Figl, Bakaev et Grigera lus ; le reste repris de la synthèse de l’agent |
| Recherche 3 (Exa, agent et recherches ciblées, 21-10-2026) | Harmonie, surface, identité, composition | Schloss et Palmer, O’Donovan, Deng, Min, Tan, Brus et al., Romaniuk, critiques de Liquid Glass, Bentley et al. (CHI 2026), cas Koto, HEX, Rugiet lus |
| Note « Esthétique, direction artistique et polish » (20-10-2026) | Comportement dans la DA, finition dans la base commune, mouvement, ressources sous licence | Sources récentes revérifiées : Levine, Design Week (EXF.STUDIO), licence FFL de Fontshare |
| Note « Composition, harmonie, craft, surfaces et identité » (20-10-2026) | Lupton, Albers, corrections optiques, Fluent 2, Liquid Glass, BFI LFF | Pentagram BFI LFF et Fluent 2 revérifiés |
| État de référence (branche `etat-de-reference`) | 15 productions, 7 journaux de mobilisation | Journaux et polices relevés pour ce document |

**Niveaux de preuve.** Chaque constat porte son niveau : **[R]** recherche évaluée par les pairs ; **[P]** prépublication ; **[D]** documentation d’un éditeur ou d’un système de design ; **[S]** pratique d’un studio ou d’un praticien. Une source marquée « agent » n’a pas été rouverte pour ce document.

**Verdicts.** **Aligné** : le système dit la même chose, avec une règle utilisable. **Partiel** : le système le dit en partie, ou sans geste concret. **Absent** : le système ne le dit pas. **En tension** : le système dit autre chose. **En avance** : le système va plus loin que la source.

## Synthèse

1. **Le savoir est là.** Sur une cinquantaine de constats, le système est aligné ou en avance sur la plupart. Ses formulations sont souvent plus opérables que les sources : gestes avec condition et réinspection, tests de retrait, marquage de vérité, plafond déclaré.
2. **Il n’est pas sur le chemin.** Le tronc `DIRECTION` contient `SAVOIR/TYPE` et `ACTION/GATE-A`, pas la composition, les gestes de craft, la couleur, les sources ni les moyens. Sur 7 runs, `SAVOIR/STATE` est lu 2 fois, `SAVOIR/FRAME/COMPOSITION` 1 fois, `SAVOIR/CRAFT/CFT-03` 0 fois, `SAVOIR/SOURCE` 0 fois, `SAVOIR/TOOLS/MOYENS` 1 fois. Le système exécute bien la couche objectivable (83 appels de la recette de rendu, 0 défaut bloquant contre 2 sans le système) ; il sollicite peu la couche qui fait la qualité visuelle.
3. **Il déplace l’attracteur sans le supprimer.** Sans le système, 3 productions sur 8 restent sur la police système ; avec lui, 7 sur 7 choisissent et embarquent leurs polices. Mais 5 sur 7 prennent Atkinson Hyperlegible Next, qu’aucune route ne cite. C’est le phénomène que décrivent la recherche et Anthropic : une consigne déplace le choix par défaut vers un autre choix par défaut.
4. **Aucun gain esthétique n’est encore prouvé.** La recette de caractère donne les mêmes signaux aux deux conditions ; l’évaluation à l’aveugle n’est pas faite ; les méthodes de direction les plus fines sont en `PILOT` sans gain observé. La recherche ne fournit d’ailleurs aucune preuve contrôlée qu’un remède (friction, références, tokens) augmente la diversité sans nuire à l’usage.
5. **Trois manques réels.** L’harmonie de couleur ne reprend pas les résultats empiriques qui l’appuieraient ; l’identité est pensée pour une page, pas pour un produit dans la durée ; la limite de l’auto-critique sur le dernier niveau de fini n’est pas dite.

## 0. Uniformisation et générique

| Constat de recherche | Niveau et source | Ce que dit le système | Verdict |
|---|---|---|---|
| Les modèles produisent des interfaces conformes au brief mais bien plus répétitives que des designers : écart moyen 0,58 entre deux briefs de même but et de domaines différents, contre 0,90 chez l’humain ; Claude Opus 5.5 13ᵉ sur 15 en originalité | [P] Rusia et al., Design Creativity Bench, 2026 (lu) | Question de convergence, test du concurrent, `REUSE-CHALLENGE`, marqueurs de vague datés ; rien ne mesure la variation **entre** runs | Partiel : le système agit dans un run, pas sur la série |
| Style par défaut reconnaissable : fond crème, serif italique, accent rouille ou terracotta, bandeau défilant, libellés espacés | [S] Chayka, The New Yorker, 06-2026 ; [D] skill frontend-design d’Anthropic (lu) | `SAVOIR/TOOLS/CONVERGENCE`, vague 2 : « fond beige ou crème, brun, serif de caractère ou serif italique, orange rouille, bandeau défilant », observée « 6 rendus sur 6, avec ou sans système » | Aligné, avec observation propre |
| Autres familles par défaut : fond quasi noir à accent acide unique ; mise en page de journal à filets fins ; kit de cartes SaaS identiques ; chrome de gabarit (sur-titre en capitales espacées, points médians, « → » ajouté) | [D] skill frontend-design d’Anthropic (lu) | Vague 1 (cartes SaaS), vague 3 (libellés mono en capitales), signaux de trame ; ni l’accent acide sur noir ni la mise en page à filets fins ne sont nommés | Partiel |
| Une liste de clichés déplace le choix vers un autre choix fixe (« vous convergez encore vers Space Grotesk ») | [D] guide de prompts d’Anthropic, 10-2025 (lu) | Les marqueurs servent à « nommer `MODAL`, jamais pour interdire » | En avance sur la forme ; l’état de référence montre le même déplacement (Atkinson) |
| Un critère d’évaluation aspirationnel (« qualité musée ») fait lui-même converger | [D] Anthropic, Harness design, 03-2026 (agent) | « Vocabulaire à rendre observable » : « premium », « beau », « élégant » ne valent pas décision | Partiel : l’hypothèse que le vocabulaire d’accessibilité du système attire vers Atkinson n’est pas examinée |
| La génération sans friction accélère la convergence ; proposition : une friction productive (interroger les choix avant de produire) | [P] Shin et al., 2026 (lu) | Phrase d’idée, test du concurrent, contre-choix situé, question de convergence, comparaison de deux voix typographiques | En avance : le système est une friction productive ; elle n’est pas encore mesurée, la recherche non plus |
| Cohorte Lovable : 88 % des sites dans six familles ; l’originalité est évoquée dans 3,4 % des jugements | [P] Boussioux et al., 2026 (agent) | — | Sans objet direct ; confirme la nécessité de mesurer la diversité entre runs |
| La convention aide l’usage ; la différence doit se construire sur des bases familières | [S] Figma 2024, Nielsen 2025 (agent) ; [R] Tuch et al., 2012 | « Convergence de genre ≠ slop » ; le test de singularité cite Tuch : le genre doit se reconnaître au premier regard | Aligné |

## 1. Composition et harmonie

| Constat | Niveau et source | Ce que dit le système | Verdict |
|---|---|---|---|
| Hiérarchie, foyer, équilibre, contraste d’échelle, vide qui groupe | [S] NN/g (agent) ; [S] Lupton, 2009 (note) | Grammaire « intention → tension → foyer → masse → rythme → matière et type → contenu → états → résolution → retenue » ; gestes « masse visuelle », « gestion du vide », « silhouette » ; contrôle C3 et C4 | Aligné, plus opérable |
| La densité peut servir le contenu ; le vide n’est pas une qualité en soi | [S] Lupton (note) | Axe `DENSITY`, « Substance : la retenue n’est pas le vide », pas de dominante unique imposée en supervision | Aligné |
| Le numérique est séquentiel : doser les moments forts aux arrivées | [S] Alright Studio pour Rugiet, 2026 (lu) | `BIBLIOTHEQUE/SEQUENCE` : arc, série, « moment de champ », fil | Aligné, mais `SEQUENCE` lu 2 fois sur 7 |
| La première impression se forme en 50 ms ; complexité contenue et prototypicalité la favorisent | [R] Lindgaard 2006, Tuch 2012, Reinecke 2013 (agent ; Tuch cité par le système) | Cité dans le noyau | Aligné |
| La complexité explique 32 % de la beauté perçue en haut de page, 3 % sur la page entière | [R] Miniukovich et Figl, 2025 (lu) | La recette de caractère mesure le premier écran ; le rythme de la page entière n’est pas mesuré | Partiel ; le dossier d’évaluation montre bien des captures complètes |
| Harmonie, préférence et figure sont trois jugements : des teintes proches sont harmonieuses ; les complémentaires ne le sont pas en paire, mais une figure ressort mieux sur un fond contrasté | [R] Schloss et Palmer, 2011 (lu) | « Nommer la relation », « une couleur étendue, une autre rare », test en niveaux de gris ; rien sur la distinction fond accordé / figure contrastée | Partiel |
| Les gabarits du cercle chromatique ne prédisent pas l’harmonie ; certaines palettes canoniques sont jugées moins harmonieuses que des palettes au hasard | [R] O’Donovan et al. (lu) ; [R] Tan et al., 2025, plus de 1 000 participants (lu) ; [R] Min, 2025 (lu) | « Complémentaire, analogue ou triade décrivent une palette ; elles n’en justifient pas une » ; références citées : Ottosson, WCAG, Itten | Aligné sur le fond, sans les sources qui l’appuient |
| Peu de couleurs, une couleur signature contrastée sur un seul élément | [R] Deng et al., 2010 (lu) | « Deux ou trois couleurs tenues valent souvent mieux qu’une palette complète » ; geste « accent » | Aligné |
| La couleur dépend de son voisinage et de sa surface ; juger la palette dans la composition | [S] Albers (note) ; [R] CHI 2024 sur la présentation des palettes (agent) | « Couleur située », palette par rôles, relevé de palette sur capture | Aligné |
| Le nombre d’or n’est pas soutenu pour le web ; échelles modulaires et grilles de 8 px sont des conventions | [R] Tractinsky et al., 2013 (agent) ; [D] Carbon (agent) | « Colonnes, tailles, espacements et breakpoints sont des diagnostics de cohérence », aucune proportion prescrite | Aligné |

## 2. Surface et matière

| Constat | Niveau et source | Ce que dit le système | Verdict |
|---|---|---|---|
| Une matière translucide brouille la séparation entre figure et fond ; Apple a fini par rendre le verre plus opaque et assombrir le fond | [S] NN/g, 10-2025 ; [S] Fast Company, 09-2025 ; AppleVis via 9to5Mac, 03-2026 (lus) | C5 « une seule logique » ; « retire ombres, bordures et flous sans rôle » ; verre et transparence notés comme signal à confirmer | Aligné |
| Les tests automatiques de contraste ne savent pas évaluer les transparences complexes | [S] Mauro, cité par Fast Company (lu) | `check_render.py` met les textes sur image ou fond non uni à part sans ratio ; le flou d’arrière-plan (`backdrop-filter`) n’est pas traité | Absent dans la documentation de la recette |
| Une lumière cohérente, des matériaux à rôle défini (solide, verre dépoli pour les surfaces passagères, voile pour bloquer) | [D] Fluent 2 (lu) ; [D] Apple, Liquid Glass (note) | Geste « surface » (lumière par le haut, liseré, ombre opposée atténuée) ; en sombre, élévation par paliers de luminosité | Aligné ; pas de typologie des matériaux par rôle |
| L’expressivité qui renforce la hiérarchie (taille, couleur, contenant) améliore l’usage : repérage 33 % plus rapide, tâche 20 % plus rapide | [R] Bentley et al., CHI 2026, auteurs de Google (lu) | Masse visuelle, accent par rôle, « une décision créative ne nuit pas à l’usage » | Aligné ; à noter : le blog de Google annonçait « jusqu’à 4 fois », la moyenne publiée est 33 % |
| Chaque texture, ombre ou grain a un rôle ; on le vérifie en l’enlevant | [S] synthèse de praticiens (agent) | Test de retrait (`CFT-01`), « une matière créée par code doit expliquer la relation qu’elle porte », `MODIFIER/PRINT_FIELD` | En avance |
| Des assets moyens tiennent ensemble par un traitement commun | [S] pratique de studio | « Traitement des assets moyens », « lot d’assets » | En avance |

## 3. Identité et direction artistique

| Constat | Niveau et source | Ce que dit le système | Verdict |
|---|---|---|---|
| Un élément d’identité se mesure par sa notoriété et son unicité, sur un test sans marque ; l’unicité compte le plus | [R] Romaniuk, Ehrenberg-Bass (lu) | Test de singularité : « si le logo et le nom disparaissent, qu’est-ce qui reste spécifique ? » | Partiel : la question est posée par l’agent, pas mesurée |
| Les professionnels jugent mal la force des éléments d’identité : ils surestiment la notoriété et sous-estiment l’unicité | [R] Brus et al., Journal of Brand Management, 2025, 405 éléments, 50 marques (lu) | Le jugement de singularité repose sur l’agent et l’évaluateur | Absent : aucun test externe de reconnaissance |
| Constance de forme pendant la construction d’un élément, liberté d’usage une fois l’élément connu | [S] Romaniuk (lu) | — | Absent ; le système raisonne run par run |
| L’identité naît d’un élément du produit qui devient signe (jauge de progression de GoFundMe) | [S] Koto, 2026 (lu) | Objet de preuve codé, « une chose vivante », phrase d’idée tirée de l’inventaire du sujet | En avance sur la méthode ; en `PILOT`, sans gain observé |
| Un procédé de fabrication peut engendrer toute une famille visuelle (lumière projetée à travers des découpes) | [S] Pentagram, BFI LFF 2026 (lu) | « Idée par rapprochement », routes de production ; pas de notion de procédé générateur | Partiel |
| Les codes d’une catégorie produisent la même marque pour tous (« developer-familiar ») | [S] HEX pour Composio, 2026 (lu) | Trame modale, test du concurrent, signaux de convergence structurelle | Aligné |
| Un élément signature a des états et des règles d’usage | [S] Adobe Lens, 2025 (agent) ; GoFundMe (lu) | « Fil » de `SEQUENCE` : un objet change d’état ou de rôle d’une section à l’autre | Partiel : dans une page, pas d’un écran ou d’un support à l’autre |
| L’identité et le numérique se conçoivent ensemble ; le comportement fait partie de la direction | [S] Kit Studio pour EXF.STUDIO, 2026 (lu) | Caractère « traduit par des relations de masse, de rythme… ou de comportement » ; dial « motion » ; geste produit codé | Aligné |

## 4. Craft et finition

| Constat | Niveau et source | Ce que dit le système | Verdict |
|---|---|---|---|
| Alignement optique, correction des formes rondes | [S] Linear, 2024 (agent) ; [S] Paget, 2016 (note) | Geste « alignement optique » à 1 px ; « une lettre ronde ou oblique en début de ligne peut demander un léger retrait optique » | Aligné |
| Survol sans changement de graisse ; chiffres tabulaires ; typographie fluide | [S] Rauno Freiberg (agent) | Geste « chiffres » (`tabular-nums`), réglage des grands corps, micro-typographie française | Aligné |
| Le mouvement se juge à sa fréquence ; court pour une action répétée ; au ralenti, répété, interrompu | [S] Kowalski (note) ; [S] Rauno (agent) | `SAVOIR/CONTEXT` : « plus un mouvement revient souvent, plus il est court » ; jouer l’interaction « répétée puis interrompue » | Aligné ; l’observation au ralenti n’est pas nommée |
| Les états réels font partie du fini | [D] Google, revue de design (agent) | `SAVOIR/STATE`, récupération après erreur, preuve d’état (`--assert`, `--in-frame`) | En avance |
| La finition se règle dans la base commune ; un défaut qui revient se corrige à la source | [S] Levine, 10-2026 (lu) | `SAVOIR/SYSTEM` (tokens primitifs et sémantiques) ; « cohérence systémique avant créativité locale » | Aligné |
| La soustraction est plus difficile que l’ajout ; l’IA ajoute | [S] « Craft is time on stone », frankstall.one, 2026 (lu) | Atelier d’édition : « retrait, réduction ou transformation ; n’ajoute rien pour compenser » | En avance |
| Une amélioration locale demande de réexaminer le tout | Note du 20-10 | « Réobserve la page entière, pas seulement la zone corrigée » | Aligné |

## 5. Moyens de production

| Constat | Niveau et source | Ce que dit le système | Verdict |
|---|---|---|---|
| Ressources libres choisies par rôle, licence vérifiée : Velvetyne, Fontshare (FFL 2.0 du 17-08-2026 ou OFL), Poly Haven, ambientCG | Note du 20-10 (licences revérifiées) | `SAVOIR/TOOLS/MOYENS` nomme exactement ces ressources, avec leurs restrictions, et bien d’autres par couche | Aligné ; la carte du système est plus large |
| Commencer par une référence visuelle plutôt qu’un texte | [S] Austin Knight (lu) | Ancre de direction, de production, de vérification ; fiche de source ; une référence dit la décision qu’elle peut changer | En avance |
| La valeur d’une ressource dépend de son intégration, pas de son existence | Notes du 20-10 | « Nommée ou seulement atteignable, elle reste une intention » ; plafond déclaré | En avance |
| — | — | La carte n’a été mise à l’épreuve par aucun run : brief 5 (sans photo) non produit, `SAVOIR/SOURCE` lu 0 fois | Non éprouvé |

## 6. Juger puis corriger son propre rendu

| Constat | Niveau et source | Ce que dit le système | Verdict |
|---|---|---|---|
| Les modèles jugent l’ensemble de façon moyenne, mais le diagnostic exact plafonne à 24,7 % et un bon diagnostic ne garantit pas une bonne réparation | [P] AUV-Bench, 2026 (lu) | Un défaut dominant par tour, geste nommé, avant/après comparé, original gardé s’il résout mieux | Aligné sur la discipline qui limite cet écart |
| L’auto-correction sur capture apporte peu ou rien ; la révision par le modèle seul peut dégrader ; la révision humaine améliore | [P] Design2Code, Revision Matters (agent) | « Ne renvoie pas la résolution au seul savoir-faire de l’agent ou à une future revue humaine » (`SAVOIR/STATE`) | En tension : la règle empêche de se défausser, ce qui est juste, mais ne dit pas où l’auto-critique cesse d’être fiable |
| La critique automatique devient moins utile à mesure que la page s’améliore | [R] CHI 2024 (agent) | Arrêt quand « aucune amélioration utile ne promet un gain réel » ; contrepoint externe recommandé si l’enjeu est identitaire | Partiel |
| Les juges automatiques de beauté restent moyens : UIClip 75 % ; GPT-4o en faible accord avec 39 experts | [R] Wu et al., 2024 (agent) ; [R] Bakaev et Grigera, ICSE 2026 (lu) | « Sans score esthétique » ; la recette de caractère rend des signaux, jamais un `PASS` | En avance |
| Un designer qui corrige la page est plus fiable qu’un designer qui classe : accord de 76 % contre 49 % | [R] Wu et al., Apple, CHI 2026 (agent) | Évaluation à l’aveugle par choix et raison en une phrase | Partiel, côté protocole |
| L’attrait influence l’utilisabilité perçue, pas l’utilisabilité réelle | [R] Tractinsky et al., 2000 (agent) | « Une appréciation perceptuelle ne devient une preuve d’utilisabilité que reliée à une tâche » | En avance |

## Ce que l’état de référence montre

**Mobilisation sur 7 runs avec le système** (journaux `DG_JOURNAL`, lectures comptées par route) :

| Route | Lectures | Dans le tronc `DIRECTION` |
|---|---|---|
| `SAVOIR/TYPE` | 11 | oui |
| `BIBLIOTHEQUE/SELECT` | 6 | non |
| `SAVOIR/CRAFT/CFT-05` (couleur) | 4 | non |
| `SAVOIR/TOOLS/CONVERGENCE` | 3 | non |
| `SAVOIR/STATE` (gestes de craft) | 2 | non |
| `BIBLIOTHEQUE/SEQUENCE` | 2 | non |
| `SAVOIR/FRAME/COMPOSITION`, `SINGULARITE`, `CFT-00`, `CFT-06`, `TOOLS/MOYENS`, `BIBLIOTHEQUE/TENSION`, `ACTION/RECETTE-CARACTERE` | 1 chacune | non |
| `SAVOIR/CRAFT/CFT-03`, `SAVOIR/SOURCE`, `SAVOIR/STYLE`, `SAVOIR/CONTEXT` | 0 | non |

Appels d’outils : `read_route.py` 91, `check_render.py` 83, `check_caractere.py` 1.

**Polices** (relevé grossier : polices embarquées et deux premières déclarations `font-family` de chaque page) :

| Condition | Polices |
|---|---|
| Sans le système (8) | police système ×3, mono ×1, Source Serif 4, Fraunces, Newsreader, variables `--sans` / `--serif` |
| Avec le système (7) | Atkinson Hyperlegible Next ×5 (dont 2 avec Source Serif 4, 1 avec Big Shoulders Stencil), Newsreader avec Schibsted Grotesk, Bricolage Grotesque |

Le système fait passer de la police par défaut à une police choisie et embarquée (critère C2), mais concentre ce choix. Hypothèse à tester, non établie : le vocabulaire d’accessibilité et de lisibilité du système, ajouté à l’obligation d’embarquer les polices, attire vers une police réputée « accessible », comme « qualité musée » attirait vers une esthétique chez Anthropic.

## Propositions

### Sans toucher au système (protocole, dès maintenant)

1. **Évaluation à l’aveugle enrichie.** Ajouter à `evaluation.csv` une colonne « ce que je changerais d’abord » : une correction nommée est un jugement plus fiable qu’un simple choix (Wu et al., 2026).
2. **Test d’association.** Mélanger les captures des 15 productions, texte flouté, et demander à l’évaluateur de rattacher chacune à son brief. Une page rattachée sans hésiter a de l’unicité (Romaniuk). Compter par condition.
3. **Briefs jumeaux.** Pour l’étape 5, deux briefs de même but et de domaine différent (par exemple la fromagerie et une brûlerie sur les mêmes marchés). Mesurer combien la page change quand le sujet change (Rusia et al., 2026).
4. **Inventaire des clichés.** Coder, sur les 15 productions, la présence des familles par défaut d’Anthropic et des vagues du système. Défaut objectivable, sans aveugle.
5. **Produire le brief 5.** Seul moyen d’éprouver la carte des moyens, les collections ouvertes et la surface sans photo.

### Dans le système (étape 7, après l’évaluation)

| N° | Ajustement | Constat qui le motive | Mesure de réussite sur l’état de référence |
|---|---|---|---|
| S1 | Rendre les gestes perceptifs de `SAVOIR/STATE` obligatoires après la première capture en `DIRECTION`, ou en placer une forme compacte dans le tronc (budget de 35 000 caractères à vérifier) | Mobilisation : 2 lectures sur 7 | Lectures de `SAVOIR/STATE` dans le journal ; réserves de Gate C en baisse |
| S2 | Compléter `CFT-05` : fond accordé, figure contrastée ; sources Schloss et Palmer, O’Donovan, Tan | Absence des résultats empiriques qui appuient la règle déjà écrite | Relevé de palette et contraste par rôle |
| S3 | Documenter la limite de `check_render.py` sur les fonds translucides et le flou d’arrière-plan ; les signaler comme non mesurés | Leçon de Liquid Glass ; limite des tests automatiques | La recette les liste au lieu de les ignorer |
| S4 | Ajouter une notion d’identité dans la durée pour le mode `SYSTÈME` : élément signature avec ses états, constance de forme puis liberté d’usage | Romaniuk ; cas Koto, Adobe | À éprouver sur un run `SYSTÈME`, pas sur l’état de référence actuel |
| S5 | Dire où l’auto-critique cesse d’être fiable : sur le dernier niveau de fini et en enjeu identitaire, proposer une correction humaine nommée plutôt qu’un tour de plus | AUV-Bench, Revision Matters, CHI 2024 | Comparer les réserves restantes avec et sans ce tour humain |
| S6 | Tester l’hypothèse de l’attracteur typographique : comparer deux voix sans le vocabulaire d’accessibilité dans la consigne de comparaison | Atkinson ×5 sur 7 | Diversité des polices de titre entre runs |
| S7 | Nommer deux familles par défaut manquantes dans les marqueurs : fond quasi noir à accent acide unique ; mise en page de journal à filets fins | Skill frontend-design d’Anthropic | Signaux de convergence relevés dans les traces |

## Limites de cette confrontation

- Une partie des sources vient de la synthèse de l’agent Exa sans avoir été rouverte ; elles sont marquées « agent ».
- Plusieurs études clés sont des prépublications de 2026, non reproduites ; Design Creativity Bench est publié par un éditeur commercial.
- Le relevé des polices ne lit que les deux premières déclarations `font-family` et les fichiers embarqués.
- Les comptes de lecture viennent de 7 runs sur 4 briefs ; ils décrivent ces runs, pas une tendance.
- Ce document compare des textes à des textes et des journaux. Il ne juge pas les rendus : c’est le rôle de l’évaluation à l’aveugle.

## Sources principales

- Rusia et al., *Design Creativity Bench*, arXiv 2610.11539, 2026 — https://arxiv.org/html/2610.11539v1
- Shin et al., *Interrogating Design Homogenization in Web Vibe Coding*, arXiv 2603.13036, 2026 — https://arxiv.org/html/2603.13036
- Deng et al., *AUV-Bench*, arXiv 2609.34854, 2026 — https://arxiv.org/html/2609.34854v1
- Miniukovich et Figl, *Measuring Webpage Visual Aesthetics with Screenshots*, 2025 — https://doi.org/10.1007/978-3-032-04999-5_18
- Bakaev et Grigera, *Rate My Web Design?*, ICSE 2026 — https://dl.acm.org/doi/full/10.1145/3774748.3795676
- Schloss et Palmer, *Aesthetic response to color combinations*, 2011 — https://doi.org/10.3758/s13414-010-0027-0
- O’Donovan et al., *Color Compatibility From Large Datasets* — https://www.dgp.toronto.edu/~donovan/color/colorcomp.pdf
- Tan, Echevarria et Gingold, *Palette-Based Color Harmonization*, IEEE TVCG, 2025 — https://doi.org/10.1109/tvcg.2025.3546210
- Deng, Hui et Hutchinson, *Consumer preferences for color combinations*, 2010 — https://doi.org/10.1016/j.jcps.2010.07.005
- Min, *Verification of Munsell’s Color Harmony Theory*, 2025 — https://doi.org/10.17289/jkscs.39.1.2025.02.15
- Bentley et al., *Usability Hasn’t Peaked*, CHI 2026 — https://dl.acm.org/doi/10.1145/3772318.3790373
- Brus et al., *Assessing branding strength*, Journal of Brand Management, 2025 — https://link.springer.com/article/10.1057/s41262-025-00395-y
- Romaniuk, *Brands of Distinction* — https://marketingscience.info/news-and-insights/brands-of-distinction
- NN/g, *Liquid Glass Is Cracked*, 2025 — https://www.nngroup.com/articles/liquid-glass/
- Fast Company, *The liquid works, but the glass is broken*, 2025 — https://www.fastcompany.com/91405580/apple-liquid-glass-the-liquid-works-but-the-glass-is-broken
- Anthropic, skill frontend-design — https://github.com/anthropics/skills/blob/HEAD/skills/frontend-design/SKILL.md
- Anthropic, *Prompting for frontend aesthetics*, 2025 — https://platform.claude.com/cookbook/coding-prompting-for-frontend-aesthetics
- Chayka, *The generic style of AI web design*, 2026 — https://kylechayka.substack.com/p/the-generic-style-of-ai-web-design
- Levine, *Paying Down the Palette*, 2026 — https://justinlevine.me/writing/paying-down-the-palette
- Pentagram, *BFI London Film Festival* — https://www.pentagram.com/work/bfi-london-film-festival
- Fluent 2, *Material* — https://fluent2.microsoft.design/material/
- Koto pour GoFundMe (Creative Boom, 2026) — https://www.creativeboom.com/news/koto-evolves-gofundmes-brand-as-platform-expands-beyond-individual-giving/
- HEX pour Composio (The Brand Identity, 2026) — https://the-brandidentity.com/project/hexs-electric-identity-for-composio-represents-how-the-product-works
- Pentagram et Alright Studio pour Rugiet (The Brand Identity, 2026) — https://the-brandidentity.com/project/pentagram-and-alright-studio-rebrand-mens-health-platform-rugiet
- Kit Studio pour EXF.STUDIO (Design Week, 2026) — https://www.designweek.co.uk/how-kit-studio-switched-exell-to-exf-studio-with-ascii-ingenuity/

## Suite donnée

Les propositions S1 à S7 ont été mises en œuvre, à l’essai (`PILOT`), dans la révision `R2026-10-21.2` du paquet (branche `ccr-35204e53-0om9bb`, commit `b7594ef`) :

- S1 : cartes de moment (`read_route.py --moment avant|regard|sortie`) et gestes de `SAVOIR/STATE` servis sous les signaux des recettes (`scripts/gestes.py`) ; la fiche de mobilisation signale une carte sautée ;
- S2 : « Fond accordé, figure contrastée » et sources dans `CFT-05` ;
- S3 : surface translucide sur flou d’arrière-plan non mesurée sur son ancêtre par `check_render.py` (réserve) ;
- S4 : « Identité dans la durée » dans `SAVOIR/SYSTEM` ;
- S5 : « Regard humain sur la dernière finition » dans `DIRECTION/DOUBLE-LOOP`, avec `scripts/planche.py` ;
- S6 : registre des choix (`scripts/registre_choix.py`, polices réellement rendues) et spécimen de voix (`scripts/specimen.py`) ; l’observation Atkinson est consignée dans `SAVOIR/TOOLS/CONVERGENCE` ;
- S7 : familles par défaut ajoutées comme signaux à confirmer dans `SAVOIR/TOOLS/CONVERGENCE`.

Premier relevé du registre sur huit productions : le fichier Atkinson Hyperlegible Next est rendu dans cinq d’entre elles, sous plusieurs noms locaux ; six fonds sur huit sont crème ou beige. Le gain sur la qualité reste à mesurer en rejouant des briefs avec cette révision (condition C du protocole).

