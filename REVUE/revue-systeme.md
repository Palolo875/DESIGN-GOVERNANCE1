# Carnet de revue — Design Governance

Ce carnet est conservé sur la branche documentaire `refonte`. Les [sources de la première revue](https://github.com/Palolo875/DESIGN-GOVERNANCE1/tree/6e5a8c2) et les [sources des compléments CORRECTIFS](https://github.com/Palolo875/DESIGN-GOVERNANCE1/tree/5a5f56357d829150ac5a1863c3c40f35c4c3bafa) identifient les états examinés. Les chemins /workspace désignent les emplacements locaux utilisés pendant la revue.

Début de revue : 11 octobre 2026. Dernière mise à jour : 12 octobre 2026. Dépôt examiné : DESIGN-GOVERNANCE1, base de revue : commit `6e5a8c2`.

Ce carnet conserve les observations de notre lecture progressive. Il ne crée aucune règle et ne remplace aucune source du système. Les recommandations restent à discuter ; aucune correction du paquet n'a été appliquée.

La base des premières revues est le checkout 6e5a8c2. Les compléments « Supports de présentation », « README principal », « Notes de version », « Agent : contenu et installation », « Guides : noms, niveaux et publics », « Maintenance, versions et V1 de référence », « Supports : état courant et actualisation », « README : entrée et état courant », « Release notes : livraison et faits vérifiés » et « Réserves répétées, briefs et runs » examinent une copie distincte et plus récente, R2026-10-11-CORRECTIFS, dans /workspace/presentation-v1-corrigee. Leurs constats et vérifications sont rattachés explicitement à cette copie ; ils ne revalident pas les observations antérieures sur une nouvelle version.

## Méthode et portée

Lire les fichiers, identifier leur fonction et l'utilité de leur contenu, confronter les formulations à leurs sources et exercer les outils lorsque cela permet de vérifier un point. Aucun brief nouveau ni comparaison de rendus n'est imposé pour cette revue.

Statuts du carnet : **vérifié** (fait observé ou défaut reproduit), **à préciser** (ambiguïté documentaire), **éditorial** (lisibilité), **non évalué** (effet qui demande une autre observation).

## Skill — lecture terminée

Fichier : `agent/skill/SKILL.md`, avec ses quatre références.

La skill sert à orienter l'agent et charger les connaissances pertinentes. Son architecture est utile : 20 blocs communs et 23 blocs différés. Les métadonnées sont lisibles ; le noyau correspond à sa compilation ; ses 30 renvois exacts se résolvent ; les 23 blocs différés sont conservés dans leurs routes ; les cinq lignes de mode sont accessibles. Taille : 18 852 octets UTF-8. Ces contrôles établissent une intégrité documentaire, pas une garantie de bonne application par un agent.

| Partie | Utilité | Appréciation |
|---|---|---|
| Métadonnées et introduction | Déclenchement, autorité et dépendances | Utiles ; le niveau senior est un objectif, pas un résultat mesuré. |
| Rôle et posture | Jugement adapté au produit, hiérarchie, direction et retenue | À conserver. |
| Classer, puis charger | Choisir la route, retrouver les sources et limiter la lecture | Essentiel. |
| Prendre le brief et viser le premier objet | Le noyau porte surtout le traitement des contenus manquants | Contenu utile ; titre à ajuster au contenu chargé. |
| Moyens et vérité | Distinguer faits, exemples, ressources et ancrage | Important. |
| Structure | Poser support, circulation, preuve et action | Bon principe ; détail servi par les routes. |
| Composition | Le noyau porte surtout le choix typographique | Utile ; titre trop large. |
| Couleur et convergence | Palette par rôles et examen des réflexes visuels | Bien cadré, sans esthétique obligatoire. |
| Boucle d'édition | Relier diagnostic, intervention, observation et arrêt | Central et concret. |
| Proposition, sortie et trace | Échange humain, acceptation et reprise | Nécessaire ; portée de certaines formulations à préciser. |
| Lire les détails au moment utile | Activer les connaissances selon la décision | Indispensable au chargement progressif. |

### Points conservés

**SK-01 — Vérifié : lien externe cassé après l'installation par copie.**

- Source : `agent/skill/references/flow.md:24` ; installation documentée dans `README.md:24`.
- Le lien d’installation `exemple: ../../../guides/designer.md` fonctionne dans le paquet.
- Après copie dans `.claude/skills/design-governance-practice`, il pointe vers la destination erronée `exemple: .claude/guides/designer.md` au lieu du guide à la racine du paquet.
- Défaut reproduit dans un dossier temporaire avec une copie de la skill et le guide présent à la racine. Les quatre références internes restent accessibles.
- Piste : rendre le renvoi indépendant de la profondeur d'installation et indiquer explicitement sa résolution depuis la racine du paquet.

**SK-02 — À préciser : portée des consignes communes de construction et d'alternative.**

- Sources : `agent/skill/SKILL.md:82` et `:88`, `V1/sections/ACTION.md:91`, `agent/repondre.md:26`, `agent/chemins.md:256`, `design/direction/standard.md:57`.
- « Construis la première scène » provient du pipeline DIRECTION, mais son bloc est chargé pour tous les modes.
- La réponse commune demande « l'alternative écartée », alors que RUN-LITE et le standard la rendent conditionnelle à un choix pouvant modifier la décision.
- Risque d'interprétation : imposer une fabrication ou un contre-choix à un correctif local ou à une demande de jugement seul.
- Piste : préciser le mode et la nature de la demande ; présenter une alternative seulement lorsqu'elle est utile.

**SK-03 — À préciser : frontière entre proposition enregistrée ou montrée et run persistant ou partagé.**

- Sources : `agent/skill/SKILL.md:41` et `:95`, `agent/repondre.md:38`, `design/direction/standard.md:34`.
- La trace légère peut être écrite à côté d'un artefact ; la proposition exploratoire peut être montrée ou partagée.
- « Persistant » et « partagé » déclenchent aussi une trace complète, sans distinction opérationnelle assez explicite entre ces situations.
- Piste : distinguer l'enregistrement ou la présentation d'une proposition d'une transmission pour reprise, d'une adoption ou d'une acceptation.

**SK-04 — Éditorial : deux titres ne correspondent plus au contenu commun.**

- Sources : `agent/skill/SKILL.md:35` et `:55`, registre `scripts/build_core.py`.
- « Prendre le brief et viser le premier objet » contient surtout la règle des contenus d'exemple ; « Composition » contient surtout une instruction typographique.
- Le détail n'est pas perdu : il est différé et activé par les routes.
- Piste : ajuster les intitulés dans le registre du compilateur, ou expliciter le détail différé, puis recompiler.

**ACC-01 — Vérifié : recherche par symptôme parfois peu précise.**

- Source : `scripts/read_route.py`, recherche et classement par mots de la phrase.
- `--trouver 'le titre écrase la photo'` propose SAVOIR/STYLE, SAVOIR/CRAFT et SAVOIR/TOOLS, sans les routes précises SAVOIR/STATE ou SAVOIR/CRAFT/CFT-03.
- `--trouver 'typographie'` place correctement SAVOIR/TYPE en premier.
- Piste : améliorer l'orientation des formulations de symptômes, sans confondre absence dans les résultats et absence du savoir.

### Références de la skill

- `examples.md` : séquences illustratives, distinctes d'une sérialisation JSON ; les exemples ne sont pas des observations réelles ni un style à copier.
- `flow.md` : carte du parcours ; utile, avec le défaut de lien SK-01.
- `machine_projection.md` : transport et validation de trace structurée ; chargement conditionnel pertinent.
- `canonical_minimum.md` : repli honnête quand les sources manquent ; interdit de revendiquer un run conforme sans le paquet.

### Vérifications déjà exécutées sur ce commit

Contrôles documentaires, compilation, structure et carte de lecture réussis. Suites réussies : budget et blocs différés (18 cas), lecteur (84 cas), régressions d'audit (68 cas), préparation (9 cas), projections et contrats selon leurs suites intégrées. Les 51 cas DOM simulés ont réussi séparément.

La validation globale `validate_all.py --lecture-seule` est restée incomplète : le test de serveur local de `test_check_render.py` rencontre `PermissionError` à l'ouverture d'une socket. Cela constitue une limite de l'environnement ; les étapes suivantes du runner et les tests navigateur ne sont pas déclarés réussis. Le build et la reproductibilité des distributions n'ont pas été exécutés dans cette revue.

## Design — lecture terminée

Les 27 fichiers Markdown de `design/` ont été lus. Le dossier porte le contenu de travail : direction à choisir, savoir pour exercer le jugement, formes pour construire et critères pour examiner le produit. La skill en est une entrée et un mécanisme de chargement, pas un remplacement. Les adresses historiques restent des routes vers les sections déplacées, sans constituer une seconde copie normative.

### Utilité des fichiers

| Fichier dans `design/` | Fonction et utilité observées |
|---|---|
| `README.md` | Explique la relation entre création, observation et correction ; donne les quatre entrées. Bon point de départ humain. |
| `design/direction/cadrer.md` | Rend une demande vague exploitable sans questionnaire systématique ; distingue contenu réel, hypothèse et exemple. Le démarrage spécialisé ne remplace pas une correction locale. |
| `design/direction/diriger.md` | Transforme une intention en cible, preuve, geste, composition et route d'asset. Les références ont un effet attendu et des limites ; elles ne deviennent pas des modèles à copier. |
| `design/direction/premier-objet.md` | Définit un objet suffisamment complet pour juger la proposition ; relie huit dimensions positives à des observations. Grounding et réemploi sont conditionnels. |
| `design/direction/boucle.md` | Fait choisir entre correction locale, reprise de direction, reclassification, nouvelle preuve et arrêt. Évite de remplacer l'artefact par une justification. Voir DI-04 pour l'arrêt. |
| `design/direction/standard.md` | Hiérarchise cinq règles transversales ; les protections critiques priment et les variantes ne sont pas un quota. Sépare direction perceptible, conformité et usage réel. |
| `design/savoir/README.md` | Indexe les sujets et les adresses lisibles. Voir DI-02 pour un emplacement devenu inexact. |
| `design/savoir/fondements.md` | Donne les principes d'appropriation, les compromis et le cadrage. Les heuristiques esthétiques sont annoncées comme des jugements, sans statut scientifique. |
| `design/savoir/qualite-creative.md` | Donne des qualités positives et leurs signes observables, puis des leviers de composition, de registre, d'émotion et de couleur. Voir DI-02 pour un renvoi incomplet. |
| `design/savoir/typographie.md` | Relie la voix au vrai texte, aux langues, aux chiffres, à la hiérarchie, au chargement et au fallback. Contenu utile à une décision typographique réelle. |
| `design/savoir/composition.md` | Relie un symptôme perceptuel à une intervention et à la réinspection ; traite aussi états et récupération. C'est une ressource concrète pour corriger, sans imposer tous les gestes. |
| `design/savoir/images-et-sources.md` | Distingue ancre de jugement et ressource de production ; précise rôle, provenance, intégration, série, droits et limites. |
| `design/savoir/styles.md` | Décrit des dimensions et profils facultatifs avec leurs contre-indications. Un style ne suffit pas comme direction et aucun profil n'est requis par défaut. |
| `design/savoir/systeme-de-design.md` | Traite tokens, composants, consommateurs et maintenance ; préserve la stack existante et distingue calibration locale et règle partagée. |
| `design/savoir/contexte.md` | Replace accessibilité, densité, responsive, performance et mouvement dans le contexte réel. Les effets ne prennent pas le pas sur les protections critiques. |
| `design/savoir/techniques.md` | Relie fabrication et preuve aux moyens du médium ; rappelle qu'une observation HTML ne valide pas les autres supports. |
| `design/savoir/gout-et-tendances.md` | Fournit des références et une veille datée, avec sources et limites. La présence d'un outil dans une liste ne prouve ni disponibilité ni licence. La watchlist interne ne mesure pas une fréquence générale. |
| `design/savoir/connexions.md` | Rapproche les domaines selon une décision ouverte, avec conditions, contre-indications et observations attendues. L'index ne classe pas automatiquement le run et n'ajoute aucun quota. |
| `design/formes/README.md` | Oriente vers la sélection et le catalogue ; rappelle que les structures sont des responsabilités plutôt que des rendus prêts à l'emploi. |
| `design/formes/choisir.md` | Traduit intention → niveau structurel → levier → effet observable ; autorise zéro sélection quand l'héritage suffit. Prévoit la dérivation locale avant toute promotion. |
| `design/formes/catalogue.md` | Distingue support, grille, scène, séquence, objet, micro-interface, modificateur et couche. Fournit usages, contre-indications et limites de preuve, sans code de composants. Voir DI-05 pour le mobile. |
| `design/produit/README.md` | Présente le parcours de premier rendu à preuve et finition. |
| `design/produit/premier-rendu.md` | Adapte la qualité initiale au mode et relie tâche, contenu, états, accessibilité, robustesse et scope observé. Voir DI-03 pour l'état qui accueille. |
| `design/produit/plancher.md` | Porte les contrôles objectivables applicables, méthodes et provenance. Les limites de `check_render.py` sont explicites : un résultat de script n'est pas une validation générale. |
| `design/produit/finition.md` | Donne des critères de craft sur capture et une mise à l'épreuve d'une décision. Une conservation de l'original peut être valide. Voir DI-01 et DI-04. |
| `design/produit/preuve-visuelle.md` | Précise les captures et scopes pertinents ; une capture ne démontre pas seule le fonctionnement ni la réussite d'une tâche. |
| `design/produit/interface.md` | Relie les outils de construction aux capacités de vérification ; un moyen technique ne devient pas une direction. |

### Appréciation d'ensemble

Les quatre parties remplissent des responsabilités distinctes. Les reprises de notions comme « premier objet », « preuve » et « boucle » ont généralement une fonction différente : objectif de création, levier de jugement ou responsabilité de vérification. Une suppression au seul motif de répétition ferait perdre ces relations.

Les contenus les plus directement opérationnels sont la cible visuelle, le contrat positif du premier objet, les gestes perceptuels, la traduction de l'intention en construction, les états d'interface et les limites des preuves. Les profils, tendances et exemples servent de pistes conditionnelles ; les fichiers les présentent majoritairement ainsi. Aucun fichier n'a été identifié comme globalement inutile à ce stade.

Le corpus sait préserver une convention adaptée, un composant existant et une décision déjà résolue. Il distingue observation perceptuelle, conformité technique et réussite de tâche. Les points ci-dessous concernent surtout la précision des renvois et la portée de quelques prescriptions.

### Points conservés

**DI-01 — Vérifié, éditorial : renvois de finition vers des rubriques qui ne portent plus le contenu annoncé.**

- Sources : `design/produit/finition.md:20–23`, `agent/skill/SKILL.md:55–57`.
- C4 et C5 demandent « Gestes de finition », titre absent de la skill actuelle. C3 et C6 renvoient à « Composition », dont le contenu commun est désormais seulement typographique.
- Les contenus restent présents : masse, vide et surface dans `SAVOIR/STATE` (`design/savoir/composition.md`), composition dans `SAVOIR/CRAFT/CFT-03`, forme située dans `SAVOIR/CRAFT/CFT-01`.
- Il s'agit d'une orientation imprécise, pas d'une perte de savoir. Le renvoi exact à `SAVOIR/STATE` déjà présent dans le même fichier atténue le problème.
- Piste : utiliser les locators propriétaires ou des liens précis plutôt que d'anciens intitulés du noyau. Ce point prolonge SK-04.

**DI-02 — Vérifié, éditorial : deux indications d'emplacement ne correspondent plus aux fichiers séparés.**

- `design/savoir/README.md:19` dit que la façon de lire le savoir est dans `V1/sections/SAVOIR.md`. La route `SAVOIR/READ` se résout effectivement dans `agent/chemins.md:338`. Les règles d'or, le routage et l'intégrité restent dans le fichier SAVOIR.
- `design/savoir/qualite-creative.md:39` renvoie à « Premium perçu » « ci-dessus ». Sa définition est dans `design/savoir/fondements.md:22`, hors de ce fichier.
- Piste : donner les destinations actuelles et des renvois explicites. Le lecteur de routes continue à fonctionner.

**DI-03 — À préciser : l'ouverture obligatoirement remplie dépasse le seul rendu de démonstration.**

- Source : `design/produit/premier-rendu.md:22`, `ACTION/UI-UX-REALITY`.
- La phrase « L'état qui ouvre la page est rempli […] l'état vide […] n'accueille pas le visiteur » s'applique textuellement à toute surface UI/UX nouvelle ou substantiellement modifiée.
- Un état de démonstration rempli est utile pour examiner la composition. Un nouvel espace de travail sans données peut cependant avoir pour état initial légitime une invitation à créer le premier élément. La phrase ne distingue pas ces destinations.
- Le fichier exige par ailleurs les états pertinents, dont `empty` ; la question porte sur l'accueil par défaut, pas sur l'absence de conception de l'état vide.
- Piste : distinguer la présentation d'un état représentatif de la première utilisation réelle ; préserver le vrai état et marquer clairement tout mode de démonstration.

**DI-04 — À préciser : l'arrêt après observation initiale et le tour d'édition obligatoire en trace légère.**

- Sources : `design/direction/boucle.md:20`, `V1/sections/ACTION.md:35`, `design/produit/finition.md:44–48`, `agent/chemins.md:171`.
- La branche one-shot autorise l'arrêt après l'observation initiale lorsque la qualité et les protections attendues sont couvertes et qu'aucune amélioration utile n'est probable. L'exception B1b est explicitée pour l'acceptation en trace complète ; B1b ne s'applique pas à la proposition en trace légère.
- L'atelier impose néanmoins à toute surface DIRECTION en trace légère au moins un tour comprenant une édition et une nouvelle capture comparée, hors du scope B1b. L'instruction « aucun ajout pour compenser » en fait une mise à l'épreuve, pas nécessairement une correction d'un défaut.
- Les deux exigences peuvent avoir des buts distincts : amélioration et confirmation par comparaison. Leur articulation avec l'arrêt initial n'est pas explicite.
- Piste : dire si le one-shot en trace légère doit toujours inclure cette mise à l'épreuve, ou dans quelles conditions elle peut être omise ; ne pas modifier le scope de B1b par implication.

**DI-05 — À préciser : « une décision par écran » comme règle générale du mobile.**

- Source : `design/formes/catalogue.md:244`.
- La phrase s'adresse à « une interface » et détaille « un champ, un choix ou une action », sans limiter cette stratégie à un parcours guidé.
- La simplification est utile pour une étape ciblée, mais un formulaire court, une comparaison ou un outil dense peuvent nécessiter plusieurs éléments coordonnés sur un écran. `SAVOIR/CONTEXT` reconnaît d'ailleurs la densité utile et l'adaptation au contexte.
- Piste : annoncer cette stratégie comme conditionnelle à la tâche ; préserver la priorité et les relations utiles plutôt qu'imposer un découpage universel.

### Vérification de cette lecture

Un contrôle via le résolveur `scripts/read_route.py` a extrait les références exactes en code inline des 27 fichiers : 97 noms distincts, dont 94 se résolvent. Les trois noms non résolus sont `SCENE/BENTO`, `SCENE/GLASS_HERO` et `SCENE/EDITORIAL_PREMIUM`, explicitement cités dans `formes/choisir.md:205` comme exemples de routes à ne pas créer ; ils ne constituent pas des renvois cassés.

Ce contrôle ne valide pas automatiquement les destinations formulées en prose, d'où DI-01 et DI-02. Il ne couvre pas non plus tous les liens, les droits des ressources externes ni l'efficacité des consignes sur des productions réelles.

Au terme de cette lecture de design, avant l’ajout du carnet au dépôt, aucun fichier du dépôt n’avait été modifié. Les validations déjà réussies sur le même commit restent pertinentes ; la limite du serveur local et l'absence de validation navigateur restent consignées plus haut. Aucun nouveau brief ni rendu n'a été créé pour cette analyse. L'effet sur la qualité des productions, la charge réelle de lecture et la cohérence entre médiums reste **non évalué**.

## Intégration du carnet

Le carnet est ajouté dans `maintenance/revue-systeme.md`, référencé par l’index de maintenance et déclaré dans les deux inventaires de distribution. Il conserve les observations de revue ; les recommandations n’ont pas été appliquées aux sources normatives.

## Gouvernance — lecture terminée

Les sept documents de `gouvernance/`, les quatre schémas, les quatre exemples et les deux validateurs ont été examinés. Les 25 fixtures ont été analysées par leurs écarts aux exemples et exercées par la suite intégrée. Cette revue concerne la cohérence des règles et leur contrôle documentaire ou machine ; elle ne simule pas une acceptation réelle d'un produit.

### Utilité des documents

| Fichier | Fonction et utilité observées |
|---|---|
| `gouvernance/README.md` | Oriente selon exploration, correction, reprise, acceptation et risque. La formalité est proportionnée ; montrer une proposition ne vaut pas acceptation. |
| `gouvernance/principes.md` | Sépare observation, interprétation, décision et persistance. Distingue capacité et autorisation ; ne transforme pas une intention en action effectuée. |
| `gouvernance/statuts.md` | Distingue état du travail, issue, verdict d'axe, fidélité de direction et verdict global. Un run fermé peut conserver un retour ou une limite ; fermeture ne signifie pas réussite. |
| `gouvernance/travail.md` | Pose les préconditions, le contenu de la RUN_CARD, la phase des champs, les capacités et leur base, la reprise et la frontière de validation. La table JSON/trace évite de forcer dans le JSON les décisions qu'il ne transporte pas. |
| `gouvernance/verification.md` | Déclenche les contrats selon la décision ; organise comparaison, preuve en contexte, regard externe, correction, droits, exception et péremption. B1b a un scope précis et une auto-comparaison ne devient pas indépendante. |
| `gouvernance/cloture.md` | Définit le paquet de chaque mode, la fraîcheur de la preuve, la structure des réserves, l'arrêt et le test de sortie. Les mesures expérimentales de la méthode restent distinctes des verdicts individuels. |
| `gouvernance/structure.md` | Encadre contrat local, contrat durable, calibration et sélection. Zéro route est possible ; une valeur ou un identifiant écrit ne constitue pas sa réussite. |

### Utilité des schémas, exemples et outils

- `gouvernance/schemas/run_card.schema.json` et son exemple structurent le transport d'un run. Le validateur ajoute les invariants de mode, de temps, de preuve, de capacité, de réserve, de risque critique, d'ancrage, de B1b et de reprise. Le schéma seul ne contrôle pas tous ces liens métier.
- `gouvernance/schemas/domain_frame.schema.json` relie public, tâche, conventions, risques et contrôles. Le validateur exige notamment une couverture des risques et un raccord au plan de preuve ; il ne vérifie pas la connaissance réelle du domaine.
- `gouvernance/schemas/research_brief.schema.json` rend une recherche structurée inspectable quand cette projection est utile. Source, statut, date, apport à la décision, limite et incertitude restent distincts. Une recherche activée demande des entrées ; sans entrée, une réduction d'incertitude ne peut être revendiquée. Ce contrat n'est pas requis pour toute recherche.
- `gouvernance/schemas/production_contracts.schema.json` regroupe comparaison créative conditionnelle, réalité UI/UX et évaluation d'un pilote. Le validateur impose au moins un contrat, des directions distinctes et la couverture des exigences déclarées. Il ne juge pas la qualité réelle des différences ni les résultats d'évaluation.
- Les exemples montrent une forme et ses limites ; leurs observations illustratives ne deviennent pas des faits. Les fixtures sont des scénarios composites, complétés par des cas unitaires à faute ciblée et motif attendu.
- `gouvernance/outils/validate_run_card.py` contrôle une carte ciblée ou sa suite intégrée. Le profil strict ajoute des contrôles d'adresses et de placeholders, avec les limites GV-01 et GV-02.
- `gouvernance/outils/validate_contracts.py` contrôle un contrat ciblé ou sa suite intégrée. Son contrôle de couverture est utile mais laisse passer le cas contradictoire GV-03.

Les deux outils refusent les clés JSON répétées, les mots-clés de schéma non supportés et les schémas manifestement inopérants. Leurs cas négatifs vérifient les motifs de rejet, pas seulement un code d'erreur. Les schémas et exemples ont donc une fonction concrète ; ils ne sont pas des formulaires à charger systématiquement.

### Appréciation d'ensemble

Le module évite plusieurs confusions importantes : fini versus accepté, capacité versus permission, capture versus réussite de tâche, provenance versus droits, auto-comparaison versus regard indépendant. Les réserves gardent responsable, périmètre, impact, prochaine preuve et condition de sortie. La preuve doit correspondre à la version livrée ; un changement pertinent appelle une réinspection.

La quantité de champs devient utile quand le travail doit être repris, audité ou accepté. La lecture doit rester conditionnelle, comme les textes le prévoient. Aucun document de ce module n'a été identifié comme globalement inutile. L'efficacité de cette proportion dans un vrai travail reste à mesurer.

La frontière machine/humain est largement déclarée : les outils ne prouvent ni la réalité d'une observation, ni les droits, ni l'identité du décideur, ni la qualité visuelle. Les points suivants concernent des contrôles plus restreints ou une cohérence de couverture ; ils ne demandent pas à la machine de juger le design.

### Points conservés

**GV-01 — Vérifié : le profil strict laisse passer certains placeholders comme adresse d'artefact.**

- Sources : `gouvernance/travail.md:188`, `gouvernance/outils/validate_run_card.py:203` et `:593–615`.
- La liste générale de placeholders comprend `?` et `inconnu`, mais la liste utilisée par le parcours strict ne les comprend pas.
- Reproduction : une carte STANDARD synthétique valide et acceptée avec réserve, avec fichiers locaux présents, passe en strict. Remplacer seulement l'adresse d'artefact et son rappel de provenance par `?`, puis par `inconnu`, produit encore un succès CLI strict.
- La concordance des deux chaînes est respectée ; leur capacité à désigner un artefact ne l'est pas. Ce résultat va au-delà de la limite normale « la machine n'atteste pas une observation réelle » : l'adresse est elle-même un placeholder reconnu ailleurs.
- Piste : appliquer une règle commune de remplissage aux locators inspectables, avec des cas négatifs ciblés. Garder les identifiants opaques légitimes et éviter d'interdire toute occurrence du mot « inconnu » dans une limitation.

**GV-02 — Vérifié : chemins locaux avec fragment ou requête mal reconnus en profil strict.**

- Sources : `gouvernance/outils/validate_run_card.py:575–586` et `:636–647` ; contrat strict dans `gouvernance/travail.md:188`.
- Le cas témoin `exemple: absent.html` est correctement rejeté comme fichier absent.
- `exemple: absent.html#hero` et `exemple: absent.html?state=empty` passent sur la même carte, bien que le fichier soit absent. Le nom avec suffixe n'est plus reconnu comme fichier local nu et échappe au contrôle d'existence.
- À l'inverse, `exemple: ./artifact.md#section` est rejeté comme absent alors que le fichier artifact.md existe : le contrôle cherche un nom de fichier contenant littéralement le fragment.
- Piste : distinguer le chemin du fragment et de la requête avant de reconnaître puis résoudre le fichier. Définir la prise en charge des locators locaux adressant un état ou une section. Le contrôle d'existence d'un fichier reste distinct de la validation de son fragment, de son état et de son contenu.

**GV-03 — Vérifié : la couverture UI/UX peut conserver deux statuts contradictoires pour une même exigence au même locator.**

- Sources : `gouvernance/outils/validate_contracts.py:261–289`, contrat de couverture dans `design/produit/premier-rendu.md:38`.
- Reproduction : dans l'exemple de contrats de production, dupliquer la ligne de loading avec le même nom d'exigence et le même locator, mais remplacer `NOT-VERIFIED` par `OBSERVED`, passe le validateur ciblé.
- Le contrôle vérifie que les exigences appartiennent aux matrices et sont présentes, mais les agrège dans des ensembles sans signaler cette contradiction. L'existence d'un observed_scope ne la résout pas.
- Cela ne prouve pas que tout doublon est invalide : deux observations peuvent couvrir des contextes différents. La structure actuelle n'explicite cependant ni version ni scope par ligne qui rendraient ce cas distinguable.
- Piste : donner une règle d'unicité ou de cohérence pour l'état courant d'une exigence, ou porter explicitement les contextes distincts si plusieurs lignes sont nécessaires. Ne pas transformer OBSERVED en PASS : une observation peut rester négative.

### Raccords aux points précédents

- **SK-03 reste à préciser.** L'index gouvernance et ACTION/HANDOFF reprennent le déclencheur « persistant, partagé, audité ». La frontière entre une proposition enregistrée ou montrée et une transmission pour reprise n'y devient pas plus opérationnelle.
- **DI-04 reste à préciser.** `gouvernance/statuts.md:57` rappelle l'arrêt après première observation ; `gouvernance/verification.md:121` renvoie à l'atelier qui vaut aussi en trace légère. Leur lecture ne tranche pas clairement l'articulation déjà relevée.

### Vérifications de cette étape

- 23 références documentaires exactes distinctes dans les sept documents : toutes résolues.
- Validation RUN_CARD : 25 fixtures, 87 cas unitaires, 10 locators admis en strict et témoin de mot-clé non supporté réussis ; contrôle d'autorité du schéma exécuté.
- Validation des contrats : les trois familles d'exemples, 25 cas unitaires, trois cas de cardinalité conditionnelle et le témoin de clé répétée réussis.
- Compilation du noyau vérifiée, carte de lecture et validation structurelle réussies après intégration du carnet.
- Paquet GitHub validé avec 109 fichiers attendus. Copie temporaire assemblée d'après l'inventaire Local validée avec 104 fichiers attendus, carnet présent. Ce contrôle d'intégration ne revendique pas le build ni la reproductibilité des archives.
- Neuf cas synthétiques supplémentaires ont été exécutés par les CLI ciblées : deux bases valides, un témoin de fichier absent correctement rejeté et les six comportements décrits par GV-01 à GV-03. Script, entrées et résultats locaux conservés hors paquet dans `/workspace/work/revue-gouvernance/`.

Les suites intégrées réussissent sur leurs cas déclarés ; les reproductions supplémentaires montrent des limites non couvertes par ces suites. Aucun correctif des règles, schémas ou validateurs n'a été appliqué dans cette étape. L'ajout concerne le carnet, son entrée dans l'index de maintenance et les deux listes du manifeste. La validation navigateur et la validation globale interrompue restent dans l'état déclaré lors de la revue précédente.

## Guides — lecture terminée

Les quatre fichiers de `guides/` ont été lus intégralement : 523 lignes au total. Leur contenu a été comparé aux sections qu'ils indiquent, notamment le classement, le traitement d'un brief vague, la boucle d'amélioration, la revue créative, la trace et la clôture. Cette étape examine l'orientation et la fidélité des résumés ; elle ne mesure pas leur efficacité auprès de lecteurs réels.

### Utilité des fichiers

| Fichier | Fonction et utilité observées | Appréciation |
|---|---|---|
| `guides/commencer.md` | Explique quoi demander, quoi fournir, quoi recevoir et comment poursuivre. Sépare la personne qui demande de l'opérateur chargé des modes. | Bonne entrée courte, sans apprentissage préalable. Les contenus manquants et les exemples sont expliqués ; proposition et validation restent distinctes. |
| `guides/designer.md` | Oriente par sujet, résultat recherché et angle à examiner. Propose des combinaisons conditionnelles et indique quand arrêter la lecture. | Utile pour mobiliser plusieurs savoirs sans tout charger. Les tables ne deviennent ni preuve ni parcours obligatoire. |
| `guides/equipe.md` | Relie cadrage, classement, production, observation, autonomie et conservation. Donne un exemple de travail encore en vérification et les limites des outils. | Utile pour piloter un travail et passer le relais. C'est le guide le plus long ; son parcours commun permet une entrée progressive. Quelques résumés doivent être mieux raccordés à leurs sources. |
| `guides/glossaire.md` | Explique les termes de design, de travail et de vérification, puis donne des exemples. | Utile pour distinguer état, issue, verdict, statut de direction et absence de preuve. Il évite notamment de confondre CLOSED et réussite, ou RUN_CARD et preuve. |

### Appréciation d'ensemble

Les quatre publics ou usages sont suffisamment distincts pour justifier ces fichiers. Aucun guide n'a été identifié comme globalement inutile. Les rappels entre guides servent l'accès par différentes entrées ; leur intérêt dépend de leur fidélité aux sections qui font foi. Les guides du designer et d'équipe annoncent explicitement leur fonction d'orientation.

Le guide du designer apporte aussi une protection contre la lecture excessive : chaque savoir doit avoir un apport nommé, les angles sont déclenchés par une décision ou un risque, et la lecture s'arrête dès que la suite est assez claire. Le guide d'équipe rappelle qu'un moyen indisponible ne justifie pas une baisse silencieuse de protection. Le glossaire conserve les distinctions importantes de gouvernance.

### Points conservés

**GU-01 — À préciser : le résumé de la boucle rend la modification trop systématique.**

- Sources : `guides/equipe.md:92` et `:180`, `guides/commencer.md:30`, `design/direction/boucle.md:8`, `:16` et `:20`.
- Le guide d'équipe dit que, lorsque perception, usage, accessibilité ou robustesse font partie de la décision, la boucle « doit conduire à une vraie modification du rendu, puis à une nouvelle observation ».
- Le même guide autorise ensuite un arrêt si le défaut dominant est absent et qu'aucune nouvelle passe ne promet de changement utile. La source de la boucle prévoit une correction lorsque la décision le requiert, ou une limite lorsqu'aucune correction utile n'est possible ; le guide pour commencer dit aussi de corriger « lorsque c'est nécessaire ».
- Risque d'interprétation : modifier un rendu déjà satisfaisant uniquement pour satisfaire le résumé, ou considérer comme non conforme une confirmation sans changement. Ce point dépasse la seule articulation DIRECTION/B1b déjà relevée dans DI-04.
- Piste : distinguer l'observation nécessaire, la modification justifiée par son résultat et la nouvelle observation après modification. Garder explicites les cas d'arrêt, de prochaine preuve et de réouverture.

**GU-02 — À préciser : la ligne « brief flou » brouille l'ordre de classement.**

- Sources : `guides/equipe.md:130`, `:15` et `:35`, `agent/chemins.md:10`, `:12` et `:23`, `design/direction/cadrer.md:10`.
- La table propose de clarifier ou de partir de `direction/cadrer#demande-vague` « avant le mode ». La section ainsi indiquée place pourtant cette vue après DIRECTION/START, avant la construction d'une surface DIRECTION ; le début du guide demande également de classer d'abord.
- Une clarification ciblée avant de pouvoir classer reste légitime et prévue. Ce qui manque est la distinction entre cette clarification et l'activation de la vue de démarrage pour une direction ouverte déjà classée.
- Risque d'interprétation : traiter le vague comme un mode implicite, ou charger une fabrication de première scène pour une demande qui pourrait finalement relever d'une retouche locale.
- Piste : indiquer la clarification ciblée dans START si le mode ou le risque reste indécidable, puis la vue de demande vague dans le périmètre où elle est utile.

**GU-03 — Éditorial : le renvoi aux six points de revue est indirect.**

- Sources : `guides/equipe.md:263`, `design/direction/boucle.md:42`, `design/savoir/qualite-creative.md:41` et `:44`.
- Le guide demande d'appliquer « les six questions de revue de la boucle d'édition » en indiquant `direction/boucle`.
- Les six points sont effectivement conservés dans la Creative Quality Review de CFT-00 : présence, spécificité, transformation culturelle, caractère générique, résolution manquante et intervention utile. La boucle demande de noter le changement et les régressions, et renvoie elle-même à CFT-00 ; elle ne contient pas cette liste.
- Piste : pointer directement vers `savoir/qualite-creative#ambition` pour la revue à six points, puis vers la boucle pour le changement observé et les régressions. Le contenu n'est pas perdu ; l'accès demande actuellement un détour.

### Raccords aux points précédents

- **SK-03 reste à préciser.** `guides/equipe.md:37` et `guides/glossaire.md:64` reprennent le déclencheur persistant/partagé/audité et la trace légère à côté du rendu, sans préciser davantage la frontière opérationnelle.
- **DI-04 reste à préciser.** La définition de B1b dans `guides/glossaire.md:70` rapproche le contrôle formalisé et l'atelier d'édition. Leur portée respective reste à articuler avec l'arrêt one-shot et l'atelier demandé en DIRECTION légère. GU-01 conserve séparément la formulation plus générale du guide d'équipe.
- **GV-01 et GV-02 concernent aussi l'explication des outils.** `guides/equipe.md:106` annonce le rejet des champs de gabarit et le contrôle d'existence des fichiers. Les limites déjà reproduites nuancent cette annonce. La limite réseau et la distinction entre validation documentaire et preuve d'usage sont, elles, bien déclarées dans ce guide.

### Vérifications de cette étape

- 53 adresses exactes distinctes en code inline dans les quatre guides, représentant 50 sections canoniques et 156 occurrences : toutes résolues par `scripts/read_route.py`.
- Les adresses lisibles désignent les sections attendues. En particulier, `produit/interface` sert UI-UX-REALITY dans `design/produit/premier-rendu.md`, et `savoir/composition#jugement-visuel` sert SAVOIR/STATE ; ce ne sont pas des liens directs vers un fichier portant le même nom.
- Les liens Markdown et leurs fragments, les références opérationnelles et la carte de lecture sont contrôlés par les validateurs existants après l'ajout de cette section.

Aucun guide ni aucune source normative n'a été modifié. Le carnet conserve les observations et leurs pistes ; aucun nouveau brief, rendu ou contrat n'a été créé. La facilité d'apprentissage, le temps de lecture et l'effet réel sur les décisions restent non évalués.

## Maintenance — lecture terminée

Les trois documents de procédure et de version ont été lus intégralement : `maintenance/README.md`, `maintenance/evolution.md` et `maintenance/versions.md`, soit 303 lignes. Le carnet de revue déjà constitué est conservé comme mémoire non normative de cette lecture progressive. Les procédures ont été confrontées à `scripts/preparer_livraison.py`, `scripts/build_distributions.sh`, `scripts/validate_all.py` et aux tests de préparation ; les annonces de version ont été rapprochées du manifeste, du README, des notes de version et des connexions. <!-- références:github -->

### Utilité des fichiers

| Fichier | Fonction et utilité observées | Appréciation |
|---|---|---|
| `maintenance/README.md` | Explique les distributions, les commandes, les dépendances, les limites des contrôles et la reprise après interruption. | Utile comme procédure pratique. La sauvegarde avant reprise, l'identification d'un build actif et le refus de supprimer un verrou selon son âge sont bien explicités. Le choix du journal demande l'ajustement MA-01. |
| `maintenance/evolution.md` | Définit la recette d'un changement, les exigences graduées de contribution, le gain réel, la promotion et la migration des routes. | Utile pour éviter une adoption fondée sur un screenshot ou la fréquence d'usage. Les contrôles automatisables sont séparés du jugement humain ; les statuts de route ne deviennent pas des verdicts de design. |
| `maintenance/versions.md` | Identifie version et révision, décrit les changements, la compatibilité, le budget et les limites de la version. | Utile pour situer le paquet et distinguer réduction de texte, réussite des contrôles et efficacité réelle. Les preuves de CI citées portent sur leurs commits historiques. |
| `maintenance/revue-systeme.md` | Conserve les fonctions des fichiers, les constats, les reproductions et les recommandations encore à discuter. | Complément utile au journal de version. Il ne consigne pas une adoption et ne crée aucune règle ; un constat de revue ne doit pas être lu comme un correctif déjà intégré. |

### Appréciation d'ensemble

Le module est utile et son chargement reste réservé à l'évolution du système. Les exports sont dérivés des sources ; ils ne sont pas modifiés comme des autorités indépendantes. La recette prévoit un run réel pour un changement substantiel avant adoption élargie, tandis qu'une revue documentaire peut conserver ses observations sans inventer un brief ni promouvoir de nouvelles règles.

La promotion d'une route est correctement graduée : contrat local réduit, périmètre de pilote, responsabilités partagées, puis usages contrastés et preuve de gain pour une adoption. SEED signifie canonique par construction, sans gain mesuré ; ADOPTED exige davantage. Compatibilité, consumers, maintenance, migration et retour arrière sont traités selon le risque. Les anciens aliases sont conservés dans une table de migration, explicitement hors des nouveaux usages.

Les vérifications de reprise ciblées confirment les branches documentées : une sauvegarde d'archives laissée en place bloque le build ; dist et sa sauvegarde présents ensemble bloquent aussi ; une sauvegarde dist seule est restaurée. Les deux premiers refus conservent exactement les fichiers et leurs empreintes. Ces observations concernent ces branches précises, pas l'ensemble de la transaction de publication des exports.

### Points conservés

**MA-01 — Vérifié : un journal accepté par l'option peut faire échouer la préparation qui le produit.**

- Sources : `maintenance/README.md:27`, `scripts/preparer_livraison.py:63` à `:75`, `scripts/validate_design_governance.py:126` à `:164`, `scripts/test_preparer_livraison.py:106` à `:121`.
- Depuis la racine d'une copie complète du paquet, l'option `--log audit.log` est acceptée et le journal est créé. La compilation réussit, puis le validateur du paquet rejette ce même fichier comme « fichier inattendu dans le package : audit.log » ; la préparation s'arrête avec le code 1. Le même cas est reproduit avec `--journal audit.log`.
- Chaque copie passe la validation du paquet avant cette commande. Déplacer ensuite uniquement le journal sous `.logs/` permet à cette même validation de réussir de nouveau. Aucune erreur de navigateur ou de construction d'archives n'est nécessaire pour reproduire le conflit.
- Le chemin par défaut sous `.logs/` est compatible avec l'inventaire. Le défaut concerne le choix libre du chemin, dont les restrictions actuelles excluent dist et .build mais ne préviennent pas cette création dans les fichiers du paquet.
- Le test intégré des deux aliases simule les étapes de contrôle : il vérifie leur équivalence, sans vérifier l'effet du journal sur l'inventaire réellement contrôlé.
- Piste : documenter et contrôler un emplacement compatible avant de créer le journal, par exemple `.logs/` à la racine ou un dossier extérieur au paquet. Conserver l'inventaire strict plutôt qu'exclure indistinctement tous les fichiers .log.

**MA-02 — Éditorial : préciser la portée de « lecture seule » et de « sans écrire ».**

- Sources : `maintenance/README.md:94`, `scripts/validate_all.py:186` à `:200` et `:267` à `:270`.
- La documentation situe correctement la protection sur dist et les archives, mais emploie aussi « sans construire ni écrire ». Le runner commence par py_compile, qui produit des caches Python ; des régressions construisent et modifient également des copies temporaires.
- Le contrôle final compare les dates et tailles des fichiers de dist, .build et des archives ; il ne garantit pas l'absence de toute écriture dans l'environnement.
- Piste : décrire cette option comme une validation sans construction ni remplacement des distributions, en précisant les caches et fichiers temporaires. Cette réserve ne remet pas en cause la protection annoncée des exports ; elle évite une attente plus large que son périmètre.

### Raccords aux points précédents

- **SK-03 reste à préciser.** Le résumé de version reprend le déclencheur persistant/partagé/audité sans mieux distinguer une proposition enregistrée d'une transmission pour reprise.
- La recette de `maintenance/evolution.md:19` demande de vérifier comment un mécanisme pourrait être satisfait sans intention. Les reproductions GV-01 à GV-03 restent pertinentes pour cette exigence : les suites actuelles ne les couvrent pas.
- La séparation entre atelier d'édition et formalisation B1b est rappelée dans la révision courante ; ce rappel ne résout pas à lui seul DI-04 ni la formulation générale GU-01.

### Vérifications de cette étape

- 18 adresses exactes distinctes dans les trois documents, représentant 17 sections canoniques et 26 occurrences : toutes résolues. Les cinq anciens aliases de la table de migration sont explicitement dépréciés, pas des routes actives manquantes.
- Version du manifeste : 1.0.0 ; révision : R2026-10-10-PHASE5, cohérente avec le README, les notes de version et la base des connexions ; taille actuelle de la skill : 18 852 octets UTF-8, budget de 46 000 octets.
- Les neuf tests existants de préparation réussissent. Ils couvrent notamment le verrou existant, les limites visibles, les aliases du journal, l'exclusion des métadonnées et le refus d'un noyau excessif avant modification des exports.
- Deux reproductions supplémentaires exécutent les CLI réelles de préparation sur des copies complètes, pour MA-01. Trois cas exécutent le script de build sur des copies minimales pour les branches de sauvegarde décrites plus haut ; la compilation y est remplacée par un succès témoin. Dans le cas de restauration seule, le staging s'arrête volontairement sur l'absence du README ; ce cas n'est pas une livraison complète réussie.
- Script, résultats et journaux de ces cinq cas conservés hors paquet dans `/workspace/work/revue-maintenance/`. La validation des liens, de l'inventaire et de la carte de lecture est exécutée après enrichissement du carnet.

Cette étape enrichit uniquement le carnet. Aucun correctif des procédures ou scripts, aucune promotion de route et aucune nouvelle révision publiée ne sont appliqués. Le build complet, la reproductibilité des deux archives et la validation navigateur ne sont pas établis par ces vérifications ciblées ; la limite de validation globale précédemment consignée reste distincte.

## Scripts — examen terminé

Le dossier contient quinze fichiers livrés : treize scripts Python, un script Bash et le manifeste JSON. Leur examen porte sur les responsabilités, les registres, les interfaces CLI, les contrôles, les limites déclarées et les familles de tests. Les scripts de préparation, de construction et le runner déjà lus pendant la maintenance ont été raccordés à cette analyse. Les grands validateurs sont examinés par leurs fonctions et registres ; cette revue ne constitue pas une preuve exhaustive de tous les chemins d'exécution.

### Utilité des outils et du manifeste

| Fichier | Fonction et utilité observées | Portée et appréciation |
|---|---|---|
| `scripts/build_core.py` | Compile le noyau depuis les blocs des sources et vérifie le fichier complet de la skill. | Important pour conserver une seule définition et des détails atteignables. Le registre protège 43 blocs, dont 20 communs et 23 différés ; les routes des détails doivent servir leur texte complet. Le budget de 46 000 octets est contrôlé avant écriture. |
| `scripts/read_route.py` | Résout les anciennes identités et les adresses lisibles, sert un mode ou une section, cherche les sujets et expose les connexions. | Central pour le chargement progressif. LIEUX est partagé avec la compilation et les validateurs. Doublons, propriétaires absents et routes ambiguës sont refusés ; un bloc n'est replié que si son texte complet est présent dans la section compilée. La recherche reste littérale, avec alias et classement. |
| `scripts/validate_design_governance.py` | Contrôle inventaire, liens, références opérationnelles, provenance des sources, valeurs structurées et présentation du paquet. | Utile pour éviter les fichiers manquants, les renvois cassés et les mélanges de distribution. Les commandes citées sont analysées sans être exécutées ; les exemples et portées explicites sont distingués. Il ne teste pas le sens ou le résultat d'un design. |
| `scripts/validate_reading_map.py` | Vérifie carte, locators, connexions, sujets et liste close des conditions de façade. | Utile pour maintenir l'orientation et ses conditions. Il réutilise le résolveur ; la pertinence des connexions et les contradictions nouvelles restent hors de sa couverture annoncée. |
| `scripts/validate_structure.py` | Protège les concepts, renvois, résumés, termes, blocs compilés, entrées et conditions de chargement. | Utile pour préserver les responsabilités pendant une refonte. Plusieurs gardes sont lexicales et demandent un entretien lors d'une reformulation. Le contrôle de l'en-tête laisse passer les types implicites de SC-03. |
| `scripts/check_render.py` | Observe un fichier HTML ou une URL dans Chromium ; produit contrôles, captures facultatives, couverture et provenance. | Utile pour les défauts objectivables : débordement, contraste borné, noms candidats, cibles, structure, clavier, mouvement réduit et objet de preuve. Aucun verdict global n'est rendu. Les zones non mesurées sont souvent réservées ; SC-01 et SC-02 montrent deux limites supplémentaires. |
| `scripts/validate_all.py` | Orchestre les contrôles, régressions, cas CLI négatifs, puis les exports et la comparaison des archives. | Utile pour exercer le paquet ensemble. Le déplacement d'une section est testé sur des copies, avec et sans mise à jour de LIEUX. Les refus CLI sont contrôlés par leur motif, pas seulement leur code. Lecture seule et export Local ont des périmètres distincts. |
| `scripts/preparer_livraison.py` | Compile, lance la validation complète, conserve un journal et affiche les limites et empreintes facultatives. | Bonne entrée opérateur ; les options log/journal sont équivalentes et l'export Local est refusé. MA-01 reste à corriger pour le choix du journal. | <!-- références:github -->
| `scripts/build_distributions.sh` | Prépare et contrôle les deux exports, archive leur contenu, vérifie leurs membres puis remplace les sorties avec sauvegardes. | Utile pour une livraison reproductible et une reprise prudente. Le staging précède le remplacement. Le manifeste contrôle les membres, mais la copie des scripts est également énumérée dans Bash : ajouter un outil demande d'entretenir ces deux lieux. La comparaison des deux builds relève du runner. | <!-- références:github -->
| `scripts/package_manifest.json` | Déclare version et fichiers des distributions GitHub et Local. | Utile pour contrôler exactement ce qui est livré. Les 109 entrées GitHub et 104 entrées Local sont sans doublon ; les cinq différences correspondent au workflow, à gitignore et aux trois outils réservés à la préparation GitHub. |

### Utilité des tests

| Fichier | Ce qu'il protège |
|---|---|
| `scripts/test_core_budget.py` | Bornes du budget, octets UTF-8 plutôt que caractères, conservation de la skill lors d'un refus, séparation commun/différé, présence et activation des détails. |
| `scripts/test_read_route.py` | Dispositions courantes et anciennes, blocs de code, identifiants structurels, connexions, recherche, options CLI, repli fidèle au contenu réellement chargé et ligne unique du mode. |
| `scripts/test_audit_regressions.py` | Mutations des conditions de façade, liens et fragments, références opérationnelles et portées de distribution, provenance, capacités disjointes, domaines d'exemple et activation des ressources. |
| `scripts/test_check_render.py` | Interprétation de données synthétiques (A), pages pièges avec navigateur (B), JavaScript réellement livré sur DOM simulés (C). Les trois niveaux ne constituent pas la même preuve. |
| `scripts/test_preparer_livraison.py` | Orchestration, journal et limites visibles, exclusion des métadonnées, verrou existant, refus d'un noyau excessif avant modification des exports. Les étapes simulées ne couvrent pas automatiquement l'intégration complète. | <!-- références:github -->

### Appréciation d'ensemble

Les outils ont des responsabilités distinctes et aucun fichier n'a été identifié comme globalement inutile. Les registres sont concrets : fichiers livrés, lieux actuels, blocs protégés, concepts et conditions de façade. Les tests négatifs et mutations apportent une protection utile contre les retours de défauts connus. Une suite réussie atteste cependant ses cas, pas une couverture générale.

La recette de rendu déclare des frontières importantes : une présence de nom candidat reste réservée, une borne de tabulation atteinte reste réservée, le texte natif et les pseudo-éléments non mesurés gardent une limite, l'objet de preuve n'atteste pas les pixels ni l'occlusion. Les captures existantes sont refusées avant mesure pour conserver un avant/après. Ces protections sont utiles, même si le vocabulaire PASS de chaque contrôle doit rester lu dans son périmètre exact.

Les validateurs documentaires s'appuient largement sur des fragments, des titres et des motifs lexicaux. Ils protègent les conditions déclarées, mais une réécriture peut demander de mettre à jour leurs motifs. La phrase générale « Une reformulation ne casse pas ces gardes » dans `scripts/validate_structure.py:31` gagnerait à être nuancée au regard de ces contrôles littéraux.

Deux commentaires sont aussi devenus périmés : `scripts/validate_design_governance.py:109` et `scripts/validate_reading_map.py:302` disent que les notes de version sont absentes de Local ; le manifeste courant les contient dans les deux distributions et le build les conserve. Ces commentaires ne changent pas le résultat observé des contrôles.

### Points conservés

**SC-01 — Vérifié sur DOM simulé : le nom candidat disparaît lorsque la visibilité est rétablie sur un descendant.**

- Sources : `scripts/check_render.py:55` à `:62`, `:179` à `:194` et `:486` à `:497` ; comparaison avec le traitement de visibilité de `:130` et `:270`.
- Un bouton ordinaire contenant « Confirmer » produit ce nom candidat et une réserve sur le nom accessible calculé, comme prévu. En plaçant ce même bouton avec visibility visible sous un conteneur visibility hidden, le candidat devient vide et le contrôle produit RETURN.
- Le helper de nom considère la visibility hidden de tout ancêtre comme un masquage irréversible. La visibilité CSS peut pourtant être rétablie sur le descendant ; les helpers de contraste et d'objet de preuve distinguent déjà ce cas. La suite C couvre ce rétablissement pour l'objet de preuve, pas pour le nom.
- Piste : distinguer la visibilité effective du candidat des masquages d'ancêtres qui restent contraignants, puis couvrir le cas dans les tests DOM et navigateur. Ne pas confondre ce correctif ciblé avec une implémentation complète d'AccName.
- Portée : le JavaScript réel et l'interprétation sont exercés sur DOM simulé. Le résultat dans l'arbre d'accessibilité d'un navigateur réel reste non observé dans cette revue.

**SC-02 — Vérifié sur DOM simulé : une couleur de remplissage du texte différente de color n'entraîne aucune réserve de contraste.**

- Sources : `scripts/check_render.py:164` à `:178` et `:445` à `:484`.
- Le cas témoin déclare un texte noir sur fond blanc et produit PASS. Le même DOM déclare ensuite webkitTextFillColor presque blanc, avec color toujours noir ; il produit encore PASS, un candidat évalué et aucune ligne non mesurée.
- Le calcul utilise seulement cs.color, sans considérer cette propriété de peinture ni déclarer le cas hors couverture. Le HTML témoin emploie la propriété CSS `-webkit-text-fill-color`. Le fait que l'algorithme ait évalué une couleur ne suffit donc pas à affirmer qu'il a évalué celle qui remplit effectivement le texte dans ce cas.
- Piste : utiliser la couleur effective dans un périmètre explicitement supporté, ou conserver une réserve lorsque la peinture du texte diffère de color. Ajouter ce cas aux témoins DOM et navigateur, avec un contrôle indépendant de la couleur peinte.
- Portée : le PASS et l'absence de réserve sont reproduits sur le JavaScript réel dans un DOM simulé. La peinture et les pixels dans Chromium ne sont pas vérifiés ici.

**SC-03 — Vérifié par CLI : une description YAML nulle ou non textuelle passe le contrôle de l'en-tête.**

- Sources : `scripts/validate_structure.py:651` à `:682` et `:685` à `:697`.
- Sur une copie complète du paquet, l'en-tête actuel passe et un parseur YAML indépendant confirme une description de type chaîne. Remplacer seulement sa valeur par null, true, puis 123, sans guillemets, laisse la CLI de validation structurelle réussir dans les trois cas.
- Le parseur YAML indépendant lit respectivement une valeur nulle, un booléen et un entier. Le parseur limité du validateur les conserve tous comme chaînes non vides ; il ne distingue donc pas ces valeurs d'une description textuelle. La valeur null entre guillemets est bien une chaîne et passe aussi, ce qui fournit un témoin de la distinction attendue.
- Piste : contrôler que les métadonnées requises sont des chaînes non vides selon le sous-ensemble YAML annoncé, ou exiger des guillemets pour les scalaires ambigus. La reproduction utilise un parseur déjà installé ; elle ne demande pas d'ajouter une dépendance au paquet.
- La description de la skill actuelle est une chaîne valide. Cette reproduction porte sur le pouvoir de rejet du validateur ; elle ne constate pas un chargement réel de skill par un hôte avec ces entrées modifiées.

### Raccords aux points précédents

- **ACC-01 reste pertinent.** La recherche par phrase combine des mots, alias et scores de rareté ; elle ne diagnostique pas le sens d'un symptôme. La réussite des tests de navigation ne garantit pas le bon premier résultat pour toute formulation humaine.
- **MA-01 et MA-02 restent pertinents.** Le journal peut entrer en conflit avec l'inventaire ; lecture seule protège les sorties de distribution mais n'interdit pas les caches et fichiers temporaires.
- Les limites **GV-01 à GV-03** restent celles des validateurs de gouvernance appelés par le runner. Leur présence dans une orchestration plus large ne leur ajoute pas de contrôle.
- Les écarts documentaires relevés dans SK, DI et GU ne sont pas annulés par les suites lexicales réussies : leur couverture reste déclarée et bornée.

### Vérifications de cette étape

- Suites réussies : lecteur (84 cas), budget et détails du noyau (18 cas), régressions d'audit (68 cas). Les neuf tests de préparation déjà réussis pendant la maintenance ne sont pas relancés sans changement les concernant.
- Partie C du rendu exécutée séparément : 51 cas sur DOM simulés, tous réussis. Cela ne vaut ni exécution complète du script de test du rendu, ni validation de ses pages pièges.
- Quatre cas DOM supplémentaires comparent deux témoins aux cas de SC-01 et SC-02. Cinq validations structurelles par CLI comparent l'en-tête courant, les trois types non textuels et une chaîne citée.
- Tentative d'observation avec Chromium installé : BrowserUnavailable au lancement, avant mesure de la première page. Aucune observation navigateur ni capture réelle n'est déclarée réussie. La limite antérieure de serveur local reste consignée séparément.
- Manifeste contrôlé : version 1.0.0, 109 fichiers GitHub, 104 fichiers Local, aucun doublon ni fichier exclusivement Local. Les membres exacts d'archives nouvellement construites ne sont pas contrôlés dans cette étape.
- Reproductions, pages témoins et résultats conservés hors paquet dans `/workspace/work/revue-scripts/`. Validation du paquet GitHub, de la carte de lecture et de la structure réussie après enrichissement du carnet ; copie temporaire assemblée d'après les 104 entrées Local également validée. Les références du carnet aux trois outils réservés à GitHub portent leur scope explicite. Ce contrôle Local ne construit pas les archives.

Cette étape enrichit le carnet ; elle ne modifie aucun outil, test ou contrat livré. Aucun brief de design ni verdict d'acceptation n'est créé. Le build complet et la reproductibilité des archives restent hors des vérifications effectuées ici.

## Supports de composition — lecture terminée

Lecture du 12 octobre 2026. Dans le checkout de base 6e5a8c2, les quatre supports de composition sont définis dans `design/formes/catalogue.md:6` à `:54`, sous BIBLIOTHEQUE/SUPPORT. Cette étape approfondit le niveau support déjà rencontré dans la revue de design. Elle provenait d'une interprétation trop étroite de la demande : le dossier supports de présentation demandé est présent dans une copie plus récente, examinée dans la section suivante. Les observations de composition sont conservées comme complément, avec leur périmètre distinct.

### Utilité du niveau support

Un support définit le champ spatial : espace disponible, limites, cadre, densité et relation entre contenu, navigation, données et produit. La grille organise la lecture dans ce champ ; la scène relie promesse, contenu, preuve et action. La distinction est utile pour ne pas choisir une scène uniquement parce qu'un cadre ou un grand vide plaît.

La chaîne support/grille/scène/objet/primitive décrit des responsabilités ; `design/formes/choisir.md:8` à `:14` précise qu'elle n'est pas une suite obligatoire. Une structure peut être héritée. En STANDARD, le support ne s'ajoute que si le champ est ouvert ; en DIRECTION, les niveaux sont examinés puis seuls ceux qui changent la décision sont retenus (`design/formes/choisir.md:151` à `:159`). L'analyse n'appelle donc pas quatre variantes ni un nouveau brief.

### Utilité des quatre supports

| Support | Ce qu'il apporte | Quand son choix est utile | Vigilance principale |
|---|---|---|---|
| `SUPPORT/FREE_FIELD` | Un champ ample sans châssis apparent, où promesse, illustration ou geste peuvent porter l'entrée. | Une relation perceptuelle ou de marque demande de l'espace avant la preuve détaillée. | Garder foyer, circulation, action et zone de preuve retrouvables ; les repères continus d'une tâche critique ou d'une comparaison dense peuvent appeler un autre champ. |
| `SUPPORT/ARCHITECTED_FRAME` | Des limites, axes ou seuils qui rendent l'organisation de la zone active sensible. | Le cadre aide à percevoir la construction et à organiser usage ou preuve. | Le cadre doit avoir une conséquence utile ; l'institution ou la maturité ne deviennent pas un style universel. Le choix reste situé selon le public et la tâche. |
| `SUPPORT/OPERATIONAL_CANVAS` | Une surface où contrôles, contexte et données forment la première lecture. | Observation, analyse, comparaison ou administration sont centrales. | Protéger la récupération des données et l'action ; la densité doit répondre au besoin de travail, comme le précise SP-01. |
| `SUPPORT/COLLECTION_PLINTH` | Des pièces distinctes, hiérarchisées par espace, proportions, voisinage ou cadence. | Une collection, un portfolio ou des cas demandent une sélection et des identités perceptibles. | Conserver métadonnées et accès à l'action ; le vide ne doit pas ralentir une comparaison rapide. Une identité visible ne prouve pas à elle seule une mémorisation. |

### Appréciation d'ensemble

Les quatre descriptions sont courtes et exploitables : définition, choix, évitement et preuve sont présents pour chacune. Aucun support n'est identifié comme inutile. Leurs différences portent sur une responsabilité spatiale ; elles ne constituent ni quatre styles exclusifs ni un catalogue exhaustif de surfaces possibles.

Les correspondances support/scène sont explicites : FREE_FIELD peut accueillir EDITORIAL_FIELD, ARCHITECTED_FRAME donne une condition encadrée à FRAMED_PRODUCT, OPERATIONAL_CANVAS décrit le champ de OPERATING_GRID. Ce sont des niveaux distincts, pas des doublons à supprimer (`design/formes/catalogue.md:170`, `:180` et `:190`).

La matrice propose des grilles et unités locales favorables pour chacun des quatre supports. Elle autorise une combinaison non listée avec le contrat applicable et ne transforme pas une ligne en prescription (`design/formes/catalogue.md:437` à `:457`). Une forme locale peut aussi être dérivée avant toute promotion ; conserver un héritage est valable si sa responsabilité suffit.

Le test de masquage est bien limité : il examine un parti perceptuel ou expert et n'atteste pas l'utilisabilité. Une composition qui dépend utilement de son contenu, avec relation déclarée et repli, reste recevable ; le test ne force pas l'ajout d'un décor indépendant du produit. Le contrôle de non-généricité conserve cette même exception dans `V1/sections/BIBLIOTHEQUE.md:49`.

Les descriptions compactes ne portent pas tout le contrat de fabrication, et cela ne constitue pas une absence de connaissance : `gouvernance/structure.md:22` à `:66` fournit preuve, portée, limites, contenu, états, mobile, accessibilité et calibration. Largeur, masses, distances et recomposition sont concrétisées dans le projet au moment où elles changent la relation ; elles ne sont pas des valeurs universelles des supports.

### Points conservés

**SP-01 — À préciser : le critère opérationnel est plus large que le besoin de densité.**

- Sources : `design/formes/catalogue.md:32` et `:34`, `design/formes/choisir.md:32` et `:122`, `gouvernance/structure.md:58`.
- OPERATIONAL_CANVAS est décrit comme dense, tandis que son critère de choix couvre observer, analyser, comparer, administrer ou décider. Ces activités n'impliquent pas toutes la même quantité d'information simultanée ni le même besoin de compression.
- Le reste du système traite déjà la densité comme un axe à choisir selon la relation et permet un champ calme avec plusieurs informations nécessaires. Il n'existe donc pas de règle générale imposant la densité à toute tâche opérationnelle ; la formulation courte du support peut toutefois suggérer cette association.
- Piste : préciser que la densité est justifiée par une lecture simultanée, une comparaison ou une manipulation qui la demande, et qu'elle reste réglée selon la tâche et le public. Conserver l'instrumentation et le contexte utiles sans les transformer en encombrement obligatoire.

**SP-02 — À préciser : la mémorisation visée par COLLECTION_PLINTH doit rester distincte de sa preuve spatiale.**

- Sources : `design/formes/catalogue.md:44` et `:48`, `design/formes/choisir.md:90` à `:99` et `:127`, `gouvernance/structure.md:13`.
- Le critère de choix vise des pièces mémorisées comme distinctes. La preuve compacte demande identité, métadonnées et relation à l'action ; elle permet d'inspecter la différenciation et l'accès, mais n'établit pas directement ce qu'une personne retient.
- Les contrats communs distinguent déjà preuve perceptuelle et accomplissement dans une tâche. Ce point explicite la portée de l'objectif ; il ne constate pas une contradiction générale ni une affirmation de mémorisation déjà validée.
- Piste : présenter la différenciation visuelle comme effet attendu, puis ajouter une observation adaptée seulement lorsqu'un run revendique réellement une amélioration de mémorisation. Garder une inspection perceptuelle pour un objectif simplement spatial ; ne pas imposer un test de mémoire à toute collection.

### Vérifications de cette étape

- 17 références exactes distinctes dans la section des supports et les quatre lignes de compatibilité : toutes résolues, y compris leurs grilles, objets, micro-interface et contrôle structurel.
- Les quatre identifiants courts et leurs formes BIBLIOTHEQUE/SUPPORT correspondantes donnent le même fichier et le même titre : lignes 10, 20, 30 et 40 du catalogue. Chaque section servie conserve choix, évitement et preuve.
- La CLI du lecteur sert seulement OPERATIONAL_CANVAS lorsqu'il est demandé. Un identifiant de support synthétique absent est refusé, sans repli silencieux vers son parent.
- Les liens et l'intégration du carnet sont contrôlés par les validations du paquet et de la carte après ajout de cette section. Les suites de navigation déjà réussies ne sont pas relancées : le lecteur et les routes n'ont pas changé.

L'appréciation est documentaire. La qualité de composition, la réussite des tâches et l'effet sur la mémorisation restent non évalués sur des rendus réels dans cette étape. Le carnet est enrichi ; aucune description de support ni aucune règle n'est modifiée.

## Supports de présentation — examen terminé

Lecture du 12 octobre 2026. Source examinée : /workspace/presentation-v1-corrigee/supports, révision R2026-10-11-CORRECTIFS. Les 24 fichiers du dossier correspondent, octet pour octet, à ceux de /workspace/correctifs-presentation-v1-2026-10-11/produit/supports. La version presentation-v1 précédente existe aussi, avec des fichiers plus lourds ; elle n'est pas la base de ce complément.

Ce dossier contient les aides de présentation et de navigation : pages HTML, cartes SVG, contenus JSON et Markdown, générateurs et police. Il est distinct des routes de composition SUPPORT/FREE_FIELD et des trois autres supports spatiaux. Les chemins supports cités dans cette section désignent les fichiers de cette copie externe ; ils ne sont pas des dépendances ajoutées au checkout de base.

### Utilité des fichiers

| Fichiers de la copie examinée | Fonction | Appréciation |
|---|---|---|
| supports/README.md | Oriente vers les trois cartes, distingue lecture GitHub et ouverture locale, explique fabrication et limites. | Utile pour trouver le bon format et reprendre les sources. Le rôle dérivé des supports est clairement déclaré. |
| supports/systeme.json et supports/systeme.md | Décrivent les entrées, responsabilités, relations et autorité des sections. | Bon point d'entrée pour comprendre qui fait quoi. Le Markdown est généré et directement lisible sur GitHub. |
| supports/parcours.json et supports/parcours.md | Présentent cadrage, direction, fabrication, observation, vérification et sortie, avec protections et retours. | Complètent la carte des responsabilités par une lecture du travail. La présentation rappelle que le parcours s'adapte au risque. |
| supports/boucle.json et supports/boucle.md | Détaillent observer, diagnostiquer, modifier, réobserver, comparer et décider, avec reprise du diagnostic. | Utiles pour relier critique et changement réel, sans quota de retouches ni acceptation automatique. |
| supports/index.html, supports/parcours.html et supports/boucle.html | Pages interactives autonomes : sélection d'entrée ou d'étape, surlignage, thème, liens, texte et export SVG. | La sélection garde le contexte complet. Le SVG de grand écran est remplacé par des blocs HTML au format étroit. Le contenu et les sources restent disponibles sans JavaScript. |
| Les six SVG clair/sombre | Images partageables, intégrables aux documents, avec texte sélectionnable, titre, description, police et licence embarquées. | Deux variantes par carte permettent la lecture selon le thème. Les illustrations sont réutilisables hors de la page interactive. |
| supports/page.template.html | Met en commun structure, CSS, comportement et adaptations des trois pages. | Utile pour conserver une présentation cohérente et éviter trois implémentations indépendantes. |
| supports/generer.py | Produit 12 sorties depuis les trois JSON, la palette commune et le gabarit. | Utile pour la fraîcheur et la reproduction. La géométrie et une partie du graphe restent codées dans Python ; SV-01 précise cette limite. |
| supports/preparer_police.py | Fabrique la police WOFF2 réduite et son relevé de couverture, avec versions épinglées. | Limite le poids tout en conservant la police source. Vérifie les caractères et l'axe de graisses pendant la fabrication ; son mode check contrôle la reproduction sans écriture. |
| Les cinq fichiers fonts | Police TTF source, police WOFF2 réduite, couverture JSON, dépendances de fabrication et licence OFL. | Chaque ressource a une fonction distincte : source reproductible, livraison légère, traçabilité, environnement de fabrication et autorisation de redistribution. |

Le validateur associé, scripts/validate_supports.py dans la même copie, contrôle la fraîcheur des sorties, les poids, les empreintes de police, la couverture demandée, les identifiants, les focus, le retour de diagnostic, les cibles locales et fragments, ainsi que la présence des alternatives et de la licence SVG. Il est appelé par le runner de cette révision. Il ne juge pas la lisibilité ni la compréhension humaine.

### Contenu et présentation

Les trois cartes se complètent : responsabilités, déroulement et boucle d'amélioration. Elles distinguent proposition et acceptation, trace légère et complète, et protègent les risques avant le choix concerné. Les textes orientent vers les sections propriétaires ; ils ne deviennent pas une quatrième définition de la règle.

L'équivalent Markdown offre le contenu complet et ses liens sans exiger une page HTML exécutée sur GitHub. Le README explique correctement que GitHub affiche le code des pages HTML et que les interactions se consultent après extraction. Les descriptions SVG sont des résumés ; les panneaux de protection, le premier objet et certains détails des responsabilités restent mieux couverts par le Markdown et l'équivalent HTML. La présence d'un titre et d'une description ne certifie donc pas une alternative exhaustive du SVG isolé.

Les captures historiques de la carte système à 1440 px et du parcours à 390 px ont été consultées. Elles montrent la carte d'ensemble sur grand écran et la recomposition en blocs sur mobile. Le rapport associé annonce 76 contrôles réussis sous Chromium et ses trois empreintes HTML concordent exactement avec les pages examinées. Ces preuves sont antérieures à la présente lecture ; elles ne sont pas une nouvelle exécution navigateur. Leur limite déclare l'absence d'observation sur téléphone physique ou lecteur d'écran, et l'absence de mesure de compréhension ou de préférence.

Les fichiers actuels respectent les budgets annoncés : SVG de 28 589 à 29 189 octets pour 50 000 autorisés ; HTML de 68 930 à 71 079 octets pour 100 000 autorisés. La police réduite pèse 10 980 octets, porte une signature WOFF2 et déclare 69 caractères. La police TTF source contient ces 69 caractères et son axe de graisses va de 200 à 800. Le contrôle standard rapproche les empreintes et le corpus déclaré ; il ne relit pas lui-même tous les glyphes du binaire réduit.

### Points conservés

**SV-01 — Vérifié : une relation JSON modifiée peut diverger entre Markdown et dessin tout en passant le validateur.**

- Sources externes : /workspace/presentation-v1-corrigee/supports/generer.py, lignes 62–77, 185–188 et 218 ; /workspace/presentation-v1-corrigee/scripts/validate_supports.py, lignes 37–59.
- Le dessin système place les flèches à des coordonnées fixes et prend leurs labels dans le JSON, sans utiliser réellement from et to pour choisir leurs extrémités. Le Markdown, lui, utilise ces deux champs.
- Reproduction sur une copie complète : la relation Guides vers Design devient Guides vers Maintenance, deux identifiants présents dans la carte. Après génération, le Markdown change et affiche la nouvelle relation ; les deux SVG et la page HTML conservent exactement leurs octets antérieurs.
- La validation des supports réussit encore : elle vérifie que les sorties égalent le générateur, mais ne contrôle pas ici la correspondance des relations entre formats.
- Les relations de la version livrée examinée concordent avec le dessin courant. Le défaut reproduit concerne la capacité à maintenir cette concordance lors d'une modification de source ; ce n'est pas le constat d'une carte actuellement fausse.
- Piste : construire les relations visuelles depuis leurs champs, ou vérifier explicitement la topologie fixe attendue et imposer une mise à jour du générateur si elle change. La régénération seule ne garantit pas l'équivalence sémantique des formats.

**SV-02 — Éditorial : le générateur ajoute un point après un titre déjà ponctué.**

- Source externe : /workspace/presentation-v1-corrigee/supports/generer.py, ligne 181 ; sorties supports/parcours.md, ligne 72, et supports/boucle.md, ligne 79.
- Les titres de pied se terminent déjà par un point. Le format commun ajoute un autre point après le titre en gras ; le texte rendu présente donc deux points successifs.
- Piste : choisir le séparateur en fonction de la ponctuation finale du titre. Cela relève de la finition documentaire, pas du contenu de la règle.

### Vérifications de cette étape

- Dossier identifié et variantes comparées : 24 fichiers de supports, identiques au lot de correctifs ; script associé de validation examiné intégralement.
- Contrôle courant des supports réussi. Deux générations sur une copie reproduisent à l'identique les 12 sorties livrées : trois HTML, six SVG et trois Markdown.
- Cibles HTML contrôlées : 11 liens dans index, 20 dans parcours et 21 dans boucle, tous vers des fichiers présents ; aucun identifiant HTML répété. Le validateur vérifie également les cibles JSON et les fragments Markdown.
- JavaScript des pages exécuté dans Node sur DOM simulé : sept sélections par page, 21 au total, avec titre, description, cible, surlignage et contexte conservés. Préférence de thème, basculement manuel et priorité du choix manuel vérifiés. Le callback d'export est présent ; le téléchargement SVG n'est pas exécuté dans cette simulation.
- Mutation de relation de SV-01 reproduite avec génération puis validation réelles. Script, copie et résultats conservés sous /workspace/work/revue-supports-presentation.
- La reproduction binaire de la police n'est pas réexécutée : l'environnement courant a FontTools 4.61.1 et ne dispose pas de Brotli, tandis que la fabrication épingle 4.60.1 et 1.1.0. Aucun outil de police n'est installé pour cette lecture. Empreintes, couverture déclarée, source TTF, poids et sorties sont contrôlés séparément.
- Validation du paquet de présentation réussie sur la copie Local examinée : 128 fichiers attendus, liens et références opérationnelles contrôlés. L'intégration du carnet reste vérifiée séparément dans le checkout de base : paquet GitHub et carte de lecture réussis, diff sans erreur de whitespace.

Le carnet est corrigé pour distinguer les supports de composition de ce dossier de présentation. Aucun fichier de la copie de présentation ni aucune source normative du checkout n'est corrigé ou remplacé. Les observations antérieures restent rattachées à leur base de revue.

## README principal — lecture terminée

Lecture du 12 octobre 2026. Fichier examiné intégralement : /workspace/presentation-v1-corrigee/README.md, 89 lignes, révision R2026-10-11-CORRECTIFS. Il est identique au README du lot /workspace/correctifs-presentation-v1-2026-10-11/produit. Les chemins et numéros de ligne de cette section désignent cette copie externe, sauf mention explicite du checkout de base.

Le README sert de porte d'entrée : comprendre la proposition du système, choisir un parcours selon son rôle, installer la skill et connaître les limites. Son contenu est utile et son découpage reste proportionné. La table par public évite de demander à toute personne de maîtriser les modes ; les règles détaillées et les procédures restent dans leurs sources.

### Utilité du contenu

| Partie | Fonction | Appréciation |
|---|---|---|
| Présentation et statut, lignes 1–5 | Dire ce que le système cherche à produire et annoncer son niveau de maturité. | Le statut expérimental et l'efficacité NOT-VERIFIED sont visibles dès l'entrée. Les objectifs de qualité ne sont pas présentés comme une amélioration mesurée. |
| Entrées par public, lignes 7–18 | Orienter débutant, designer, opérateur, relecteur, agent et mainteneur. | Les six destinations existent et correspondent au rôle annoncé. Le glossaire reste une aide accessible, sans lecture préalable obligatoire. |
| Installation, lignes 20–28 | Distinguer noyau copié et paquet complet, indiquer le répertoire d'exécution et vérifier l'accès aux routes. | Architecture correctement expliquée ; les opérations de première copie et de mise à jour demandent les précisions RM-01 et RM-02. La relocalisation des renvois reste fragile, RM-03. |
| Cinq règles, lignes 30–42 | Donner un résumé des priorités et pointer vers le standard propriétaire. | Correspondance documentaire avec les cinq absolus vérifiée. L'ancrage identitaire, les preuves applicables et la coordination avec les contraintes restent présents. Ce résumé renvoie explicitement au détail qui fait foi. |
| Fonctionnement, lignes 44–46 | Relier création et amélioration par observation. | Bon aperçu de la fabrication ; les deux cartes permettent d'approfondir sans recopier leur contenu. Ce paragraphe décrit le travail créatif courant ; il ne redéfinit pas les modes ni les conditions d'arrêt. |
| Carte, inventaire et lecture ciblée, lignes 48–81 | Comprendre les responsabilités, l'autorité et ouvrir une seule partie. | La carte dispose d'une voie texte ; la hiérarchie des sources est explicite. Les exemples de lecteur fonctionnent et la limite d'une recherche sans résultat est correctement déclarée. |
| Limites, lignes 83–89 | Situer version, efficacité, portée des validations et responsabilité. | Révision cohérente avec journal et notes. Bonne distinction entre capture, preuve d'usage et validation documentaire ; les CI antérieures restent rattachées à leur commit dans les notes de version. |

Par rapport au README du checkout 6e5a8c2, cette copie ajoute le statut expérimental au titre, les cartes de présentation et leurs liens, puis actualise la révision. Le texte d'installation et les cinq règles restent identiques. Cette comparaison ne revalide pas tout le système sur la nouvelle révision.

### Points conservés

**RM-01 — Vérifié : l'exemple de première copie suppose un répertoire non créé.**

- Source externe : README.md, ligne 24.
- Dans un projet où le dossier .claude/skills n'existe pas, la commande cp -r donnée en exemple échoue avec « No such file or directory ». La source de la skill est pourtant présente.
- Le texte dit où copier, mais ne rend pas explicite la création préalable des répertoires parents. L'exemple fonctionne lorsque ceux-ci existent déjà.
- Piste : inclure la création du répertoire dans la procédure de première installation et indiquer clairement depuis quel dossier l'exécuter. Il s'agit de compléter la recette, pas d'un défaut du noyau.

**RM-02 — Vérifié : répéter l'exemple de copie ne met pas à jour le fichier principal installé.**

- Sources externes : README.md, lignes 24 et 28 ; maintenance/versions.md, ligne 15.
- Après une première installation réussie, une modification synthétique est apportée à la source de la skill dans une copie isolée. La même commande cp -r est relancée, comme un utilisateur pourrait le faire pour suivre « recopiez la skill ».
- La commande réussit, mais crée un sous-dossier skill dans design-governance-practice. Le fichier SKILL.md à la racine d'installation conserve exactement son empreinte antérieure ; la version modifiée se trouve dans le sous-dossier imbriqué.
- Le README ne donne pas une commande distincte pour la mise à jour. La reproduction porte sur la réutilisation de son exemple, pas sur toutes les méthodes manuelles possibles de copie.
- Piste : documenter une mise à jour qui synchronise réellement le contenu à la racine de la skill installée, traite les anciens fichiers et vérifie le fichier principal après copie.

**RM-03 — Vérifié : les renvois externes de la skill restent dépendants de son emplacement d'origine.**

- Sources externes : README.md, lignes 22–28 ; agent/skill/references/flow.md, lignes 5–12 et 18.
- Après la copie prescrite dans .claude/skills/design-governance-practice, cinq destinations distinctes du flux pointent sous .claude/guides ou .claude/supports : guide du designer, index des supports, parcours Markdown et deux SVG.
- Ces destinations sont absentes alors que les guides et supports correspondants sont présents à la racine du paquet de test. Les mêmes renvois fonctionnent dans l'arborescence d'origine.
- Le constat SK-01 du checkout de base est donc confirmé séparément sur cette copie ; il s'étend aux nouveaux renvois de présentation. Les quatre références internes de la skill restent dans le dossier copié, et le lecteur fonctionne depuis le paquet : cela ne rend pas tout le système inutilisable.
- Piste : expliciter des renvois résolus depuis la racine connue du paquet, ou prévoir une installation qui conserve leur validité. Indiquer le répertoire d'exécution des commandes ne répare pas automatiquement les liens relatifs d'un document déplacé.

### Vérifications de cette étape

- 20 occurrences de cibles locales dans les liens Markdown et attributs HTML du README, dont deux fragments Markdown : toutes valides. Les images claire et sombre existent également. Cela contrôle les fichiers et ancres, pas leur rendu sur GitHub.
- Les cinq usages du lecteur réussissent sous Python 3.12.14 : START, sommaire, couleur, recherche contraste, recherche contraste avec guides. Les sorties ont été consultées ; la dernière ajoute bien les résultats d'orientation. L'exigence minimale Python 3.10 n'est pas réexécutée dans un interpréteur 3.10.
- Sources confrontées : standard de direction, classification et chargement de l'agent, guides d'entrée, index design, journal et notes de version. Les résumés restent des aides de lecture ; aucune nouvelle règle n'en est déduite.
- Première installation, recopie après changement de source et résolution des renvois reproduites dans des dossiers isolés. Script, journaux et résultats conservés sous /workspace/work/revue-readme. Aucun dossier d'installation réel de l'utilisateur n'est modifié.
- Validation documentaire de la copie Local réussie : 128 fichiers attendus. Ce contrôle ne couvre pas la copie de la skill hors de son emplacement d'origine. L'intégration du carnet réussit séparément sur le checkout GitHub de base : 109 fichiers attendus, carte de lecture valide et diff sans erreur de whitespace.

L'appréciation porte sur l'utilité et la cohérence documentaire du README, avec exécution de ses exemples utiles. La compréhension par une personne découvrant le système, le chargement effectif par Claude Code et l'amélioration des productions restent non évalués. Les observations sont ajoutées au carnet ; le README et la skill examinés ne sont pas corrigés.

## Notes de version — lecture terminée

Lecture du 12 octobre 2026. Fichier examiné intégralement : /workspace/presentation-v1-corrigee/RELEASE_NOTES.md, 53 lignes, révision R2026-10-11-CORRECTIFS. Il est identique au fichier du lot de correctifs, à celui des deux archives distribuées examinées et à celui de la référence main locale 5a5f563. Cette dernière est l'état disponible dans le dépôt local ; aucune mise à jour des références distantes n'est effectuée.

Les notes expliquent ce qui est livré, ce qui change et ce que les contrôles permettent d'affirmer. Elles complètent utilement le README, qui oriente, et le journal, qui conserve la suite des révisions. Leur répétition du statut expérimental est pertinente : une personne peut consulter les notes sans avoir lu le README.

### Utilité du contenu

| Partie | Fonction | Appréciation |
|---|---|---|
| Statut, destination et dates, lignes 1–6 | Identifier version, révision et usage recommandé. | Cohérent avec le README et le journal ; le pilote avec revue humaine reste clairement annoncé. |
| Ce que permet la V1, lignes 8–12 | Résumer fabrication, savoir chargé progressivement et responsabilités. | Utile pour comprendre le produit livré ; distingue déjà Web mobile et preuve native, ainsi que règles propriétaires et cartes d'orientation. |
| Changements, lignes 14–23 | Rendre lisibles cartes, police, navigation, compatibilité et noyau. | Annonces confrontées aux fichiers, aux archives et aux différences de version. La présentation ne crée pas de mode ni de style obligatoire. |
| Installation et utilisation, lignes 25–29 | Rejoindre la procédure et les entrées par rôle, rappeler proposition et acceptation. | Évite de recopier une seconde recette. Le lien d'installation fonctionne ; les limites RM-01 à RM-03 de cette recette restent applicables. |
| Contrôles inclus, lignes 31–41 | Donner une commande et préciser navigateur, CI et commit couvert. | Le navigateur est bien exigé par l'option et le workflow. Le périmètre Local et le renvoi aux preuves des correctifs peuvent être précisés, RN-01 et RN-02. |
| Attestation et limites, lignes 43–53 | Séparer forme validée, réalité de l'observation et efficacité du système. | Formulation fidèle au périmètre déclaré de RUN_CARD ; l'efficacité et la compréhension humaine des cartes restent explicitement non vérifiées. |

### Concordance des annonces

Les tailles annoncées sont exactes dans les copies disponibles : 18 852 octets pour PHASE5, 18 960 pour la copie PRESENTATION qui conserve le noyau PRATIQUE, puis 18 971 pour CORRECTIFS. La comparaison de ces deux dernières skills ne trouve que les titres « Structure » devenu « Situer l'interface » et « Composition » devenu « Typographie ». La vérification de compilation du noyau réussit.

Entre les copies PRESENTATION et CORRECTIFS, 25 fichiers de design, les 42 fichiers de gouvernance et les six fichiers de V1 sont identiques. Les deux différences restantes dans design sont la présentation du README et la révision déclarée de l'index des connexions ; leurs écarts ont été lus. Les fichiers de classification et de réponse de l'agent sont identiques. Ces comparaisons soutiennent l'annonce de conservation des règles pour ce passage de version ; elles ne prouvent pas l'absence de défauts antérieurs.

L'alias SYSTEME et le mode SYSTÈME donnent exactement la même sortie CLI. Les deux archives ont les empreintes enregistrées dans le relevé de livraison : 133 membres pour GitHub, 128 pour Local, inventaires conformes aux manifests. Chacune contient les 24 fichiers de supports et les notes examinées, identiques à la copie de référence. La présence des cartes et de la police dans les livraisons est donc directement vérifiée.

L'annonce d'une source commune aux formats est cohérente avec le générateur. Elle ne constitue pas une preuve automatique d'équivalence sémantique : SV-01 conserve la limite des relations visuelles codées dans Python. La couverture et la légèreté de la police sont déjà contrôlées dans la revue des supports ; sa fabrication binaire avec les versions épinglées n'est pas relancée ici.

### Points conservés

**RN-01 — À préciser : le périmètre de reproductibilité dépend de la distribution.**

- Sources externes : RELEASE_NOTES.md, lignes 33–39 ; scripts/validate_all.py, lignes 268–285, dans la copie examinée.
- Les notes annoncent que la validation couvre la reproductibilité, puis donnent la même commande disponible dans les deux distributions.
- Le runner vérifie deux constructions et leurs empreintes dans le dépôt GitHub. Dans Local, le script de construction est volontairement absent ; le runner annonce que construction et reproductibilité sont hors périmètre. L'option require-browser exige les tests de pages, sans ajouter ce script de construction.
- Ce périmètre est explicite dans le code et dans le journal historique de validation complète : la fin des contrôles Local le déclare. Le comportement est cohérent ; la présentation générale des notes peut laisser attendre la même couverture partout.
- Piste : ajouter une précision courte sur la portée de chaque distribution. Vérifier Local contrôle le paquet exporté ; reproduire les deux distributions demande les outils du dépôt GitHub.

**RN-02 — Éditorial : le paragraphe de CI ne renvoie pas aux preuves archivées des correctifs.**

- Source externe : RELEASE_NOTES.md, ligne 41. Preuves : instantanés de la référence origin/refonte locale, SUPPORTS-V1/lot-02/ci-hebergee.json et SUPPORTS-V1/lot-03/ci-hebergee.json ; relevé de livraison du lot de correctifs.
- Les CI 55 et 56 annoncées réussies correspondent bien à 213cfbaf8867142eb834c834311adb0fa626d8fe dans le relevé historique. Les notes disent correctement qu'elles précèdent les correctifs et n'attestent que ce commit.
- Le relevé des correctifs contient également les CI 57 et 58 réussies sur b3e071b24bd67a71c9438779eaf8f6810aa8b3a1. Le texte ne les cite pas ; « cette révision exige ses propres contrôles » reste une exigence correcte, sans donner accès à ceux déjà archivés.
- Les objets Git locaux confirment que l'arbre du commit d'intégration 5a5f563 est identique à celui de ce commit testé. L'instantané consulté conserve la CI 59 en cours ; aucun résultat actuel de cette CI n'est déduit de ce relevé.
- Piste : compléter le renvoi avec le relevé de livraison daté, ou avec les CI 57 et 58 et leur commit exact. Il s'agit de rendre la preuve disponible plus facile à trouver, sans transformer une CI en preuve esthétique ou d'usage.

### Vérifications de cette étape

- Huit liens locaux des notes, dont un fragment Markdown : tous valides. Les deux liens CI sont rapprochés de leurs identifiants, commits et résultats archivés ; aucune requête GitHub actuelle n'est effectuée.
- Tailles, deux seuls changements de titres, compilation du noyau et égalité de l'alias SYSTEME vérifiés sur les fichiers et par CLI.
- Deux archives lues sans extraction ni reconstruction : empreintes, inventaires, 24 supports et notes identiques contrôlés.
- Contrôle des supports exercé sur trois copies : baseline réussie ; sortie Markdown altérée refusée ; cible JSON absente refusée après régénération, pour les motifs attendus. Script, copies, journaux et résultats conservés sous /workspace/work/revue-release-notes.
- Route ACTION/RUN_CARD ouverte avec le lecteur et confrontée à la portée annoncée. Workflow disponible dans la référence main locale lu : il installe Playwright/Chromium et lance le runner avec require-browser.
- Conservation de l'historique constatée dans la référence origin/refonte locale, avec les anciens travaux, révisions et relevés de livraison. Le journal historique de validation complète comprend contrôles navigateur et fin de validation avec reproductibilité réussie ; il est consulté comme preuve antérieure, pas comme une nouvelle exécution.
- La suite complète, le navigateur et les constructions d'archives ne sont pas réexécutés dans cette étape. Les contrôles ciblés distinguent annonces vérifiables, portée du runner et preuves historiques.
- Intégration du carnet vérifiée sur le checkout de base : validation GitHub réussie avec 109 fichiers attendus, carte de lecture valide et diff sans erreur de whitespace.

Les notes sont utiles et les annonces matérielles contrôlées concordent avec la livraison. RN-01 et RN-02 sont des précisions documentaires ; aucun nouveau défaut bloquant de livraison n'est reproduit. Les observations sont ajoutées au carnet sans modifier les notes, les règles ni les outils examinés.

## Agent : contenu et installation — discussion

Lecture et discussion du 12 octobre 2026. Source : les sept fichiers de /workspace/presentation-v1-corrigee/agent, révision R2026-10-11-CORRECTIFS, avec la procédure du README et le registre du compilateur. Les chemins de fichiers agent de cette section désignent cette copie externe. L'objectif est d'expliquer et d'évaluer l'interface destinée à l'agent ; aucune installation dans un hôte n'est effectuée.

### Ce que contient agent

| Fichier | Rôle et utilité |
|---|---|
| agent/chemins.md | Porte classification, chargement, routes d'exécution et lecture ciblée à leurs emplacements propriétaires actuels. Il se consulte selon le besoin ; ses 368 lignes ne sont pas une lecture intégrale obligatoire à chaque demande. |
| agent/repondre.md | Définit réponse visible, transmission pour reprise et niveaux de trace. La réponse humaine garde les limites utiles ; les codes internes restent dans la trace sauf demande. |
| agent/skill/SKILL.md | Point d'activation : métadonnées, noyau commun compilé et déclencheurs de détail. La skill actuelle mesure 18 971 octets ; le registre garde 20 blocs communs et 23 blocs différés. |
| agent/skill/references/examples.md | Exemples déclarés illustratifs : correctif local, fabrication, direction, style et composant partagé. Aide à comprendre les séquences ; les valeurs et choix ne sont pas à recopier. |
| agent/skill/references/flow.md | Vue courte du parcours, avec liens vers les supports et le guide du designer. Ses renvois déplacés restent concernés par RM-03. |
| agent/skill/references/machine_projection.md | Aide conditionnelle à la sérialisation d'une RUN_CARD ; schéma et validateur restent les autorités de structure. Elle ne rend pas la projection obligatoire pour toute demande. |
| agent/skill/references/canonical_minimum.md | Repli lorsque le paquet est indisponible : conserver les distinctions et déclarer la limite. Il ne permet pas de présenter une hypothèse comme un run conforme. |

Le dossier fournit des instructions et des sources à un agent hôte. Il ne lance pas lui-même un modèle, ne crée pas ses outils et ne lui accorde pas des capacités. La pertinence du classement, l'application des consignes et la qualité produite demandent une observation de l'agent en situation.

### Installation et portabilité

**AG-01 — À préciser : le contenu est indépendant de Claude, mais la documentation d'installation privilégie Claude Code.**

- Le README, ligne 24, détaille les répertoires Claude Code puis dit seulement de donner SKILL.md comme instructions aux autres agents. Aucun appel d'API Claude ni dépendance au modèle Claude n'est présent dans les sept fichiers agent ; les commandes utilisent les outils Python du paquet.
- Les sources officielles consultées via Context7 confirment les racines de skills Claude Code et Codex. Claude Code découvre les dossiers .claude/skills du projet et ~/.claude/skills de l'utilisateur. Codex dispose notamment des racines .agents/skills du projet et ~/.agents/skills ; certaines racines .codex sont conservées pour compatibilité. Ces constats concernent les sources consultées, pas un test des applications installées chez l'utilisateur.
- Donner un texte d'instructions, installer une skill reconnue par l'hôte et fournir l'accès au paquet sont trois opérations distinctes. Une intégration native dépend du mécanisme de découverte et d'activation de l'hôte ; la lecture manuelle ne prouve pas cette intégration.
- Piste : conserver une seule skill commune et préciser les recettes pour les hôtes pris en charge, avec portée projet/utilisateur, accès au paquet, activation et mise à jour. Les autres hôtes restent à documenter ou à vérifier avant d'annoncer leur support natif.

**AG-02 — Vérifié : le contrôle d'accès au lecteur n'atteste pas l'installation native.**

- Source externe : README.md, lignes 25–26. La commande START a réussi dans la copie de référence pendant la revue du README, sans skill présente sous les répertoires locaux .claude/skills ou .agents/skills de cette copie.
- Ce résultat atteste l'accès aux routes du paquet. Il n'atteste ni découverte par l'hôte, ni activation, ni fichier installé effectivement chargé, ni mise à jour de cette copie. Une éventuelle installation globale n'est pas inspectée.
- Piste : séparer contrôle du paquet et contrôle de l'hôte. Pour ce dernier, constater la skill disponible, sa provenance et sa version, puis son activation et sa capacité à lire une route du paquet. Vérifier une copie de fichiers ne suffit pas à prouver l'exécution par un agent.

RM-01 à RM-03 restent les constats concrets de la recette actuelle : création des parents manquante dans l'exemple, fichier principal non actualisé lorsque la même commande est répétée, renvois externes cassés après déplacement. L'installation globale exige également un paquet et une version retrouvables ; installer une skill au niveau utilisateur ne transporte pas automatiquement le reste du dépôt.

### Contenu à discuter

- La séparation noyau/détails est utile et les blocs différés restent accessibles. Une modification du noyau doit passer par sa source propriétaire et le compilateur ; éditer le bloc généré seul ne constitue pas une évolution durable.
- La portée de SK-02 reste à préciser dans cette copie : la description inclut « juger », alors que les lignes 82 et 88 demandent construction de première scène et alternative. La route LITE et le standard rendent l'alternative conditionnelle. Expliciter la nature de la demande permettrait de conserver une revue seule lorsqu'aucune fabrication n'est demandée ou nécessaire.
- SK-03 reste une ambiguïté documentaire dans la ligne 95 : conserver ou montrer une proposition peut être lu comme persister ou partager un run. La transmission pour reprise ou acceptation mérite d'être distinguée de l'enregistrement de travail exploratoire.
- Les titres 5 et 6 ont été précisés dans CORRECTIFS. Le titre « Prendre le brief et viser le premier objet » couvre encore dans le noyau principalement les contenus manquants et leur marquage ; les détails de cadrage et du premier objet sont différés. Cela confirme seulement cette partie de SK-04 sur la nouvelle copie.
- La réponse en quatre rubriques facilite une remise de proposition. La maintenir adaptable à un correctif ou à un jugement éviterait les rubriques artificielles, notamment « ce qui manque pour la vraie version ». Ce point relève de l'adaptation du format par défaut, pas d'une suppression des limites ou de la trace requise.
- La posture senior exprime une ambition de travail. Ni le nom de la skill, ni sa découverte native, ni sa taille ne démontrent une qualité senior ou une amélioration générale de la production.

Les emplacements d'installation et références de la discussion sont conservés sous /workspace/work/revue-agent/constats-installation.json. Sources externes consultées : [racines de skills Codex](https://github.com/openai/codex/blob/main/codex-rs/ext/skills/src/host_roots.rs), [journal Claude Code](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) et [structure de skill Claude Code](https://github.com/anthropics/claude-code/blob/main/plugins/plugin-dev/skills/skill-development/references/skill-creator-original.md). La découverte et l'activation natives, les différences de comportement entre agents et l'efficacité en production restent non évaluées.

Le carnet conserve cette discussion. Aucune recette d'installation nouvelle ni modification des sources agent n'est appliquée.

## Guides : noms, niveaux et publics — discussion

Discussion du 12 octobre 2026. Les points sur agent sont déjà conservés dans la section précédente. Les quatre guides de /workspace/presentation-v1-corrigee/guides sont relus pour examiner leur nom, leur contenu et la proposition d'organisation par niveaux. Ils sont tous identiques, octet pour octet, aux guides du checkout de base : 34, 98, 295 et 96 lignes, 523 au total. Les chemins de cette section désignent la copie CORRECTIFS sauf mention contraire.

### Adéquation des noms actuels

| Nom actuel | Ce que le contenu fait réellement | Appréciation du nom |
|---|---|---|
| commencer | Expliquer comment demander, fournir les éléments utiles, comprendre la proposition et poursuivre ; ajouter ensuite une courte entrée pour opérateur ou agent. | Bonne idée de prise en main. La seconde partie change de destinataire et doit être distinguée dans une entrée de niveau 1. |
| designer | Fournir une carte de sujets, des combinaisons par résultat, des angles conditionnels et un arrêt de lecture. | Le métier décrit un public plausible, mais la fonction sert aussi un développeur, un responsable produit ou une personne apprenant à concevoir. Le document est surtout un guide de consultation, pas une formation graduée au métier. |
| equipe | Cadrer et piloter un travail, confier l'exécution, examiner les preuves et conserver une décision ou une reprise. | L'organisation collective est trop restrictive : l'introduction inclut déjà opérateur, designer et responsable. Une personne seule avec un agent utilise aussi ce guide. Pilotage décrit mieux cette fonction. |
| glossaire | Expliquer les mots et distinctions à consulter selon le besoin. | Nom juste ; référence commune aux autres guides, sans en faire un quatrième niveau. |

Les trois premiers noms mélangent action, métier et organisation. Une dénomination cohérente peut mieux exprimer l'intention du lecteur, tout en précisant les publics dans chaque introduction.

### Proposition de niveaux

Proposition de l'utilisateur : organiser les guides par niveaux en les adaptant au public. Recommandation de cette discussion : faire porter les niveaux sur la profondeur de lecture et l'implication dans le système. Une échelle « débutant, intermédiaire, expert » mélangerait connaissance du système, compétence de design et responsabilité de décision. Ces dimensions ne progressent pas nécessairement ensemble.

| Entrée proposée | Besoin et public | Fichier proposé, non créé |
|---|---|---|
| Niveau 1 — Prise en main | Demander un résultat ou une analyse, comprendre la réponse et poursuivre. Toute personne souhaitant utiliser le système sans apprendre son fonctionnement interne. | guides/prise-en-main.md, à partir de commencer. |
| Niveau 2 — Pratique | Concevoir, analyser ou améliorer ; retrouver les connaissances utiles et choisir les angles pertinents. Designer, développeur, responsable produit ou personne participant à la conception. | guides/pratique.md, à partir de designer. |
| Niveau 3 — Pilotage | Cadrer, superviser, vérifier, décider, conserver et transmettre. Opérateur, responsable, designer qui pilote, personne seule ou équipe. | guides/pilotage.md, à partir de equipe. |
| Glossaire — Référence commune | Comprendre un terme au moment où il intervient, depuis n'importe quelle entrée. | guides/glossaire.md conservé. |

Les numéros seraient affichés dans les titres et la navigation ; les fichiers garderaient des noms descriptifs. Cette forme est une proposition concrète, pas un renommage effectué ni une décision normative. Une personne expérimentée peut utiliser la prise en main pour déléguer simplement ; un responsable peu familier du design peut consulter le pilotage. Le lecteur entre directement par son besoin, sans parcours obligatoire des trois niveaux.

Le niveau de guide modifie l'explication et l'accompagnement. Les modes LITE, ITER, STANDARD, DIRECTION et SYSTÈME restent liés au travail et à son risque ; ils ne désignent pas le niveau du lecteur. La classification, les preuves applicables et les conditions d'acceptation ne sont pas abaissées par une entrée courte.

### Adaptation du contenu

- Prise en main : garder demande, éléments utiles, réponse et suite en langage courant. Proposer aussi explicitement le jugement ou l'analyse seuls, en cohérence avec la discussion agent. Le bloc de commencer aux lignes 23–34 s'adresse déjà à l'opérateur ou à l'agent ; le déplacer vers le pilotage ou le présenter comme un approfondissement séparé préserverait la simplicité de l'entrée.
- Pratique : conserver carte des sujets et combinaisons conditionnelles ; préciser que chacun peut consulter un sujet sans maîtriser tout le design ni adopter un métier particulier. Une courte introduction explique comment utiliser cette carte. Le changement de titre ne transforme pas automatiquement l'index actuel en cours d'apprentissage.
- Pilotage : conserver les responsabilités et le parcours court en tête. Faire lire les sections détaillées seulement si la décision, la preuve ou la reprise le demande. Le niveau 3 ne doit pas imposer les 295 lignes à tout responsable, ni devenir un protocole plus lourd par prestige du niveau.
- Publics : annoncer dans chaque introduction le besoin servi, les connaissances utiles, le rôle exercé et ce qui est attendu à la sortie. Adapter exemples et vocabulaire à cette situation ; éviter une catégorie figée de personnes.
- Glossaire : garder l'accès transversal et les termes reliés aux propriétaires. La définition d'un terme reste commune aux différents niveaux.

### Raccords et portée du renommage

GU-01, GU-02 et GU-03 sont confrontés séparément aux sources actuelles et restent à traiter : la modification trop systématique à la ligne 92 du guide equipe, l'ordre de classement brouillé par sa ligne 130 et le renvoi indirect à la revue créative à la ligne 263. Les sources actuelles de la boucle et du démarrage vague conservent respectivement correction justifiée/arrêt et passage après START ; la revue à six points reste dans CFT-00. Renommer les guides ne résout pas ces formulations.

Les noms actuels apparaissent dans 19 fichiers de la copie examinée : liens des documents, références de l'agent et de son noyau, table LIEUX du lecteur, manifests, contrôles et tests, JSON système et sorties de présentation. Une mise en œuvre doit modifier les sources de ces références, recompiler le noyau si ses chemins changent, régénérer les supports concernés et contrôler les deux distributions. Les sorties générées ne se corrigent pas seules à la main. Une transition pour les anciens liens doit être définie si leur compatibilité est conservée.

Vérifications de cette discussion : 23 occurrences de liens Markdown locaux, fragments inclus, et 53 adresses exactes distinctes des guides résolues dans la copie actuelle. Les mots DIRECTION et direction utilisés seuls sont des termes ou valeurs de mode, pas des adresses. Les comparaisons, références et cartographie du renommage sont conservées sous /workspace/work/revue-guides-niveaux/resultats.json. La compréhension des nouveaux intitulés auprès de lecteurs réels n'est pas mesurée.

La proposition de niveaux et les adaptations sont ajoutées au carnet. Aucun guide, titre publié ni chemin de fichier du système n'est renommé dans cette discussion.

## Maintenance, versions et V1 de référence — discussion

Lecture et discussion du 12 octobre 2026. Source courante : /workspace/presentation-v1-corrigee/maintenance, révision R2026-10-11-CORRECTIFS. Les trois documents sont relus : README, évolution et versions, 121, 115 et 59 lignes. Le journal de 66 lignes du checkout PHASE5 est comparé séparément ; les archives de la référence origin/refonte locale sont consultées. Aucun contenu distant n'est mis à jour.

### Fonction et appréciation

| Fichier de la copie courante | Fonction | Appréciation |
|---|---|---|
| maintenance/README.md | Sources et distributions, préparation, validation, dépendances, reprise après interruption et lecture des routes. | Procédure utile au mainteneur, hors du chargement ordinaire d'une proposition. Le texte est identique à celui du commit de base, avant l'ajout local du lien vers notre carnet. |
| maintenance/evolution.md | Recette d'une modification, portée de la contribution, promotion/dépréciation, gain observé et migrations. | Contrat de maintenance actif, identique au commit de base. Le contenu garde son utilité après un nettoyage éditorial du chantier. |
| maintenance/versions.md | Identifier version et révision, résumer les changements, conserver compatibilité, contraintes et limites. | Journal déjà allégé, mais qui mêle encore chronologie, noms internes de chantier et un contrat permanent de budget. Un nouveau lecteur n'a pas besoin de toute l'histoire pour utiliser le système. |

MA-01 reste à traiter pour le choix d'un journal de préparation : le preparer disponible dans main local et le validateur d'inventaire sont identiques à ceux de la reproduction de base. Le mécanisme n'est pas modifié par CORRECTIFS ; la préparation complète n'est pas réexécutée ici. MA-02 reste une précision utile : le README conserve « sans construire ni écrire », tandis que le runner distingue les distributions des caches et copies temporaires. RN-01 conserve également la différence de périmètre entre validation Local et reproductibilité des distributions GitHub.

### Travaux, progression et dates

L'ancien journal PHASE5 raconte le noyau commun, la finalisation de la refonte, un correctif de recette et la version initiale, avec étapes, dates et résultats. Le journal CORRECTIFS est davantage centré sur la livraison : il annonce la version initiale du 1 octobre 2026, la révision du 11 octobre et résume dix révisions intermédiaires. Des noms tels que PHASE5, PRATIQUE, U5 et les numéros d'audit restent visibles.

Le chantier détaillé a déjà été déplacé hors du paquet. La référence origin/refonte locale contient plans, progression, anciens journaux, runs, captures et preuves, avec notamment HISTORIQUE/journal-decisions.md et les lots de SUPPORTS-V1. Les copies de versions conservent les états PRATIQUE, PRESENTATION avant/après et CORRECTIFS. Le journal public peut donc être allégé sans faire disparaître cette mémoire.

Notre carnet reste une mémoire de revue en cours. Il est inclus dans les manifests modifiés du checkout PHASE5, mais absent de main local et de la copie CORRECTIFS examinée. Les propositions et constats qu'il conserve ne doivent pas être annoncés comme des changements déjà livrés dans versions. Lors du futur nettoyage, sa place dans les archives documentaires et dans les distributions doit être choisie explicitement.

| Date consignée | Progression de notre revue | Portée réelle |
|---|---|---|
| 11 octobre 2026 | Début du carnet et de la lecture progressive du système. | Fonctions des fichiers, observations, reproductions et pistes de correction. Les dates individuelles non consignées de chaque première lecture ne sont pas reconstruites. |
| 12 octobre 2026 | Compléments sur les supports de présentation, le README et les notes de version ; discussions sur agent, installation, guides, niveaux et maintenance. | Lectures et vérifications ciblées terminées pour ces étapes ; propositions enregistrées. Installation multi-agent, renommage des guides et corrections du paquet restent non appliqués. |
| Étape future, à dater lorsqu'elle sera réalisée | Traitement des observations retenues, préparation d'une V1 de référence et archivage du chantier. | Proposition de travail ; aucune date de publication, purge ou adoption n'est décidée dans cette discussion. |

### Proposition de nettoyage avant une V1 de référence

L'utilisateur propose de purger à un moment donné les travaux pour rendre la V1 neuve. La recommandation conservée est de nettoyer le contenu livré une fois la revue et les corrections retenues traitées, puis de figer une édition de référence identifiable. Ce nettoyage porterait sur le récit de chantier, les répétitions et les références devenues réellement inutiles ; l'historique Git et les archives datées resteraient disponibles pour comprendre et reproduire les décisions.

| Contenu | Place proposée après le nettoyage |
|---|---|
| Instructions, connaissances et contrats actifs | Paquet V1, avec leurs propriétaires et chemins valides. |
| Installation, guides et supports utiles à l'usage | Paquet V1, avec les clarifications retenues et leurs vérifications. |
| Version actuelle, date d'actualisation, contenu effectivement intégré, compatibilité, vérifications et limites actuelles | Fiche publique de l'état courant et notes de version correspondantes. |
| Plans de phase, progression détaillée, propositions, carnet de revue, essais et ancienne chronologie | Archives de chantier datées et retrouvables, avec les preuves associées. |
| Dates et versions des sources, observations, licences et contrôles | Conservées là où elles établissent la provenance, la compatibilité ou la portée de la preuve. |

Précision de l'utilisateur : le document public doit refléter d'abord l'état actuel et factuel, sans être organisé autour de la progression depuis le 1 octobre. Cette priorité remplace la proposition de conserver cette chronologie en première lecture. La date d'origine et les anciennes étapes restent dans les archives. Le document courant présente ce qui existe réellement aujourd'hui, la version identifiée, la date d'actualisation, la compatibilité, les vérifications obtenues et les points encore ouverts. Les propositions en attente continuent dans le carnet ; seuls les changements effectivement intégrés sont annoncés comme présents. Une actualisation documentaire porte sa date réelle sans faire passer une proposition ou une correction non appliquée pour une nouvelle livraison.

### Limites techniques du nettoyage

- versions contient encore le budget permanent du SKILL.md et l'autorité de maintenance. Si le fichier se recentre sur l'état courant, déplacer ce contrat vers sa documentation de maintenance exige de conserver sa définition, ses renvois et ses contrôles.
- Le validateur rapproche la version de CHANGELOG et celle du manifest ; le lecteur rapproche la révision du journal et celle des connexions. Effacer ou réinitialiser ces métadonnées sans mise à jour coordonnée casserait la cohérence contrôlée.
- Les « sections conservées » sont des sources actives, pas seulement des souvenirs : ACTION/PIPELINE-DIRECTION se résout dans V1/sections/ACTION.md, SAVOIR/INTEGRITY dans V1/sections/SAVOIR.md et BIBLIOTHEQUE/GATE dans V1/sections/BIBLIOTHEQUE.md. Leur éventuel déplacement demande une conservation de contenu et une migration de routes avant tout retrait.
- Le nettoyage éditorial ne mesure pas l'efficacité du système. Le statut expérimental et les limites observées demeurent tant qu'une autre preuve ne justifie pas leur évolution.

Vérifications de cette étape : trois liens Markdown locaux de maintenance valides ; neuf routes et aliases ciblés résolus ; dix révisions datées recensées dans le journal courant ; quatre états de journal retrouvés dans les archives locales de refonte. Les correspondances, dates et faits de progression sont conservés sous /workspace/work/revue-maintenance-version/resultats.json. Aucun nouveau build, test navigateur ou run créatif n'est exécuté pour cette discussion documentaire.

La proposition d'une V1 de référence et le suivi daté sont enregistrés dans le carnet. Aucun fichier du paquet ni aucune archive n'est supprimé ; le journal public n'est pas réécrit dans cette étape.

### Clarification : afficher l'état actuel et factuel

Clarification du 12 octobre 2026. Le document versions doit être actualisé pour répondre aux questions « quelle version ai-je, que contient-elle, qu'est-ce qui a été vérifié et qu'est-ce qui reste ouvert ? ». L'historique du chantier n'est pas un préalable d'utilisation et n'a pas à occuper cette présentation. La progression de notre revue est conservée dans ce carnet et dans les archives de travail.

Le repère factuel disponible à cette date est le paquet CORRECTIFS examiné, distinct du checkout PHASE5 qui contient notre carnet. Ce repère ne revendique pas une interrogation actuelle du dépôt distant. Les faits constatés sont notamment :

| Sujet | État constaté dans le paquet examiné |
|---|---|
| Identification | V1.0.0, révision R2026-10-11-CORRECTIFS ; lecture et actualisation de la discussion le 12 octobre 2026. |
| Contenu livré | Noyau commun compilé, routes de détail, quatre guides, gouvernance, maintenance et trois cartes de présentation ; les deux archives vérifiées contiennent les 24 fichiers de supports. |
| Installation | Recette détaillée pour Claude Code, instruction générale pour les autres agents. Les problèmes de première copie, recopie et renvois déplacés sont reproduits ; leur correction n'est pas intégrée. |
| Guides | Les noms commencer, designer et equipe restent dans les fichiers livrés. Prise en main, Pratique et Pilotage sont des propositions conservées dans le carnet. |
| Vérifications | Contrôles ciblés documentaires, de compilation, d'archives et de comportement des outils réalisés ; preuves historiques distinguées des exécutions courantes. L'intégration et l'activation natives dans plusieurs agents ne sont pas testées. |
| Limites | Efficacité générale non mesurée ; réserves et défauts documentés restent ouverts tant que leur traitement n'est pas appliqué et vérifié. |

Lors de la mise à jour du document public, établir ces faits depuis les sources et les résultats correspondant à la version réellement livrée. Une ancienne preuve ne devient pas actuelle simplement parce que la date du document change. La date du 1 octobre demeure un fait d'archive ; elle n'est pas le centre de la fiche publique envisagée. Cette clarification est enregistrée dans le carnet sans annoncer une réécriture déjà effectuée de versions.

## Supports : état courant et actualisation — complément

Lecture du 12 octobre 2026. Le dossier supports désigne ici celui de /workspace/presentation-v1-corrigee, révision R2026-10-11-CORRECTIFS. Ses 24 fichiers distribués sont toujours identiques au lot de correctifs examiné précédemment. Un cache Python local est présent après les vérifications ; il n'appartient pas à l'inventaire des supports distribués.

Ce complément applique la priorité donnée par l'utilisateur à un état actuel et factuel. Il ne recommence pas toute la première revue : celle-ci conserve l'examen des ressources, les reproductions, la génération identique et les limites des preuves de rendu.

### Utilité et représentation du système

| Carte | Ce qu'elle permet de comprendre | Appréciation |
|---|---|---|
| Système | Entrées, responsabilités, relations, autorité des sources et maintenance. | Bonne vue d'ensemble. Les publics et noms de guides restent ceux du paquet effectivement livré. |
| Parcours | De la demande à la proposition ou à la clôture, avec protections et retours. | Utile pour situer le travail ; son déroulement est une vue de lecture, à adapter à la tâche et au risque. |
| Boucle | Observer, diagnostiquer, modifier, réobserver, comparer et décider. | Utile pour relier jugement, intervention et observation ; elle rappelle l'arrêt et l'absence de quota de retouches. |

Les supports décrivent déjà le fonctionnement, et non la progression du chantier depuis octobre. Leur présence est donc cohérente avec une V1 centrée sur l'usage. Ils restent dérivés des sections propriétaires et ne remplacent ni ces sources, ni une preuve d'efficacité.

L'architecture reste utile : trois JSON pour le contenu, un gabarit HTML commun, un générateur et douze sorties (trois HTML, six SVG et trois Markdown). La fabrication de police et ses cinq ressources assurent légèreté, reproduction et licence. Le Markdown se lit directement sur GitHub, les SVG s'intègrent aux documents et les HTML servent la navigation interactive locale. Les sources, sorties et ressources ont des fonctions distinctes.

### SV-03 — Vérifié : la version affichée des cartes n'est pas contrôlée contre celle du paquet

- Sources externes : supports/systeme.json, ligne 2 ; supports/generer.py, lignes 54, 121, 179 et 192–228 ; supports/page.template.html, lignes 5, 19 et 27 ; scripts/validate_supports.py, lignes 19–36.
- La carte système utilise le champ version du JSON pour son SVG. Les SVG parcours et boucle portent V1.0.0 directement dans le générateur ; HTML et Markdown emploient aussi des mentions génériques de V1. La version n'est pas issue d'une identification commune du paquet.
- Reproduction sur une copie complète : changer uniquement la version de systeme.json en V1.0.1 expérimentale, puis régénérer. Les SVG système affichent V1.0.1 ; les SVG parcours et boucle restent V1.0.0 ; le manifest reste à 1.0.0.
- Le validateur des supports et la validation documentaire Local réussissent tous deux. La fraîcheur et les cibles sont vérifiées, mais cette divergence d'identification n'est pas rejetée.
- Le paquet actuel livré affiche des versions concordantes. Le constat reproduit porte sur une dérive possible lors d'une actualisation, pas sur une version déjà fausse dans la livraison originale.
- Piste : dériver l'identification des cartes depuis les métadonnées propriétaires du paquet, puis vérifier leur concordance. Une source JSON de présentation ne doit pas définir une version concurrente.

### Identification et contenu à actualiser

Aucune des douze sorties ne porte la révision R2026-10-11-CORRECTIFS. Les JSON ne déclarent ni révision ni date ; seul systeme déclare une version. Une carte extraite ou partagée seule ne permet donc pas de retrouver directement l'édition précise du système qu'elle représente. Il s'agit d'une limite de provenance à préciser pour les usages de partage, pas d'une preuve que le contenu actuel est périmé.

La recommandation est d'afficher une identification discrète et commune, avec version/révision et date liée à la source ou à la livraison concernée. Une horloge de génération variable à chaque build compromettrait les sorties déterministes ; l'actualisation doit dépendre d'un état de source identifié. L'ajout de texte demande également les vérifications de corpus de police et de poids déjà prévues.

Pour les évolutions discutées :

- Guides : conserver les noms actuels dans les supports tant que les fichiers ne sont pas renommés. Si Prise en main, Pratique et Pilotage sont intégrés, adapter les entrées et cibles de systeme.json, puis régénérer toutes les sorties concernées. Le libellé actuel « Je travaille en équipe » est plus restrictif que la fonction de pilotage accessible aussi à une personne seule.
- Agent : garder une présentation indépendante de l'hôte. Une nouvelle documentation d'installation peut être reliée lorsqu'elle existe ; le diagramme ne doit pas annoncer une intégration native multi-agent non vérifiée.
- Demande de jugement : rendre explicite que l'observation peut porter sur un artefact existant et que fabrication ou modification dépendent de la demande et du diagnostic. Les supports ne doivent pas faire interpréter les étapes dessinées comme une obligation de produire une nouvelle scène pour toute analyse. L'obligation de modifier sans gain attendu, déjà discutée dans GU-01 et SK-02, ne se résout pas par un diagramme.
- État public : actualiser les responsabilités, possibilités et liens effectivement intégrés. Les plans, essais et anciennes étapes restent dans le carnet et les archives, sans ajout d'une chronologie dans les cartes.

SV-01 reste le défaut de correspondance des relations entre JSON et dessin ; SV-02 reste la double ponctuation de deux pieds de carte. Aucun des fichiers concernés n'a changé depuis leur examen et ces observations ne sont pas corrigées. Générer des sorties fraîches ne garantit donc ni leur équivalence sémantique complète, ni leur identification cohérente avec le paquet.

### Vérifications de ce complément

- 24 fichiers de supports comparés au lot livré : tous identiques. Le contrôle courant des supports réussit.
- Sources de contenu, gabarit et passages d'identification du générateur relus ; absence de révision constatée dans les douze sorties.
- Divergence de version reproduite sur une copie isolée avec génération et deux validations réelles ; script, copie et résultats sous /workspace/work/revue-supports-etat. La source de référence n'est pas modifiée.
- Les preuves historiques de rendu et tests d'interaction de la première revue restent identifiées comme antérieurs. Aucun nouveau navigateur, test utilisateur ou téléchargement SVG n'est exécuté dans ce complément.

Les recommandations d'actualisation et SV-03 sont ajoutés au carnet. Les JSON et supports livrés ne sont pas modifiés pour afficher des changements encore proposés.

## README : entrée et état courant — complément

Relecture du 12 octobre 2026 : /workspace/presentation-v1-corrigee/README.md, 89 lignes, révision R2026-10-11-CORRECTIFS. Le fichier reste identique à celui de la première revue et du lot livré, empreinte 62b427e51245adfaaf486ac8f5115356b518962378df5eaf808e4046711561de. Ce complément confronte sa présentation aux discussions agent, guides, maintenance et supports ; il ne constitue pas une réécriture du README livré.

### Ce qui reste utile

Le README est déjà centré sur la fonction et l'utilisation du système. Il ne raconte pas la progression depuis le 1 octobre. Son statut expérimental est visible dès le début ; sa carte mène à une lecture texte, ses règles renvoient au propriétaire et ses limites distinguent validation documentaire, rendu observé et preuve d'usage. Ces fonctions sont pertinentes pour la page d'entrée.

Les liens actuels continuent de désigner le contenu réellement livré. La proposition de niveaux des guides, les nouvelles recettes d'installation et les corrections des générateurs ne sont pas intégrées ; le README ne doit pas les présenter comme disponibles avant leur réalisation.

### Adaptations à retenir

| Partie actuelle | Adaptation proposée | Raccord |
|---|---|---|
| Présentation, ligne 3 | Nommer conception, correction et jugement, puis expliquer l'apport concret. Distinguer une demande de création d'une analyse d'existant ; l'aboutissement demandé dépend de la tâche. | Discussion agent et SK-02 ; le README ne résout pas seul la portée des consignes de fabrication. |
| État, lignes 1–5 et 85 | Rendre version/révision et état vérifié visibles ensemble dès le début. La date d'actualisation doit correspondre aux informations réellement mises à jour ; aucune chronologie de chantier n'est nécessaire ici. | Clarification de l'utilisateur sur l'état actuel et factuel. |
| Entrées, lignes 7–18 | Organiser les trois guides par besoin et niveau de lecture si la proposition est intégrée : Prise en main, Pratique, Pilotage. Garder des entrées directes pour relecture, agent et maintenance, et le glossaire transversal. | Proposition des guides ; les niveaux ne remplacent ni les modes de travail ni les rôles. |
| Installation, lignes 20–28 | Distinguer reconnaissance de la skill, accès au paquet et vérification d'activation. Corriger première copie, mise à jour et renvois déplacés. Donner des instructions adaptées aux hôtes documentés, en précisant ce qui est testé. | RM-01 à RM-03 et AG-01/AG-02. |
| Cinq règles, lignes 30–42 | Conserver le résumé et son autorité explicite ; faire évoluer une règle dans sa source avant ses projections. Les principes servent l'orientation, avec les détails au bon endroit. | Source propriétaire de direction et contrôles de fidélité du bloc constitution. |
| Fonctionnement, ligne 46 | Décrire la fabrication et l'amélioration comme un parcours adapté à la demande. L'observation d'un objet existant et l'arrêt sans modification inutile doivent rester possibles. | SK-02, GU-01 et discussion des supports. |
| Organisation, lignes 48–71 | Garder la vue d'ensemble ; rendre explicite le rôle du dossier supports dans l'inventaire puisqu'il dispose désormais de douze sorties de présentation. Conserver l'autorité active des sections conservées. | Supports et discussion du nettoyage V1. |
| Vérifications et limites, lignes 73–89 | Donner les moyens utiles de consulter ou contrôler, et renvoyer vers un état de preuves attaché à la version concernée. Décrire les limites opérationnelles ayant une incidence sur l'usage, avec détails dans les documents dédiés. | RN-01/RN-02, défauts d'installation et distinction preuves anciennes/courantes. |

### Ordre proposé pour une mise à jour

1. Rôle du système et demandes couvertes.
2. État courant identifié : version/révision, statut et portée des faits constatés.
3. Choisir l'entrée selon son besoin et son implication dans le système.
4. Utiliser le système et installer la skill, avec une procédure complète retrouvable.
5. Comprendre l'organisation et consulter les trois cartes.
6. Principes essentiels et autorité des sources.
7. Vérifications disponibles, conditions d'usage et limites.
8. Références utiles vers guides, maintenance, état de version et notes de livraison.

Ce plan est une proposition de structure. Il garde une page d'entrée courte et reporte les détails vers leurs documents utiles. La mise à jour du README et des cartes devra suivre les changements effectivement intégrés, sans transformer notre revue et ses propositions en récit de livraison achevée.

Les cartes embarquées restent concernées par SV-01 et SV-03 : contrôler leur fraîcheur ne garantit pas toutes leurs relations ni leur identification. Il n'est pas constaté que la carte du README actuel représente une relation ou une version erronée ; ces défauts concernent la maintenance de cette correspondance lors d'un changement.

Vérifications : 20 occurrences de liens et attributs d'images, dont deux fragments Markdown, toujours valides ; fichier identique à la référence examinée précédemment. Les cinq usages du lecteur et les reproductions d'installation sont conservés dans la première revue et ne sont pas réexécutés sans changement des sources. Résultats de cette relecture et ordre proposé sous /workspace/work/revue-readme-etat/resultats.json.

La recommandation d'actualisation est ajoutée au carnet. Le README de la copie de référence n'est pas modifié dans ce complément.

## Release notes : livraison et faits vérifiés — complément

Relecture du 12 octobre 2026 : /workspace/presentation-v1-corrigee/RELEASE_NOTES.md, 53 lignes, révision R2026-10-11-CORRECTIFS. Le fichier est toujours identique au lot distribué et à celui de la première revue. Les huit liens locaux, dont le fragment d'installation, restent valides. Les deux liens CI sont externes ; leurs identifiants et résultats ont été rapprochés des archives lors de la première revue, sans nouvelle interrogation GitHub dans ce complément.

### Rôle dans la présentation actuelle

Le README oriente vers l'utilisation du système. Le document versions identifie l'état courant du paquet. Les release notes décrivent une livraison précise : contenu effectivement livré, changements utiles, compatibilité, vérifications et limites. Elles restent attachées à cette version et à ses artefacts ; une nouvelle livraison doit être identifiée comme telle plutôt que confondue avec les anciennes.

Cette fonction est compatible avec la priorité de l'utilisateur : la page publique présente d'abord la livraison concernée et ses faits vérifiés. La progression du chantier depuis le 1 octobre et les noms de phases ne doivent pas occuper son récit principal.

### Adaptations à retenir

| Contenu actuel | Actualisation proposée |
|---|---|
| En-tête avec version initiale du 1 octobre | Mettre en tête la livraison concernée, sa version/révision, sa date réelle et son statut. Conserver la date initiale dans les archives, sans en faire le repère principal de la page courante. |
| Ce que permet la V1 | Résumer l'usage et renvoyer au README pour l'orientation complète. Distinguer création, correction et jugement lorsque les adaptations correspondantes sont réellement intégrées. |
| Ce qui change dans cette présentation | Décrire les différences réellement intégrées à cette livraison, depuis une base clairement identifiée. Ne pas transformer les propositions du carnet en nouveautés déjà disponibles. |
| Comparaison des tailles PRATIQUE et PHASE5 | Donner la taille actuelle mesurée si elle est utile ; déplacer la progression détaillée dans les archives. La taille de 18 971 octets reste vérifiée pour CORRECTIFS, pas pour une livraison future modifiée. |
| Installation et noms de guides | Garder un lien vers la procédure correspondant au paquet livré. Actualiser les noms et le support des hôtes après mise en œuvre, en précisant le périmètre effectivement testé. |
| Contrôles inclus | Distinguer commandes disponibles et contrôles réellement exécutés. Rendre explicite la portée différente des paquets GitHub et Local, conformément à RN-01. |
| CI citées | Attacher les résultats à la version, au commit testé et à la date d'observation. Les CI 55/56 sont antérieures aux correctifs ; les preuves archivées 57/58 concernent b3e071b. Réinterroger les résultats nécessaires avant d'annoncer un état de CI actuel. |
| Attestation et limites | Conserver les limites de RUN_CARD et de l'efficacité générale. Indiquer les problèmes connus qui affectent l'usage de cette livraison et mettre à jour leur état seulement après correction et vérification. |

Les annonces matérielles de CORRECTIFS déjà vérifiées restent concordantes : trois cartes et 24 fichiers de supports présents dans les deux archives, police réduite, alias SYSTEME et deux titres du noyau modifiés sans changement des consignes. La première revue conserve les contrôles de taille, d'inventaire, de compilation et de refus des supports. Ils ne sont pas relancés pour un texte et des fichiers inchangés.

RM-01 à RM-03 restent pertinents pour la procédure liée ; SV-01 et SV-03 restent des limites des contrôles de correspondance et d'identification des supports. Les phrases annonçant génération commune, fraîcheur et cibles ne doivent pas être lues comme une certification de toute équivalence sémantique ni de toute cohérence de version. Aucun de ces constats n'est annoncé comme corrigé dans ce complément.

La structure envisagée est courte : identification de la livraison ; contenu et changements intégrés ; installation/compatibilité ; vérifications avec leurs résultats et périmètres ; problèmes connus et limites ; liens vers le README et l'état de version. Les étapes de revue, essais et anciennes progressions restent dans le carnet et les archives.

Les comparaisons et références de cette relecture sont conservées sous /workspace/work/revue-release-notes-etat/resultats.json. La recommandation est ajoutée au carnet ; les release notes de la copie de référence ne sont pas réécrites à cette étape.

## Réserves répétées, briefs et runs — discussion

Discussion du 12 octobre 2026, sur la copie CORRECTIFS. L'utilisateur signale deux gênes liées : les rappels que le système n'est pas testé, vérifié ou utilisé, et l'insistance à vouloir lancer des runs ou produire des briefs. L'objectif de la revue reste de lire, comprendre et vérifier les enjeux utiles ; une nouvelle création n'est pas un passage obligé pour y parvenir.

### Constats documentaires

- Répétition vérifiée : README, ligne 86 ; release notes, lignes 49–51 ; versions, lignes 17, 43 et 59 ; guide equipe, lignes 3, 248 et 261. Ces passages portent sur des périmètres différents, mais leur cumul peut faire entendre une réserve générale et permanente.
- Les textes relus n'affirment pas que le système n'a jamais servi ou qu'aucun contrôle n'a été réalisé. Le document versions mentionne des créations et jugements exploratoires ; les revues précédentes consignent des contrôles exécutés. L'absence de mesure comparative d'efficacité générale ne doit pas être reformulée en absence de tout usage ou de toute vérification.
- Le format de réponse est imposé en quatre rubriques dans agent/repondre, lignes 22–28, et repris dans la skill, lignes 84–90. « Ce qui manque pour la vraie version » et « La suite » peuvent encourager une liste de manques ou une relance, même lorsqu'une explication ou une analyse répond déjà à la demande.
- La description de la skill inclut construire, corriger ou juger ; son noyau commun exige cependant « Construis la première scène », ligne 82. Le guide equipe demande aussi « le rendu est construit dans tous les cas », ligne 49, dans le passage consacré au lancement créatif et au brief vague. La portée de ces consignes mérite d'être explicite pour ne pas les appliquer à un jugement seul. Ce point prolonge SK-02 et GU-01.
- Des protections existent déjà : trace proportionnée au risque ; modules chargés seulement s'ils peuvent modifier une décision ; absence de nouveau protocole si la preuve ne change rien (agent/chemins, lignes 12 et 183) ; alternative conditionnelle (standard, ligne 57). Elles doivent être cohérentes avec les formulations communes de fabrication et de sortie.

La répétition et les prescriptions de format sont constatées dans les fichiers. Leur effet systématique sur le comportement d'un agent n'est pas établi par cette lecture ; le retour de l'utilisateur décrit la gêne vécue et indique une priorité de correction.

### Orientation retenue pour les adaptations

1. **Partir de la demande.** Lire, expliquer, discuter ou analyser peut constituer un résultat complet. Déterminer la nature du travail avant d'appliquer un mode de fabrication ; une revue d'existant n'implique pas de fabriquer une nouvelle scène, une variante ou un prototype.
2. **Rendre le cadrage proportionné.** Utiliser l'objectif, le contexte et les éléments déjà fournis. Demander une information supplémentaire seulement si elle peut changer le travail ou la décision. Le brief est un moyen de clarifier une production ; il ne devient pas un document ou un formulaire à produire systématiquement.
3. **Adapter la réponse.** Exposer le résultat, les raisons utiles et les limites qui affectent effectivement son utilisation. Omettre une rubrique sans contenu pertinent. Une analyse terminée peut se terminer sans proposition de nouveau run ni rubrique « vraie version ».
4. **Préciser la portée des réserves.** Distinguer contrôles du paquet, observations sur une production particulière et mesure d'efficacité générale. Présenter les faits positifs disponibles avec leurs limites. Une absence de test sans rapport avec la demande n'est pas un manque à rappeler dans chaque réponse.
5. **Placer les informations au bon endroit.** Maintenir une présentation courte du statut dans les pages d'entrée qui doivent pouvoir se lire seules ; regrouper le détail des preuves et limites dans une référence identifiable. Dans une réponse de travail, signaler une limite lorsqu'elle affecte la conclusion ou la prochaine décision, sans réciter l'état général du système.
6. **Limiter les formalités à leur fonction.** Une trace complète sert une reprise, une acceptation ou un audit lorsque ces besoins sont présents. Une conversation ou la conservation d'une note d'analyse ne doit pas automatiquement devenir un run de production. Préciser cette frontière avec SK-03. Conserver l'honnêteté des contrôles réellement applicables ; ne pas exiger de nouveaux essais uniquement pour combler une liste générique de preuves.

La modification éventuelle doit porter sur les sources propriétaires de classification, de fabrication et de réponse, puis sur leurs projections compilées et leurs guides. Changer seulement le README ou supprimer les mentions de limite ne réglerait pas les consignes qui déclenchent cette insistance.

Critère de revue pour la future adaptation : une demande d'explication ou d'analyse reçoit une réponse complète, sans création imposée, brief artificiel ni relance automatique ; une limite déterminante reste clairement nommée. Une demande de production conserve les contrôles adaptés à son objet et à son risque.

Cette priorité est ajoutée au carnet. Les consignes du paquet restent à adapter dans une étape de modification ; la présente discussion ne lance aucun brief ni run créatif.
