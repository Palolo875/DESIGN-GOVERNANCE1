# Ce que contient Design Governance V1.0.0

**Version expérimentale :** `V1.0.0`
**Statut expérimental :** Design Governance V1.0.0 est une expérimentation maintenue.  
**Révision :** `R2026-10-23`, 23 octobre 2026.  
**Usage recommandé :** pilote avec revue humaine et preuves adaptées au risque.

Cette fiche décrit ce que le système possède aujourd’hui et ce qui en est vérifié. Elle ne retrace pas son histoire.

## Ce que fait le système

Design Governance aide un agent, ou une personne, à concevoir des pages, des écrans et des identités visuelles qui ont une direction, qui sont construits et soignés dès la première proposition, puis à les améliorer en regardant le rendu. Quand un travail doit être repris, livré ou accepté, il garde la trace de ce qui a été vérifié et de ce qui ne l’a pas été.

## Cap

| Niveau | Contenu |
|---|---|
| **Utilité** | Aider une personne ou un agent à transformer une demande en réalisation de design pertinente, avec une vraie direction, construite et soignée dès la première proposition, puis améliorée à partir du rendu réel ; analyser et corriger un existant. |
| **Objectif** | Obtenir un niveau élevé plus régulièrement, avec moins d’oublis, de tâtonnements et de reprises inutiles : esthétique, identité, usage et solidité de l’exécution. |
| **Hypothèse à éprouver** | Le système oriente-t-il les choix ? Mobilise-t-il les bons moyens ? Conduit-il au niveau visé ? Chaque question se juge par comparaison avec un travail fait sans lui, sur des demandes comparables. |

Aucune comparaison de ce type n’a encore été faite : l’efficacité reste `NOT-VERIFIED` (voir plus bas). Toute évolution du système dit quelle question elle sert et comment on le saura.

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
| `sections/` | Sections regroupées par domaine (ACTION, BIBLIOTHEQUE, DIRECTION, SAVOIR) et carte de lecture. Chaque fichier ne contient qu’une partie de sa responsabilité ; un bandeau généré depuis `LIEUX` liste en tête les fichiers et routes qui portent le reste. |

## Ce que le système sait faire

- **Classer un travail** en cinq modes (retouche, itération, écran cadré, direction, système), lire le noyau de fabrication (premier objet, composition, typographie, couleur, boucle d’édition), puis le tronc de son mode (routes lues à chaque run, sous un budget de 35 000 caractères, `read_route.py --tronc`) ; le reste se charge quand son signal apparaît.
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

**Contrats de projection.** Dans une `RUN_CARD`, le champ `direction` porte la thèse, le modal (`direction.modal`), le parti (`direction.parti`), la trame modale facultative (`direction.trame`) et le premier objet ; une fiche qui porte l’ancien champ `anti_direction` est refusée avec l’indication de conversion (son premier élément devient `modal`, la décision prise face à lui devient `parti`). Le contrat `EVALUATION_CASE` porte la condition (avec ou sans le système), la campagne et le cas apparié, l’évaluateur et son indépendance ; un gain affirmé y cite sa référence, sinon le validateur le refuse.

## Sections à l’essai

Ces sections et cette option sont des essais, suivis selon le cycle de vie de `maintenance/evolution.md` : aucune n’est adoptée. Owner : mainteneur du corpus ; revue avant 2027-04. Elles sont couvertes par les tests du paquet, pas encore éprouvées sur un run de design complet (`ACTION/MAINTENANCE`, « Run réel »).

| Section | Statut | Ce qu’elle couvre, et sa limite | Preuve attendue avant adoption | Retrait |
|---|---|---|---|---|
| `SAVOIR/CRAFT/CFT-06` — écriture et contenu | `PILOT` | Forme et spécificité du texte : argument, budget et formes de titre, actions, micro-typographie française. Ne juge ni la justesse commerciale, ni la conformité légale, ni la conversion. | Contrat de gain réel (`BIBLIOTHEQUE/EVOLUTION`) : runs contrastés avec et sans la route, référence, observation et limite. | Retirer la section et son adresse lisible. |
| `SAVOIR/TYPE-VOIX` — trouver, apparier et comparer des voix typographiques | Méthode | Chercher des candidats par construction, filtrer, apparier, comparer sur le vrai titre, trancher par la thèse. Ne cite aucune police et ne garantit pas une meilleure voix. | Runs contrastés : la voix retenue diffère-t-elle du réflexe que la question de convergence nomme pour la police de titre, et sert-elle le titre réel ? | Retirer la sous-route et son renvoi dans le noyau. |
| `SAVOIR/CRAFT/CFT-01` — « Inventaire du sujet et phrase d’idée » | `PILOT` | Trouver l’idée dans ce que le sujet a de propre : inventaire, phrase d’idée, test du concurrent, une chose vivante. Ne garantit ni la qualité ni une préférence ; ne remplace ni `MODAL` ni le test de singularité. | Contrat de gain réel : runs contrastés avec et sans la procédure. | Retirer la sous-section. |
| `SAVOIR/CRAFT/CFT-00` — « Mouvement » | Question de revue | Qu’est-ce qui bouge, et pourquoi ? Sans quota ni seuil ; ne dit pas que le mouvement améliore une page. | Runs contrastés : la page qui doit se montrer a-t-elle un mouvement justifié, sans mouvement ajouté là où il n’a pas d’usage ? | Retirer le paragraphe. |
| `SAVOIR/CRAFT/CFT-05` — « Relations de couleur » | `PILOT` | Fixer un rôle par sa luminosité (OKLCH), nommer la relation d’une palette, fonds voisins, neutres teintés, fond sombre. Repères établis sur des neutres ; WCAG reste le critère. | Runs contrastés : contrastes tenus là où les accents servent, fonds voisins distincts par la luminosité. | Retirer la sous-section. |
| `BIBLIOTHEQUE/READ` « Traduire un caractère en leviers » | Valeurs `[À ADAPTER]` | Leviers de départ et piège réflexe pour douze caractères perceptuels (calme, tension, intimité…). Servi par sa route, hors du noyau. | Runs contrastés avec et sans le tableau : le caractère visé se lit-il dans le rendu sans tomber dans le piège réflexe ? | Retirer le tableau et sa ligne dans l’index des signaux. |
| `SAVOIR/TYPE` « Réglage d’un grand texte » et `SAVOIR/CONTEXT` « Durées et courbes, points de départ » | Valeurs `[À ADAPTER]` | Points de départ, non des mesures, pour régler un grand titre et calibrer un mouvement ; chacun porte ses contre-indications et sa preuve. | Essais sur des rendus du paquet jugés par plusieurs personnes. | Retirer les deux paragraphes. |
| `SAVOIR/SOURCE` « Chercher le monde du sujet dans des collections ouvertes » | `PILOT` | Requêtes tirées de l’inventaire du sujet, critères de choix, honnêteté, droits. Ne remplace ni la fiche de source ni un avis juridique ; aucun accès n’est testé par le paquet. | Contrat de gain réel, accès atteint depuis l’environnement du run, droits relus. | Retirer la sous-section et sa mention dans `MOYENS`. |
| `DIRECTION/CHARGE` — tronc par mode | `PILOT` | Routes lues à chaque run d’un mode, sous un budget de 35 000 caractères. Invariant : une route bloquante citée dans la ligne d’un mode (`ACTION/GATE-A`) est dans son tronc ; le budget se règle sur l’explicatif, jamais sur une contrainte bloquante. La notice de `check_render.py` vit dans `ACTION/RECETTE-RENDU`, hors du tronc. Le tronc `DIRECTION` approche ce budget : un ajout s’y compense par un allègement du même tronc ; `--tronc` affiche sa taille et sa marge, et signale une marge sous 10 %. | Runs réels : le tronc suffit-il à fabriquer sans lecture manquée d’une contrainte ? | Retirer les mentions « Tronc » de la table et l’option `--tronc`. |
| `ACTION/RECETTE-CARACTERE` — recette de caractère | `PILOT` | Confronte le caractère déclaré au rendu : polices, densité et matière en signal ; foyer, intensité et vide en relevé. Bornes provisoires, figées entre deux recalibrations par lot ; ne mesure ni le goût ni le caractère générique. | Signaux qui changent des décisions sur au moins cinq runs réels qui n’ont pas servi à régler les bornes. Une calibration sur le jugement du mainteneur peut régler les bornes ; elle ne valide pas la recette. | Retirer `scripts/check_caractere.py` et sa route ; les autres contrôles restent inchangés. |
| `scripts/journal_mobilisation.py` — journal de mobilisation | `PILOT` | Passif, activé par `DG_JOURNAL` : routes lues ou proposées, appels des recettes et leurs résultats, puis fiche de mobilisation. Observe des lectures et des appels, ni l’attention de l’agent, ni l’application d’une route, ni les ressources cherchées hors des outils du paquet. | Fiches qui permettent, sur des runs réels, de relier une réussite ou un échec à ce qui a été mobilisé ou manqué. | Retirer le script, son test et les trois appels ; les outils restent inchangés. |
| `scripts/check_render.py --mesures` | Option facultative | Relevés chiffrés de composition : titres et textes, gros textes du premier écran couverts ou au haut rogné, palette en OKLCH, actions et navigation du premier écran. Aucun statut, aucun seuil, aucun effet sur le code de sortie. | Usage sur des runs réels avant de lier un relevé à une règle. | Retirer l’option ; les contrôles restent inchangés. |

Le noyau de la skill ne dépend d’aucune de ces sections : leur retrait ne le modifie pas.

## Ce qui est vérifié, ce qui ne l’est pas

Le paquet contrôle sa cohérence : inventaire, liens et références, noyau compilé, atteignabilité des règles, planchers des obligations `[REQUIS]`, schémas et fixtures, carte de lecture, lecteur de routes, fraîcheur des cartes et, dans le dépôt GitHub, reproductibilité des distributions. La recette de rendu et ses tests de pages demandent un navigateur.

**Efficacité : `NOT-VERIFIED`.** Aucune mesure comparative n’établit une amélioration générale de qualité, de variété ou de coût. Les seules observations avec et sans le système ne montrent aucune différence, sur un point précis : en septembre 2026, 6 rendus sur 6 sont sortis sur la même palette (fond crème et brun), avec ou sans système ; et sur un même brief, 6 rendus ont repris le même objet central et la même grotesque de titre, avec ou sans système. Ce sont des essais internes, peu nombreux, jugés par leur auteur (`SAVOIR/TOOLS/CONVERGENCE`). Ils ne mesurent pas l’effet du système ; ils indiquent que, sur la palette et la police de titre par défaut, aucune différence n’a été observée. Une première comparaison a suivi, en octobre 2026 : huit briefs contrastés, un run avec et un run sans le système, par des agents d’un même modèle, jugés à l’aveugle. Le juge automatique a préféré les rendus faits avec le système sur les huit briefs ; la personne qui pilote le système, sur les quatre briefs qu’elle a notés, a préféré trois fois le rendu fait sans lui. Aucun gain n’est donc établi. Avec le système, un run a coûté environ 1,7 fois plus de jetons et trois à quatre fois plus de temps. Limites : un run par condition, un seul juge humain, non indépendant, et un juge automatique de la même famille que les agents. Une validation du paquet ou d’une `RUN_CARD` confirme les contrôles exécutés ; elle ne remplace ni l’observation d’un rendu, ni un test utilisateur, ni une vérification d’accessibilité exécutée, ni une mesure de performance. Toute conclusion d’usage précise ce qui a été observé, par quelle méthode, dans quel scope et avec quelle limite.
