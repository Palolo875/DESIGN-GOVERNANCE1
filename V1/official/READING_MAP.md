# READING_MAP — carte dérivée de lecture et d’activation

**Statut :** guide dérivé non normatif. Les cinq sources normatives, le schéma `RUN_CARD` et les validateurs propriétaires font foi en cas de divergence.

## Utilisation

Cette carte réduit la recomposition mentale du lecteur. Elle ne crée ni mode, ni gate, ni axe, ni statut, ni verdict, ni owner de décision supplémentaire. Elle indique seulement où commencer, quoi charger, ce qui doit sortir et quand transmettre.

Pour composer plusieurs capacités selon un résultat recherché — direction, beauté située, créativité, usage, preuve, vitesse ou système — voir la section « Combinaisons par résultat recherché » ci-dessous : elle aide à ajuster la combinaison et l’intensité sans remplacer les propriétaires normatifs.

## Chemin canonique de démarrage

1. Localiser la version V1 réellement fournie.
2. Lire `QUICKSTART.md` ou cette carte si le besoin est déjà identifiable.
3. Ouvrir `DIRECTION/START` pour classer le mode et le risque dominant.
4. Charger la ligne du mode dans `DIRECTION/CHARGE`, puis approfondir seulement le propriétaire capable de modifier la prochaine décision.
5. Ouvrir `ACTION` dès qu’un artefact, une observation, une preuve, un état ou une clôture est concerné.
6. Persister la sortie selon `ACTION/HANDOFF` et `ACTION/CLOSE-PACKAGE` lorsque le run doit être repris, comparé ou fermé ; la forme courte LITE peut être complète sans RUN_CARD, la projection structurée suit `ACTION/RUN_CARD`.

`DIRECTION/START` reste la seule classification. Cette carte ne reclassifie pas.

## Constitution minimale

Les cinq absolus de `DIRECTION` protègent chaque run : résumé dans la section « Constitution minimale » du README du package, formulation canonique dans [`DIRECTION.md`](DIRECTION.md#les-cinq-règles-absolues).

## Routage minimal par décision

| Décision dominante | Première lecture | Ajouter seulement si nécessaire |
|---|---|---|
| Brief vague ou risque inconnu | `DIRECTION/START` | `DIRECTION/EXTERNAL-START` |
| Correction locale | `DIRECTION/START` → `ACTION/RUN-LITE` ou `RUN-ITER` | `SAVOIR` ou `BIBLIOTHEQUE` si la décision change |
| Nouvelle surface opérationnelle | `DIRECTION/START` → `ACTION/RUN-STANDARD` | `BIBLIOTHEQUE/SELECT`, `SAVOIR/CONTEXT` |
| Direction identitaire | `DIRECTION/START` → `DIRECTION/CHARGE` (mode `DIRECTION`) | `SAVOIR/CRAFT`, `DIRECTION/DIRECTION-ATELIER` |
| Structure ou composant partagé | `DIRECTION/START` → `ACTION/RUN-SYSTEM` | `BIBLIOTHEQUE/COMPONENTS`, `SAVOIR/SYSTEM`, `CHANGELOG` |
| Preuve, vérification ou clôture | `ACTION` | Gate et route correspondant au risque |
| Règle ou route durable | `CHANGELOG` et source propriétaire | `ACTION` pour preuve et `BIBLIOTHEQUE/EVOLUTION` si structure |

Sortie : réponse visible et trace légère par défaut ; handoff et clôture (`ACTION/CLOSE-PACKAGE`) en trace complète (`ACTION/HANDOFF`).

## Combinaisons par résultat recherché

Cette section aide à combiner plusieurs capacités lorsque chacune peut **modifier la même décision** ou **protéger un risque déclaré**. Elle ne crée ni mode, ni route, ni gate, ni statut, ni verdict, ni champ machine. Le mode est d’abord classé par `DIRECTION/START` ; la combinaison est ensuite choisie selon le résultat recherché et le scope réel.

> **Principe :** ne pas charger le maximum de routes ; composer le maximum de contribution pertinente. Toute capacité activée doit avoir une contribution nommable et être retirée si elle ne change ni la décision, ni l’artefact, ni la preuve, ni la limite, ni la prochaine action.

La combinaison choisie reste dans la trace existante du run, seulement si elle peut modifier la décision. Ne crée pas une trace par capacité et ne transforme pas une table d’orientation en preuve.

| Résultat recherché | Noyau possible | Renforcement seulement si nécessaire | Preuve à privilégier |
|---|---|---|---|
| **Direction forte et spécifique** | `DIRECTION/CHARGE` (mode `DIRECTION`) | `DIRECTION/CREATIVE-BOOT`, `DIRECTION/DOMAIN-FRAME`, `SAVOIR/CRAFT`, `SAVOIR/SOURCE`, `SAVOIR/STYLE`, `BIBLIOTHEQUE/SELECT` | Premier objet réel, revue créative, observation du défaut dominant et correction réellement observée. |
| **Beauté, goût et craft situés** | `DIRECTION/FIRST-OBJECT` + `SAVOIR/CRAFT` + `ACTION/FIRST-RENDER` | Traduction de `BIBLIOTHEQUE/SELECT` si l’intention reste sans levier ; calibration de `BIBLIOTHEQUE/CONTRACTS` si la fabrication reste ouverte ; gestes conditionnels de `SAVOIR/STATE` (dans le noyau), puis `SAVOIR/STYLE`, contenu, matière, typographie ou ancre seulement selon la décision, par `DIRECTION/CHARGE` | Relation et effet attendu nommés avant build ; effet réinspecté dans le même scope ; jugement créatif séparé des preuves d’usage, d’accessibilité et de robustesse. |
| **Créativité variée mais utile** | `DIRECTION/CREATIVE-BOOT` + `DIRECTION/VISUAL_TARGET` + une alternative située | `DIRECTION/DOMAIN-FRAME`, `SAVOIR/SOURCE` ou atelier seulement si l’axe de divergence change une décision | Comparaison dans le même scope par public, JTBD, promesse, geste, structure ou expression. |
| **UI/UX habitable** | `ACTION/UI-UX-REALITY` + `BIBLIOTHEQUE/SELECT` + `ACTION/GATE-A` (contrôles applicables) + contenu et états réels | Responsive, focus, récupération, runtime ou `SAVOIR/CONTEXT` selon le risque | Tâche, états, viewports, contenu extrême, clavier ou méthode adaptée au claim. |
| **Preuve et décision fiables** | `ACTION/STRUCTURED-PROOF` + artefact réel + gate correspondant au risque + `ACTION/CLOSE-EXIT-CHECK` | Preuve croisée ou `RUN_CARD` stricte si la persistance l’exige | Claim, méthode, scope, date, artefact, limite et `TRACE-LOCATOR` retrouvables. |
| **Vitesse sans appauvrissement** | `DIRECTION/START` + `ACTION/FAST-PATH` + `LITE` ou `ITER` correctement classé | Ajouter une seule capacité si elle peut changer la décision ; reclassifier si le risque ou le périmètre augmente | Artefact réel, observation ciblée, preuve minimale applicable et prochaine action. |
| **Système maintenable** | `ACTION/RUN-SYSTEM` + `BIBLIOTHEQUE/COMPONENTS` si un composant change + migration, rollback et `CHANGELOG` (paquet SYSTÈME) | `BIBLIOTHEQUE/EVOLUTION` ou `SAVOIR/SYSTEM` selon la décision partagée | Consumers, compatibilité, non-régression, owner, migration et condition de reprise. |
| **Domaine sensible ou incertain** | `DIRECTION/DOMAIN-FRAME` + `SAVOIR/SOURCE` + `ACTION/STRUCTURED-PROOF` | Contexte culturel, conventions, confiance ou recherche seulement si un déclencheur peut changer la décision | Source ou observation reliée à la décision, transformation, rejet et limite. |
| **Agent contrôlé** | `DIRECTION/START` + `ACTION/AUTHORITY` + `SKILL.md` + owner | Cette carte seulement si plusieurs capacités sont réellement nécessaires ; `RUN_CARD` en trace complète (run persistant, partagé, audité ou acceptation demandée), quel que soit le nombre de capacités ; exception de forme courte LITE sans RUN_CARD selon `ACTION/HANDOFF` | Artefact livré, autonomie exercée, décision, preuve, limite, escalade et prochaine action. |

Ces combinaisons ne sont pas des parcours obligatoires. Elles indiquent des capacités compatibles ; les sources propriétaires définissent le contenu exact des routes.

### Variation créative

Pour produire du beau varié sans bruit : `SAVOIR/CRAFT/CFT-02` (un axe situé à la fois).

Une alternative est utile si elle peut modifier le choix. Une référence, une ancre, une rationale ou une variante ne constitue pas une preuve indépendante.

### Garde-fous de la combinaison

- `ITER` demande de rappeler et réévaluer une direction retrouvable dans son périmètre ; un fix local qui la conserve reste `LITE` (`DIRECTION/START`).
- Un chemin court ne réduit jamais la protection d’un risque critique.
- Une capacité indisponible limite le claim correspondant ; elle ne justifie pas une baisse silencieuse du mode.
- Ne pas remplir toutes les routes d’une combinaison si une route principale suffit.
- Ne pas ajouter de trace, de variante ou de preuve qui ne peut changer la décision, l’artefact, la limite ou l’action suivante.

Arrêter l’orchestration lorsque la décision, le risque, le scope, l’owner, l’artefact, la preuve, la limite et la prochaine action sont suffisamment explicites. La richesse de lecture n’est pas un résultat ; **l’effet positif observable dans le périmètre déclaré** est le résultat recherché.

## Connexions situées

**Base de sources :** `R2026-10-04-AUDIT2-FIXES`.

Cet index dérivé rapproche des contributions des propriétaires ; chaque liaison est une hypothèse d’orientation à confronter au contexte. Il ne classe pas le mode, ne remplace pas CHARGE et ne déclare ni applicabilité ni résultat par reconnaissance d’un mot. Les sources ci-dessous appartiennent à la révision indiquée ; une différence de version impose leur réexamen. Les protections applicables restent dues même lorsqu’une suggestion facultative est écartée.

Pour une décision ouverte, consulter le sommaire avec `python3 scripts/read_route.py --connexions`, puis une entrée avec `python3 scripts/read_route.py --connexions C03`. Le lecteur expose condition, contributions, limites et locators résolus ; il ne compose pas automatiquement une snapshot et ne choisit pas les connexions applicables. La vue courte et sa fraîcheur restent définies par `ACTION/RUN_CARD`, section « Vue d’exécution dérivée ».

Une condition établie peut appeler la contribution utile ; une relation déjà résolue conserve sa source sans exploration supplémentaire. Une condition fausse écarte seulement la suggestion facultative. Une condition inconnue appelle une recherche, une clarification nécessaire ou une hypothèse explicite proportionnée selon le coût d’erreur. Avant construction, l’effet est attendu ; après observation seulement, il peut être déclaré observé. Aucun quota de connexions ou score de qualité n’est créé.

### C01 — Contexte incertain

**Condition et décision.** Une inconnue de public, tâche, culture, confiance ou contrainte peut changer structure, expression ou preuve.

**Sources.** `DIRECTION/DOMAIN-FRAME` ; `SAVOIR/FRAME/FND-03` ; `SAVOIR/SOURCE` si une recherche peut réduire l’incertitude.

**Intervention et effet attendu.** Nommer la question et sa conséquence ; approfondir le point susceptible de modifier l’artefact.

**Contre-indication et alternative.** Éviter la recherche de tout un secteur ou l’esthétique déduite du seul domaine ; conserver une hypothèse explicite lorsque le scope l’autorise.

**Moyens et limites.** Distinguer faits fournis, source retrouvée et hypothèse ; la disponibilité d’une recherche ne démontre pas la connaissance du public.

**Observation et réexamen.** Prévoir source, retour ou observation capable de corriger le cadrage ; réexaminer si tâche, public, culture, risque ou contrainte change.

### C02 — Typographie déterminante

**Condition et décision.** Voix, langue, chiffres, hiérarchie ou rendu typographique peuvent changer la décision.

**Sources.** `SAVOIR/TYPE` ; `SAVOIR/CRAFT/CFT-03` ; `DIRECTION/CREATIVE-BOOT` ; `ACTION/STRUCTURED-PROOF`.

**Intervention et effet attendu.** Partir de la police disponible et du vrai texte ; régler rôle, échelle, mesure, poids, interligne ou composition du titre pour la relation recherchée.

**Contre-indication et alternative.** Un overflow local n’appelle pas une nouvelle voix ; garder la famille adaptée et corriger le paramètre concerné.

**Moyens et limites.** Vérifier la famille livrée et ses axes disponibles ; une impression de marque ne démontre pas une meilleure compréhension.

**Observation et réexamen.** Préparer petit format, contenu long, glyphes, repli et hiérarchie ; réexaminer après changement de police, langue, contenu, format ou rôle.

### C03 — Asset déterminant

**Condition et décision.** Un asset porte une relation importante : choix, qualité, intégration, série ou usage restent ouverts, même si un fichier existe déjà.

**Sources.** `DIRECTION/VISUAL_TARGET` ; `SAVOIR/SOURCE` ; `SAVOIR/DESIGN-ATLAS` ; `SAVOIR/TOOLS` ; `BIBLIOTHEQUE/CONTRACTS` ; `ACTION/STRUCTURED-PROOF`.

**Intervention et effet attendu.** Nommer son rôle ; choisir une route disponible et régler sujet, cadrage, occupation, voisinage du texte et traitement utile. Relier qualité propre de la représentation, intégration et cohérence de série.

**Contre-indication et alternative.** Éviter l’image de remplissage et la confusion entre ancre et fichier de production. Un crop ou un traitement ne corrige pas un sujet inadéquat ; changer de ressource ou déclarer le plafond.

**Moyens et limites.** Fourniture, curation, génération dirigée, hybride, code natif ou absence d’asset restent conditionnels. Dans la fiche d’asset existante, rapprocher locator/version, constat de disponibilité, rôle, modification d’intégration, fallback et observation qui changerait le choix. Provenance, droits et limites sont conservés ; un contenu illustratif ne devient pas preuve d’un produit réel.

**Observation et réexamen.** Inspecter sujet, détail pertinent, crop, contraste, raccord, série et formats requis dans la scène ; réexaminer si asset, destination, droits, format, texte voisin ou moyen change.

### C04 — Récupération après erreur

**Condition et décision.** Une erreur peut interrompre une tâche ou faire perdre une saisie.

**Sources.** `SAVOIR/STATE` ; `ACTION/UI-UX-REALITY` ; `ACTION/GATE-A` pour les contrôles applicables.

**Intervention et effet attendu.** Préserver la saisie, expliquer l’erreur près de l’élément et rendre la reprise explicite. Après soumission bloquée, diriger le focus vers l’erreur ou le résumé si adapté.

**Contre-indication et alternative.** Éviter le déplacement de focus à chaque frappe ; annoncer l’erreur de façon accessible sans interrompre inutilement la saisie.

**Moyens et limites.** Une capture du message ne démontre ni conservation des données ni reprise ; la preuve demande le comportement pertinent dans le runtime réel.

**Observation et réexamen.** Parcourir erreur, correction puis succès ou issue claire ; réexaminer si validation, ordre, texte, focus, permissions ou réseau change.

### C05 — Réemploi situé

**Condition et décision.** Un ancien projet, une préférence, un composant, un profil ou une structure oriente le nouveau travail.

**Sources.** `DIRECTION/FIRST-OBJECT` ; `BIBLIOTHEQUE/CONTRACTS` ; `SAVOIR/STYLE` ; `SAVOIR/SYSTEM` selon le choix repris.

**Intervention et effet attendu.** Retrouver l’antécédent ; comparer teinte, paire typographique, ossature et objet de preuve lorsque la direction est concernée. Justifier la continuité située et calibrer la relation encore ouverte.

**Contre-indication et alternative.** Beauté et disponibilité seules ne justifient pas la reprise ; une conservation pertinente reste valide et n’impose pas de nouveauté.

**Moyens et limites.** Les champs absents restent inconnus ; l’antécédent n’est pas reconstruit de mémoire. Les valeurs adaptées et retrouvables restent réemployées.

**Observation et réexamen.** Comparer avec l’antécédent retrouvé et examiner les relations touchées ; réexaminer après changement de contexte, tâche, source de l’héritage ou artefact.

### C06 — Changement partagé

**Condition et décision.** Une modification touche une règle, un composant partagé ou plusieurs usages réels.

**Sources.** `DIRECTION/START` ; `ACTION/RUN-SYSTEM` ; `BIBLIOTHEQUE/COMPONENTS` ; `BIBLIOTHEQUE/EVOLUTION` ; `SAVOIR/SYSTEM` ; `CHANGELOG` pour la décision durable.

**Intervention et effet attendu.** Identifier usages, responsabilités, compatibilité, migration, owner et retour ; protéger les consommateurs concernés.

**Contre-indication et alternative.** Une correction locale ne devient pas une règle générale par sa beauté ou son nombre de réemplois ; maintenir la calibration locale si son périmètre suffit.

**Moyens et limites.** Baseline et liste des consommateurs demandent des sources retrouvables ; le gain observé et l’autorité de promotion restent distincts.

**Observation et réexamen.** Préparer non-régression sur les usages et états concernés ; réexaminer après changement de contrat, token, primitive, usage ou règle.

### C07 — Ambition vers construction

**Condition et décision.** Une relation visuelle reste ouverte : présence, caractère ou crédibilité doivent être construits. Aucun défaut observé n’est requis pour préparer cette relation.

**Sources.** `DIRECTION/CREATIVE-BOOT` ; `DIRECTION/VISUAL_TARGET` ; `SAVOIR/CRAFT/CFT-00` ; `SAVOIR/STYLE` ; `BIBLIOTHEQUE/SELECT` ; `BIBLIOTHEQUE/CONTRACTS`.

**Intervention et effet attendu.** Relier promesse et objet de preuve à une masse, un rythme, une voix, une matière, un contenu ou un comportement concret ; préparer le premier objet complet avec les qualités prioritaires utiles.

**Contre-indication et alternative.** Un adjectif ou nom de style ne spécifie pas l’intervention ; une relation déjà résolue ou un delta strictement local peut conserver sa préparation existante.

**Moyens et limites.** Le bilan FABRICATION conserve moyens réels et plafonds par couche. Une photographie absente n’est pas remplacée par une image présentée comme celle d’un produit réel.

**Observation et réexamen.** Prévoir présence, spécificité et résolution dans l’objet entier ; l’effet reste attendu avant observation. Réexaminer après changement de promesse, contenu, direction ou moyens.

### C08 — Élément vers ensemble

**Condition et décision.** Asset, primitive ou objet sont retenus, mais intégration, états ou déclinaisons laissent une relation importante ouverte.

**Sources.** `BIBLIOTHEQUE/COMPONENTS` ; `BIBLIOTHEQUE/CONTRACTS` ; `SAVOIR/CRAFT/CFT-00` ; `SAVOIR/SYSTEM` ; `SAVOIR/STATE` ; `ACTION/STRUCTURED-PROOF`.

**Intervention et effet attendu.** Régler les raccords image/texte, valeur/unité, objet/action, silhouette/grille et état/espace réservé. Composer une anatomie propre au produit en conservant les comportements et la sémantique fiables des primitives.

**Contre-indication et alternative.** Des effets supplémentaires ne résolvent pas une structure qui contredit le geste ; rouvrir la relation responsable. Conserver la calibration déjà adaptée.

**Moyens et limites.** Paramètres dans la spec, les tokens ou les composants existants du projet ; qualité intrinsèque et contribution à la scène restent distinctes. Une capture nominale isolée ne couvre pas les états ni la série.

**Observation et réexamen.** Préparer contenu long, états, formats et cohérence d’ensemble pertinents ; réexaminer après changement d’asset, anatomie, donnée, comportement, scène ou série.

### C09 — Intention vers médium

**Condition et décision.** Un support ou une déclinaison change les conditions de lecture, d’interaction ou de fabrication.

**Sources.** `SAVOIR/DESIGN-ATLAS` ; `SAVOIR/TECH` ; `DIRECTION/CREATIVE-BOOT` ; `ACTION/RUN_CARD` ; `ACTION/AUTHORITY`.

**Intervention et effet attendu.** Conserver la relation porteuse, puis adapter ordre, échelle, cadrage ou geste. Distinguer jugement transférable, moyens spécialisés et observation propre au support.

**Contre-indication et alternative.** Une réduction mécanique ne remplace pas une recomposition. Les routes d’interface apportent des responsabilités à traduire ; elles ne prescrivent pas universellement une affiche, une vidéo ou un espace.

**Moyens et limites.** Nommer production disponible, rendu observable, référentiel, budget pertinent et limite de preuve ; la traduction par médium de `SAVOIR/TECH` aide à les rapprocher. La couverture documentaire et l’outillage spécialisé diffèrent selon les médiums ; leur mention ne démontre pas leur maîtrise. La recette HTML ne couvre pas les autres supports.

**Observation et réexamen.** Préparer format et distance pour le print, séquence et interruption applicable pour le motion, contexte et runtime pour le spatial. Une image fixe ne prouve pas la fluidité ; une prévisualisation numérique ne prouve pas la fabrication physique. Réexaminer si support, diffusion, moyens ou contexte change.

## Activation multi-perspective

Une perspective ne se charge que si son déclencheur peut modifier la décision. `N/A-JUSTIFIED` est une sortie valide lorsque la perspective est examinée et non applicable. Ne pas charger une lecture ne rend jamais `N/A` un contrôle applicable du propriétaire.

| Perspective | Déclencheur | Lecture minimale | Sortie | Non-chargement |
|---|---|---|---|---|
| Direction | Identité, présence, premier objet ou composition ouverte | `DIRECTION` + cible | Thèse, objet, ancre, relation, défaut dominant | Décision visuelle intacte et delta strictement local |
| Production | Artefact ou modification à construire | `ACTION` + route du mode | Artefact, scope, état et prochaine preuve | Aucun artefact ou simple clarification |
| Usage | JTBD, action, confiance, récupération ou tâche critique | `ACTION/UI-UX-REALITY` | Geste, résultat, état, limite | Aucun impact sur usage déclaré |
| Contenu | Données, longueur, langue, claim ou état | `SAVOIR/TYPE` ou `STATE` | Contenu crédible, hiérarchie, limite | Contenu inchangé et non déterminant |
| Responsive | Mobile, zoom, reflow ou viewport critique | `ACTION/UI-UX-REALITY` + `SAVOIR/CONTEXT` | Recomposition, priorité, preuve de scope | Aucun changement de viewport ou risque déclaré |
| Accessibilité | Focus, clavier, sémantique, contraste, motion ou population critique | `SAVOIR/CONTEXT` + `ACTION/GATE-A` | Méthode, scope, résultat, limite | Aucun risque d’accessibilité au-delà des contrôles `ACTION/GATE-A` applicables, qui restent dus |
| Runtime | Compatibilité, performance, fallback ou plateforme | `SAVOIR/TECH` + `ACTION` | Runtime, méthode, erreur, fallback, preuve | Aucun claim technique |
| Preuve | Claim, capture, mesure, verdict ou clôture | `ACTION` | Claim, méthode, scope, date, limite, locator | Aucune affirmation de résultat |
| Maintenance | Consumer partagé, trace, migration ou reprise | `ACTION` + `CHANGELOG` si durable | Owner, diff, compatibilité, revue, réouverture | Delta local sans conséquence future |
| Coordination | Handoff, escalade, action externe ou owner suivant | `ACTION/AUTHORITY` et sortie | Destinataire, autonomie, confirmation, prochaine action | Aucun transfert |
| Mémoire | Décision durable, version, réserve ou migration | `RUN_CARD` et `CHANGELOG` si promotion | Décision, date, statut, preuve, réserve, revue | Décision strictement éphémère |

## Handoff minimal commun

Ce bloc est une copie du handoff canonique (voir `ACTION/HANDOFF`) ; il ne remplace pas `ACTION` ni le schéma `RUN_CARD`.

```text
MODE:
DECISION:
RISK:
SCOPE:
ARTIFACT:
OBSERVATION / METHOD:
PROOF / TRACE-LOCATOR:
LIMIT / NOT-VERIFIED:
DECISION-CHANGE:
NEXT-ACTION:
OWNER:
NEXT-PROOF:
EXIT-CONDITION:
```

Les champs non applicables doivent être marqués `N/A-JUSTIFIED` ; ils ne doivent pas être inventés. Si un run est persistant, la projection `RUN_CARD` et son validateur restent obligatoires selon le mode et le risque, sauf la forme courte LITE sans RUN_CARD définie par `ACTION/HANDOFF` et `ACTION/CLOSE-PACKAGE`. Une demande de projection structurée conserve le schéma et le validateur.

## Résolution des routes

Les noms de route sont des locators documentaires. Pour les résoudre, utiliser le fichier propriétaire, puis son titre exact. Un renvoi qui ne résout pas doit être déclaré obsolète, conceptuel ou `NOT-VERIFIED`; il ne doit jamais être traité comme une instruction active par supposition.

| Préfixe | Propriétaire |
|---|---|
| `DIRECTION/*` | `DIRECTION.md` |
| `ACTION/*` | `ACTION.md` |
| `SAVOIR/*` | `SAVOIR.md` |
| `BIBLIOTHEQUE/*` | `BIBLIOTHEQUE.md` |
| `CHANGELOG/*` | `CHANGELOG.md` |
| `RUN_CARD` | `schemas/run_card.schema.json`, exemple et validateur |

`RUN_CARD` est un **adaptateur machine**, pas un locator Markdown résolvable par `scripts/read_route.py`. Pour l’inspecter ou le valider, utiliser le schéma, l’exemple et `scripts/validate_run_card.py`; ne pas l’invoquer comme une route documentaire.

## Locators principaux

Les identifiants structurels documentés, tels que `GRID/HIERARCHICAL` ou `MICRO/USAGE_LEDGER`, sont aussi acceptés par le lecteur, seuls ou préfixés par `BIBLIOTHEQUE/`. Il sert le titre exact, ou la section porteuse lorsque l’identifiant est une ligne de table. Ce raccourci n’ajoute pas de route canonique ; un identifiant absent, ambigu ou situé seulement dans un exemple de code est refusé.

Cette table liste des **raccourcis et sous-locators** ; elle n’est pas un inventaire. `scripts/read_route.py` résout un locator en trois étapes : (1) la table ci-dessous, y compris les sous-locators écrits `titre › titre` ; (2) le préfixe propriétaire et le titre unique qui commence par le locator ; (3) le sous-locator `X/Y/Z`, cherché sous le titre `X/Y`. Un locator porté par deux titres est refusé comme ambigu. Un sous-bloc qui porte son propre locator est exclu du bloc parent et servi séparément. Une route qui ne résout pas ne doit pas être devinée.

| Locator | Destination exacte |
|---|---|
| `DIRECTION/START` | `DIRECTION.md` — `## DIRECTION/START — classer avant d’agir` |
| `DIRECTION/START/TREE` | `DIRECTION.md` — `## DIRECTION/START — classer avant d’agir` › `### Arbre de classification` |
| `DIRECTION/FIRST-OBJECT` | `DIRECTION.md` — `## DIRECTION/FIRST-OBJECT — compiler le brief et produire le premier objet` |
| `DIRECTION/VISUAL_TARGET` | `DIRECTION.md` — `## DIRECTION/VISUAL_TARGET — rendre la direction pilotable` |
| `DIRECTION/DOUBLE-LOOP` | `DIRECTION.md` — `## DIRECTION/DOUBLE-LOOP — créer puis apprendre` |
| `DIRECTION/FAST-PATH` | `DIRECTION.md` — `### DIRECTION/FAST-PATH — renvoi vers l’exécution courte` |
| `ACTION/RUN-LITE` | `ACTION.md` — `### \`ACTION/RUN-LITE\`` |
| `ACTION/RUN-ITER` | `ACTION.md` — `### \`ACTION/RUN-ITER\`` |
| `ACTION/RUN-STANDARD` | `ACTION.md` — `### \`ACTION/RUN-STANDARD\`` |
| `ACTION/RUN-DIRECTION` | `ACTION.md` — `### \`ACTION/RUN-DIRECTION\`` |
| `ACTION/RUN-SYSTEM` | `ACTION.md` — `### \`ACTION/RUN-SYSTEM\`` |
| `ACTION/FIRST-RENDER` | `ACTION.md` — `## ACTION/FIRST-RENDER — qualité initiale attendue` |
| `ACTION/FAST-PATH` | `ACTION.md` — `## ACTION/FAST-PATH — preuve minimale sans rituel` |
| `ACTION/UI-UX-REALITY` | `ACTION.md` — `### ACTION/UI-UX-REALITY — construire l’interface et la tâche ensemble` |
| `ACTION/CLOSE-PACKAGE` | `ACTION.md` — `## ACTION/CLOSE-PACKAGE — paquet de clôture` |
| `ACTION/GATE-A` | `ACTION.md` — `## ACTION/GATE-A — plancher objectivable` |
| `ACTION/ROUTING` | `ACTION.md` — `## ACTION/ROUTING — prérequis de jugement et de structure` |
| `ACTION/CLOSE-EXIT-CHECK` | `ACTION.md` — `## ACTION/CLOSE-EXIT-CHECK — test de sortie canonique` |
| `SAVOIR/READ` | `SAVOIR.md` — `## SAVOIR/READ — comment utiliser cette bibliothèque` |
| `SAVOIR/ROUTING` | `SAVOIR.md` — `## SAVOIR/ROUTING — routes stables` |
| `SAVOIR/CRAFT` | `SAVOIR.md` — `# SAVOIR/CRAFT — anti-slop, composition et expression` |
| `BIBLIOTHEQUE/READ` | `BIBLIOTHEQUE.md` — `## BIBLIOTHEQUE/READ — responsabilités et convention de route` |
| `BIBLIOTHEQUE/SELECT` | `BIBLIOTHEQUE.md` — `## BIBLIOTHEQUE/SELECT — choisir avant de composer` |
| `BIBLIOTHEQUE/COMPONENTS` | `BIBLIOTHEQUE.md` — `## BIBLIOTHEQUE/COMPONENTS — couches et dépendances` |
| `BIBLIOTHEQUE/EVOLUTION` | `BIBLIOTHEQUE.md` — `## BIBLIOTHEQUE/EVOLUTION — promotion et dépréciation` |

## Condition d’arrêt

Arrêter la lecture lorsque la décision, le risque, le propriétaire, la sortie, la prochaine preuve et la limite sont suffisamment explicites pour le prochain propriétaire. Continuer uniquement si une section supplémentaire peut modifier l’un de ces éléments. Une décision visuelle peut rester `EXPLORATORY` ; une validation documentaire ne devient pas une preuve d’usage, d’accessibilité, de performance ou de qualité réelle.
