# Complément : parties restantes et analyses par code (manche 7)

> **Statut.** Hors paquet, branche orpheline `suivi-comparaison-taste-skill`. Complète `COMPARAISON-TEXTUELLE.md` (manche 6) et `SUIVI.md`.
> **Méthode.** Lecture des fichiers restants, plus **des analyses par code sur les données de Taste Skill (TS) et sur le texte de Design Governance (DG)**. **Aucun skill n'a été lancé sur un brief** : aucun rendu produit, aucun tirage. Les scripts et leurs sorties brutes sont dans `essais/analyses/` (voir son `LISEZMOI.md`). Date : 2026-10-14.

## 0. Ce qui a été lu, ce qui a été exécuté

**Lu.** DG : `design/produit/` (`finition`, `premier-rendu`, `interface`, `preuve-visuelle`), `design/direction/standard` (les cinq absolus et les invariants), `design/savoir/systeme-de-design`, `design/savoir/connexions` (C01 à C09), fin de `design/formes/catalogue` (objets, micro-interfaces, modificateurs, composants, compatibilité). TS : `research.md` en entier (§1 à §11), `scripts/draw.mjs` (tirage, historique, sélection, fonction `adjustments`), `scripts/assets.mjs` (en-tête et usage), `lib/probe.mjs` (liste des mesures), `assets/base.css` et `assets/base.js`, `library/` (schémas et entrées).

**Exécuté (lecture et comptage seulement).** (1) contrôle de contraste et de familles de couleur des 56 palettes avec les propres règles de TS ; (2) polices des 44 systèmes typographiques contre les listes du `lint` de TS ; (3) recherche de motifs bannis dans la prose de 240 entrées de la bibliothèque ; (4) couverture de la bibliothèque ; (5) application de la fonction `adjustments()` de `draw.mjs` aux 172 sections et 48 héros (la fonction est extraite du fichier puis exécutée sur les données, `draw.mjs` n'est pas lancé) ; (6) comptage des valeurs chiffrées prescrites ; (7) comptage de termes à motif précis dans les deux corpus ; (8) relecture, un chiffre après l'autre, des 16 lignes de `POINTS-DE-DEPART` contre `research.md` ; (9) requêtes `read_route.py --trouver` sur le propre moteur de recherche de DG.

## 1. Lecture : les parties restantes

### 1.1 Les « portes » de forme

**DG.** `ABSOLU 1` : « une surface identitaire conforme mais sans direction perceptible est un échec de livraison » ; trois décisions nommables avant livraison (stratégie matérielle, typographie déclarée avec une raison, composition intentionnelle). `Gate C` (`finition.md`) : six critères, chacun avec « présent si », « retour ou réserve si », « geste si absent » : C1 stratégie de surface, C2 typographie choisie, C3 composition intentionnelle, C4 densité optique, C5 stratégie de profondeur, C6 résolution située. `FIRST-RENDER` : qualité initiale attendue par mode (`LITE` à `SYSTÈME`), « jamais un artefact volontairement creux ». Invariant : « PASS technique ≠ direction tenue ».

**TS.** `inspect.mjs` passant « ne veut rien dire » sur la qualité (`critique.md`, première phrase) ; 14 passes ; note et plafonds ; porte de sortie appliquée par outil.

**Équivalence nette.** « Le contrôle technique n'établit pas que la page est bonne » est écrit des deux côtés, presque dans les mêmes termes.

**Écart.** DG relie un défaut à un geste (colonne « geste si absent » de C1 à C6) ; TS relie un défaut à une mesure et à un plafond de note. DG n'a pas d'équivalent des plafonds ; TS n'a pas de table symptôme → geste.

### 1.2 Ancrage et références

**DG.** `ABSOLU 2` : « Ne fais jamais accepter une direction identitaire calibrée uniquement de mémoire » ; trois voies (`ANCHOR-GENERATED`, `ANCHOR-OBSERVED`, `ANCHOR-PROVIDED`) ; explorer sans ancre est possible, **accepter** non ; une source Web doit être « réellement ouverte et réinspectable » ; le validateur de `RUN_CARD` refuse une direction acceptée sans ancre (c'est une des rares règles esthétiques qu'un outil fait respecter).

**TS.** Les ancres sont livrées : 181 sites étudiés avec idée, héros, typographie, couleur, images, mise en page, sections et « à voler » ; `draw.mjs` en joint deux ou trois à chaque fiche (`dealReferences`) ; `--site <id>` donne la fiche complète.

**Lecture.** DG exige une ancre **vérifiée par l'agent** (donc dépendante de la capacité Web) ; TS livre des ancres **déjà préparées** (donc figées à la date du corpus). Une ancre de DG est fraîche mais peut manquer ; une ancre de TS est toujours là mais peut être périmée. Aucune des deux ne contient d'exemple faible : la bibliothèque de TS ne contient que des sites notés 6,8 ou plus (voir A4) ; les contre-exemples de DG sont les vagues datées de `CONVERGENCE`.

### 1.3 Le réel et le beau

`ABSOLU 5` (DG) : contenu réel et microcopie honnête, pas de faux réalisme, contenu synthétique permis en exploration s'il garde longueur, densité, langue, ambiguïté ; en contexte à enjeu, la clarté prime sur l'esthétique spectaculaire. `copy.md` §5 et `SKILL.md` étape 5 (TS) : jamais de preuve inventée, détails d'exemple attendus et listés dans le rapport. **Convergence**, avec en plus chez DG la priorité donnée aux contextes à enjeu.

### 1.4 Système, composants, objets : DG ; fondation de code : TS

**DG.** `SAVOIR/SYSTEM` (tokens primitifs et sémantiques, source de vérité, migration, rollback) ; `BIBLIOTHEQUE/COMPONENTS` (6 couches, contrat de composant en 13 lignes, graphe de dépendance à sens unique, `BRAND_GRAMMAR` gouvernée) ; `OBJECT` (9 routes, contrat de 10 champs) ; `MICRO` (7 unités denses avec « identité → état → mesure ou choix → conséquence → action ») ; `MODIFIER` (3) ; `COMPAT` (10 lignes de combinaisons favorables).

**TS.** Aucune notion de composant ni d'objet partagé. À la place : **un code de départ**. `assets/base.css` (100 lignes) : 6 jetons de rôle, 5 pas typographiques en `clamp()`, marge, gouttière, espace de section, un seul rayon (0 par défaut), 3 courbes et 4 durées de mouvement, réinitialisation, grille à 12 colonnes, contrôles de 48 px, champs sans bordure avec focus visible, aides de mouvement activées sous `prefers-reduced-motion: no-preference` et sous une classe `.js`. `assets/base.js` (37 lignes) : révélation par `IntersectionObserver`, jamais rejouée, avec filet de sécurité à 2,5 s si l'observateur ne s'est pas déclenché.

**Lecture.** DG décrit comment gouverner un système de composants ; TS donne un point de départ qui incarne sa maison. Le code de TS applique ses propres règles (rayon unique, focus visible, contenu visible sans script) : c'est la seule partie de la comparaison où une règle esthétique est livrée sous forme exécutable.

### 1.5 Routage conditionnel

`SAVOIR/connexions` (DG) : neuf connexions C01 à C09, chacune avec condition, sources, intervention, contre-indication, moyens et limites, observation et réexamen (exemples : contexte incertain, typographie déterminante, asset déterminant, réemploi situé, ambition vers construction). TS : une table « Files — read it when » de 14 lignes (`SKILL.md`). Les connexions de DG sont conditionnelles et portent leur contre-indication ; la table de TS est une carte de lecture.

### 1.6 Cadrage de médium et de capacité

`produit/interface.md` (DG) : choisir la **capacité minimale** qui permet de construire ou de vérifier la décision (code, fichier de design, CMS, primitive accessible, motion d'état, scène 3D, aucune), distinguer construction et vérification, « une technique ne devient jamais la direction par défaut ». TS ne traite pas la question : pages publiques en HTML et CSS, Node et Chromium requis, sinon « dis-le dans le rapport ».

### 1.7 Le tirage de TS (`draw.mjs`) : ce qu'il fait vraiment

Lu en détail. Le tirage n'est pas uniforme :
- générateur à graine (mulberry32) ; **historique** des 24 derniers tirages dans `~/.taste-skill/history.json` ; les pools écartent les 5 dernières directions, les 3 derniers héros, les 6 derniers systèmes et palettes tant qu'il reste des candidats (`fresh`) ;
- **filtres** : secteur (22 secteurs, `--sector` obligatoire), ton (si au moins 2 candidats restent), **actifs réellement disponibles** (`--have`, option `needs`), mode d'images (`interface`, `no-product-photo`, `atmosphere`, `own`) ;
- **sections** : un modèle compatible par rôle, dans l'ordre demandé, en évitant la forme de la section précédente (`prevShape`) et les modèles déjà utilisés ;
- **photos** : choix d'un jeu selon le secteur et les mots du brief, avec marquage `lookalike` des images qui ressemblent trop au produit ;
- **`--redraw`** par créneau avec compteur, **`--alternatives <rôle>`**, **`--keep palette,type`** pour une marque existante ;
- **`adjustments()`** : une douzaine de règles à expressions régulières qui, pour chaque modèle tiré, listent là où il contredit les règles de la maison (texte de 9 à 12 px, texte atténué, coins arrondis, filets, ombres, mélange `difference`, phrase longue en grand corps, numérotation, action en simple lien, etc.). Le commentaire du code le dit : « Blueprints were measured on real sites and carry that site's sizes, greys, faces, colours and corners. »

**Conséquence pour la comparaison.** Ce qui est « aléatoire » chez TS est **un choix contraint par des règles, des disponibilités et un historique**. Ce qu'on a appelé le « tirage externe » (N2) est donc surtout un **sélecteur** avec un peu de hasard. DG n'a ni les données, ni le sélecteur, ni l'historique.

### 1.8 `research.md` en entier

- Échantillon : 248 sites au 2026-10-05, 235 utilisables, 202 mesurables ; 21 relecteurs modèles ; notes « à la Awwwards » (40/30/20/10) d'après des images fixes.
- **Aveux de l'étude sur ses limites** : « it is fashion as much as quality » ; le détecteur d'eyebrow sur-compte (60 % mesuré contre 35 % observé) ; mouvement inféré des images.
- **Les règles de la maison sont plus strictes que la galerie** : en appliquant son propre `inspect.mjs` aux 202 sites, le site médian a 4 FAIL et seuls 4 % n'en ont aucun (§9).
- **Neuf « moteurs d'idée »** (§3) : le produit se démontre lui-même ; la page est un artefact du monde du sujet ; le nom est le héros ; un motif du sujet porte tout ; déguisé en autre catégorie ; le lieu porte la page ; une scène fixe ; une section, une couleur ; l'understatement radical.
- **Les défauts des meilleurs sites** (§8) : texte de 9 à 13 px sur environ 24 des 90 sites à 7,5 ou plus ; information cachée derrière le concept (20) ; idée qui s'épuise (15) ; texte sur vidéo sans voile (12) ; portes et premiers écrans vides (12).
- **Test du skill** (§11) : 5 manches, un juré modèle par brief, « les notes isolées portent environ un demi-point de bruit » ; **les briefs de la manche 5 avaient été vus à la manche 4**. Le dernier résultat (7,7 contre 7,8, 2 victoires sur 3) n'est donc pas indépendant.

## 2. Analyses par code

### A1 : les 56 palettes face aux règles de TS (`palettes.mjs`)

| Mesure | Résultat |
|---|---|
| Encre sur sol | min 7,4, médiane 13,2, max 21,0 ; **aucune sous 7:1** (la bibliothèque l'annonce) |
| Texte atténué sur sol | min 4,7, médiane 5,2 ; aucune sous 4,5:1 |
| Texte sur accent | min 4,8, médiane 7,0 ; aucune sous 4,5:1 |
| Champs de couleur (encre sur fond) | aucune sous 4,5:1 |
| Familles interdites (crème avec terracotta, violet) détectées par la fonction `colourFamily` de TS | **aucune** |
| Accent sur sol sous 4,5:1 (non utilisable en texte) | 20 palettes sur 56 |
| **Accent sur sol sous 3:1** | **13 palettes sur 56** |

Les 13 : `paper-grey-brass` 1,8 ; `white-navy-tab` 2,3 ; `black-crimson` 2,8 ; `white-mint-tiles` 1,2 ; `offwhite-bottle-yellow` 1,3 ; `pink-field-lime` 1,9 ; `sky-field-navy` 1,4 ; `tobacco-olive` 1,9 ; `poster-chapters` 1,9 ; `candy-chapters` 2,2 ; `orange-sky-lime` 1,9 ; `mint-orange-grey` 1,2 ; `report-blocks` 2,7.

**Ce que cela veut dire.** `base.css` donne le focus clavier par `outline: 2px solid var(--accent)`. Pour ces 13 palettes, ce contour a moins de 3:1 contre le sol (seuil de contraste non textuel de WCAG 1.4.11). Mesuré contre la couleur de sol de la palette, **pas contre chaque champ** pour les palettes à champs (limite). Le contrôle de TS n'en voit rien : ni `inspect.mjs`, ni `probe.mjs`, ni `rules.mjs` n'examinent le focus (la recherche de « focus » ne trouve qu'une occurrence, dans `lint.mjs`, pour ne pas prendre un contour pour un filet).

### A2 : les 44 systèmes typographiques face au `lint` de TS

0 famille de la liste `default-font`, 0 monospace. 49 familles distinctes pour 88 emplacements ; **27 systèmes sur 44 n'utilisent qu'une famille**. Les plus dealées : Switzer (5 systèmes), Archivo (4), General Sans, Hanken Grotesk, Work Sans, EB Garamond (3 chacune). La bibliothèque suit son propre lint à la lettre. Au passage : Archivo figure dans les « signaux à confirmer » de `CONVERGENCE` de DG (« grotesque large ou condensée (Archivo) sur fond blanc neutre avec un seul accent vif ») et dans 4 systèmes sur 44 de TS (9 %). C'est une coïncidence de noms à garder en tête, pas une preuve.

### A3 : motifs bannis dans la prose des 240 entrées (20 directions, 48 héros, 172 sections)

13 motifs recherchés, 9 occurrences après resserrement des motifs, **aucune ne prescrit un motif banni** : 3 négations explicites (« no gradients », « no blur », « no shadows »), 3 « ombre » au sens de zone sombre d'une photographie, 1 « backdrop » au sens de fond de l'image, 1 « label above each value » (lignes d'un formulaire), 1 ombre d'un dialogue dans un fragment d'interface `data-ui` (l'exception prévue par la règle). **La prose de la bibliothèque respecte la maison.**

### A5 : modèles qui contredisent la maison selon `adjustments()` de TS

| | Entrées | Avec au moins une correction | Dont correction autre qu'une adaptation de couleur, de famille ou de coins |
|---|---|---|---|
| Sections | 172 | 75 (44 %) | **61 (35 %)** |
| Héros | 48 | 44 (92 %) | **28 (58 %)** |

Motifs corrigés, par fréquence (sections) : phrase longue en grand corps (18), texte atténué (12), texte à 12 px (12), famille nommée (10), coins nommés (9), filets ou bordures (9), mélange `difference` (4), épinglage de plus de trois écrans (3), texte à 10 px (3), ombre (2), lettres coupées en haut (1), numérotation (1). Pour les héros : famille nommée (22), phrase longue (11), action en simple lien (10), etc.

**Lecture.** La prose de la bibliothèque est propre (A3), mais ses **modèles chiffrés** (tailles, gris, coins) viennent de sites réels et contredisent la maison pour plus d'un tiers des sections et plus de la moitié des héros. TS le traite **par le code** : la fiche imprime les corrections. C'est un mécanisme que DG n'a pas, faute de données de ce type.

### A4 : couverture et espace des combinaisons

- 22 secteurs ; chaque secteur a entre **5 et 13 directions** (`real-estate` et `architecture` : 5) ; 7 tons, couverts par 6 à 11 directions chacun.
- 16 rôles de section, de 7 (`proof`, `contact`) à 21 (`features`) modèles ; **chaque rôle est couvert pour chacune des 20 directions**.
- Par direction : 4 à 9 héros, 9 à 44 palettes (médiane 24), 10 à 23 systèmes typographiques (médiane 16) ; **48 122 combinaisons** héros × palette × système sur l'ensemble, avant les sections.
- 19 jeux de photos (7 à 59 images chacun), servis par Lorem Picsum (licence Unsplash).
- **181 sites étudiés, tous notés de 6,8 à 8,6** (90 à 7,5 ou plus, 69 entre 7,0 et 7,4, 22 entre 6,8 et 6,9) : la bibliothèque ne contient aucun site faible.

### A6 : contradiction interne : `stillness`

`quiet-instrument` et `dense-tiles` tirent le mouvement `stillness` : « Do not add a load animation or scroll reveals to this direction » (`motions.json`). **Aucune des 20 directions ne porte de dérogation `allow`** (champ vide partout). Et la fiche imprime, juste après la description du mouvement (`draw.mjs`, ligne 509) : « This is the signature move… Around it the page still needs the rest of the motion layer (SKILL.md step 9): an entrance for the parts of every section, feedback on every control, and one moving picture. The inspector fails a page that barely moves. » **Deux consignes opposées dans la même fiche**, pour 2 directions sur 20.

### A7 : valeurs chiffrées prescrites

| | Mots | Valeurs chiffrées | Par 100 mots |
|---|---|---|---|
| TS `SKILL.md` et références | 23 422 | 434 (dont 164 dans `research.md`) | 1,9 |
| TS bibliothèque : 172 sections | médiane 194 mots par entrée | **médiane 13 par entrée**, 2 189 au total | 6,5 |
| TS bibliothèque : 48 héros | médiane 248 mots | **médiane 17,5**, 825 au total | 6,1 |
| DG `design/**` avant les pilotes | 37 755 | **11** | 0,03 |
| DG section `POINTS-DE-DEPART` (ajoutée) | 1 048 | 56 | 5,3 |
| DG catalogue : 16 entrées support, grille, scène | médiane 59 mots | **0** | 0 |

« Valeur chiffrée » : nombre suivi de `px`, `vw`, `vh`, `em`, `rem`, `ms`, `ch`, `fr`, `dp`, `pt`, `fps` ou `%`, plus `clamp(` et `cubic-bezier(`. C'est une **description du choix de conception** de DG (« points de départ adaptables, jamais validations universelles »), non un défaut en soi ; elle quantifie l'écart de « matière » constaté en lecture.

### A8 : lexique à motif précis (occurrences, TS contre DG, hors `POINTS-DE-DEPART`)

| Seulement chez TS | TS | DG |
|---|---|---|
| `clamp()` | 9 | 0 |
| `prefers-reduced-motion` (écrit tel quel) | 9 | 0 (DG dit « mouvement réduit ») |
| chargement des polices (`font-display`, `preconnect`) | 6 | 0 |
| licences Creative Commons (CC BY, CC0) | 6 | 0 |
| bord à bord, `full-bleed` | 8 | 0 |
| `cubic-bezier` | 3 | 0 |
| crénage | 2 | 0 |
| `credits.json` | 2 | 0 |
| inventaire du sujet | 1 | **0** |

| Seulement chez DG | TS | DG |
|---|---|---|
| récupération après erreur | 0 | 18 |
| interruption d'une animation | 0 | 10 |
| WCAG | 0 | 6 |
| rollback, retour arrière | 0 | 3 |
| View Transitions, FLIP, Web Animations | 0 | 3 |
| lecteur d'écran | 0 | 2 |
| OKLCH, gamut, police variable | 0 | 1 chacun |

**Contrôle croisé.** `python3 scripts/read_route.py --trouver "inventaire du sujet"` ne renvoie rien de pertinent (le mot « inventaire » n'apparaît qu'ailleurs) ; `--trouver "sous-construit"` répond « AUCUNE OCCURRENCE ». Les deux absences relevées en manche 6 (inventaire du sujet, test de page sous-construite) sont confirmées par l'outil de DG lui-même, qui rappelle que ce résultat « ne prouve pas l'absence du savoir ». Limite générale : les motifs sont précis, mais le comptage de mots reste une approximation.

### A9 : relecture de `POINTS-DE-DEPART` contre `research.md`

Les 16 lignes ont été relues une à une contre §1 à §9 de `research.md`. **Aucun écart de valeur.** Un défaut de présentation : trois lignes opposaient « faibles » et « hauts » dans un ordre qui changeait d'une ligne à l'autre. Corrigé dans le commit `27db80d` de `ccr-38b0a56f-t8xdo8` (chaque cellule dit « Faibles contre hauts » ou « Hauts contre faibles »). Validation complète rejouée.

## 3. Ce que cela change

**Nouvelles contradictions ou tensions** (à ajouter à celles de la section 5 de `COMPARAISON-TEXTUELLE.md`).
- **TS, focus contre palettes** : `base.css` donne un contour de focus de 2 px à la couleur d'accent ; 13 palettes sur 56 le rendent à moins de 3:1 contre le sol (A1).
- **TS, `stillness`** : deux consignes opposées dans la même fiche, aucune dérogation (A6).
- **TS, modèles et maison** : 35 % des sections et 58 % des héros contredisent la maison avant correction par `adjustments()` (A5).

**Mises à jour des propositions U** (`COMPARAISON-TEXTUELLE.md` section 8).
- **U1** (inventaire du sujet et phrase d'idée) : ajouter les **neuf moteurs d'idée** de `research.md` §3 comme leviers de la phrase. DG n'en couvre qu'un (« déguisé en autre catégorie », par `CFT-01` « idée par rapprochement »).
- **U3** (gabarit de départ sur deux routes) : l'ordre de grandeur est maintenant connu : une section de TS porte en médiane 13 valeurs chiffrées en 194 mots ; une entrée de DG en porte 0 en 59 mots. Un gabarit de départ pour deux routes de DG (une grille, une scène) aurait donc environ 150 mots et une dizaine de valeurs `[À ADAPTER]`.
- **Nouvelle U8, à ne pas faire sans D1 à D4** : un point de départ de code (comme `base.css`) n'est pas dans la nature de DG. Il imposerait une maison. À consigner, non à proposer.

**Faiblesses de TS ajoutées par cette manche** : contour de focus insuffisant pour 13 palettes ; `stillness` contradictoire ; test publié par un juré modèle par brief avec des briefs réutilisés à la manche finale ; bibliothèque sans exemple faible ; ancres figées à 2026-10 ; aucune notion de composant, d'état ni d'erreur.

**Forces de TS confirmées par les données** : bibliothèque propre au regard de ses règles (A2, A3) ; palettes qui respectent leurs seuils annoncés de contraste (A1) ; modèles accompagnés d'un correcteur automatique (A5) ; combinatoire large (A4) ; fondation de code (1.4).

## 4. Bilan consolidé sur la capacité esthétique et design

1. **Matière.** TS : environ 3 000 valeurs chiffrées dans 220 modèles, 56 palettes, 44 systèmes typographiques, 19 jeux de photos, 181 sites. DG : 0 valeur dans ses 16 entrées de support, de grille et de scène, 56 valeurs dans une section pilote datée. **Écart net, en faveur de TS.**
2. **Décision.** DG : critères, gestes avec condition et réinspection, protection des risques critiques, vérité de la scène. TS : règles de maison, tirage contraint, correcteur de modèles. **Avantage DG sur les cas non standard** (applications, états, médiums, contextes à enjeu), **avantage TS sur la vitesse d'un résultat cohérent** pour une page publique.
3. **Contrôle.** TS : outil de gate (lint, inspecteur, code de retour) ; DG : recette de rendu limitée à la porte A, validateur de `RUN_CARD`. Les deux contrôlent des choses disjointes (manche 3). **Un défaut de chaque côté** : focus des palettes (TS), taille du texte (DG, traité par `--mesures`).
4. **Honnêteté.** TS : limites écrites dans `research.md`, mais deux contradictions internes (`stillness`, skills voisines). DG : étiquettes d'autorité, limites partout, mais plusieurs signaux contraires (traitements d'asset, repères de coin) et aucun test comparatif.
5. **Preuve d'efficacité.** TS : un test publié, défavorable. DG : aucune. **Aucun des deux n'a démontré qu'il fait mieux qu'un modèle sans skill.**

## 5. Limites de ce complément

- Aucun rendu n'a été produit ni jugé : tout ce qui précède porte sur des textes et des données.
- Les contrastes sont calculés par la formule WCAG sur les valeurs hexadécimales des palettes ; l'effet réel dépend de l'usage dans la page.
- `adjustments()` est une fonction à expressions régulières : elle sur-signale (couleurs nommées) et peut sous-signaler ; les chiffres A5 donnent un ordre de grandeur.
- Le comptage lexical (A8) et le comptage de valeurs (A7) sont des approximations mécaniques ; les motifs sont précis mais non exhaustifs.
- `assets.mjs` et `probe.mjs` ont été lus en en-tête et par sondage, non en entier ; `catalogue.md` de DG a été lu en entier pour cette manche, mais `gouvernance/structure.md` (`BIBLIOTHEQUE/CONTRACTS`) ne l'a été que par recherche ciblée.
