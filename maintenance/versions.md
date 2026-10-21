# Ce que contient Design Governance V1.0.0

**Version expérimentale :** `V1.0.0`
**Statut expérimental :** Design Governance V1.0.0 est une expérimentation maintenue.  
**Révision :** `R2026-10-21.2`, 21 octobre 2026.  
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
| `scripts/` | Lecteur de routes, recettes de rendu et de caractère dans un navigateur, gestes servis, outils du regard (registre des choix, spécimen, planche), journal de mobilisation, compilation du noyau, contrôles du paquet et construction des distributions. |
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
- **Servir le savoir au moment utile** : trois cartes de moment (avant le build, après une capture, avant de proposer ; `read_route.py --moment`) rangent des routes existantes à leur rendez-vous ; sous leurs signaux, les deux recettes servent le geste lié du tableau de `SAVOIR/STATE`.
- **Rendre la convergence et la finition visibles** : registre local des choix d’un run à l’autre (polices réellement rendues, fond, accent), spécimen du vrai titre dans plusieurs voix, planche de correction humaine nommée pour la dernière finition.
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
| `SAVOIR/CRAFT/CFT-05` — « Relations de couleur » | `PILOT` | Fixer un rôle par sa luminosité (OKLCH), nommer la relation d’une palette, fond accordé et figure contrastée, fonds voisins, neutres teintés, fond sombre ; études de paires et de palettes citées (Schloss et Palmer, O’Donovan, Tan), pas d’interfaces. Repères établis sur des neutres ; WCAG reste le critère. | Runs contrastés : contrastes tenus là où les accents servent, fonds voisins distincts par la luminosité. | Retirer la sous-section. |
| `BIBLIOTHEQUE/READ` « Traduire un caractère en leviers » | Valeurs `[À ADAPTER]` | Leviers de départ et piège réflexe pour douze caractères perceptuels (calme, tension, intimité…). Servi par sa route, hors du noyau. | Runs contrastés avec et sans le tableau : le caractère visé se lit-il dans le rendu sans tomber dans le piège réflexe ? | Retirer le tableau et sa ligne dans l’index des signaux. |
| `SAVOIR/TYPE` « Réglage d’un grand texte » et `SAVOIR/CONTEXT` « Durées et courbes, points de départ » | Valeurs `[À ADAPTER]` | Points de départ, non des mesures, pour régler un grand titre et calibrer un mouvement ; chacun porte ses contre-indications et sa preuve. | Essais sur des rendus du paquet jugés par plusieurs personnes. | Retirer les deux paragraphes. |
| `SAVOIR/SOURCE` « Chercher le monde du sujet dans des collections ouvertes » | `PILOT` | Requêtes tirées de l’inventaire du sujet, critères de choix, honnêteté, droits. Ne remplace ni la fiche de source ni un avis juridique ; aucun accès n’est testé par le paquet. | Contrat de gain réel, accès atteint depuis l’environnement du run, droits relus. | Retirer la sous-section et sa mention dans `MOYENS`. |
| `DIRECTION/CHARGE` — tronc par mode | `PILOT` | Routes lues à chaque run d’un mode, sous un budget de 35 000 caractères. Invariant : une route bloquante citée dans la ligne d’un mode (`ACTION/GATE-A`) est dans son tronc ; le budget se règle sur l’explicatif, jamais sur une contrainte bloquante. La notice de `check_render.py` vit dans `ACTION/RECETTE-RENDU`, hors du tronc. Le tronc `DIRECTION` occupe 98 % de ce budget : un ajout s’y compense par un allègement du même tronc ; `--tronc` affiche la marge et la signale sous 10 %. | Runs réels : le tronc suffit-il à fabriquer sans lecture manquée d’une contrainte ? | Retirer les mentions « Tronc » de la table et l’option `--tronc`. |
| `ACTION/RECETTE-CARACTERE` — recette de caractère | `PILOT` | Confronte le caractère déclaré au rendu : polices, densité et matière en signal ; foyer, intensité et vide en relevé. Bornes provisoires, figées entre deux recalibrations par lot ; ne mesure ni le goût ni le caractère générique. | Signaux qui changent des décisions sur au moins cinq runs réels qui n’ont pas servi à régler les bornes. Une calibration sur le jugement du mainteneur peut régler les bornes ; elle ne valide pas la recette. | Retirer `scripts/check_caractere.py` et sa route ; les autres contrôles restent inchangés. |
| `scripts/journal_mobilisation.py` — journal de mobilisation | `PILOT` | Passif, activé par `DG_JOURNAL` : routes lues ou proposées, appels des recettes et leurs résultats, puis fiche de mobilisation. Observe des lectures et des appels, ni l’attention de l’agent, ni l’application d’une route, ni les ressources cherchées hors des outils du paquet. | Fiches qui permettent, sur des runs réels, de relier une réussite ou un échec à ce qui a été mobilisé ou manqué. | Retirer le script, son test et les trois appels ; les outils restent inchangés. |
| `DIRECTION/CHARGE` — cartes de moment | `PILOT` | Trois rendez-vous (avant, regard, sortie) servent des routes existantes au moment utile (`read_route.py --moment`) ; la fiche de mobilisation signale une carte sautée en `DIRECTION`. Range des lectures, ne prouve pas qu’une route est appliquée. | État de référence rejoué : lectures des routes du regard en hausse, réserves de Gate C restantes en baisse, coût en jetons comparable. | Retirer la table, l’option `--moment`, la phrase des rendez-vous du bloc `CHARGE-REGLE` (noyau) et le contrôle de la fiche. |
| `scripts/gestes.py` — gestes servis par les recettes | `PILOT` | Sous les signaux de `check_render.py` et `check_caractere.py`, la ligne liée du tableau de `SAVOIR/STATE`, lue dans sa source : trois au maximum, rappelée seulement si déjà servie dans le journal ; `--sans-gestes` la retire. Un geste servi est un point de départ, pas une correction. | Gestes servis suivis d’une modification observable de l’artefact sur des runs réels. | Retirer le module, son test, les deux appels et la phrase du bloc `BOUCLE` (noyau). |
| `scripts/registre_choix.py`, `scripts/specimen.py`, `scripts/planche.py` — outils du regard | `PILOT` | Registre local des choix (police du titre, fichiers de police rendus, fond, accent) et convergence d’un run à l’autre ; spécimen du vrai titre dans plusieurs voix avec repli signalé ; planche de correction humaine nommée. Rien n’est écrit sans fichier choisi ; aucun statut, aucun seuil. | Registre qui change une décision de convergence ; spécimen consulté avant le choix d’une voix ; correction de planche reliée à la modification suivante. | Retirer les trois scripts, leur test et leurs mentions (`CFT-05`, `SAVOIR/TYPE`, `SAVOIR/TOOLS/CONVERGENCE`, `DIRECTION/DOUBLE-LOOP`). |
| `DIRECTION/DOUBLE-LOOP` — « Regard humain sur la dernière finition » | `PILOT` | Quand deux tours ne changent plus la relation visée, ou que la finition restante est perceptive, une planche demande une correction nommée, après le geste tenté. Ne prouve ni l’usage, ni l’accessibilité, ni la qualité. | Corrections reçues qui changent l’artefact, comparées aux tours autonomes. | Retirer la sous-section et sa ligne dans la carte « sortie ». |
| `SAVOIR/SYSTEM` — « Identité dans la durée » | `PILOT` | Élément signature et ses états, forme constante pendant qu’il s’installe, force mesurée auprès du public sans nom ni logo. Ne remplace pas une étude de marque. | Run `SYSTÈME` où la notion change une décision de continuité. | Retirer le paragraphe. |
| `scripts/check_render.py --mesures` | Option facultative | Relevés chiffrés de composition : titres et textes, gros textes du premier écran couverts ou au haut rogné, palette en OKLCH, actions et navigation du premier écran. Aucun statut, aucun seuil, aucun effet sur le code de sortie. | Usage sur des runs réels avant de lier un relevé à une règle. | Retirer l’option ; les contrôles restent inchangés. |

Le noyau de la skill ne dépend d’aucune de ces sections, sauf deux phrases (les rendez-vous de moment dans `CHARGE-REGLE`, les gestes servis dans `BOUCLE`) et deux renvois aux outils du regard dans `COMP-CONVERGENCE`, que leur retrait supprime aussi.

## Ce qui est vérifié, ce qui ne l’est pas

Le paquet contrôle sa cohérence : inventaire, liens et références, noyau compilé, schémas et fixtures, carte de lecture, lecteur de routes, fraîcheur des cartes et, dans le dépôt GitHub, reproductibilité des distributions. La recette de rendu et ses tests de pages demandent un navigateur.

**Efficacité : `NOT-VERIFIED`.** Aucune mesure comparative n’établit une amélioration générale de qualité, de variété ou de coût. Une validation du paquet ou d’une `RUN_CARD` confirme les contrôles exécutés ; elle ne remplace ni l’observation d’un rendu, ni un test utilisateur, ni une vérification d’accessibilité exécutée, ni une mesure de performance. Toute conclusion d’usage précise ce qui a été observé, par quelle méthode, dans quel scope et avec quelle limite.
