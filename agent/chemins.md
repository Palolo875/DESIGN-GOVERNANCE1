# Agent — chemins

Comment l’agent classe une demande, choisit son chemin et décide quoi lire. La skill (`SKILL.md`, à la racine du paquet) en porte le noyau ; ce fichier en est la version complète.

<!-- origine:DIRECTION.md -->
## DIRECTION/START — classer avant d’agir

`START` est le point d’entrée quotidien d’un humain, d’une IA ou d’un pipeline. Il choisit le mode et la prochaine route ; il ne remplace ni les cinq absolus, ni les procédures, ni le jugement. Avant d’ouvrir un run, une proposition de cadrage reste possible (`DIRECTION/SERVICE-BOUNDARY`).

**Source normative de classification.** `DIRECTION/START` est la source normative unique des modes et du risque dominant. `DIRECTION/CHARGE` est la liste de chargement par mode ; `FAST-PATH` est un raccourci pour un delta local ; `EXTERNAL-START` est une vue de transport pour un brief vague. Aucun de ces encadrés ne crée une classification concurrente. En cas de différence, `START` prévaut et le conflit devient un risque explicite, corrigé selon la recette `ACTION/MAINTENANCE`.

> **Ordre de lecture minimal.** 1) `START` classe le mode et le risque. 2) La protection de niveau interdit toute baisse silencieuse face à un risque critique. 3) `CHARGE` choisit la plus petite route utile ; `FAST-PATH` n’est qu’un encadré pour un correctif local ou une décision presque tranchée. 4) Une capacité n’est chargée que si elle change la construction ou la preuve. 5) `ACTION` porte la preuve et la clôture ; `SAVOIR` le jugement ; `BIBLIOTHEQUE` la structure. 6) Les modules `ATELIER`, grounding, réemploi et atlas restent silencieux tant qu’aucune décision ne peut être modifiée ; chacun n’est activé que si sa décision à modifier est identifiée, et plusieurs ne coexistent que si leurs décisions sont distinctes et utiles.

### Arbre de classification

Pose les questions dans cet ordre :

1. La décision partagée est-elle l’objet direct du run, avec plusieurs consumers, un token, un composant, une convention, une dépendance ou une règle migrable à protéger ? → `ACTION/RUN-SYSTEM`.
2. Faut-il définir ou redéfinir une identité, un premier contact, une surface de marque ou une hypothèse de direction autonome ? → `ACTION/RUN-DIRECTION`.
3. Une surface avec direction retrouvable est-elle retouchée en demandant de rappeler et réévaluer la direction dans son périmètre, au-delà d’un fix ou delta local qui la conserve, sans remise en cause identitaire ni changement systémique ? → `ACTION/RUN-ITER`.
4. S’agit-il d’un fix ou d’un delta local dans un système déjà tranché ? → `ACTION/RUN-LITE`.
5. Sinon, s’agit-il d’un écran ou flow nouveau sans charge identitaire autonome ni blast radius systémique ? → `ACTION/RUN-STANDARD`.
6. Si aucune réponse n’est nette, pose **une clarification ciblée** : celle qui peut changer le mode ou le risque dominant. Ne devine pas.

**Frontière LITE / ITER.** Un fix local de contraste, libellé, focus ou wrapping qui conserve la direction déjà tranchée relève de `LITE`. Une retouche de composition qui demande de rappeler et réévaluer la direction retrouvable relève de `ITER`. La taille du diff ne décide pas du mode : une règle partagée reste `SYSTÈME` et la protection de niveau ci-dessous prime sur ces deux cas.

Une décision de système est l’objet direct du run lorsqu’elle doit être adoptée, migrée ou protégée pour plusieurs consumers. Si le changement partagé apparaît comme conséquence d’une décision de direction, traite d’abord la direction ; ouvre ensuite le run système dépendant, sauf si les décisions sont inséparables.

**Protection de niveau.** Un risque critique de tâche, de santé, de sécurité, de confidentialité, de permission ou d’accessibilité interdit `LITE` ou `ITER` dès que le changement touche une action, un état, une sémantique, une donnée, une récupération ou une preuve de ce risque. Un nouvel onboarding, formulaire, consentement, flux de santé, permission ou mécanisme de récupération n’est jamais un micro-delta `LITE` ou `ITER`, même si une seule étape ou un seul libellé semble local. Reclassifie vers `STANDARD`, `DIRECTION` ou `SYSTÈME` selon le blast radius. `LITE` ou `ITER` restent possibles seulement lorsqu’il est démontré que le delta est strictement local, réversible et sans effet sur ces responsabilités.

**Silence des micro-deltas.** Une correction de libellé, de traduction, d’overflow, de contraste, de focus, d’état ou de wrapping dans un composant existant ne constitue pas à elle seule une décision de style, de technique, d’effet, d’asset ou de structure. Ne charge pas `SAVOIR/DESIGN-ATLAS` pour ce type de delta ; reste sur la route locale tant qu’aucune responsabilité n’est réellement modifiée.

**Règle de conflit.** Si plusieurs signaux sont positifs, découpe le travail lorsque les risques sont indépendants. Deux risques sont indépendants si la preuve de l’un ne dépend pas de la décision de l’autre et si leur owner, leur artefact et leur condition de sortie peuvent être distincts. Sinon, retiens le mode qui protège le risque dominant, sans importer les artefacts sans rapport.

### Entrée minimale

En trace complète, l’entrée de lancement rend retrouvables les décisions qui peuvent changer l’artefact :

```text
DECISION — ce qui doit être tranché
RISK — coût d’erreur dominant
SCOPE — surface, état, viewport, consumer ou périmètre concerné
CONSTRAINT — contrainte réelle qui peut changer la décision, dont la destination (démo, prototype ou produit réel) et l’enjeu identitaire
NEXT-PROOF — observation ou test qui permettra de trancher
OWNER — responsable de la décision et de la prochaine action
```

Ce gabarit est la projection de la ligne `RUN` (« Sortie immédiate ») pour la trace complète, pas un second schéma : `ACTION/RUN_CARD` reste propriétaire des champs complets, des états, des issues, des verdicts et de la clôture. En trace complète, `OWNER` et `SCOPE` ne sont jamais omis : ils rendent la reprise et la portée vérifiables. Les autres lignes sont omises ou `N/A-JUSTIFIED` si elles ne peuvent rien changer. En trace légère, la ligne `RUN` suffit.

### Sortie immédiate

Crée ou mets à jour une ligne de run. C’est la seule déclaration de lancement (absolu 4 de `DIRECTION/STANDARD`) :

> `RUN — [MODE] — [décision dominante] — [risque principal] — [preuve suivante] — [condition d’arrêt].`

En trace complète, elle porte aussi un identifiant et l’état du run (`ACTION/STATUS`) : `RUN — [ID] — … — [état]`. La ligne de run doit exister dès qu’une action de production, une vérification ou un changement d’état commence. Lorsque le risque ou la reprise l’exige, l’owner doit être retrouvable depuis cette ligne ou son identifiant.

Sa décision dominante est la `DECISION-INTENT` : la décision que la procédure doit permettre de trancher. Aucune ligne séparée n’est écrite en trace légère ; en trace complète, elle se reporte dans `decision_intent`.

Après une observation qui modifie, confirme ou abandonne effectivement une décision, ajoute :

> `DECISION-CHANGE — [décision effectivement changée, confirmée ou abandonnée grâce à la procédure].`

À la clôture, si aucune décision n’a été changée, confirmée ou abandonnée, les valeurs de repli d’`ACTION/STATUS` s’appliquent : `N/A-JUSTIFIED` lorsqu’aucune conséquence n’était applicable, avec la raison, le risque de continuer sans changement et la prochaine action éventuelle ; `NOT-OBSERVED` lorsqu’une conséquence attendue n’a pas été observée. Ne déclare jamais un changement avant qu’une observation ne l’ait rendu réel.

### Mémoire de lancement et renvoi de `RUN_CARD`

En trace complète, la ligne de run s’étend en mémoire de lancement, sous-ensemble de lancement de `ACTION/HANDOFF`, non un handoff ni une `RUN_CARD` : `ID`, `MODE`, `DECISION`, `RISK`, `SCOPE`, `ARTIFACT` attendu, `OWNER`, `NEXT-PROOF`, `LIMIT` et `EXIT-CONDITION`. Elle peut vivre dans un ticket, un manifeste de projet, un espace de travail ou un fichier local.

Le schéma complet de `RUN_CARD` appartient exclusivement à **`ACTION/RUN_CARD`**. DIRECTION ne le reproduit pas et transmet la projection `ACTION/HANDOFF`; les champs non applicables sont `N/A-JUSTIFIED`, les observations non vérifiées restent `NOT-VERIFIED`. Une surface `DIRECTION` qui accepte avec V en `PASS` ou `PASS-WITH-RESERVATION`, dont le risque V/craft est dominant ou dont le verdict V dépend d’une intention encore non confrontée doit suivre `ACTION/GATE-B — B1b` avant clôture. Pour une `RUN_CARD DIRECTION` en `CLOSED`, `creative_close` contient `presence`, `signature`, `craft_detail`, `dominant_defect` et `next_polish_action` ; `direction_status`, `issue` et `verdict` restent les registres séparés d’ACTION.

Un run `STANDARD`, `DIRECTION` ou `SYSTÈME` persistant, partagé ou audité conserve une trace persistante (trace complète, `ACTION/HANDOFF`) ; sinon, la trace légère suffit. `ITER` peut s’appuyer sur la mémoire locale du projet si la direction précédente, le périmètre, le dernier artefact, la décision, la preuve et le risque restant sont retrouvables. `LITE` peut se limiter à la ligne de run et au verdict court si l’artefact et le risque restent retrouvables.

---

<!-- origine:DIRECTION.md -->
## DIRECTION/CHARGE — classer, puis charger

<!-- noyau:début CHARGE-REGLE -->
> **Règle de vitesse.** Ouvre l’arbre `DIRECTION/START/TREE`, classe le mode, puis lis sa ligne avec `python3 scripts/read_route.py --mode MODE`. Le **tronc** de la ligne (au plus 35 000 caractères, `--tronc MODE`) se lit à chaque run de ce mode ; le reste de la ligne se lit quand son signal apparaît. `DIRECTION/START` complet reste disponible si le contexte de lancement ou les capacités doivent être précisés. Lis ce qui peut changer la décision présente ; les routes d’observation et de clôture attendent leur usage. Toute contrainte critique est lue avant le choix qu’elle protège. Pour une relation de craft ouverte, même dans un correctif local, lis les gestes de `SAVOIR/STATE` ; n’approfondis que le savoir qui peut modifier l’intervention, sans ouvrir de nouvelle direction. Avant de construire, déclare le mode, la décision dominante, le risque principal, la preuve minimale et la condition d’arrêt (absolu 4) : une ligne suffit, dans la trace.

**Retrouver un savoir.** `python3 scripts/read_route.py --trouver "terme"` cherche une notion ; sans résultat, reformule, sans conclure à l’absence du savoir. `python3 scripts/read_route.py LOCATOR` lit une route en entier, blocs du noyau repliés ; `python3 scripts/read_route.py --connexions` relie plusieurs propriétaires. Le mode d’emploi complet du lecteur est servi par `DIRECTION/CHARGE`.
<!-- noyau:fin CHARGE-REGLE -->

<!-- noyau:début CHARGE-RECHERCHE -->
**Retrouver un savoir utile.** Route inconnue, notion apparemment absente ou finesse sans geste concret : `python3 scripts/read_route.py --trouver "terme"`. La recherche couvre les sections normatives à leurs emplacements actuels : mots entiers, quelques synonymes et traductions, puis correspondances partielles ; routes classées, `--tout` pour tout afficher. Elle ne comprend pas le sens : sans résultat, reformule puis déclare la limite, sans conclure à l’absence du savoir. `python3 scripts/read_route.py --sommaire` liste les routes ; `--sommaire LOCATOR`, leurs sous-sections. `SAVOIR/READ` guide le chargement et `SAVOIR/ROUTING` le jugement. Lis la route utile en entier avec `scripts/read_route.py LOCATOR`, puis applique-la à la décision. Les blocs déjà dans le noyau sont repliés (`--complet` les affiche). Lecteur indisponible : cherche dans la source propriétaire avec son contexte. Respecte la ligne du mode : ni lecture exhaustive, ni direction supplémentaire.

Si plusieurs propriétaires peuvent éclairer une relation ouverte, consulte les connexions situées de `sections/READING_MAP.md` avec `python3 scripts/read_route.py --connexions`. Cette aide dérivée conserve les conditions et limites ; elle ne remplace ni la ligne de CHARGE ni les sources.
<!-- noyau:fin CHARGE-RECHERCHE -->

Une intention perceptuelle encore sans levier de construction active la traduction de `BIBLIOTHEQUE/SELECT` dans le périmètre du mode ; une route connue se lit directement. Si seule sa fabrication reste ouverte, utilise la calibration de `BIBLIOTHEQUE/CONTRACTS`. Ce passage relie direction, structure et gestes de SAVOIR sans charger le catalogue entier ni ajouter une seconde liste de chargement.

`CHARGE` est la seule liste de chargement du corpus : la skill active sa ligne à la demande, les façades y renvoient. Les modes restent définis par `START` ; les verdicts et les sorties, par `ACTION`.

<!-- noyau:début CHARGE-TABLE -->
| Mode | Charger d’abord | Ajouter seulement si cela change la décision |
|---|---|---|
| **LITE** | **Tronc** : `ACTION/RUN-LITE`, `ACTION/FAST-PATH`, `ACTION/GATE-A` (contrôles applicables), de Gate B seulement `ACTION/GATE-B/B2` (familles de preuve) et `ACTION/GATE-B/B6` (sortie compacte). Sans risque critique touché — voir Protection de niveau (`DIRECTION/START`). | Une route SAVOIR ou BIBLIOTHEQUE si le correctif touche réellement le jugement ou la structure. `SAVOIR/DESIGN-ATLAS` reste silencieux ; une famille seule ne reclassifie pas. Si le périmètre, le blast radius, la responsabilité ou le risque dominant change la décision, reviens à `DIRECTION/START` puis reclassifie vers `ITER`, `STANDARD`, `DIRECTION` ou `SYSTÈME`. |
| **ITER** | **Tronc** : `ACTION/RUN-ITER` et `ACTION/GATE-A` (contrôles applicables). Selon le cas : mémoire locale (direction existante), non-régression pertinente et `ACTION/GATE-B` du risque touché. Sans risque critique touché — voir Protection de niveau (`DIRECTION/START`). | `ACTION/GATE-C` si le craft change ; une route SAVOIR ; BIBLIOTHEQUE seulement si support, grille, scène ou objet change. `SAVOIR/DESIGN-ATLAS` reste silencieux dans le même périmètre ; une famille seule ne reclassifie pas. Si le périmètre, la responsabilité ou le risque dominant change la décision, reviens à `DIRECTION/START`. Les corrections de libellé, overflow, contraste, focus, état ou wrapping restent locales. |
| **STANDARD** | **Tronc** : `ACTION/RUN-STANDARD`, `ACTION/GATE-A` ciblé et, de Gate B, les familles de preuve (`ACTION/GATE-B/B2`). Selon le signal : `ACTION/UI-UX-REALITY` si la surface UI/UX est nouvelle ou substantiellement modifiée ; `BIBLIOTHEQUE/SELECT` si la structure est ouverte ; en trace complète (`ACTION/HANDOFF`), `ACTION/GATE-B` ciblé. | `SAVOIR/FRAME` si le cadrage est ambigu ; `DIRECTION/DOMAIN-FRAME` si la demande est nouvelle, ambiguë ou multi-domaines et que le domaine peut changer la structure, l’expression ou la preuve ; une route BIBLIOTHEQUE structurante et la route SAVOIR du risque dominant. |
| **DIRECTION** | **Tronc, avant le premier objet** : `ACTION/RUN-DIRECTION` pour le lancement et les préconditions, `DIRECTION/CREATIVE-BOOT`, `DIRECTION/VISUAL_TARGET`, `DIRECTION/FIRST-OBJECT`, `SAVOIR/TYPE` (voix comparées sur le vrai titre), `ACTION/FIRST-RENDER` et `ACTION/GATE-A` (contrôles applicables). **Avant le premier objet, selon le signal** : `DIRECTION/EXTERNAL-START` si le brief est vague, `ACTION/UI-UX-REALITY` si la surface UI/UX est nouvelle ou substantiellement modifiée. **Pendant la fabrication et l’observation** : `ACTION/PIPELINE-DIRECTION`, `ACTION/VISUAL_PROOF` et `ACTION/GATE-C`, avec exécution des contrôles A applicables. **À la sortie, en trace complète (`ACTION/HANDOFF`)** : `ACTION/GATE-B`, `ACTION/RUN_CARD`, `DIRECTION/ANCHOR-RESERVE` si l’ancre est seulement générée et l’enjeu identitaire élevé, et `ACTION/CLOSE-PACKAGE`. Une précondition ou un risque critique avance la lecture qui le protège ; ces étapes ne dispensent d’aucune preuve applicable. | Active une route lorsque son déclencheur apparaît ; garde son rôle ou une exclusion qui change la décision dans la trace existante, sans inventaire anticipé de toutes les exclusions. `DIRECTION/DOUBLE-LOOP`, `ACTION/ROUTING` ou `SAVOIR/CRAFT/CFT-00` si la décision l’exige (la boucle commune est dans le noyau ; les gestes se lisent dans `SAVOIR/STATE`) ; `DIRECTION/DIRECTION-ATELIER` si la tension, le geste produit ou un anti-choix peuvent modifier la première scène ; `SAVOIR/FRAME`, `SAVOIR/CRAFT`, `SAVOIR/SOURCE` et `BIBLIOTHEQUE/SELECT` si nécessaires ; `BIBLIOTHEQUE/SEQUENCE` si la page compte plusieurs sections ; `DIRECTION/DOMAIN-FRAME` si la demande est nouvelle, ambiguë ou multi-domaines et que le domaine peut changer la structure, l’expression ou la preuve. Charge `SAVOIR/STYLE` seulement si le choix de style peut modifier une décision de composition, de voix, de matière, de contraste ou de relation produit ; jamais comme catalogue automatique. `SAVOIR/CRAFT/CFT-03`, `SAVOIR/STATE` ou `SAVOIR/INTEGRITY` si un détail final peut modifier le caractère, un état, la hiérarchie, la densité ou la robustesse ; `SAVOIR/INTEGRITY` avant un verdict (trace complète). |
| **SYSTÈME** | **Tronc** : `ACTION/RUN-SYSTEM`, `SAVOIR/SYSTEM`, `ACTION/GATE-A` (contrôles applicables). `BIBLIOTHEQUE/COMPONENTS` si un composant change. | `maintenance/versions` si une règle partagée change. |
<!-- noyau:fin CHARGE-TABLE -->

<!-- noyau:début CHARGE-FIN -->
Réponds dans la langue de la demande. La clôture de chaque mode est `ACTION/CLOSE-PACKAGE`, en trace complète ; en trace légère, le run s’arrête à la proposition (`ACTION/HANDOFF`). Tags du noyau : `[REQUIS PAR LE MODULE — scope]`, obligation dans ce scope (sinon `NOT-VERIFIED`, ou `N/A-JUSTIFIED` motivé) ; `[MÉTHODE]`, procédure à adapter.
<!-- noyau:fin CHARGE-FIN -->

<!-- noyau:début CHARGE-LECTEUR -->
Les codes du noyau et les adresses lisibles servent les mêmes sections : une seule lecture suffit. Pour l’agent, seuls les blocs effectivement compilés dans la skill sont déjà lus ; les autres restent servis par leur route propriétaire. Le lecteur ne replie un bloc que si son texte complet est présent dans la skill ; `README.md`, `guides/3-maitriser.md` et `guides/2-comprendre.md` sont des lectures d’orientation pour les humains ; l’agent n’interroge READING_MAP que par `--connexions`.
<!-- noyau:fin CHARGE-LECTEUR -->

<!-- noyau:début CHARGE-DETAILS -->
**Lire les détails selon le signal.** Lis la route utile en entier, au moment où elle peut changer la décision ; les blocs déjà dans le noyau y sont repliés. Une retouche locale conserve la direction retrouvée et charge seulement le savoir utile au delta. Ces lectures éclairent un choix situé, sans prescrire une police, une palette ou un gabarit.

| Signal | Route |
|---|---|
| Composition nouvelle ou direction réévaluée | `SAVOIR/FRAME/COMPOSITION` et `SAVOIR/FRAME/SINGULARITE`, avant de construire |
| Structure ouverte | `BIBLIOTHEQUE/READ`, `BIBLIOTHEQUE/SELECT` ; `BIBLIOTHEQUE/TENSION` si l’alternative peut changer le choix |
| Caractère perceptuel à traduire en leviers (calme, tension, intimité…) | `BIBLIOTHEQUE/READ`, « Traduire un caractère en leviers » |
| Brief vague | `DIRECTION/EXTERNAL-START` ; le premier objet et son plafond suivent la ligne du mode |
| Typographie ouverte | `SAVOIR/TYPE`, sur le vrai contenu ; `SAVOIR/TYPE-VOIX` pour choisir une voix |
| Relation de couleur ouverte | `SAVOIR/CRAFT/CFT-05` |
| Texte sur image, densité ou harmonie | `SAVOIR/CRAFT/CFT-03` |
| Choix de style utile | `SAVOIR/STYLE` |
| Asset, provenance ou calibration culturelle | `SAVOIR/SOURCE` |
| Bibliothèque, police, icônes, texture, données ou 3D à choisir | `SAVOIR/TOOLS/MOYENS`, par couche, licence relue à l’intégration |
| Ancien projet, préférence, profil, asset ou composant qui peut orienter le brief | `DIRECTION/FIRST-OBJECT`, « Réutilisation située » (`REUSE-CHALLENGE`) |
| Un fait, un claim, un asset, un terme métier, une contrainte, un droit ou une capacité réelle peut modifier la scène, la preuve ou l’action | `DIRECTION/GROUNDING` |
| Levier CSS récent ou limité à un moteur, compatibilité | `SAVOIR/TECH` |
| Médium non Web, plateforme ou capacité spéciale à choisir (CMS, primitive, motion d’état, 3D) | `DIRECTION/CAPACITY`, puis `SAVOIR/TECH` pour la preuve propre au médium |
| Finesse sans geste concret, craft ou états | `SAVOIR/STATE`, avant l’intervention |
| Revue créative | `SAVOIR/CRAFT/CFT-00` |
| Alternative située | `DIRECTION/DIVERGENCE` (déclenchement), puis `SAVOIR/CRAFT/CFT-02` (leviers) |
| Motif générique ou réflexe | `SAVOIR/CRAFT/CFT-01` (test motivation/construction) ; conséquence de gate : `ACTION/ANTI-SLOP` |
| Détail final susceptible de modifier le caractère, l’état, la hiérarchie, la densité ou la robustesse d’une surface `DIRECTION` | `SAVOIR/CRAFT/CFT-03`, `SAVOIR/STATE` ou `SAVOIR/INTEGRITY` selon la question ouverte, et capture rendue ; conditionnel, comme la colonne « Ajouter seulement si » de `DIRECTION/CHARGE` |
| Recette de rendu exécutée ou citée (options, états, captures, comparaison) | `ACTION/RECETTE-RENDU` |
| Un asset, ou son absence, porte une décision perceptible | `DIRECTION/ASSET-ROUTE`, avant le build : une route de production nommée |
| Asset, motion, scène ou type spécifique à construire | Le contrat correspondant d’ACTION et la route SAVOIR utile ; pour une scène, `BIBLIOTHEQUE/SELECT` puis la route `BIBLIOTHEQUE/SCENE` retenue |
| Token, composant partagé, theming ou blast radius | `SAVOIR/SYSTEM` si une décision partagée change, `BIBLIOTHEQUE/COMPONENTS` si un composant change, `ACTION/RUN-SYSTEM` si partagé |
| Cadrage ambigu : public, tâche ou compromis | `SAVOIR/FRAME` |
| Contexte critique, responsive, performance ou mouvement | `SAVOIR/CONTEXT` |
| Famille de design, technique, effet ou médium qui peut modifier la décision | `SAVOIR/DESIGN-ATLAS`, après la classification, puis seulement la route spécialisée utile |
| Claim daté, tendance ou outil externe | `SAVOIR/TOOLS`, avec source, date, portée et limite dans la trace |
| Doute sur l’application d’une règle, limite, délégation ou théâtre procédural | `SAVOIR/INTEGRITY`, avant tout verdict |
| Échec connu à assumer malgré un gate | `ACTION/OVERRIDE` (`FAIL-ASSUMED`), jamais pour une preuve qui manque |
| Repasse | `SAVOIR/INTEGRITY/REPASSE`, dans son périmètre |
| Texte calculé, état animé ou résultat d’une action à prouver | `ACTION/VISUAL_PROOF`, à l’état qui compte (`--assert`, `--in-frame`) |
| Diagnostic ou condition d’arrêt encore ouvert | `DIRECTION/DOUBLE-LOOP` |

Aucun détail n’est considéré lu parce qu’il porte un marqueur « noyau » dans sa source.
<!-- noyau:fin CHARGE-DETAILS -->

**Déclenchement de l’atlas.** Si aucune famille ne peut être reliée à une décision modifiable, n’ouvre pas `SAVOIR/DESIGN-ATLAS` ; reste sur la route existante. Si le signal est ambigu, pose une seule clarification ciblée ou reviens à `DIRECTION/START` pour classer le mode et le risque. Si un risque critique apparaît, reclassifie avant de charger une famille. L’atlas ne sert jamais à résoudre par catalogue un JTBD, un mode ou une intention manquante.

**Règle de passage.** `DIRECTION` décide du mode et du risque dominant ; `ACTION` des preuves exécutables, gates, statuts et verdicts ; `SAVOIR` du jugement ; `BIBLIOTHEQUE` de la structure ; la maintenance (`maintenance/evolution.md` et `maintenance/versions.md`) de la gouvernance du système.

### DIRECTION/FAST-PATH — renvoi vers l’exécution courte

`FAST-PATH` est une vue dérivée de `START`, non une porte d’entrée concurrente. Pour un correctif local ou une décision déjà presque tranchée, les quatre questions sont celles d’`ACTION/FAST-PATH`, seul bloc d’exécution courte, à poser avant de charger un module.

Si la réponse à la quatrième question (ce que la preuve changera) est « rien », ne lance pas un nouveau protocole et ne charge pas l’atlas. Conserve l’existant et omets la ligne sans effet ; utilise `N/A-JUSTIFIED` seulement si aucun contrôle ou aucune décision applicable ne peut changer dans le scope déclaré. `EXPLORATORY` reste réservé au cas où un rendu observable existe mais qu’une preuve requise manque. En exploration, `DECISION-INTENT` peut être une hypothèse à formuler ; `DECISION-CHANGE` devient obligatoire seulement lorsque le run prétend qu’une décision de production a été changée, confirmée ou abandonnée.

---

<!-- origine:ACTION.md -->
## ACTION/RUN — routes d’exécution

Les blocs `RUN-*` donnent l’entrée, la sortie et le contrôle minimal de chaque mode. Les sections détaillées ci-dessous sont canoniques lorsque le bloc les appelle. Le contrat ACTION minimal de chaque mode est dans `ACTION/PRECONDITION`.

### `ACTION/RUN-LITE`

**Entrée.** Système et direction retrouvables ; delta local ou fix ; décision dominante connue.

**Faire.** Écrire la ligne de run, déclarer `DECISION-INTENT`, modifier, contrôler les gates A applicables et obtenir une preuve B du risque dominant. Charger `SAVOIR` ou `BIBLIOTHEQUE` uniquement si cela peut changer le correctif. Une alternative n’est documentée que si un choix plausible peut modifier le delta ou le risque.

**Sortie.** Paquet `LITE` d’`ACTION/CLOSE-PACKAGE`. Trace légère : la proposition (`ACTION/HANDOFF`).

**Clôture.** En trace complète, passer à `DECIDED`, puis `CLOSED`. Reclassifier en `SYSTÈME` si une règle partagée est touchée, en `ITER` si la direction précédente doit être réévaluée ou en `DIRECTION` si une nouvelle décision identitaire apparaît.

### `ACTION/RUN-ITER`

**Entrée.** Direction, composants, tokens et périmètre précédent retrouvables dans la trace légère (ligne de thèse), la `RUN_CARD`, le manifeste ou le projet. Dans une `RUN_CARD`, le rappel de direction est porté par `direction.thesis` et la trace par `trace_locator`. Si la direction n’est pas retrouvable, reconstitue le contexte et reclasse avec `DIRECTION/START` : `DIRECTION` si la retouche remet en cause un axe de direction, `SYSTÈME` si elle touche une règle partagée.

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

**Faire.** Cartographier l’impact et les consumers. Nommer la décision, l’owner, la migration, le rollback et les tests de non-régression. Consulter `maintenance/evolution.md` pour le cycle de vie et `maintenance/versions.md` pour l’état actuel avant adoption, pilotage ou dépréciation. Si le changement touche ACTION ou un contrat connexe, le clore par la recette documentaire `ACTION/MAINTENANCE`.

**Sortie.** Paquet `SYSTÈME` d’`ACTION/CLOSE-PACKAGE`. Trace légère : la proposition (`ACTION/HANDOFF`). Dans une `RUN_CARD` acceptée, ces éléments forment `closure.system_package` : impact, consumers, owner, migration, rollback, non-régression (claim et baseline : locator, version, état) et référence CHANGELOG.

**Clôture.** En trace complète, passer à `DECIDED`, puis `CLOSED` lorsque consumers et réserves sont traçables. Passer à `ESCALATED` si owner, droit, décision externe ou risque externe manque.

---

<!-- origine:ACTION.md -->
## ACTION/FAST-PATH — preuve minimale sans rituel

Pour `LITE` et les petits `ITER`, arrête le protocole après quatre réponses : décision ou delta touché ; risque dominant et son owner ; preuve la moins coûteuse (capture, diff, test, scénario, mesure ou comparaison) ; conséquence si la preuve est positive ou négative, avec condition d’arrêt et prochaine action ; puis, en trace complète, clôture avec le paquet de son mode : forme courte LITE pour `LITE`, paquet `ITER` pour un `ITER` (`ACTION/CLOSE-PACKAGE`) ; en trace légère, la proposition suffit.

Si aucune décision ne peut changer, n’ajoute pas de capture, comparaison ou route uniquement pour remplir le paquet. Journalise `N/A-JUSTIFIED` lorsque la procédure ne peut rien modifier.

Reviens à un mode plus riche si le changement touche une règle partagée, l’identité, une décision coûteuse, ou un risque critique de tâche, de santé, de sécurité, de confidentialité, de permission ou d’accessibilité (Protection de niveau de `DIRECTION/START`). Un fix local de contraste, libellé, focus ou wrapping qui conserve la direction reste `LITE`.

---

<!-- origine:ACTION.md -->
## ACTION/ROUTING — prérequis de jugement et de structure

DIRECTION déclenche la classification générale. ACTION appelle ensuite les routes de `SAVOIR` et `BIBLIOTHEQUE` qui peuvent modifier la prochaine décision : elles s’ajoutent à la ligne du mode dans `DIRECTION/CHARGE` (colonne « Ajouter seulement si ») et ne forment pas une seconde liste.

Les routes de `SAVOIR` et de `BIBLIOTHEQUE` se choisissent dans la table des signaux du noyau (« Lire les détails selon le signal », `DIRECTION/CHARGE`) ; ACTION n’en tient pas de seconde liste.

Les anciennes références de section ne sont pas des routes quotidiennes. Leur migration est documentée dans `maintenance/evolution.md`, et un nouveau run utilise uniquement les routes stables.

---

<!-- origine:SAVOIR.md -->
## SAVOIR/READ — comment utiliser cette bibliothèque

`DIRECTION` détermine **si** une route est requise. `ACTION` détermine **quelle preuve** et quelle sortie sont nécessaires. `SAVOIR` explique **comment juger** dans le domaine concerné.

Ne charge jamais l’ensemble de SAVOIR par réflexe. Charge typiquement zéro à deux routes ; une route par question active (CRAFT, TYPE, SOURCE, CONTEXT…) ; zéro route est valide lorsqu’aucune responsabilité de jugement ne change. Ajoute une route seulement si elle peut modifier la prochaine décision ou le statut de preuve.

**Chemin minimal.** Décide d’abord la décision et le risque ; charge ensuite la route SAVOIR principale, ou aucune si le changement reste local. Ajoute une route seulement si elle change une question, une preuve ou une limite ; `ACTION` reste propriétaire des preuves, des gates, des verdicts et de la clôture. Un tag `[REQUIS PAR LE MODULE — scope]` indique qu’une responsabilité devient applicable dans le périmètre déclaré ; il n’impose pas de charger toute la bibliothèque, mais d’exécuter ou de tracer honnêtement le contrôle concerné selon le contrat d’ACTION. Sur le chemin d’un run, le plancher de ces obligations est compilé dans le noyau de la skill ou servi par le tronc des modes visés ; leur détail s’applique lorsque la route est chargée.

Le bénéfice attendu de chaque route doit être identifiable avant son chargement.

> Un principe SAVOIR guide une décision ; une méthode décrit comment formuler la raison ; une preuve ACTION établit ce qui a été observé ou mesuré. Aucun principe, ancre, profil ou texte de justification ne produit seul un `PASS` d’usage, d’accessibilité ou de qualité.

La sortie de SAVOIR n’est pas un verdict. Elle doit transmettre à ACTION la décision jugée, le principe ou la méthode utilisés, la conséquence observable, la preuve attendue, la limite, le propriétaire et la prochaine preuve. Si aucune décision ne peut changer, ne chargez pas une route supplémentaire. À la clôture, si aucune décision n’est changée, confirmée ou abandonnée, les valeurs de repli d’`ACTION/STATUS` s’appliquent : `N/A-JUSTIFIED` lorsqu’aucune conséquence n’était applicable, `NOT-OBSERVED` lorsqu’une conséquence attendue n’a pas été observée.

### SAVOIR/JUGEMENT-COURT — juger sans produire un dossier

Pour un delta local, écris seulement les quatre réponses d’`ACTION/FAST-PATH` et le principe utile. Si le principe ne change aucune décision, ne le charge pas.

Le fast path n’autorise pas à ignorer une preuve critique lorsque le risque dominant est élevé. Il réduit la formalité ; il ne réduit pas l’honnêteté du statut.

### Niveaux d’autorité

Les tags indiquent le statut de lecture. Ils ne transforment pas une heuristique en résultat scientifique.

| Tag | Sens | Usage autorisé |
|---|---|---|
| `[DURABLE]` | Principe de jugement stable du système. | Guider une décision ; ne pas le présenter comme loi empirique universelle. |
| `[MÉTHODE]` | Procédure de raisonnement interne. | Adapter au mode, au contenu et au contexte. |
| `[REQUIS PAR LE MODULE — scope]` | Obligation spécialisée. | Exécuter dans le scope ; sinon déclarer `NOT-VERIFIED` (preuve manquante), ou `N/A-JUSTIFIED` avec sa raison si l’obligation ne s’applique pas. |
| `[À ADAPTER]` | Point de départ ou valeur illustrative. | Ajuster avec une raison située, un public et une contre-indication. |
| `[VEILLE]` | Observation datée, outil, tendance ou support. | Vérifier avant de l’invoquer comme fait. |
| `[OPINION DE SYSTÈME]` | Heuristique éditoriale du corpus. | Utiliser comme hypothèse, jamais comme preuve externe. |
| `[DÉPRÉCIÉ]` | Élément conservé pour migration. | Ne pas appliquer à un nouveau run. |

Un principe `[DURABLE]` qui concerne perception, esthétique, émotion ou culture conserve son statut de principe de jugement mais doit être lu avec sa portée et sa contre-indication. Les claims externes, mesures, standards et outils suivent le contrat `SAVOIR/TOOLS`.

Les anciens identifiants de section sont documentés dans la table de migration de `maintenance/evolution.md` et ne doivent pas être utilisés comme instructions actives.

<!-- origine:SAVOIR.md -->
## SAVOIR/ROUTING — routes stables

Une question possède une route principale. Les autres routes sont des renvois qui ne créent pas une seconde procédure.

La route principale d’une question est celle que donne la table des signaux du noyau (« Lire les détails selon le signal », `DIRECTION/CHARGE`) ; chaque route de SAVOIR nomme elle-même ses renvois. SAVOIR n’en tient pas de seconde liste.
