# ACTION — Pipeline de livraison & preuves

**Design Governance V1 — expérimentation maintenue.** Cette V1 est un cadre de travail en évaluation ; elle n’est pas présentée comme une release publique stabilisée. Ses limites, preuves et conditions d’usage restent explicites. ACTION transforme une direction ou une décision produit en trace de run, artefacts observables, preuves adaptées, gates proportionnés et verdicts inspectables.

## Responsabilité

`ACTION` est le propriétaire des preuves exécutables, des gates, des statuts de run, des verdicts et de la clôture. Dans un run, le chargement suit `DIRECTION/CHARGE`, seule liste de chargement. Pour lire ACTION hors run, commencez par `ACTION/STATUS` et `ACTION/PRECONDITION`, puis la route de votre mode `ACTION/RUN-<MODE>`, et chargez seulement les gates correspondant au risque déclaré. `ACTION/FAST-PATH` est une vue de formalité réduite pour un delta local ; il ne supprime ni la preuve requise ni l’honnêteté du statut.

**Capacité positive d’ACTION.** ACTION ne sert pas seulement à filtrer ou accepter un résultat : elle transforme une direction en livraison observable et améliorable. Son chemin positif est la boucle d’édition (`DIRECTION/DOUBLE-LOOP`), prolongée par la preuve et, en trace complète, par une clôture avec une limite et une prochaine preuve. Les gates protègent ce chemin ; ils ne sont pas sa finalité. La qualité du premier rendu, la lisibilité de la décision et la possibilité de reprendre le run font partie de la valeur livrée.

### Carte de lecture par mode

La liste de chargement de chaque mode est `DIRECTION/CHARGE`, la seule du corpus ; la skill en porte une copie compilée. Cette section ne la répète pas : elle précise seulement ce qui s’ajoute selon la trace.

**Socle pour tous les modes :** `ACTION/STATUS` et `ACTION/PRECONDITION`, dès que le run écrit un statut, un gate ou un verdict (trace complète) ; `DIRECTION/CHARGE` reste la liste du démarrage.

Le paquet de sortie de chaque mode est défini par `ACTION/CLOSE-PACKAGE` ; `ACTION/RUN-DIRECTION` (ancrages) et `ACTION/RUN-SYSTEM` (`closure.system_package`) en précisent le détail.

Les sections `RUN_CARD`, `CLOSE-PACKAGE` et `CLOSE-EXIT-CHECK` s’ajoutent lorsque la trace est persistante ou que la clôture l’exige. `FAST-PATH` n’est pas une sixième voie : chaque occurrence de ce nom reste une vue locale du propriétaire qui l’emploie.

### ACTION/HANDOFF — sortie minimale commune

`ACTION` est propriétaire de la preuve, des gates, des statuts, des verdicts et de la clôture. Une sortie de run a deux formes, à ne pas confondre. Les façades peuvent les préparer ou les recopier, jamais les redéfinir.

1. **Handoff**, pour une reprise ou un run persistant : les éléments suivants doivent être résolubles.

```text
MODE — DECISION — RISK — SCOPE — ARTIFACT
OBSERVATION/METHOD — PROOF/TRACE-LOCATOR — LIMIT/NOT-VERIFIED
DECISION-CHANGE — NEXT-ACTION — OWNER — NEXT-PROOF — EXIT-CONDITION
```

2. **Réponse visible**, pour un humain, par défaut :

<!-- noyau:début SORTIE -->
<!-- concept:SOR-01 -->
La personne reçoit une réponse en langage produit, sans le jargon interne du système, en quatre rubriques :

```text
Ce que j’ai fait : la proposition et ses choix principaux, en une ou deux phrases.
Pourquoi : la thèse, l’alternative écartée et ce que le rendu permet de décider.
Ce qui manque pour la vraie version : contenus, assets, droits, tests ou capacités, avec le plafond atteint.
La suite : une ou deux actions proposées, et ce qu’il faut de la personne pour les engager.
```

L’agent active le système en silence : la personne donne l’objectif, le périmètre et l’autonomie ; l’agent choisit le mode, charge les sources et tient la trace. Le mode, la conséquence décisionnelle d’`ACTION/STATUS` (décision changée, confirmée ou abandonnée, `N/A-JUSTIFIED` ou `NOT-OBSERVED`), la preuve et l’owner restent dans la trace et sont exposés sur demande (« pourquoi ? », « qu’as-tu vérifié ? »). Les codes de route, de concept et de statut n’apparaissent dans la réponse visible que si la personne travaille sur le système lui-même ou les demande explicitement ; quand la trace est écrite dans le fichier livré, la réponse ne la recopie pas sauf demande explicite. Les limites de vérification qui affectent l’usage ou la décision restent visibles, même lorsque la trace est persistée. La réponse visible ne remplace jamais le handoff d’un run persistant.
<!-- noyau:fin SORTIE -->

3. **Niveau de trace**, choisi par l’agent :

<!-- noyau:début TRACE -->
<!-- concept:TRA-01 -->
**Trace légère par défaut.** Hors run persistant, partagé ou audité, la trace tient en six lignes au plus : mode ; thèse (promesse → objet de preuve → geste) ; modal, trame et parti ; plafond atteint et contenus marqués ; défaut dominant restant ; prochaine preuve. Lorsque la qualité perceptuelle est une décision du run, la ligne du défaut dominant résume la revue de `SAVOIR/CRAFT/CFT-00` : ce qui retient, ce qui reste générique, puis le geste de `SAVOIR/STATE` appliqué et réinspecté, ou seulement envisagé, ou la raison de conserver. Elle s’écrit à côté de l’artefact quand l’agent écrit des fichiers (fichier de trace ou en-tête du fichier livré) ; sinon, après la réponse visible, sous « Trace ». Les planchers s’appliquent pendant la fabrication (vérité, `ACTION/GATE-A` selon le profil de surface, boucle d’édition) ; seule leur écriture s’allège. Le run livre une **proposition** `EXPLORATORY` : ni verdict, ni acceptation, ni clôture, ni `RUN_CARD`. **Trace complète** (handoff, paquet de clôture, gates écrits et projection selon `ACTION/CLOSE-PACKAGE`, `B1b` dans son scope) si le run est persistant, partagé, audité, ou si une acceptation ou une clôture est demandée. La forme courte LITE conserve une trace complète sans RUN_CARD (`ACTION/HANDOFF`).
<!-- noyau:fin TRACE -->

**Formes.** La ligne de run de `DIRECTION` est la mémoire de lancement, sous-ensemble de lancement de ce handoff ; le handoff est la transmission ; `ACTION/CLOSE-PACKAGE` est la clôture par mode ; la `RUN_CARD` JSON est la projection persistante, selon la table de correspondance d’`ACTION/RUN_CARD`. **Forme courte LITE** (trace complète d’un `LITE` clôturé sans `RUN_CARD`, distincte de la trace légère, qui ne clôture pas) : le paquet LITE de `ACTION/CLOSE-PACKAGE` ; les autres champs du handoff sont `N/A-JUSTIFIED` par défaut, avec deux pertes déclarées (METHOD, EXIT-CONDITION) ; TRACE-LOCATOR est alors l’artefact. Une reprise par un autre agent exige OWNER et NEXT-ACTION ; sinon la forme courte reste une préparation.

Le handoff réutilise les champs existants ; il ne crée ni statut, ni gate, ni nouveau schéma. Les champs non applicables sont marqués `N/A-JUSTIFIED`. Un run persistant utilise la projection `RUN_CARD` et son validateur, sauf la forme courte LITE définie ci-dessus : sa trace complète persiste dans l’artefact selon `ACTION/CLOSE-PACKAGE`. Cette exception ne dispense ni des preuves dues ni des conditions de reprise ; une demande de projection structurée requiert la `RUN_CARD` validée. Une sortie courte qui ne fournit pas le paquet applicable reste une préparation, une clarification ou une décision non clôturée.

**Condition d’arrêt de lecture :** arrêter lorsque le mode, le risque, la route, la preuve, la limite, le propriétaire et la prochaine action sont connus. Charger un registre, une route ou un gate supplémentaire uniquement s’il peut modifier l’un de ces éléments.

### Parcours minimal

Le parcours d’un run est celui du noyau de la skill : classer et charger (`DIRECTION/CHARGE`), prendre le brief, construire une première scène complète, boucler (`DIRECTION/DOUBLE-LOOP`), répondre et tracer (`ACTION/HANDOFF`). ACTION en porte les preuves, les gates et, en trace complète, la clôture ; ses contrats restent applicables dès que le risque ou le mode les déclenche.

## ACTION/FAST-PATH — preuve minimale sans rituel

Pour `LITE` et les petits `ITER`, arrête le protocole après quatre réponses : décision ou delta touché ; risque dominant et son owner ; preuve la moins coûteuse (capture, diff, test, scénario, mesure ou comparaison) ; conséquence si la preuve est positive ou négative, avec condition d’arrêt et prochaine action ; puis, en trace complète, clôture avec le paquet de son mode : forme courte LITE pour `LITE`, paquet `ITER` pour un `ITER` (`ACTION/CLOSE-PACKAGE`) ; en trace légère, la proposition suffit.

Si aucune décision ne peut changer, n’ajoute pas de capture, comparaison ou route uniquement pour remplir le paquet. Journalise `N/A-JUSTIFIED` lorsque la procédure ne peut rien modifier.

Reviens à un mode plus riche si le changement touche une règle partagée, l’identité, une décision coûteuse, ou un risque critique de tâche, de santé, de sécurité, de confidentialité, de permission ou d’accessibilité (Protection de niveau de `DIRECTION/START`). Un fix local de contraste, libellé, focus ou wrapping qui conserve la direction reste `LITE`.

---

## ACTION/RUN — routes d’exécution

Les blocs `RUN-*` donnent l’entrée, la sortie et le contrôle minimal de chaque mode. Les sections détaillées ci-dessous sont canoniques lorsque le bloc les appelle. Le contrat ACTION minimal de chaque mode est dans `ACTION/PRECONDITION`.

### `ACTION/RUN-LITE`

**Entrée.** Système et direction retrouvables ; delta local ou fix ; décision dominante connue.

**Faire.** Écrire la ligne de run, déclarer `DECISION-INTENT`, modifier, contrôler les gates A applicables et obtenir une preuve B du risque dominant. Charger `SAVOIR` ou `BIBLIOTHEQUE` uniquement si cela peut changer le correctif. Une alternative n’est documentée que si un choix plausible peut modifier le delta ou le risque.

**Sortie.** Paquet `LITE` d’`ACTION/CLOSE-PACKAGE`. Trace légère : la proposition (`ACTION/HANDOFF`).

**Clôture.** En trace complète, passer à `DECIDED`, puis `CLOSED`. Reclassifier en `SYSTÈME` si une règle partagée est touchée, en `ITER` si la direction précédente doit être réévaluée ou en `DIRECTION` si une nouvelle décision identitaire apparaît.

### `ACTION/RUN-ITER`

**Entrée.** Direction, composants, tokens et périmètre précédent retrouvables dans la trace légère (ligne de thèse), la `RUN_CARD`, le manifeste ou le projet. Dans une `RUN_CARD`, le rappel de direction est porté par `direction.thesis` et la trace par `trace_locator`.

**Faire.** Rappeler la direction en une phrase, déclarer `DECISION-INTENT`, appliquer le delta et vérifier la non-régression pertinente : visuelle, fonctionnelle, responsive, typographique ou systémique.

**Sortie.** Paquet `ITER` d’`ACTION/CLOSE-PACKAGE`. Trace légère : la proposition (`ACTION/HANDOFF`).

**Clôture.** En trace complète, passer à `DECIDED`, puis `CLOSED`. Utiliser `RETURNED` si une preuve ou correction doit être reprise dans le même mode, `RECLASSIFIED` si l’identité, la portée ou le système sont remis en cause.

### `ACTION/RUN-STANDARD`

**Entrée.** Écran ou flow nouveau, sans charge identitaire autonome ni blast radius systémique.

**Faire.** Cadrer le JTBD et la décision dominante. Appeler `BIBLIOTHEQUE/SELECT` si support, grille, scène ou objet restent ouverts. Produire dès le premier rendu une composition jugeable : contenu crédible, hiérarchie, typographie appropriée, états pertinents, responsive applicable et détail de finition utile. Exécuter les Gates A et B ciblés. Utiliser une ancre visuelle seulement lorsqu’une direction locale, une matière, une composition ou une comparaison perceptuelle le rend utile.

**Sortie.** Paquet `STANDARD` d’`ACTION/CLOSE-PACKAGE`. Trace légère : la proposition (`ACTION/HANDOFF`).

**Clôture.** En trace complète, passer à `DECIDED`, puis `CLOSED`. Passer à `EXPLORATORY` si une preuve requise manque, à `RETURNED` si une correction doit être reprise dans le même mode ou à `DIRECTION` si la surface devient identitaire.

### `ACTION/RUN-DIRECTION`

**Entrée.** Identité, surface de marque, premier contact ou hypothèse de direction autonome.

**Faire.** Exécuter le pipeline `ACTION/PIPELINE-DIRECTION` : positions distinctes lorsque la décision est ouverte, alternative située lorsque nécessaire, ancre utile, `DIRECTION/VISUAL_TARGET`, spec, checkpoint si nécessaire, build de la première scène significative, `ACTION/VISUAL_PROOF`, capture et comparaison. La première scène significative doit être présentable par défaut : elle porte déjà la direction, la hiérarchie, la typographie, la composition, la palette, la matière ou l’asset pertinent, les composants authored nécessaires et un niveau de finition suffisant pour juger la proposition comme un objet réel plutôt qu’un wireframe générique. Les détails sans rôle produit restent exclus. Lorsque la direction est nouvelle, ambiguë ou exposée à la convergence générique, le sourcing Web ou documentaire est recommandé ; s’il soutient un claim, une tendance, une provenance ou une décision non fondée en mémoire, il devient une ancre à ouvrir, dater, borner et transformer.

**Sortie.** Paquet `DIRECTION` d’`ACTION/CLOSE-PACKAGE`. En trace légère (`ACTION/HANDOFF`), la réponse visible et la trace légère en tiennent lieu. Pour chaque ancrage mobilisé, distinguer si nécessaire son rôle de direction, de production ou de vérification, les attributs retenus et rejetés, la transformation effectuée et les limites de transfert ; une référence Web n’est ni une preuve de réussite, ni une autorisation de copie.

**Clôture.** En trace complète, passer à `DECIDED`, puis `CLOSED` lorsque l’artefact et la trace sont persistés : `CLOSED` ne dit pas que la direction est tenue (`ACTION/STATUS`). Le résultat se déclare à part : une direction tenue, preuves applicables déclarées, peut recevoir un verdict accepté ; sinon, l’issue est `RETURNED`, `EXPLORATORY`, `FAIL-ASSUMED` (échec connu) ou `ESCALATED`, avec le verdict `RETURN-DIRECTION` si la direction doit être reprise, selon la preuve et le risque.

### `ACTION/RUN-SYSTEM`

**Entrée.** Règle, token, composant, convention, dépendance ou format partagé affecté.

**Faire.** Cartographier l’impact et les consumers. Nommer la décision, l’owner, la migration, le rollback et les tests de non-régression. Consulter `CHANGELOG.md` avant adoption, pilotage ou dépréciation. Si le changement touche ACTION ou un contrat connexe, le clore par la recette documentaire `ACTION/MAINTENANCE`.

**Sortie.** Paquet `SYSTÈME` d’`ACTION/CLOSE-PACKAGE`. Trace légère : la proposition (`ACTION/HANDOFF`). Dans une `RUN_CARD` acceptée, ces éléments forment `closure.system_package` : impact, consumers, owner, migration, rollback, non-régression (claim et baseline : locator, version, état) et référence CHANGELOG.

**Clôture.** En trace complète, passer à `DECIDED`, puis `CLOSED` lorsque consumers et réserves sont traçables. Passer à `ESCALATED` si owner, droit, décision externe ou risque externe manque.

---

## ACTION/PIPELINE-DIRECTION — direction vérifiable

Ce pipeline s’applique au mode `DIRECTION`. Il vise une direction réellement choisie, non un catalogue de variantes.

`DIRECTION/DOUBLE-LOOP` décrit la boucle d’édition, seule description de la boucle (copiée dans le noyau). `ACTION/PIPELINE-DIRECTION` décrit son exécution livrable : préparer, construire, produire la preuve, appliquer les corrections, comparer et clôturer ou retourner. `ACTION/GATE-B/B1b` est un contrôle spécialisé déclenché dans ce pipeline lorsque son scope est actif ; ces trois niveaux ne sont pas trois boucles concurrentes.

### Boucle de qualité et branche one-shot

Pour tout run qui produit un rendu, la boucle est celle de `DIRECTION/DOUBLE-LOOP` ; ce pipeline en exécute la préparation, la preuve, puis la clôture ou le retour. Observe le rendu réel sans te laisser guider par la rationale.

La branche `one-shot` est une exécution raccourcie de cette même boucle, jamais une suppression de la boucle. Elle permet de clôturer après l’observation initiale lorsque le premier rendu atteint la qualité attendue du mode, que la direction est identifiable, que les risques applicables sont couverts et qu’aucune amélioration utile n’est probable. Si le premier rendu est faible, générique ou incomplet, la branche one-shot ne s’applique pas : corrige, retourne ou déclare honnêtement la limite. Sur une surface `DIRECTION` acceptée avec V positif, l’arrêt suppose `ACTION/GATE-B/B1b` fait ou l’un de ses deux motifs `N/A-JUSTIFIED` ; la comparaison peut confirmer la décision initiale (`confirmed`). En trace légère, la proposition reste `EXPLORATORY` et B1b ne s’applique pas.

### 1. Situer les positions

Lorsque la décision est ouverte, formule des positions distinctes sur les axes pertinents : structure, matière, voix, temporalité, densité, rapport texte/image, rythme ou émotion traduite en levier visuel.

Il n’existe aucun quota obligatoire de directions. Une position retenue et une alternative située suffisent lorsque le risque dominant et les tensions sont déjà clairs.

La projection `creative_direction_set` de `gouvernance/schemas/production_contracts.schema.json` est conditionnelle : elle décrit une comparaison lorsqu’une décision ouverte et une alternative plausible la rendent utile. Si elle est produite, au moins deux positions distinctes matérialisent cette comparaison ; aucun plafond de directions n’est imposé. Ce minimum de structure du contrat ne demande ni variantes ni builds supplémentaires aux autres runs. Les qualités prioritaires de CREATIVE-BOOT sont un foyer de construction distinct du nombre de positions.

### 2. Traduire l’émotion

Une émotion n’est une direction que lorsqu’elle change une décision visible : composition, contraste, densité, échelle typographique, rythme de motion, contenu, relation texte/image ou traitement matériel.

« Premium », « chaleureux » ou « dynamique » sont des intentions à traduire, non des options de design autonomes.

### 3. Développer une alternative située

Le déclenchement appartient à `DIRECTION` (« Direction divergente ») et les leviers à `SAVOIR/CRAFT/CFT-02`. En trace complète, avant le build, la trace du run (retrouvable par `trace_locator`) nomme la position retenue, l’alternative considérée, la raison de son niveau de matérialisation et la preuve attendue ; la projection JSON ne porte pas ce paquet (voir `ACTION/RUN_CARD`). En trace légère, la première proposition nomme l’alternative écartée (checkpoint, étape 7).

Matérialise l’alternative seulement au niveau nécessaire pour comparer la décision : phrase, schéma, cible ou rendu. Ne construis pas une variante qui ne peut modifier aucune décision. Si aucune alternative située ne change raisonnablement le choix, note cette condition et passe à la spec après avoir nommé la raison.

### 4. Produire la spec visuelle

Une spec visuelle synthétique existe avant le premier code ou rendu d’une surface `DIRECTION`. La définition des voies `ANCHOR-GENERATED`, `ANCHOR-OBSERVED` et `ANCHOR-PROVIDED` appartient à `DIRECTION/VISUAL_TARGET` ; ACTION en conserve seulement la trace opératoire : type et identifiant de l’ancre, cible ou hypothèse, attributs observés, éléments retenus et rejetés, contre-indications, limites de transfert et preuve attendue.

`ANCHOR-GENERATED` reste une hypothèse visuelle comparable, non une calibration externe suffisante par défaut. Lorsque l’enjeu identitaire est élevé, accompagne-la d’une référence observée, d’une contrainte réelle ou d’une réserve explicite sur l’absence de calibration externe.

La spec décrit uniquement les décisions utiles : structure, hiérarchie, relation texte/preuve, traitement perceptible, typographie lorsque pertinente, contenu réel, actions, états, contre-indications et palette lorsque la couleur porte une décision.

Une ancre est utile seulement si elle apporte une décision structurelle ou perceptuelle, une contre-indication et une liste d’attributs retenus, rejetés et non transférables.

Sans ancre utile et spec exploitable, les axes concernés sont `NOT-VERIFIED`. Le run devient `RETURNED`, `EXPLORATORY` ou `ESCALATED` selon le périmètre ; `FAIL-ASSUMED` ne vaut que pour un échec connu (`ACTION/OVERRIDE`), jamais pour une ancre absente.

Dans une `RUN_CARD`, chaque ancre porte son `type` (`generated`, `observed` ou `provided`) et une date ISO ; `direction.identity_stake` déclare l’enjeu identitaire (`high` ou `normal`). Lorsque l’enjeu est élevé, que toutes les ancres sont générées et que la direction est tenue, `direction.calibration` nomme sa base : `real_constraint`, ou `generated_only_reserved`, qui interdit `ACCEPTED`. Une revue indépendante n’est pas une base de calibration. Une ancre manquante se sérialise par l’issue — ancres vides, issue non nulle, aucun verdict accepté —, jamais par une ancre inventée.

### 5. Sourcer et tracer

Trace dans la `RUN_CARD` ou le manifeste les références, requêtes, images ou assets réellement observés, avec leur rôle et leur statut. `BIBLIOTHEQUE.md` fournit des structures de décision ; il ne devient ni ancre visuelle, ni source d’asset, ni preuve de comparaison.

Pour toute recherche substantielle, distingue : `VERIFIED-THIS-RUN`, `MODEL-KNOWLEDGE-NOT-RECHECKED` et `USER-SOURCED-NOT-RECHECKED`. Les claims mesurés, datés, réglementaires ou dépendants d’un outil portent source, date, portée et limite dans la trace locale du run ; ils ne deviennent partagés qu’après décision de gouvernance.

Pour un asset directeur, trace aussi la route `CODE-NATIVE`, `FOURNI`, `CURATÉ`, `GÉNÉRÉ-DIRIGÉ` ou `HYBRIDE`, sa raison, son traitement prévu, ses droits ou incertitudes et l’alternative refusée. Une requête ou un prompt ne prouve pas qu’un asset est adéquat : observe l’asset à son ratio, son crop, son contraste et son voisinage de texte réels.

### 6. Sélectionner contre la facilité

Si plusieurs solutions restent plausibles, nomme ce qui distingue le choix retenu. Si la solution est la plus simple à implémenter, défends-la par le JTBD, le risque, les droits, la performance, la maintenance ou une contrainte réelle.

> La faisabilité immédiate n’est pas une preuve d’appropriation.

### 7. Écrire la direction et demander une décision si nécessaire

Écris la direction retenue en une phrase : position, intention, décision dominante et contrainte servie. Compare-la à l’alternative située et formule l’avantage vérifiable du choix.

<!-- noyau:début CHECKPOINT -->
<!-- concept:CHK-01 -->
**La première proposition vaut checkpoint.** Construis la première scène, puis présente-la avec sa thèse, l’alternative écartée et ce qu’il faut décider ; la personne valide, réoriente ou arrête. Valider oriente la suite (affiner, décliner, préparer la vraie version) ; ce n’est pas une acceptation. Pour retenir la direction pour un produit réel, la personne le demande : le run passe en trace complète, avec ancre observée ou fournie, gates et verdict (absolu 2 de `DIRECTION`). Jusque-là, la proposition reste `EXPLORATORY`. Un checkpoint avant le build n’est requis que si la personne l’a demandé ou si le build engage une action irréversible ou coûteuse (publier, envoyer, payer, consommer des crédits, écraser un existant, engager l’owner). Une marque, un public ou une hypothèse nouvelle est nommée dans la proposition ; elle ne bloque pas le build.
<!-- noyau:fin CHECKPOINT -->

Si un checkpoint préalable est requis et que l’autorisation manque, n’engage pas le build : applique `ACTION/AUTHORITY` (exploratoire, retourné ou escaladé). L’absence de regard externe est une autre question : déclare-la et compense-la par capture, comparaison, réserve et prochaine preuve ; cette compensation n’autorise rien.

### 8. Vérifier le rendu réel

Après le build, capture le rendu et compare-le à la spec. Pour chaque écart significatif, nomme l’observation, la cause probable, l’effet sur la tâche ou la direction et l’issue : `CORRECTED`, `ACCEPTED-DIFFERENCE` ou `REMAINING-RISK`. Ces valeurs sont des résultats locaux de comparaison, pas des statuts : `CORRECTED` se traduit par une conséquence décisionnelle `CHANGED` avec la nouvelle preuve ; `ACCEPTED-DIFFERENCE`, par `HELD-WITH-ACCEPTED-DIFFERENCE` et une réserve ; `REMAINING-RISK`, par une réserve. Inspecte en priorité la structure, la hiérarchie, la typographie, la composition, la spécificité, la qualité des assets, les composants authored, les états et la cohérence de finition ; ne corrige pas un défaut structurel par un effet décoratif terminal.

### Passe créative et polish

Lorsque la qualité perceptuelle est une décision du run, effectue après la première scène la revue créative définie par `SAVOIR/CRAFT/CFT-00` (Creative Quality Review), puis une repasse ciblée avant la clôture. ACTION en fixe le moment et la trace ; la revue ne produit ni score esthétique ni statut concurrent. Elle vérifie aussi si le premier rendu atteignait déjà la qualité attendue du mode, ou si la boucle est en train de réparer une préparation insuffisante.

La repasse examine les rapports entre masses, vides, échelles, rythme, typographie, matière, lumière ou profondeur, contenu, objet de preuve, états, responsive, transitions et détails de finition. Elle corrige d’abord le défaut dominant avec l’activation de `SAVOIR/STATE` ; la trace existante relie observation initiale, geste appliqué, condition, effet réinspecté et décision de conserver, ajuster ou retirer. Une capacité manquante reste une limite de preuve, pas un effet observé. Ajouter des effets, des variantes ou des assets sans améliorer une relation observable ne constitue pas une passe de polish.

Pour un run `DIRECTION`, la clôture créative doit pouvoir répondre à quatre questions : **quelle présence est effectivement produite, quelle signature rend la proposition spécifique, quel détail ou état montre le niveau de craft, et quel défaut reste prioritaire ?** Les réponses citent le rendu ou un objet inspectable et restent distinctes des preuves d’usage, d’accessibilité et de robustesse.

La comparaison vérifie notamment silhouette, opération dominante, matière/asset, typographie, objet de preuve, états et retenue. « Plus beau », « plus premium » ou « ressemble à la référence » ne sont pas des observations suffisantes.

Lorsque le risque visuel ou identitaire le requiert, la preuve doit être représentative de l’artefact construit et de son scope : elle montre, selon la décision, hiérarchie, composition, typographie, matière, spécificité, cohérence, retenue, états et résolution réelle. Une capture idéale ne masque pas un état, un viewport, un contenu ou un comportement non inspecté. La trace peut qualifier le niveau de craft observé — `Correction`, `Précision` ou `Intention` — mais cette qualification reste une lentille locale de jugement ; elle ne devient ni un score esthétique, ni un verdict global, ni un statut de direction. Une qualité visuelle observée ne prouve pas à elle seule la fidélité de la direction, la réussite d’usage, l’accessibilité ou la robustesse technique.

Retourne à la direction, à l’ancre, à la spec ou au build lorsque l’écart dominant persiste, lorsque la preuve manque ou lorsqu’une correction locale ne change plus réellement le résultat. Aucun nombre fixe d’itérations n’est requis.

---

## ACTION/ROUTING — prérequis de jugement et de structure

DIRECTION déclenche la classification générale. ACTION appelle ensuite les routes de `SAVOIR` et `BIBLIOTHEQUE` qui peuvent modifier la prochaine décision : elles s’ajoutent à la ligne du mode dans `DIRECTION/CHARGE` (colonne « Ajouter seulement si ») et ne forment pas une seconde liste.

| Situation | Routes ciblées |
|---|---|
| Spec `DIRECTION` | `SAVOIR/CRAFT`, `SAVOIR/TYPE` ou `SAVOIR/SOURCE` si la composition, la typographie ou l’ancrage restent ouverts, `SAVOIR/STYLE` si registre, `BIBLIOTHEQUE/SELECT` si structure ouverte. |
| Craft ou états | `SAVOIR/STATE`. |
| Couleur, contraste ou theming | `SAVOIR/CRAFT`, `SAVOIR/SYSTEM` et politique de contraste ACTION. |
| Risque critique, responsive, performance ou motion | `SAVOIR/CONTEXT`. |
| Technique ou compatibilité | `SAVOIR/TECH`. |
| Claim, outil ou tendance datée | `SAVOIR/TOOLS` et trace locale indiquant source, date, portée et limite. |
| Doute d’application ou théâtre procédural | `SAVOIR/INTEGRITY`. |
| Une famille de design peut modifier la prochaine décision | Section `DESIGN-ATLAS` de `SAVOIR.md`, puis seulement la route propriétaire utile. |
| Structure d’un écran | `BIBLIOTHEQUE/SELECT`, puis routes retenues. |
| Token, composant ou blast radius | `SAVOIR/SYSTEM` si une décision partagée change, `BIBLIOTHEQUE/COMPONENTS` si un composant change, `ACTION/RUN-SYSTEM` si partagé. |

Les anciennes références de section ne sont pas des routes quotidiennes. Leur migration est documentée dans `CHANGELOG.md`, et un nouveau run utilise uniquement les routes stables.

---

## ACTION/MAINTENANCE — recette documentaire

Tout cycle qui modifie ACTION ou un contrat connexe se clôt par une recette avant adoption.

| Contrôle | Preuve attendue |
|---|---|
| Fichiers et renvois | Chaque fichier et route référencés existent et portent la bonne portée. |
| Statuts | Les états, issues, verdicts et statuts de direction appartiennent aux registres canoniques ; aucun plan de maturité concurrent n’est ajouté. |
| Scopes | Chaque obligation précise son mode, contexte ou niveau de proportionnalité. |
| Exemples | Aucun exemple ne propage un statut ou une règle dépréciée. |
| Claims datés | Source, version/date, portée, limite et prochaine preuve sont renseignées dans la trace locale quand le run en dépend. |
| Routage | Chaque signal a une route principale ; les miroirs sont dérivés explicitement. |
| Quotas artificiels | Aucun quota de variantes, retraits, comparaisons, itérations ou appels ne gouverne la qualité. |
| Échappatoire théâtrale | Chaque mécanisme est testé contre sa manière la plus facile d’être satisfait sans intention. |
| Run réel | Une modification substantielle est exercée sur un run réel avant adoption élargie. |
| Ownership | Owner du changement, statut d’adoption et prochaine revue sont nommés. |
| Réserves | Owner, périmètre, date ou version, impact, date de revue, prochaine preuve et condition de sortie sont persistants. |

La recette peut être automatisée pour les fichiers, routes, statuts et renvois. Elle doit rester humaine pour le scope, l’intention, l’échappatoire théâtrale, la proportionnalité et le jugement du risque.

Une contradiction non résolue devient un risque explicite, jamais une règle silencieusement concurrente.

---
