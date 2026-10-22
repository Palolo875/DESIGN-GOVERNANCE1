J’ai fait une première version du site de votre atelier. C’est une page unique : elle s’ouvre dans un navigateur et tient sur téléphone comme sur ordinateur. Je n’avais aucune information sur l’atelier : **le nom (« Atelier Mareuil »), l’adresse, le numéro, l’adresse e-mail, les horaires et les délais sont donc des exemples**. Ils sont signalés sur la page et sont à remplacer.

**Ce que j’ai fait**
- La page s’ouvre sur une phrase, « Le son se règle de l’intérieur. », à côté d’une coupe dessinée d’un violon au niveau du chevalet. Le dessin montre l’âme, la barre d’harmonie, la table, le fond et les éclisses, avec la liste des pièces et leurs bois.
- Une rubrique « Ce que votre instrument vous dit » liste ce que le musicien constate : une corde frise, le son est sourd, le chevalet penche, quelque chose bouge à l’intérieur, une fissure, des chevilles qui glissent, un instrument pour un enfant. Chaque cas donne une piste et l’endroit concerné, qui s’allume sur le dessin. Un lien « Écrire à l’atelier à ce sujet » ouvre un e-mail déjà rempli.
- Viennent ensuite vos quatre types de travaux (réglages, réparations et restauration, fabrication, location et vente), un tableau des tailles de violon pour les enfants (de 1/16 à 4/4, selon la longueur du bras), puis l’adresse, les horaires et le contact.
- La page se termine sur l’étiquette que le luthier colle à l’intérieur de l’instrument, avec de nouveau « Prendre rendez-vous » et le téléphone.

**Pourquoi**
- J’ai pris pour point de départ ce que seul un luthier sait montrer : l’intérieur de l’instrument et ce qu’on y règle. Le site part de ce que le musicien entend et le mène au rendez-vous.
- J’ai écarté la page d’artisan habituelle : grande photo d’atelier, fond crème et brun, quatre cartes de services, témoignages. Elle irait aussi bien à un ébéniste.
- Les couleurs suivent la lumière du nord sous laquelle on travaille le vernis : un fond gris clair un peu froid, une encre bleu foncé pour les boutons et les liens. Seuls le bois et le vernis de l’instrument sont chauds.
- Les titres sont dans une police étroite qui rappelle l’écriture des plans de lutherie, le texte dans une police à empattements plus agréable à lire.
- J’ai supposé un atelier de **violon, alto et violoncelle**. Si vous travaillez la guitare ou d’autres instruments, le dessin et la rubrique « Ce que votre instrument vous dit » sont à refaire (une guitare n’a pas d’âme). Ce choix change le reste de la page.
- Ce qu’il faut décider sur cette version : est-ce bien votre atelier ? Le ton vous convient-il ? Le diagnostic est-il utile à vos clients, ou préférez-vous une page plus simple : travaux, tarifs, contact ?

**Ce qui manque pour la vraie version**
- Vos vraies informations : nom de l’atelier, adresse, téléphone, e-mail, jours et horaires, délais habituels, et tarifs si vous souhaitez les afficher (location surtout).
- Des photos de votre atelier et de vos instruments. J’ai laissé un emplacement signalé plutôt que de mettre une photo d’un autre atelier.
- Une relecture de votre part, comme luthier, des pistes du diagnostic, du dessin et du tableau des tailles. Les tailles sont des repères courants, pas vos mesures, et le dessin est un schéma aux proportions approchées.
- Le texte de votre vraie étiquette, si vous en avez une.
- Les mentions légales, et la mise en ligne : nom de domaine et hébergement. Rien n’est publié pour l’instant.

**La suite**
1. Envoyez-moi les informations ci-dessus et quelques photos : je remplace les exemples et j’ajuste la page.
2. Dites-moi ce que vous changeriez d’abord (le ton, le dessin, l’ordre des rubriques). Je reprends à partir de là.

---

## Trace

- Mode : DIRECTION, trace légère, proposition EXPLORATORY (premier contact d’un atelier réel, aucune ancre fournie). Décision : la direction de la première scène. Risque principal : faux contenu et page artisan interchangeable. Preuve minimale : recette de rendu à 390/768/1440 px et état « diagnostic » prouvé au clic. Arrêt : défaut dominant traité et réobservé.
- Thèse : un atelier qui règle le son de l’intérieur → coupe au chevalet avec repères (objet codé, TRUTH/ILLUSTRATIVE + MECHANISM : schéma, proportions approchées) → choisir un symptôme surligne l’endroit sur la coupe et ouvre un e-mail prérempli. Phrase d’idée : « Sur cette page, l’âme devient la coupe qui ouvre la page. » Elle passe le test du concurrent : ni l’ébéniste ni le luthier guitare n’ont d’âme.
- Modal : vague 2 (crème/brun, serif de caractère, rouille, photo d’atelier), trame hero photo / à propos / 4 cartes / galerie / témoignages / contact. Parti : la trame est rompue (coupe → diagnostic → travaux en registre → tailles → venir → étiquette). Fond froid « lumière du nord » #e9edf0, encre bleue #23467a, vernis #9b3f1b réservé à l’instrument. Titres en Barlow Semi Condensed (voix de plan), comparée à Spectral et IBM Plex Sans Condensed avec specimen.py ; corps en Spectral. Registre des choix : aucun choix partagé avec les 9 entrées précédentes. Contre-choix situé : titres en Spectral pour un atelier tourné vers l’expertise d’instruments anciens.
- Plafond : aucun contenu ni asset fourni. Coupe CODE-NATIVE, photo d’atelier en emplacement marqué (pas de photo d’un autre atelier). Contenus marqués « exemple » : nom, adresse, téléphone (plage fictive 01 99 00), e-mail (.example), horaires, délais, tarifs, étiquette. Le diagnostic et les tailles relèvent du savoir général du métier, présentés comme des pistes et des repères. Famille d’instruments (quatuor) supposée.
- Défaut dominant : le titre coupé contre le sens à 1440 px (« Le son se / règle de ») est corrigé par des coupes de sens (« Le son / se règle / de l’intérieur. ») et réobservé. Autres corrections faites : focus invisible sur fond ébène (1,89:1, corrigé), liens « Écrire » à 20 px de haut (corrigés à 44 px), travaux en quatre blocs égaux passés en registre. Le chevauchement signalé venait du texte des volets fermés, non affiché (vérifié avec checkVisibility) : il est rendu explicite en CSS et la recette passe. Ce qui retient : la coupe et le surlignage. Ce qui reste générique ou peu résolu : le dessin du chevalet, un peu lourd, et les bords de table qui se lisent comme des ailes séparées ; l’emplacement photo vide. Geste envisagé, non appliqué : affiner la silhouette du chevalet sur la relecture d’un luthier.
- Prochaine preuve : relecture métier du schéma, des pistes et des tailles par la personne ; contrôle à 200 % de zoom et au lecteur d’écran (NOT-VERIFIED) ; contraste du texte SVG calculé à la main (≥ 6:1 estimé, non mesuré par la recette) ; vraies photos à placer.
