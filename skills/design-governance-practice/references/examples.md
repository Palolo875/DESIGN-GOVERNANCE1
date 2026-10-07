# Exemples de runs

> Ces exemples sont des aides non canoniques. Reprendre la séquence, pas le style, les valeurs, les composants ou les décisions visuelles. Les cas sont `ILLUSTRATIVE` et `SIMULATED` sauf mention contraire. Les champs affichés varient volontairement selon le mode : une omission dans une condensation n’est pas une suppression de la règle correspondante et ces blocs ne constituent pas un formulaire universel de `RUN_CARD`. Les champs affichés respectent les contrats d’ACTION ; un champ omis reste dû dans la `RUN_CARD`.
>
> **Trace, pas sérialisation.** Ces blocs sont des traces : leurs noms (`OBSERVED`, `AXES`, `RISK` en phrase…) ne sont pas des clés JSON. Pour produire une `RUN_CARD`, partir de `schemas/run_card.example.json`, suivre [machine_projection.md](machine_projection.md) et la table de correspondance d’`ACTION/RUN_CARD`, puis contrôler avec `scripts/validate_run_card.py`.
>
> **Niveau de trace.** Les exemples qui se terminent par `CLOSED` montrent une trace complète (clôture demandée ou run persistant) ; « fabrication depuis un brief flou » montre la sortie par défaut : une proposition, sa réponse visible et sa trace légère, sans clôture.

## LITE — correctif local

**Demande :** améliorer le contraste du bouton secondaire sans modifier la structure.

**Chemin :** classer `LITE` (fix local qui conserve la direction déjà tranchée, selon `DIRECTION/START`) → déclarer `DECISION-INTENT` → modifier → vérifier le ratio et l’état focus → clôturer avec la limite. Une retouche qui demande de rappeler et réévaluer la direction retrouvable relève de `ITER`. La clôture courte ci-dessous suit `ACTION/HANDOFF` et `ACTION/CLOSE-PACKAGE` ; elle est une trace complète sans RUN_CARD, avec artefact retrouvé et conditions de reprise applicables.

```text
MODE: LITE
DECISION-INTENT: améliorer la lisibilité sans élargir le scope
RISK: libellé secondaire illisible en contraste faible
ARTIFACT: diff et snapshot avant/après
OBSERVED: ratio 3,1:1 → 5,2:1 ; focus visible ; structure et interaction conservées
LIMIT: autres thèmes hors scope
AXES: V PASS · A PASS (contraste, focus) · U N/A-JUSTIFIED · T N/A-JUSTIFIED
DECISION-CHANGE: CONFIRMED — garder la hiérarchie du bouton secondaire et ne corriger que sa couleur (observation : snapshot avant/après, ratio mesuré)
VERDICT: ACCEPTED
STATE: CLOSED
```

Ne pas charger l’atlas ou une analyse de style si aucune responsabilité de design ne change.

## DIRECTION — fabrication depuis un brief flou

**Demande :** « Il me faut un site pour mon atelier de réparation de vélos. » Rien d’autre.

Les crochets marquent ce que chaque run tire de son propre brief : l’exemple ne fournit volontairement ni thèse ni objet de preuve, pour qu’ils ne soient pas recopiés.

**Prise de brief, dans le même tour :** la destination est une vraie mise en ligne. L’agent n’attend pas de réponse pour construire : il nomme ses hypothèses, marque les contenus d’exemple et place ses trois demandes dans la proposition (contenus réels : services, tarifs, horaires, adresse, numéro ; logo ou couleurs s’ils existent ; deux ou trois photos de l’atelier).

**Réponse visible :** « J’ai construit une page d’accueil organisée autour de [l’objet de preuve, nommé avec ce qu’il montre]. Pourquoi : [ce qu’un client veut savoir avant de venir, et comment l’objet y répond] ; j’ai écarté la grande photo d’entrée suivie de trois cartes de services, que n’importe quel atelier aurait. Ce qui manque pour la vraie version : vos tarifs, vos horaires et votre numéro, votre logo ou vos couleurs s’ils existent, et deux ou trois photos de l’atelier ; les contenus affichés sont des exemples marqués comme tels, et le bouton « Appeler l’atelier » fonctionne avec un numéro d’exemple. La suite : envoyez ces éléments, je les intègre et je vérifie le mobile. »

**Trace (trace légère, écrite à côté de l’artefact) :**

```text
MODE: DIRECTION
THÈSE: [ce que le client veut savoir] → [objet de preuve, composant codé, contenus marqués « exemple »] → [ce que l’objet remplace dans la trame attendue]
MODAL, TRAME ET PARTI: photo pleine largeur, titre centré, trois cartes « nos services » ; trame héros → services → avis → contact, rompue : l’objet de preuve ouvre la page ; s’écarter pour la première scène seulement, garder la navigation et le contact attendus
PLAFOND ET CONTENUS MARQUÉS: typographie et couleur au plafond (polices libres, palette choisie pour la thèse) ; pas encore de photos : route SANS-ASSET assumée, l’objet codé porte la scène, aucune fausse photo ; tarifs, horaires et numéro marqués « exemple »
DÉFAUT DOMINANT RESTANT: aucun bloquant ; [défaut vu sur la capture mobile], corrigé, seconde capture comparée
PROCHAINE PREUVE: vrais tarifs, horaires et numéro intégrés, puis capture mobile
```

## DIRECTION — première scène identitaire

**Demande :** créer une hero mémorable pour un service de cartographie sonore, sans page SaaS générique.

**Décisions :** thèse située, premier objet sonore, composition asymétrique, matière utile, composant authored, modal et parti. L’artefact doit être ouvrable et les données fictives marquées.

```text
MODE: DIRECTION
DECISION-INTENT: choisir une direction située pour le premier geste de découverte
THESIS: la ville se découvre par couches d’écoute
FIRST-OBJECT: topographie sonore interactive
MODAL: carte plate à pins, titre centré, cartes de fonctionnalités
PARTI: s’écarter de la carte à pins ; l’écoute par couches porte la scène
ARTIFACT: hero construite avec objet, contenu et geste
OBSERVED: hiérarchie, matière et premier geste dans le viewport inspecté
NOT-VERIFIED: préférence, utilisabilité générale, accessibilité exécutée
AXES: V PASS · U NOT-VERIFIED · A NOT-VERIFIED · T PASS
DECISION-CHANGE: CHANGED — la topographie sonore remplace la carte à pins comme premier objet (observation : paire v1/v1b, le premier geste est lu en premier dans le viewport inspecté)
CREATIVE-REVIEW: présence portée par la topographie sonore ; signature spécifique dans la relation entre ville, couche et écoute ; résolution à renforcer dans les états secondaires ; prochaine action : polir la transition entre découverte et premier geste
VERDICT: ACCEPTED-WITH-RESERVATION
RESERVATION: accessibilité exécutée non vérifiée — owner : lead design ; scope : hero ; impact : parcours clavier de la topographie inconnu ; prochaine preuve : parcours clavier et lecteur d’écran ; revue : 2026-10-09 ; condition de sortie : parcours clavier observé sans blocage
DIRECTION-STATUS: HELD
STATE: CLOSED
```

Une belle capture ne prouve pas l’usage. Une rationale ne prouve pas l’implémentation.

Lecture visuelle illustrative — annotation narrative, non-champ `RUN_CARD` : la direction artistique est visible dans la matière et le premier objet ; le craft est observé dans la hiérarchie et la composition du viewport ; la revue créative rend explicites la présence, la signature et le défaut dominant ; le polish des états secondaires et l’usage général restent non vérifiés. `CREATIVE-REVIEW` est ici un libellé narratif illustratif ; dans la projection machine, cette observation est transportée par `creative_close`. Ce contenu ne constitue pas un nouveau statut ni un verdict esthétique.

## DIRECTION + STYLE — profil d’expression situé

**Demande :** donner une présence culturelle à une archive numérique sans transformer l’interface en nostalgie décorative.

**Choix :** tester `STYLE/DIGITAL_MEMORY` comme hypothèse d’expression. Le profil modifie la matière, le rythme et le traitement des fragments ; il ne choisit ni la structure de l’archive ni le verdict.

```text
MODE: DIRECTION
PROFILE: STYLE/DIGITAL_MEMORY
PROFILE-DECISION: transformer la mémoire d’écran en repère de collection
PROFILE-PHASE: observed
DIALS: densité haute dans l’archive, motion basse dans la navigation, variance modérée dans les pièces
COUNTERINDICATION: lecture critique, contraste faible, nostalgie sans relation au contenu
ARTIFACT: scène d’archive avec fragments, métadonnées et états réels
EVIDENCE: paire de captures avec et sans traitement pixel/raster : les pièces se distinguent des contrôles et les métadonnées restent lisibles (claim visuel seulement)
PROOF-LIMIT: mémorisation et tâche NOT-VERIFIED (elles exigeraient un protocole utilisateur : participants, tâche, mesure) ; droits des fragments externes non validés
DECISION-CHANGE: CHANGED — le traitement numérique est limité aux pièces et retiré des contrôles critiques (observation : paire de captures)
```

Le profil peut être refusé si la paire ne change aucune décision ou si la matière nuit à la lisibilité. `PROFILE-DECISION` ne devient ni un score, ni un verdict esthétique, ni une autorisation d’imiter une référence.

## SYSTÈME — composant partagé

**Demande :** ajouter au Select un libellé long, une aide et un état d’erreur sans casser les écrans existants.

**Chemin :** classer `SYSTÈME` → inventorier les dépendances → modifier la primitive et ses états → inspecter des consommateurs représentatifs → corriger ou restaurer.

```text
MODE: SYSTÈME
DECISION-INTENT: étendre le Select sans rompre clavier, focus ou compatibilité
RISK: blast radius partagé
ARTIFACT: composant, états, captures et consommateurs représentatifs
OBSERVED: libellé long, erreur, focus et clavier dans trois consommateurs ; troncature observée sur mobile dans le consommateur 2
NOT-VERIFIED: autres écrans, plateformes et thèmes
DECISION-CHANGE: ABANDONED — l’extension du Select en l’état est abandonnée : la troncature mobile casse ce consommateur ; une version corrigée reprend dans le même mode (observation : consommateur 2)
ISSUE: RETURNED
VERDICT: RETURN
STATE: CLOSED
```

Le blast radius appartient au scope du run ; il ne devient pas un score global.

