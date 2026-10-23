# Sections de référence — ACTION : livraison et preuves

**Design Governance V1 — expérimentation maintenue.** Cette V1 est un cadre de travail en évaluation ; elle n’est pas présentée comme une release publique stabilisée. Ses limites, preuves et conditions d’usage restent explicites. ACTION transforme une direction ou une décision produit en trace de run, artefacts observables, preuves adaptées, gates proportionnés et verdicts inspectables.

<!-- lieux:début -->
> **Ce fichier ne contient pas toute la responsabilité `ACTION`.** Il contient les sections rangées dans ce fichier ; les autres sections `ACTION` vivent à leur emplacement, avec la même autorité, et ne sont pas recopiées ici. Une route se lit avec `python3 scripts/read_route.py LOCATOR`, qui trouve son fichier. _Bandeau généré par `scripts/build_core.py` depuis le registre `LIEUX` ; ne pas modifier à la main._
>
> - [`agent/chemins.md`](../agent/chemins.md) : `ACTION/RUN`, `ACTION/RUN-LITE`, `ACTION/RUN-ITER`, `ACTION/RUN-STANDARD`, `ACTION/RUN-DIRECTION`, `ACTION/RUN-SYSTEM`, `ACTION/FAST-PATH`, `ACTION/ROUTING`
> - [`agent/repondre.md`](../agent/repondre.md) : `ACTION/HANDOFF`
> - [`gouvernance/principes.md`](../gouvernance/principes.md) : `ACTION/AUTHORITY`
> - [`gouvernance/statuts.md`](../gouvernance/statuts.md) : `ACTION/STATUS`
> - [`gouvernance/travail.md`](../gouvernance/travail.md) : `ACTION/PRECONDITION`, `ACTION/RUN_CARD`, `ACTION/PIPELINE-DIRECTION`
> - [`gouvernance/verification.md`](../gouvernance/verification.md) : `ACTION/STRUCTURED-PROOF`, `ACTION/GATE-B`, `ACTION/OVERRIDE`
> - [`gouvernance/cloture.md`](../gouvernance/cloture.md) : `ACTION/CLOSE-PACKAGE`, `ACTION/CLOSE-EXIT-CHECK`
> - [`design/produit/premier-rendu.md`](../design/produit/premier-rendu.md) : `ACTION/FIRST-RENDER`, `ACTION/UI-UX-REALITY`
> - [`design/produit/plancher.md`](../design/produit/plancher.md) : `ACTION/GATE-A`, `ACTION/RECETTE-RENDU`, `ACTION/POLICIES`
> - [`design/produit/finition.md`](../design/produit/finition.md) : `ACTION/GATE-C`, `ACTION/ANTI-SLOP`, `ACTION/ATELIER-EDITION`
> - [`design/produit/preuve-visuelle.md`](../design/produit/preuve-visuelle.md) : `ACTION/VISUAL_PROOF`, `ACTION/RECETTE-CARACTERE`
> - [`maintenance/evolution.md`](../maintenance/evolution.md) : `ACTION/MAINTENANCE`
<!-- lieux:fin -->

<!-- orientation:début -->
## Responsabilité

`ACTION` est le propriétaire des preuves exécutables, des gates, des statuts de run, des verdicts et de la clôture. Dans un run, le chargement suit `DIRECTION/CHARGE`, seule liste de chargement. Pour lire ACTION hors run, commencez par `ACTION/STATUS` et `ACTION/PRECONDITION`, puis la route de votre mode `ACTION/RUN-<MODE>`, et chargez seulement les gates correspondant au risque déclaré. `ACTION/FAST-PATH` est une vue de formalité réduite pour un delta local ; il ne supprime ni la preuve requise ni l’honnêteté du statut.

**Capacité positive d’ACTION.** ACTION ne sert pas seulement à filtrer ou accepter un résultat : elle transforme une direction en livraison observable et améliorable. Son chemin positif est la boucle d’édition (`DIRECTION/DOUBLE-LOOP`), prolongée par la preuve et, en trace complète, par une clôture avec une limite et une prochaine preuve. Les gates protègent ce chemin ; ils ne sont pas sa finalité. La qualité du premier rendu, la lisibilité de la décision et la possibilité de reprendre le run font partie de la valeur livrée.

### Carte de lecture par mode

La liste de chargement de chaque mode est `DIRECTION/CHARGE`, la seule du corpus ; la skill active sa ligne à la demande. Cette section ne la répète pas : elle précise seulement ce qui s’ajoute selon la trace.

**Socle pour tous les modes :** `ACTION/STATUS` et `ACTION/PRECONDITION`, dès que le run écrit un statut, un gate ou un verdict (trace complète) ; `DIRECTION/CHARGE` reste la liste du démarrage.

Le paquet de sortie de chaque mode est défini par `ACTION/CLOSE-PACKAGE` ; `ACTION/RUN-DIRECTION` (ancrages) et `ACTION/RUN-SYSTEM` (`closure.system_package`) en précisent le détail.

Les sections `RUN_CARD`, `CLOSE-PACKAGE` et `CLOSE-EXIT-CHECK` s’ajoutent lorsque la trace est persistante ou que la clôture l’exige. `FAST-PATH` n’est pas une sixième voie : chaque occurrence de ce nom reste une vue locale du propriétaire qui l’emploie.

### Parcours minimal

Le parcours d’un run est celui du noyau de la skill : classer et charger (`DIRECTION/CHARGE`), prendre le brief, construire une première scène complète, boucler (`DIRECTION/DOUBLE-LOOP`), répondre et tracer (`ACTION/HANDOFF`). ACTION en porte les preuves, les gates et, en trace complète, la clôture ; ses contrats restent applicables dès que le risque ou le mode les déclenche.
<!-- orientation:fin -->
