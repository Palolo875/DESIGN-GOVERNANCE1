# SAVOIR — Bibliothèque de jugement, craft et production

**Design Governance V1 — expérimentation maintenue.** Cette V1 est un cadre de travail en évaluation ; elle n’est pas présentée comme une release publique stabilisée. Ses limites, preuves et conditions d’usage restent explicites. SAVOIR porte le jugement de design : craft, style, contenu, contexte, technique, sources, intégrité et limites de ce qui peut être affirmé.

## Responsabilité

SAVOIR explique **comment exercer le jugement** : cadrer, choisir, comparer, retirer, vérifier et reconnaître une limite. Il contient les fondations, le craft, les profils de style, la production, la veille et la gouvernance de principes.

**Capacité positive de SAVOIR.** SAVOIR transforme une impression visuelle ou une question de craft en décision située : il aide à comprendre ce qui doit être perceptible, à choisir les leviers de composition et de fabrication, à comparer des options, à retirer ce qui détourne l’attention et à formuler une limite honnête. Il augmente la précision du jugement et la qualité de l’artefact ; il ne remplace ni l’observation réelle d’ACTION, ni la décision de clôture, ni le contexte humain.

**Chemin par problème.** Charge SAVOIR lorsqu’une décision de jugement peut modifier le prochain artefact ou sa preuve : `FRAME` pour le problème, le public et le compromis ; `CRAFT` pour la composition et la fabrication ; `TYPE`, `STATE` ou `CONTEXT` pour la lisibilité, les états et les contraintes ; `SOURCE`, `STYLE`, `SYSTEM`, `TECH`, `TOOLS` ou `INTEGRITY` seulement lorsque leur question est active. Le bénéfice attendu de chaque route doit être identifiable avant son chargement.

SAVOIR ne remplace pas :

| Document | Responsabilité |
|---|---|
| `DIRECTION.md` | Rôle, cinq absolus, classification, routage général et capacité. |
| `ACTION.md` | Routes de run, preuves, gates, verdicts et maintenance. |
| `BIBLIOTHEQUE.md` | Structures, supports, grilles, scènes, objets, micro-interfaces et composants. |
| `CHANGELOG.md` | État de release, changements futurs, pilotes optionnels et décisions de gouvernance. |

> Un principe SAVOIR guide une décision ; une méthode décrit comment formuler la raison ; une preuve ACTION établit ce qui a été observé ou mesuré. Aucun principe, ancre, profil ou texte de justification ne produit seul un `PASS` d’usage, d’accessibilité ou de qualité.

---

### Orientation interne et sortie vers ACTION

`SAVOIR/ROUTING` est la carte de décision principale de ce fichier. Commencez par une seule route principale ; ajoutez une route de renvoi uniquement si elle peut modifier la décision, la preuve ou la limite. `READING_MAP.md` fournit une vue dérivée des déclencheurs et du non-chargement ; il ne remplace ni DIRECTION ni ACTION.

La sortie de SAVOIR n’est pas un verdict. Elle doit transmettre à ACTION la décision jugée, le principe ou la méthode utilisés, la conséquence observable, la preuve attendue, la limite, le propriétaire et la prochaine preuve. Si aucune décision ne peut changer, ne chargez pas une route supplémentaire. À la clôture, si aucune décision n’est changée, confirmée ou abandonnée, les valeurs de repli d’`ACTION/STATUS` s’appliquent : `N/A-JUSTIFIED` lorsqu’aucune conséquence n’était applicable, `NOT-OBSERVED` lorsqu’une conséquence attendue n’a pas été observée.

**Condition d’arrêt de lecture :** arrêter lorsque la question de jugement, le levier choisi, la contre-indication, la limite et la prochaine observation sont explicites.

## SAVOIR/READ — comment utiliser cette bibliothèque

`DIRECTION` détermine **si** une route est requise. `ACTION` détermine **quelle preuve** et quelle sortie sont nécessaires. `SAVOIR` explique **comment juger** dans le domaine concerné.

Ne charge jamais l’ensemble de SAVOIR par réflexe. Charge typiquement zéro à deux routes ; une route par question active (CRAFT, TYPE, SOURCE, CONTEXT…) ; zéro route est valide lorsqu’aucune responsabilité de jugement ne change. Ajoute une route seulement si elle peut modifier la prochaine décision ou le statut de preuve.

**Chemin minimal.** Décide d’abord la décision et le risque ; charge ensuite la route SAVOIR principale, ou aucune si le changement reste local. Ajoute une route seulement si elle change une question, une preuve ou une limite ; `ACTION` reste propriétaire des preuves, des gates, des verdicts et de la clôture. Un tag `[REQUIS PAR LE MODULE — scope]` indique qu’une responsabilité devient applicable dans le périmètre déclaré ; il n’impose pas de charger toute la bibliothèque, mais d’exécuter ou de tracer honnêtement le contrôle concerné selon le contrat d’ACTION. Sur le chemin d’un run, le plancher de ces obligations est compilé dans le noyau de la skill (composition, typographie, couleur, états, vérité) ; leur détail s’applique lorsque la route est chargée.

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

Les routes stables suivantes sont les routes quotidiennes. Les anciens identifiants de section sont documentés dans la table de migration de `CHANGELOG.md` et ne doivent pas être utilisés comme instructions actives.

## SAVOIR/ROUTING — routes stables

Une question possède une route principale. Les autres routes sont des renvois qui ne créent pas une seconde procédure.

| Question | Route principale | Renvoi |
|---|---|---|
| Public, JTBD, décision, compromis | `SAVOIR/FRAME` | `ACTION` pour preuve et sortie. |
| Direction, matière, composition, émotion | `SAVOIR/CRAFT` | `SOURCE` ou `STYLE` si nécessaire. |
| Langue, lecture, données, ton | `SAVOIR/TYPE` | `CONTEXT` pour accessibilité et `ACTION` pour preuve. |
| États, contenu extrême, récupération | `SAVOIR/STATE` | `CONTEXT` et `ACTION/GATE-A`. |
| Ancre, référence, asset, droit | `SAVOIR/SOURCE` | `TOOLS` pour claims et `ACTION` pour trace. |
| Profil ou dial d’expression | `SAVOIR/STYLE` | `CRAFT` et `BIBLIOTHEQUE`. |
| Token, consumer, composant partagé | `SAVOIR/SYSTEM` | `ACTION/RUN-SYSTEM`. |
| Accessibilité, responsive, performance, motion, risque critique | `SAVOIR/CONTEXT` | `TECH` ; `ACTION/GATE-A` pour le contrôle objectivable et l’axe `T` dans la portée de preuve d’ACTION. |
| Technique, compatibilité, mesure | `SAVOIR/TECH` | `TOOLS` si claim daté. |
| Source, tendance, outil, claim | `SAVOIR/TOOLS` | `CHANGELOG` si promotion. |
| Récitation, limite, délégation | `SAVOIR/INTEGRITY` | `ACTION` pour issue et verdict. |

---

# SAVOIR/FRAME — fondations et cadrage

## FND-01 — principe fondateur

[DURABLE] Une interface senior ne cherche pas à paraître différente par défaut. Elle choisit une réponse appropriée, hiérarchise ce qui compte, retire ce qui détourne l’attention et tient sa décision dans les détails.

**Portée.** Il s’agit d’un principe de jugement et non d’une loi empirique. Sa valeur se vérifie par les décisions qu’il permet de prendre et les artefacts qu’il aide à produire.

Trois lois organisent l’ordre de jugement :

1. **Intention avant décoration.** Chaque élément sert une tâche, une émotion choisie ou une information. Si sa justification ne relie pas l’élément au produit, le retrait est le défaut raisonnable.
2. **Retenue avant accumulation.** La valeur perçue vient d’un rapport juste entre vide, précision, contenu et craft, jamais d’un empilement d’effets.
3. **Cohérence systémique avant créativité locale.** Tokens, états, grilles et conventions cohérentes valent mieux que des gestes brillants isolés.

> Aucun signal de craft — matière, effet, typographie expressive, asymétrie ou motion — ne vaut comme qualité s’il ne sert pas le JTBD, la compréhension ou la direction retenue.

### Premium perçu comme heuristique de jugement

[OPINION DE SYSTÈME] Pour une revue de surface, le caractère premium peut être examiné comme une relation entre **clarté, cohérence, précision, singularité maîtrisée et confiance**. Cette formule n’est ni une mesure scientifique, ni un score, ni un verdict. Elle sert uniquement à poser une question de critique : où la valeur perçue est-elle soutenue ou affaiblie par la structure, le système visuel, les détails, les états et le comportement ?

Ne déduis jamais le premium d’un style minimaliste, d’une palette sombre, d’une grande typographie ou d’un espace généreux. Une direction peut être éditoriale, technique, chaleureuse, colorée, tactile ou ludique ; elle reste située si ses choix servent le JTBD, la compréhension, la confiance et la spécificité du produit. Si la clarté ou la confiance tombe, aucun polish expressif ne compense silencieusement cette perte.

### Comprendre, ouvrir, converger, prouver

[MÉTHODE] Pour une décision créative ou identitaire, alterne quatre mouvements sans créer une nouvelle route : **comprendre** le public, le JTBD, les contraintes et le risque ; **ouvrir** le champ par plusieurs directions réellement distinctes ; **converger** vers une proposition principale et, seulement si utile, une alternative qui change une décision ; **prouver** par un artefact réel, une observation dans le scope déclaré et une limite explicite.

Un moodboard, une référence ou une rationale doit être annoté par la décision qu’il peut modifier : composition, lumière, densité, matière, typographie, rythme, contenu ou ton. Une belle référence sans conséquence observable reste une ancre de jugement, jamais une preuve. La sélection fait partie du craft : retirer les variantes faibles et les éléments décoratifs qui ne changent ni la compréhension, ni la tâche, ni la direction, ni la preuve.

### Singularité sans rejet des conventions

<!-- noyau:début COMP-SINGULARITE -->
Le test de singularité demande : si le logo et le nom disparaissent, qu’est-ce qui reste spécifique au produit ? La réponse peut être une donnée, une tâche, une hiérarchie, une voix, une densité, une interaction, une microcopie ou un traitement matériel.
<!-- noyau:fin COMP-SINGULARITE -->

La singularité n’exige pas une structure spectaculaire lorsque la convention de genre sert mieux l’usage. La convergence de genre est légitime lorsque la structure partagée répond à un besoin connu et que contenu, états, données, microcopie et craft sont propres au produit.

Le recipe-slop apparaît lorsque structure, copie et détails deviennent interchangeables ou copiés sans adaptation. Utilise `ACTION/ANTI-SLOP` avant de flaguer une ressemblance comme défaut.

L’ordre de décision reste : **JTBD → structure → hiérarchie → lisibilité → accessibilité → système visuel → polish**.

Une architecture faible ne se répare pas par un dégradé, une typographie rare ou de la motion. La singularité doit survivre aux états, au contenu long, au responsive et à la récupération. Une homepage spécifique qui devient générique dans l’usage n’est pas une direction tenue.

### Grammaire positive de composition

<!-- noyau:début COMP-GRAMMAIRE -->
Lorsque la décision visuelle est ouverte, construis dans cet ordre : **intention → tension → foyer → masse → rythme → matière et type → contenu réel → états → résolution → retenue**. Cette séquence n’est ni une recette de style ni une checklist obligatoire ; elle vérifie que les choix se renforcent au lieu d’être ajoutés séparément.

| Élément | Question de composition |
|---|---|
| **Intention** | Quelle promesse, tâche ou relation doit être rendue crédible ? |
| **Tension** | Quelle polarité productive donne de l’énergie à la proposition sans nuire à la compréhension ? |
| **Foyer et masse** | Quel objet ou geste domine, où se trouve le poids visuel et pourquoi ? |
| **Rythme** | Comment le regard, la lecture ou la révélation progressent-ils ? |
| **Matière et type** | Quelle surface, voix, typographie, donnée ou absence d’asset porte cette relation ? |
| **Résolution et retenue** | Quels états, contenus, contraintes et détails doivent déjà tenir, et qu’est-il volontairement retiré ? |

Une proposition est forte lorsque sa beauté vient d’une relation tenue entre produit, composition, contenu, matière, type, geste et contrainte. Elle n’est pas forte parce qu’elle accumule des effets, ni parce qu’elle s’écarte arbitrairement d’une convention.
<!-- noyau:fin COMP-GRAMMAIRE -->

### Pluralité esthétique et goût situé

[À ADAPTER] L’anti-slop, la retenue, le premium et la maturité ne constituent pas un canon visuel unique. Une direction peut être calme ou énergique, minimale ou dense, populaire ou sophistiquée, ludique ou institutionnelle, étrange ou familière, maximaliste ou silencieuse ; elle est jugée par son adéquation au produit, au public, au médium, au contexte culturel et à l’ambition déclarée, non par sa proximité avec un style dominant.

Avant de rejeter une expression forte comme gratuite, vérifie qu’elle ne porte pas une fonction de présence, de mémoire, d’émotion, de culture, de voix ou de différenciation. Avant de qualifier une solution de premium, nomme le contexte qui rend cette qualité pertinente et les personnes pour lesquelles elle doit inspirer confiance. Une préférence personnelle ou professionnelle ne devient pas une règle générale par le seul emploi de termes comme « senior », « cultivé », « mature », « beau » ou « haut de gamme ».

Lorsque plusieurs regards sont disponibles et que l’enjeu est identitaire, culturel ou irréversible, cherche un contrepoint pertinent : utilisateur concerné, expert du domaine, regard culturel situé, designer différent ou responsable produit. Le regard externe ne garantit ni neutralité ni absence de biais ; il rend seulement le jugement plus contestable et moins dépendant d’une seule autorité.

Une revue de pluralité ne demande pas de produire des variantes artificielles. Elle demande de pouvoir répondre à trois questions : **quelle expression valide est rendue possible par le contexte, quelle expression serait injustement disqualifiée par un canon implicite, et quelle observation permettrait de distinguer préférence personnelle, inadéquation réelle et risque critique ?**

## FND-02 — compromis

[DURABLE] Il n’existe pas de solution qui maximise tout. Une décision senior nomme la tension, choisit ce qui gagne pour une raison située et rend visible ce qui reste à risque.

Utilise ce format :

> **Décision.** Je privilégie X au détriment de Y parce que Z.  
> **Risque résiduel.** Ce qui peut rester moins bon ou moins couvert.  
> **Réversibilité / signal.** Ce qui ferait revenir sur la décision.  
> **Owner / prochaine preuve.** Qui peut reconsidérer et quelle observation déclenchera la revue.

Les compromis alimentent les axes V/U/A/T d’ACTION sans devenir une note concurrente. Un effet qui dégrade usage, performance, accessibilité ou confiance est une dette explicitée, jamais un sacrifice silencieux.

## FND-03 — cadrage et preuve de contexte

[REQUIS PAR LE MODULE — toute tâche de surface ; une ligne compacte peut suffire en LITE uniquement si le changement est réellement local] Ne dessine pas avant d’avoir cadré public, JTBD, décision dominante, preuves et contraintes. Si un élément manque, formule une hypothèse et son impact.

| Question | Décision attendue |
|---|---|
| **Qui ?** | Utilisateur principal, expertise, contexte, contrainte et état émotionnel. |
| **Pourquoi ?** | JTBD : « Quand [situation], je veux [motivation], afin de [résultat]. » |
| **Quelle décision ?** | Action ou compréhension qui doit être évidente dans cette vue. |
| **Quelle preuve ?** | Données, états, explications ou sources qui rendent l’action crédible. |
| **Quelles contraintes ?** | Plateforme, permissions, contenu, localisation, accessibilité, performance, droits et temps. |

Toute hypothèse importante indique, dans la ligne de run ou la `RUN_CARD` existante :

| Champ | Rôle |
|---|---|
| **Nature et confiance** | `PRODUIT`, `CONTENU`, `DIRECTION`, `TECHNIQUE` ou `CONFORMITÉ`, avec ce qui est connu, inféré ou incertain. |
| **Source et coût d’erreur** | Utilisateur, contenu, observation, recherche ou inférence ; impact si l’hypothèse est fausse. |
| **Owner et prochaine preuve** | Qui peut confirmer ou corriger, et par quel test, retour, donnée, capture ou décision. |
| **User input requis** | `YES`, `NO` ou `NOT-REQUIRED` selon le risque U/A et le contexte ; une non-applicabilité doit être justifiée séparément et ne constitue pas un verdict. |

Ces champs sont une projection lisible du handoff d’ACTION ; ils ne créent ni nouveau schéma ni nouveau statut. Lorsque le run passe à ACTION, ces champs rejoignent le handoff canonique (`ACTION/HANDOFF`) ; en trace complète, ils vont dans la `RUN_CARD` ou la trace équivalente. `Nature et confiance` alimente la qualification de la décision et du risque ; `Source et coût d’erreur` alimente les sources, le scope et la limite ; `User input requis` déclenche une méthode proportionnée lorsque U ou A domine.

Distingue hypothèses de produit, de contenu et de direction : elles n’ont pas le même coût d’erreur. Une microcopie peut être provisoire ; une cible d’utilisateur, une contrainte critique ou un droit d’asset doivent rester visiblement incertains jusqu’à preuve.

Lorsque le risque dominant concerne l’utilisabilité réelle, déclenche dans ACTION une méthode `USER/TASK` avec personne, tâche, contexte, échantillon et résultat observé. Lorsque l’accessibilité ou une population concernée domine, choisis `USER`, `EXPERT` ou le regard d’une personne concernée selon le risque et justifie ce choix. Dans tous les cas, conserve scope, limite, owner et `NEXT-PROOF` ; cette preuve ne remplace ni les contrôles techniques ni l’inspection experte.

L’architecture regroupe l’information par tâche et vocabulaire utilisateur, jamais par organigramme interne. Elle distingue contenu primaire, secondaire, état et action ; elle prévoit cas vides, erreurs, permissions, données longues, succès partiel et localisation.

---

# SAVOIR/CRAFT — anti-slop, composition et expression

Dans V1, le **polish structurel** concerne les proportions, la hiérarchie, la densité, la lisibilité, les états et le comportement.

### Qualité du premier rendu, one-shot et preuve

Lorsque la direction visuelle est ouverte, le premier rendu doit déjà être **composé, spécifique, crédible, désirable et suffisamment résolu** dans le périmètre du mode. Il ne peut pas être seulement un moodboard, une structure vide, un assemblage de primitives ou une surface nominalement conforme lorsque la décision exige une scène réelle.

Distingue trois moments de la qualité : **qualité intrinsèque visée** — ce que l’objet doit déjà posséder avant toute prétention de réussite ; **qualité construite observée** — ce que le rendu réel permet d’inspecter dans son contexte ; **qualité prouvée** — ce qu’ACTION établit sur l’usage, l’accessibilité, la robustesse, la performance ou la conformité. Un rendu peut être visuellement fort mais encore non prouvé en utilisabilité ; un rendu peut être conforme et propre mais rester générique. À chaque moment, la résolution atteinte se lit avec un seul modèle de niveaux : `Correction`, `Précision` et `Intention` (« Jugement visuel situé »).

Le `one-shot` suit la branche one-shot d’`ACTION/PIPELINE-DIRECTION` : une exécution raccourcie de la boucle, jamais sa suppression ; un premier objet faible se corrige ou se retourne.

La boucle de jugement est la boucle d’édition de `DIRECTION/DOUBLE-LOOP`, copiée dans le noyau de la skill.

Le **polish expressif** concerne la matière, la typographie, la couleur, l’image, la silhouette, le rythme et la singularité située. Le polish décoratif ajoute une impression de finition sans conséquence utile ou perceptuelle défendable ; il doit être réduit, même s’il est séduisant.

## CFT-00 — qualité créative et niveau d’ambition

[DURABLE] Lorsqu’une surface, une identité ou une scène engage directement la perception, la qualité attendue ne se limite pas à l’absence de slop ou à la conformité d’une structure. La proposition doit viser, dans la mesure du possible, une **présence**, un **point de vue**, une **spécificité**, une **culture visuelle transformée**, une **composition maîtrisée**, une **expression cohérente**, une **désirabilité située** et une **résolution proportionnée à l’ambition**.

Ces qualités ne constituent ni un score, ni un verdict automatique, ni une promesse universelle. Elles forment une grille de regard qui aide à choisir, comparer, retirer et polir. Une proposition peut être fonctionnelle sans être expressive, soignée sans être spécifique, créative sans être compréhensible ou premium dans son intention sans atteindre encore le niveau de résolution attendu. Décris alors l’écart observable au lieu de le masquer derrière un adjectif.

| Dimension | Question de critique | Signal observable attendu |
|---|---|---|
| **Présence** | Le premier contact possède-t-il une force perceptuelle juste ? | Un foyer, une silhouette ou une relation retient le regard sans effet gratuit. |
| **Point de vue** | Sent-on une position plutôt qu’une application de composants ? | Des choix de composition, de rythme, de type, de matière ou de contenu sont assumés. |
| **Culture visuelle** | Les références ont-elles été comprises et transformées ? | Une relation extraite d’un autre domaine devient un choix propre au produit. |
| **Spécificité** | Qu’est-ce qui appartiendrait moins à un autre produit ? | Contenu, donnée, voix, interaction, structure ou matière portent le contexte réel. |
| **Composition** | Les masses, vides, axes, échelles et tensions sont-ils maîtrisés ? | Le regard circule avec une hiérarchie et un rythme perceptibles. |
| **Désirabilité** | Le rendu donne-t-il envie d’entrer, de comprendre ou de continuer ? | La valeur, la confiance ou la curiosité sont soutenues sans manipulation décorative. |
| **Résolution** | Les détails sont-ils au niveau de l’idée ? | États, responsive, microcopie, transitions, assets et composants tiennent la direction. |
| **Retenue** | Le design sait-il s’arrêter ? | Les effets, variantes et détails faibles ont été retirés lorsqu’ils n’ajoutent rien. |

Une **proposition premium** est une proposition dont la valeur perçue est soutenue par la relation entre clarté, cohérence, précision, singularité maîtrisée, confiance et désirabilité. Elle n’est pas définie par une palette sombre, une grande typographie, un espace vide, une matière riche ou un nom de style. Le premium doit survivre au contenu réel, aux états, au mobile, aux contraintes du produit et au geste principal.

### Creative Quality Review

<!-- noyau:début BOUCLE-REVUE -->
[MÉTHODE] Pour une décision où la qualité visuelle est dominante, conduis une revue courte après la première scène et après la repasse de craft : **ce qui est présent**, **ce qui est spécifique**, **ce qui est culturellement transformé**, **ce qui est encore générique**, **ce qui manque de résolution** et **l’intervention au gain attendu le plus utile**. Utilise l’activation et le vocabulaire perceptuel de `SAVOIR/STATE`, compilés dans le noyau : relie le défaut observé à un geste exécutable, à sa condition d’usage et au résultat à réinspecter. Les gestes proposés sont des points de départ, pas une liste fermée ; un autre geste reste recevable s’il traite le défaut et rend son effet observable. Nomme l’objet, le terme et la modification (par exemple « Surface : tester un liseré de 1 px sur le bord supérieur de la carte, lumière venant du haut ; comparer la séparation sans halo »). Une incohérence de direction appelle une réouverture, pas une accumulation de détails. Si aucun geste ne promet de gain utile, justifie la conservation. La revue produit une prochaine action, sans score esthétique ni substitution aux preuves d’ACTION.
<!-- noyau:fin BOUCLE-REVUE -->

Un rendu n’est pas considéré comme suffisamment travaillé parce qu’il contient davantage de détails. Il l’est lorsque chaque détail important renforce la hiérarchie, le sens, la relation au produit ou la qualité de présence. La beauté pertinente peut venir de l’intensité comme de la retenue ; elle peut être éditoriale, technique, tactile, chaleureuse, colorée, ludique ou silencieuse selon le contexte.

Un **composant authored** est un objet visible conçu pour le produit : sa silhouette, son contenu, sa hiérarchie, sa matière et son comportement forment une unité. Il peut être construit à partir de primitives robustes ; authored ne signifie ni inédit dans le code, ni inhabituel par obligation. Les primitives critiques restent sémantiques, accessibles et fiables.

L’**AI slop** désigne ici une production à faible soin par rapport à son but, souvent favorisée par la vitesse et le faible coût de génération, qui peut être générique, répétitive, trompeuse, incomplète ou coûteuse à vérifier et à maintenir. L’origine IA seule ne suffit pas à établir le slop. Une sortie n’est pas améliorée par une étiquette : elle doit rendre une décision, un artefact, une preuve, une limite ou une prochaine action plus clairs.

Une référence, une ancre, un profil, un choix de style ou une présélection de `DESIGN-ATLAS` calibre une possibilité et peut soutenir un jugement de direction. Aucun ne constitue une preuve indépendante. `DECISION-MODIFIED` et `WHEN-USEFUL` sont des hypothèses de sélection ; seule une observation dans le scope déclaré peut alimenter `DECISION-CHANGE` dans `ACTION`.

## CFT-01 — motivation, construction et forme située

[DURABLE] Une liste de motifs n’est pas un verdict. Évalue un élément par motivation et construction.

| Motivation | Construction | Décision |
|---|---|---|
| Oui | Oui | Légitime, sous réserve des gates d’usage, craft et cohérence. |
| Oui | Non | Justifié, mais à améliorer, simplifier ou expliquer. |
| Non | Oui | Forme construite ; expliciter son intention produit ou retirer. |
| Non | Non | Slop signalé. |

Cette matrice est une heuristique de jugement interne, pas une classification scientifique universelle du slop.

> **Source canonique.** Cette matrice appartient à `SAVOIR/CRAFT/CFT-01`. `ACTION/ANTI-SLOP` en contrôle la conséquence de gate sans la reproduire ; toute évolution de ses cas ou de son vocabulaire se fait ici.

Un principe générateur remplace un interdit sans devenir une recette. La structure peut suivre l’action critique, la profondeur porter une hiérarchie, un accent révéler un statut, une matière contribuer au produit et des panneaux partager une fonction distincte.

Un principe récité sans conséquence visible est du théâtre procédural.

### Dérivation bornée d’une forme située

[MÉTHODE] Les objets, matières et références du système sont des démonstrateurs de relation, jamais un catalogue à reproduire.

<!-- noyau:début COMP-FORME -->
> **Forme située = tâche + donnée ou objet métier + état et conséquence + densité de lecture + phénomène ou métaphore justifiable + preuve attendue.**

Le phénomène ou la métaphore est facultatif. Il peut rendre perceptible un seuil, une trace, une séquence, une origine, un volume ou une relation matérielle. Il n’est jamais ajouté pour éviter un rectangle ou paraître créatif.
<!-- noyau:fin COMP-FORME -->

| Test | Question |
|---|---|
| **Tâche** | Quel geste, choix ou compréhension la forme rend-elle plus directe ? |
| **Donnée** | Quel attribut réel — seuil, comparaison, trace, séquence, provenance ou volume — rend-elle perceptible ? |
| **État** | Comment loading, erreur, indisponibilité, succès et contenu extrême survivent-ils ? |
| **Preuve** | Quelle information, interaction, capture ou test montre qu’elle aide réellement ? |
| **Retrait** | Si matière, métaphore ou profondeur disparaît, qu’est-ce qui devient moins clair ou moins juste ? |

Une appréciation perceptuelle montre une impression ou un jugement situé. Elle ne devient une preuve d’utilisabilité que lorsqu’elle est reliée à une tâche, un contexte, un comportement ou une mesure adaptée.

Ne crée ni quota de variantes ni obligation de nouveauté. Une variation est recevable seulement si une différence de tâche, donnée, contexte, preuve ou registre la rend nécessaire. Toute forme dérivée reste soumise à `FND-01`, `SAVOIR/STATE`, accessibilité et gates ACTION.

## CFT-02 — registres et alternative située

[MÉTHODE] Une direction n’est pas un nom de style. C’est une position relative sur plusieurs axes.

| Axe | Pôles possibles | Question utile |
|---|---|---|
| Structure | Grille stricte ↔ tension sur grille ↔ hors grille | Où la lecture est-elle stabilisée puis décalée ? |
| Matière | Plat ↔ texturé ↔ photographique ↔ illustré/peint/spatial | Quelle matérialité transmet une information ou un registre ? |
| Voix | Neutre ↔ expressif ↔ bruyant | Quelle intensité aide la tâche et le public ? |
| Temporalité | Intemporel ↔ contemporain ↔ nostalgique ↔ prospectif | Quelle relation au temps est justifiée ? |
| Densité | Respiration focalisée ↔ information concentrée | Quelle densité sert la décision ? |
| Texte / image | Texte souverain ↔ preuve souveraine ↔ relation équilibrée | Quel élément porte la crédibilité ? |

Ces axes servent à produire une **alternative située**, jamais un menu de styles ni une obligation de marginalité.

> **Alternative située :** position différente parce qu’elle répond à une contrainte, un public, un JTBD ou une opportunité distincte.

<!-- noyau:début BOUCLE-AXE -->
Pour produire du beau varié sans produire du bruit, faire varier **un axe situé à la fois** : public, JTBD, promesse, geste, structure, densité, matière ou ton. Pour chaque alternative, préciser en trace complète (en trace légère, la première proposition nomme l’alternative écartée) :

- la décision qu’elle peut changer ;
- le public, le contexte, le risque ou le JTBD qui la justifie ;
- le niveau de matérialisation nécessaire ;
- la comparaison ou la preuve prévue ;
- la condition de retrait.
<!-- noyau:fin BOUCLE-AXE -->

Une alternative n’a pas à être matérialisée si elle ne peut modifier aucune décision. Lorsque le choix est ouvert et qu’une position différente peut réellement changer le résultat, développe-la au niveau nécessaire pour comparer : phrase, schéma, cible ou rendu.

Les axes survivent aux tendances ; les étiquettes culturelles et les exemples doivent être révisés dans `SAVOIR/TOOLS`.

## CFT-03 — composition, densité et harmonie

[REQUIS PAR LE MODULE — surface identitaire, hiérarchie complexe ou revue perceptuelle] La composition rend l’action et le contenu lisibles avant la couleur. Choisis grille, échelle, densité et hiérarchie selon le contenu ; une valeur de départ n’est jamais une validation universelle.

Colonnes, tailles, espacements et breakpoints sont des diagnostics de cohérence. Adapte-les lorsque contenu, plateforme ou direction produisent une relation plus juste.

<!-- noyau:début COMP-CONTROLES -->
Les contrôles principaux sont : alignements nets, compensation optique, proximité qui révèle les groupes, priorités lisibles, et responsive pensé comme recomposition. Une grille desktop peut devenir liste ; un panneau peut devenir écran ; un bloc dense peut devenir séquence progressive.
<!-- noyau:fin COMP-CONTROLES -->

Une vue peut avoir une priorité dominante ou un groupe de priorités liées. Ne force pas une dominante unique dans une surface de comparaison ou de supervision lorsque plusieurs décisions doivent rester simultanément visibles.

<!-- noyau:début COMP-TEXTE-IMAGE -->
<!-- concept:TXI-01 -->
**Texte sur image.** Quand un texte est posé sur une photo, une illustration ou une texture, place-le dans la zone calme de l’image ou recadre pour en créer une ; sinon, ajoute un voile ou un dégradé localisé, ou sors le texte de l’image. Mesure le contraste aux points les plus défavorables, à chaque largeur où le recadrage change. Une image sans zone calme demande un autre recadrage ou un autre placement.
<!-- noyau:fin COMP-TEXTE-IMAGE -->

### Cohérence et harmonie

La cohérence vérifie si les éléments suivent les mêmes règles. L’harmonie vérifie si les éléments entretiennent une relation juste. Une interface peut être cohérente et monotone ; elle peut contenir tension, asymétrie ou variation tout en restant harmonieuse si ces écarts sont tenus en relation.

Inspecte sur capture : typographie ↔ espace, image ou matière code-native ↔ hiérarchie, motion ↔ personnalité, densité ↔ usage, détail ↔ ambition. Une direction ambitieuse tenue par un craft faible se lit comme un potentiel non résolu ; une direction calme mais précisément exécutée peut être plus convaincante.

Une matière créée par code — trame, règle, masque, gradient, SVG, découpe ou composition procédurale — doit expliquer la relation qu’elle porte avant d’être préférée à un asset externe.

Une observation de clarté, d’harmonie ou d’unité est perceptuelle. Pour la nommer utilisabilité, ajoute une tâche, un contexte et une preuve d’usage lorsque le risque U est dominant.

## CFT-04 — design émotionnel

[MÉTHODE] Choisis l’émotion seulement lorsqu’elle aide la tâche ou la direction. Elle n’est pas une couche décorative ajoutée après la structure.

Sépare :

- **Viscéral :** impact immédiat ;
- **Comportemental :** ressenti pendant l’usage ;
- **Réflexif :** ce que le produit dit à l’utilisateur après l’interaction.

Les intentions ci-dessous sont des hypothèses de travail, non des effets garantis :

| Intention | Leviers à explorer | Contre-indication à vérifier |
|---|---|---|
| Calme | Rythme régulier, vide utile, contraste lisible, faible surcharge. | Contexte où densité et vitesse de décision priment. |
| Énergie | Accent net, rythme serré, échelle ou mouvement ciblé. | Contexte critique, surcharge sensorielle ou action essentielle masquée. |
| Confiance | Alignements, états, confirmations, données lisibles et prédictibilité. | Décision où le design semble plus certain que la preuve réelle. |
| Luxe | Proportion, matériau maîtrisé, palette restreinte, détail rare et retenu. | Public, prix, accessibilité ou tâche qui exigent un registre plus direct. |
| Sérieux | Hiérarchie stable, copie directe, saturation contrôlée et récupération claire. | Contexte où froideur, distance ou opacité empêchent la compréhension. |

Ces associations sont culturelles et contextuelles. Pour conserver une intention émotionnelle dans une direction, nomme le public, la tâche ou la relation produit visée, la contre-indication et la preuve perceptuelle ou comportementale attendue.

Aucune couleur, typographie, motion ou matière ne produit universellement une émotion. N’infère jamais qu’un effet doit être présent parce qu’une émotion a été nommée.

### CFT-04a — premier contact, preuve et rapport de personne

[À ADAPTER] Le premier contact peut mettre au premier plan soit un **geste ou une promesse**, soit un **objet de preuve concret**. Aucun des deux ne gagne par défaut. Privilégie l’objet lorsque l’utilisateur doit comprendre immédiatement un mécanisme actionnable et que cet objet représente honnêtement le produit sans réduire une relation à une démonstration. Privilégie le geste, la promesse ou un seuil plus indirect lorsque le contexte exige d’abord de la retenue, de la confiance, une présence éditoriale ou une distance juste envers un contenu intime.

La décision porte sur la relation, non sur une géométrie de hero. Trois cards égales, un split hero, un feuillet, une image ou un texte souverain peuvent tous être justes si leur place rend la tâche, la crédibilité et le registre plus cohérents. Une preuve placée au hero ne doit ni imiter un faux dashboard, ni utiliser une personne, une histoire ou une donnée sensible comme argument fonctionnel avant que le contexte l’autorise.

| Question de jugement | Signal en faveur d’un objet de preuve tôt | Signal en faveur d’un geste ou d’une promesse d’abord |
|---|---|---|
| Compréhension | Le mécanisme reste abstrait sans exemple visible ; le premier usage est court ou mobile. | Le mécanisme est déjà lisible ; la première décision est relationnelle ou émotionnelle. |
| Nature de l’objet | L’objet est actionnable, représentatif et peut être montré sans dépersonnaliser son contenu. | L’objet expose une personne, une trace intime ou une situation dont la mise en vitrine change le rapport de confiance. |
| Registre | La clarté immédiate est une forme d’honnêteté. | La lenteur, la pause ou la médiation font partie de la promesse. |
| Responsive | L’objet peut rester lisible et léger à petit écran. | L’objet peut apparaître tôt après le hero ou être recontextualisé sans être imposé au premier regard. |

Formule le compromis : ce qui gagne entre compréhension immédiate et juste distance, le coût assumé, et le signal qui ferait revenir sur la décision. `ACTION` reste propriétaire de la preuve ; une revue perceptuelle peut confirmer un effet situé, mais ne prouve ni tâche utilisateur ni vérité émotionnelle universelle.

## CFT-05 — couleur et contraste

<!-- noyau:début COMP-COULEUR -->
[REQUIS PAR LE MODULE — couleur, thème, statut ou surface identitaire] Conçois une palette par rôles : surfaces, textes, actions, états et frontières. La répartition entre neutres et couleurs est une décision de direction, pas un défaut : une structure neutre à accent, une identité multicolore structurelle ou un codage par zones sont recevables si les rôles, les états, le contraste calculé et un indice non chromatique pour toute information critique tiennent. Une couleur sémantique n’est pas une décoration.
<!-- noyau:fin COMP-COULEUR -->

<!-- noyau:début COMP-CONVERGENCE -->
**Question de convergence.** Cette palette et cette police de titre sont-elles celles que le modèle produirait sans brief (palette : neutres et un seul accent, sombre et doré, dégradé froid ; police : la grotesque large ou la serif de caractère prise par réflexe) ? Si oui, nomme ce qui, dans le produit, les justifie ; si rien ne les justifie, reconsidère-les. Pour la police de titre, compare au moins deux voix typographiques distinctes (par exemple grotesque, serif, mécane, manuscrite ou vernaculaire du lieu) sur le vrai titre avant de choisir. La question ne prescrit aucun écart : un choix convergent justifié reste valide.
<!-- noyau:fin COMP-CONVERGENCE -->

La palette est conditionnelle : elle est documentée lorsqu’elle peut changer la décision, le thème, le statut ou la direction. Si le système existant est conservé et qu’aucun choix de couleur ne change le run, note cette conservation et sa raison.

OKLCH peut servir d’espace de conception perceptuel. HEX, HSL ou autre format restent des sorties techniques selon le projet. Le dark mode est recomposé — luminosité, saturation et élévation adaptées — et non inversé naïvement.

Le gamut élargi peut enrichir l’expression, mais ne porte jamais une information indispensable. Le contraste est calculé selon la politique d’ACTION ; aucune relation texte/fond ou état/fond ne reçoit un `PASS` à l’œil.

Une relation de couleur peut exprimer un registre ou une hiérarchie, mais ne doit pas porter seule une information critique. Les impressions de statut, chaleur, sérieux ou premium restent des hypothèses de perception à vérifier dans leur contexte.

Les claims sur chroma, statut perçu ou tendances de palette passent par `SAVOIR/TOOLS` et portent source, date, portée et limite dans la trace locale du run.

---

# SAVOIR/TYPE — typographie et données

<!-- noyau:début COMP-TYPO -->
[REQUIS PAR LE MODULE — lecture, ton, données, hiérarchie ou surface identitaire] Choisis une typographie pour ses langues, chiffres, ponctuation, graisses, lisibilité, licence, performance, fallback et ton.
<!-- noyau:fin COMP-TYPO -->

Une famille fréquente n’est pas un problème en soi. Le problème est le réflexe sans alternative comparée, système existant interrogé ou raison formulée.

Une ou deux voix expressives peuvent souvent suffire, mais cette heuristique reste `[À ADAPTER]`. Une famille mono-fonctionnelle pour données, version ou métadonnées ne constitue pas nécessairement une voix supplémentaire.

Hiérarchie, longueur de ligne, interligne, figures tabulaires, fallback et chargement font partie de la décision.

Une police variable peut devenir un système adaptatif : poids pour hiérarchie, largeur pour densité justifiée, taille optique pour rendu à l’échelle et grade lorsqu’il existe. N’utilise que les axes présents dans la famille livrée. Préfère les propriétés typographiques de haut niveau et évite les styles synthétiques non déclarés.

Une signature typographique ne tient pas si zoom, reflow, locale ou ajustement d’espacement la transforment en défaut de lecture.

<!-- noyau:début COMP-TITRE -->
<!-- concept:TIT-01 -->
**Équilibre d’un titre.** Quand un titre porte la scène (grand titre, accroche, chiffre mis en avant), règle-le sur le vrai texte, puis corrige ce que la capture montre : une coupe de ligne qui casse le sens ; un mot isolé en dernière ligne qui n’est pas voulu ; des lignes si inégales que le bloc se lit mal (`text-wrap: balance` peut aider si la cible le permet) ; une approche trop lâche aux grandes tailles, si la police le demande ; une hiérarchie aplatie, que l’on rétablit par l’écart d’échelle entre le titre et le texte qui suit, ou par le poids, la position ou l’espace. Un mot isolé, un déséquilibre ou un faible écart peut être le choix de composition : on le garde si la capture montre qu’il fonctionne. Observe sur capture, en desktop et en mobile, avec le contenu réel : la forme du bloc de titre reste lisible au flou.
<!-- noyau:fin COMP-TITRE -->

### Preuve typographique

La preuve est documentée dans `ACTION/STRUCTURED-PROOF` lorsque la typographie peut changer la décision. Sépare, lorsque nécessaire :

```text
FORM-LEGIBILITY — reconnaissance des formes et caractères.
TEXT-READABILITY — lecture du texte dans son contexte.
HIERARCHY — distinction des rôles et priorités.
PERSONALITY — tonalité ou individuation perçue.
TASK-EFFECT — effet sur compréhension ou action lorsque pertinent.
LIMIT
```

| Preuve | Cas |
|---|---|
| Spécimen de rôle | Display, corps, interface, données et légale sur contenu réel. |
| Résilience | Texte long, locale, chiffres, zoom, ajustement d’espacement, reflow, petit corps, fallback et caractère absent. |
| Rendu | Couple taille/interligne/mesure et axe variable si pertinent. |
| Décision | Voix, lisibilité ou densité réellement améliorées ; contre-indication déclarée. |

Une famille n’est jamais déclarée supérieure sur la seule base d’une impression de marque. Lorsque U est dominant, l’effet sur la tâche est prouvé par ACTION, pas inféré de la typographie seule.

---

# SAVOIR/STATE — craft, composants et états

[REQUIS PAR LE MODULE — composant, état, surface `DIRECTION` ou Gate C] Le craft n’est pas une couche de polish. Il concerne états, alignements, contenus réels, microcopie, données extrêmes, récupération et détails qui empêchent l’interface de paraître héritée d’un défaut de stack.

### Jugement visuel situé

Le jugement visuel porte sur le rendu réellement construit, dans son contexte et son périmètre. Il distingue les qualités suivantes sans les transformer en score, en verdict ou en statut :

| Dimension | Question de jugement |
|---|---|
| **Direction artistique** | Quelle position visuelle située relie produit, public, contenu, médium et contexte ? |
| **Craft** | La hiérarchie, la composition, la typographie, la matière, les états et le comportement sont-ils construits avec précision ? |
| **Polish** | Le rendu est-il résolu dans ses détails, ses transitions, ses erreurs, son responsive et sa cohérence réelle, plutôt que décoré par des effets ? |
| **Créativité située** | L’écart, la relation ou la reformulation apporte-t-il une réponse spécifique et utile, plutôt qu’une nouveauté forcée ? |
| **Goût situé** | Les choix sont-ils sélectionnés, proportionnés et retenus pour ce contexte, avec une préférence assumée comme située ? |
| **Spécificité** | Que resterait-il de pertinent si le logo, la référence ou le template disparaissait ? |

La direction artistique donne le point de vue ; le craft le construit ; le polish le résout ; la créativité ouvre une possibilité pertinente ; le goût sélectionne et retient. Ces termes sont des lentilles de jugement, pas des valeurs de `DIRECTION-STATUS`, de `VERDICT` ou du schéma machine.

Une revue visuelle peut examiner hiérarchie, composition, typographie, matière, premier objet, spécificité, cohérence, retenue et résolution lorsque ces dimensions peuvent modifier la décision. Elle ne les recopie pas toutes par réflexe : une observation nomme l’élément visible, sa conséquence sur la direction ou la décision, son scope et sa limite éventuelle. Une capture, une rationale ou une image générée ne prouve ni le build complet, ni l’usage, ni l’accessibilité, ni la robustesse.

Trois niveaux se complètent :

1. **Correction :** comportement et accessibilité de base fonctionnent.
2. **Précision :** mesures, alignements, transitions, états et relations sont ajustés.
3. **Intention :** une décision située répond à une difficulté réelle et produit une différence visible ou d’usage.

En lecture visuelle, ces niveaux décrivent la résolution effectivement atteinte : `Correction` permet de juger la base ; `Précision` permet de juger la construction et le polish pertinent ; `Intention` permet de juger une différence située. Ils ne forment pas une note de beauté. Un rendu peut être précis mais générique, avoir une intention forte mais une finition insuffisante, ou être poli dans une vue tout en restant non vérifié dans ses états secondaires.

La question de niveau 3 est :

> Quel choix résulte ici d’un jugement délibéré, serait absent d’une version par défaut, et quelle contrainte sert-il ?

Le temps investi est un indice, jamais une preuve. Une simplification juste, un ordre de lecture, une microcopie ou un token peuvent être rapides à implémenter et néanmoins intentionnels.

### Vocabulaire perceptuel

Si le défaut vient de l’organisation de la scène, reprends la traduction de `BIBLIOTHEQUE/SELECT` avant un geste de finition. Si la relation est retenue mais ses paramètres restent ouverts, utilise la calibration de `BIBLIOTHEQUE/CONTRACTS` ; le jugement demeure chez SAVOIR et les preuves chez ACTION.

<!-- noyau:début COMP-VOCABULAIRE -->
<!-- concept:FIN-01 -->
**Activation du craft.** Le système doit aider à produire la finesse, au-delà de la cohérence : **signal visible → savoir pertinent → geste concret et condition → modification de l’artefact → réinspection → conserver, ajuster ou retirer**. Avant le premier build, anticipe la relation fragile à partir du contenu réel et prépare son geste ; après le rendu, confirme ou corrige ce diagnostic. Pour le défaut dominant, utilise une ligne pertinente de la table ; ne déroule pas toutes les lignes. Si le geste reste vague, approfondis la source indiquée selon `DIRECTION/CHARGE` ; ne renvoie pas la résolution au seul « savoir-faire de l’agent » ou à une future revue humaine. Un pixel peut suffire si la relation est déjà juste ; un pixel ne répare pas une direction faible.

| Terme | Signal à traiter | Geste concret et condition | Réinspection et savoir à approfondir |
|---|---|---|---|
| Cohérence de rayon | Un cadre et son contenu emboîté paraissent non concentriques. | Pour deux rectangles arrondis à inset uniforme, tester `rayon intérieur = max(0, rayon extérieur − inset)` ; intégrer l’épaisseur de bord à l’inset mesuré. Pour une autre géométrie, ajuster ses courbes propres, sans imposer cette formule. | Inspecter les coins à taille réelle et au viewport étroit ; éviter une rupture de courbe ou un contenu coupé. `SAVOIR/SYSTEM`. |
| Masse visuelle | Un élément secondaire concurrence la priorité de lecture ou d’action. | Réduire son échelle, sa densité ou son contraste, ou renforcer le foyer par sa position ; choisir le levier qui sert la tâche ou le parti. L’objet de preuve peut être discret ; il n’est pas nécessairement le plus grand. | Relire l’ensemble à faible détail, puis le geste principal à taille réelle ; conserver le rythme expressif utile. `SAVOIR/CRAFT/CFT-03`. |
| Gestion du vide | Un groupe paraît disloqué, ou deux contenus indépendants paraissent liés. | Rapprocher ce qui appartient à la même unité, ou augmenter la distance entre unités. Préserver les vides qui portent respiration, tension, information ou émotion ; resserrer seulement le vide qui affaiblit la relation voulue. | Comparer le groupement et le rythme dans la page entière, avec contenu long et mobile. `SAVOIR/CRAFT/CFT-03`. |
| Silhouette | À faible détail, aucun foyer ou ordre de lecture n’émerge. | Déplacer ou redimensionner une masse, modifier un recadrage ou un contraste pour rendre la priorité perceptible ; si la trame reste interchangeable, rouvrir la structure plutôt qu’ajouter un effet. | Comparer les silhouettes au même format puis la lecture normale ; ne pas exiger du spectaculaire dans une vue de gestion. `SAVOIR/CRAFT/CFT-03` ; structure par `BIBLIOTHEQUE/SELECT`. |
| Surface | Un bloc semble collé, ses bords se perdent, ou ombre et lumière se contredisent. | Si une matière éclairée par le haut est voulue, tester un liseré clair de **1 px CSS** sur son bord supérieur et atténuer l’ombre opposée. Ajuster l’opacité au fond réel. Pour une surface plane, tester plutôt une frontière ou un écart de valeur ; pour plusieurs matières, régler leur relation sans les uniformiser. | Inspecter à taille réelle : séparation accrue sans halo, bord trop dur ni lumière contradictoire ; retirer le liseré s’il ne sert pas la matière. Une hauteur visuelle ne code pas automatiquement l’importance. `SAVOIR/STYLE` ; `SAVOIR/STATE`. |
| Chiffres | Une valeur changeante saute en largeur, ou une colonne devient difficile à comparer. | Si les chiffres sont alignés ou dynamiques, activer des figures tabulaires (`font-variant-numeric: tabular-nums` en CSS), aligner les nombres sur un axe et garder leur unité liée. Ne pas atténuer un zéro, une décimale ou un identifiant nécessaires à l’interprétation. | Tester changement de valeur, signe, unité, locale et police de repli ; contrôler la stabilité sans effacer de précision utile. `SAVOIR/TYPE`. |
| Accent | Plusieurs couleurs réclament la même action, ou une couleur critique devient ambiguë. | Réaffecter les couleurs par rôles, distinguer action et statut, puis retirer ou réduire seulement les usages parasites. Une palette multicolore, culturelle ou expressive est recevable ; ne pas la réduire à un accent unique par réflexe. | Inspecter l’action, les états, le contraste mesuré et les indices non chromatiques critiques ; préserver le parti coloré. `SAVOIR/CRAFT/CFT-05`. |
| Détail révélateur | L’idée est forte mais une jonction, une graduation ou un état paraît laissé par défaut. | Résoudre d’abord ce détail : aligner une graduation à sa mesure, soigner le passage entre deux zones ou la relation d’un repère à l’objet. En conserver plusieurs si chacun a un rôle ; retirer ceux qui n’apportent qu’une impression de finition. | Vérifier la relation à l’idée, à la donnée ou à l’usage, puis l’ensemble sans surcharge. Une graduation doit rester exacte. `SAVOIR/STATE` ; `SAVOIR/CRAFT/CFT-01`. |
| Texte secondaire | L’appoint disparaît ou concurrence le contenu principal. | Corriger d’abord le contraste texte/fond selon `ACTION/GATE-A`, puis régler graisse, position ou espacement pour établir la hiérarchie. Réduire la taille seulement si la lecture reste confortable dans le contexte ; ne pas résoudre la concurrence par l’illisibilité. | Mesurer le contraste, inspecter à taille réelle, au zoom et sur mobile ; garder lisibles aide, unité et erreur. `SAVOIR/TYPE` ; `SAVOIR/CONTEXT`. |
| États | Un changement d’état semble improvisé, déplace la scène ou empêche de reprendre. | Réserver la place utile pendant le chargement, conserver la saisie en erreur et placer une reprise explicite près du problème. Dessiner les états nécessaires au composant ; ne pas fabriquer tous les états possibles. | Parcourir l’état et sa sortie avec contenu réel ; une capture seule ne prouve pas la reprise ni le focus. `SAVOIR/STATE` ; preuve par `ACTION/GATE-A`. |
| Alignement optique | Une icône, un titre ou une courbe semble décentré malgré ses boîtes alignées. | Comparer les contours visibles et la ligne de base ; tester un décalage local de **1 px CSS** ou un ajustement d’approche si le déséquilibre persiste. Conserver la grille et la zone interactive ; ne pas déplacer tous les éléments ni rasteriser le texte par réflexe. | Comparer avant/après à taille réelle, avec la police chargée et son repli ; retirer le décalage s’il corrige une vue mais casse les autres. `SAVOIR/TYPE` ; `SAVOIR/STATE`. |
| Image intégrée | Le sujet est coupé, un détourage porte un halo, ou le texte lutte avec l’image. | Ajuster le point focal et le recadrage selon le viewport ; traiter le bord sur son fond réel si un détourage est requis. Pour le texte superposé, choisir une zone calme ou un voile local plutôt qu’assombrir toute l’image par défaut. | Inspecter bord, sujet, texte et raccord sur desktop et mobile ; mesurer le contraste au fond défavorable. Si l’asset est inadéquat, remplacer ou produire par la route autorisée. `SAVOIR/SOURCE` ; `SAVOIR/CRAFT/CFT-03`. |
| Mouvement | Une transition est saccadée, gratuite ou déstabilise le repère de lecture. | Relier le mouvement à un changement d’état ; régler trajectoire, durée ou atténuation sur ce changement précis. Si le mouvement n’apporte rien, supprimer l’animation ; prévoir une alternative réduite selon le contexte. | Jouer l’interaction, vérifier interruption, fin d’état et mouvement réduit ; une image fixe n’atteste pas la fluidité. `SAVOIR/CONTEXT`. |

**Choix et contrôle.** Chaque ligne relie un symptôme, une intervention possible et une observation ; elle n’impose pas une esthétique. Choisis le geste dont le gain attendu traite le défaut avec le moins de dommages aux relations déjà réussies. Modifie l’artefact, compare avant/après dans le même scope et à taille réelle, puis réinspecte l’ensemble et les états concernés. Conserve, ajuste ou retire selon l’effet observé ; sans capacité de rendu ou d’interaction, déclare la limite correspondante. Si un autre savoir du corpus devient nécessaire, nomme la décision qu’il peut changer avant de le charger. La trace existante suffit ; aucun score, nouveau gate ou dossier par geste.
<!-- noyau:fin COMP-VOCABULAIRE -->

La silhouette n’exige pas une identité spectaculaire. Dans une vue administrative ou transactionnelle, elle vérifie surtout la lecture prioritaire au flou.

### États pertinents

Un composant ne possède pas tous les états imaginables, mais aucun état nécessaire ne peut être implicite : focus clavier, empty de liste, erreur de formulaire, overflow, chargement, permission refusée, image absente, valeur extrême et contenu long lorsque pertinents.

HTML sémantique, nom accessible, focus visible, erreur associée et récupération compréhensible sont des conditions de craft autant que de conformité. `ACTION/GATE-A` vérifie leur présence ; `ACTION/GATE-C` peut ensuite juger leur résolution perceptuelle ; une tâche utilisateur peut être requise lorsque la récupération ou la compréhension est le risque dominant.

<!-- concept:RCV-01 -->
**Récupération après erreur.** Un message d’erreur dit ce qui s’est passé, pourquoi si c’est utile, et comment reprendre ; il apparaît près de l’élément concerné, dans la langue du produit. La saisie de la personne est conservée et une action de reprise est proposée : corriger, réessayer ou revenir. Le focus dépend du moment : après une soumission bloquée, il peut aller à l’erreur ou au résumé des erreurs ; pendant la saisie, l’erreur est annoncée de façon accessible (région live) sans déplacer le focus. Une capture montre le message ; seule une interaction montre la reprise : parcours l’erreur, puis la correction, jusqu’au succès, ou jusqu’à une issue claire lorsque la réussite est impossible (alternative ou sortie expliquée).

---

# SAVOIR/SOURCE — ancre et sourcing visuel

[REQUIS PAR LE MODULE — surface `DIRECTION`] Regarder n’est pas lire une légende. Une description textuelle peut expliquer un principe ; elle ne transmet pas seule masse, lumière, trame, densité ou rapport image/texte.

Utilise les voies `ANCHOR-GENERATED` / `ANCHOR-OBSERVED` / `ANCHOR-PROVIDED` définies par `DIRECTION/VISUAL_TARGET` et exécutées dans `ACTION/PIPELINE-DIRECTION` seulement si une ancre peut modifier la décision et si sa limite sera déclarée. Pour une surface identitaire, l’ancre suit l’absolu 2 de `DIRECTION` : exploration possible sans ancre, limite déclarée ; acceptation avec une ancre, observée ou fournie pour un produit réel ; si elle manque, les axes concernés restent `NOT-VERIFIED` et le run suit l’issue ACTION appropriée (`ACTION/PIPELINE-DIRECTION`). Hors surface identitaire, justifie la non-applicabilité. Termine par une spec visuelle exploitable. Une image générée peut matérialiser une direction ; une référence observée peut calibrer une résolution ; une ancre fournie peut exprimer une intention ou un actif réel.

`ANCHOR-GENERATED` est une **hypothèse visuelle générée**, utile pour explorer une direction et comparer une possibilité, mais elle ne fait pas autorité par défaut dans `SAVOIR/SOURCE`. Elle ne constitue ni une calibration externe suffisante, ni une preuve de qualité ou d’usage, et ne calibre pas seule un principe durable, un niveau de craft ou une résolution de détail. Lorsque l’enjeu identitaire est élevé, accompagne-la d’une référence observée, d’une contrainte réelle ou d’une réserve explicite sur l’absence de calibration externe ; une revue indépendante est un contrepoint (`ACTION/GATE-B`, B3), pas une calibration. Cette limite concerne l’autorité de la source, pas la valeur exploratoire de l’hypothèse.

### Test d’utilité de l’ancre

Une ancre est utile si elle fournit :

1. une décision structurelle ou perceptuelle qu’elle change réellement ;
2. une contre-indication identifiable ;
3. des attributs retenus, rejetés et non transférables.

Une image jolie mais sans conséquence de décision est décorative et ne suffit pas. Une ancre ne prouve ni qualité finale, ni utilisabilité, ni droit de réemploi.

Les galeries de composants, templates et bibliothèques sont utiles pour observer conventions, états et accessibilité. Elles ne suffisent pas à fournir matière, direction ou singularité. Cherche hors écran lorsqu’une affiche, une signalétique, un packaging, une photo, une édition ou une architecture apporte une contrainte de composition utile.

Les pièges sont : prompts qui convergent, image créée puis ignorée, image générée utilisée comme asset final sans décision de droits, rôle et fidélité, résultat de recherche choisi seulement parce qu’il est thématique, ou asset isolément séduisant qui détruit la lecture une fois intégré.

### Recherche orientée décision — chercher loin seulement quand cela change le résultat

Lorsque le `DOMAIN-FRAME`, le risque ou l’ambition déclenche une recherche, ne collecte pas des liens pour décorer la trace. Recherche ce qui peut modifier une décision : conventions du domaine, modèles mentaux, terminologie, contraintes réglementaires ou d’accessibilité, références culturelles, comportements concurrents, systèmes existants, matériaux, images, données ou mécanismes de preuve.

Chaque source retenue porte une fiche minimale :

```text
SOURCE: origine, date et portée
ROLE: direction, production ou vérification
STATUS: vérifié dans ce run, connaissance non revérifiée ou source utilisateur non revérifiée
WHAT-WAS-OBSERVED: observation réellement faite
WHAT-WAS-RETAINED: relation retenue
WHAT-WAS-REJECTED: motif, surface ou hypothèse écarté
HOW-TRANSFORMED: traduction propre au produit et au contexte
DECISION-CHANGED: décision que la source a modifiée, confirmée ou abandonnée
LIMIT: ce que la source ne permet pas d’affirmer
TRACE-LOCATOR: où réinspecter la source, l’observation et l’artefact
OWNER / NEXT-PROOF: responsable et prochaine vérification
RIGHTS / UNCERTAINTY: droits, autorisation ou inconnue lorsque l’asset ou le claim le requiert
```

**Projection machine, facultative.** Quand une recherche doit être contrôlée par machine, `RESEARCH_BRIEF` (`schemas/research_brief.schema.json`, validé par `scripts/validate_contracts.py`) la porte : question, décision à risque, profondeur, classes de sources, incertitude avant et après, condition d’arrêt, puis une entrée par source qui reprend cette fiche. `ROLE` et `OWNER / NEXT-PROOF` n’y ont pas de champ et restent dans la trace. Ce schéma n’est jamais exigé pour faire une recherche.

Une recherche de domaine et une recherche de calibration visuelle peuvent se compléter, mais elles ne se substituent pas l’une à l’autre. Une source de tendance ne prouve pas l’usage ; une référence visuelle ne prouve pas les droits ; une convention concurrente ne devient pas une vérité produit ; un résultat généré ne devient pas une observation externe. Lorsque la recherche ne peut modifier aucune décision, déclare `N/A-JUSTIFIED` et n’approfondis pas par réflexe ; une recherche faite qui confirme la décision est une confirmation (`ACTION/STATUS`), pas un `N/A-JUSTIFIED`.

La profondeur de recherche augmente par déclencheur : confiance ou erreur coûteuse, public ou JTBD incertain, contexte culturel sensible, convention inconnue, matériau ou asset directeur à calibrer, ou écart créatif qui ne peut être défendu par le seul jugement interne. La recherche doit ensuite revenir dans le premier objet, la structure, le contenu, le geste ou la preuve ; sinon elle reste une archive et non un levier de production.

### Curer, produire et intégrer

Le point de départ n’est pas « quelle image produire ? », mais « quelle relation manque à la promesse, à la preuve ou à l’action ? ».

<!-- noyau:début MOY-CALIBRATION -->
Cherche des calibrations dans les domaines qui peuvent changer cette relation — cinéma pour lumière et séquence, édition pour rythme et crop, affichage pour échelle et distance, architecture pour masse, photographie pour focalisation, packaging pour matière, signalétique pour orientation, arts vivants pour mouvement — sans transformer une référence culturelle en décor interchangeable.
<!-- noyau:fin MOY-CALIBRATION -->

Choisis ensuite une route de production déclarée dans `DIRECTION/VISUAL_TARGET`. Une génération réussie ne se mesure pas à son réalisme intrinsèque : elle doit répondre au cadrage, au plan de lecture, au rôle du type, au contraste, au mouvement éventuel, au crop mobile et au niveau de preuve requis.

Avant de retenir un asset directeur, formule une contre-épreuve proportionnée : quel rendu code-native, asset retiré, crop alternatif ou autre médium ferait mieux apparaître la même relation ? Persiste dans la trace la contre-épreuve, la décision qu’elle pourrait modifier, son résultat et l’alternative refusée. Ne produis cette contre-épreuve que si elle peut réellement modifier la décision ; sinon, conserve la justification de non-applicabilité prévue par ACTION et avance.

---

# SAVOIR/DESIGN-ATLAS — familles et responsabilités

`DESIGN-ATLAS` est la section atlas de `SAVOIR.md` : un index de jugement, pas un catalogue de recettes. Commence par la décision et le risque ; si aucune famille ne peut modifier la prochaine décision, ne charge pas l’atlas. Il aide à nommer la famille d’un choix avant de charger la route spécialisée. Il ne choisit ni le mode, ni le JTBD, ni une esthétique par défaut. Il ne peut jamais réduire un mode, un niveau de preuve ou une protection déjà imposée par `DIRECTION/START` ou par un risque critique ; s’il révèle un risque supérieur, retourne à `DIRECTION/START` pour mettre à jour `MODE`, `RISK` et `SCOPE`, puis laisse ACTION recalculer owner, preuve, gates et prochaine action avant toute reprise.

| Famille | Responsabilité | Route approfondie | Question de sélection |
|---|---|---|---|
| **Médium** | Traduire la décision dans l’environnement réel. | `SAVOIR/CONTEXT`, `SAVOIR/TECH` | Quels appareils, supports, inputs, budgets et idiomes peuvent changer le résultat ? |
| **Style / registre** | Donner une manière située d’exprimer une décision. | `SAVOIR/STYLE`, `SAVOIR/CRAFT` | Quelle relation de type, matière, densité ou rythme doit être différente ici ? |
| **Technique** | Modifier une relation visuelle, informationnelle ou de production. | `SAVOIR/CRAFT`, `SAVOIR/TYPE`, `SAVOIR/TECH` | Quelle décision la technique rend-elle plus claire, plus crédible ou plus robuste ? |
| **Effet** | Produire une conséquence perceptive, comportementale, narrative, spatiale, identitaire ou informative. | `SAVOIR/CRAFT`, `SAVOIR/CONTEXT` | Que comprendra, fera, ressentira ou localisera la personne grâce à cet effet ? |
| **Asset / média** | Rendre tangible une preuve, une identité, un contenu, un contexte ou une atmosphère. | `DIRECTION/VISUAL_TARGET` pour le rôle et la route de production ; `SAVOIR/SOURCE` pour provenance, droits et transformation ; `ACTION` pour intégration, fallback, preuve et clôture. | Quel rôle porte l’asset, et que se passe-t-il s’il est absent, recadré ou remplacé ? |
| **Structure / composant** | Organiser l’espace, la lecture, l’état, la donnée ou l’action. | `BIBLIOTHEQUE/SELECT` si la structure est ouverte ; `BIBLIOTHEQUE/COMPONENTS` et `ACTION/RUN-SYSTEM` si le composant ou le blast radius est partagé, avec `SAVOIR/SYSTEM` pour le jugement du système partagé ; `ACTION` pour preuve et clôture. | Quelle unité rend la décision et les états plus directs ? |

### Cartographie non exhaustive

Les familles ci-dessous orientent la recherche ; elles ne sont ni des quotas, ni des tags obligatoires, ni des styles prêts à appliquer.

| Relation à améliorer | Techniques possibles | Effets possibles |
|---|---|---|
| Hiérarchie et orientation | Échelle, contraste, espace négatif, groupement, grille, alignement, rythme | Perceptif, informationnel, comportemental |
| Matière et contexte | Photographie, illustration, texture, trame, couleur, lumière, matériau code-native | Identitaire, atmosphérique, spatial |
| Preuve et compréhension | Donnée, diagramme, comparaison, vue produit, annotation, séquence, avant/après | Informationnel, comportemental, narratif |
| Rythme et feedback | Transition, motion d’état, progressive disclosure, scroll, réaction, son | Comportemental, narratif, perceptif |
| Profondeur et espace | Couches, masque, blur, ombre, perspective, 3D, parallax | Spatial, perceptif, identitaire |
| Voix et reconnaissance | Typographie, microcopie, couleur sémantique, marque, motif, langage | Identitaire, informationnel, narratif |

Un effet est retenu seulement s’il modifie une relation observable. Une ombre, un blur, un gradient, une texture, une animation ou une transition peuvent être légitimes, mais leur présence seule ne prouve rien. `DÉCORATIF-SANS-CONSEQUENCE` est une catégorie de retrait, jamais une technique à promouvoir.

<!-- noyau:début MOY-ASSETS -->
**Traitement des assets moyens.** Quand les assets disponibles sont moyens (photos de téléphone, banque d’images), choisis le traitement que justifie la thèse — recadrage, étalonnage, duotone, grain ou trame — plutôt que de les poser bruts ou de les remplacer par un dessin. Un traitement commun peut unifier une série disparate ; plusieurs traitements se justifient si leurs rôles sont distincts et lisibles. Vérifie sur capture la relation entre les images et la composition. Le traitement ne masque ni un droit inconnu, ni une image hors sujet.
<!-- noyau:fin MOY-ASSETS -->

### Rôles d’asset

Un asset peut servir de **preuve produit**, **contenu**, **identité**, **orientation**, **contexte**, **atmosphère**, **matière**, **signal d’état**, **donnée**, **média temporel** ou **modèle spatial**. Son rôle doit être observable dans la scène. `DIRECTION/VISUAL_TARGET` possède le rôle et la route de production ; `SAVOIR/SOURCE` possède la provenance, la transformation et la contre-indication ; `ACTION` observe l’intégration, le fallback, le scope, les droits selon le contrat du run, le statut et la clôture.

### Portée par médium

Les médiums usuels sont le **Web**, le **mobile natif**, le **desktop natif**, le **print et l’édition**, la **signalétique**, l’**espace et l’exposition**, la **vidéo et le motion**, le **jeu**, la **3D/spatial**, le **service** et l’**embarqué**. Cette liste est un index, pas une promesse d’exhaustivité. `SAVOIR/CONTEXT` définit les contraintes et les questions de robustesse ; ACTION conserve pour le scope retenu le rendu observable, les idiomes d’interaction, le référentiel applicable, l’unité de budget, la méthode, le résultat et la limite de preuve. Ces éléments sont des slots regroupables ; ils ne constituent pas cinq livrables obligatoires.

### Test de sélection et de non-recyclage

Après classification, décision et risque, et avant de charger une famille, évalue dans la trace existante : `DECISION-MODIFIED` — décision que la famille pourrait modifier ; `WHEN-USEFUL` — condition située où elle peut aider ; `COUNTERINDICATION` — cas où elle nuirait ; `MEDIUM-SCOPE` — médium et surface concernés ; `PROOF-LIMIT` — ce qui restera non prouvé. Si `DECISION-MODIFIED` ne peut pas être renseigné honnêtement, ne charge pas la famille. Ces champs préparent la sélection ; ils ne remplacent pas la trace canonique d’ACTION. Après observation, inscris `DECISION-CHANGE` si une décision a effectivement changé, été confirmée ou abandonnée ; sinon utilise `N/A-JUSTIFIED` ou `NOT-OBSERVED` selon le contrat d’ACTION. `WHY-NOW` et `REUSE-CHALLENGE` sont requis surtout lorsqu’une famille ou un profil provient d’un run précédent. Si la famille ne peut modifier aucune décision, ne la charge pas. L’absence de style, de technique, d’effet, d’asset ou de composant est une sortie valide.

**Frontière maintenance/design.** Une correction de microcopie, traduction, overflow, wrapping, contraste, focus, nom accessible ou état dans un composant existant reste une maintenance locale ; elle ne devient pas automatiquement une décision de style, de technique, d’effet, d’asset ou de structure. Si aucune famille n’est applicable, ne renseigne pas de famille et conserve la décision dans la trace ACTION ; n’utilise `N/A-JUSTIFIED` que si sa condition canonique est satisfaite. Ne transforme pas la phrase « rendre le libellé lisible » en profil typographique, ni « vérifier le contraste » en effet visuel.

---

# SAVOIR/STYLE — profils contrôlés et dials

Un profil de style règle une manière d’exprimer une décision : rapport au type, matière, densité, contraste et mouvement. Il ne choisit ni JTBD, ni support, ni grille, ni scène.

Le parcours est : `DIRECTION/START → SAVOIR/FRAME si le cadrage est à éclaircir → SAVOIR/STYLE si nécessaire → ACTION/RUN-*`. Ajoute `BIBLIOTHEQUE/SELECT` uniquement lorsque la structure d’écran ou la combinaison de routes est ouverte ; si la structure existante suffit, justifie le non-chargement dans la trace.

### Règle de sélection

Un profil est retenu seulement s’il modifie une décision que le run doit réellement prendre et soutient le public, la tâche, le positionnement ou le contexte. Aucun profil n’est choisi par défaut.

La `RUN_CARD` ou la trace locale note, sans créer de nouveau schéma :

```text
PROFILE-DECISION — décision réellement modifiée.
DIALS — dials relevés, abaissés ou inchangés.
COUNTERINDICATION — situation où le profil devient nuisible.
EVIDENCE — capture, observation ou preuve montrant son effet.
```

`PROFILE-DECISION` se lit en deux temps : le profil retenu, qui est une intention (vers `DECISION-INTENT`), puis l’effet constaté après capture (vers `DECISION-CHANGE`). Ces libellés se mappent aux champs canoniques d’ACTION : `PROFILE-DECISION` vers `DECISION-INTENT` puis `DECISION-CHANGE`, `DIALS` vers la décision perceptuelle et son scope, `COUNTERINDICATION` vers `RISK` et `LIMIT`, et `EVIDENCE` vers `PROOF/TRACE-LOCATOR` avec méthode, résultat, owner et `NEXT-PROOF`. Ils ne sont ni des états de run, ni des issues, ni des verdicts.

Un profil est refusé lorsqu’il sert de raccourci pour un genre, un ensemble de composants, une esthétique « premium » ou une collection de motifs. Les profils ci-dessous sont des profils internes d’expression ; ils ne sont ni des catégories scientifiques, ni des packs de composants, ni des styles prêts à appliquer.

Le catalogue est **borné et non exhaustif** : l’absence d’un profil ne justifie ni d’en choisir un par confort, ni d’en inventer un nouveau pour chaque brief. Un profil peut être réutilisé seulement si la décision, le public, le contexte et la relation produit restent suffisamment comparables ; la trace doit alors dire `WHY-NOW`, ce qui reste identique et ce qui change. Une répétition due à la disponibilité d’un profil ou à la réussite d’un run précédent n’est pas une décision située. Lorsqu’un profil précédent est disponible, `REUSE-CHALLENGE` s’applique aussi au style, et l’absence de profil reste une sortie valide.

Un profil observé dans une référence réelle, découvert par recherche ou construit pour la décision peut être préféré aux profils internes ci-dessus lorsqu’il sert mieux le JTBD, le public ou le contexte. Il suit la même discipline : intention, axes d’expression, contre-indication, transformation de la référence et `PROFILE-DECISION` dans la trace. Le catalogue interne n’est ni exhaustif ni prioritaire par défaut ; une référence n’est jamais une recette, un profil externe n’est jamais une autorisation de copier une marque, une interface, un asset ou un composant tel quel.

### Taxonomie transversale

Les profils ne sont pas tous du même type. Avant de choisir un profil, distingue sa dimension principale et les dimensions qu’il influence réellement :

| Dimension | Exemples | Question de décision |
|---|---|---|
| Composition | `EDITORIAL_PRECISION`, Swiss, modulaire, radial, asymétrique | Comment le regard circule-t-il et où se situe le foyer ? |
| Matière et rendu | `RAW_BRUTALISM`, `TACTILE_VOLUME`, imprimé, plat, métallique | Quelle matérialité ou quel degré de planéité sert le produit ? |
| Représentation | `PICTORIAL_UTILITY`, pixel art, collage, vectoriel, photographie, 3D | Que rend visible ou compréhensible le mode de représentation ? |
| Époque et culture | rétro, Y2K, cyberpunk, moderniste, vernaculaire | Quelle mémoire ou relation culturelle est activée, pour quel public ? |
| Densité et énergie | minimaliste, maximaliste, silencieuse, énergique, contemplative | Quelle quantité de signal et de variation la tâche peut-elle porter ? |
| Interaction et temps | instrumentale, ludique, cinétique, réactive, séquentielle | Que change le geste, la transition ou le temps dans la compréhension ? |
| Voix et comportement | populaire, institutionnelle, expérimentale, chaleureuse, radicale | Quelle relation la surface établit-elle avec la personne ? |

Ces dimensions peuvent être combinées, mais leur combinaison doit produire une thèse. `Y2K`, `cyberpunk`, `rétro`, `pop art`, `Swiss` ou `brutalisme` peuvent être des références culturelles, des influences ou des dials ; ils ne sont pas automatiquement des profils canoniques ni des prescriptions de surface.

| Profil | Intention | Expression possible | Contre-indications |
|---|---|---|---|
| `STYLE/RAW_BRUTALISM` | Rendre une position, contrainte ou matière impossible à ignorer. | Structure tendue, type frontal mais lisible, matière franche, contraste net, densité concentrée. | Contexte critique, première fois, données sensibles ou friction qui masque état/action. Ne jamais imiter un défaut d’accessibilité. |
| `STYLE/EDITORIAL_PRECISION` | Donner au langage, au rythme et à la sélection le poids principal. | Baseline, colonnes, blancs calibrés, hiérarchie typo, métadonnées précises, densité séquencée. | Dashboard temps réel, comparaison très rapide ou données dominantes. Éviter la préciosité. |
| `STYLE/PICTORIAL_UTILITY` | Transformer image, illustration ou scène en explication ou repère. | Composition autour d’un artefact, type sobre, matière visuelle porteuse d’une relation produit. | Image sans fonction explicative, droits/provenance/alternative/performance non maîtrisés. |
| `STYLE/QUIET_SYSTEM` | Rendre un système fiable, calme et opérable sans neutralité vide. | Colonnes, baseline, modules réglés, type rationnel, matière réduite à des seuils et états utiles. | Campagne, manifeste ou objet de collection à présence émotionnelle autonome. |
| `STYLE/MAXIMAL_EXPRESSION` | Donner à l’abondance, à l’énergie ou à la pluralité une hiérarchie lisible et mémorable. | Contrastes de masse, couleurs ou matières coordonnées, rythme dense, superposition maîtrisée, contenu riche et points de repos. | Tâche urgente, surcharge cognitive, statut critique ambigu ou public non préparé. |
| `STYLE/DIGITAL_MEMORY` | Transformer une mémoire numérique ou une culture d’écran en relation utile au produit. | Pixel, raster, scanline, interface rétro, signal, néon ou artefact de compression soumis à une hiérarchie actuelle. | Nostalgie plaquée, cliché cyberpunk, faible lisibilité, motion agressive ou performance non maîtrisée. |
| `STYLE/TACTILE_VOLUME` | Donner chaleur, proximité et matérialité à une interaction ou une identité. | Volume doux, ombres calibrées, surface tactile, objets authored, feedback physique et profondeur mesurée. | Contraste faible, affordance ambiguë, interface dense, donnée critique ou poids de rendu excessif. |
| `STYLE/COLLAGE_ASSEMBLY` | Rendre visibles l’archive, la pluralité, la tension ou l’assemblage de sources. | Fragments, découpes, superpositions, échelles disjointes, annotations et provenance intégrées à la composition. | Provenance ou droits incertains, hiérarchie confuse, lecture linéaire indispensable ou collage purement décoratif. |

### Usage et test

BIBLIOTHEQUE fournit l’architecture, pas l’habillage. Un même objet ou une même scène peut recevoir des expressions différentes sans changer sa responsabilité de preuve.

> **Test de style.** Masque les couleurs de marque, l’image et le logo. Si hiérarchie, type, densité et matière ne traduisent plus une différence substantielle, le profil dépend du médium masqué. Il est légitime si ce médium porte une relation déclarée et dispose d’un fallback. Sinon, il n’y avait pas de profil choisi, seulement une étiquette.

### Dials

[À ADAPTER] Les dials sont des relations perceptuelles qualitatives, non des recettes de layout, des valeurs machine ou des scores. Un dial peut rester inchangé si aucune décision du run ne le concerne ; sa position, sa contre-indication, son médium, son scope et sa conséquence observable doivent être formulés sans fabriquer de seuil esthétique.

| Dial | Pôle bas | Pôle haut | Vérification |
|---|---|---|---|
| Variance | Prévisibilité, répétition, repères stables. | Surprise, contraste et rupture justifiée. | La variation aide-t-elle le parcours ? |
| Motion | Continuité minimale, feedback discret. | Expressivité au service du repérage, de la causalité ou de la matière. | La motion améliore-t-elle la compréhension ? |
| Densité | Respiration et focalisation. | Information utile par viewport et accès rapide. | La densité reflète-t-elle une décision réelle ? |
| Contraste | Différence contenue, transitions douces et hiérarchie calme. | Seuils nets, opposition et signal prioritaire. | Le contraste clarifie-t-il sans écraser les états ou la lecture ? |
| Matérialité | Planéité, abstraction et économie de surface. | Texture, volume ou présence tactile. | La matière porte-t-elle une relation ou seulement une décoration ? |
| Voix typographique | Neutralité fonctionnelle et continuité. | Personnalité, rythme éditorial ou expressivité contrôlée. | La voix survit-elle à la locale, au contenu long et au reflow ? |
| Formalité | Proximité, spontanéité et adresse directe. | Institution, précision et distance maîtrisée. | Le registre correspond-il au contexte de confiance et au public ? |
| Intensité émotionnelle | Retenue, calme et juste distance. | Énergie, chaleur ou impact immédiat. | L’intensité sert-elle la relation sans masquer la tâche ? |
| Originalité | Convention appropriée et repères familiers. | Écart structurel ou expressif défendu. | L’écart produit-il une compréhension, une mémoire ou une valeur située ? |

Aucun dial ne neutralise une exigence d’accessibilité, de contexte critique, de preuve ou de direction retenue. Les dials sont des hypothèses de jugement de SAVOIR ; ACTION vérifie leurs conséquences avec ses méthodes, gates, statuts et verdicts. Ils sont choisis après `DOMAIN-FRAME` et `CREATIVE-BOOT`, seulement s’ils changent une décision ; une position extrême est une décision à défendre, non un style à démontrer. La position retenue, l’alternative ou l’absence justifiée, la contre-indication et la conséquence observable doivent pouvoir être reliées au premier objet.

### Styles visuels, culturels et multi-médias

Un profil peut s’exprimer dans le graphique, l’interface, l’image, le mouvement, le son, l’espace ou la matière, selon le médium. Le nom du profil ne fixe donc pas une technique. `STYLE/DIGITAL_MEMORY` peut conduire à une typographie, une animation, un son, une texture ou une logique de navigation ; `STYLE/TACTILE_VOLUME` peut concerner une illustration, une interaction, une scène 3D ou un feedback haptique. Toute traduction doit déclarer le médium, les capacités disponibles, les contraintes de production et la preuve adaptée.

Le style est une hypothèse de direction, jamais un raccourci de secteur. Ne déduis pas qu’une marque culturelle doit être maximaliste, qu’un outil financier doit être minimaliste ou qu’un produit technique doit être cyberpunk. Le produit, le JTBD, le public, la donnée, la culture et la contrainte déterminent si une expression est pertinente.

### Ponctuation située : le tiret cadratin n’est pas une signature

Le tiret cadratin (`—`) n’est ni interdit ni recommandé par défaut. Utilise-le lorsqu’il exprime réellement une rupture, une apposition, une relation éditoriale ou une voix locale compatible avec la langue et le support. Dans une instruction, une microcopie, un label ou une trace, préfère la ponctuation qui rend la relation la plus précise : point pour séparer deux décisions, deux-points pour introduire une explication, virgule pour une incise courte, point-virgule pour deux propositions étroitement liées, ou aucune ponctuation si le label doit rester compact.

Un emploi répétitif du cadratin pour donner un rythme « premium », relier artificiellement des clauses, remplacer une relation logique non formulée ou produire une cadence reconnaissable est un signal de **slop stylistique**. Plusieurs cadratins rapprochés ne constituent pas une violation automatique ; ils déclenchent une relecture : le sens, la locale, le reflow, la lecture assistée et la densité de l’interface doivent rester meilleurs avec la ponctuation choisie. Le style doit être identifiable par une décision de contenu, de structure ou de typographie, jamais par une marque de ponctuation répétée.

### Test anti-slop procédural

> **Slop procédural :** trace ou procédure qui respecte la forme attendue sans produire de décision modifiée, d’observation inspectable, de preuve adaptée, de limite explicite ou de prochaine action utile.

Avant de conserver une étape, un tag, un profil ou une formulation, demande : **qu’est-ce qui change si cette ligne est vraie, fausse ou absente ?** Si rien ne change, supprime-la, regroupe-la dans la source propriétaire ou utilise `N/A-JUSTIFIED`. Une procédure qui exige de nommer une décision sans jamais la trancher, qui charge tous les profils, qui répète les mêmes adjectifs ou qui produit seulement des statuts rassurants est du slop procédural, même si sa trace est complète.

Le terme « slop » reste un diagnostic de mécanisme, pas un verdict esthétique. Décris toujours le symptôme observable : répétition de famille visuelle, profil choisi sans décision, claim non vérifié, champ sans effet, jargon non actionnable ou preuve recyclée.

### Vocabulaire à rendre observable

Les termes ci-dessous ne sont pas interdits comme citations, hypothèses ou langage de marque. Ils sont insuffisants comme décision seuls. Lorsqu’ils apparaissent dans une justification, ajoute leur conséquence perceptible, comportementale ou technique et leur contre-indication.

| Terme faible seul | À préciser par | À éviter comme preuve de |
|---|---|---|
| « premium », « luxe », « haut de gamme » | proportion, matière, rareté, prix, public, tâche et signal observé | qualité universelle ou statut automatique |
| « moderne », « contemporain », « actuel » | contraste avec une convention datée, public, usage ou contrainte réelle | nouveauté ou pertinence par défaut |
| « beau », « élégant », « propre » | relation de forme, hiérarchie, rythme, lisibilité ou défaut retiré | direction ou efficacité |
| « original », « créatif », « audacieux » | position choisie, parti (écart au modal), risque assumé et différence perceptible | divergence simplement décorative |
| « intuitif », « simple », « fluide », « seamless » | tâche, étape, état, effort, erreur et preuve d’usage | utilisabilité sans observation |
| « cohérent », « harmonieux », « aligné » | relation précise entre éléments, règle de système et exception | approbation globale non vérifiable |
| « immersif », « impactant », « émotionnel » | effet attendu, contexte, durée, risque de surcharge et preuve située | effet garanti sur tout public |

Cette table ne remplace pas le jugement de contexte. Elle empêche seulement le vocabulaire d’acquitter une décision qu’aucun objet, changement ou test ne soutient.

---

# SAVOIR/SYSTEM — tokens et composants

[REQUIS PAR LE MODULE — blast radius partagé, token ou primitive] Sépare tokens primitifs — mesures, palette, familles — et tokens sémantiques — surface, texte, action, danger, élévation.

Documente le comportement des tokens et composants, pas seulement leurs noms. Lorsqu’un token, composant, convention, format ou comportement affecte plusieurs consumers, plusieurs surfaces ou une source de vérité partagée, signale à `DIRECTION/START` l’effet partagé. START classe en `SYSTÈME` si la décision partagée est l’objet direct du run ; si elle découle d’une décision de direction, la direction est traitée d’abord et le run système dépendant ouvert ensuite, sauf décisions inséparables (`DIRECTION/START/TREE`).

`DIRECTION/START` et `ACTION/RUN-SYSTEM` restent les autorités de classification et d’exécution ; `SAVOIR/SYSTEM` décrit le jugement technique et systémique.

Quand plusieurs consumers existent — fichier de design, web, mobile, thèmes ou documentation — évalue un format interopérable, des modes et une source de vérité. La décision précise impact, semanticité, thème, owner, consumers, migration, rollback, fallback, coût de maintenance, méthode et scope de non-régression, résultat, limite et prochaine revue.

La stack existante prime. Toute fondation de composants est choisie pour accessibilité, maintenance, conventions et capacité à adapter tokens et états. Une primitive accessible peut protéger les comportements sans imposer la direction visuelle.

N’empile pas plusieurs bibliothèques concurrentes sans raison de compatibilité ou migration. Un framework ou un kit n’est jamais la direction créative du produit.

Le contrat de composant partagé est défini par `BIBLIOTHEQUE/COMPONENTS`. SAVOIR en garde le jugement : tokens primitifs et sémantiques, modes, interopérabilité et maintenance ; `ACTION/RUN-SYSTEM` conserve l’impact, les consumers, la migration, le rollback, la preuve et le verdict.

---

# SAVOIR/CONTEXT — accessibilité, contexte et robustesse

[REQUIS PAR LE MODULE — contrôle applicable dans ACTION] SAVOIR décrit la décision de conception contextualisée. ACTION porte le contrôle, le scope, la méthode, la preuve et le verdict. Une phrase de conformité dans SAVOIR ne remplace pas un contrôle Gate A.

Les principes de livraison sont : contraste calculé, sémantique, nom accessible, clavier, focus visible, information non chromatique, cibles adaptées, reduced motion, contenu long et récupération compréhensible.

### Contextes à fort enjeu

Cette liste est indicative et non exhaustive.

| Catégorie | Exemples | Priorité |
|---|---|---|
| Réglementé ou sécurité critique | Santé, paiement, commande machine, sécurité. | Convention, confirmation, traçabilité, prévention et récupération. |
| Décision intensive | Supervision, finance professionnelle, data dense. | Hiérarchie, densité utile, vitesse de lecture et précision. |
| Réactivité ou gameplay | Jeu, contrôle temps réel, action à latence sensible. | Lisibilité, feedback et réponse immédiate. |

La singularité d’un contexte critique peut être la clarté, la robustesse et la convention fiable. Elle ne requiert ni spectacle ni rupture de repère.

Lorsque expression et sécurité, clarté, conformité ou récupération entrent en tension, la protection critique déclarée par `DIRECTION/START` prévaut. Résous la direction par hiérarchie, contenu, confirmation et robustesse, non par un effet spectaculaire ; le référentiel, le médium, le scope, la méthode et la limite restent explicites dans ACTION.

### Responsive et performance

Recompose plutôt que comprimer. Contenu, priorité, ordonnancement et interaction peuvent changer selon appareil et contexte. Réserve l’espace des médias, donne un feedback immédiat, rends les erreurs récupérables, évite les attentes silencieuses et protège l’information prioritaire.

Les propriétés CSS, valeurs de viewport, formats, budgets et support navigateur sont des ressources techniques, non des lois de style.

### Motion et espace

La motion doit expliquer, confirmer, orienter ou rendre une relation matérielle compréhensible. Elle ne doit pas retarder la tâche. Intensité, durée, easing, distance et ressort s’ajustent à l’action, au device et au langage du produit.

Une animation interactive est décrite comme un système d’états : état initial, trigger, transition, interruption et résultat. Une scène 3D ou spatiale est justifiée seulement lorsqu’elle rend un produit, une relation de profondeur, une navigation ou une information spatiale plus compréhensible.

Documente l’équivalent de motion réduite, l’interruption, le fallback statique, clavier/tactile, contenu alternatif, performance, device, runtime, mobile et capture. Une capture documente le rendu dans son scope, mais ne remplace pas un test d’accessibilité, de performance ou de tâche. Si motion ou scène ne donnent ni feedback, ni information, ni relation spatiale, préfère la suppression ou une composition 2D plus juste.

---

# SAVOIR/TECH — techniques, tests et stack

[MÉTHODE] CSS, code, outils et automatisation servent hiérarchie, performance, cohérence et accessibilité. Utilise une technique parce qu’elle produit un effet ou une robustesse impossible à obtenir plus simplement, non parce qu’elle est disponible.

Associe chaque technique à une preuve adaptée :

| Question | Preuve adaptée |
|---|---|
| Transformation ou calcul non trivial | Script ou test déterministe. |
| Comportement d’interface | Inspection du runtime. |
| Relation visuelle simple | Capture et revue de code. |
| Coût de performance | Mesure de build, profiling ou observation runtime. |
| Compatibilité | Test sur support déclaré et fallback. |

### Hiérarchie de jugement pour les interfaces

Le jugement commence par `P0` : direction visuelle, hiérarchie, composition, typographie, matière, états, contenu et action dominante. `P1` vérifie le plancher de compréhension, d’usage et d’accessibilité. `P2` vérifie que la décision est correctement traduite dans le runtime réel — web, Flutter, Swift, Kotlin ou autre stack. `P3` couvre performance, compatibilité, robustesse et maintien lorsque le risque le requiert. Si un risque critique d’usage, d’accessibilité, de sécurité, de confidentialité ou de permission est déclaré, sa protection passe avant l’optimisation visuelle, sans supprimer les autres contrôles. Une plateforme ne justifie ni une dégradation silencieuse du craft ni un `PASS` sans preuve.

### Preuve par médium

### Traduire production et observation par médium

Ces points de départ adaptent le contrat au support utile ; ils ne constituent ni catalogue obligatoire ni preuve que les moyens sont connectés. Rapproche ressource retrouvable, action de fabrication et observation dans la fiche ou la spec existante ; charge seulement la famille qui peut changer la décision.

| Médium concerné | Ressource et intervention à concrétiser | Observation adaptée et limite |
|---|---|---|
| Web ou application native | Primitives de la stack réelle, tokens, contenu, états et intégration des assets. | Runtime, device, clavier ou gestes pertinents ; la recette HTML ne couvre pas automatiquement le natif. |
| Image ou identité | Fichiers source, police, marque, dessin, photo ou pack autorisé ; silhouette, cadrage, matière et déclinaisons. | Taille d’usage, détails, fonds et série ; l’image produite ne prouve ni authenticité ni droits. |
| Print, document ou présentation | Gabarit, contenu, police, format, marges, pagination ou ordre de lecture ; préparer l’export utile. | Pages ou slides finales, distance et support ; une prévisualisation numérique ne prouve pas encre, papier ou projection. |
| Motion ou vidéo | Assets, séquence, transitions, rythme, interruptions et alternative adaptée au canal. | Séquence rendue et durée, lecture et interruption si applicables ; une image fixe ne prouve pas la fluidité. |
| Son | Fichier, voix ou matière autorisée ; montage, niveaux, temporalité et alternative textuelle lorsque pertinente. | Écoute du fichier exporté et contexte de restitution ; waveform et transcription ne prouvent pas la qualité sonore. |
| Spatial ou 3D | Modèle, matériaux, éclairage, échelle, caméra, interaction et fallback selon le support. | Runtime, device, profondeur, confort et coût ; une capture 2D ne prouve pas l’expérience spatiale. |

Si production ou observation manque, conserve le plafond et la prochaine preuve dans les responsabilités ci-dessous ; une documentation de médium n’est pas une capacité de fabrication.

[MÉTHODE] Pour tout médium non web — natif mobile, desktop, spatial, print ou embarqué — examine cinq responsabilités de preuve, regroupables dans un même artefact, avant de juger :

| Dérivation | Question | Conséquence de preuve |
|---|---|---|
| Rendu observable | Comment le rendu réel est-il observé ? | Capture device, émulateur, build sur support réel, capture casque, vidéo d’interaction ou épreuve print. Sans support d’observation, le craft reste `NOT-VERIFIED`. |
| Idiomes d’interaction | Pointer/clavier, tactile/gestes, controller, regard ou voix ? | Un idiome est `N/A-JUSTIFIED` uniquement s’il est non applicable au médium et au scope déclarés ; tout substitut est nommé, testé et limité. |
| Référentiel applicable | Quelle norme ou guideline fait référence ? | Séparer `CONFORMANCE-TARGET` — référentiel, version, niveau, scope et owner — de `QUALITY-TARGET` — confort, lisibilité, contraste ou autre cible qualitative. |
| Unité de budget | Qu’est-ce qui coûte dans ce médium ? | Load/INP pour le web ; lancement, frame rate et mémoire pour le natif ; frame rate, confort motion et lisibilité à distance pour le spatial ; encre et contraste pour le print, ou équivalent déclaré. |
| Preuve indisponible | Que ne peut-on pas vérifier ici ? | `NOT-VERIFIED` + `NEXT-PROOF`, jamais simulé. Traduire en équivalent du médium lorsque cela est possible. |

Un médium non web ne rétrograde pas silencieusement la décision : il traduit le craft et l’usage dans d’autres idiomes, puis adapte le support, l’unité de budget et la limite de la preuve lorsque le risque le requiert. L’adaptation de production est distincte : stack, délais, équipe et capacité déterminent ce qui est exécutable. Une contrainte déterminante porte owner, conséquence et prochaine preuve. L’absence de preuve produit d’abord `NOT-VERIFIED` et `NEXT-PROOF` ; `FAIL-ASSUMED` reste réservé à un échec connu, limité, assigné, documenté et re-testable selon ACTION/OVERRIDE, sans usage pour masquer une indisponibilité de runtime.

`CONFORMANCE-TARGET` nomme la référence ou le niveau visé ; il ne signifie pas que la conformité est obtenue. Pour juger ou transmettre un claim, conserver séparément la cible, la méthode exécutée, le scope et le runtime observés, le résultat, la limite et la `NEXT-PROOF`. Une cible déclarée sans observation adaptée reste `NOT-VERIFIED` ; une observation hors scope ne s’étend pas silencieusement à l’ensemble du produit.

Aucun outil, script ou package ne reçoit automatiquement un `PASS`. Une nouvelle dépendance exige l’approbation et les champs de la politique d’`ACTION/POLICIES` (inspection et ressources techniques) ; à défaut, conserve `NOT-VERIFIED` ou retourne le run.

Toute ressource de stack indique les sept champs d’`ACTION/POLICIES` (inspection et ressources techniques) et, lorsqu’elle soutient un claim, les claims applicables (`SAVOIR/TOOLS`). `SAVOIR/TOOLS` définit les exigences et limites ; ACTION conserve la fiche exécutée, la preuve, les statuts et le verdict ; CHANGELOG intervient lorsqu’une règle ou une route devient partagée.

---

# SAVOIR/TOOLS — claims, tendances et calibration

## Claims externes et péremption

[REQUIS PAR LE MODULE — claim qui influence une décision, un seuil, une route, une tendance ou un livrable] Tout claim utilisé dans un run indique :

```text
CLAIM-TYPE — empirique, normatif, technique, culturel, réglementaire ou local.
STATEMENT
SCOPE
SOURCE
VERSION / DATE-VERIFIED
LIMIT
INTENDED-USE
OWNER
REVIEW-DATE
NEXT-PROOF
```

Il reste dans la trace locale du run tant qu’il ne modifie pas une règle partagée. Toute promotion vers une règle commune exige une décision explicite du propriétaire, la compatibilité, l’owner, la preuve et l’entrée de gouvernance appropriée ; un claim local ne devient pas une règle par répétition.

Un claim `À REVÉRIFIER` peut guider une recherche ou un test local. Il ne justifie jamais seul une règle universelle, un seuil, une obligation de production ou une promesse de résultat.

Sépare :

- claim transférable ;
- source observée ;
- asset et droit ;
- observation locale de run.

Une source ou un asset ne devient pas automatiquement un claim. Une observation de run ne devient pas automatiquement une règle durable. Une référence observée ne devient pas automatiquement une autorisation de réemploi.

## Goût, références et tendances

[DURABLE] Le goût n’est pas un canon de marques. C’est la capacité à reconnaître une solution proportionnée, spécifique, lisible et tenue.

Observe une référence pour extraire une relation — rythme, densité, hiérarchie, matériau ou compromis — et non une surface à copier.

En `DIRECTION`, nomme une interface, une ressource hors écran ou un principe réellement observé qui apporte une calibration utile sur un axe concret. Lorsque la direction est nouvelle, ambiguë, risquée ou exposée à une forte convergence générique, un sourcing Web ou une recherche de références est recommandé ; il devient requis seulement si le contrat du run dépend d’un claim, d’une tendance, d’une provenance ou d’une décision qui ne peut pas être honnêtement fondée en mémoire. Si aucune calibration pertinente n’est disponible, déclare cette limite et recherche ou génère une ancre utile.

Le sourcing de `DIRECTION` sépare trois rôles : **ancrage de direction** — pourquoi une référence éclaire un axe ou une décision ; **ancrage de production** — comment un asset, une matière ou un composant peut être construit ; **ancrage de vérification** — comment contrôler lisibilité, accessibilité, comportement, performance ou crédibilité. Une même source peut remplir plusieurs rôles seulement si chacun est explicité. La référence est analysée puis transformée en choix propres au produit ; elle ne sert jamais simultanément de moodboard décoratif, de spécification implicite et de preuve de réussite.

[VEILLE] Les listes de produits contemporains, tendances, registres culturels et snapshots ne sont pas neutres. Chaque élément mobilisé dans un run porte source, date, portée et limite dans sa trace locale.

<!-- noyau:début COMP-VAGUES -->
<!-- concept:ANT-01 -->
[VEILLE 2026-10] **Marqueurs de vague**, pour nommer `MODAL` (`DIRECTION/CREATIVE-BOOT`), jamais pour interdire : un marqueur gardé par décision reste valide. Charge `SAVOIR/TOOLS/CONVERGENCE` si la convergence peut changer une décision ; les observations, sources et Signaux à confirmer y restent datés et limités. Retrouve les sources avant tout claim de fréquence, tendance ou provenance ; revue avant 2027-03.
<!-- noyau:fin COMP-VAGUES -->

### CONVERGENCE — observations datées

[VEILLE 2026-09] **Marqueurs de vague**, pour nommer `MODAL` (`DIRECTION/CREATIVE-BOOT`), jamais pour interdire : un marqueur gardé par décision reste valide. Vague 1 : violet, police Inter, halos et gradient décoratif, hero SaaS à cartes répétées. Vague 2 : fond beige ou crème, brun, serif de caractère ou serif italique, orange rouille, bandeau défilant, illustration peinte, tramage. Vague 3 : dithering, logos pixel, ASCII, hachures de plan, gravures, bleu Klein, libellés mono en capitales, repères de recadrage, paysage peint en fond. Source : essais internes (26-09-2026) et revue de références de designers (27-09-2026), 6 rendus sur 6 sur fond crème et brun, avec ou sans système. Signaux à confirmer : grotesque large ou condensée (Archivo) sur fond blanc neutre avec un seul accent vif (27-09-2026, 3 rendus sur 3, même auteur, non retrouvé ensuite) ; même objet central par brief (fournées du jour ; facture tamponnée) et même grotesque de titre sur un brief, avec ou sans système (30-09-2026, auto-comparaison, 6 rendus). À revoir avant 2027-03.
[VEILLE 2026-10] **Écran d’accueil d’app**, même usage (nommer `MODAL`, jamais interdire) : image d’ambiance ou illustration dominant le haut, slogan court, boutons d’inscription en bas et conditions en petit ; contre-exemple : montrer le produit en action (un objet de preuve) plutôt qu’une ambiance. Source : revue interne des références fournies en conversation (02-10-2026) ; sélection et fichiers images non archivés dans cette distribution. Observation qualitative limitée, fréquence `NOT-VERIFIED` ; l’apparence d’une image ne permet pas d’attester sa génération. Retrouver les sources avant tout claim de fréquence, de tendance générale ou de provenance. À revoir avant 2027-03.

<!-- noyau:début MOY-CARTE -->
<!-- concept:MOY-01 -->
[VEILLE 2026-09] **Carte des moyens par couche** : des sources, jamais des styles. Si une ressource ou son intégration reste à choisir, charge `SAVOIR/TOOLS/MOYENS` pour chercher par rôle. Vérifie disponibilité, licence et conditions pour chaque ressource retenue au moment de l’intégrer ; le nom d’une plateforme ne vaut ni connexion ni autorisation. Sans intrant ni route autorisée, assets figuratifs et contenu réel restent hors plafond (`FABRICATION`). Revue avant 2027-03.
<!-- noyau:fin MOY-CARTE -->

### MOYENS — ressources par couche

[VEILLE 2026-09] **Carte des moyens par couche** : des sources, jamais des styles. Licence et conditions d’usage vérifiées pour chaque ressource retenue, au moment de l’intégrer ; le nom d’une plateforme ne vaut pas autorisation. Pour chaque couche : où chercher, comment choisir, ce qui limite.
- **Typographie :** polices de la marque ; Google Fonts (licences ouvertes, surtout SIL OFL) ; Fontshare (licence FFL ou OFL selon la police). Choisir par la voix et la donnée à porter ; vérifier chargement, graisses et glyphes (accents, chiffres) dans la cible.
- **Icônes :** une famille qui couvre les pictogrammes nécessaires (par exemple Lucide, Phosphor) ; poids, taille et sens accordés au texte ; mélanger des familles demande une raison visible.
- **Composants :** design system fourni, sinon bibliothèque éprouvée (par exemple shadcn, Radix) ; hors Web, les idiomes de la plateforme.
- **Données et objets de preuve :** contenu du client, sinon exemples marqués ; codables, donc au plafond sans intrant.
- **Texture et traitement :** CSS, SVG, canvas ; rendu inspecté sur capture, performance mesurée dans le runtime cible.
- **Photographie :** client (même au téléphone, en lumière du jour), banques sous licence (Wikimedia Commons, Unsplash).
- **Illustration et 3D :** commande, packs sous licence, génération dirigée avec références (`GÉNÉRÉ-DIRIGÉ`).
- **Fichiers et marque :** Figma ou kit de marque par connecteur.

Sans intrant ni route autorisée, les assets figuratifs et le contenu réel restent hors plafond (`FABRICATION`). À revoir avant 2027-03.

**Ce que vaut cette carte.** Elle nomme des sources : le paquet n’en contient aucune et n’a testé ni leur accès ni leur intégration. Une ressource compte dans le plafond seulement une fois atteinte depuis l’environnement du run, chargée dans l’artefact et vue sur capture ; nommée ou seulement atteignable, elle reste une intention. Une police ou une image externe bloquée par `scripts/check_render.py` sans `--allow-external` n’est pas observée. Si l’accès échoue (réseau, licence, connecteur), dis-le et prends la route de production qui tient sans elle (`DIRECTION/VISUAL_TARGET` : `CODE-NATIVE`, `SANS-ASSET` ou emplacement marqué) ; le plafond baisse et la trace le dit.

Une tendance est une hypothèse de direction. Avant de l’utiliser, vérifie qu’elle sert le JTBD, améliore la compréhension, reste accessible et performante et survit lorsque son nom marketing disparaît.

Distingue :

| Niveau | Définition |
|---|---|
| Signal de veille | Observation datée. |
| Principe durable | Mécanisme transférable. |
| Style | Décision située d’expression. |
| Technique | Moyen de production ou de preuve. |

Le terme `same-energy` peut indexer un risque de convergence, mais ne remplace jamais une description causale de l’échec.

---

# SAVOIR/INTEGRITY — limites, délégation et critique

### Test de non-récitation

Avant de conserver un artefact de jugement, demande : « Quelle décision concrète a changé grâce à ce module ? » Si la réponse est aucune, l’artefact est documentaire plutôt que décisionnel ; arrête ou simplifie. Une décision que le module a confirmée se déclare comme confirmation ; `N/A-JUSTIFIED` reste réservé au module qui ne pouvait rien changer.

## Modes d’échec d’application

[REQUIS PAR LE MODULE — avant verdict `DIRECTION` ou lorsqu’une règle risque d’être satisfaite dans la forme] Le danger principal n’est pas l’absence de règles ; c’est l’artefact textuel qui affirme qu’une règle a été suivie sans que décision, observation ou preuve aient réellement eu lieu.

Les échecs récurrents sont :

- mode choisi par confort ;
- directions seulement adjectivales ;
- fiche textuelle présentée comme ancre ;
- référence citée mais non observée ;
- test non rejoué après modification ;
- compromis vague ;
- retrait artificiel ;
- effet de matière choisi avant la direction ;
- feedback humain invoqué sans artefact regardable ;
- preuve de contexte produit supposée plutôt qu’établie ;
- style ou dial choisi sans décision réelle à modifier.

Avant un verdict `DIRECTION`, réponds par une phrase liée à un objet concret :

| Question | Bloque si… |
|---|---|
| Quelle ancre utile et quelle spec ont été réellement observées ? | Une ancre ou une spec est requise par le risque ou le contrat, mais aucune n’est exploitable ; si aucune ancre ne peut modifier la décision, justifie sa non-applicabilité. |
| Quelle décision perceptible porte la direction ? | Rien ne dépasse un défaut de stack ou une intention déclarée. |
| Quelle alternative située a été considérée ? | La décision est ouverte ou exposée à la convergence, mais aucune position distincte ni raison de non-comparaison n’est donnée. |
| Quel écart entre spec et rendu reste ? | Écart important ignoré ou justifié après coup. |
| Quelle preuve manque encore ? | `PASS` affirmé sans preuve adaptée. |
| Quelle hypothèse de contexte reste incertaine ? | Coût d’erreur élevé sans owner ni prochaine preuve. |
| Quelle décision concrète a changé grâce à cette procédure ? | Aucune décision modifiée, confirmée ou abandonnée, sans `N/A-JUSTIFIED` justifié ni `NOT-OBSERVED` déclaré (valeurs de repli d’`ACTION/STATUS`). |
| Quelle règle risque d’être satisfaite dans la lettre seulement ? | Aucun test d’échappatoire théâtrale ni artefact de conséquence observable n’a été fourni. |

## Contrôle d’intégrité

Relie au moins une réponse portant sur le risque le plus élevé à un artefact consultable : capture, spec, diff, test, code, URL, donnée ou journal.

Si le lien ne peut pas être inspecté, la réponse n’est pas une preuve. Si une capacité a été déléguée, inspecte l’artefact et le résultat ; la délégation seule ne constitue jamais une validation.

Lorsque la règle est satisfaite par le texte mais qu’aucun objet ou changement de décision n’est inspectable, renvoie le run à ACTION avec le couple canonique approprié : `N/A-JUSTIFIED` si le contrôle ou la décision est réellement non applicable ; `NOT-VERIFIED` si la preuve pertinente manque ; `EXPLORATORY` si un artefact existe mais que le périmètre ou la preuve de décision est incomplet ; `RETURNED` si une correction ou une preuve doit être reprise. SAVOIR rend visible la limite ; ACTION décide si le run peut être fermé.

## Limites, délégation et critique

[REQUIS PAR LE MODULE — capacité incertaine, direction ambiguë, asset critique ou besoin de second regard] Distingue ce qui est connu, inféré, vérifié et hors de portée.

Une capacité disponible modifie le type de preuve possible ; elle ne permet jamais d’affirmer une qualité sans examen du résultat. Toute délégation conserve délégataire, rôle, capacité déclarée, méthode, scope, artefact/résultat consulté, date/version, limite, owner de décision finale, `NEXT-PROOF` et condition de reprise ou d’escalade.

<!-- noyau:début VER-FAUX-ASSET -->
<!-- concept:HON-02 -->
Ne fais jamais passer abstraction CSS, SVG, image générée ou placeholder pour photo, illustration, logomark, son ou asset authentique. Une abstraction assumée est autorisée si son rôle est honnête, son contenu non trompeur et son effet approprié. Un faux asset de marque ne l’est pas.
<!-- noyau:fin VER-FAUX-ASSET -->

Le modèle, le prompt ou l’outil de génération ne constituent jamais, à eux seuls, une preuve de qualité, de droit ou d’adéquation au contexte.

La curation dirigée est admise lorsqu’elle comble un besoin réel, avec type d’origine, source/provenance, statut d’autorisation, portée d’usage, transformation, limite, owner et prochaine revue dans la trace locale du run. Ne la confonds pas avec une accumulation passive.

Les rôles de critique sont des lentilles, non une simulation d’équipe. Chaque rôle identifie un problème observable, une correction, une preuve et un périmètre. Un regard humain distinct de l’auteur ou de l’owner peut apporter un contrepoint situé ; ne le qualifie pas d’indépendant sans déclarer relation, rôle, méthode, date et limites. Active `ACTION/GATE-B/B3` lorsque son scope est requis.

L’autonomie accordée à l’agent par l’utilisateur ou l’owner couvre uniquement le périmètre `DIRECTION` explicitement annoncé. Elle ne remplace ni les droits, ni l’owner final, ni une escalade requise ; le checkpoint suit `ACTION/PIPELINE-DIRECTION` (la première proposition en tient lieu, sauf action irréversible ou coûteuse).

---

## Règles d’or — lecture rapide

Ce résumé n’est pas une procédure de livraison. Il ne crée aucune route, gate, issue ou verdict concurrent ; `DIRECTION` est propriétaire de la classification et du routage général, `SAVOIR` de ses routes de jugement, `BIBLIOTHEQUE` de ses routes structurelles et `ACTION` des routes d’exécution, preuves, gates, états, issues, verdicts et clôtures.

1. Classe le mode dans `DIRECTION/START` avant de choisir la procédure.
2. Cadre JTBD, décision dominante, contraintes et hypothèses à impact.
3. Retire avant d’ajouter ; une décision tenue vaut mieux qu’une accumulation de signaux.
4. Utilise contenu réel, états pertinents et microcopie honnête.
5. Fais passer accessibilité, responsive, récupération et performance avant l’effet.
6. Sur une surface `DIRECTION`, la spec est toujours requise ; l’ancre suit `DIRECTION/VISUAL_TARGET` (utile, ou absence déclarée en exploration ; avant l’acceptation, absolu 2 de `DIRECTION`).
7. Exécute les preuves applicables au mode ; déclare `NOT-VERIFIED` plutôt que de le noter comme `PASS`.
8. Si un risque bloquant reste, retourne, passe en `EXPLORATORY` ou journalise un `FAIL-ASSUMED` autorisé (échec connu) ; un risque non bloquant peut rester en réserve structurée (`ACCEPTED-WITH-RESERVATION`, `ACTION/STATUS`) ; ne compense jamais un axe bloquant par une moyenne.

---

## Méthodologie studio

[MÉTHODE] Le niveau de formalité dépend du mode :

- cadrage et preuve de contexte ;
- direction si `DIRECTION` ;
- système si blast radius partagé ;
- contrat de composant si pattern réutilisable ou critique ;
- assemblage ;
- repasse ciblée ;
- QA et gates applicables ;
- décision et persistance.

<!-- noyau:début BOUCLE-REPASSE -->
Une repasse complète est attendue en `DIRECTION`, recommandée en `STANDARD` et ciblée en `ITER` ou `LITE` sur le périmètre modifié. Cherche ce qui est resté par défaut : alignement optique, échelle, distance, état, composant, mouvement, contenu réel, breakpoint ou récupération. Traduis le défaut retenu avec `SAVOIR/STATE` en intervention concrète et conditionnée, puis réinspecte son effet ; « rendre plus fin » ou « harmoniser » seul n’est pas une résolution.
<!-- noyau:fin BOUCLE-REPASSE -->

Le système n’installe pas mécaniquement le goût. Il soutient la finesse par des gestes précis, conditionnés et réinspectés, et rend le jugement plus difficile à simuler : références observées, décisions nommées, preuves adaptées, compromis assumés et limites déclarées.

> Ce résumé et cette méthodologie aident à lire SAVOIR ; ils ne créent pas de route, gate, statut ou obligation concurrente. Les routes de jugement et de structure restent définies par SAVOIR et BIBLIOTHEQUE ; les routes de classification et d’exécution, ainsi que les verdicts, restent définis par DIRECTION et ACTION.

L’honnêteté sur ce qui manque fait partie de la qualité.
