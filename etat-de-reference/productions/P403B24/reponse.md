# Page article : « Le pont de la Clé rouvre »

Voici la page de l'article, dans `index.html`. C'est un seul fichier, autonome : les polices sont intégrées et la page ne charge rien depuis l'extérieur. Elle s'ouvre directement dans un navigateur.

## Ce que j'ai fait

La page est faite pour lire l'article en entier, sans fatigue, et pour retrouver d'un coup d'œil les deux chiffres et la citation à mettre en valeur.

- **Lecture.** Le corps du texte est dans un serif de presse conçu pour l'écran (Newsreader). Les lignes font environ 70 signes, ce qui reste confortable pendant 6 minutes.
- **Titre.** Il est dans une grotesque de presse (Schibsted Grotesk). Il tient en trois lignes sur ordinateur, et chaque ligne s'arrête à un endroit qui respecte le sens de la phrase.
- **Chiffres clés.** Sur grand écran, ils sont dans la marge, à hauteur du paragraphe qui en parle. Sur mobile, ils s'insèrent dans le fil du texte. Chacun s'accompagne d'un petit graphique construit uniquement avec des données de l'article :
  - **4,2 millions d'euros.** Une barre montre la part de 1,6 million apportée par la région. Une seconde barre, à la même échelle, montre les 6,8 millions estimés pour l'option de démolition-reconstruction, écartée en 2023.
  - **9 300 traversées par jour.** Une barre en quatre parts montre « près d'un quart à vélo ou à pied ».
- **Citation.** Celle d'Agnès Vidal est mise en exergue, en largeur, juste avant le passage sur la clé de voûte et les initiales des bâtisseurs.
- **Encadré de fin.** « Ce qui change pour la circulation » contient la liste fournie, plus un plan des voies vu de dessus (trottoirs, voies cyclables, voie unique alternée).
- **Couleurs.** La page est en gris de suie sur blanc, avec une seule couleur chaude : l'ocre clair, celui que le nettoyage a fait réapparaître sous la pierre noircie. Un petit motif en forme de clé de voûte revient à trois endroits : devant la rubrique, en puce dans l'encadré et en marque de fin d'article.

## Pourquoi

C'est un quotidien local qui annonce un fait : le pont rouvre samedi. Le réflexe pour un sujet patrimonial aurait été une page « nostalgie » : fond crème, grand titre en serif à l'ancienne, tons sépia et lettrine. J'ai écarté cette piste. Elle aurait transformé une information en carte postale. Ici, l'histoire du pont passe par le contenu (la clé de voûte, la photo de 1911, les souvenirs des habitants) et non par un habillage rétro.

J'ai comparé les deux options de titre sur le vrai texte avant de choisir.

Cette page sert à décider si cette direction peut devenir celle des longs articles de L'Écho du Val.

## Hypothèses et points à vérifier

- **Texte.** L'article est repris intégralement, sans coupe ni réécriture. Je l'ai vérifié automatiquement, paragraphe par paragraphe. Je n'ai appliqué que les règles typographiques françaises : apostrophes typographiques et espaces insécables avant « : ; ? ! » et à l'intérieur des guillemets. Je n'ai ajouté aucun intertitre, puisque cela aurait ajouté du texte.
- **Textes ajoutés autour de l'article.** Ce sont uniquement :
  - les étiquettes des chiffres (« Le coût », « La fréquentation ») ;
  - les légendes des graphiques ;
  - la légende du plan des voies ;
  - une mention discrète en pied de page : « Page de démonstration : le média, la ville et le pont de la Clé sont fictifs ».

  Tout est à valider par la rédaction.
- **Photo d'archive.** Elle n'a pas été fournie. J'ai réservé un cadre au format 3:2, marqué « Photo d'archive à intégrer », avec la légende fournie. Je n'ai mis aucune fausse image à la place.
- **Plan des voies.** L'article ne donne que la largeur des trottoirs (1,80 m). Le plan est donc indiqué comme « schéma de principe, sans échelle ». Le côté de chaque voie cyclable suit la circulation à droite. Il est à confirmer avec les services de la ville.
- **En-tête du site.** Il se limite au nom du média : je n'ai inventé ni menu ni boutons de partage, faute de liens réels. Je n'ai pas non plus ajouté l'heure de publication, qui n'était pas fournie.

## Ce qui manque pour la vraie version

- La photo d'archive, avec les droits de reproduction des Archives municipales.
- Votre charte, si L'Écho du Val en a une (logo, couleurs, polices). J'ai composé le nom du média en texte simple. La page s'adapte facilement à une charte existante.
- La largeur des voies, si vous voulez un plan à l'échelle.
- Une relecture par la rédaction des textes ajoutés et des légendes.

## Vérifications faites

J'ai regardé la page sur mobile (390 px), sur tablette (768 px) et sur ordinateur (1440 px), et lancé un contrôle automatique sur ces trois largeurs. Il ne trouve aucun débordement, aucun texte coupé ou superposé, et tous les contrastes de texte atteignent le niveau WCAG 2.2 AA. La structure est accessible : langue déclarée, un seul titre principal, graphiques décrits en texte.

Ce qui n'a pas été vérifié :
- un test de lecture avec de vrais lecteurs ;
- l'intégration dans votre système de publication ;
- un mode sombre, qui n'a pas été réalisé.

Une réserve : avec le cadre photo vide, le milieu de la page paraît plus lourd qu'il ne le sera une fois la photo en place.

## La suite

1. Envoyez-moi la photo d'archive et, si elle existe, votre charte. J'intègre les deux et je vérifie le recadrage de la photo sur mobile.
2. Si cette direction vous convient, je peux en faire un gabarit réutilisable pour vos longs articles : marge à chiffres, citation, encadré.

---

**Fichiers produits**
- `index.html` : la page de l'article, autonome (polices Newsreader et Schibsted Grotesk intégrées, sous licence libre OFL).
- `reponse.md` : cette réponse.
