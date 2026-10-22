J'ai fait une première version complète de votre site, sur une seule page. Pour l'ouvrir, double-cliquez sur `projet/site/index.html` : il n'a besoin de rien d'autre, et les polices sont fournies.

**Ce que j'ai fait**
La page s'ouvre sur un plan de violon dessiné, avec ses cotes. Le visiteur choisit ce qu'il entend ou voit : « une corde frise », « le chevalet penche », « le son s'est fermé depuis l'automne »… La partie concernée s'allume sur le plan, et une fiche dit ce que fait l'atelier, en combien de temps et pour quel prix. On peut alors appeler, ou écrire avec le sujet déjà rempli.
Le même violon revient ensuite pour la location : les sept tailles, de 1/16 à 4/4, dessinées à leur vraie échelle, avec la longueur de bras correspondante et le loyer. Viennent après les instruments faits à l'atelier, avec les étapes, les délais et l'étiquette collée dans la caisse, puis l'adresse et les horaires.

**Pourquoi**
Un site de luthier sert surtout à quelqu'un dont l'instrument a un problème, ou à un parent qui cherche la bonne taille. J'ai donc mis ces deux usages au centre, avec votre propre vocabulaire (âme, chevalet, touche, décollement), plutôt que la vitrine habituelle : grande photo d'établi, trois encarts de services, témoignages.
La seule couleur de la page est celle du vernis, sur l'instrument. Le reste est en noir d'ébène sur papier clair. Le nom est composé dans un caractère proche de celui des étiquettes d'instruments.
L'autre choix que j'ai écarté : ouvrir sur la location pour enfants. Il serait meilleur si la location fait l'essentiel de votre activité. Dites-le-moi, l'ordre s'inverse facilement.

**Ce qui manque pour la vraie version**
Tout ce qui concerne votre atelier est inventé, et marqué « exemple » sur la page. Il me faut :
1. **Votre identité et vos coordonnées** : nom, adresse, téléphone, courriel et horaires. Le numéro actuel appartient à une plage réservée à la fiction, et l'adresse mail ne fonctionne pas.
2. **Ce que vous faites vraiment, et à quels prix** : quels instruments (j'ai supposé violon, alto et violoncelle ; si vous faites des guitares, le plan change), vos tarifs et délais de réparation, vos conditions de location et vos prix d'instruments neufs.
3. **Des photos** de l'atelier, de vos mains au travail et de vos instruments. Il n'y en a aucune pour l'instant, et je n'ai pas voulu en mettre de fausses. Des photos prises au téléphone, en lumière du jour, suffisent.

Deux limites à connaître :
- Le violon est un dessin schématique fait de mémoire. Il se reconnaît, mais un œil de luthier y verra des approximations, par exemple la mentonnière en aplat et la volute simplifiée. Les explications techniques des fiches sont aussi à relire par vous.
- Les tailles par longueur de bras sont des repères courants, qui varient d'une source à l'autre.

**La suite**
- Envoyez-moi les trois éléments ci-dessus, et je remplace tous les exemples.
- Regardez la planche `projet/planche/planche.html` et dites-moi ce que vous changeriez d'abord sur le dessin du violon. Je peux le corriger d'après votre œil, ou le redessiner d'après un plan ou une photo de l'un de vos instruments.

Sources consultées pour rester vraisemblable (non liées à votre atelier) : [Luthier Vidal, location 3/4](https://luthiervidal.com/en/rental/violins-rental/violin-rental-study-34.html) ; [Atelier de lutherie la Volute (fiche)](https://provence-alpes-cotedazur.com/sejourner/informations-pratiques/tous-les-services-pratiques/atelier-de-lutherie-la-volute-aubagne-fr-2879043/) ; [Marion Tissot Luthier (fiche)](https://provence-alpes-cotedazur.com/sejourner/informations-pratiques/tous-les-services-pratiques/marion-tissot-luthier-pernes-les-fontaines-fr-4709339/) ; [CIDJ, métier de luthier](https://www.cidj.com/s-orienter/metiers/luthier-luthiere) ; [tableau des tailles, alcuinfonds.be](https://alcuinfonds.be/blog/violon-pour-enfant/) ; [tailles 1/16 à 4/4, Twigg Musique](https://www.twiggmusique.com/blogs/news/violin-sizes-from-1-16-to-4-4-a-complete-guide-for-parents-and-adult-beginners).

---

## Trace

1. **Mode** : DIRECTION. C'est le premier contact d'un commerce réel, sur un brief vague, sans personne joignable.
   - Décision dominante : ce que le site d'un luthier montre et fait faire d'abord.
   - Risque principal : une vitrine générique (vague 2 : crème, brun, serif, photo d'établi) ou des contenus inventés lus comme réels.
   - Preuve minimale : captures à 390, 768 et 1440 px ; `check_render` ; preuve d'état du diagnostic (`--click`, `--assert`, `--in-frame`).
   - Condition d'arrêt : deux passages sans défaut bloquant et le défaut restant nommé. Elle est atteinte.
2. **Thèse** : « on écoute l'instrument avant d'y toucher ».
   - Objet de preuve : un plan coté du violon, dont six repères ouvrent une fiche (symptôme → intervention, délai, prix).
   - Geste : choisir ce qu'on entend, puis écrire avec le sujet prérempli ou appeler.
   - Phrase d'idée : « le plan d'atelier devient la carte des réparations ».
   - Test du concurrent : la phrase tient encore pour un autre luthier, puisque le brief ne donne rien de propre à l'atelier. Elle tombe pour une boutique de musique ou un ébéniste.
   - Fil : le même dessin revient à sept échelles (location), puis l'étiquette sert pour la commande. L'état est prouvé pour « fissure » et « bord » (9 assertions vraies, fiche dans le cadre aux trois largeurs).
3. **Modal, trame et parti**
   - Modal : crème, brun, serif, photo d'établi, trois cartes de services, galerie et témoignages. Le registre compte déjà crème ×6 et orange ×4.
   - Parti : papier neutre #f3f4f1 et encre d'ébène. La seule chroma est le vernis, posée sur l'objet.
   - Polices : Libre Caslon Text, voix de l'étiquette, comparée au spécimen à IBM Plex Sans Condensed et à Old Standard TT. La serif est gardée parce que l'étiquette la justifie. IBM Plex porte la voix du plan.
   - Trame rompue : réparer → louer → commander → venir.
   - Déclaration de caractère : `site/caractere.json`, écrite après le premier build et non avant (écart de méthode).
   - Contre-choix : ouvrir sur la location (échelle des tailles) si elle domine l'activité.
4. **Plafond et contenus marqués**
   - Plafond : route CODE-NATIVE, sans photo ni asset de l'atelier. Wikimedia a répondu 429 et l'API de recherche du Met est retirée.
   - Ancres : seulement des ancres de contenu, observées et non visuelles (annuaires de luthiers, location Vidal à 16–19,50 €/mois avec 3 mois minimum, tableaux de tailles divergents). La proposition reste donc EXPLORATORY.
   - Marqués « exemple » : nom, adresse, téléphone (plage ARCEP de fiction 01 99), courriel en `.example`, horaires, délais, prix, conditions de location, étiquette.
   - Savoir métier repris de mémoire, non revérifié : âme, fissures d'hiver, cotes 356/208.
5. **Défaut dominant restant** : l'objet dessiné reste schématique (mentonnière en aplat, volute simplifiée, proportions de mémoire).
   - Gestes appliqués puis réinspectés :
     - volute redessinée et bas de caisse resserré : la silhouette se lit mieux ;
     - cote du diapason retirée (atelier d'édition) : décision confirmée, rien de perdu ;
     - masse visuelle (h1 de 96 à 84 px, sous-titre sur une ligne, plan élargi à 440 px) : le SIGNAL de matière est levé à 1440 px. Il est gardé à 390 px, où le nom et l'appel passent d'abord, par choix.
   - Corrigés : le RETURN de préchargement de police en `file://` et le RETURN `--in-frame` à 768 px (la fiche est maintenant amenée dans la fenêtre).
   - Contrastes du texte SVG et des `::before` calculés à part : 6,9:1 au minimum.
   - Résilience : le repli typographique ne crée ni débordement ni troncature.
   - Planche préparée : `planche/planche.html`.
6. **Prochaine preuve** : le regard d'un ou une luthière sur le dessin et sur les fiches, avec les vraies données de l'atelier. Ensuite, un essai sur mobile avec un parent qui loue et un musicien qui a un problème.
