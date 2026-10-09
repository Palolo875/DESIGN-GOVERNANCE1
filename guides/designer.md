# Guide du designer

Pour qui connaît le design : où se trouve chaque sujet, comment combiner les capacités selon le résultat cherché, et quand s’arrêter de lire. Les connexions entre domaines sont dans [`design/savoir/connexions.md`](../design/savoir/connexions.md).

<!-- origine:READING_MAP.md -->
## Carte des sujets

Pour un sujet traité dans plusieurs routes, cette carte dérivée nomme la route propriétaire puis les renvois utiles. Elle ne crée ni route, ni chargement, ni autorité : la source propriétaire reste normative. `python3 scripts/read_route.py --trouver` l’affiche en tête lorsque la requête nomme un sujet ou l’un de ses alias. Le validateur vérifie que chaque route citée se résout et traite le sujet en toutes lettres.

| Sujet | Propriétaire | Voir aussi |
|---|---|---|
| capture | `ACTION/VISUAL_PROOF` | `ACTION/GATE-B/B1b`, `ACTION/GATE-A` |
| hiérarchie | `SAVOIR/CRAFT/CFT-03` | `SAVOIR/CRAFT/CFT-00`, `SAVOIR/TYPE` |
| contraste | `ACTION/GATE-A` | `SAVOIR/CRAFT/CFT-05`, `ACTION/POLICIES` |
| typographie | `SAVOIR/TYPE` | `SAVOIR/CRAFT/CFT-05`, `ACTION/GATE-C` |
| couleur | `SAVOIR/CRAFT/CFT-05` | `ACTION/GATE-A` |
| mobile | `ACTION/UI-UX-REALITY` | `SAVOIR/STATE`, `SAVOIR/CONTEXT`, `BIBLIOTHEQUE/SEQUENCE` |
| état | `SAVOIR/STATE` | `ACTION/UI-UX-REALITY` |
| performance | `SAVOIR/TECH` | `SAVOIR/CONTEXT` |
| accessibilité | `SAVOIR/CONTEXT` | `ACTION/GATE-A`, `ACTION/POLICIES` |
| densité | `SAVOIR/CRAFT/CFT-03` | `ACTION/GATE-C` |
| grille | `BIBLIOTHEQUE/GRID` | `BIBLIOTHEQUE/SELECT` |
| composant | `BIBLIOTHEQUE/COMPONENTS` | `SAVOIR/SYSTEM`, `ACTION/RUN-SYSTEM` |
| exemple | `DIRECTION/EXTERNAL-START` | `DIRECTION/FIRST-OBJECT` |
| image | `SAVOIR/SOURCE` | `DIRECTION/VISUAL_TARGET`, `SAVOIR/DESIGN-ATLAS` |
| convergence | `SAVOIR/TOOLS/CONVERGENCE` | `SAVOIR/CRAFT/CFT-05`, `BIBLIOTHEQUE/SELECT` |
| structure | `BIBLIOTHEQUE/SELECT` | `BIBLIOTHEQUE/READ` |
| séquence | `BIBLIOTHEQUE/SEQUENCE` | `BIBLIOTHEQUE/SCENE` |
| texte sur image | `SAVOIR/CRAFT/CFT-03` | — |
| graphique | `BIBLIOTHEQUE/MICRO` | — |
| état vide | `ACTION/UI-UX-REALITY` | `SAVOIR/STATE` |
| pied de page | `BIBLIOTHEQUE/SEQUENCE` | — |
| cartes | `BIBLIOTHEQUE/SEQUENCE` | `BIBLIOTHEQUE/SELECT` |

<!-- origine:READING_MAP.md -->
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

<!-- origine:READING_MAP.md -->
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

<!-- origine:READING_MAP.md -->
## Condition d’arrêt

Arrêter la lecture lorsque la décision, le risque, le propriétaire, la sortie, la prochaine preuve et la limite sont suffisamment explicites pour le prochain propriétaire. Continuer uniquement si une section supplémentaire peut modifier l’un de ces éléments. Une décision visuelle peut rester `EXPLORATORY` ; une validation documentaire ne devient pas une preuve d’usage, d’accessibilité, de performance ou de qualité réelle.
