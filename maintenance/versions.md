# Ce que contient Design Governance V1.0.0

**Version expérimentale :** `V1.0.0`
**Statut expérimental :** Design Governance V1.0.0 est une expérimentation maintenue.  
**Révision :** `R2026-10-16`, 16 octobre 2026.  
**Usage recommandé :** pilote avec revue humaine et preuves adaptées au risque.

Cette fiche décrit ce que le système possède aujourd’hui et ce qui en est vérifié. Elle ne retrace pas son histoire.

## Ce que fait le système

Design Governance aide un agent, ou une personne, à concevoir des pages, des écrans et des identités visuelles qui ont une direction, qui sont construits et soignés dès la première proposition, puis à les améliorer en regardant le rendu. Quand un travail doit être repris, livré ou accepté, il garde la trace de ce qui a été vérifié et de ce qui ne l’a pas été.

## Ce que contient le paquet

| Partie | Contenu |
|---|---|
| `design/` | Direction (cadrer, diriger, boucle d’édition, cinq règles), savoir (composition, typographie, couleur, styles, images et sources, contexte, techniques, qualité créative, écriture et contenu), formes (supports, grilles, scènes, composants) et qualité du produit (premier rendu, plancher, finition, preuve visuelle, interface). |
| `SKILL.md`, `references/` | La skill : point d’entrée de l’agent (noyau commun) et ses références. Le paquet entier est le dossier de la skill. |
| `agent/` | Les chemins de l’agent par mode et la forme de sa réponse. |
| `gouvernance/` | Trace, statuts, vérification, clôture et structure ; schémas `RUN_CARD` et contrats de production, exemples, fixtures et validateurs. |
| `guides/` | Trois niveaux de maîtrise (utiliser, comprendre, maîtriser) et un glossaire. |
| `supports/` | Trois cartes du système (responsabilités, parcours d’un travail, boucle créer/apprendre) en HTML, SVG clair et sombre, et texte. |
| `scripts/` | Lecteur de routes, recette de rendu dans un navigateur, compilation du noyau, contrôles du paquet et construction des distributions. |
| `maintenance/` | Cette fiche, l’évolution du système et la préparation des livraisons. |
| `sections/` | Sections propriétaires regroupées par domaine (ACTION, BIBLIOTHEQUE, DIRECTION, SAVOIR) et carte de lecture ; même autorité que les autres sections. |

## Ce que le système sait faire

- **Classer un travail** en cinq modes (retouche, itération, écran cadré, direction, système), lire le noyau de fabrication (premier objet, composition, typographie, couleur, boucle d’édition), puis le tronc de son mode (routes lues à chaque run, sous un budget de 30 000 caractères, `read_route.py --tronc`) ; le reste se charge quand son signal apparaît.
- **Diriger une proposition** : premier objet, cible visuelle, alternative située, direction lisible dans le rendu ; une reprise se compare à ses antécédents sur six champs (teinte, paire typographique, ossature, objet de preuve, thèse, registre).
- **Construire avec un contenu vrai** : exemples marqués plutôt qu’emplacements vides, données et graphiques d’exemple cohérents, sources et droits vérifiés au moment de l’intégration, provenance des images générées conservée.
- **Protéger la personne** : dans les flux d’inscription, de paiement, de consentement ou de résiliation, refuser reste aussi visible et aussi court qu’accepter ; une culture se calibre par des références locales nommées, jamais par un registre régional générique.
- **Choisir ses moyens** : une carte datée nomme, par couche, des sources gratuites avec leurs restrictions connues : bases techniques, typographie, couleur, icônes, composants, mouvement et 3D, données et cartes, textures, photographie, illustration, références à observer. Une ressource nommée n’est ni atteinte ni vérifiée ; sa licence se relit au moment de l’intégrer.
- **Construire sur le socle des navigateurs** : un levier encore limité à un ou deux moteurs s’ajoute en amélioration progressive, avec un repli qui garde la direction lisible.
- **Observer et corriger** : boucle d’édition sur capture, recette de rendu automatisée pour les fautes objectivables (débordement, contraste, noms accessibles, clavier, cibles, images visibles qui ne se chargent pas, contraste du focus dans les cas lisibles, mouvement réduit observé dès le chargement, textes qui se recouvrent ou sont tronqués) ; preuve à l’état qui compte, après clic et attente : assertions sur un texte calculé (`--assert`) et objet de l’état clé dans son cadre (`--in-frame`) ; comparaison à une mesure antérieure pour distinguer les défauts introduits, et relevés de composition facultatifs (`--mesures`), sans seuil ni verdict.
- **Tracer selon le besoin** : trace légère par défaut, trace complète et fiche `RUN_CARD` validable lorsqu’un travail est repris, partagé, audité ou accepté.
- **Retrouver un savoir** : lecteur de routes par code, adresse lisible, recherche ou connexions entre domaines.

## Compatibilité

Les codes de route (`DIRECTION/START`) et les adresses lisibles (`agent/chemins#classer`) désignent les mêmes sections. Cette fiche est aussi accessible par `maintenance/versions` et `CHANGELOG`. Les distributions GitHub et Local ont la même arborescence ; Local est un export dérivé, sans les outils de construction. La skill suit le format ouvert Agent Skills ; son installation est décrite dans le README.

Une promotion, une dépréciation ou une migration décidée se reflète ici, dans l’état courant ; la règle de cycle de vie et le contrat de la décision sont dans `maintenance/evolution.md`.

## Sections à l’essai

Ces sections et cette option sont des essais, suivis selon le cycle de vie de `maintenance/evolution.md` : aucune n’est adoptée. Owner : mainteneur du corpus ; revue avant 2027-04. Elles sont couvertes par les tests du paquet, pas encore éprouvées sur un run de design complet (`ACTION/MAINTENANCE`, « Run réel »).

| Section | Statut | Ce qu’elle couvre, et sa limite | Preuve attendue avant adoption | Retrait |
|---|---|---|---|---|
| `SAVOIR/CRAFT/CFT-06` — écriture et contenu | `PILOT` | Forme et spécificité du texte : argument, budget et formes de titre, actions, micro-typographie française. Ne juge ni la justesse commerciale, ni la conformité légale, ni la conversion. | Contrat de gain réel (`BIBLIOTHEQUE/EVOLUTION`) : runs contrastés avec et sans la route, référence, observation et limite. | Retirer la section et son adresse lisible. |
| `SAVOIR/CRAFT/CFT-01` — « Inventaire du sujet et phrase d’idée » | `PILOT` | Trouver l’idée dans ce que le sujet a de propre : inventaire, phrase d’idée, test du concurrent, une chose vivante. Ne garantit ni la qualité ni une préférence ; ne remplace ni `MODAL` ni le test de singularité. | Contrat de gain réel : runs contrastés avec et sans la procédure. | Retirer la sous-section. |
| `SAVOIR/CRAFT/CFT-00` — « Mouvement » | Question de revue | Qu’est-ce qui bouge, et pourquoi ? Sans quota ni seuil ; ne dit pas que le mouvement améliore une page. | Runs contrastés : la page qui doit se montrer a-t-elle un mouvement justifié, sans mouvement ajouté là où il n’a pas d’usage ? | Retirer le paragraphe. |
| `SAVOIR/CRAFT/CFT-05` — « Relations de couleur » | `PILOT` | Fixer un rôle par sa luminosité (OKLCH), nommer la relation d’une palette, fonds voisins, neutres teintés, fond sombre. Repères établis sur des neutres ; WCAG reste le critère. | Runs contrastés : contrastes tenus là où les accents servent, fonds voisins distincts par la luminosité. | Retirer la sous-section. |
| `BIBLIOTHEQUE/READ` « Traduire un caractère en leviers » | Valeurs `[À ADAPTER]` | Leviers de départ et piège réflexe pour douze caractères perceptuels (calme, tension, intimité…). Servi par sa route, hors du noyau. | Runs contrastés avec et sans le tableau : le caractère visé se lit-il dans le rendu sans tomber dans le piège réflexe ? | Retirer le tableau et sa ligne dans l’index des signaux. |
| `SAVOIR/TYPE` « Réglage d’un grand texte » et `SAVOIR/CONTEXT` « Durées et courbes, points de départ » | Valeurs `[À ADAPTER]` | Points de départ, non des mesures, pour régler un grand titre et calibrer un mouvement ; chacun porte ses contre-indications et sa preuve. | Essais sur des rendus du paquet jugés par plusieurs personnes. | Retirer les deux paragraphes. |
| `SAVOIR/SOURCE` « Chercher le monde du sujet dans des collections ouvertes » | `PILOT` | Requêtes tirées de l’inventaire du sujet, critères de choix, honnêteté, droits. Ne remplace ni la fiche de source ni un avis juridique ; aucun accès n’est testé par le paquet. | Contrat de gain réel, accès atteint depuis l’environnement du run, droits relus. | Retirer la sous-section et sa mention dans `MOYENS`. |
| `DIRECTION/CHARGE` — tronc par mode | `PILOT` | Routes lues à chaque run d’un mode, sous un budget de 30 000 caractères. En `DIRECTION`, les contraintes de `ACTION/GATE-A` restent hors du tronc pour tenir le budget : elles se lisent dès qu’elles s’appliquent, avant le choix qu’elles protègent. | Runs réels : le tronc suffit-il à fabriquer sans lecture manquée d’une contrainte ? | Retirer les mentions « Tronc » de la table et l’option `--tronc`. |
| `scripts/check_render.py --mesures` | Option facultative | Relevés chiffrés de composition : titres et textes, gros textes du premier écran couverts ou au haut rogné, palette en OKLCH, actions et navigation du premier écran. Aucun statut, aucun seuil, aucun effet sur le code de sortie. | Usage sur des runs réels avant de lier un relevé à une règle. | Retirer l’option ; les contrôles restent inchangés. |

Le noyau de la skill ne dépend d’aucune de ces sections : leur retrait ne le modifie pas.

## Ce qui est vérifié, ce qui ne l’est pas

Le paquet contrôle sa cohérence : inventaire, liens et références, noyau compilé, schémas et fixtures, carte de lecture, lecteur de routes, fraîcheur des cartes et, dans le dépôt GitHub, reproductibilité des distributions. La recette de rendu et ses tests de pages demandent un navigateur.

**Efficacité : `NOT-VERIFIED`.** Aucune mesure comparative n’établit une amélioration générale de qualité, de variété ou de coût. Une validation du paquet ou d’une `RUN_CARD` confirme les contrôles exécutés ; elle ne remplace ni l’observation d’un rendu, ni un test utilisateur, ni une vérification d’accessibilité exécutée, ni une mesure de performance. Toute conclusion d’usage précise ce qui a été observé, par quelle méthode, dans quel scope et avec quelle limite.
