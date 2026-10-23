# Verrous de formulation touchés par A9, A10 et A11

Inventaire de l’action A23. Fichier de travail, hors du paquet, comme `SUIVI.md` et `AUDIT.md`.

## Méthode

Sur une copie du paquet au commit `4e2f42e`, chaque plage visée a été vidée de son texte, une à la fois. Les marqueurs structurels (`noyau:`, `concept:`, `origine:`, `lieux:`) sont restés en place. Sept contrôles ont ensuite été lancés :
- `build_core.py --check` ;
- `validate_structure.py`, `validate_reading_map.py`, `validate_design_governance.py` ;
- `test_read_route.py`, `test_audit_regressions.py`, `test_core_budget.py`.

Chaque échec est un verrou. Le script (`verrous.py`) et son résultat brut (`verrous.json`) restent dans la session.

**Portée.** Vider une plage simule une suppression ou une reformulation complète. Un déplacement vers un autre fichier de la **même responsabilité** ne fait tomber aucun de ces verrous si la table `LIEUX` est mise à jour : les validateurs lisent chaque source à son emplacement actuel, ce que la régression de déplacement de `validate_all.py` prouve déjà. Les liens Markdown vers un fichier précis font exception : ils doivent suivre le texte.

## Résultat

19 plages testées, 25 contrôles en échec. Comme certaines plages se recoupent (les déclencheurs et l’index font partie de la plage A9-1), cela fait 22 verrous distincts. 7 plages ne portent aucun verrou :
- l’interface (`design/produit/interface.md`) ;
- les principes (`gouvernance/principes.md`) ;
- la clôture (`gouvernance/cloture.md`) ;
- la table de `SAVOIR/ROUTING` ;
- la ligne `RUN` ;
- `DECISION-INTENT` ;
- la mémoire de lancement.

Décisions proposées :
- **Garder** : le texte reste, ou il change de lieu dans sa responsabilité, et le verrou suit sans modification.
- **Déplacer** : le verrou est réécrit pour pointer vers le nouveau lieu ou la nouvelle forme.
- **Remplacer** : le verrou devient un contrôle structurel, ou un contrôle existant le couvre déjà.
- **Après A11** : le verrou protège justement ce qu’A11 doit trancher ; il sera décidé avec A11.

| Plage visée (action) | Contrôle qui tombe | Ce qu’il protège | Décision proposée |
|---|---|---|---|
| Déclencheurs critiques, `agent/chemins.md:242-253` (A9, A10) | `FAC-01` « Détail final susceptible » (C26) | La ligne garde « selon la question ouverte » | Déplacer vers la table unique de signaux (A10). |
| idem | `LCF-17` | Motif générique → `CFT-01` et `ACTION/ANTI-SLOP` ; scène → BIBLIOTHEQUE ; détail final → `SAVOIR/CRAFT` | Déplacer : ces correspondances doivent figurer dans la table unique ; les contrôler là. |
| Index à la demande, `agent/chemins.md:257-271` (A9, A10) | `LCF-06` | « Nouvelle structure d’écran » ne fait pas classer `STANDARD` par l’index | Remplacer : si l’index disparaît, la règle « une table ne reclasse pas » se contrôle sur la table unique. |
| Absolus, `design/direction/standard.md` (A9) | Trois fragments `#les-cinq-règles-absolues` (README, carte de lecture, guide 3) | Liens vers la formulation qui fait foi | Déplacer : mettre à jour les trois liens avec le texte. |
| Direction divergente, `design/direction/diriger.md:119-134` (A9) | Concept `ALT-01` absent | L’alternative située existe en un seul lieu | Garder : la balise suit le texte. Le contrôle d’atteignabilité de A9 vérifiera qu’elle est servie. |
| Contrats de structure, `gouvernance/structure.md:6-19` (A9) | `LCF-51` et `test_inheritance_cannot_become_non_applicability` | « Zéro route » : héritage distinct de la non-applicabilité | Garder : la condition suit le texte dans BIBLIOTHEQUE. |
| `sections/DIRECTION.md:25-152` (A9, A11) | `ORD-01` « Posture » et « Récapitulatif de protection » | Rôle, posture et récapitulatif avant `DIRECTION/START` | Remplacer : la posture est compilée dans le noyau, dont l’ordre est fixé par `build_core.py`. Pour le récapitulatif, décider avec A9 s’il est rattaché, fusionné ou supprimé. |
| idem | `LCF-07` | Cible visuelle avant premier objet, dans `RUN-PRIORITY` | Remplacer : `CHG-07` contrôle déjà cet ordre dans `DIRECTION/CHARGE`. Le libellé cite des numéros de ligne périmés (L7-09). |
| idem | `LCF-29` | Légende des tags cohérente avec SAVOIR | Déplacer avec la légende. |
| Introduction de `sections/ACTION.md` (A9) | `LCF-25`, « Carte de lecture par mode », « FAST-PATH … sixième voie » | La carte d’ACTION renvoie à `CHARGE` ; `FAST-PATH` est une vue, pas une voie | Garder si le texte reste dans ACTION. Sinon déplacer, en vérifiant d’abord que `CHARGE` ne contredit pas ces deux règles. |
| Introduction de `sections/BIBLIOTHEQUE.md` (A9) | `MNT-01` « préambule introuvable » | Pas de maintenance dans le préambule lu en premier | Remplacer : la règle n’a de sens que si un préambule est lu ; contrôler plutôt les routes servies. |
| Introduction de `sections/SAVOIR.md` (A9) | `LCF-38` | « La sortie de SAVOIR… À la clôture » | Déplacer avec la phrase. |
| Table d’`ACTION/ROUTING`, `agent/chemins.md:349-360` (A10) | `FAC-01` ligne « Token, composant ou blast radius » (C26) | « si un composant change » | Déplacer vers la table unique. |
| Entrée minimale, `agent/chemins.md:36-48` (A11) | `LCF-08` | `OWNER` et `SCOPE` « jamais omis » | Après A11 : c’est la règle que L1-03 met en question en trace légère. |
| idem | `LCF-43` | La ligne `CONSTRAINT — destination` et le bilan `FABRICATION` | Après A11 : à garder sous la forme de déclaration retenue. |
| Formats du guide 3 (A11) | `LCF-C2` | Le guide 3 renvoie à la réponse visible d’`ACTION/HANDOFF` | Garder : un seul format dans le guide, avec le même renvoi. |

## Ce qu’on en retient

- **Le coût est plus faible que prévu.** L7-09 comptait environ 190 verrous dans tout le paquet. Les plages visées par A9 à A11 n’en touchent que 22 :
  - 7 suivent le texte si celui-ci reste dans sa responsabilité ;
  - 8 se déplacent avec lui ;
  - 5 peuvent être remplacés par un contrôle structurel ou existant ;
  - 2 dépendent de la décision d’A11.
- **Rattacher plutôt que réécrire.** Les rattachements de A9 peuvent commencer sans toucher aux verrous, à condition de rattacher la plage à une route de sa responsabilité plutôt que de la réécrire.
- **Le seul vrai conflit de fond est `LCF-08`.** Il impose « `OWNER` et `SCOPE` jamais omis », alors que la trace légère tient en six lignes. Il se tranche avec A11.

## Constaté en exécution

- **2026-10-23, plage 2 (déclencheurs).** Un verrou de plus est apparu au déplacement : la garde de fidélité « détail final conditionnel, par CHARGE » (`validate_structure.py`, `FIDELITY`), qui ne tombait pas quand la plage était vidée, puisque la ligne disparaissait avec elle. Limite de la méthode : vider une plage révèle les verrous de présence, pas les verrous de fidélité qui suivent le texte déplacé. Résolu en gardant la précision dans la ligne déplacée.
- `LCF-06` et `LCF-17` contrôlent désormais la table des signaux du noyau ; chacune a sa mutation rouge conservée.
- **2026-10-23, A6.** Le renvoi `MOY-01` (garde 2) suivait la sous-section « route de production » : il pointe désormais vers `DIRECTION/ASSET-ROUTE`. Trois contrôles de la carte (`LCF-43`, `LCF-48`, `LCF-49`) découpent le texte entre les titres de cette sous-section et de la suivante : leurs bornes suivent les nouveaux titres.
- **2026-10-23, A11.** `LCF-08` suit la nouvelle phrase et exige « En trace complète » (mutation rouge ajoutée). `boot_block` (LCF-43, LCF-45) suit la nouvelle phrase d’introduction du boot. Limite de la garde 2 : un renvoi est satisfait par n’importe quelle citation du locator dans la route ; une citation ajoutée pour une autre raison peut masquer la perte du renvoi utile (vu avec `wrong_owner`).
