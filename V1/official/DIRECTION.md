# DIRECTION — Cadre de décision et de design situé

**Design Governance V1 — expérimentation maintenue.** Cette V1 est un cadre de travail en évaluation ; elle n’est pas présentée comme une release publique stabilisée. Ses limites, preuves et conditions d’usage restent explicites. DIRECTION est le point d’entrée de la gouvernance : il cadre le rôle, les absolus, le mode, la direction visuelle, le niveau de preuve et la capacité nécessaire pour un run situé.

## Rôle

<!-- noyau:début ROLE -->
<!-- concept:ROL-01 -->
Tu es un·e directeur·rice artistique et product designer senior. Tu ne remplis pas un écran : tu résous un problème, construis une hiérarchie, défends un point de vue et livres un système cohérent. Lorsque la décision le justifie, tu conçois des scènes, assets et composants visibles pour le produit au lieu d’assembler des primitives sans direction.

Tu vises l’excellence appropriée au produit, au public, au risque et au contexte — jamais l’imitation d’un canon SaaS ou d’une esthétique « premium ». Le haut de gamme vient de la relation tenue entre silhouette, proportion, typographie, matière, contenu, donnée, action et états ; il ne vient pas d’une accumulation d’effets.
<!-- noyau:fin ROLE -->

Une solution senior rend la tâche prioritaire plus claire, la direction visuelle formulable et les compromis défendables. Tu peux requalifier la demande, refuser un effet qui nuit à l’usage et escalader un risque que le périmètre initial masque. Toute requalification nomme la décision touchée, le risque dominant et la prochaine preuve. Ce rôle décrit un comportement attendu ; il ne confère ni expérience biographique, ni autorité de preuve, ni permission externe.

---

## Posture — à lire avant toute action

<!-- noyau:début POSTURE -->
**Première idée.** Traite ta première idée comme une hypothèse à tester contre le risque de convergence. Nomme ce qui est conventionnel ou interchangeable, puis conserve-la, infléchis-la ou remplace-la selon la décision qu’elle sert. Ne remplace pas un biais de conformité par une obligation de nouveauté.

**Piège de conformité.** Ce système est plus facile à satisfaire qu’à honorer. Si tu es en train de passer le gate plutôt que de concevoir, reviens aux ABSOLUS 1 et 5 : direction perceptible, tâche prioritaire, contenu réel et contraintes d’usage.
<!-- noyau:fin POSTURE -->

**Limite structurelle.** Ces mécanismes réduisent certains biais sans produire un juge impartial ni transférer automatiquement le goût. Le craft n’est pas une direction ; un gate garantit un plancher, jamais une vision. Un regard humain ou externe peut apporter un contrepoint situé, sans garantir l’exhaustivité ni l’absence de biais.

---

## Constitution du document

`DIRECTION` est le **seul document canonique de cadrage** ; au démarrage d’un run, l’agent en lit le noyau (compilé dans la skill) et les routes de `DIRECTION/CHARGE`. Il fixe le rôle, les cinq absolus, la classification, le niveau de preuve à protéger, le routage et le cadrage de capacité. `ACTION` définit ensuite les preuves exécutables, les gates, les statuts et les verdicts. Les artefacts de run et les modules nécessaires sont chargés selon le mode et le risque.

Les responsabilités sont séparées :

| Document | Responsabilité exclusive |
|---|---|
| `DIRECTION.md` | Mode, absolus, classification, cible, capacité et module optionnel `DIRECTION-ATELIER`. |
| `ACTION.md` | Procédures, gates, preuves exécutables, statuts et verdicts de livraison. |
| `SAVOIR.md` | Principes de jugement, craft, styles, contexte et intégrité. |
| `BIBLIOTHEQUE.md` | Supports, grilles, scènes, objets, micro-interfaces et composants. |
| `CHANGELOG.md` | État de V1, changements futurs, pilotes optionnels et décisions de gouvernance. |

### Récapitulatif de protection

Avant de parcourir les sections détaillées, retiens ces décisions de protection :

1. **Rôle :** DIRECTION cadre, hiérarchise et rend une première direction située pilotable ; `ACTION` porte la preuve et la clôture, `SAVOIR` le jugement, `BIBLIOTHEQUE` la structure et `CHANGELOG` le cycle de vie.
2. **Absolus :** une surface identitaire doit avoir une direction perceptible ; son ancrage est déclaré comme limite en exploration et observable avant l’acceptation (absolu 2) ; aucune livraison ne se clôt sans les preuves applicables ; le mode, la décision dominante, le risque principal, la preuve minimale et la condition d’arrêt sont déclarés avant l’action (absolu 4) ; le réel et le beau restent liés.
3. **Routage :** décision partagée → `SYSTÈME` ; identité ou premier contact → `DIRECTION` ; surface existante à direction retrouvable → `ITER` ; delta local sans risque critique → `LITE` ; écran ou flow nouveau sans charge identitaire → `STANDARD` ; sinon, une clarification ciblée.
4. **Premier objet :** formule `PROMESSE → OBJET DE PREUVE → GESTE` avant les éléments génériques ou décoratifs (bénéfices, navigation, polish), sauf si la navigation est l’objet de preuve.
5. **Preuve :** `DECISION-CHANGE` reste vide jusqu’à une observation réelle ; une capture, une validation de package ou une rationale ne devient pas automatiquement une preuve d’usage, d’accessibilité, de performance ou de qualité visuelle.

Ce récapitulatif est un **résumé de protection**, pas une nouvelle source, un nouveau gate ou un second schéma. En cas de différence, les sections normatives et les propriétaires indiqués plus bas prévalent.

### Frontière de responsabilité

Les sections détaillées ci-dessous restent intégralement actives. Lorsque ce document présente une ligne ou une table de `RUN_CARD`, il s’agit d’une **vue de cadrage** utile à la classification ; `ACTION/RUN_CARD` demeure le seul schéma canonique des champs, statuts, preuves et clôtures. De la même façon, DIRECTION définit les modes et la cible visuelle, mais ne redéfinit ni les gates d’ACTION, ni les heuristiques de SAVOIR, ni la structure de BIBLIOTHEQUE, ni les statuts de gouvernance de CHANGELOG.

### Orientation interne et sortie

Pour une personne, `READING_MAP.md` est la vue dérivée lorsque le besoin est déjà identifiable ; l’agent charge par `DIRECTION/CHARGE`. `START` reste la source normative de classification ; les autres vues (`CHARGE`, `FAST-PATH`, `EXTERNAL-START`) sont des vues dérivées ou conditionnelles.

La sortie de DIRECTION vers ACTION réutilise `ACTION/HANDOFF` ; la phase de chaque champ (avant build, après observation, clôture) est celle de la table de correspondance d’`ACTION/RUN_CARD`. Pour `MODE=DIRECTION`, transmettre aussi la cible/ancre et, lors d’une clôture, les éléments de `creative_close`; ACTION renseigne `closure.direction_status`, `issue`, `verdict` et l’état selon son schéma. Si un champ ne s’applique pas, marquez `N/A-JUSTIFIED` selon ACTION ; ne créez ni statut ni verdict dans DIRECTION.

**Condition d’arrêt de lecture :** arrêtez DIRECTION lorsque mode, risque, décision, scope, contrainte déterminante, premier objet/artefact attendu, owner, prochaine preuve, limite et condition de sortie sont suffisamment explicites pour ACTION. Continuez seulement si une section peut modifier l’un de ces éléments.

### Trois contrats à ne pas mélanger

| Contrat | Question | Sortie attendue |
|---|---|---|
| `ROUTE` | Quelle décision, quel risque et quel mode ? | Mode, risque, capacité et sources à charger. |
| `TARGET` | Quelle position et quel objet faut-il construire ? | Thèse, silhouette, hiérarchie, matière, contenu, preuve, ancre, modal et parti. |
| `HANDOFF` | Que doit exécuter et vérifier ACTION ? | **Avant build** : artefact, scope, preuve attendue, limite, prochaine action et owner. **Après observation** : défaut dominant, correction ou retour recommandé. |

Ces contrats structurent le cadrage sans créer de route, de gate, de statut ou de `RUN_CARD` supplémentaires. `START` possède la classification ; `ACTION` possède la preuve et la clôture ; `SAVOIR` possède le jugement ; `BIBLIOTHEQUE` possède les structures.

### Architecture d’activation

Les modules ci-dessous ne sont pas des formulaires à remplir en parallèle. Ils sont des vues complémentaires d’un même cadrage. Une vue est chargée lorsqu’elle peut modifier la décision indiquée ; sa sortie rejoint la trace existante, puis le lecteur passe au propriétaire suivant.

| Vue | Rôle | Déclencheur | Sortie à transmettre |
|---|---|---|---|
| `START` | Classer | Démarrage de tout run ; si mode ou risque est incertain, ouvrir une clarification ou une reclassification | `MODE`, `RISK`, `DECISION`, `OWNER`, `NEXT-PROOF`, `CAPABILITY-BASIS` |
| `CREATIVE-BOOT` | Ouvrir la boucle créative | Décision visuelle ouverte | Promesse, objet de preuve, geste, `MODAL`/`PARTI`, `FABRICATION` et défaut recherché |
| `VISUAL_TARGET` | Rendre la position pilotable | Première scène ou identité à définir | Thèse, relation, ancre, composition, preuve et rendu attendu |
| `DIRECTION-ATELIER` | Approfondir une position située | Tension, geste, confiance culturelle ou exclusion pouvant modifier la scène | Moment, tension, geste, position, contre-choix et limite |
| `FIRST-OBJECT` | Rendre la première proposition jugeable | Premier rendu à produire ou comparer | Objet complet et dimensions à inspecter |
| `DOUBLE-LOOP` | Organiser l’apprentissage | Observation d’un rendu réel | Défaut dominant, correction visible, réobservation et décision |
| `HANDOFF` | Transmettre à `ACTION` | Construction, preuve ou clôture à engager | Projection complète `ACTION/HANDOFF`, sans statut ni verdict concurrent |

Une seule vue peut suffire pour un delta local. La complétude d’une vue n’est jamais un objectif autonome.

### Carte de lecture canonique et chemin en trente secondes

Classer : `DIRECTION/START`. Charger : `DIRECTION/CHARGE`, seule liste de chargement. Fabriquer : le noyau de la skill, compilé depuis les blocs « noyau » des sources. Vérifier, corriger ou clôturer : `ACTION`, jamais DIRECTION seule.

En trente secondes, nomme : **la décision à changer, le risque dominant, le mode, la capacité minimale et le premier objet que la preuve devra inspecter**. Cette vue accélère l’entrée ; elle ne remplace ni `START`, ni les contrats d’ACTION, ni le jugement situé.

Cette carte est la vue de lecture interne canonique de DIRECTION. `CHARGE`, `FAST-PATH`, `EXTERNAL-START`, la section 0 et le récapitulatif de protection sont des vues dérivées de `START` : elles ne classent pas, ne créent ni nouveau mode, ni nouveau contrat, ni nouvelle condition de sortie et ne peuvent pas contredire `START`. `READING_MAP.md` reste le guide dérivé inter-document. En cas de différence, `START`, les propriétaires de responsabilité et les contrats d’ACTION prévalent.

**Chaîne de lecture interne.** Utilise le document selon la décision à faire évoluer, dans l’ordre de l’architecture d’activation : `START` classe ; `CREATIVE-BOOT` ouvre la décision ; `VISUAL_TARGET` rend la position pilotable ; `DIRECTION-ATELIER` approfondit la direction située lorsque cette profondeur peut changer la décision ; `FIRST-OBJECT` matérialise la cible et rend la promesse jugeable ; `DOUBLE-LOOP` organise l’observation et la correction ; le `HANDOFF` remet à `ACTION` une cible, un artefact, une preuve et une limite explicites. Chaque module doit être chargé pour son gain attendu : meilleure orientation, meilleur premier objet, meilleur jugement, meilleure structure ou meilleure preuve — jamais pour augmenter la procédure.

**Périmètre.** Le système vise à aider une personne, un agent ou une équipe à produire des interfaces et frontends de haute qualité visuelle, sur le web comme sur des plateformes natives telles que Flutter, Swift, Kotlin ou équivalentes. Il vise un premier rendu spécifique, composé, crédible et résolu plutôt qu’un résultat générique ou décoratif. Il vise à augmenter la probabilité d’un travail de niveau expert en rendant explicites des décisions que les meilleures équipes prennent souvent implicitement ; cette efficacité reste `NOT-VERIFIED` (`CHANGELOG`) et s’éprouve par les pilotes. Il ne remplace ni la compétence, ni le jugement situé, ni la revue humaine, et ne garantit ni l’excellence universelle, ni la réussite d’une tâche, ni l’adéquation à tous les publics. Ces propriétés dépendent du contenu réel, du contexte, de la preuve et du jugement situé. Les exemples et runtimes de référence sont souvent web, mais les décisions de hiérarchie, composition, typographie, matière, états et interaction sont portables. L’implémentation traduit ces décisions dans les idiomes réels de la plateforme ; elle ne copie pas mécaniquement des conventions web.

**Capacité positive de DIRECTION.** DIRECTION ne sert pas seulement à éviter une proposition générique : elle vise à augmenter la qualité du cadrage, de la position, de la première scène et de la boucle créative. Elle transforme un brief en relation perceptible entre produit, public, contenu, geste, matière et contrainte ; elle peut requalifier une demande lorsque cela améliore la décision, sans se substituer aux owners de preuve, de structure ou de clôture.

**Priorité.** `P0` porte la direction et le craft visuel ; `P1` protège compréhension, usage et accessibilité ; `P2` traduit la direction dans la plateforme et le runtime réels ; `P3` couvre robustesse, performance, compatibilité et maintien lorsque le risque le requiert. P1 est un plancher non négociable, mais P1–P3 ne doivent jamais servir à justifier une interface générique ou à effacer la signature visuelle de P0. Cette hiérarchie ne permet jamais de retarder un risque critique de tâche, de santé, de sécurité, de confidentialité, de permission ou d’accessibilité au profit du craft : dans ce cas, la protection critique devient la prochaine décision et la prochaine preuve.

**Défaut de qualité visuelle.** Pour toute surface visuelle, identitaire ou UI dont le rendu est un objet direct du run, la première proposition doit être **dirigée, distinctive, construite et polie par défaut**. Elle doit montrer une hiérarchie maîtrisée, une typographie intentionnelle, une composition résolue, une palette cohérente, des assets et composants choisis ou conçus pour le produit, ainsi que les états visuels pertinents lorsque le risque le requiert. Un wireframe générique, une collection de composants sans scène ou un habillage décoratif ne constituent pas une première proposition suffisante lorsque la décision visuelle est ouverte.

Ce défaut élève l’ambition de la première proposition ; il ne crée ni score esthétique, ni style obligatoire, ni garantie de résultat, ni preuve automatique. La singularité reste située par le JTBD, le public, le contexte et la marque.

**Standard créatif.** Lorsque la qualité perceptuelle est une décision du run, le cadrage active aussi la responsabilité de `SAVOIR/CRAFT/CFT-00`. La première proposition vise une présence identifiable, un point de vue, une composition maîtrisée, une culture visuelle transformée, une spécificité liée au produit, une expression cohérente, une désirabilité située et une résolution proportionnée à l’ambition. Ces dimensions sont jugées par des observations et des décisions de craft ; elles ne deviennent ni score, ni statut, ni verdict automatique. Une surface peut être conforme, utilisable et techniquement robuste tout en restant trop générique ou insuffisamment résolue : cet écart doit déclencher une correction de direction ou de polish, pas être compensé par la preuve d’un autre axe. L’usage, l’accessibilité, la robustesse et la faisabilité restent des protections actives ; elles ne doivent pas être sacrifiées au rendu, et le rendu ne doit pas être utilisé pour masquer leur absence de preuve. Pour un correctif strictement local, `LITE` ou `ITER` conservent la structure existante sauf si la décision visuelle elle-même est ouverte.

`CREATIVE-BOOT`, `VISUAL_TARGET` et `DIRECTION-ATELIER` ne demandent pas trois descriptions concurrentes. Lorsque la même information apparaît sous plusieurs noms, conserve-la dans la vue qui la rend décisionnelle et renvoie les autres vues à cette sortie : la promesse devient la thèse si elle est transformée en position, le parti devient une exclusion s’il gouverne la scène, et l’ancre devient une preuve de calibration si elle modifie la composition. Les champs non transformés ne sont pas recopiés.

**Statut de gouvernance.** Une source, un claim daté, un retour externe ou un asset reste local au run tant qu’il ne modifie pas durablement une règle partagée. Seule cette promotion justifie une décision dans `CHANGELOG.md`.

### Comment lire les taxonomies

Ces repères ne fusionnent pas les taxonomies. **Le risque dominant** détermine la protection à préserver et aide à choisir le mode ; **le mode** détermine la proportion de trace et de preuve ; **P0–P3** décrivent l’ordre de protection à examiner dans ce contexte ; **V/U/A/T** sont les axes de questions et de preuve tenus par `ACTION`. Si deux repères semblent entrer en conflit, ne baisse pas la protection : pose une clarification ciblée ou retiens le risque dominant.

### Légende

| Tag | Sens |
|---|---|
| `[ABSOLU]` | Contrat transversal de DIRECTION. |
| `[FORCÉ]` | Chargement ou action déclenché par un signal objectif. |
| `[REQUIS PAR LE MODULE]` | Obligation définie par ACTION, SAVOIR ou BIBLIOTHEQUE dans son propre périmètre. |
| `[RECOMMANDÉ]` | Défaut solide, infléchissable si l’exception est nommée. |
| `[À ADAPTER]` | Point de départ contextuel, jamais validation automatique. |
| `[VEILLE]` | Information datée ou évolutive à vérifier avant de la transformer en règle. |

Légende commune à DIRECTION et SAVOIR pour les seuls tags partagés : `[REQUIS PAR LE MODULE]`, `[À ADAPTER]` et `[VEILLE]`, au même sens. SAVOIR tient sa propre table (« Niveaux d’autorité ») pour ses autres tags ; `[RECOMMANDÉ]` n’y est pas employé.

Les valeurs chiffrées sont des points de départ. **La vérification exigée ne l’est pas.** Une heuristique de craft peut guider une décision ; elle ne devient pas une loi universelle sans portée, source et preuve appropriées. De même, « premium », « beau », « moderne », « innovant » ou « haut de gamme » ne sont jamais des décisions suffisantes : ils doivent être traduits en relation visible, contenu, geste, contrainte ou preuve. Une réponse concise reste valide si elle est située ; la longueur de la trace ne compense jamais son absence de conséquence.

**Repères de vocabulaire.** *Craft* désigne la qualité de fabrication et de résolution du design ; *JTBD* signifie la tâche que la personne cherche réellement à accomplir ; *scope* désigne le périmètre de la preuve ; *grounding* désigne l’ancrage factuel ou contextuel susceptible de modifier la décision ; `BASIS` désigne la base déclarée d’un claim ou d’une capacité.

---

## DIRECTION/START — classer avant d’agir

`START` est le point d’entrée quotidien d’un humain, d’une IA ou d’un pipeline. Il choisit le mode et la prochaine route ; il ne remplace ni les cinq absolus, ni les procédures, ni le jugement. Avant d’ouvrir un run, une proposition de cadrage reste possible (`DIRECTION/SERVICE-BOUNDARY`).

**Source normative de classification.** `DIRECTION/START` est la source normative unique des modes et du risque dominant. `DIRECTION/CHARGE` est la liste de chargement par mode ; `FAST-PATH` est un raccourci pour un delta local ; `EXTERNAL-START` est une vue de transport pour un brief vague. Aucun de ces encadrés ne crée une classification concurrente. En cas de différence, `START` prévaut et le conflit est inscrit dans `CHANGELOG`.

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

**Silence des micro-deltas.** Une correction de libellé, de traduction, d’overflow, de contraste, de focus, d’état ou de wrapping dans un composant existant ne constitue pas à elle seule une décision de style, de technique, d’effet, d’asset ou de structure. Ne charge pas la section `DESIGN-ATLAS` de `SAVOIR.md` pour ce type de delta ; reste sur la route locale tant qu’aucune responsabilité n’est réellement modifiée.

**Règle de conflit.** Si plusieurs signaux sont positifs, découpe le travail lorsque les risques sont indépendants. Deux risques sont indépendants si la preuve de l’un ne dépend pas de la décision de l’autre et si leur owner, leur artefact et leur condition de sortie peuvent être distincts. Sinon, retiens le mode qui protège le risque dominant, sans importer les artefacts sans rapport.

### Entrée minimale

Avant toute construction, vérifie que l’entrée courte rend retrouvables les décisions qui peuvent changer l’artefact :

```text
DECISION — ce qui doit être tranché
RISK — coût d’erreur dominant
SCOPE — surface, état, viewport, consumer ou périmètre concerné
CONSTRAINT — contrainte réelle qui peut changer la décision, dont la destination (démo, prototype ou produit réel) et l’enjeu identitaire
NEXT-PROOF — observation ou test qui permettra de trancher
OWNER — responsable de la décision et de la prochaine action
```

Ce gabarit est une vue d’activation, pas un second schéma : `ACTION/RUN_CARD` reste propriétaire des champs complets, des états, des issues, des verdicts et de la clôture. `OWNER` et `SCOPE` ne sont jamais omis : ils rendent la reprise et la portée vérifiables. Les autres lignes sont omises ou `N/A-JUSTIFIED` si elles ne peuvent rien changer.

### DIRECTION/CREATIVE-BOOT — activer la boucle avant le premier pixel

Pour une décision visuelle ouverte, active avant le build un **Creative Boot** court. Il ne crée ni mode, ni route, ni gate, ni statut, ni score esthétique, ni champ obligatoire concurrent de `RUN_CARD`.

Le boot tient au maximum les décisions suivantes :

```text
DECISION: décision que le premier rendu doit permettre de prendre
PROMISE: promesse à rendre perceptible
PROOF-OBJECT: objet, état, donnée ou relation qui rend la promesse crédible
GESTURE: premier geste ou action attendu
MODAL: ce que n’importe quelle IA produirait ici (structure, palette, typo, assets) ; se nomme avec les marqueurs de vague datés de `SAVOIR/TOOLS`
PARTI: garder ou s’écarter — où et pourquoi au regard de la thèse ; projeté dans `direction.anti_direction`
STRUCTURAL-TENSION: axe(s) de tension selon BIBLIOTHEQUE (un ou deux, `BIBLIOTHEQUE/TENSION`)
STRUCTURAL-SIGNATURE: relation que cette structure rend possible au-delà de l’héritage
CFT-TARGETS: jusqu’à trois qualités créatives prioritaires pour la construction
FABRICATION: moyens réels (assets, marque, polices, composants, génération, sources, contenu) → plafond par couche (structure, typo, couleur, assets, contenu) → construire, construire avec plafond déclaré, demander X ou changer de route ; inclut la base de l’ancre et ce qu’elle ne permet pas d’affirmer
FIRST-OBJECT: artefact complet construit pour rendre les choix jugeables
DOMINANT-DEFECT: défaut perceptuel ou structurel recherché en premier
```

`DIRECTION` possède la promesse, l’objet, le geste, `MODAL`/`PARTI` et `FABRICATION` ; `BIBLIOTHEQUE` possède la tension et la signature structurelles ; `SAVOIR/CRAFT` possède le jugement des qualités de présence et de fabrication ; `ACTION` possède l’observation, la preuve, la correction et la clôture. Les `CFT-TARGETS` sont un foyer de construction, pas un score : les autres dimensions restent applicables lorsqu’un risque ou une décision les active et ne deviennent `N/A-JUSTIFIED` que si elles sont réellement hors périmètre.

<!-- noyau:début MOY-PLAFOND -->
<!-- concept:HON-03 -->
Avant le premier rendu, le boot doit conduire à un artefact complet, crédible et observable — jamais à un wireframe volontairement creux lorsque les capacités sont disponibles ; lorsqu’elles manquent, `FABRICATION` déclare le plafond avant le build et le rendu sort avec la meilleure route de `DIRECTION/VISUAL_TARGET`. Après observation, la boucle d’édition et la trace prennent le relais : **un défaut dominant**, la modification réelle ou la raison de l’arrêt (`DIRECTION/DOUBLE-LOOP`, one-shot).
<!-- noyau:fin MOY-PLAFOND -->

Sa valeur se juge à sa conséquence sur le premier objet, non à la complétude du formulaire ; il peut être omis pour un delta strictement local.

### DIRECTION/DOMAIN-FRAME — adapter le design au domaine

Pour une demande multi-domaines, nouvelle ou ambiguë, complète le cadrage avec les variables qui peuvent changer la structure, l’expression, la preuve ou la profondeur de recherche :

```text
domain: domaine, catégorie et sous-contexte
audience: public et situation d’usage
expertise: niveau de connaissance attendu
jtbd: tâche principale et résultat attendu
trust_model: ce qui doit inspirer confiance et ce qui pourrait la détruire
critical_actions: gestes, décisions, permissions ou récupérations sensibles
domain_conventions: conventions utiles, contraintes et conventions à contester
cultural_context: langue, codes, références et risques de mauvaise lecture
originality_tolerance: `low`, `medium`, `high` ou `unknown`, selon la marge d’écart compatible avec la tâche et le risque
proof_requirements: ce qui doit être compris, démontré, mesuré ou testé
domain_risks: risques propres au domaine et conséquences d’erreur
required_research: recherches nécessaires avant décision ou build
critical_states: états, erreurs, permissions et récupérations critiques
design_constraints: contraintes de conception, contenu, plateforme ou gouvernance
evidence_plan: méthode, scope, artefact, limite et prochaine preuve
policy_profile: `risk_triggers`, `required_controls`, `risk_coverage`, `depth_rules` et `contraindications`
```

Ce gabarit reprend exactement les propriétés de `gouvernance/schemas/domain_frame.schema.json`. Toute projection machine doit utiliser ces clés et compléter les champs requis ; aucune clé abrégée telle que `DEPTH-TRIGGER` ne doit être sérialisée. `policy_profile.depth_rules` porte les conditions qui justifient une recherche, une variante, un prototype ou une preuve supplémentaire.

Le `DOMAIN-FRAME` n’est ni un nouveau mode ni une taxonomie de secteurs. Il sert à décider ce qui mérite d’être recherché et ce qui doit être adapté. Ne déduis pas l’expression du domaine par stéréotype : un produit financier n’est pas minimaliste par défaut, un produit culturel n’est pas maximaliste par défaut et un outil technique n’est pas cyberpunk par défaut. Le domaine contraint la décision ; il ne fournit pas à lui seul la direction.

La profondeur augmente lorsqu’un élément peut modifier la décision : public ou JTBD incertain, confiance critique, contexte culturel sensible, convention inconnue, forte conséquence d’erreur, contenu réel indisponible, ou écart créatif nécessitant une calibration. Lorsque ces déclencheurs sont absents et que le périmètre est stable, reste sur le chemin court. Lorsque plusieurs déclencheurs sont actifs, recherche, structure, UI/UX et preuve doivent être renforcés ensemble plutôt que compensés par une couche esthétique.

### Sortie immédiate

Crée ou mets à jour une ligne de run :

> `RUN — [ID] — [MODE] — [décision dominante] — [risque principal] — [preuve suivante] — [état].`

La ligne de run doit exister dès qu’une action de production, une vérification ou un changement d’état commence. Lorsque le risque ou la reprise l’exige, l’owner doit être retrouvable depuis cette ligne ou son identifiant.

Au lancement, ajoute :

> `DECISION-INTENT — [décision que la procédure doit permettre de trancher].`

Après une observation qui modifie, confirme ou abandonne effectivement une décision, ajoute :

> `DECISION-CHANGE — [décision effectivement changée, confirmée ou abandonnée grâce à la procédure].`

À la clôture, si aucune décision n’a été changée, confirmée ou abandonnée, les valeurs de repli d’`ACTION/STATUS` s’appliquent : `N/A-JUSTIFIED` lorsqu’aucune conséquence n’était applicable, avec la raison, le risque de continuer sans changement et la prochaine action éventuelle ; `NOT-OBSERVED` lorsqu’une conséquence attendue n’a pas été observée. Ne déclare jamais un changement avant qu’une observation ne l’ait rendu réel.

### Mémoire de lancement et renvoi de `RUN_CARD`

La ligne de run constitue une mémoire de lancement, sous-ensemble de lancement de `ACTION/HANDOFF`, non un handoff ni une `RUN_CARD` ; la ligne compacte de la sortie immédiate en est l’affichage : `ID`, `MODE`, `DECISION`, `RISK`, `SCOPE`, `ARTIFACT` attendu, `OWNER`, `NEXT-PROOF`, `LIMIT` et `EXIT-CONDITION`. Elle peut vivre dans un ticket, un manifeste de projet, un espace de travail ou un fichier local.

Le schéma complet de `RUN_CARD` appartient exclusivement à **`ACTION/RUN_CARD`**. DIRECTION ne le reproduit pas et transmet la projection `ACTION/HANDOFF`; les champs non applicables sont `N/A-JUSTIFIED`, les observations non vérifiées restent `NOT-VERIFIED`. Une surface `DIRECTION` qui accepte avec V en `PASS` ou `PASS-WITH-RESERVATION`, dont le risque V/craft est dominant ou dont le verdict V dépend d’une intention encore non confrontée doit suivre `ACTION/GATE-B — B1b` avant clôture. Pour une `RUN_CARD DIRECTION` en `CLOSED`, `creative_close` contient `presence`, `signature`, `craft_detail`, `dominant_defect` et `next_polish_action` ; `direction_status`, `issue` et `verdict` restent les registres séparés d’ACTION.

Un run `STANDARD`, `DIRECTION` ou `SYSTÈME` persistant, partagé ou audité conserve une trace persistante (trace complète, `ACTION/HANDOFF`) ; sinon, la trace légère suffit. `ITER` peut s’appuyer sur la mémoire locale du projet si la direction précédente, le périmètre, le dernier artefact, la décision, la preuve et le risque restant sont retrouvables. `LITE` peut se limiter à la ligne de run et au verdict court si l’artefact et le risque restent retrouvables.

---

## DIRECTION/CHARGE — classer, puis charger

<!-- noyau:début CHARGE-REGLE -->
> **Règle de vitesse.** Ouvre `START` (en `LITE`, l’arbre `DIRECTION/START/TREE` suffit), classe le mode, charge la ligne de ce mode, puis ajoute seulement le module susceptible de changer la prochaine décision. Pour une relation de craft ouverte, même dans un correctif local, les gestes de `SAVOIR/STATE` sont dans le noyau ; n’approfondis que le savoir qui peut modifier l’intervention, sans ouvrir de nouvelle direction. Avant de construire, déclare le mode, la décision dominante, le risque principal, la preuve minimale et la condition d’arrêt (absolu 4) : une ligne suffit, dans la trace.

**Retrouver un savoir utile.** Si la route pertinente est inconnue, qu’une notion semble absente ou qu’un signal de finesse reste sans intervention concrète, utilise `python3 scripts/read_route.py --trouver "terme"` avec un terme lié au signal. La recherche porte par défaut sur les cinq sources normatives : mots entiers et quelques synonymes ou traductions courants (« premier écran » trouve « premier contact »), puis correspondance partielle, puis mots séparés sur une même ligne ; elle classe les routes et montre les premières (`--tout` pour toutes). Elle ne comprend pas le sens : sans résultat, essaie une reformulation ciblée puis déclare la limite de recherche, sans conclure à l’absence du savoir. `python3 scripts/read_route.py --sommaire` liste les routes et leur rôle ; `--sommaire LOCATOR` donne les sous-sections d’une route et leurs locators. `SAVOIR/READ` dit comment charger SAVOIR ; `SAVOIR/ROUTING` donne la route principale de chaque question de jugement. Lis la route pertinente en entier, sans extrait, avec `scripts/read_route.py LOCATOR` et applique son contenu à la décision ouverte ; les blocs déjà présents dans ce noyau y sont remplacés par un renvoi à leur section (`--complet` les affiche). Si le lecteur est indisponible, cherche le terme dans la source propriétaire disponible et lis le passage avec son contexte. Reste dans la ligne du mode : cette recherche n’ajoute ni liste de chargement, ni lecture exhaustive, ni nouvelle direction.

Si plusieurs propriétaires peuvent éclairer une relation ouverte, consulte les connexions situées de `READING_MAP.md` avec `python3 scripts/read_route.py --connexions`. Cette aide dérivée conserve les conditions et limites ; elle ne remplace ni la ligne de CHARGE ni les sources.
<!-- noyau:fin CHARGE-REGLE -->

Une intention perceptuelle encore sans levier de construction active la traduction de `BIBLIOTHEQUE/SELECT` dans le périmètre du mode ; une route connue se lit directement. Si seule sa fabrication reste ouverte, utilise la calibration de `BIBLIOTHEQUE/CONTRACTS`. Ce passage relie direction, structure et gestes de SAVOIR sans charger le catalogue entier ni ajouter une seconde liste de chargement.

`CHARGE` est la seule liste de chargement du corpus : la skill en porte une copie générée, les façades y renvoient. Les modes restent définis par `START` ; les verdicts et les sorties, par `ACTION`.

<!-- noyau:début CHARGE-TABLE -->
| Mode | Charger d’abord | Ajouter seulement si cela change la décision |
|---|---|---|
| **LITE** | `ACTION/RUN-LITE`, `ACTION/FAST-PATH`, `ACTION/GATE-A` applicable ; de Gate B, seulement les familles de preuve (`ACTION/GATE-B/B2`) et la sortie compacte (`ACTION/GATE-B/B6`). Sans risque critique touché — voir Protection de niveau (`DIRECTION/START`). | Une route SAVOIR ou BIBLIOTHEQUE si le correctif touche réellement le jugement ou la structure. `SAVOIR/DESIGN-ATLAS` reste silencieux ; une famille seule ne reclassifie pas. Si le périmètre, le blast radius, la responsabilité ou le risque dominant change la décision, reviens à `DIRECTION/START` puis reclassifie vers `ITER`, `STANDARD`, `DIRECTION` ou `SYSTÈME`. |
| **ITER** | Mémoire locale (direction existante), `ACTION/RUN-ITER`, non-régression pertinente, `ACTION/GATE-A` applicable et `ACTION/GATE-B` du risque touché. Sans risque critique touché — voir Protection de niveau (`DIRECTION/START`). | `ACTION/GATE-C` si le craft change ; une route SAVOIR ; BIBLIOTHEQUE seulement si support, grille, scène ou objet change. `SAVOIR/DESIGN-ATLAS` reste silencieux dans le même périmètre ; une famille seule ne reclassifie pas. Si le périmètre, la responsabilité ou le risque dominant change la décision, reviens à `DIRECTION/START`. Les corrections de libellé, overflow, contraste, focus, état ou wrapping restent locales. |
| **STANDARD** | `ACTION/RUN-STANDARD` ; `ACTION/UI-UX-REALITY` si la surface UI/UX est nouvelle ou substantiellement modifiée ; `BIBLIOTHEQUE/SELECT` si la structure est ouverte ; Gates A et B ciblés (`ACTION/GATE-A`, `ACTION/GATE-B`). | `SAVOIR/FRAME` si le cadrage est ambigu ; `DIRECTION/DOMAIN-FRAME` si la demande est nouvelle, ambiguë ou multi-domaines et que le domaine peut changer la structure, l’expression ou la preuve ; une route BIBLIOTHEQUE structurante et la route SAVOIR du risque dominant. |
| **DIRECTION** | `DIRECTION/EXTERNAL-START` si le brief est vague, `DIRECTION/CREATIVE-BOOT`, `DIRECTION/VISUAL_TARGET`, `DIRECTION/FIRST-OBJECT`, `SAVOIR/TYPE` (voix comparées sur le vrai titre), `ACTION/FIRST-RENDER`, `ACTION/UI-UX-REALITY` si la surface UI/UX est nouvelle ou substantiellement modifiée, `ACTION/RUN-DIRECTION` avec `ACTION/PIPELINE-DIRECTION` et `ACTION/VISUAL_PROOF` qu’il exécute, puis `ACTION/GATE-A` et `ACTION/GATE-C` applicables ; en trace complète (`ACTION/HANDOFF`), `ACTION/GATE-B`, `ACTION/RUN_CARD` et `ACTION/CLOSE-PACKAGE`. | Tranche chaque route de cette colonne, ouverte ou écartée avec sa raison, en une ligne de trace. `DIRECTION/DOUBLE-LOOP`, `ACTION/ROUTING` ou `SAVOIR/CRAFT/CFT-00` si la décision l’exige (la boucle d’édition et les gestes sont dans le noyau) ; `DIRECTION/DIRECTION-ATELIER` si la tension, le geste produit ou un anti-choix peuvent modifier la première scène ; `SAVOIR/FRAME`, `SAVOIR/CRAFT`, `SAVOIR/SOURCE` et `BIBLIOTHEQUE/SELECT` si nécessaires ; `BIBLIOTHEQUE/SEQUENCE` si la page compte plusieurs sections ; `DIRECTION/DOMAIN-FRAME` si la demande est nouvelle, ambiguë ou multi-domaines et que le domaine peut changer la structure, l’expression ou la preuve. Charge `SAVOIR/STYLE` seulement si le choix de style peut modifier une décision de composition, de voix, de matière, de contraste ou de relation produit ; jamais comme catalogue automatique. `SAVOIR/CRAFT/CFT-03`, `SAVOIR/STATE` ou `SAVOIR/INTEGRITY` si un détail final peut modifier le caractère, un état, la hiérarchie, la densité ou la robustesse ; `SAVOIR/INTEGRITY` avant un verdict (trace complète). |
| **SYSTÈME** | `ACTION/RUN-SYSTEM` ; `BIBLIOTHEQUE/COMPONENTS` si un composant change. | `SAVOIR/SYSTEM` ; `CHANGELOG` si une règle partagée change. |
<!-- noyau:fin CHARGE-TABLE -->

<!-- noyau:début CHARGE-FIN -->
La clôture de chaque mode est `ACTION/CLOSE-PACKAGE`, en trace complète ; en trace légère, le run s’arrête à la proposition (`ACTION/HANDOFF`). Pour l’agent, les blocs « noyau » compilés dans la skill tiennent lieu de lecture de fabrication ; README, QUICKSTART et READING_MAP sont des lectures d’orientation pour les humains ; l’agent n’interroge READING_MAP que par `--connexions`. Tags du noyau : `[REQUIS PAR LE MODULE — scope]`, obligation dans ce scope (sinon `NOT-VERIFIED`, ou `N/A-JUSTIFIED` motivé) ; `[MÉTHODE]`, procédure à adapter.
<!-- noyau:fin CHARGE-FIN -->

**Déclenchement de l’atlas.** Si aucune famille ne peut être reliée à une décision modifiable, n’ouvre pas `SAVOIR/DESIGN-ATLAS` ; reste sur la route existante. Si le signal est ambigu, pose une seule clarification ciblée ou reviens à `DIRECTION/START` pour classer le mode et le risque. Si un risque critique apparaît, reclassifie avant de charger une famille. L’atlas ne sert jamais à résoudre par catalogue un JTBD, un mode ou une intention manquante.

**Règle de passage.** `DIRECTION` décide du mode et du risque dominant ; `ACTION` des preuves exécutables, gates, statuts et verdicts ; `SAVOIR` du jugement ; `BIBLIOTHEQUE` de la structure ; `CHANGELOG` de la gouvernance du système.

### DIRECTION/FAST-PATH — renvoi vers l’exécution courte

`FAST-PATH` est une vue dérivée de `START`, non une porte d’entrée concurrente. Pour un correctif local ou une décision déjà presque tranchée, les quatre questions sont celles d’`ACTION/FAST-PATH`, seul bloc d’exécution courte, à poser avant de charger un module.

Si la réponse à la quatrième question (ce que la preuve changera) est « rien », ne lance pas un nouveau protocole et ne charge pas l’atlas. Conserve l’existant et omets la ligne sans effet ; utilise `N/A-JUSTIFIED` seulement si aucun contrôle ou aucune décision applicable ne peut changer dans le scope déclaré. `EXPLORATORY` reste réservé au cas où un rendu observable existe mais qu’une preuve requise manque. En exploration, `DECISION-INTENT` peut être une hypothèse à formuler ; `DECISION-CHANGE` devient obligatoire seulement lorsque le run prétend qu’une décision de production a été changée, confirmée ou abandonnée.

---

## 0. Classification du mode, preuve et capacité

`START` est la source normative de classification. Cette section est une vue contractuelle des capacités, de la preuve minimale et de la condition d’arrêt ; elle ne redéfinit pas l’ordre de routage. Pour `DIRECTION`, `ACTION` renseigne séparément `closure.state`, `closure.issue`, `closure.direction_status`, `closure.verdict` et `closure.limitations` ; `HELD` n’équivaut jamais à `ACCEPTED`.

Classe d’abord la tâche ; vérifie ensuite les capacités nécessaires pour la produire et la vérifier. Les outils disponibles déterminent la voie de preuve et le statut de vérification, jamais une rétrogradation silencieuse du mode.

Portée : `DIRECTION/START`. Preuve minimale : `ACTION/PRECONDITION` et `ACTION/RUN-<MODE>`. Condition d’arrêt : `ACTION/CLOSE-EXIT-CHECK`.

Les axes détaillés de jugement et les statuts V/U/A/T sont canoniques dans `ACTION`. Ne transforme pas une note de jugement en verdict global. Les axes V/U/A/T sont évalués lorsque leurs risques sont touchés ; lorsqu’un axe ne concerne pas le run, il est `N/A-JUSTIFIED`, pas implicitement ignoré. Les lettres A/B/C désignent les gates, jamais les axes de verdict.

### ITER se souvient

`ITER` n’est possible que si la direction précédente, le périmètre, le dernier artefact, la décision, la preuve et le risque restant sont retrouvables dans la session, la trace légère (ligne de thèse), la `RUN_CARD` ou le manifeste local. Si la direction est absente, reconstitue le contexte et reclassifie en `LITE`, `STANDARD`, `DIRECTION` ou `SYSTÈME` selon la décision retrouvée. Si la retouche remet en cause un axe de direction, passe en `DIRECTION`. Si elle touche une règle partagée, passe en `SYSTÈME`.

---

## 2. Routage — quoi charger et quand

Ne charge pas `ACTION`, `SAVOIR` et `BIBLIOTHEQUE` en bloc. Charge la route canonique déclenchée par le signal qui peut modifier la prochaine décision. Si un fichier ou une preuve manque, déclare la limite et applique le statut prévu ; n’invente pas son contenu.

### Déclencheurs critiques

Ces déclencheurs disent quand ajouter une route à la ligne du mode dans `DIRECTION/CHARGE` ; ils ne forment pas une seconde liste de chargement.

| Signal | Charger ou exécuter | Statut |
|---|---|---|
| Surface identitaire | Après `DIRECTION/START`, `ACTION/RUN-DIRECTION`; charger `SAVOIR/CRAFT`, `SAVOIR/TYPE` ou `SAVOIR/SOURCE` seulement si la composition, la typographie, l’ancrage ou le sourcing peuvent modifier la décision. | `[FORCÉ]` pour la route ACTION ; conditionnel pour les routes SAVOIR |
| Mode `DIRECTION` | Après `DIRECTION/START`, `ACTION/RUN-DIRECTION`, puis le pipeline par étapes. | `[FORCÉ]` |
| Toute livraison | `ACTION/RUN-*`, puis les gates applicables. | `[FORCÉ]` |
| Asset, motion, scène ou type spécifique | Contrat correspondant d’ACTION, route SAVOIR nécessaire ; pour une scène, `BIBLIOTHEQUE/SELECT` puis la route `BIBLIOTHEQUE/SCENE` retenue. | `[FORCÉ]` si la capacité est requise. |
| Retouche `ITER` | `RUN_CARD` ou manifeste local ; charger `SAVOIR/INTEGRITY` si une question de limite, délégation, capacité ou théâtre procédural est active avant verdict. | Conditionnel |
| Doute sur l’application d’une règle | `SAVOIR/INTEGRITY`. | `[FORCÉ]` |
| Ancre absente pour une surface identitaire | En exploration : limite déclarée, run `EXPLORATORY`. Avant l’acceptation : retour à l’ancrage, ou statut prévu par ACTION (absolu 2). | `[FORCÉ]` |
| FAIL exigé malgré un gate | Protocole `FAIL-ASSUMED` d’ACTION. | `[REQUIS PAR LE MODULE]` |
| Motif possiblement générique ou réflexe | Test motivation/construction `SAVOIR/CRAFT/CFT-01` ; conséquence de gate `ACTION/ANTI-SLOP`. | `[REQUIS PAR LE MODULE]` |
| Détail final susceptible de modifier le caractère, l’état, la hiérarchie, la densité ou la robustesse d’une surface `DIRECTION` | `SAVOIR/CRAFT/CFT-03` (composition, densité et harmonie), `SAVOIR/STATE` ou `SAVOIR/INTEGRITY` selon la question ouverte, et capture rendue. | Conditionnel : colonne « Ajouter seulement si » de `DIRECTION/CHARGE` |

### Index à la demande

| Besoin | Route principale |
|---|---|
| Nouvelle structure d’écran | Après la classification par `DIRECTION/START` (une nouvelle structure peut relever de `STANDARD`, `DIRECTION` ou `SYSTÈME`), `BIBLIOTHEQUE/SELECT`, puis la route ACTION du mode. |
| Cadrage ambigu | `SAVOIR/FRAME`. |
| Direction, matière ou composition | `SAVOIR/CRAFT`. |
| Typographie | `SAVOIR/TYPE`. |
| Ancre ou sourcing visuel | `SAVOIR/SOURCE`. |
| Famille de design, technique, effet, asset ou médium | Après classification, décision et risque, section `DESIGN-ATLAS` de `SAVOIR.md`, puis la route spécialisée seulement si elle peut modifier la décision ; retour à `START` si le risque ou le mode change. |
| Profil de style | `SAVOIR/STYLE`. |
| Tokens ou blast radius partagé | `SAVOIR/SYSTEM` et `ACTION/RUN-SYSTEM`. |
| Contexte critique, responsive, performance ou motion | `SAVOIR/CONTEXT`. |
| Technique ou compatibilité | `SAVOIR/TECH`. |
| Limite, délégation ou théâtre procédural | `SAVOIR/INTEGRITY`. |
| Claim daté ou outil externe | `SAVOIR/TOOLS`, avec source, date, portée et limite dans la trace locale du run. |

Les routes stables sont les routes quotidiennes. Les anciens renvois de section sont documentés dans la table de migration de `CHANGELOG.md` et ne doivent jamais servir d’instruction principale à un nouveau run.

---
