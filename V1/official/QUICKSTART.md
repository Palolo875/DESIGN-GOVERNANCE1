# Design Governance V1.0.0 — Quickstart (guide opérateur)

**Package Design Governance V1.0.0.** Expérimentation maintenue pour diriger, construire et vérifier un travail de design avec une trace proportionnée au risque. Il est destiné à un usage supervisé et ne constitue pas une preuve d’efficacité en production.

> **Rôle de ce guide :** fournir une interface d’activation rapide. Il oriente la lecture et l’action, mais n’ajoute aucune règle, route, gate, axe, statut, verdict ou autorité. Les cinq sources normatives font foi.

> **Pour qui :** ce guide sert à piloter un run (opérateur, designer ou agent). Pour faire simplement une demande, la section [« Commencer »](../../README.md#commencer) du README du package suffit : vous n’avez pas à choisir de mode.

V1 aide à transformer une demande en **décision située, artefact réel, observation pertinente et trace honnête**. Elle ne promet ni beauté automatique, ni réussite universelle, ni validation d’usage sans preuve adaptée. Elle vise néanmoins un niveau positif : lorsque la décision visuelle est ouverte et que les capacités sont disponibles, le premier rendu doit déjà être composé, spécifique, crédible, présentable et suffisamment résolu pour être jugé comme un objet réel.

## Parcours commun

Pour piloter un run, commencez ici ; les sections suivantes n’approfondissent que si le risque, le périmètre ou la décision le justifie. Une fois la demande classée par `DIRECTION/START` (par l’opérateur ou l’agent, jamais par la personne qui demande), notez :

```text
MODE — DECISION — RISK — NEXT-PROOF — OWNER
```

Répondez ensuite à ces cinq questions :

| Question | Réponse minimale |
|---|---|
| Quelle décision doit changer ? | Le choix concret à trancher, confirmer ou abandonner. |
| Quel risque domine ? | Identité, usage, accessibilité, technique, système ou autre risque déclaré. |
| Quelle preuve peut distinguer les options ? | Mesure, capture, test, comparaison, inspection ou observation adaptée. |
| Qu’est-ce qui est réellement disponible ? | Artefact, navigateur, DOM/CSS, contraste, clavier/AT, participant, runtime, donnée ou source. |
| Qui porte la décision et la prochaine action ? | Owner explicite, avec confirmation ou escalade si nécessaire. |

Produisez la ligne de run, faites l’action la moins coûteuse qui peut changer la décision, puis choisissez une seule suite : **corriger**, **approfondir la preuve**, **rouvrir**, **reclassifier**, **proposer** ou **fermer**. Par défaut, le run s’arrête à la proposition, en trace légère : la première proposition vaut checkpoint, sauf action irréversible ou coûteuse ; **fermer** suppose la trace complète (run persistant, partagé, audité ou acceptation demandée). Passez aux sections suivantes seulement si le risque, le périmètre ou la décision le justifie.

## Carte de résolution rapide

Si la demande est déjà identifiable, consultez [`READING_MAP.md`](./READING_MAP.md) pour le premier chemin, la perspective conditionnelle et la sortie attendue. Cette carte est dérivée et non normative. Si le brief est vague, commencez directement par `DIRECTION/START`.

Une sortie de run a deux formes : la **réponse visible**, par défaut, et le **handoff**, pour une reprise ou un run persistant (voir `ACTION/HANDOFF`). Le niveau de trace ne dépend pas du mode : sans persistance, partage, audit ni acceptation demandée, la **trace légère** suffit (six lignes au plus, à côté de l’artefact ou sous « Trace » après la réponse) ; dans les autres cas, la **trace complète** s’impose. Utilisez `N/A-JUSTIFIED` lorsqu’un champ ou une perspective ne s’applique pas.

## 1. Choisir la profondeur de lecture

Le guide se lit par couches. Ne chargez pas tout le corpus par réflexe ; chargez uniquement ce qui peut modifier la prochaine décision.

### Façade d’activation : ce que chaque source apporte

La ligne du parcours commun est la façade d’activation. `DIRECTION/START` classe la demande ; `DIRECTION` intervient si la cible ou la direction change ; `ACTION` intervient dès qu’un artefact, une preuve, un état ou une clôture est concerné ; `SAVOIR` intervient si le jugement, le craft, la source ou le contexte peut changer la décision ; `BIBLIOTHEQUE` intervient si la structure, le composant ou la micro-interface peut changer la décision. Cette façade ne crée ni mode, ni gate, ni statut, ni propriétaire supplémentaire.

**Bénéfice attendu.** Chargez `DIRECTION` pour obtenir une position située et un premier objet plus fort ; `SAVOIR` pour transformer une impression en jugement et en choix de craft ; `BIBLIOTHEQUE` pour rendre la structure habitable, compatible et maintenable ; `ACTION` pour transformer la décision en livraison observable, corrigible et prouvable. Si aucun de ces gains ne peut modifier la prochaine décision, restez sur le chemin court ; si un risque critique est actif, ne confondez pas chemin court et profondeur insuffisante.

Pour une décision visuelle ouverte, utilisez le **Creative Boot** de `DIRECTION` avant le premier pixel : promesse, objet de preuve, geste, tension et signature structurelles (nombre d’axes : `BIBLIOTHEQUE/TENSION`), jusqu’à trois cibles créatives `SAVOIR/CRAFT`, `MODAL`/`PARTI`, bilan de fabrication (`FABRICATION`), le premier objet et le défaut dominant. Le boot est une vue de cadrage, pas un nouveau formulaire ou une obligation pour les deltas locaux ; il doit modifier la construction ou rester omis. Sur brief vague, la prise de brief de `DIRECTION/EXTERNAL-START` demande au plus trois intrants, en un seul échange, par gain de plafond : contenu réel, marque, asset principal ou route autorisée, destination si elle est incertaine ; ces demandes accompagnent la première proposition, construite dans le même tour avec des hypothèses nommées ; la réponse n’est attendue avant le build que si la personne l’a demandé ou si l’action est irréversible ou coûteuse ; le rendu est construit dans tous les cas.

Si le domaine, le public, la confiance, la culture, la convention ou l’ambition peuvent changer le résultat, activez `DIRECTION/DOMAIN-FRAME`, puis `SAVOIR/SOURCE` pour une recherche orientée décision. Augmentez la profondeur seulement lorsqu’un déclencheur est nommé ; la recherche doit revenir dans le contenu, la structure, le geste ou la preuve. Pour une UI/UX nouvelle, ajoutez le contrat de réalité d’ACTION : tâche, contenu, états, responsive, accessibilité, robustesse et scope de preuve.

### Constitution et entrées par besoin

Les cinq absolus de `DIRECTION` protègent chaque run : leur résumé est dans la section « Constitution minimale » du README du package, leur formulation canonique dans [`DIRECTION.md`](DIRECTION.md#les-cinq-règles-absolues).

| Pour… | Faites d’abord… | Puis approfondissez avec… |
|---|---|---|
| Un agent à activer | Objectif, périmètre, autonomie, confirmation et format de sortie. | Skill pratique, `RUN_CARD` et références conditionnelles. |
| Une direction visuelle ouverte | Creative Boot : promesse, objet, geste, modal et parti, tension, signature, cibles CFT, fabrication et premier objet. | `DIRECTION/CHARGE` (mode `DIRECTION`). |
| Un run à persister | Scope, artefact, preuve, limite, owner et forme de clôture. | `ACTION/HANDOFF`, `ACTION/CLOSE-PACKAGE`, puis schéma `RUN_CARD` et validateur si projection structurée. |

## 2. La ligne de run

Avant de construire ou de modifier, répondez aux cinq questions du parcours commun.

Produisez ensuite la ligne minimale ; elle reprend la ligne du parcours commun avec un identifiant et l’état du run (`ACTION/STATUS`), l’owner restant nommé dans l’entrée minimale de `DIRECTION/START` :

```text
ID — MODE — DECISION — RISK — NEXT-PROOF — STATE
```

Ajoutez `DECISION-INTENT` au lancement. Ne produisez `DECISION-CHANGE` qu’après une observation ayant réellement confirmé, modifié ou abandonné une décision. Ne prétendez jamais avoir construit, observé ou vérifié ce qui n’était pas disponible. Une capacité manquante limite le claim correspondant ; elle ne réduit pas silencieusement le niveau de protection.

Si le package V1 ou une source canonique est indisponible, signalez-le. Une proposition créative peut rester explicitement hypothétique, mais elle ne doit pas être présentée comme un run V1 conforme.

## 3. Le parcours complet

Le parcours complet est le suivant ; chaque mode n’en garde que les étapes de sa route (`ACTION/RUN-<MODE>`) :

> **Classer → diriger → construire → observer → corriger, résoudre, rouvrir ou décider → persister.**

Il comporte deux boucles liées :

| Boucle | Fonction | Sortie attendue |
|---|---|---|
| **Boucle 1 — création** | Comprendre le produit et le public, classer le risque, formuler une direction située, choisir une structure, composer et construire un premier objet complet. | Un artefact réel, dirigé, spécifique, crédible et suffisamment résolu pour être observé. |
| **Boucle 2 — amélioration** | Observer dans le scope déclaré, interpréter avec une limite, isoler le défaut dominant, modifier réellement, réobserver et décider de la suite. | Correction visible, direction rouverte, réserve explicite, décision ou prochaine preuve persistée. |

Après observation, choisissez la suite selon la table de diagnostic de `DIRECTION/DOUBLE-LOOP` (boucle d’édition).

Une rationale seule ne constitue pas une correction. Lorsque la perception, l’usage, l’accessibilité ou la robustesse font partie de la décision, la boucle doit normalement conduire à une modification réelle de l’artefact, puis à une nouvelle observation. Si l’observation invalide l’hypothèse, le JTBD ou la cible, consignez dans la trace existante l’observation, son impact sur l’hypothèse, la décision touchée, le recadrage et la prochaine preuve ; cette note ne crée ni statut, ni gate, ni troisième boucle.

### Charger une route et renforcer une RUN_CARD

Pour charger seulement un bloc documenté, utilisez le lecteur de route :

```bash
python3 scripts/read_route.py DIRECTION/START
python3 scripts/read_route.py ACTION/RUN-LITE
python3 scripts/read_route.py --trouver "cohérence de rayon"
```

`--trouver` cherche le terme en mots entiers dans les cinq sources normatives, en ignorant la casse et les accents, avec quelques synonymes et traductions courants ; à défaut, une correspondance partielle, puis tous les mots sur une même ligne. Il regroupe les passages par route, classe les routes et montre les premières (`--tout` pour toutes). Il ne comprend pas le sens : sans résultat, essayer une reformulation ciblée ; l’absence d’occurrence ne prouve pas l’absence du savoir. `--sommaire` liste les routes avec leur rôle ; `--sommaire LOCATOR` donne la table des matières d’une route et ses sous-locators. À la lecture d’une route, les blocs déjà compilés dans le noyau de la skill sont remplacés par un renvoi à leur section ; `--complet` les affiche, et `--trouver` marque ces passages « (noyau) ». L’activation pour l’agent appartient à `DIRECTION/CHARGE` et figure dans le noyau compilé. `--guides`, utilisable avec `--trouver`, ajoute les documents d’orientation (guides du corpus, README racine et références de la skill), explicitement séparés des résultats normatifs. Les marqueurs de compilation et de concept ne sont pas des passages de lecture.

Le lecteur résout le locator selon `READING_MAP.md` (raccourci, titre propriétaire, puis sous-locator) et n’affiche que le bloc demandé. Pour une carte concrète, le mode strict rejette les placeholders et vérifie l’existence des locators locaux : artefact, trace et captures avant/après de la paire B1b. Remplacez les chemins d’exemple ci-dessous par ceux de vos fichiers :

```bash
python3 scripts/validate_run_card.py --strict chemin/vers/run_card.json
python3 scripts/validate_contracts.py --type production_contracts chemin/vers/contrat.json
```

Le mode strict complète la validation structurelle ; il ne transforme pas une preuve documentaire en preuve d’usage. Pour les locators HTTP(S) d’artefact, de trace et de captures, il refuse les familles `example.com`, `example.org`, `example.net` et `.invalid`, y compris leurs sous-domaines, après normalisation de casse et du point final. Une URL admise n’est pas vérifiée sur le réseau. Pour une préparation interrompue, voir la procédure de diagnostic et de reprise dans le README du paquet.

## 4. Choisir le mode sans le deviner

Évaluez les situations dans l’ordre canonique :

1. **`SYSTÈME`** — une règle, un token, un composant, une convention ou une dépendance partagée change pour plusieurs consommateurs ;
2. **`DIRECTION`** — l’identité, le premier contact, le rebrand ou la position visuelle autonome est la décision ;
3. **`ITER`** — une direction existante est retrouvable ; la retouche demande de la rappeler et réévaluer dans son périmètre, au-delà d’un fix local qui la conserve ;
4. **`LITE`** — un delta local, peu risqué, dans une structure connue ;
5. **`STANDARD`** — une page ou un flow nouveau sans charge identitaire autonome ni blast radius partagé.

| Situation | Mode probable |
|---|---|
| Fix ou delta local qui conserve la direction déjà tranchée | `LITE` |
| Retouche qui demande de rappeler et réévaluer une direction retrouvable dans son périmètre | `ITER` |
| Nouvelle page ou nouveau flow sans identité autonome ; craft exigeant : Gate C ciblé, pas un critère de mode | `STANDARD` |
| Brief flou ou risque impossible à classer | Clarification ou `EXTERNAL-START` avant le mode |
| Identité, premier contact ou direction visuelle autonome | `DIRECTION` |
| Token, composant, pattern, convention ou format partagé | `SYSTÈME` |

Première lecture de chaque mode : `DIRECTION/CHARGE`.

Classement : voir `DIRECTION/START`.

Le mode est une hypothèse de routage, jamais un moyen de réduire la protection. Avant de conserver `LITE` ou `ITER`, vérifiez qu’aucun consumer partagé, geste critique, état, donnée, permission, sécurité, confidentialité ou preuve critique n’est touché. Si le périmètre ou le risque augmente, reclassifiez.

## 5. Charger seulement ce qui peut changer la décision

La liste de chargement par mode est unique : `DIRECTION/CHARGE`. La skill en porte une copie générée.

« Non chargé par défaut » signifie qu’un module n’est pas lu sans raison ; ce n’est jamais une interdiction d’activer une source nécessaire. La charge documentaire ne diminue ni le mode, ni le niveau de preuve, ni la protection d’un risque.

## 6. Produire une qualité positive dès le premier rendu

Cette section projette le contrat positif du premier objet (voir `DIRECTION/FIRST-OBJECT`), dans le même ordre et sous les mêmes noms : elle impose un niveau d’intention et de résolution, jamais un style, une palette, un score ou un verdict esthétique.

Lorsque la décision visuelle est ouverte, le premier rendu n’est pas un échafaudage volontairement générique. Il doit rendre jugeables, dans la mesure du scope disponible :

| Dimension | Ce que le premier rendu doit rendre visible | Retour si… |
|---|---|---|
| Présence | Une position perceptible plutôt qu’un assemblage de composants neutres. | La proposition est plate, interchangeable ou sans foyer. |
| Foyer | Masse, rythme, hiérarchie et point d’entrée discernables. | Le texte, l’asset, le CTA et la preuve se concurrencent. |
| Signature | Un détail ou une relation non interchangeable, avec une raison située. | Le produit pourrait être remplacé sans modifier la scène. |
| Intégration | Une scène, un geste ou une relation qui rend la promesse tangible dès l’entrée ; la direction appartient à ce produit, ce public et ce contenu ; aucun effet, asset ou composant n’existe sans conséquence identifiable. | L’élément est décoratif, mal cadré, hors récit ou simplement disponible. |
| Résolution | Typographie, matière, action, responsive et états critiques assez construits pour révéler les défauts réels ; contenu suffisamment crédible pour juger la composition. | Le rendu reporte la décision à une future passe de polish. |
| Désirabilité située | L’attrait vient d’une relation au produit, au contexte et au public, pas d’un adjectif. | « Premium », « moderne » ou « beau » remplace une décision observable. |
| Vérité de scène | Texte, données, états et libellés crédibles ; tout exemple non observé est marqué comme illustratif. | Une hypothèse ressemble à une preuve de résultat, de client ou de disponibilité. |
| Résilience visible | La direction tient dans les transformations pertinentes pour le risque : mobile, contenu long, état critique ou fallback. | Un changement de contenu, viewport, asset ou état détruit le foyer ou la compréhension. |

Un « Retour si… » observé renvoie à la décision responsable (`DIRECTION/FIRST-OBJECT`) ; il ne crée ni gate, ni verdict, ni quota.

Cette barre ne constitue ni un score, ni un verdict, ni un style obligatoire. Un rendu peut être dense, joyeux, vernaculaire, maximaliste, étrange, populaire ou minimaliste si cette expression sert le contexte, le public et la décision. `SAVOIR/CRAFT` aide à juger ; `ACTION` possède la preuve et la clôture.

## 7. One-shot : compression, jamais dispense

Un run peut être traité en one-shot lorsque le périmètre est stable, que la direction est suffisamment déterminée, que les capacités critiques sont disponibles, que le premier objet peut être observé dans son scope et qu’aucun risque critique ne reste non protégé.

Le one-shot réduit le nombre de cycles ; il ne supprime pas :

1. la classification et la déclaration du risque ;
2. la construction d’un artefact réel ;
3. l’observation du premier rendu ou comportement ;
4. la revue créative lorsque la décision est visuelle ;
5. la vérification du risque dominant ;
6. la trace des preuves, limites et décisions, à son niveau (légère par défaut, complète si le run est persistant, partagé ou audité).

En trace légère, la sortie one-shot est la proposition. En trace complète, la sortie one-shot peut être une décision directement clôturée si l’observation confirme que le défaut dominant est absent ou corrigé et qu’aucune nouvelle itération ne promet un changement visible ou utile. Sinon, le run retourne à la branche appropriée : correction, réouverture, reclassification ou prochaine preuve.

## 8. Handoff agentique

Pour qu’un agent exécute V1, fournissez :

```text
OBJECTIVE — résultat recherché.
SCOPE — surface, état, public, médium et version.
AUTONOMY — actions autorisées sans confirmation.
CONFIRMATION — actions qui exigent un accord préalable.
CONSTRAINTS — contraintes de produit, technique, contenu, droits et délai.
OUTPUT — artefact, trace, preuve, limite et prochaine action attendus.
```

L’agent localise le package réellement fourni, lit le noyau de la skill, classe la demande avec `DIRECTION/START`, charge la ligne de son mode dans `DIRECTION/CHARGE` et seulement les propriétaires utiles, produit l’artefact, vérifie le risque dominant et restitue par défaut la réponse visible en langage produit : ce qui a été fait, pourquoi, ce qui manque pour la vraie version, la suite (voir `ACTION/HANDOFF`), avec la trace légère par défaut.

Il demande confirmation avant toute action externe, irréversible, publique, destructive, financière ou persistante hors du périmètre autorisé. Il ne choisit pas un mode plus léger parce qu’une capacité manque. Il déclare la capacité indisponible, requalifie la protection nécessaire ou conserve explicitement la limite.

## 9. Exemple complet minimal

Exemple d’une nouvelle page d’accueil dont la direction visuelle est ouverte :

```text
ID: home-042
MODE: DIRECTION
DECISION: rendre la promesse principale mémorable sans ralentir la compréhension
RISK: identity + usage
SCOPE: desktop 1440, mobile 390, état initial, contenu réel de la page d’accueil
NEXT-PROOF: capture des deux viewports + revue créative + test de compréhension ciblé
OWNER: design-lead
STATE: CHECKING

DECISION-INTENT:
La page doit donner une présence éditoriale forte tout en faisant comprendre
le bénéfice principal avant le premier geste.

DIRECTION:
Thèse : la preuve du produit porte la première scène ; la promesse se lit
avant le premier geste.
Modal : titre centré, sous-titre, deux boutons, trois cartes de bénéfices.
Parti : s’écarter pour la première scène seulement, où la preuve remplace le titre ;
garder la structure attendue pour le reste de la page.
First object : titre, objet visuel propriétaire et CTA principal dans la première scène.

ARTIFACT:
Page construite avec contenu crédible, objet visuel authored, responsive et état focus.

OBSERVATION:
La présence et la signature sont visibles. Sur mobile, le CTA secondaire concurrence
le premier geste et l’objet visuel perd sa relation avec le titre.

DOMINANT-DEFECT:
La hiérarchie mobile sépare l’objet de la promesse et dilue le premier geste.

CORRECTION:
Rapprocher l’objet et le titre, réduire la saillance du CTA secondaire et réviser le crop.

DECISION-CHANGE:
ABANDONED — la composition mobile du premier rendu est abandonnée : l’objet s’y sépare de la promesse et le CTA secondaire concurrence le premier geste (observation : capture mobile 390). La recomposition est décrite dans `CORRECTION` et reste à réobserver.

LIMIT:
Aucun test de lecteur d’écran ni test de performance exécuté dans ce run.

NEXT-ACTION:
Réobserver le mobile puis exécuter la preuve d’accessibilité appropriée avant clôture.
```

Pour une `RUN_CARD` persistante, cet exemple doit être sérialisé selon le schéma réel. En mode `DIRECTION`, documentez notamment les `sources`, l’objet `direction`, les `anchors`, l’`artifact`, le `trace_locator`, la `proof`, la `next_proof`, le `capability_profile` et la `closure`. Pour une `DIRECTION` décidée ou clôturée, la `closure` porte aussi `direction_status` ; pour une `DIRECTION` clôturée, `creative_close` est obligatoire avec ses cinq champs, même si la revue créative reste réservée ou signale une limite. La projection machine transporte le contrat ; elle ne constitue pas une preuve par elle-même. Une validation JSON, CLI ou package confirme la structure contrôlée, mais ne prouve ni l’implémentation runtime, ni l’usage, ni l’accessibilité exécutée, ni la performance, ni la qualité visuelle.

## 10. Observer, interpréter et améliorer

Inspectez l’artefact ou le comportement réel dans le scope déclaré. Une méthode de preuve doit toujours pouvoir répondre à quatre questions :

| Question | Réponse attendue |
|---|---|
| Qu’a-t-on réellement observé ? | Artefact, état, viewport, tâche, participant, mesure, version et date. |
| Que peut-on en déduire ? | Interprétation limitée au scope et à la méthode. |
| Que ne peut-on pas en déduire ? | Limite explicite : usage, accessibilité, robustesse, droits, préférence ou performance. |
| Quelle décision change maintenant ? | Correction, résolution, réouverture, reclassification, réserve ou clôture. |

Une capture prouve un rendu dans son scope ; elle ne prouve pas à elle seule une tâche utilisateur, un lecteur d’écran, une sécurité, une performance ou une intégration réelle. Une mesure d’accessibilité bornée ne certifie pas toute l’expérience. Une revue experte de craft ne remplace pas un test d’usage.

Pour une décision créative, appliquez les six questions de revue de `DIRECTION/DOUBLE-LOOP` (boucle d’édition).

Le polish est la résolution cohérente de la structure, du contenu, de la typographie, de la matière, de l’action et des états. Ce n’est pas une couche automatique de gradients, d’ombres, de flou ou de gros rayons.

## 11. Persister et fermer honnêtement

Pour un run persistant, suivez `ACTION/HANDOFF` et conservez un `TRACE-LOCATOR` : la forme courte LITE sans RUN_CARD est admise selon `ACTION/CLOSE-PACKAGE` ; les autres projections structurées utilisent la RUN_CARD et son validateur. Les projections machine-readable transportent les contrats existants ; elles ne remplacent ni les sources normatives, ni l’observation, ni le jugement humain.

Avant de fermer, vérifiez que :

1. le défaut dominant est corrigé, absent ou explicitement réservé ;
2. la preuve attendue est obtenue ou déclarée `NOT-VERIFIED` ; une conséquence attendue non observée est `NOT-OBSERVED` ; `N/A-JUSTIFIED`, avec sa raison, ne vaut que si la preuve ne s’applique pas ;
3. une correction technique ou de conformité n’a pas effacé la direction spécifique ;
4. la trace, les artefacts, les limites et l’owner sont retrouvables ;
5. une nouvelle itération ne promet plus de changement visible ou utile, ou bien la prochaine action est nommée.

`STATE: CLOSED` signifie que la trace et les artefacts sont persistés. Cela ne signifie pas que le run a réussi, que l’usage est validé ou que toutes les limites ont disparu. Un run peut être fermé sans acceptation ; les conditions dépendent de l’issue (voir `ACTION/CLOSE-PACKAGE` et `ACTION/OVERRIDE`) : archive simple pour `BLOCKED`, `RETURNED` ou `EXPLORATORY` (owner, limite et prochaine preuve) ; structure de réserve pour une acceptation avec réserve ; exception pour `FAIL-ASSUMED` (voir `ACTION/OVERRIDE`). Archiver un blocage n’exige aucune approbation.

Si une étape, une variante, une référence ou un tag ne change aucune décision, observation, preuve, limite ou prochaine action, retirez-le ou justifiez `N/A-JUSTIFIED`. Une trace complète sans conséquence est du slop procédural.

## 12. Sources propriétaires

| Besoin | Source |
|---|---|
| Classification, absolus et direction | [`DIRECTION.md`](./DIRECTION.md) |
| Trace, preuve, gates, verdict et clôture | [`ACTION.md`](./ACTION.md) |
| Craft, contenu, contexte, sources et intégrité | [`SAVOIR.md`](./SAVOIR.md) |
| Support, grille, scène, objet et composants | [`BIBLIOTHEQUE.md`](./BIBLIOTHEQUE.md) |
| État officiel du package et changements partagés | [`CHANGELOG.md`](./CHANGELOG.md) |

Lisez une source détaillée uniquement si elle peut modifier une décision, un artefact, une preuve, une limite ou la prochaine action. Pour les exemples, le flux et la projection machine, consultez les références de la skill pratique lorsque le parcours le justifie : `skills/design-governance-practice/references/examples.md`, `skills/design-governance-practice/references/flow.md` et `skills/design-governance-practice/references/machine_projection.md`.
