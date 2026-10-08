# Matière à enrichir — affiches de référence et forme de page (2026-10-08)

Statut : **intégrée** le 2026-10-08 (révision `R2026-10-08-ACCES-MATIERE`, commits `d11b8ff` à `9681d4e`, branche `claude/repo-analysis-g87gag`) ; voir « Intégration » en fin de document. À transformer en **opérations** (savoir), jamais en exemples à copier (règle 9).

## Affiches partagées par le propriétaire (5)

rétro (collines devant le mot), BORING (figure devant le mot), Fieldtrip (formulaire administratif comme décor), warmth (image dans les lettres), main et curseur (collision pixel / fresque).

Constat commun : une seule opération visuelle, poussée à fond, dans un grand champ calme.

Manques repérés dans le système :
1. TXI-01 traite le texte sur image seulement de façon défensive ; rien sur le mot et l'image dans le même plan (figure devant, image dans la lettre, mot comme horizon).
2. Rien sur le rapport d'échelle et le champ calme majoritaire autour d'une seule opération.
3. Rien sur l'idée par collision ou contresens de registres.

Mises en garde : c'est aussi une vague (grain, fausses métadonnées, code-barres, ✦) à nommer comme MODAL ; les fausses métadonnées sont de la fiction assumée sur une affiche, de fausses preuves sur une page produit.

## Forme de page (discussion)

Constat U3/U5 : les pages rompent la trame modale au premier écran, puis le bas retombe dans le gabarit (sections de même poids, titre à gauche et texte à droite, tarifs, FAQ, CTA). Le propriétaire juge tout le défilement : rythme, cartes, pied de page.

Manques repérés : aucune occurrence de « pied de page », « fin de page » ou « séquence de sections » dans les sources ; le test de trame (TRM-01) est lu comme un test de premier écran. La N-convergence crème + serif correspond déjà au marqueur « vague 2 » de SAVOIR/TOOLS/CONVERGENCE, que le chemin par défaut n'ouvre pas toujours.

## Lecture structurelle des affiches (côté BIBLIOTHEQUE)

Une affiche est un champ unique et fixe ; une page web est une séquence qui défile. Ce qui se transpose : le premier écran, un « moment affiche » en cours de page, les transitions entre sections et la fin. Ce qui ne se transpose pas : la lecture d'un seul coup d'œil de toute la surface.

| Opération de structure | Où on la voit | Couverture actuelle | Transposition web |
|---|---|---|---|
| Bandes de cadrage haut et bas : une bande d'informations en haut, un colophon en bas, un champ libre entre les deux | rétro (métadonnées en 5 colonnes ; n°, devise, code-barres) ; Fieldtrip (bande de formulaire) | Partielle : `MODIFIER/NAVIGATION_SHELL`, `SUPPORT/ARCHITECTED_FRAME` ; rien sur la bande basse | Navigation comme bande typographique ; pied de page comme colophon qui referme |
| Ancrage aux coins : de petits éléments aux coins tiennent un grand vide sans boîte | BORING (4 coins), warmth, rétro (étoiles) | Absente | Structure sans cartes : repères en périphérie, champ central libre |
| Franchissement de cadre : un élément chevauche deux zones | warmth (mot à cheval sur le bord de la photo) ; rétro et BORING (le paysage ou la figure coupe le mot) | Absente (aucune occurrence de chevauchement ou de franchissement) | Un élément qui traverse la frontière entre deux sections, au lieu de sections-boîtes fermées |
| Plans superposés comme structure | rétro, BORING, warmth | Partielle : « relations de plans » dans `DIRECTION/VISUAL_TARGET`, sans route de structure | Profondeur entre titre, objet et fond, avec ses risques (lecture, recadrage mobile) |
| Champ libre et petit objet : échelle disjointe | rétro (bus minuscule), main et curseur | Couverte : `SUPPORT/FREE_FIELD`, `SCENE/EDITORIAL_FIELD` | Moment affiche |
| Le document vernaculaire comme gabarit : formulaire, ticket, carnet ou fiche structure la page | Fieldtrip (autorisation de sortie) | Absente en structure (« vernaculaire » n'existe que pour la typo et le style) ; N4 l'a trouvé seul (le carnet à souche) | Facturation : la facture ou le carnet ; natation : fiche d'inscription, carnet de progrès, planning du bassin |

Limites : six opérations tirées de cinq images ; à transformer en opérations avec conditions, contre-indications et preuve, comme les routes existantes, jamais en catalogue d'exemples.

## Constat outil incident

`read_route.py --trouver ... | head` lève un BrokenPipeError (trace Python) quand la sortie est coupée. Les agents utilisent `| head` : à corriger (sortie silencieuse sur tube fermé).

## Deuxième série d'images (4) : séries, présentations, page web

Images : présentation Matisse (portrait-silhouette rempli de ses œuvres, puis diapositives) ; présentation « Originality » (illustrations, « Part. 01 / 02 ») ; série de six affiches des termes solaires (même gabarit, scène changeante) ; page web « Stand out » (tentacules).

Leçon dominante : **la série**. Une page est une suite de sections ; ces images montrent comment varier sans uniformiser.

| Opération | Où on la voit | Couverture actuelle | Transposition web |
|---|---|---|---|
| Constantes et variables : un mobilier de cadre fixe (repères aux coins, numérotation, bande basse) et une variation réglée (position et échelle de l'image, côté du texte) | Matisse, Originality, termes solaires | Absente (GRID règle la circulation dans une surface, pas la variation d'une surface à l'autre) | Rythme des sections sans boîtes identiques : on change la position et l'échelle, on garde les repères |
| Numérotation comme ossature | « Part. 01 / 02 », « 01 / 02 » | Absente | Sections ordonnées quand la page est un parcours (étapes, paliers) |
| Bord travaillé comme transition : le bas de l'image a une forme, le titre la chevauche | termes solaires | Absente | Transition entre sections ; à condition que le bord vienne du sujet (la ligne d'eau pour la natation), sinon c'est le cliché du séparateur en vague |
| Motif récurrent qui traverse la séquence | Stand out (les tentacules reviennent et débordent le cadre de la photo) | Absente | Le fil de l'arc de page ; relie le premier écran au reste |
| Image dans une forme : le portrait fait des œuvres | Matisse | Partielle (côté savoir : warmth) | Un objet composite qui dit la thèse |
| Accent prélevé dans l'image | Originality (pastilles de couleur tirées des illustrations) | Couverte côté savoir (CFT-05, palette par rôles) | — |

Contre-exemple dans la même image : « Stand out » réussit son premier écran et son fil, puis retombe au milieu dans la rangée générique « icône + titre + texte × 4 ». C'est exactement le schéma de nos runs U5 (premier écran situé, milieu gabarit).

Mises en garde : deux présentations sont des modèles avec faux texte (« Far far away… ») : la structure est la leçon, pas le contenu. La page web date d'environ 2014 (icônes plates, rangée de services) : c'est la vague de son époque. Le séparateur en vague est un cliché sauf s'il vient du sujet.

### Compléments de la deuxième série côté savoir, direction et esthétique

- Savoir : texte vertical comme ancrage de bord ; calligraphie ou écriture manuscrite comme voix (déjà ouvert par la comparaison de voix de `SAVOIR/CRAFT`, à relier) ; bord peint ou déchiré comme matière.
- Direction : l'objet-thèse composite (l'artiste fait de ses œuvres) ; le jeu sur son propre sens (« 180° » retourné), qui rejoint l'idée par contresens.
- Esthétique : le **registre d'illustration**. Le même outil peut être professionnel (aquarelle d'Originality) ou enfantin ; c'est le reproche du propriétaire à P en U3 (« trop centré sur les enfants avec ce côté dessiné »). À relier à `SAVOIR/STYLE`.

## Troisième série d'images (5) : écrans d'application mobile

Images : Plan&go (partage de voyage, billet orange, tampons de passeport, avatars à bulles) ; Kidory (livres pour enfants, mode lecture brun) ; application de tennis de table (écran d'accueil illustré) ; Peloton (photo plein cadre, inscription) ; Numi (ciel et nuage, puis carte de patrimoine qui émerge du nuage).

Déjà connu du système : trois de ces écrans (tennis de table, Peloton, Numi 1) correspondent exactement au marqueur de vague `[VEILLE 2026-10] Écran d'accueil d'app` de `SAVOIR/TOOLS/CONVERGENCE` (ambiance en haut, slogan court, boutons en bas, conditions en petit). Le contre-exemple qu'il recommande, montrer le produit en action, est ce que font Numi 2 et Plan&go.

| Opération | Où on la voit | Couverture actuelle |
|---|---|---|
| Personnalité dans l'objet du domaine, conventions dans les contrôles : le billet et les tampons portent le voyage, les boutons et formulaires restent standards | Plan&go | Partielle (OBJECT, UI-UX-REALITY) ; le partage explicite n'est pas formulé |
| Le mécanisme montré par la présence : des avatars dessinés et des bulles (« Tickets uploaded ») montrent la collaboration sans faux témoignage | Plan&go | Partielle (geste produit) |
| Une décision par écran sur mobile : un champ, un choix, une action dans la zone du pouce ; feuille posée sur le contexte, l'objet reste visible au-dessus | Plan&go, Peloton | Absente (aucune occurrence de « pouce » ni de « une seule tâche ») ; nos pages mobiles sont des pages d'ordinateur empilées |
| Le contenu d'abord : en mode lecture, l'interface se retire (réglages repliés, thème chaud) | Kidory | Partielle |
| Franchissement de cadre en interface : la carte émerge du nuage, les avatars débordent du billet | Numi 2, Plan&go | Absente (voir la première série) |

Vérité : Plan&go affiche une adresse e-mail réaliste (« 9760960795@gmail.com ») dans une maquette ; c'est la donnée personnelle d'apparence réelle que le système veut éviter. Peloton est une marque réelle : référence d'exécution, pas d'identité à reprendre.

## Quatrième série d'images (5) : widgets et micro-unités

Images : cartes de score de crédit (jauge, bulletin par lettres, barre d'utilisation graduée, courbe annotée) ; tuner radio (« 088.5 » au zéro estompé, échelle 87-90 à aiguille rouge, mascotte pixel posée sur le bord) ; invitation et résumé d'appel (accent vert acide) ; deux cartes de portefeuille crypto (gros montant, pile de jetons, échanger et envoyer).

Déjà couvert, et bien : `BIBLIOTHEQUE/MICRO` (lecture « identité → état → mesure ou choix → conséquence → action » ; `USAGE_LEDGER` : valeur, unité, plafond, période ; `QUERY_HEALTH` : « comparé à quoi »). La carte d'utilisation (solde, plafond, échelle, 6 %) est presque la définition d'`USAGE_LEDGER`. `BIBLIOTHEQUE/DERIVE` refuse déjà les noms de peau comme `SCENE/BENTO`. Figures tabulaires : `SAVOIR/TYPE` et `SAVOIR/STATE`.

À ajouter (savoir et esthétique, pas de nouvelle route) :
- **Une carte, une question** : le chiffre héros à très grande échelle, son repère visible (échelle « Great → Poor », graduation 87-90, plafond), une conséquence, une action. C'est l'inverse de nos tableaux de bord U5 à micro-libellés.
- **Le graphique qui s'annote** : la conclusion est écrite sur la courbe (« score en hausse de 13 points »), pas laissée au lecteur.
- **L'instrument réduit** : cadran, jauge, règle graduée, issus d'un objet physique du domaine. Même famille que le document vernaculaire ; N4 (premier choix du propriétaire) graduait déjà son échéancier au jour. Natation : profondimètre, ligne d'eau.
- **Le chiffre comme typographie** : le zéro estompé du tuner dit « afficheur » sans dessin.
- **Une dose de caractère** : la mascotte pixel posée sur le bord (franchissement de cadre, quatrième série où il revient).
- **La série de cartes** : forme et place du titre constantes, teinte et type de graphique propres à chaque carte.

Vague à nommer (VEILLE, fréquence NOT-VERIFIED) : widgets « bento » (carrés arrondis, très gros chiffre, accent vert acide, ombre douce, pile de jetons, dégradé vitreux, ce dernier déjà en vague 1).

Vérité : montants et scores fictifs, logos de cryptomonnaies réels ; sur une page produit, à marquer et à ne pas présenter comme résultats.

## Cinquième série d'images (5) : premiers écrans de SaaS IA (2025-2026)

Images : Meetary (bureau macOS, notification « I'll take it from here! » pendant un appel vidéo, puis bandeau de photos sans rapport) ; Finlayer (fenêtre de navigateur, paysage tramé, carte vitrée de question-réponse, logos Google, Payoneer, Stripe, Amazon) ; Chainova (grille de plan apparente, cases hachurées, libellés mono, « 50B+ », cubes isométriques tramés bleu Klein, « Trusted by 500+ », logos) ; Growcode (paysage tramé vert, navigation en pilule, slogan en deux temps) ; Fabric (papier déchiré rouge, extrait de code, slogan en deux temps).

**Lecture : c'est la vague actuelle, presque entièrement nommée par le système.** Vague 3 de `SAVOIR/TOOLS/CONVERGENCE` : tramage, bleu Klein, libellés mono en capitales, hachures de plan, repères de recadrage, paysage peint en fond (Chainova, Growcode, Finlayer). Vague 1 : halos et dégradés (fond macOS de Meetary). Fausses preuves déjà bloquées : plinthe de logos avant l'objet de preuve (`STRUCT-SIGNAUX`), « Trusted by 500+ », chiffres « 50B+ » non sourcés (vérité). Usage : un jeu de calibration négative, ce à quoi ressemble le choix attendu en 2026.

Marqueurs à ajouter en VEILLE (datés, fréquence NOT-VERIFIED, à revoir avant 2027-03) :
- **Slogan en deux temps** (« Build an agent. Give it a job. », « Elevate your brand. Dominate your market. ») ; déjà vu dans les écrans d'app (série 3) et chez N4 (« Facturez une fois. Souche relance jusqu'au paiement. »).
- **Pastille-étiquette au-dessus du titre** (« AI-POWERED MEETING NOTES », « ABOUT US ») ; les pastilles et micro-libellés de nos runs U5 en relèvent.
- **Carte vitrée posée sur un paysage tramé**, dans une fenêtre de navigateur ou de système.

Ce qui reste bon à garder, déjà couvert par `FIRST-OBJECT` et `OBJECT` :
- **Le produit là où il vit, au moment de l'usage** : la notification de Meetary pendant l'appel montre le geste en situation.
- **L'artefact que l'utilisateur écrira** comme preuve : le code de Fabric se termine par sa conséquence (« ticket #4821 resolved »).

Contre-exemple de forme de page : Meetary passe d'un premier écran situé à une section « About us » en deux colonnes de texte, puis à un bandeau de photos d'illustration sans lien avec le produit (œil, montagne, ballon de football).

## Lecture transversale par dimension (les cinq séries, 24 images)

Couverture vérifiée par `read_route.py --trouver` le 2026-10-08. « Couvert » = le système le dit déjà ; « manque » = rien de trouvé.

### Structure
- Couvert : support, grille, scène, objet, micro-unités, signaux de convergence, test de trame.
- Manque : forme de page (arc, fin, série de sections, transitions, fil) ; structure mobile (une décision par écran, zone du pouce, feuille sur contexte) ; franchissement de cadre ; ancrage aux coins ; document ou instrument vernaculaire comme gabarit.

### Savoir (jugement)
- Couvert : premier objet, objet de preuve en situation, convergence, vérité des preuves.
- Manque : mot et image dans le même plan (TXI-01 défensif seulement) ; idée par collision ou contresens ; graphique qui s'annote ; échelle extrême et champ calme majoritaire.

### Système de design (cohérence des composants)
- Couvert : rayons concentriques (`SAVOIR/STATE`), une seule logique de lumière, élévation ou planéité (`ACTION/GATE-C`), tokens et contrats (`BIBLIOTHEQUE/COMPONENTS`).
- Vu dans les références : une famille de rayons tenue (widgets, Plan&go), une hiérarchie de boutons à trois niveaux (plein, teinté, lien : Plan&go), le mobilier de cadre constant d'une série (Matisse, termes solaires).
- Correction : l'état désactivé est couvert (`disabled` dans la liste d'états d'`ACTION/UI-UX-REALITY` ; la recherche en français l'avait manqué).
- Manque : la série de cartes à forme constante et teinte propre.

### Colorimétrie
- Couvert : palette par rôles, contraste calculé, indice non chromatique, question de convergence de palette, dark mode recomposé, OKLCH (`SAVOIR/CRAFT/CFT-05`).
- Vu dans les références : palettes de deux ou trois couleurs (rétro, BORING, main et curseur) ; couleur partagée entre l'image et le texte (le titre vert de rétro reprend les collines ; le ciel dans les lettres de warmth) ; accent prélevé dans l'asset (Originality) ; une teinte dominante par pièce d'une série (termes solaires, cartes de crédit) ; température d'ensemble (chaud délavé de Fieldtrip, chaud de Peloton).
- Manque : la palette dérivée de l'asset ou du sujet ; la couleur qui relie image et texte ; la température et l'étalonnage d'ensemble (une seule occurrence d'« étalonnage », dans l'atlas ; aucune de « température ») ; la retenue du nombre de couleurs comme levier.

### Qualité et finition des assets
- Couvert : provenance et droits, route d'asset (code natif, fourni, généré dirigé), pas d'image de remplissage, traitement par recadrage, duotone, grain ou trame (`SAVOIR/DESIGN-ATLAS`, `SAVOIR/SOURCE`).
- Vu dans les références : un même traitement sur tout un lot (tramage constant de Chainova, aquarelle d'Originality) ; contre-exemple, le bandeau de photos disparates de Meetary (œil, montagne, ballon) ; registre d'illustration professionnel ou enfantin ; étalonnage photo cohérent.
- Manque : la cohérence d'un lot d'assets (aucune occurrence) ; le registre d'illustration ; le critère « l'asset dit-il quelque chose du produit » appliqué à chaque image d'un bandeau, pas seulement au premier écran.

### Finition des composants et du détail
- Couvert : figures tabulaires, alignements, coins concentriques, cibles, états, focus, contraste.
- Vu dans les références : le chiffre comme typographie (zéro estompé du tuner) ; l'icône dans un champ de saisie ; le choix sélectionné marqué par une coche et pas seulement par la couleur (Plan&go) ; la bande basse d'information (termes solaires).
- Manque : rien de structurel ; ce sont des gestes à verser dans les exemples de craft, sans en faire une liste.

### Vérité (rappel)
Logos de marques réelles en preuve sociale, chiffres « 50B+ », « Trusted by 500+ », e-mail d'apparence réelle, fausses métadonnées d'affiche : le système bloque déjà l'essentiel ; la distinction fiction assumée (affiche) / fausse preuve (page produit) reste à écrire.

## ACTION/UI-UX-REALITY : rôle et constats

Rôle : contrat de construction pour une surface UI/UX nouvelle ou très modifiée. Le premier objet doit rendre observables la hiérarchie de contenu, le premier geste et son retour, les états (chargement, vide, erreur, indisponible, désactivé, succès partiel), le contenu long, le responsive recomposé, le focus et la récupération. Neuf lignes (CONTENT-MODEL, PRIMARY-TASK, FIRST-GESTURE, CRITICAL-STATES, RESPONSIVE-RELATION, ACCESSIBILITY-BASIS, ROBUSTNESS-BASIS, EXPECTED-SCOPE, OBSERVED-SCOPE), chacune couverte par OBSERVED, NOT-VERIFIED ou N/A-JUSTIFIED. Pas de gate ni de verdict : ACTION les garde. Chargé d'office en STANDARD et DIRECTION (verrou UIX-01).

Usage observé : les cinq runs U5 et les trois runs « avec » de U3 l'ont ouvert. Effets visibles : formulaires qui valident et confirment, états prévus. Ses lignes n'apparaissent pas nommément dans les traces plafond.

Constats :
1. **L'état vide devenu premier écran.** Les juges reprochent à plusieurs pages de natation un « panneau de résultat vide au premier écran » (J09, J10, J21, J22). L'état vide était prévu, comme le demande la route, mais rien ne dit quel état le visiteur voit d'abord. Les références font l'inverse : Numi et Plan&go ouvrent sur un état rempli (un exemple montré) et gardent l'état vide pour l'usage.
2. **RESPONSIVE-RELATION pose la bonne question sans savoir derrière** : « ce qui est préservé, recomposé ou remplacé ». Le savoir de structure mobile (une décision par écran, zone du pouce, feuille sur contexte) manque pour y répondre.
3. **C'est un contrat de couverture, pas un savoir d'interface** : il dit quoi rendre observable, pas comment le rendre bon. Plan&go est un bon exemple de ce que le contrat vise (état désactivé, retour « Tickets uploaded », une tâche par écran).

## Sixième série d'images (5, dont Meetary déjà vu)

Images : Vaultline (tournesols peints, puis pied de page) ; Veloscope (prairie peinte plein cadre, navigation en capitales espacées, « (4 CURRENT OPENINGS) ») ; tarifs (crème, cadres hachurés, trois cartes teintées anthracite, sauge, terre cuite) ; gestionnaire de mots de passe (titre gris puis noir, onglets, carte produit sur paysage tramé en caractères) ; Meetary (doublon de la série 5).

Par dimension :
- **Assets et vague.** Le paysage peint « façon animation » revient dans cinq des dix dernières images (Vaultline, Veloscope, Growcode, Finlayer, mots de passe) : marqueur « paysage peint en fond » de la vague 3, confirmé. Aucun ne dit quelque chose du produit (des tournesols pour un outil de développement, une prairie pour de l'ingénierie) : nouveau cas pour le critère « l'asset dit-il quelque chose du produit ». L'apparence ne permet pas d'attester une génération par IA.
- **Typographie et vague.** Titre bicolore gris puis noir pour l'emphase (mots de passe ; « Built to Capture What Matters » de Meetary) : marqueur à ajouter en VEILLE.
- **Structure, forme de page.** Vaultline montre une fin correcte : une dernière scène (image et action) puis un colophon (marque, plan du site, réseaux, lettre d'information, mentions). Le gestionnaire de mots de passe remplace la rangée de cartes de fonctionnalités par des **onglets** qui montrent une fonctionnalité à la fois avec une vraie vue produit et ses états (Compromised, Weak, Reused) : alternative structurelle à la rangée de cartes.
- **Structure, cartes.** Les trois cartes de tarifs sont un usage légitime : objets séparables à comparer. Elles illustrent aussi la série à forme constante et teinte propre. Leur peau (crème, terre cuite, sauge, hachures) relève des vagues 2 et 3.
- **Rédaction.** « (4 CURRENT OPENINGS) » chez Veloscope : un signal précis et vérifiable en action secondaire, plus spécifique qu'un deuxième bouton générique.
- **Finition et vérité.** Le gestionnaire de mots de passe associe le logo de Framer au nom « Dribble » (erreur d'asset), et affiche des logos de marques réelles et une adresse e-mail réaliste. Vaultline pose un petit émoji de tournesols sous le bouton (détail parasite). Les boutons mêlent anneau vitré (Vaultline) et ombre portée lourde (mots de passe) : deux logiques d'élévation différentes d'un site à l'autre, chacune à tenir seule sur sa surface (`ACTION/GATE-C`).

## Septième série d'images (5) : système, données, composants, identité

Images : DevLabs (page sombre, gravure orange de coureurs sur grille, bord pixelisé, bandeau de logos, cartes de chiffres, photos en bichromie) ; tableau de bord SEO sombre ; deux cartes de réservation d'expert (pastels peints, titre à empattements) ; comparaison « Left / Right » d'une même carte ; charte de marque Mimo (logo, déclinaisons, typographies, palette).

Par dimension :
- **Cohérence d'un lot d'assets (cas positif).** DevLabs passe toutes ses images, illustration et photos, dans le même traitement (bichromie orange et vert, trame) : c'est l'exemple inverse du bandeau de Meetary. Le traitement commun fait tenir des sources disparates.
- **Transition.** Le bord pixelisé de DevLabs (l'image se dissout en carrés) est une transition dessinée, cohérente avec un sujet de développeurs. Même famille que le bord peint des termes solaires.
- **Données (tableau de bord SEO).** Bien couvert par `MICRO/QUERY_HEALTH`, et la référence le montre bien : chaque chiffre porte sa comparaison (« vs. previous 30 days »), des pastilles affichent le périmètre et la période (« Scope: Root domain », « Historical data »), une moyenne est marquée sur les courbes, et un segment hachuré distingue une série sans compter sur la couleur seule (indice non chromatique déjà exigé par `CFT-05`). Palette rose, bleu et violet : vague 1.
- **Finition de composant.** Cartes d'expert : bouton aligné en bas quelle que soit la longueur du texte, beaucoup d'air, un repère de marque discret dans le coin. « Left / Right » : un avant/après purement esthétique (icône dans l'étiquette, flèche dans le bouton, dégradé adouci). La version de droite est plus finie mais plus générique ; `BIBLIOTHEQUE/MICRO` (avant/après) exige déjà qu'une comparaison valide une hypothèse, pas une impression de modernité : bon cas d'école.
- **Système d'identité (Mimo).** Logo qui se simplifie selon la taille (version détaillée en grand, réduite en petit, échelle 32 à 220 px) ; deux typographies à rôles distincts (Hedvig, GT Walsheim) ; couleurs nommées avec valeurs et teintes ; une famille d'assets (illustration au trait, motif, carte typographique). Le système couvre tokens et composants, pas la **simplification progressive d'une marque selon la taille** (aucune occurrence) ; utile si un run crée un logo ou un pictogramme.
- **Finition et vérité.** La charte elle-même contient des erreurs : diapositive de couleurs titrée « Typeface system », « Scalling », même code couleur pour deux teintes différentes. Les logos du bandeau DevLabs sont des marques fictives présentées comme clients (« Used by startups and small businesses »), et la carte « Left / Right » utilise une marque réelle (OpenAI). Les chiffres « 2000+ », « $150K+ » ne sont pas sourcés.

## Axes de jugement du système non encore appliqués aux références

Grille du système : CFT-00 (présence, point de vue, culture visuelle, spécificité, composition, désirabilité, résolution, retenue), axes V/U/A/T d'`ACTION/STATUS`, critères C1 à C6 de Gate C, `SAVOIR/CONTEXT`. Les lectures précédentes ont surtout porté sur V, composition, spécificité, résolution et vérité. Limite : sur des images fixes, U, A et T ne sont jugeables qu'en partie ; mouvement, clavier, lecteur d'écran et performance restent NOT-VERIFIED.

- **U, compréhension et usage.** Sait-on en cinq secondes ce que c'est, pour qui, et quoi faire ? Fort : Plan&go (une tâche par écran), Meetary (le geste en situation), tableau SEO (comparaison et période). Faible : Veloscope et Growcode (slogan abstrait, paysage sans lien : on ne sait pas ce que fait l'entreprise), BORING et warmth (affiches, pas de tâche, normal pour le médium). Nos runs U5 : tâche claire, mais noyée sous les libellés.
- **A, accessibilité.** Risques visibles : titres bicolores gris clair sur fond clair (mots de passe, Meetary) ; petits libellés mono gris (Chainova, SEO) ; texte posé sur peinture ou trame (Veloscope, Growcode, Finlayer) ; état porté par la couleur seule dans certaines cartes. Bons gestes : segment hachuré du tableau SEO, coche en plus de la couleur (Plan&go), cibles larges des écrans mobiles. Le mot posé dans le même plan que l'image (affiches) est un risque de lisibilité à mesurer à chaque largeur.
- **T, robustesse.** Paysages peints et images tramées plein cadre : poids et chargement ; la trame fine se dégrade à la compression et au redimensionnement. Franchissement de cadre et mot derrière un sujet : à recomposer sur mobile, sinon ils cassent. Les références sont des captures fixes : aucune ne prouve son comportement responsive.
- **Culture visuelle (références transformées ou copiées).** Transformées : la main de Michel-Ange devenue curseur ; le formulaire d'autorisation de sortie devenu affiche ; les tampons de passeport de Plan&go. Reprises sans transformation : le paysage façon film d'animation (cinq sites), le dégradé macOS. C'est le critère qui sépare le mieux la matière utile de la vague.
- **Désirabilité.** Donne-t-elle envie d'entrer, sans manipulation ? Fort : rétro, termes solaires, Kidory, Numi. Manipulation douce à surveiller : fausses preuves sociales (logos, « Trusted by 500+ »), urgence (« 4 current openings » est vrai et sobre, à l'inverse).
- **Retenue.** Fort : BORING, la main et le curseur, les cartes d'expert. Faible : Chainova (grille, hachures, chiffres, cubes, logos tous ensemble), Meetary (bandeau de photos ajouté), nos runs U5 (pastilles et mentions partout).
- **Contexte (`SAVOIR/CONTEXT`) et éthique.** Les termes solaires sont lisibles dans leur culture (calendrier chinois, calligraphie) : la transposition hors de ce contexte demande prudence. Finlayer donne un conseil d'investissement chiffré dans son exemple : un contexte critique (finance) traité comme décor. Score de crédit et portefeuille crypto : données sensibles, à marquer comme fictives.
- **Voix et rédaction.** Formules répétées (slogan en deux temps, « All in one place », « Stand out »). Voix forte : BORING (contresens), Fieldtrip (« Destination Uncertain »), la notification de Meetary (« I'll take it from here! »), la phrase d'humour de « Stand out » sur les bonbons à l'orange.
- **Mouvement.** Non jugeable sur image fixe ; à observer en rendu (transitions de section, franchissements, bord pixelisé qui pourrait s'animer).

## Huitième série d'images (5), lue sur la grille complète

Images : publication « Alternative Off-White Colors to #FFFFFF » (huit blancs cassés attribués à des marques) ; carte « Real-Time Alerts » (barres d'usage, plafond hachuré, seuil en pointillé rouge) ; carte « Support Analytics » (2450 tickets, ligne d'objectif, tableau Actual / Avg avec statut écrit) ; application de santé (tendances, phases de sommeil, olive et jaune) ; pied de page Jooba (brun sombre, logo géant qui émerge sur une bande de paysage granuleux).

- **Colorimétrie : le blanc est une décision.** Le fond blanc a une température (chaud, froid, neutre) et la publication le montre bien. Le système n'en dit rien (aucune occurrence de « température », une seule de « fond blanc », dans un marqueur de vague). Le blanc cassé chaud recoupe la vague 2 (fond crème). Vérité : l'attribution des valeurs aux marques vient d'une publication de réseau social, non sourcée ; à ne pas reprendre comme fait (`CFT-05` exige source et date pour tout claim de palette).
- **Données : la couleur suit le sens, pas le signe.** Dans « Support Analytics », un temps de réponse en baisse (−22 %) est vert parce que c'est bien ; un CSAT en baisse (−0,3 %) est rouge. Le statut est aussi écrit (« Below SLA », « Meeting SLA », « Above Target ») : pas de couleur seule. Ligne d'objectif (« Target : 30m ») et jour courant mis en avant. « Real-Time Alerts » : plafond montré en barre fantôme hachurée, seuil en pointillé, conséquence écrite (« notifications à 80 % d'usage »). C'est `MICRO/USAGE_LEDGER` et `QUERY_HEALTH` parfaitement appliqués ; la **polarité de la couleur selon le sens de la mesure** n'est écrite nulle part dans le système.
- **Vérité et usage : des données d'exemple incohérentes avec le métier.** L'application de santé est soignée mais son contenu est faux pour le domaine : légende « Meditation, Back Pain, Walking » sur des phases de sommeil, une fréquence cardiaque en millisecondes, une température corporelle de −3,7 °C. Le système exige un contenu d'exemple **plausible et marqué** (`DIRECTION/EXTERNAL-START`), mais pas sa **cohérence de domaine** (unités, catégories, ordres de grandeur). Manque à ajouter : un exemple faux pour le métier abîme la confiance autant qu'une fausse preuve.
- **Structure : la fin comme dernière scène (Jooba).** Phrase de clôture avec un point de vue (« Your perfect hire won't apply. Let's reach them for you. »), action, navigation numérotée en deux groupes (01, 02), mentions, puis le logo géant qui déborde sur une bande de paysage granuleux : la marque referme la page en franchissant le cadre. Meilleur exemple de fin de page de toute la matière. Peau : brun, crème, grain (vague 2).
- **Accessibilité.** Textes gris clair de petite taille (dates de « Real-Time Alerts », libellés de l'application de santé), chiffres mono très petits ; jaune pâle sur blanc cassé dans les graphiques de sommeil. Bons gestes : statuts écrits, ligne d'objectif étiquetée.
- **Culture, désirabilité, retenue.** Retenue forte : « Real-Time Alerts » (une carte, une question). Désirabilité : Jooba. Culture visuelle : rien de transformé ; ce sont des pièces de bonne exécution, pas de références détournées.
- **Voix.** Spécifique et concrète : « long before invoices explode » ; « Your perfect hire won't apply ».


## Intégration (2026-10-08)

| Matière | Intégrée dans | Commit |
|---|---|---|
| Forme de page : arc, série, moment de champ, transition, fil, fin et colophon ; trame sur toute la page ; cartes et onglets | `BIBLIOTHEQUE/SEQUENCE` (nouvelle route), chargement conditionnel en mode DIRECTION | `d11b8ff` |
| Structure mobile : une décision par écran, zone du pouce, feuille sur contexte | `BIBLIOTHEQUE/SEQUENCE`, « Structure mobile » | `d11b8ff` |
| Document ou instrument du métier comme objet | `BIBLIOTHEQUE/OBJECT`, « Objet du métier » | `d11b8ff` |
| Mot et image dans le même plan ; échelle et champ calme ; franchissement et ancrage aux coins | `SAVOIR/CRAFT/CFT-03` ; renvoi dans TXI-01 du noyau | `6506e3e` |
| Idée par rapprochement ou contresens | `SAVOIR/CRAFT/CFT-01` | `6506e3e` |
| Couleur située : palette tirée du sujet, lien image-texte, température du fond, retenue | `SAVOIR/CRAFT/CFT-05` | `6506e3e` |
| Lot d'assets, pertinence de chaque image, registre d'illustration | `SAVOIR/SOURCE` | `f059f96` |
| Graphique annoté, repère, couleur selon le sens de la mesure | `BIBLIOTHEQUE/MICRO` | `f059f96` |
| Premier état montré (rempli, pas vide) | `ACTION/UI-UX-REALITY` | `f059f96` |
| Cohérence de domaine des exemples ; fiction assumée contre fausse preuve | Noyau, bloc du contenu | `f059f96` |
| Marqueurs : slogan en deux temps, pastille-étiquette, titre en deux tons, carte vitrée sur image de fond, widget à gros chiffre | `SAVOIR/TOOLS/CONVERGENCE`, [VEILLE 2026-10] « Signaux de page » | `18055c3` |

Non intégré, par choix : simplification d'un logo selon la taille (utile seulement si un run crée une marque) ; texte vertical, calligraphie et bord peint (couverts par la comparaison de voix et la matière conçue existantes). Aucun effet sur les rendus n'est mesuré à ce jour.
