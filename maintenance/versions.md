# Ce que contient Design Governance V1.0.0

**Version expérimentale :** `V1.0.0`
**Statut expérimental :** Design Governance V1.0.0 est une expérimentation maintenue.  
**Révision :** `R2026-10-14-REVUE`, 14 octobre 2026.  
**Usage recommandé :** pilote avec revue humaine et preuves adaptées au risque.

Cette fiche décrit ce que le système possède aujourd’hui et ce qui en est vérifié. Elle ne retrace pas son histoire.

## Ce que fait le système

Design Governance aide un agent, ou une personne, à concevoir des pages, des écrans et des identités visuelles qui ont une direction, qui sont construits et soignés dès la première proposition, puis à les améliorer en regardant le rendu. Quand un travail doit être repris, livré ou accepté, il garde la trace de ce qui a été vérifié et de ce qui ne l’a pas été.

## Ce que contient le paquet

| Partie | Contenu |
|---|---|
| `design/` | Direction (cadrer, diriger, boucle d’édition, cinq règles), savoir (composition, typographie, couleur, styles, images et sources, contexte, techniques, qualité créative, écriture et contenu, points de départ mesurés), formes (supports, grilles, scènes, composants) et qualité du produit (premier rendu, plancher, finition, preuve visuelle, interface). |
| `SKILL.md`, `references/` | La skill : point d’entrée de l’agent (noyau commun) et ses références. Le paquet entier est le dossier de la skill. |
| `agent/` | Les chemins de l’agent par mode et la forme de sa réponse. |
| `gouvernance/` | Trace, statuts, vérification, clôture et structure ; schémas `RUN_CARD` et contrats de production, exemples, fixtures et validateurs. |
| `guides/` | Trois niveaux de maîtrise (utiliser, comprendre, maîtriser) et un glossaire. |
| `supports/` | Trois cartes du système (responsabilités, parcours d’un travail, boucle créer/apprendre) en HTML, SVG clair et sombre, et texte. |
| `scripts/` | Lecteur de routes, recette de rendu dans un navigateur, compilation du noyau, contrôles du paquet et construction des distributions. |
| `maintenance/` | Cette fiche, l’évolution du système et la préparation des livraisons. |
| `sections/` | Sections conservées à leur emplacement d’origine et carte de lecture ; même autorité que les sections rangées ailleurs. |

## Ce que le système sait faire

- **Classer un travail** en cinq modes (retouche, itération, écran cadré, direction, système) et ne charger que ce qui peut changer la décision.
- **Diriger une proposition** : premier objet, cible visuelle, alternative située, direction lisible dans le rendu.
- **Construire avec un contenu vrai** : exemples marqués plutôt qu’emplacements vides, sources et droits vérifiés au moment de l’intégration.
- **Observer et corriger** : boucle d’édition sur capture, recette de rendu automatisée pour les fautes objectivables (débordement, contraste, noms accessibles, clavier, cibles, mouvement réduit observé dès le chargement), avec comparaison à une mesure antérieure pour distinguer les défauts introduits, et relevés de composition facultatifs (`--mesures`), sans seuil ni verdict.
- **Tracer selon le besoin** : trace légère par défaut, trace complète et fiche `RUN_CARD` validable lorsqu’un travail est repris, partagé, audité ou accepté.
- **Retrouver un savoir** : lecteur de routes par code, adresse lisible, recherche ou connexions entre domaines.

## Compatibilité

Les codes historiques (`DIRECTION/START`) et les adresses lisibles (`agent/chemins#classer`) désignent les mêmes sections. Cette fiche est aussi accessible par `maintenance/versions` et `CHANGELOG`. Les distributions GitHub et Local ont la même arborescence ; Local est un export dérivé, sans les outils de construction. La skill suit le format ouvert Agent Skills ; son installation est décrite dans le README.

Une promotion, une dépréciation ou une migration décidée se reflète ici, dans l’état courant ; la règle de cycle de vie et le contrat de la décision sont dans `maintenance/evolution.md`.

## Pilotes en cours

Ajouts de cette révision, suivis comme candidats (`maintenance/evolution.md`, cycle de vie) : aucun n’est `ADOPTED`. Owner : mainteneur du corpus. Revue : avant 2027-04.

| Ajout | Statut | Périmètre et limite | Preuve exigée avant adoption | Retour arrière |
|---|---|---|---|---|
| `SAVOIR/CRAFT/CFT-06` — écriture et contenu | `PILOT` | Forme et spécificité du texte (budget de titre, formes de titre, actions, micro-typographie française) ; ne juge ni la justesse commerciale, ni la conformité légale, ni la conversion. | Contrat de gain réel (`BIBLIOTHEQUE/EVOLUTION`) : plusieurs runs contrastés avec et sans la route, baseline, observation et limite. | Retirer la section et son adresse lisible ; le noyau de la skill n’est pas touché. |
| `SAVOIR/TOOLS/POINTS-DE-DEPART` — mesures d’observation datées | Veille `[VEILLE 2026-10]`, claims `À REVÉRIFIER` | Ordres de grandeur tirés d’une étude de galeries notée par des modèles (source, limites et date dans la section) ; guident un essai local, n’imposent aucun seuil. | Remesure sur des rendus du paquet comparés à des rendus jugés par plusieurs personnes ; sans elle, ils restent des hypothèses de départ. | Retirer la section et son adresse lisible. |
| `scripts/check_render.py --mesures` | Option facultative | Relevés chiffrés de composition ; aucun statut, aucun code de sortie, aucun seuil. | Usage sur des runs réels avant de les lier à une règle ; leur concordance avec un autre outil de mesure a été vérifiée sur deux pages de test. | Retirer l’option, sa sonde et ses tests. |

Ces ajouts ont été exercés sur des pages de test et par les tests du paquet, non sur un run de design complet : pas d’adoption élargie avant cet essai (`ACTION/MAINTENANCE`, « Run réel »). Deux corrections de `check_render.py` accompagnent ces ajouts : le mouvement réduit enregistre les animations dès leur démarrage (une animation d’entrée courte qui ignorait la préférence passait auparavant sans réserve), et une icône SVG réduite à des formes sans nom accessible est un `RETURN` au lieu d’une réserve.

## Ce qui est vérifié, ce qui ne l’est pas

Le paquet contrôle sa cohérence : inventaire, liens et références, noyau compilé, schémas et fixtures, carte de lecture, lecteur de routes, fraîcheur des cartes et, dans le dépôt GitHub, reproductibilité des distributions. La recette de rendu et ses tests de pages demandent un navigateur.

**Efficacité : `NOT-VERIFIED`.** Aucune mesure comparative n’établit une amélioration générale de qualité, de variété ou de coût. Une validation du paquet ou d’une `RUN_CARD` confirme les contrôles exécutés ; elle ne remplace ni l’observation d’un rendu, ni un test utilisateur, ni une vérification d’accessibilité exécutée, ni une mesure de performance. Toute conclusion d’usage précise ce qui a été observé, par quelle méthode, dans quel scope et avec quelle limite.
