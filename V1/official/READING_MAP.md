# READING_MAP — carte dérivée de lecture et d’activation

**Statut :** guide dérivé non normatif. Les sources normatives sont leurs sections propriétaires à leurs emplacements actuels ; le schéma `RUN_CARD` et les validateurs propriétaires font foi en cas de divergence.

## Utilisation

Cette carte réduit la recomposition mentale du lecteur. Elle ne crée ni mode, ni gate, ni axe, ni statut, ni verdict, ni owner de décision supplémentaire. Elle indique seulement où commencer, quoi charger, ce qui doit sortir et quand transmettre.

Pour composer plusieurs capacités selon un résultat recherché — direction, beauté située, créativité, usage, preuve, vitesse ou système — voir la section [« Combinaisons par résultat recherché »](../../guides/designer.md#combinaisons-par-résultat-recherché) du guide du designer : elle aide à ajuster la combinaison et l’intensité sans remplacer les propriétaires normatifs.

## Chemin canonique de démarrage

1. Localiser la version V1 réellement fournie.
2. Lire `guides/equipe.md` ou cette carte si le besoin est déjà identifiable.
3. Ouvrir `DIRECTION/START` pour classer le mode et le risque dominant.
4. Charger la ligne du mode dans `DIRECTION/CHARGE`, puis approfondir seulement le propriétaire capable de modifier la prochaine décision.
5. Ouvrir `ACTION` dès qu’un artefact, une observation, une preuve, un état ou une clôture est concerné.
6. Persister la sortie selon `ACTION/HANDOFF` et `ACTION/CLOSE-PACKAGE` lorsque le run doit être repris, comparé ou fermé ; la forme courte LITE peut être complète sans RUN_CARD, la projection structurée suit `ACTION/RUN_CARD`.

`DIRECTION/START` reste la seule classification. Cette carte ne reclassifie pas.

## Constitution minimale

Les cinq absolus de `DIRECTION` protègent chaque run : résumé dans la section « Les cinq règles essentielles » du README du package, formulation canonique dans [standard de qualité](../../design/direction/standard.md#les-cinq-règles-absolues).

## Routage minimal par décision

| Décision dominante | Première lecture | Ajouter seulement si nécessaire |
|---|---|---|
| Brief vague ou risque inconnu | `DIRECTION/START` | `DIRECTION/EXTERNAL-START` |
| Correction locale | `DIRECTION/START` → `ACTION/RUN-LITE` ou `RUN-ITER` | `SAVOIR` ou `BIBLIOTHEQUE` si la décision change |
| Nouvelle surface opérationnelle | `DIRECTION/START` → `ACTION/RUN-STANDARD` | `BIBLIOTHEQUE/SELECT`, `SAVOIR/CONTEXT` |
| Direction identitaire | `DIRECTION/START` → `DIRECTION/CHARGE` (mode `DIRECTION`) | `SAVOIR/CRAFT`, `DIRECTION/DIRECTION-ATELIER` |
| Structure ou composant partagé | `DIRECTION/START` → `ACTION/RUN-SYSTEM` | `BIBLIOTHEQUE/COMPONENTS`, `SAVOIR/SYSTEM`, `maintenance/versions.md` |
| Preuve, vérification ou clôture | `ACTION` | Gate et route correspondant au risque |
| Règle ou route durable | `maintenance/evolution.md`, `maintenance/versions.md` et source propriétaire | `ACTION` pour preuve et `BIBLIOTHEQUE/EVOLUTION` si structure |

Sortie : réponse visible et trace légère par défaut ; handoff et clôture (`ACTION/CLOSE-PACKAGE`) en trace complète (`ACTION/HANDOFF`).

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
