# Guide d’équipe — Design Governance V1.0.0

Pour qui pilote un travail de design avec un agent ou en équipe : opérateur, designer, responsable. Design Governance V1.0.0 est une expérimentation maintenue, pensée pour un usage supervisé ; elle ne prouve pas son efficacité en production.

> **Ce que fait ce guide :** il oriente la lecture et l’action, sans ajouter aucune règle. Ce sont les sections citées qui font foi.

> **Pour faire simplement une demande,** le [guide pour commencer](commencer.md#commencer) suffit : vous n’avez pas à choisir de mode.

Le but : transformer une demande en **décision adaptée au projet, rendu réel, observation utile et trace honnête**. Le système ne promet ni beauté automatique, ni réussite universelle, ni usage validé sans preuve adaptée. Il vise pourtant haut : quand la décision visuelle est ouverte et que les moyens sont là, le premier rendu doit déjà être composé, spécifique, crédible, présentable et assez abouti pour être jugé comme un vrai objet.

Dans ce guide, un **run** est un travail délimité : une décision, un risque, un rendu, une preuve. Les adresses entre accents graves (`agent/chemins#classer`) se lisent avec `python3 scripts/read_route.py ADRESSE`.

## Parcours commun

Pour piloter un run, commencez ici ; la suite ne sert que si le risque, le périmètre ou la décision le demande. Une fois la demande classée avec `agent/chemins#classer` (par l’opérateur ou l’agent, jamais par la personne qui demande), notez :

```text
MODE — DECISION — RISK — NEXT-PROOF — OWNER
```

Soit : le chemin choisi, la décision, le risque, la prochaine preuve, le responsable. Répondez ensuite à ces cinq questions :

| Question | Réponse minimale |
|---|---|
| Quelle décision doit changer ? | Le choix concret à trancher, confirmer ou abandonner. |
| Quel risque domine ? | Identité, usage, accessibilité, technique, système ou autre risque déclaré. |
| Quelle preuve peut départager les options ? | Mesure, capture, test, comparaison, inspection ou observation adaptée. |
| Qu’a-t-on réellement à disposition ? | Rendu, navigateur, code de la page, contraste, clavier et technologies d’assistance, participants, environnement, données ou sources. |
| Qui porte la décision et la suite ? | Un responsable nommé, avec confirmation ou remontée si nécessaire. |

Écrivez la ligne de run, faites l’action la moins coûteuse qui peut changer la décision, puis choisissez une seule suite : **corriger**, **approfondir la preuve**, **rouvrir**, **reclasser**, **proposer** ou **fermer**. Par défaut, le run s’arrête à la proposition, en trace légère : la première proposition vaut checkpoint, sauf action irréversible ou coûteuse ; **fermer** suppose la trace complète (run persistant, partagé, audité ou acceptation demandée).

## Où trouver la suite

Si la demande est déjà claire, le [guide du designer](designer.md) indique quoi combiner, quels angles examiner et quand s’arrêter. Si le brief est vague, commencez par `agent/chemins#classer`.

Une sortie de run a deux formes : la **réponse visible**, par défaut, et la trace de reprise, pour un travail qui sera repris ou conservé (voir `agent/repondre`). Le niveau de trace ne dépend pas du mode : sans conservation, partage, audit ni acceptation demandée, la **trace légère** suffit (six lignes au plus, à côté du rendu ou sous « Trace » après la réponse) ; sinon, la **trace complète** s’impose. Écrivez `N/A-JUSTIFIED` (« sans objet, justifié ») quand un champ ou un angle ne s’applique pas.

## 1. Lire juste ce qu’il faut

Ne chargez pas tout le système par réflexe : seulement ce qui peut changer la prochaine décision.

### Ce que chaque partie apporte

La ligne du parcours commun sert de cadrage d’entrée. `agent/chemins#classer` classe la demande ; la direction (`design/direction/`) intervient si la cible ou la direction change ; la qualité du produit (`design/produit/`) et, pour un travail tracé, la gouvernance interviennent dès qu’un rendu, une preuve, un état ou une clôture est en jeu ; le savoir (`design/savoir/`) intervient si le jugement, le craft, les sources ou le contexte peuvent changer la décision ; les formes (`design/formes/`) interviennent si la structure, un composant ou une micro-interface peuvent la changer. Ce cadrage ne crée ni chemin, ni vérification, ni responsable de plus.

**Ce qu’on y gagne.** La direction donne une position adaptée au projet et un premier objet plus fort ; le savoir transforme une impression en jugement et en choix de craft ; les formes rendent la structure habitable, compatible et maintenable ; la qualité du produit et la gouvernance rendent la livraison observable, corrigible et prouvable. Si aucun de ces gains ne peut changer la prochaine décision, restez sur le chemin court ; si un risque critique est actif, ne confondez pas chemin court et profondeur insuffisante.

Pour une décision visuelle ouverte, faites le **lancement créatif** (Creative Boot, `direction/diriger#lancement`) avant le premier pixel : promesse, objet de preuve, geste, tension et signature de structure (nombre d’axes : `formes/choisir#tension`), jusqu’à trois qualités visées (`savoir/qualite-creative`), `MODAL`/`PARTI`, bilan des moyens (`FABRICATION`), premier objet et défaut dominant. C’est un cadrage, pas un formulaire de plus ni une obligation pour un changement local : il doit changer la construction, sinon on l’omet. Sur brief vague, la prise de brief (`direction/cadrer#demande-vague`) demande au plus trois éléments, en un seul échange, selon ce qui relève le plus le plafond : contenu réel, marque, asset principal ou route autorisée, destination si elle est incertaine ; ces demandes accompagnent la première proposition, construite dans le même tour avec des hypothèses nommées ; la réponse n’est attendue avant de construire que si la personne l’a demandé ou si l’action est irréversible ou coûteuse ; le rendu est construit dans tous les cas.

Si le domaine, le public, la confiance, la culture, les conventions ou l’ambition peuvent changer le résultat, cadrez le domaine (`direction/cadrer#domaine`), puis cherchez des sources utiles à la décision (`savoir/images-et-sources`). N’allez plus loin que si un déclencheur est nommé ; la recherche doit revenir dans le contenu, la structure, le geste ou la preuve. Pour une interface nouvelle, ajoutez le contrat d’interface réelle (`produit/interface`) : tâche, contenu, états, responsive, accessibilité, robustesse et périmètre de preuve.

### Règles et entrées selon le besoin

Les cinq règles essentielles protègent chaque run : leur résumé est dans la section « Les cinq règles essentielles » du README du package, leur formulation qui fait foi dans [`direction/standard`](../design/direction/standard.md#les-cinq-règles-absolues).

| Pour… | Faites d’abord… | Puis approfondissez avec… |
|---|---|---|
| Un agent à activer | Objectif, périmètre, autonomie, confirmation et format de sortie. | La skill, la fiche de travail (`RUN_CARD`) et les références utiles. |
| Une direction visuelle ouverte | Lancement créatif : promesse, objet, geste, modal et parti, tension, signature, qualités visées, moyens et premier objet. | `agent/chemins#quoi-lire` (mode `DIRECTION`). |
| Un run à conserver | Périmètre, rendu, preuve, limite, responsable et forme de clôture. | `agent/repondre`, `gouvernance/cloture`, puis le schéma `RUN_CARD` et son validateur si la trace doit être structurée. |

## 2. La ligne de run

Avant de construire ou de modifier, répondez aux cinq questions du parcours commun.

Écrivez ensuite la ligne minimale : celle du parcours commun, avec un identifiant et l’état du run (`gouvernance/statuts`) ; le responsable reste nommé dans l’entrée minimale de `agent/chemins#classer`.

```text
ID — MODE — DECISION — RISK — NEXT-PROOF — STATE
```

Ajoutez `DECISION-INTENT` (la décision visée) au lancement. N’écrivez `DECISION-CHANGE` qu’après une observation qui a réellement confirmé, modifié ou abandonné une décision. Ne prétendez jamais avoir construit, observé ou vérifié ce qui n’était pas disponible. Un moyen qui manque limite ce qu’on peut affirmer ; il ne baisse jamais en silence le niveau de protection.

Si le paquet ou une section qui fait foi est indisponible, dites-le. Une proposition créative peut rester explicitement hypothétique, mais elle ne doit pas être présentée comme un run conforme.

## 3. Le parcours complet

Le parcours complet est le suivant ; chaque mode n’en garde que les étapes de sa route (`agent/chemins#modes`) :

> **Classer → diriger → construire → observer → corriger, résoudre, rouvrir ou décider → conserver.**

Il comporte deux boucles liées :

| Boucle | Rôle | Ce qu’elle produit |
|---|---|---|
| **Boucle 1 — créer** | Comprendre le produit et le public, classer le risque, formuler une direction adaptée, choisir une structure, composer et construire un premier objet complet. | Un rendu réel, dirigé, spécifique, crédible et assez abouti pour être observé. |
| **Boucle 2 — améliorer** | Observer dans le périmètre déclaré, interpréter avec une limite, isoler le défaut dominant, modifier réellement, observer de nouveau et décider de la suite. | Une correction visible, une direction rouverte, une réserve explicite, une décision ou une prochaine preuve conservée. |

Après observation, choisissez la suite avec la table de diagnostic de la boucle d’édition (`direction/boucle`).

Une justification seule ne corrige rien. Quand la perception, l’usage, l’accessibilité ou la robustesse font partie de la décision, la boucle doit conduire à une vraie modification du rendu, puis à une nouvelle observation. Si l’observation invalide l’hypothèse, la tâche visée ou la cible, notez dans la trace existante l’observation, son effet sur l’hypothèse, la décision touchée, le recadrage et la prochaine preuve ; cette note ne crée ni statut, ni vérification, ni troisième boucle.

### Lire une section et vérifier une fiche de travail

Pour lire seulement une section, utilisez le lecteur :

```bash
python3 scripts/read_route.py agent/chemins#classer
python3 scripts/read_route.py agent/chemins#retouche
python3 scripts/read_route.py --trouver "cohérence de rayon"
```

`--trouver` cherche un terme en mots entiers (sans tenir compte de la casse ni des accents, avec quelques synonymes) et classe les sections qui en parlent ; `--tout` les montre toutes. Il ne comprend pas le sens : sans résultat, reformulez, car l’absence d’occurrence ne prouve pas l’absence du savoir. `--sommaire` liste les sections et leur rôle. Les passages déjà présents dans le noyau de la skill sont remplacés par un renvoi et marqués « (noyau) » ; `--complet` les affiche. `--guides` ajoute aux résultats les guides, le README et les références de la skill, séparés de ce qui fait foi.

Le mode strict du validateur rejette les champs laissés en gabarit et vérifie que les fichiers cités existent : rendu, trace et captures avant/après de la comparaison sur capture. Remplacez les chemins d’exemple par les vôtres :

```bash
python3 gouvernance/outils/validate_run_card.py --strict chemin/vers/run_card.json
python3 gouvernance/outils/validate_contracts.py --type production_contracts chemin/vers/contrat.json
```

Le mode strict ne transforme pas une preuve écrite en preuve d’usage ; il refuse les domaines d’exemple (`example.com`…) et ne vérifie pas les adresses sur le réseau. Pour reprendre une préparation interrompue, voir la [maintenance](../maintenance/README.md#reprendre-une-préparation-interrompue).

## 4. Choisir le mode sans le deviner

Examinez les situations dans cet ordre :

1. **`SYSTÈME`** (système de design) — une règle, un token, un composant, une convention ou une dépendance partagée change pour plusieurs utilisateurs ;
2. **`DIRECTION`** (direction ouverte) — l’identité, le premier contact, le changement d’image ou la position visuelle autonome est la décision ;
3. **`ITER`** (itération) — une direction existante est retrouvable ; la retouche demande de la rappeler et réévaluer dans son périmètre, au-delà d’un fix local qui la conserve ;
4. **`LITE`** (retouche) — un changement local, peu risqué, dans une structure connue ;
5. **`STANDARD`** (écran cadré) — une page ou un parcours nouveau, sans enjeu d’identité propre ni effet sur des éléments partagés.

| Situation | Mode probable |
|---|---|
| Correctif ou changement local qui garde la direction déjà tranchée | retouche (`LITE`) |
| Retouche qui demande de rappeler et réévaluer une direction retrouvable dans son périmètre | itération (`ITER`) |
| Nouvelle page ou nouveau parcours sans identité propre ; un craft exigeant se traite par une finition ciblée, pas par le mode | écran cadré (`STANDARD`) |
| Brief flou ou risque impossible à classer | Clarifier, ou partir d’une demande vague (`direction/cadrer#demande-vague`), avant le mode |
| Identité, premier contact ou direction visuelle autonome | direction ouverte (`DIRECTION`) |
| Token, composant, pattern, convention ou format partagé | système de design (`SYSTÈME`) |

Première lecture de chaque mode : `agent/chemins#quoi-lire`.

Classement : voir `agent/chemins#classer`.

Le mode est une hypothèse de travail, jamais un moyen de baisser la protection. Avant de garder une retouche ou une itération, vérifiez qu’aucun élément partagé, geste critique, état, donnée, permission, sécurité, confidentialité ou preuve critique n’est touché. Si le périmètre ou le risque grandit, reclassez.

## 5. Charger seulement ce qui peut changer la décision

La liste de lecture par mode est unique : `agent/chemins#quoi-lire`. La skill en porte une copie générée.

« Non chargé par défaut » veut dire qu’une section n’est pas lue sans raison ; jamais qu’il est interdit de lire une section nécessaire. Lire moins ne baisse ni le mode, ni le niveau de preuve, ni la protection d’un risque.

## 6. Produire une qualité positive dès le premier rendu

Cette table reprend, dans le même ordre et sous les mêmes noms, le contrat du premier objet (`direction/premier-objet`) : elle fixe un niveau d’intention et d’aboutissement, jamais un style, une palette, une note ou un verdict esthétique.

Quand la décision visuelle est ouverte, le premier rendu n’est pas un échafaudage volontairement générique. Il doit permettre de juger, autant que le périmètre le permet :

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

Un « Retour si… » observé renvoie à la décision responsable (`direction/premier-objet`) ; il ne crée ni vérification, ni verdict, ni quota.

Ce niveau n’est ni une note, ni un verdict, ni un style obligatoire. Un rendu peut être dense, joyeux, vernaculaire, maximaliste, étrange, populaire ou minimaliste si cette expression sert le contexte, le public et la décision. Le savoir (`savoir/qualite-creative`) aide à juger ; la preuve et la clôture relèvent de la qualité du produit et, pour un travail tracé, de la gouvernance.

## 7. En une seule passe : plus court, jamais dispensé

Un run peut se faire en une seule passe (one-shot) quand le périmètre est stable, que la direction est assez déterminée, que les moyens critiques sont disponibles, que le premier objet peut être observé dans son périmètre et qu’aucun risque critique ne reste sans protection.

Une seule passe réduit le nombre de cycles ; elle ne supprime pas :

1. le classement et la déclaration du risque ;
2. la construction d’un rendu réel ;
3. l’observation du premier rendu ou comportement ;
4. la revue créative quand la décision est visuelle ;
5. la vérification du risque dominant ;
6. la trace des preuves, des limites et des décisions, à son niveau (légère par défaut, complète si le run est persistant, partagé ou audité).

En trace légère, la sortie one-shot est la proposition. En trace complète, la sortie one-shot peut être une décision directement clôturée si l’observation confirme que le défaut dominant est absent ou corrigé, et qu’aucune nouvelle passe ne promet de changement visible ou utile. Sinon, le run repart vers la bonne suite : correction, réouverture, reclassement ou prochaine preuve.

## 8. Confier le travail à un agent

Pour qu’un agent travaille avec le système, donnez-lui :

```text
OBJECTIVE — résultat recherché.
SCOPE — surface, état, public, médium et version.
AUTONOMY — actions autorisées sans confirmation.
CONFIRMATION — actions qui exigent un accord préalable.
CONSTRAINTS — contraintes de produit, technique, contenu, droits et délai.
OUTPUT — artefact, trace, preuve, limite et prochaine action attendus.
```

L’agent localise le package réellement fourni, lit le noyau de la skill, classe la demande avec `agent/chemins#classer`, lit la ligne de son mode dans `agent/chemins#quoi-lire` et seulement les sections utiles, produit le rendu, vérifie le risque dominant et rend par défaut la réponse visible en langage produit : ce qui a été fait, pourquoi, ce qui manque pour la vraie version, et la suite (voir `agent/repondre`), avec la trace légère par défaut.

Il demande confirmation avant toute action externe, irréversible, publique, destructive, financière ou durable hors du périmètre autorisé. Il ne choisit pas un mode plus léger parce qu’un moyen manque : il le dit, ajuste la protection nécessaire ou garde explicitement la limite.

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

Pour une fiche de travail (`RUN_CARD`) conservée, cet exemple doit suivre le schéma réel (`gouvernance/schemas/`). En mode `DIRECTION`, renseignez notamment les `sources`, l’objet `direction`, les `anchors`, l’`artifact`, le `trace_locator`, la `proof`, la `next_proof`, le `capability_profile` et la `closure`. Pour une direction décidée ou clôturée, la `closure` porte aussi `direction_status` ; pour une direction clôturée, `creative_close` est obligatoire avec ses cinq champs, même si la revue créative reste réservée ou signale une limite. La fiche transporte le contrat ; elle n’est pas une preuve en elle-même. Une validation du fichier ou du paquet confirme la structure contrôlée, mais ne prouve ni le fonctionnement réel, ni l’usage, ni l’accessibilité, ni la performance, ni la qualité visuelle.

## 10. Observer, interpréter et améliorer

Regardez le rendu ou le comportement réel dans le périmètre déclaré. Toute méthode de preuve doit pouvoir répondre à quatre questions :

| Question | Réponse attendue |
|---|---|
| Qu’a-t-on réellement observé ? | Rendu, état, taille d’écran, tâche, participant, mesure, version et date. |
| Que peut-on en déduire ? | Une interprétation limitée au périmètre et à la méthode. |
| Que ne peut-on pas en déduire ? | La limite explicite : usage, accessibilité, robustesse, droits, préférence ou performance. |
| Quelle décision change maintenant ? | Correction, résolution, réouverture, reclassement, réserve ou clôture. |

Une capture prouve un rendu dans son périmètre ; à elle seule, elle ne prouve ni une tâche utilisateur, ni un lecteur d’écran, ni la sécurité, la performance ou une intégration réelle. Une mesure d’accessibilité limitée ne certifie pas toute l’expérience. Une revue experte du craft ne remplace pas un test d’usage.

Pour une décision créative, appliquez les six questions de revue de la boucle d’édition (`direction/boucle`).

Le polish est l’aboutissement cohérent de la structure, du contenu, de la typographie, de la matière, de l’action et des états. Ce n’est pas une couche automatique de dégradés, d’ombres, de flou ou de grands arrondis.

## 11. Conserver et fermer honnêtement

Pour un run conservé, suivez `agent/repondre` et gardez un emplacement de trace (`TRACE-LOCATOR`) : la forme courte LITE sans RUN_CARD est admise selon `gouvernance/cloture` ; les autres traces structurées utilisent la fiche de travail et son validateur. Ces fichiers transportent les contrats ; ils ne remplacent ni les sections qui font foi, ni l’observation, ni le jugement humain.

Avant de fermer, vérifiez que :

1. le défaut dominant est corrigé, absent ou explicitement réservé ;
2. la preuve attendue est obtenue ou déclarée `NOT-VERIFIED` ; une conséquence attendue non observée est `NOT-OBSERVED` ; `N/A-JUSTIFIED`, avec sa raison, ne vaut que si la preuve ne s’applique pas ;
3. une correction technique ou de conformité n’a pas effacé la direction spécifique ;
4. la trace, les rendus, les limites et le responsable sont retrouvables ;
5. une nouvelle passe ne promet plus de changement visible ou utile, ou bien la prochaine action est nommée.

`STATE: CLOSED` veut dire que la trace et les rendus sont conservés. Cela ne veut pas dire que le run a réussi, que l’usage est validé ou que toutes les limites ont disparu. Un run peut être fermé sans être accepté ; les conditions dépendent de l’issue (voir `gouvernance/cloture` et `gouvernance/verification#derogation`) : simple archive pour `BLOCKED`, `RETURNED` ou `EXPLORATORY` (responsable, limite et prochaine preuve) ; réserve structurée pour une acceptation avec réserve ; exception pour `FAIL-ASSUMED` (voir `gouvernance/verification#derogation`). Archiver un blocage n’exige aucune approbation.

Si une étape, une variante, une référence ou une étiquette ne change aucune décision, observation, preuve, limite ou prochaine action, retirez-la ou justifiez `N/A-JUSTIFIED`. Une trace complète sans conséquence est du slop procédural.

## 12. Où se trouvent les règles

| Besoin | Où lire |
|---|---|
| Classer et choisir quoi lire | [`agent/chemins.md`](../agent/chemins.md) |
| Direction, cinq règles essentielles | [`design/direction/`](../design/README.md) |
| Craft, contenu, contexte, sources | [`design/savoir/`](../design/savoir/README.md) |
| Structures, grilles, scènes, composants | [`design/formes/`](../design/formes/README.md) |
| Qualité du rendu, plancher, finition | [`design/produit/`](../design/produit/README.md) |
| Trace, statuts, vérification, clôture | [`gouvernance/`](../gouvernance/README.md) |
| Version et évolution du système | [`maintenance/`](../maintenance/README.md) |

Ne lisez une section détaillée que si elle peut changer une décision, un rendu, une preuve, une limite ou la prochaine action. Pour des exemples, le déroulé et le format des fiches, voir les références de la skill quand c’est utile : `agent/skill/references/examples.md`, `agent/skill/references/flow.md` et `agent/skill/references/machine_projection.md`.
