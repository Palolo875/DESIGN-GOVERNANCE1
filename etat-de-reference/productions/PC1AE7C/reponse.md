# Théâtre de la Halle — page de la saison 2026-2027

Bonjour,

Voici la page de votre saison : `index.html`, avec sa police dans le dossier `fonts/`. Elle s'ouvre dans un navigateur sans connexion et sans autre fichier.

## Ce que j'ai fait

Une page d'affiche de salle, construite sur le texte seul. En haut, « Saison 2026–2027 » en grand, puis une phrase qui dit l'essentiel : six spectacles, de novembre à mai, et 14 € la place quel que soit le spectacle. Juste dessous, la saison prend la forme d'un **rouleau de six billets** : chaque spectacle a sa couleur, mais tous portent le même prix. Un billet mène à la fiche du spectacle.

Le programme suit dans l'ordre des dates. Pour chaque spectacle, vous trouvez la date en gros, le genre, la durée et l'âge, le titre et le résumé. À droite (ou dessous sur téléphone), un talon de la couleur du spectacle porte « Réserver · 14 € · réduit 7 € » et ouvre votre billetterie. La page se termine sur le tarif (14 € et 7 €, avec leurs conditions) et sur « Venir au théâtre » : l'adresse, l'ouverture des portes, le bar, la salle, l'accessibilité et le contact.

La page tient aussi compte de la date du jour. Elle signale le **prochain spectacle**, ou « En ce moment » pendant les représentations. Une fois un spectacle passé, elle le grise et remplace son bouton par « Représentations terminées ». Vous n'aurez donc pas à la retoucher pendant la saison.

## Pourquoi

- **Le tarif unique est votre point fort.** J'ai voulu qu'il se voie, et pas seulement qu'on le lise : six billets différents qui portent le même prix le montrent d'un coup d'œil.
- **Pas de photos, et rien d'imité.** Le brief n'en fournit pas. Plutôt que des images d'ambiance ou des emplacements vides, la page fonctionne comme une affiche typographique de théâtre, avec de grands titres étroits comme sur les affiches imprimées. La police (Bricolage Grotesque, licence libre OFL) loge les titres longs comme « Bal pour les pieds qui hésitent » sur une seule ligne, à la même taille que « Le Poids des clés ».
- **Ce que j'ai écarté** : la page de saison habituelle, avec une grande photo en ouverture, une grille de six cartes illustrées et des tons crème et bordeaux de « rideau rouge ». Sans visuels, elle aurait été vide ou fausse. Elle aurait aussi caché la chronologie de la saison, que la liste par dates rend lisible.

Je n'ai rien ajouté au contenu que vous avez fourni. Seuls les titres de section (« Le programme », « Un seul tarif », « Venir au théâtre ») et les libellés de boutons sont de moi.

## Ce que j'ai vérifié

J'ai regardé la page sur téléphone (390 px), sur tablette (768 px) et sur ordinateur (1440 px). Un contrôle automatique n'a relevé aucun défaut : pas de débordement, contrastes conformes WCAG AA, navigation au clavier, tailles des boutons. J'ai aussi vérifié le comportement selon la date (début décembre, pendant le spectacle de janvier, aujourd'hui).

Ce qui n'a pas été testé : la lecture avec un vrai lecteur d'écran, et l'avis de vos spectateurs.

## Ce qu'il faut pour la mise en ligne

1. **Les liens.** La billetterie (`billetterie.example/...`) et l'adresse e-mail (`...theatre-halle.example`) sont celles du brief. Ces domaines ne mènent nulle part et sont à remplacer par les vrais. Si votre billetterie a une page par spectacle, envoyez-moi les six liens : chaque bouton « Réserver » ira directement au bon spectacle. Aujourd'hui, ils mènent tous à l'accueil de la billetterie.
2. **Le numéro de téléphone** (04 00 00 00 00) est celui du brief, à confirmer.
3. **Un avis sur les couleurs.** Le pari, ce sont les six couleurs de billets, une par spectacle. Elles donnent un ton populaire et joyeux qui me semble aller à une salle de quartier. Si vous les trouvez trop vives ou trop « jeune public », je peux les adoucir sans toucher au reste.
4. **Pour aller plus loin** (facultatif) : des photos des spectacles, ou un logo s'il en existe un. La page tient sans eux, mais une photo par spectacle trouverait sa place à côté du résumé.

## La suite

- Dites-moi si la direction vous convient : l'affiche typographique et les billets de couleur.
- Envoyez-moi les vrais liens et, si vous les avez, les liens par spectacle : je les intègre et la page est prête à être mise en ligne.

---

**Fichiers produits**

- `index.html` : la page de saison (styles et script intégrés)
- `fonts/bricolage-grotesque-latin.woff2` et `fonts/bricolage-grotesque-latin-ext.woff2` : la police, hébergée à côté de la page
- `fonts/OFL.txt` : la licence de la police
- `reponse.md` : ce message
