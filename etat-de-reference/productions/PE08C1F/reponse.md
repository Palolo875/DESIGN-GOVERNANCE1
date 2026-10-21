# Théâtre de la Halle — page de la saison 2026-2027

Bonjour,

Voici une première proposition de la page de saison : `index.html`, avec ses polices dans le dossier `fonts/`. Elle s'ouvre directement dans un navigateur, sans connexion.

## Ce que j'ai fait

La page ne commence pas par une grande image ni par une accroche. Elle s'ouvre sur **la saison elle-même** : un tableau qui montre les six spectacles sur une frise de novembre à mai, à l'échelle réelle du calendrier. Il y a un trait rouge par représentation, à sa date exacte. On voit d'un coup d'œil ce qui se joue, quand, et que la salle joue trois soirs en novembre, six fois en janvier et une seule fois en mai. Juste au-dessus, le message principal : **14 € la place, quel que soit le spectacle**.

Ensuite, la page suit cet ordre :

1. **Les six fiches**, toujours construites de la même façon :
   - les dates en grand ;
   - le genre, la durée et l'âge ;
   - le texte de présentation ;
   - la liste des représentations ;
   - un bouton « Réserver » qui mène à la billetterie.

   La frise revient en petit dans chaque fiche pour situer le spectacle dans la saison.
2. **Une bande rouge « Tarif unique »** : 14 € pour tous, 7 € pour les moins de 18 ans et les minima sociaux, entrée gratuite pour les participants de la Nuit de la parole libre.
3. **Une bande bleue « Venir à la Halle »** : adresse, salle (gradin, plain-pied, boucle magnétique), ouverture des portes, bar et contact.
4. **Une dernière phrase** pour conclure, avec le bouton de la billetterie.

Côté typographie et couleurs :
- Les titres sont écrits en **lettres pochoir**. C'est un clin d'œil aux lettres peintes sur les caisses des théâtres en tournée. Marcel Jacno en avait tiré l'identité du TNP de Jean Vilar, le grand théâtre populaire voisin, à Villeurbanne. Je n'ai rien copié : j'ai seulement repris l'idée.
- Le texte courant utilise une police conçue pour être très lisible (Atkinson Hyperlegible), ce qui va dans le même sens que l'accessibilité de votre salle.
- La page n'utilise que deux couleurs, un bleu de travail et un rouge d'affiche, sur fond papier, comme une affiche imprimée en deux couleurs.

**La page se met à jour seule avec le temps.** Une représentation passée est barrée. Quand toutes les dates d'un spectacle sont passées, il est marqué « terminé » et son bouton « Réserver » est retiré. La ligne en haut de page affiche toujours la prochaine représentation, par exemple « Prochaine représentation : Ce que la rivière emporte, jeudi 21 janvier, 19 h ». À la fin de la saison, elle indique que la saison est terminée. J'ai vérifié ces trois états en simulant plusieurs dates.

## Pourquoi

Ce que vous vendez, c'est un calendrier de quartier à prix unique : il n'y a ni formules ni catégories de places à comparer. J'ai donc choisi de montrer ce calendrier dès l'ouverture plutôt qu'une grille de six vignettes à photos. C'est la solution la plus courante, mais elle aurait demandé des photos que nous n'avons pas, et elle cache les dates.

**L'option écartée** était une page « affiche », avec un grand visuel par spectacle. Elle sera intéressante quand vous aurez des photos. Le tableau de saison pourra alors rester en haut et les photos entrer dans les fiches.

Ce premier rendu vous permet de décider :
- si ce ton (populaire, typographique, sans photo) vous ressemble ;
- si l'ouverture sur la saison entière vous convient mieux qu'une ouverture sur un seul spectacle.

## Hypothèses que j'ai faites

- **Contenus :** j'ai repris tous vos textes à l'identique. Je n'ai ajouté que des titres de section et des libellés de boutons, plus les jours de la semaine abrégés dans les listes de dates, que j'ai vérifiés sur le calendrier.
- **Liens « Réserver » :** ils mènent tous à l'accueil de votre billetterie (`https://billetterie.example/theatre-de-la-halle`), car je n'ai pas de lien par spectacle ou par date. La page indique qu'on choisit la date sur la billetterie et que c'est un site externe.
- **Photos :** il n'y en a aucune, puisque vous n'en avez pas fourni. Je n'ai fabriqué aucune image de remplacement.
- **Caractère fictif :** comme le brief présente le lieu comme fictif, le pied de page porte la mention discrète « Lieu fictif — page de démonstration ». Il faudra la retirer pour la mise en ligne.
- **Liens de contact :** le courriel et le téléphone sont cliquables.

## Ce qui manque pour la vraie version

- **Coordonnées réelles :** votre adresse, votre téléphone et votre courriel. Les valeurs actuelles (`.example`, `04 00 00 00 00`) sont des valeurs de démonstration.
- **Liens de billetterie** par spectacle, ou mieux par représentation, si votre billetterie les propose.
- **Photos des spectacles**, si vous le souhaitez, avec leurs droits et le nom des photographes.
- **Mentions légales** et éventuels crédits des compagnies (distribution, production), si vous voulez les afficher.
- **Polices :** elles sont libres (licence SIL OFL) et leurs licences sont jointes dans `fonts/`. Gardez ce dossier à côté de la page.

## Vérifications faites

- J'ai contrôlé la page sur ordinateur, tablette et téléphone (1440, 768 et 390 px de large) :
  - rien ne déborde ;
  - aucun texte mesuré n'a un contraste insuffisant ;
  - la navigation au clavier fonctionne et le focus reste visible ;
  - les boutons sont assez grands au toucher ;
  - aucune animation n'est imposée.
- Sur un écran d'ordinateur courant, toute la saison tient dans le premier écran.

Ces contrôles ne valent pas un test avec de vraies personnes. Le plus utile serait de demander à quelques habitants de lire le tableau sur leur téléphone et de trouver la date qui les intéresse.

## La suite

1. Dites-moi si la direction vous convient ou ce que vous voulez changer : ton, couleurs, ordre des sections.
2. Envoyez-moi vos coordonnées réelles, les liens de billetterie et vos photos éventuelles. J'en tirerai la version à mettre en ligne.

---

**Fichiers produits**

- `index.html` : la page de saison, autonome (styles et script inclus).
- `fonts/bigshoulders-stencil-latin.woff2`, `fonts/bigshoulders-stencil-latin-ext.woff2` : police des titres (Big Shoulders Stencil).
- `fonts/atkinson-next-latin.woff2`, `fonts/atkinson-next-latin-ext.woff2` : police du texte (Atkinson Hyperlegible Next).
- `fonts/OFL-big-shoulders-stencil.txt`, `fonts/OFL-atkinson-hyperlegible-next.txt` : licences des polices.
- `reponse.md` : ce message.
