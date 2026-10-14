# Comparaison textuelle : capacité esthétique et design, Design Governance (DG) contre Taste Skill v2 (TS)

> **Statut.** Document de travail, **hors paquet**, sur la branche orpheline `suivi-comparaison-taste-skill`. Complète `SUIVI.md` (manche 6).
> **Méthode.** **Lecture seule : aucun outil de TS ni de DG n'a été exécuté pour ce document** (seuls des fichiers ont été lus, comptés ou extraits). Les résultats d'exécution sont dans `SUIVI.md` (manches 3 et 5). Chaque affirmation cite le fichier et la section lus. Date : 2026-10-14.
> **Ce que « capacité » veut dire ici.** Ce qu'un agent peut faire avec le texte seul : une valeur à utiliser, une procédure à suivre, un critère pour trancher, un contrôle pour vérifier. Aucun avis sur la qualité des rendus produits : ni TS ni DG n'ont montré qu'ils battent un modèle sans skill (TS l'a testé et perd, `research.md` §11 ; DG ne l'a pas testé).

## 0. Fichiers lus pour ce document

| Côté | Fichiers (lus en entier sauf mention) |
|---|---|
| TS | `SKILL.md` ; `references/` : `type`, `colour`, `layout`, `imagery`, `motion`, `copy`, `critique`, `tells` ; `library/` : une entrée de `directions`, `heroes`, `sections`, `motions` et la liste des 20 directions (les 7 fichiers de données ne sont pas lus en entier : 172 sections, 48 héros, 56 palettes, 44 systèmes typographiques, 181 sites) |
| DG | `design/savoir/` : `typographie`, `qualite-creative` (CFT-00 à CFT-06), `composition` (STATE), `styles`, `images-et-sources`, `contexte`, `techniques`, `gout-et-tendances`, `fondements` (70 premières lignes) ; `design/direction/` : `premier-objet`, `diriger`, `boucle`, `cadrer` ; `design/formes/` : `choisir` en entier, `catalogue` (supports, grilles, scènes, séquence, objets, début des micro-interfaces ; pas les composants ni la compatibilité) |
| Non lus pour ce document | DG : `produit/*`, `direction/standard`, `savoir/connexions`, `savoir/systeme-de-design`, `gouvernance/*` (lus en manche 4), fin de `catalogue` ; TS : `research.md` (lu en manche 5), `probe.mjs`, `assets.mjs`, `base.css` |

## 1. Lecture d'ensemble

1. **Deux couches différentes.** TS dit **quoi mettre** : valeurs, géométrie, recettes de code, jeux de données. DG dit **comment décider et comment vérifier** : critères, gestes conditionnels, contrats de preuve. Ce ne sont pas deux réponses à la même question.
2. **Test d'opérabilité.** Pour la typographie, la couleur, la mise en page et le mouvement, un agent peut appliquer TS tel quel (tailles, interlignes, proportions, durées, CSS). Avec DG seul, il applique des questions et des gestes, sans valeur de départ. Les valeurs que DG a depuis (`POINTS-DE-DEPART`, `CFT-06`) viennent de TS, datées et marquées « à revérifier ».
3. **Seule DG a** : la protection des risques critiques, les états et la récupération d'erreur, l'accessibilité comme plancher, les supports non web, le marquage de vérité de la scène, la preuve typographique en cinq axes, la table de gestes de craft avec condition et réinspection.
4. **Seule TS a** : la matière concrète (une géométrie de bureau et de mobile par section et par héros), l'inventaire du sujet et la phrase d'idée, le tirage externe, la recherche d'images libres, les jetons et recettes de mouvement, les 14 passes de regard avec leur garde-fou contre l'épure.
5. **Convergences indépendantes** (section 4) : les deux écrivent la même règle de vérité, le même diagnostic de la « vague crème », la même méfiance envers les listes de remplacement.
6. **Contradictions de fond** (section 5) : interdits ou noms, mouvement obligatoire ou justifié, plancher d'images réelles ou `SANS-ASSET` à égalité, score chiffré ou aucun score, accent unique ou palette plurielle.
7. **Chaque système se contredit lui-même sur un point** (section 6) : TS (direction `stillness` contre son contrôle `still-page`) ; DG (traitements « duotone, grain ou trame » contre ses marqueurs de vague).

## 2. Tableau de verdicts

| # | Catégorie | Équivalent ? | Plus exécutable (par lecture) | Plus prudent ou robuste | Écart principal |
|---|---|---|---|---|---|
| 1 | Typographie | En partie (titres, chiffres, voix) | **TS** : échelle, composition du titre et du texte, chargement | **DG** : langue, reflow, zoom, preuve en 5 axes | TS donne des valeurs, DG des critères ; TS signale les « polices par défaut », DG dit qu'une famille fréquente n'est pas un défaut |
| 2 | Couleur | En partie (rôles, mode sombre, teinte tirée du sujet) | **TS** : proportions, champs de couleur, surfaces par teinte | **DG** : indice non chromatique, palette plurielle | Accent unique sous 5 % (TS) contre « ne pas réduire à un accent unique par réflexe » (DG) |
| 3 | Composition et structure | En partie (séquence, trame, mobile recomposé) | **TS** : marges, ligne d'ancrage, vides, géométrie de chaque section | **DG** : chaîne support → grille → scène → objet, tensions, signature, condition de sortie | Matière (TS) contre logique de choix (DG) |
| 4 | Direction et idée | Oui dans l'esprit | **TS** : inventaire de 8 à 12 éléments, phrase d'idée, tirage | **DG** : cible visuelle, vérité de scène, plafond de fabrication | Pas d'inventaire du sujet chez DG |
| 5 | Styles et directions | Non | **TS** : 20 directions complètes | **DG** : profils avec contre-indications, 9 réglages | Un « look » prêt à construire (TS) contre des couches à combiner (DG) |
| 6 | Images | Oui sur l'ordre de préférence et sur les droits | **TS** : recherche, critères, recadrage, traitements, vidéo | **DG** : fiche de source, réserve sur image générée, contre-épreuve | Plancher de 4 images réelles (TS) contre `SANS-ASSET` à égalité (DG) |
| 7 | Mouvement | Non | **TS** : jetons, durées, 10 recettes | **DG** : états, interruption, rappels périmés | Mouvement obligatoire (TS) contre mouvement justifié (DG) |
| 8 | Rédaction | Oui depuis `CFT-06` (adapté de TS) | **TS** (garde-fou outillé par `lint`) | **DG** : contre-indications, langues sans espaces | Reste : l'outillage |
| 9 | Critique du rendu | En partie | **TS** : 14 passes, score, plafonds | **DG** : diagnostic → geste, test de résilience | Score chiffré (TS) contre aucun score (DG) ; contrepoids anti-épure chez TS seulement |
| 10 | Convergence | Oui sur le diagnostic | **TS** : registre daté avec statut banni ou signalé | **DG** : marqueurs jamais interdits, sources datées | Interdire (TS) contre nommer (DG) |
| 11 | Interfaces, états, accessibilité | Non | — | **DG** | TS v2 exclut les écrans d'application (`SKILL.md`, description) |

## 3. Détail par catégorie

### 3.1 Typographie

**TS** (`references/type.md`) : mesures sur 202 sites (§1 : titre d'accueil médian 72 px, soit 5 vw ; 6 vw chez les mieux notés ; rapport titre sur corps 4,3 ; deux familles en médiane) ; échelle de cinq tailles au plus, écartées, avec jetons `clamp()` (§2) ; réglage du grand texte : interligne 0,85 à 1,05, approche de −0,02 à −0,05 em, plus serrée quand le corps grandit, alignement optique de −0,05 em pour les lettres rondes, taille en `vw` calculée sur le nombre de caractères (§3) ; texte courant : 62 ch, interligne 1,45 à 1,6, jamais de paragraphe centré sur plus de trois lignes (§4) ; procédure de chargement des polices avec repli (§5) ; une ou deux familles (§6) ; détails (chiffres tabulaires, soulignement, `hyphens: none`, espace au-dessus d'un titre au moins double de celui du dessous, `::selection`) (§7) ; erreurs que l'inspecteur ne voit pas (§8).

**DG** (`design/savoir/typographie.md`, 565 mots) : choisir pour les langues, chiffres, ponctuation, graisses, lisibilité, licence, performance, repli et ton ; « une famille fréquente n'est pas un problème en soi, le problème est le réflexe sans alternative comparée » ; une ou deux voix expressives (`[À ADAPTER]`) ; polices variables et leurs axes ; signature typographique qui doit survivre au zoom, au reflow et à la locale ; `COMP-TITRE` (équilibre d'un titre : sens, forme, hiérarchie ; un mot isolé voulu se garde) ; preuve typographique en cinq axes (`FORM-LEGIBILITY`, `TEXT-READABILITY`, `HIERARCHY`, `PERSONALITY`, `TASK-EFFECT`) avec un tableau (spécimen de rôle, résilience, rendu, décision). Ajouts récents, venus de TS : points de départ chiffrés et budget de titre (`POINTS-DE-DEPART`, `CFT-06`).

**Équivalences.** Équilibre et mot isolé (`COMP-TITRE` ↔ `type.md` §8 et `copy.md` §2) ; `text-wrap: balance` ; chiffres tabulaires (ligne « Chiffres » de `STATE` ↔ `type.md` §7) ; alignement optique (ligne « Alignement optique » de `STATE`, essai d'un décalage local de 1 px ↔ `type.md` §3) ; une ou deux voix.

**Seulement TS.** Valeurs par rôle ; approche et interligne par taille ; vérification des collisions d'un interligne inférieur à 1 ; taille en `vw` calculée ; chargement des polices ; règle 2 pour 1 de l'espace autour des titres ; interdiction d'ombre, de contour et de dégradé sur un grand texte.

**Seulement DG.** Langue, chiffres, licence, performance ; axes d'une police variable ; preuve en cinq axes ; « une famille n'est jamais déclarée supérieure sur une impression de marque » ; comparer au moins deux voix sur le vrai titre (`COMP-CONVERGENCE`).

**Divergence.** `lint.mjs` de TS signale comme « police par défaut » (WARN) Inter, Poppins, Montserrat, Roboto, Space Grotesk, Instrument Serif, Playfair Display, Plus Jakarta Sans, Outfit, Sora et quelques autres, et dit « utilise les polices de la direction tirée ». DG dit l'inverse sur le principe : une famille courante reste valide si le choix est comparé et justifié.

**Lecture.** Pour régler un grand titre et un texte courant, TS est directement exécutable et DG laisse l'agent à ses défauts (hors `COMP-TITRE`). Pour tenir une typographie dans une langue autre, au zoom ou au reflow, ou la prouver, DG est le seul. Les facteurs `k` du budget de titre supposent des écritures à espaces ; `CFT-06` le dit en contre-indication, `copy.md` non.

### 3.2 Couleur

**TS** (`references/colour.md`) : mesures (§1 : 41 % de pages sombres, boutons neutres sur 52 % des sites, dégradés sur 22 % des mieux notés contre 52 % des moins bien notés) ; six rôles en jetons (`--bg`, `--surface`, `--ink`, `--muted`, `--accent`, `--accent-ink`), « une couleur brute dans un composant est une seconde palette qui commence » ; proportions (sol 70 à 90 %, accent sous 5 % de l'écran, jamais sur titres, icônes, puces, filets) ; surfaces séparées par un pas de teinte, sans ligne ni ombre ; **champs de couleur** par section (limites franches, encre propre à chaque champ, champs voisins différant en clarté) ; pages sombres ; couleur et photographies (interface neutre, teinte d'encre prise dans l'image, voile neutre) ; contraste (4,5 pour le corps, 3 pour le grand texte) ; familles interdites (crème avec terracotta, violet et indigo) avec la procédure pour obtenir de la chaleur sans beige.

**DG** (`qualite-creative.md`, `CFT-05`) : palette par rôles (surfaces, textes, actions, états, frontières) ; « la répartition entre neutres et couleurs est une décision de direction » ; identité multicolore ou codage par zones recevables si rôles, états, contraste calculé et indice non chromatique tiennent ; `COMP-CONVERGENCE` (cette palette et cette police sont-elles celles que le modèle produirait sans brief ?) ; **couleur située** (teintes prises dans l'image ou la matière du produit, température du fond nommée, deux ou trois couleurs tenues) ; OKLCH comme espace de conception ; mode sombre recomposé, non inversé ; gamut élargi sans information indispensable ; contraste calculé, jamais jugé à l'œil.

**Équivalences.** Rôles ; mode sombre recomposé ; teinte tirée du sujet (`CFT-05` « couleur située » ↔ `colour.md` §7, « the ink from the darkest tone in the imagery ») ; texte sur image : zone calme ou voile local (`COMP-TEXTE-IMAGE` ↔ `colour.md` §7).

**Seulement TS.** Proportions chiffrées ; champs de couleur comme remplacement des séparateurs, des cartes et des décors ; accent réservé à l'action ; surfaces par pas de teinte ; jetons obligatoires ; liste de familles refusées et procédure de chaleur.

**Seulement DG.** Indice non chromatique ; gamut ; OKLCH ; claims de couleur soumis à `SAVOIR/TOOLS` ; palette plurielle recevable.

**Divergence franche.** Accent unique sous 5 % (TS) contre « ne pas la réduire à un accent unique par réflexe » (DG, ligne « Accent » de `STATE`). TS l'admet partiellement : ses palettes à champs plats multiples suivent d'autres règles (`colour.md` §3).

**Lecture.** TS donne une grammaire de proportions qu'un agent peut appliquer sans l'avoir jamais vue ; DG donne les rôles et la discipline de contraste, et ses proportions chiffrées viennent de la section datée `POINTS-DE-DEPART`.

### 3.3 Composition et structure

**TS** (`references/layout.md`, `library/sections.json`) : ce que font les pages fortes (marges de 32 px ou moins pour environ 45 des 114 retenues, texte accroché à une ligne hors centre, deux ou trois tailles, un objet par écran, sections distinguées par leur fond, système rompu une fois exprès, souvent pas de barre de navigation, mots peu nombreux) ; code de marges et de grille ; ligne d'ancrage réutilisée sur toute la page ; vide placé, jamais résiduel ; écart entre sections nettement supérieur à tout écart interne (120 à 220 px) ; **deux sections voisines ne partagent pas la même mise en page** ; module répété réservé aux archives ; navigation, fin de page, **mobile comme seconde composition** ; échecs comptés sur 54 sites. La bibliothèque donne pour chacune des 172 sections un paragraphe de géométrie chiffrée, une variante mobile, les directions compatibles et les sites où elle a été vue (entrée lue : `features-capabilities-at-poster-scale`, liste de 5 à 8 noms à `clamp(40px, 5.2vw, 84px)`, descriptions en colonnes 9 à 12 alignées sur la première ligne de base, 18 à 22 vh de sol vide autour).

**DG** : `STATE` (« jugement visuel situé » : 6 lentilles, 3 niveaux Correction, Précision, Intention ; **table de 13 gestes** : cohérence de rayon avec la formule « rayon intérieur = max(0, rayon extérieur − inset) », masse, vide, silhouette, surface, chiffres, accent, détail révélateur, texte secondaire, états, alignement optique, image intégrée, mouvement) ; `CFT-03` (alignements, compensation optique, proximité, responsive comme recomposition ; texte sur image ; mot et image dans le même plan ; échelle et champ calme ; franchissement et ancrage) ; `FND-01` (grammaire : intention → tension → foyer → masse → rythme → matière et type → contenu réel → états → résolution → retenue) ; `choisir.md` (chaîne support → grille → scène → objet → primitive ; sept axes de tension ; signature structurelle ; thèse structurelle ; test de trame ; signaux de convergence ; dérivation locale) ; `catalogue.md` (4 supports, 6 grilles, 6 scènes, 9 objets, 7 micro-interfaces, 3 modificateurs, chacun en 3 à 5 lignes avec « choisir lorsque » et « éviter lorsque » ; contrat de grille avec `UNIT`, `MARGIN + GUTTER`, `ANCHORS`, `RHYTHM`, familles `MOBILE-*`) ; `SEQUENCE` (arc, série, moment de champ, transition, fil, fin).

**Équivalences.** « Sections recomposées, pas répétées » (TS §5) ↔ `SEQUENCE` « série » et test de trame appliqué à toute la page ; « un objet par écran » ↔ « moment de champ » et « échelle et champ calme » ; « l'idée survit jusqu'au dernier pixel » ↔ « trame sur toute la page » ; fin de page dessinée ↔ « fin » ; cartes réservées aux objets séparables (TS « module répété pour les archives ») ↔ `SEQUENCE` « cartes » ; mobile recomposé (TS §8) ↔ « recompose plutôt que comprimer » (`CONTEXT`) et « structure mobile ».

**Seulement TS.** Chiffres (marges, écarts, parts de sites) ; ligne d'ancrage ; géométrie par section ; navigation et fin de page spécifiées ; « ne jamais dessiner la grille » ; statistiques d'échec.

**Seulement DG.** Applications et micro-interfaces (instrument, grille opérationnelle, valeur de contrôle, journal d'usage) ; chaîne de responsabilités ; axes de tension avec pôle retenu et conséquence ; signature avec limite antérieure et condition de sortie ; gestes avec condition et réinspection ; états.

**Divergence.** Un exemple précis : `CFT-03` de DG dit que « de petits repères placés aux coins peuvent tenir un grand champ sans cadre ni carte » ; TS interdit « crosshairs, crop marks » (`tells.md` §4, `layout.md` §2). DG range pourtant « repères de recadrage » parmi les marqueurs de la vague 3 (`gout-et-tendances.md`, `CONVERGENCE`) : voir 6.

**Lecture.** Un agent construit directement une section depuis une entrée de TS. Depuis DG, il choisit une route par ses conditions, puis dérive : `BIBLIOTHEQUE/DERIVE` demande huit lignes avant build, mais aucune valeur. DG décide mieux ce qu'on construit, TS dit comment le construire.

### 3.4 Direction et idée

**TS** (`SKILL.md` étapes 1 à 4) : **inventorier le sujet** (8 à 12 éléments qui appartiennent à ce client et à aucun concurrent : le nom et son sens, l'adresse, le lieu et ce qu'il donne à voir, les nombres du brief, la contrainte, les matériaux, les rituels, les objets imprimés de son monde) ; écrire l'argument en revendications avec preuve ; tirer trois directions sur vingt et en choisir une contre l'inventaire ; **phrase d'idée** « Sur cette page, [quelque chose qui appartient au sujet] devient [le dispositif que la direction appelle] » avec sept lieux où chercher (sa production, son objet, son nom, son lieu, son rituel, son artefact, son opposé) ; **test du concurrent** ; **une chose vivante** (un geste ou un état différent à chaque visite). Preuve invoquée : en aveugle, la page gagnante de chaque brief venait d'un élément de l'inventaire (`SKILL.md` §1).

**DG** : `VISUAL_TARGET` (11 champs : thèse, conséquence observable, ancre, silhouette, relations de plans, opération dominante, matière ou asset, typographie, objet de preuve, modal et parti, résolution initiale) ; `CREATIVE-BOOT` (décision, promesse, objet de preuve, geste, modal, parti, tension, signature, trois qualités prioritaires, `FABRICATION`, premier objet, défaut dominant) ; `FIRST-OBJECT` (promesse → objet de preuve → geste ; marquage `TRUTH/*` ; contrat de huit dimensions) ; `DIRECTION-ATELIER` (moment humain, tension, geste produit, position et exclusion, contre-choix situé) ; `CFT-01` (idée par rapprochement de deux registres) ; `CFT-02` (axes de position).

**Équivalences.** « L'idée vient du sujet, pas de la catégorie » (TS) ↔ test de singularité (« si le logo et le nom disparaissent, qu'est-ce qui reste ? », `COMP-SINGULARITE`) et `MODAL`/`PARTI` ; test du concurrent ↔ `MODAL` (ce que n'importe quelle IA produirait ici) ; chose vivante ↔ geste produit et objet de preuve « de préférence codé » ; argument avant la page ↔ test de trame (`choisir.md`) et `CFT-06` ; brief vague : TS « décide et dis ta lecture en une ligne, demande seulement si un fait bloque » ↔ `EXTERNAL-START`, « au plus trois demandes, le build se fait dans le même tour » ; détails d'exemple attendus et signalés (TS étape 5) ↔ `CNT-01`, `EXD-01`.

**Seulement TS.** L'inventaire du sujet, la phrase d'idée à deux blancs, la liste de sept lieux où chercher, la mise en relation « inventaire = requêtes de recherche d'images » (étape 6).

**Seulement DG.** `FABRICATION` (plafond par couche selon les moyens réels : structure, typographie, couleur, assets, contenu), destination (démo ou produit réel), marquage de vérité de la scène, réserve quand la direction n'est calibrée que sur une image générée (`diriger.md`), contre-choix.

**Lecture.** Même exigence, deux méthodes. DG cadre et protège ; TS fournit une **procédure de génération** de l'idée. La recherche dans `design/direction`, `design/savoir` et `design/produit` ne trouve aucun équivalent de l'inventaire du sujet ; le plus proche est `DOMAIN-FRAME` (public, JTBD, modèle de confiance), qui décrit un domaine et non ce que ce client est seul à avoir.

### 3.5 Styles et directions

**TS** : 20 directions (`name-as-monument`, `sentence-as-layout`, `pinned-poster`, `colour-chapters`, `one-motif`, `product-performs`, `quiet-instrument`…), chacune avec idée, composition, typographie (classes), couleur (étiquettes), images, mouvement et « richesse » ; entrée lue : `name-as-monument` (le nom comme architecture, 16 à 24 vw, marges de 20 à 32 px, deux tailles qui font presque tout, pied de page qui reprend le nom en couleurs inversées). 56 palettes, 44 systèmes typographiques, 48 héros, indexés par secteur et ton. Pas de réglages chiffrés (« dials ») dans la v2 par défaut : ils sont dans la variante expérimentale (`CHANGELOG`, `README`).

**DG** (`styles.md`) : 8 profils (`RAW_BRUTALISM`, `EDITORIAL_PRECISION`, `PICTORIAL_UTILITY`, `QUIET_SYSTEM`, `MAXIMAL_EXPRESSION`, `DIGITAL_MEMORY`, `TACTILE_VOLUME`, `COLLAGE_ASSEMBLY`), chacun avec intention, expression, contre-indications ; taxonomie en 7 dimensions ; **9 réglages qualitatifs** (variance, motion, densité, contraste, matérialité, voix typographique, formalité, intensité émotionnelle, originalité) avec pôle bas, pôle haut et vérification ; test de style (masquer couleurs, image et logo) ; « aucun profil n'est choisi par défaut » ; l'absence de profil est une sortie valide ; table du vocabulaire faible (« premium », « moderne », « seamless »… à rendre observable).

**Équivalences.** Aucune des deux ne traite le style comme une étiquette. TS : « la direction est une façon de composer, l'idée vient du sujet ». DG : « un profil règle une manière d'exprimer une décision, il ne choisit ni JTBD, ni support, ni grille, ni scène ».

**Différence structurelle.** Une direction de TS prescrit d'un coup composition, typographie, couleur, images et mouvement : un « look » prêt à construire, tiré au sort. DG sépare les couches (support, grille, scène, profil, réglages) : plus combinatoire, moins prêt à construire.

**Un point d'honnêteté.** `RAW_BRUTALISM` de DG dit « ne jamais imiter un défaut d'accessibilité » et « type frontal mais lisible ». Le skill `brutalist` de TS prescrit, lui, des micro-textes de 10 à 14 px en majuscules et un rouge à 4,22:1 (manche 5).

### 3.6 Images et assets

**TS** (`references/imagery.md`) : ordre de préférence en six niveaux (images du projet ; images générées ; **images réelles de l'univers du sujet dans les collections ouvertes** ; images dessinées en code ; photographies fournies par la fiche ; type et couleur seuls) ; recherche par l'inventaire, dans les mots du lieu (« azulejo », pas « carreau bleu ») ; critères d'une bonne trouvaille ; **règles d'honnêteté** (une image trouvée n'est jamais celle du client ; légende de la source ; crédits enregistrés ; télécharger, ne pas lier) ; recadrage (peu de rapports, grand format, bord à bord, coins carrés, pas de cadre) ; traitement unique par page (intact, niveaux de gris, `multiply`, assombri ; « pas des traitements » : voile de couleur, duotone, flou, grain, vignette) ; montrer un logiciel par un fragment d'interface réel (`data-ui`) ; dessiner le sujet (trois niveaux de détail, aplats de teinte) ; vidéo en boucle (courte, légère, affiche, arrêt sous mouvement réduit) ; plancher vérifié de quatre images réelles (`SKILL.md` étape 6).

**DG** (`images-et-sources.md`, `diriger.md`) : fiche de source de 12 champs (origine, rôle, statut, observé, retenu, rejeté, transformé, décision changée, limite, localisation, responsable, droits) avec projection machine facultative ; test d'utilité de l'ancre ; réserve sur l'image générée utilisée comme ancre unique ; **lot d'assets** (traitement commun) ; registre d'illustration ; calibrations hors écran (cinéma pour la lumière, édition pour le rythme, affichage pour l'échelle…) ; contre-épreuve (un rendu natif au code ou sans l'asset ferait-il mieux apparaître la relation ?) ; `MOY-ASSETS` (traiter les assets moyens : recadrage, étalonnage, duotone, grain ou trame) ; six routes de production (`CODE-NATIVE`, `FOURNI`, `CURATÉ`, `GÉNÉRÉ-DIRIGÉ`, `HYBRIDE`, `SANS-ASSET`) ; carte des moyens par couche (`MOYENS`) dont la limite est écrite : « le paquet n'en contient aucune ».

**Équivalences.** Ordre de préférence ↔ routes ; droits, provenance et incertitude (TS « crédits » ↔ DG `RIGHTS / UNCERTAINTY`) ; traitement commun d'une série (TS §6 ↔ DG « lot d'assets ») ; dessiner le sujet avec soin ↔ `CODE-NATIVE` ; ne pas fabriquer un faux tableau de bord (TS `tells.md` §2 ↔ DG « NO-GO : faux réalisme, dashboard décoratif »).

**Seulement TS.** L'outil et la méthode de recherche dans les collections libres ; les critères de choix et de recadrage chiffrés ; la vidéo ; le plancher.

**Seulement DG.** Fiche de source ; réserve de calibration ; contre-épreuve ; calibrations dans d'autres domaines.

**Divergences.** (a) Plancher de quatre images réelles (TS) contre `SANS-ASSET` « à égalité » et « jamais un faux asset » (DG). (b) Traitements : TS exclut duotone et grain ; DG les cite comme traitements possibles si la thèse les justifie.

**Lecture.** La différence la plus nette de la comparaison côté matière. DG décrit un processus de calibration et de droits ; il ne fournit aucune source et n'en teste aucune. TS fournit la source, la méthode et le contrôle.

### 3.7 Mouvement

**TS** (`references/motion.md`) : budget en quatre parties (un moment signature, des entrées par section en ordre de lecture avec décalage de 60 à 90 ms, du retour sous la main, une image qui bouge) ; quatre questions avant toute animation (fréquence, rôle, courbe, durée) ; jetons (`--ease-out`, `--ease-in-out`, `--ease-soft`, 140/180/240/800 ms) ; 10 recettes en code (séquence de chargement, révélation de lignes masquées, révélation au défilement avec `IntersectionObserver`, volet d'image, appui et survol, progression liée au défilement, histoire épinglée, liste avec aperçu, accordéon, menu) ; 11 mouvements signature (`library/motions.json`) ; mouvement réduit = moins et plus doux, pas aucun ; « ce qui trahit un mouvement généré » (même fondu-glissé partout, boucles infinies sans sens, élan et rebond). Obligatoire : « le calque de mouvement est requis » (étape 9).

**DG** (`contexte.md`, `techniques.md`, ligne « Mouvement » de `STATE`) : le mouvement « doit expliquer, confirmer, orienter ou rendre une relation matérielle compréhensible, et ne pas retarder la tâche » ; une animation interactive se décrit comme un système d'états (initial, déclencheur, transition, interruption, résultat) ; documenter l'équivalent en mouvement réduit, l'interruption, le repli statique ; « si le mouvement n'apporte rien, supprimer » ; implémentation : état correct sans animation d'abord, transitions annulables, FLIP, View Transitions, Web Animations ; fragilités à éprouver (répétition rapide, inversion, annulation, rappel périmé).

**Équivalences.** `transform` et `opacity` ; mouvement réduit prévu ; pas de mouvement sans rôle ; mouvement relié à un changement d'état (TS : « it shows where something came from, it confirms an action… ») ↔ DG.

**Seulement TS.** Jetons, durées, recettes prêtes, signatures, liste de signes d'un mouvement « généré ».

**Seulement DG.** Interruption et annulation ; ordre « état correct puis continuité » ; fragilités à tester ; médium spatial ou 3D.

**Divergences.** Mouvement obligatoire (TS) contre mouvement justifié ou supprimé (DG). Voir aussi 6 : TS contredit lui-même son plancher avec la direction `stillness`.

**Lecture.** TS est une bibliothèque de gestes esthétiques ; DG est un contrat de correction. On ne peut pas bâtir une jolie séquence de chargement avec DG seul, ni vérifier une interruption avec TS seul.

### 3.8 Rédaction et contenu

**TS** (`references/copy.md`) : argument d'abord ; titre en deux lignes au plus avec arithmétique de caractères ; formes de titre (le nom, ce que c'est, l'affirmation, l'instruction, le lieu ou le moment) et formes à éviter ; ligne d'appui, corps, boutons ; preuve sans l'inventer ; « ce qui fait générique » ; micro-typographie. **DG** : `CFT-06` (ajouté en pilote, adapté de ce fichier), `CNT-01`, `EXD-01`, `EXTERNAL-START`.

**Équivalence** : forte depuis `CFT-06`. Restent : chez TS, le contrôle outillé (`lint.mjs` repère formules et clichés) ; chez DG, les contre-indications (langues sans espaces, textes fournis par un tiers, sujets intimes) et le rattachement à la vérité de scène.

### 3.9 Critique du rendu et boucle de correction

**TS** (`references/critique.md`) : **14 passes** (une seconde, plisser les yeux, couvrir le logo, bords, espace, typographie, couleur, images, uniformité, téléphone, plénitude, substance, collisions, concurrent et chose vivante) ; **note** pondérée à la manière d'un jury (design 40 %, utilisabilité 30 %, créativité 20 %, contenu 10 %) ; **plafonds** qui l'emportent sur l'arithmétique (un FAIL de l'inspecteur : 6,0 ; titre de trois lignes ou eyebrow ou mono : 6,5 ; moins de quatre vraies images : design 6,5…) ; format d'écriture imposé ; ordre de correction (idée, hiérarchie, composition, typographie, images, couleur, détail, mouvement) ; **au plus trois tours**, et « si le troisième tour reste sous 7,5, dis-le sans arrondir ».

**DG** : `CFT-00` (8 dimensions avec question et signal observable : présence, point de vue, culture visuelle, spécificité, composition, désirabilité, résolution, retenue) ; revue créative en 6 points (`BOUCLE-REVUE`) ; table symptôme → geste (`STATE`) ; `DOUBLE-LOOP` (observer, isoler **un** défaut dominant, modifier, réobserver la page entière, comparer, décider ; « aucun nombre d'itérations, score… ») ; tableau diagnostic → suite ; signaux de réouverture ; **test de résilience visuelle** (asset absent, contenu long, mobile, état critique, effet réduit) ; contrat de huit dimensions du premier objet avec « retour si… ».

**Équivalences.** Plisser les yeux ↔ « relire à faible détail » (`STATE`, lignes « Masse visuelle » et « Silhouette ») ; couvrir le logo ↔ test de singularité et test de style (masquer logo, couleurs, image) ; ordre de correction ↔ ordre de décision de `FND-01` (« JTBD → structure → hiérarchie → lisibilité → accessibilité → système visuel → polish ») ; arrêt : pas de quota (DG), trois tours (TS).

**Divergences.** Score chiffré avec plafonds (TS) contre « aucun score » (DG, trois fichiers). Les plafonds de TS relient des mesures d'outil à un verdict ; DG sépare jugement perceptuel et preuve.

**Le contrepoids propre à TS.** Les passes 11 à 13 (plénitude, substance, collisions) et la note d'essai : « en comparaison aveugle, une page plus riche pleine de motifs-gabarits battait toujours une page plus propre mais mince » (`critique.md` §1) ; `tells.md` §8 appelle « esthétique d'évitement » une page où tout est retiré et rien n'est mis à la place. DG a `retenue` (une dimension sur huit de `CFT-00`) et `FND-01` « retenue avant accumulation », mais **aucun test explicite de page sous-construite** : le plus proche est « résolution » et « présence » (« la proposition est plate, interchangeable ou sans foyer »), et la règle contre le « wireframe volontairement creux » (`MOY-PLAFOND`).

**Lecture.** DG isole mieux un défaut et le relie à un geste ; TS regarde mieux l'ensemble et protège contre l'excès de retrait.

### 3.10 Convergence et signes de génération

**TS** (`references/tells.md`) : registre daté (vagues 2023-2024, 2025, 2025-2026, « mode des galeries », signes de structure, de texte, de mouvement), avec **statut** (banni ou signalé) et « à faire à la place » ; principe : « il ne nomme jamais une police, une couleur ou un composant de remplacement, parce que toute liste “utilise ceci” devient la vague suivante » ; aveu : le « mode des galeries » (mono, numérotation, filets) est **banni par décision du propriétaire**, alors que l'étude le trouve plus fréquent sur les sites mieux notés (mono 44 % contre 24 %, numérotation 38 % contre 21 %).

**DG** (`gout-et-tendances.md`, `CONVERGENCE` et `COMP-VAGUES`) : trois vagues datées avec sources et « signaux à confirmer » (vague 1 : violet, Inter, halos ; vague 2 : crème, brun, serif italique, rouille, tramage ; vague 3 : dithering, ASCII, hachures, bleu Klein, libellés mono en capitales, repères de recadrage…) ; « pour nommer `MODAL`, jamais pour interdire » ; `STRUCT-SIGNAUX` (7 compositions en signal d'enquête) ; test de trame ; « same-energy » ne remplace pas une description causale.

**Équivalences.** Même diagnostic de la vague crème et brun ; même méfiance envers les listes de remplacement ; registres tous deux datés, à revoir (DG : avant 2027-03) ; même constat que « retirer ne suffit pas » (`tells.md` §8 ↔ `FND-01`) ; même liste de signes de structure (trois cartes égales, hero avec double CTA, plinthe de logos, faux écran).

**Divergence.** Application : TS fait échouer un contrôle (15 règles de la maison, `SKILL.md`), DG demande de se reconnaître. C'est D1 du suivi.

**Honnêteté comparée.** TS dit « par décision du propriétaire » pour un interdit que ses données contredisent ; DG a une étiquette `[OPINION DE SYSTÈME]` (`SAVOIR/READ`) et une table de sept niveaux d'autorité. Chacune est franche à sa façon : TS au cas par cas, DG par système d'étiquettes.

### 3.11 Interfaces, états et accessibilité

Seule DG couvre le sujet : `STATE` (états pertinents, récupération d'erreur `RCV-01`), `CONTEXT` (contextes à fort enjeu, plancher d'accessibilité), `TECH` (médiums non web, cinq responsabilités de preuve), `produit/interface`. TS v2 l'exclut explicitement (« Not for dashboards or app screens », description de `SKILL.md`). L'accessibilité chez TS tient en quelques lignes (contraste, `:focus-visible`, texte alternatif, cibles de 44 px sur téléphone dans `layout.md` §8).

## 4. Convergences indépendantes (à garder)

| Sujet | TS | DG |
|---|---|---|
| Vérité du contenu | « Proof is never invented » (`copy.md` §5) | `CNT-01`, `TRUTH/*` |
| Exemples attendus et signalés | `SKILL.md` étape 5 et rapport | `CNT-01`, `EXD-01` |
| Brief vague | décider, dire sa lecture en une ligne | au plus trois demandes, build dans le même tour |
| Idée qui vient du sujet | inventaire, test du concurrent | singularité, `MODAL` et `PARTI` |
| Argument avant la page | `copy.md` §1 | trame (`choisir.md`), `CFT-06` |
| Une preuve plus forte que le texte | « une démonstration réelle bat toute citation » | promesse → objet de preuve → geste |
| Retirer plutôt qu'ajouter | « ne remplis jamais le vide par un autre ornement » | « retenue avant accumulation » |
| Mobile | seconde composition | recomposer plutôt que comprimer |
| Registres de signes datés, sans liste de remplacement | `tells.md` (intro) | `CONVERGENCE`, `MOYENS` (« des sources, jamais des styles ») |
| Texte sur image | zone calme ou voile local | `COMP-TEXTE-IMAGE` |
| Pas de faux tableau de bord | `tells.md` §2 | « NO-GO : dashboard décoratif » |
| Mouvement réduit | repli obligatoire | document l'équivalent réduit |

## 5. Contradictions de fond entre TS et DG

| # | Sujet | TS | DG | Décision (manche 11) |
|---|---|---|---|---|
| 1 | Interdits | 15 règles de maison appliquées par `lint` et `inspect` (`SKILL.md`) | « jamais pour interdire » (`COMP-VAGUES`), signaux d'enquête | D1 : **recommandé** côté DG (non tranché par l'utilisateur) ; planchers seulement pour les défauts objectifs (porte A) |
| 2 | Mouvement | obligatoire, plancher de 8 éléments (`SKILL.md` étape 9) | justifié ou supprimé (`CONTEXT`) | D2 : côté DG, appliqué à la demande de l'utilisateur ; question « qu'est-ce qui bouge, et pourquoi ? » dans `CFT-00`, sans quota (livrée) |
| 3 | Images | plancher de 4 réelles, vidéo conseillée | `SANS-ASSET` à égalité, jamais de faux asset | D3 : **recommandé** côté DG (non tranché) ; plafond déclaré à écrire, route d'images libres livrée en U6 |
| 4 | Traitements d'image | duotone et grain « pas des traitements » (`imagery.md` §6) | duotone, grain ou trame possibles si la thèse les justifie (`MOY-ASSETS`) ; la tension interne de DG avec ses marqueurs de vague est alignée depuis la manche 8 | **tranché : côté DG**, déjà aligné (U7) |
| 5 | Note | score chiffré avec plafonds (`critique.md`) | aucun score (`CFT-00`, `DOUBLE-LOOP`) | **tranché : côté DG** ; les plafonds de TS ont presque tous un pendant (5.1) |
| 6 | Accent | un seul, sous 5 % | palette plurielle recevable, ne pas réduire par réflexe | **tranché : côté DG** ; le schéma « monochrome plus un accent » est le plus fréquent du panel de TS (23 %) mais aucun écart entre hauts et faibles n'est publié |
| 7 | Polices fréquentes | « par défaut » signalées (lint) | « pas un problème en soi » | **tranché : côté DG** ; la liste de TS est un choix de maison |
| 8 | Repères de coin, filets | bannis (`layout.md` §2, `tells.md` §4) | cités comme geste possible (`CFT-03`) | **tranché : côté DG**, avec test de retrait (U7) ; TS avoue que les filets fins sont bannis par choix, non par les données (61 % chez les hauts contre 52 %) |
| 9 | Réglages | absents de la v2 par défaut | 9 réglages qualitatifs (`styles.md`) | D4 : **recommandé** côté DG (non tranché ; la skill expérimentale de TS a aussi trois réglages) |
| 10 | Style maison | un parti unique, sans ornements | pluralité esthétique (`FND-01`, « Pluralité esthétique et goût situé ») | D4 : **recommandé** côté DG (non tranché) ; le style de TS reste possible comme profil `STYLE`, sur demande |

### 5.1 Les plafonds de TS et leur pendant dans DG (manche 11)

La note de TS (`critique.md` §2-3) est une grille à quatre critères avec treize plafonds qui l'emportent sur l'arithmétique. Chaque plafond, rapproché de DG après les manches 4 à 10 :

| Plafond de TS | Pendant dans DG |
|---|---|
| Un `FAIL` de l'inspecteur : 6,0 au plus | Un `RETURN` de la porte A : le verdict n'est pas accepté |
| Titre de 3 lignes ou plus, étiquette, monospace, numérotation 01/02, dégradé, ombre, filet : 6,5 au plus | Aucun, **par choix** (D1) : questions de convergence et relevés |
| La page pourrait appartenir à n'importe qui : créativité 6 au plus | Test de singularité et `MODAL` (`SAVOIR/FRAME/SINGULARITE`, `CFT-02`) |
| L'idée vaut pour le concurrent le plus proche : 7 au plus | Test du concurrent (`CFT-01`, U1) |
| Moins de 4 images réelles : design 6,5 au plus | Aucun (D3) : plafond déclaré, images libres (U6) |
| Une page qui bouge à peine : 7 au plus | Question sur le mouvement (`CFT-00`, D2) |
| Aucune chose vivante : créativité 7,5 au plus | « Une chose vivante » (`CFT-01`, U1) |
| Un emplacement vide (boîte grise, lorem) : contenu 5 au plus | Contenu d'exemple marqué, jamais d'emplacement vide (noyau) |
| Deux écrans de bureau presque vides ou texte courant petit et grisé : 6,5 au plus | Signal de substance (`CFT-00`, U2) ; plus petit texte relevé (`--mesures`) |
| Section demandée absente ou réduite à quelques mots : contenu 6 au plus | Signal de substance (`CFT-00`, U2) |
| Pas de vrai bouton d'action au premier écran : utilisabilité 7 au plus | **Aucun contrôle équivalent** ; l'objet de preuve (`--proof`) ne vise pas l'action |
| Un élément couvre un titre à une position de défilement : utilisabilité 6 au plus | Relevé du premier écran (`--mesures`, U8), sans plafond ; défilement non parcouru |
| Bande vide où une révélation ne s'est pas déclenchée, ou contenu rogné hors écran : utilisabilité 5 au plus | La recette fait défiler toute la page avant de mesurer ; haut de titre rogné relevé (U8) ; reste partiel |

**Lecture.** Sur treize plafonds, huit ont un pendant dans DG (cinq ajoutés par les changements de cette série, trois qui existaient), deux sont des refus assumés (les motifs de galerie, le plancher d'images réelles), deux sont partiels (recouvrement d'un titre, bande vide ou rognage) et un manque (action principale au premier écran). TS exprime en note ce que DG exprime en geste, en plafond déclaré ou en `RETURN`. Le désaccord de fond porte sur la **forme** (un nombre contre une description de l'écart), non sur ce qui est regardé. La seule absence réelle est le contrôle de l'action principale au premier écran, qui relèverait d'un relevé (`--mesures`) plutôt que d'un verdict.

**Données de TS à garder en tête pour trancher.** `research.md` écrit lui-même que les étiquettes monospace, la numérotation d'index et les grilles à filets sont « exclues par choix du propriétaire, non par les données » (plus fréquentes chez les hauts : 44 % contre 24 %, 38 % contre 21 %), et que les filets fins ne montrent aucun écart (61 % contre 52 %). Ses interdits de maison sont donc un style, pas une mesure de qualité.

## 6. Tensions internes à chaque système (vues à la lecture)

**TS.**
- **`stillness` contre `still-page`.** Deux des 20 directions de la bibliothèque (`quiet-instrument`, `dense-tiles`) tirent le mouvement `stillness` : « pas de démonstration ; ne pas ajouter d'animation de chargement ni de révélation au défilement » (`motions.json`). L'inspecteur fait échouer toute page à moins de 8 éléments mobiles (`inspect.mjs`, `MOTION_MIN = 8`), sauf option `--allow still-page`. **Vérifié en manche 7** : aucune des 20 directions ne porte de dérogation `allow`, et la fiche imprime juste après la description du mouvement « The inspector fails a page that barely moves » (`draw.mjs` ligne 509 ; `COMPARAISON-COMPLEMENT.md` A6).
- **Bans contre données.** Les motifs « de galerie » (mono, numérotation) sont plus fréquents chez les mieux notés ; ils sont bannis quand même (`SKILL.md`, « Why these, honestly »). Avoué.
- **Skills voisines.** Voir `SUIVI.md` 6.2 : `soft`, `brutalist`, `stitch`, `image-to-code` contredisent la v2.

**DG.**
- **Marqueurs de vague contre traitements d'asset.** `MOY-ASSETS` propose « duotone, grain ou trame » ; `CONVERGENCE` range « tramage » en vague 2 et « dithering » en vague 3 ; `STRUCT-SIGNAUX` pose la question de reprise pour « grain, trame, texture reprise d'un brief à l'autre ». La nuance est écrite (« si la thèse le justifie », « nommer, jamais interdire »), mais l'agent reçoit des signaux contraires.
- **Repères de coin.** `CFT-03` les propose ; `CONVERGENCE` les range en vague 3 (« repères de recadrage »).
- **Retrait contre plénitude.** Voir 3.9 : la place donnée à la retenue sans test de page sous-construite.
- **Calibration.** Une ancre exige une source observée ou fournie (`SOURCE`, `diriger.md`) ; la carte des moyens avoue que le paquet n'en contient aucune ; sans accès web, la direction reste `EXPLORATORY`.

## 7. Faiblesses propres, par lecture

**TS.** Périmètre limité aux pages publiques ; v2 cohérente mais entourée de skills qui ne lui obéissent pas ; étude faite par un panel de modèles sur des sites de galerie (biais de sélection reconnu dans `research.md`) ; résultat du test publié défavorable ; arithmétique des titres pensée pour des écritures à espaces ; accessibilité réduite à quelques lignes ; bibliothèque figée à une date.

**DG.** Aucune valeur de départ dans ses fichiers de savoir hors pilotes datés ; 32 routes en quelques lignes, sans géométrie ni variante mobile chiffrée ; vocabulaire lourd (statuts, champs, tags) pour qui n'a pas l'habitude ; pas d'inventaire du sujet ; pas d'outil de tirage (les deux mécanismes anti-convergence reposent sur la discipline du modèle) ; plusieurs signaux contraires (section 6) ; bénéfice non démontré.

## 8. Ce qui serait utile à DG, trié (propositions, rien n'est fait)

Règles : un seul changement à la fois ; `PILOT` avec contre-indication, preuve attendue et retour arrière (recette `ACTION/MAINTENANCE`) ; aucun quota ni interdit ; valeurs importées au format de claim daté de `SAVOIR/TOOLS`.

| # | Proposition | Source dans TS | Où dans DG | Coût | Risque |
|---|---|---|---|---|---|
| U1 **(fait en manche 8, PILOT : sous-section de `CFT-01`)** | **Inventaire du sujet** (8 à 12 éléments propres au client) et **phrase d'idée** à deux blancs, reliés à `FIRST-OBJECT` et à la recherche d'images | `SKILL.md` étapes 1 et 4 | `CFT-01` (idée par rapprochement) ou un paragraphe de `FIRST-OBJECT` | un paragraphe, une ligne dans `maintenance/versions.md` | faible ; peut se confondre avec `DOMAIN-FRAME` : le dire |
| U2 **(fait en manche 8 : paragraphe « Substance » de `CFT-00`)** | **Test de page sous-construite** (écran presque vide, section demandée livrée en quelques mots) comme ligne de `CFT-00`, sans seuil ni score | `critique.md` passes 11 et 12 | `CFT-00`, ligne « Résolution » ou nouvelle ligne | une ligne | faible ; ne pas en faire un quota |
| U3 **(fait en manche 9, PILOT, deux routes)** | **Gabarit de départ** (une géométrie de bureau et une de mobile, `[À ADAPTER]`) pour quelques routes seulement (une scène, une grille) | `library/sections.json`, `heroes.json` | `catalogue.md`, sous « choisir lorsque / éviter lorsque » | moyen, à faire sur 2 routes d'abord | risque de recettes figées, d'où deux routes seulement |
| U4 **(fait en manche 9, `[À ADAPTER]`)** | **Jetons de mouvement et durées** en `[À ADAPTER]`, avec la contre-indication « mouvement utile seulement » | `motion.md` §2 et §3 | `CONTEXT` ou `POINTS-DE-DEPART` | une table | faible |
| U5 **(fait en manche 9, `[À ADAPTER]`)** | **Réglages de grand texte** (approche selon la taille, collisions d'interligne, espace 2 pour 1 autour d'un titre) | `type.md` §3 et §7 | `typographie.md` | quelques lignes | faible |
| U6 **(fait en manche 9, PILOT)** | **Méthode de recherche d'images libres** (requêtes tirées de l'inventaire, mots du lieu) et la règle « une image trouvée n'est jamais celle du client » | `imagery.md` §3 | `SOURCE` | un paragraphe | à vérifier : DG a déjà une règle sur « image hors sujet » (`MOY-ASSETS`) |
| U7 **(fait en manche 8 : deux phrases hors noyau)** | **Aligner les signaux contraires** de la section 6 : une phrase par tension (traitements d'asset, repères de coin) | — | `MOY-ASSETS`, `CFT-03` | deux phrases | très faible |

Ordre conseillé : U7 (cohérence, quasi gratuit), U1 (le plus grand écart de méthode), U2 (corrige le biais de retrait), puis U5, U4, U6, U3.

## 9. Ce que cette lecture ne permet pas de dire

- Lequel produit de meilleurs rendus : aucun test comparatif ne le dit (4 et 5 dans `SUIVI.md`).
- Si les valeurs de TS sont justes : elles viennent d'un panel de modèles sur 247 sites de galerie.
- Si le texte de DG est lu comme prévu par un agent : les 32 routes sont courtes, mais la charge réelle de lecture n'a été mesurée qu'en mots (`SUIVI.md` 4.3).
- Le contenu complet de `library/` de TS et de `catalogue.md` de DG au-delà des passages cités.
