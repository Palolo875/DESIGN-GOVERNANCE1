# Run 7 — atelier de lutherie (condition C)

**Système :** skill en révision `R2026-10-21.2`, commit `ff865cd`. **Agent :** session neuve, skill seule, sans contenu fourni. **Brief :** « Il me faut un site pour mon atelier de lutherie. » **Journal :** actif. **Registre :** les huit productions précédentes de l’état de référence, plus une entrée de test.

Le caractère attendu par l’évaluateur (`evaluateur/caractere-7.json`) a été écrit avant de voir la production.

## Ce que la production montre

| Piège attendu | Observé |
|---|---|
| Fond crème et serif de labeur, dominants dans le registre | Évité : fond gris froid `#e9edf0`, encre bleue, titres en Barlow Semi Condensed. Le registre ne relève aucun choix partagé avec les huit productions précédentes. |
| Bois ou photo de banque d’images | Évité : coupe dessinée en SVG ; l’emplacement photo est vide et marqué « à fournir ». |
| Contenus inventés présentés comme réels | Évité : nom, adresse, numéro (plage fictive), e-mail (`.example`), horaires et délais sont marqués « exemple ». Un bandeau le dit aussi en tête de page. |
| Trame héros → services → avis → contact | Rompue : coupe → diagnostic par symptôme → travaux en registre → tailles → venir → étiquette. |
| Reprise de l’exemple de l’atelier de vélos | Non reprise : la séquence est suivie, mais aucune décision visuelle n’est copiée. |

Objet de preuve : la coupe au chevalet. Choisir un symptôme surligne l’endroit concerné sur la coupe et ouvre un e-mail prérempli ; l’état au clic est prouvé avec `--assert` et `--in-frame`.

Recette de rendu (relancée après correction de la recette) : aucun RETURN à 390, 768 et 1440 px. Restent des réserves : texte SVG non mesuré, noms accessibles calculés non vérifiés.

Recette de caractère face au caractère attendu, que l’agent n’a pas lancée :
- un SIGNAL de densité à 390 px (respiration attendue, rendu compressé) ;
- un relevé de foyer : la coupe capte 14 à 18 % de la saillance pour 24 % de la surface.

Défaut dominant restant, selon l’agent : le chevalet est lourd, les bords de la table se lisent comme deux ailes séparées, et l’emplacement photo reste vide. Aucune recette ne voit ce défaut ; c’est l’objet de la planche.

## Mobilisation

| Élément | Consultation | Conséquence observée |
|---|---|---|
| Tronc `DIRECTION`, `EXTERNAL-START` | lus | Prise de brief sans contenu ; trois demandes dans la réponse ; contenus marqués |
| Carte « avant » (inventaire, signaux, séquence, relations de couleur) | lue | Inventaire du sujet → l’âme et la coupe ; trame rompue |
| Registre des choix (`--lire`) | lu avant la direction | Écart assumé du crème et de l’orange, cités par l’agent (crème ×6, orange ×4) |
| `SAVOIR/TOOLS/CONVERGENCE` | lue | Marqueurs de vague datés nommés dans la trace |
| Spécimen | 3 voix comparées | Choix de Barlow Semi Condensed justifié, Spectral en contre-choix |
| `check_render`, quatre passages | gestes servis au premier (Gestion du vide, États), puis retirés (`--sans-gestes`) | Focus rendu visible (1,89:1 corrigé), cibles portées à 44 px, titre recoupé selon le sens |
| Carte « regard » | **jamais ouverte**, malgré trois tours de correction | Le manque est signalé par la fiche |
| Carte « sortie » | lue à la fin | Réponse structurée : décision demandée, contenus manquants, suite |
| Recette de caractère | non lancée, aucun caractère déclaré | — |
| Planche | non utilisée ; demande de correction faite dans la réponse | Conforme à la contre-indication : la personne lira la réponse |

## Défauts d’outils révélés et corrigés

1. **Objet de preuve mesuré pendant un défilement doux.** Sur une page en `scroll-behavior: smooth`, la recette remontait en haut puis mesurait aussitôt : l’intersection variait d’un passage à l’autre (0 px ou la hauteur entière). Le défilement est désormais immédiat. La page `defile_doux.html` est ajoutée aux tests.
2. **Volets `<details>` fermés pris pour un chevauchement.** Leur texte n’est pas rendu, mais `getBoundingClientRect` le place sur le contenu suivant. La recette écarte maintenant ce que `checkVisibility()` dit non rendu. La page `volets.html` est ajoutée aux tests.
3. **Police du corps mal relevée par le registre.** Le registre prenait le premier paragraphe de 40 caractères, ici le bandeau « Maquette » en Barlow ; il prend maintenant le plus long texte courant visible. Un test le vérifie.
4. **Outils du regard absents du journal.** Le registre, le spécimen et la planche n’écrivaient rien dans le journal : la fiche ne les voyait pas. Ils y écrivent maintenant, et la fiche signale aussi des gestes retirés par `--sans-gestes`.

## Remarques de l’agent à décider

- **Volume de lecture avant le premier pixel :** noyau, tronc proche du budget, cartes, routes. Le journal montre pourtant les lectures groupées en 30 secondes ; le coût est en contexte, pas en temps.
- **Format de la trace légère :** « six lignes au plus », mais la déclaration de l’absolu 4 (mode, décision, risque, preuve, arrêt) doit aussi y tenir. Les lignes deviennent très longues.
- **Marqueurs de convergence :** ils couvrent presque tous les partis courants, ce qui pousse à justifier chaque choix contre une liste plutôt qu’à concevoir.
- **Hypothèse structurante sans réponse possible :** quatuor ou guitare change toute la page. La skill ne dit que de la nommer.
- **Justesse métier d’un schéma dessiné :** aucune aide ; c’est la limite connue du regard autonome.
