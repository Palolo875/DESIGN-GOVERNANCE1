# Agent — répondre

Ce que l’agent remet à la personne : la réponse visible, la trace courte, et quand une trace complète est nécessaire.

<!-- origine:ACTION.md -->
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

Ces rubriques servent une proposition fabriquée ; omets celle qui n’a pas de contenu utile. Une réponse de jugement, d’explication ou de correction donne le résultat, ses raisons et les limites qui l’affectent, sans rubrique « vraie version » ni relance automatique.

L’agent active le système en silence : la personne donne l’objectif, le périmètre et l’autonomie ; l’agent choisit le mode, charge les sources et tient la trace. Le mode, la conséquence décisionnelle d’`ACTION/STATUS` (décision changée, confirmée ou abandonnée, `N/A-JUSTIFIED` ou `NOT-OBSERVED`), la preuve et l’owner restent dans la trace et sont exposés sur demande (« pourquoi ? », « qu’as-tu vérifié ? »). Les codes de route, de concept et de statut n’apparaissent dans la réponse visible que si la personne travaille sur le système lui-même ou les demande explicitement ; quand la trace est écrite dans le fichier livré, la réponse ne la recopie pas sauf demande explicite. Les limites de vérification qui affectent l’usage ou la décision restent visibles, même lorsque la trace est persistée. La réponse visible ne remplace jamais le handoff d’un run persistant.
<!-- noyau:fin SORTIE -->

3. **Niveau de trace**, choisi par l’agent :

<!-- noyau:début TRACE -->
<!-- concept:TRA-01 -->
**Trace légère par défaut.** Adapte contrôles et trace au risque et à la décision ; réutilise la trace existante. Chaque ajout doit vérifier une affirmation, protéger un risque, permettre une reprise ou préparer une acceptation. Hors run persistant, partagé ou audité, la trace tient en six lignes au plus : mode ; thèse (promesse → objet de preuve → geste) ; modal, trame et parti ; plafond atteint et contenus marqués ; défaut dominant restant ; prochaine preuve. Lorsque la qualité perceptuelle est une décision du run, la ligne du défaut dominant résume la revue de `SAVOIR/CRAFT/CFT-00` : ce qui retient, ce qui reste générique, puis le geste de `SAVOIR/STATE` appliqué et réinspecté, ou seulement envisagé, ou la raison de conserver. Elle s’écrit à côté de l’artefact quand l’agent écrit des fichiers (fichier de trace ou en-tête du fichier livré) ; sinon, après la réponse visible, sous « Trace ». Les planchers s’appliquent pendant la fabrication (vérité, `ACTION/GATE-A` selon le profil de surface, boucle d’édition) ; seule leur écriture s’allège. Le run livre une **proposition** `EXPLORATORY` (au sens d’`ACTION/STATUS` : le rendu existe, les preuves d’acceptation manquent encore) : ni verdict, ni acceptation, ni clôture, ni `RUN_CARD`. **Trace complète** (handoff, paquet de clôture, gates écrits et projection selon `ACTION/CLOSE-PACKAGE`, `B1b` dans son scope) si le run est persistant, partagé, audité, ou si une acceptation ou une clôture est demandée. Montrer, enregistrer ou envoyer une proposition pour avis ne rend pas le run persistant ni partagé : ces mots désignent un travail transmis pour être repris par un autre, adopté ou accepté. La forme courte LITE conserve une trace complète sans RUN_CARD (`ACTION/HANDOFF`).
<!-- noyau:fin TRACE -->

**Formes.** La ligne de run de `DIRECTION` est la mémoire de lancement, sous-ensemble de lancement de ce handoff ; le handoff est la transmission ; `ACTION/CLOSE-PACKAGE` est la clôture par mode ; la `RUN_CARD` JSON est la projection persistante, selon la table de correspondance d’`ACTION/RUN_CARD`. **Forme courte LITE** (trace complète d’un `LITE` clôturé sans `RUN_CARD`, distincte de la trace légère, qui ne clôture pas) : le paquet LITE de `ACTION/CLOSE-PACKAGE` ; les autres champs du handoff sont `N/A-JUSTIFIED` par défaut, avec deux pertes déclarées (METHOD, EXIT-CONDITION) ; TRACE-LOCATOR est alors l’artefact. Une reprise par un autre agent exige OWNER et NEXT-ACTION ; sinon la forme courte reste une préparation.

Le handoff réutilise les champs existants ; il ne crée ni statut, ni gate, ni nouveau schéma. Les champs non applicables sont marqués `N/A-JUSTIFIED`. Un run persistant utilise la projection `RUN_CARD` et son validateur, sauf la forme courte LITE définie ci-dessus : sa trace complète persiste dans l’artefact selon `ACTION/CLOSE-PACKAGE`. Cette exception ne dispense ni des preuves dues ni des conditions de reprise ; une demande de projection structurée requiert la `RUN_CARD` validée. Une sortie courte qui ne fournit pas le paquet applicable reste une préparation, une clarification ou une décision non clôturée.

**Quatre registres de la trace.** Une trace ne mélange pas quatre registres, dans cet ordre : observation, interprétation, décision, persistance. La preuve réunit observation et interprétation ; elle ne se confond pas avec la décision. Ces registres structurent la trace sans créer d’état ni de statut.

| Registre | Question | Sortie minimale |
|---|---|---|
| **Observation** | Qu’est-ce qui a été regardé, par quelle méthode, dans quel scope et quelle version ? | Artefact, méthode, scope, version, date et capacité. |
| **Interprétation** | Que montre réellement l’observation, avec quelle couverture et quelle limite ? | Relation, effet, défaut dominant, incertitude et limite. |
| **Décision** | Que fait-on maintenant et pourquoi ? | Correction, retour, acceptation, réserve, reclassification ou escalade. |
| **Persistance** | Où la décision et ses limites restent-elles inspectables ? | Trace complète selon `ACTION/HANDOFF`, projection `RUN_CARD` selon la forme de clôture, trace locator, owner, prochaine preuve et condition de sortie. |

**Condition d’arrêt de lecture :** arrêter lorsque le mode, le risque, la route, la preuve, la limite, le propriétaire et la prochaine action sont connus. Charger un registre, une route ou un gate supplémentaire uniquement s’il peut modifier l’un de ces éléments.
