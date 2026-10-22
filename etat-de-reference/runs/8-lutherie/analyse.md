# Run 8 — atelier de lutherie, comparé au run 7

**Système :** skill en révision `R2026-10-22.3`, commit `d71159e` (étapes 1 à 3 appliquées). **Run 7 :** révision `R2026-10-21.2`, commit `ff865cd`.

**Mêmes conditions que le run 7 :** brief, consigne mot pour mot, registre de départ (neuf entrées) et caractère attendu de l'évaluateur. Agent neuf, sans contenu fourni. Seul le système change.

## Mobilisation

| Élément | Run 7 | Run 8 |
|---|---|---|
| Carte « avant » | lue | lue, avec « Chercher » (`SAVOIR/SOURCE`) et « Vignettes » |
| Références observées | aucune recherche | six sources de contenu consultées (tarifs de location, tableaux de tailles, annuaires) ; aucune ancre visuelle : Wikimedia a répondu 429 et l'API de recherche du Met est retirée ; limite déclarée, proposition `EXPLORATORY` |
| Vignettes | — | lues ; alternative formulée en texte (ouvrir sur la location), non matérialisée |
| Carte « regard » | jamais ouverte | ouverte juste après le premier défaut bloquant (rappel T1) |
| Gestes servis | servis une fois, puis retirés par `--sans-gestes` | « Masse visuelle » servi par la recette de caractère et appliqué (titre de 96 à 84 px, plan élargi), puis retirés par `--sans-gestes` sur sept passages sur neuf |
| Recette de caractère | non lancée | lancée, déclaration écrite après le premier build (l'agent le signale comme écart) |
| Moment fort | — | la carte « sortie » sert la question ; la page a son moment de champ : le même violon à sept tailles, à l'échelle |
| Planche | non faite (demande dans la réponse) | faite, avec le défaut restant et deux gestes essayés |
| Preuve d'état | état au clic prouvé | état au clic prouvé ; a trouvé un vrai défaut d'usage (fiche hors de l'écran à 768 px), corrigé |
| Caractères de routes lus | 74 000 | 134 500 (+82 %) |

La fiche de mobilisation du run 8 ne relève aucun manque : tronc, trois cartes et recette de caractère sont présents.

## Production

| Critère | Run 7 | Run 8 |
|---|---|---|
| Idée | La coupe au chevalet : « le son se règle de l'intérieur » | Le plan coté devient la carte des réparations ; le même violon revient à sept échelles pour la location |
| Objet dessiné | Coupe maladroite : planches disjointes, chevalet démesuré, pastilles de notice | Violon de face, reconnaissable et dégradé de bois ; restent schématiques la mentonnière, les ouïes et le cordier |
| À 390 px | La coupe arrive sous le texte, à pleine largeur | Le premier écran est tout en texte ; le plan se réduit ensuite à une vignette à côté de la liste des symptômes : l'objet de preuve perd sa force sur téléphone |
| Usage | Diagnostic par symptôme, tailles en tableau | Diagnostic avec délai et prix d'exemple, location par taille et par loyer, commande en six étapes, prix d'instruments |
| Typographie | Barlow Semi Condensed et Spectral | Libre Caslon Text (voix de l'étiquette) et IBM Plex ; une serif de caractère, marqueur de la vague 2, gardée par une raison nommée |
| Couleur | Gris froid, encre bleue, vernis réservé à l'instrument | Papier neutre, encre d'ébène, vernis seulement sur l'objet ; aucun accent d'interface |
| Registre | Aucun choix partagé | Aucun choix partagé ; fond clair neutre, aucun accent relevé |
| Recette de rendu (relancée) | Aucun RETURN | Aucun RETURN |
| Recette de caractère face au caractère attendu | SIGNAL de densité à 390 px ; foyer à 14–18 % de la saillance | Aucun signal |
| Lisière, pont de couleur | Bandes droites | Bandes droites ; un bloc brun porte l'étiquette ; pas de pont de couleur, faute d'image |

## Lecture

1. **L'entrée du run et la boucle de correction sont maintenant mobilisées.** Les trois cartes, la recette de caractère et la planche, qui manquaient au run 7, sont là. Le rappel de la carte « regard » a été suivi au premier défaut bloquant.
2. **La page est plus riche et mieux construite.** L'idée sert deux usages réels (réparer, louer), l'objet dessiné passe de maladroit à reconnaissable, et la série des sept tailles donne à la page son moment fort. Ce jugement est celui de l'analyste ; il n'est pas une évaluation à l'aveugle.
3. **Trois leviers restent sans effet.** Les vignettes sont lues mais pas faites. Les gestes sont encore retirés par `--sans-gestes`. La lisière et le pont de couleur ne sont pas appliqués : sans image, le pont n'a pas d'objet, et la lisière n'a pas été tentée.
4. **Le coût monte.** Les lectures passent de 74 000 à 134 500 caractères, et le run a pris environ 21 minutes. L'agent juge encore le volume trop lourd avant le premier pixel.
5. **L'image reste le plafond.** La seule route d'image tentée a échoué (429, API retirée). C'est l'argument concret pour l'étape 4.

## Écarts et pistes

- La déclaration de caractère doit précéder le build, mais la carte « avant » ne la rappelle pas.
- `--sans-gestes` reste le réflexe pour alléger la sortie. Il faudrait comprendre pourquoi avant de le retirer : bruit, ou gestes non pertinents.
- Les vignettes ne sont faites que si l'alternative est due. L'agent a jugé qu'une phrase suffisait.
- Lectures : `ACTION/PIPELINE-DIRECTION` entier, `ACTION/RECETTE-RENDU`, `SAVOIR/TOOLS/MOYENS` et `ACTION/RECETTE-CARACTERE` ont été lus deux fois. Le coût de lecture est le prochain défaut à traiter.
- La recette de rendu a relevé un RETURN « Erreurs JavaScript » pour une police préchargée en `file://` (CORS). C'était un défaut réel pour une page ouverte par double-clic, et l'agent l'a corrigé.

## Limites

- Un run par condition. Deux productions ne font pas une tendance.
- Même modèle que celui qui a écrit les ajouts.
- Le jugement visuel est celui de l'analyste, pas celui d'une évaluation à l'aveugle ; la planche commune est préparée pour cela.
