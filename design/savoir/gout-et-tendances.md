# Savoir — goût et tendances

Claims, goût, références, tendances datées et ressources.

<!-- origine:SAVOIR.md -->
# SAVOIR/TOOLS — claims, tendances et calibration

## Claims externes et péremption

[REQUIS PAR LE MODULE — claim qui influence une décision, un seuil, une route, une tendance ou un livrable] Tout claim utilisé dans un run indique :

```text
CLAIM-TYPE — empirique, normatif, technique, culturel, réglementaire ou local.
STATEMENT
SCOPE
SOURCE
VERSION / DATE-VERIFIED
LIMIT
INTENDED-USE
OWNER
REVIEW-DATE
NEXT-PROOF
```

Il reste dans la trace locale du run tant qu’il ne modifie pas une règle partagée. Toute promotion vers une règle commune exige une décision explicite du propriétaire, la compatibilité, l’owner, la preuve et l’entrée de gouvernance appropriée ; un claim local ne devient pas une règle par répétition.

Un claim `À REVÉRIFIER` peut guider une recherche ou un test local. Il ne justifie jamais seul une règle universelle, un seuil, une obligation de production ou une promesse de résultat.

Sépare :

- claim transférable ;
- source observée ;
- asset et droit ;
- observation locale de run.

Une source ou un asset ne devient pas automatiquement un claim. Une observation de run ne devient pas automatiquement une règle durable. Une référence observée ne devient pas automatiquement une autorisation de réemploi.

## Goût, références et tendances

[DURABLE] Le goût n’est pas un canon de marques. C’est la capacité à reconnaître une solution proportionnée, spécifique, lisible et tenue.

Observe une référence pour extraire une relation — rythme, densité, hiérarchie, matériau ou compromis — et non une surface à copier.

En `DIRECTION`, nomme une interface, une ressource hors écran ou un principe réellement observé qui apporte une calibration utile sur un axe concret. Lorsque la direction est nouvelle, ambiguë, risquée ou exposée à une forte convergence générique, un sourcing Web ou une recherche de références est recommandé ; il devient requis seulement si le contrat du run dépend d’un claim, d’une tendance, d’une provenance ou d’une décision qui ne peut pas être honnêtement fondée en mémoire. Si aucune calibration pertinente n’est disponible, déclare cette limite et recherche ou génère une ancre utile.

Le sourcing de `DIRECTION` sépare trois rôles : **ancrage de direction** — pourquoi une référence éclaire un axe ou une décision ; **ancrage de production** — comment un asset, une matière ou un composant peut être construit ; **ancrage de vérification** — comment contrôler lisibilité, accessibilité, comportement, performance ou crédibilité. Une même source peut remplir plusieurs rôles seulement si chacun est explicité. La référence est analysée puis transformée en choix propres au produit ; elle ne sert jamais simultanément de moodboard décoratif, de spécification implicite et de preuve de réussite.

[VEILLE] Les listes de produits contemporains, tendances, registres culturels et snapshots ne sont pas neutres. Chaque élément mobilisé dans un run porte source, date, portée et limite dans sa trace locale.

<!-- noyau:début COMP-VAGUES -->
<!-- concept:ANT-01 -->
**Marqueurs de vague** : pour nommer `MODAL` (`DIRECTION/CREATIVE-BOOT`), jamais pour interdire ; un marqueur gardé par décision reste valide. Ils sont datés, avec leurs sources, limites et Signaux à confirmer, dans `SAVOIR/TOOLS/CONVERGENCE` : charge-la si la convergence peut changer une décision, et retrouve les sources avant tout claim de fréquence, tendance ou provenance.
<!-- noyau:fin COMP-VAGUES -->

### CONVERGENCE — observations datées

[VEILLE 2026-09] **Marqueurs de vague**, pour nommer `MODAL` (`DIRECTION/CREATIVE-BOOT`), jamais pour interdire : un marqueur gardé par décision reste valide. Vague 1 : violet, police Inter, halos et gradient décoratif, hero SaaS à cartes répétées. Vague 2 : fond beige ou crème, brun, serif de caractère ou serif italique, orange rouille, bandeau défilant, illustration peinte, tramage. Vague 3 : dithering, logos pixel, ASCII, hachures de plan, gravures, bleu Klein, libellés mono en capitales, repères de recadrage, paysage peint en fond. Source : essais internes (26-09-2026) et revue de références de designers (27-09-2026), 6 rendus sur 6 sur fond crème et brun, avec ou sans système. Signaux à confirmer : grotesque large ou condensée (Archivo) sur fond blanc neutre avec un seul accent vif (27-09-2026, 3 rendus sur 3, même auteur, non retrouvé ensuite) ; même objet central par brief (fournées du jour ; facture tamponnée) et même grotesque de titre sur un brief, avec ou sans système (30-09-2026, auto-comparaison, 6 rendus). À revoir avant 2027-03.

<!-- noyau:début MOY-CARTE -->
<!-- concept:MOY-01 -->
**Carte des moyens par couche** (datée, dans `SAVOIR/TOOLS/MOYENS`) : des sources, jamais des styles. Si une ressource ou son intégration reste à choisir, charge-la pour chercher par rôle. Vérifie disponibilité, licence et conditions pour chaque ressource retenue au moment de l’intégrer ; le nom d’une plateforme ne vaut ni connexion ni autorisation.
<!-- noyau:fin MOY-CARTE -->

### MOYENS — ressources par couche

[VEILLE 2026-09] **Carte des moyens par couche** : des sources, jamais des styles. Licence et conditions d’usage vérifiées pour chaque ressource retenue, au moment de l’intégrer ; le nom d’une plateforme ne vaut pas autorisation. Pour chaque couche : où chercher, comment choisir, ce qui limite.
- **Typographie :** polices de la marque ; Google Fonts (licences ouvertes, surtout SIL OFL) ; Fontshare (licence FFL ou OFL selon la police). Choisir par la voix et la donnée à porter ; vérifier chargement, graisses et glyphes (accents, chiffres) dans la cible.
- **Icônes :** une famille qui couvre les pictogrammes nécessaires (par exemple Lucide, Phosphor) ; poids, taille et sens accordés au texte ; mélanger des familles demande une raison visible.
- **Composants :** design system fourni, sinon bibliothèque éprouvée (par exemple shadcn, Radix) ; hors Web, les idiomes de la plateforme.
- **Données et objets de preuve :** contenu du client, sinon exemples marqués ; codables, donc au plafond sans intrant.
- **Texture et traitement :** CSS, SVG, canvas ; rendu inspecté sur capture, performance mesurée dans le runtime cible.
- **Photographie :** client (même au téléphone, en lumière du jour), banques sous licence (Wikimedia Commons, Unsplash).
- **Illustration et 3D :** commande, packs sous licence, génération dirigée avec références (`GÉNÉRÉ-DIRIGÉ`).
- **Fichiers et marque :** Figma ou kit de marque par connecteur.

Sans intrant ni route autorisée, les assets figuratifs et le contenu réel restent hors plafond (`FABRICATION`). À revoir avant 2027-03.

**Ce que vaut cette carte.** Elle nomme des sources : le paquet n’en contient aucune et n’a testé ni leur accès ni leur intégration. Une ressource compte dans le plafond seulement une fois atteinte depuis l’environnement du run, chargée dans l’artefact et vue sur capture ; nommée ou seulement atteignable, elle reste une intention. Une police ou une image externe bloquée par `scripts/check_render.py` sans `--allow-external` n’est pas observée. Si l’accès échoue (réseau, licence, connecteur), dis-le et prends la route de production qui tient sans elle (`DIRECTION/VISUAL_TARGET` : `CODE-NATIVE`, `SANS-ASSET` ou emplacement marqué) ; le plafond baisse et la trace le dit.

Une tendance est une hypothèse de direction. Avant de l’utiliser, vérifie qu’elle sert le JTBD, améliore la compréhension, reste accessible et performante et survit lorsque son nom marketing disparaît.

Distingue :

| Niveau | Définition |
|---|---|
| Signal de veille | Observation datée. |
| Principe durable | Mécanisme transférable. |
| Style | Décision située d’expression. |
| Technique | Moyen de production ou de preuve. |

Le terme `same-energy` peut indexer un risque de convergence, mais ne remplace jamais une description causale de l’échec.

### POINTS-DE-DEPART — mesures d’observation datées

[VEILLE 2026-10] **Points de départ chiffrés**, pour caler un premier essai de typographie, de composition, de couleur ou de mouvement sur des ordres de grandeur observés ; jamais pour valider un rendu, imposer un seuil ou interdire un motif. Chaque ligne est un claim `À REVÉRIFIER` : il guide un essai local, se confronte au rendu réel et ne justifie seul ni règle universelle, ni obligation de livraison. Une ligne utilisée dans un run est copiée dans la trace locale au format de claim ci-dessus (type, portée, source, date, limite, usage prévu, owner, date de revue, prochaine preuve).

**Source commune.** Étude de Taste Skill v2.0.0 (dépôt Leonxlnx/taste-skill, licence MIT, fichier research.md des références du skill taste-skill, lue le 2026-10-14) : 248 sites réunis le 2026-10-05 (156 de One Page Love, 92 Awwwards Sites of the Day), 247 chargés, capturés à 1440×900 et 390×844, décrits et notés par 21 modèles. Pour les mesures, « haut » désigne une note de panel de 7,5 ou plus (82 sites mesurables) et « faible » une note sous 6,5 (23 sites mesurables) ; pour les classements du panel, 90 sites hauts et 29 faibles.

**Limites communes.** Notes de modèles d’après des images fixes, ni jurés humains ni notes Awwwards ; une capture par site et par jour ; l’étude dit elle-même que son échantillon est « la mode autant que la qualité » ; vitrines, portfolios et pages d’événements, non des produits ni des outils ; l’effectif « faible » est petit ; le mouvement est inféré des images, non observé. Une corrélation de galerie n’établit pas une cause.

| Domaine | Observation | Usage à tester | Limite propre |
|---|---|---|---|
| Titre d’accueil, taille | Médiane 72 px, soit 5,0 vw ; 6,0 vw chez les sites hauts, 4,7 vw chez les faibles. Sur téléphone, médiane 40 px. | Point de départ d’un essai de hiérarchie : l’écart d’échelle est le levier mesuré. | Mesuré sur des vitrines ; un produit dense ou un outil appelle une échelle plus basse. |
| Plus grand texte de la page | Médiane 6,4 vw ; 8,4 vw chez les hauts, 5,0 vw chez les faibles. | Tester un écart plus net entre le texte dominant et le reste avant d’ajouter un effet. | Corrélation, pas cause. |
| Rapport titre sur corps | Médiane 4,3 ; 4,7 chez les hauts, 4,0 chez les faibles. | Repère de contraste d’échelle pour un titre d’accueil. | Un rapport isolé ne décrit pas une page à plusieurs niveaux. |
| Corps et réglage du titre | Corps : médiane 16 px (moitié centrale 14 à 18). Titre : interlignage médian 1,0 (0,95 à 1,1), approche médiane -0,01 em (-0,03 à 0). | Point de départ avant réglage sur la police livrée. | Polices latines d’abord ; vérifier lisibilité, langue et reflow (`SAVOIR/TYPE`). |
| Nombre de familles | 1 famille sur 31 % des sites, 2 sur 45 %, 3 sur 22 %. | Comparer deux voix sur le vrai titre avant d’en ajouter une troisième. | Une police mono-fonctionnelle pour la donnée n’est pas une voix de plus. |
| Poids du titre | Régulier 48 %, moyen 18 %, gras ou plus 22 %. | Chercher la force dans l’échelle et l’espace avant le poids. | Observation de forme, non de lisibilité. |
| Longueur du titre | Médiane 5 mots et 32 caractères ; 70 % tiennent sur deux lignes à 1440 px, 57 % à 390 px. | Budget de lecture d’un titre (`SAVOIR/CRAFT/CFT-06`). | La longueur ne sépare pas hauts et faibles dans l’étude (71 % contre 83 % sur deux lignes). |
| Marges extérieures | 32 px ou moins sur environ 45 des 114 sites notés 7,3 ou plus ; 80 px ou plus sur environ 8. | Essayer des marges serrées avec de grandes masses à fleur de bord. | Comptes manuels approximatifs, tirés des notes du panel. |
| Titre centré | 39 % des sites, 52 % chez les faibles. Énoncé centré avec média dessous : 7 % chez les hauts, 24 % chez les faibles. | Nommer la trame modale avant de la garder (`BIBLIOTHEQUE/SELECT`, test de trame). | Une trame conventionnelle peut être juste : la convergence de genre n’est pas un défaut en soi. |
| Média au premier écran | Au moins la moitié du premier écran sur 60 % des sites (68 % des hauts, 48 % des faibles). Images par page : médiane 24 ; 37 chez les hauts, 5 chez les faibles. | Tester un média dominant quand la promesse est visuelle. | Suppose des assets réels (`SAVOIR/SOURCE`). |
| Fonds de section | Médiane de 2 fonds distincts chez les hauts, 1 chez les faibles. | Essayer un changement de fond comme articulation avant un filet ou une carte. | Choix de composition, non preuve de lisibilité. |
| Fond et boutons | Fond sombre 41 %, blanc pur 25 %, noir pur 12 %. Bouton principal neutre sur 52 %. Un site sur 246 a un bouton terracotta. | Situer une palette face aux marqueurs de vague (`SAVOIR/CRAFT/CFT-05`). | Corpus de 2026-10 ; la mode de galerie change. |
| Motifs plus fréquents chez les faibles | Dégradés 52 % contre 22 % ; ombres sur éléments au repos 48 % contre 24 % ; petites capitales espacées, trois ou plus, 43 % contre 6 % ; cartes à icône 28 % contre 1 % ; pastille au-dessus d’un titre 26 % contre 5 %. | Signaux d’enquête pour une revue de convergence (`SAVOIR/CRAFT/CFT-01`), non des interdits : un motif motivé et construit reste légitime. | L’étude écarte aussi des motifs « par choix du propriétaire », non par les données. |
| Motifs sans écart net | Flou d’arrière-plan 32 % contre 39 % ; filets fins 61 % contre 52 % ; mot de titre en italique serif 4 % contre 7 %. | Ne pas déduire un défaut de la seule présence. | Pas d’écart ne veut pas dire sans effet sur une page donnée. |
| Motifs plus fréquents chez les hauts | Étiquettes monospace 44 % contre 24 % ; numérotation d’index 38 % contre 21 %. | Nommer la mode avant de la reprendre (`SAVOIR/TOOLS/CONVERGENCE`). | L’étude les écarte de sa propre pratique parce que les générateurs les copient d’abord. |
| Mouvement | Vidéo présente sur 49 % ; environ 10 des 114 sites notés 7,3 ou plus montrent peu ou pas de mouvement ; survol et parallaxe rarement cités. | Un mouvement est un choix de scène, non un plancher (`SAVOIR/CONTEXT`). | Inféré des images ; vitrines seulement. |

**Revue.** Owner : mainteneur du corpus. À revoir avant 2027-04, ou dès qu’une étude plus large ou à jurés humains est disponible. **Prochaine preuve.** Mesurer ces grandeurs sur des rendus du paquet et les comparer à des rendus jugés par plusieurs personnes ; sans cette mesure, ces lignes restent des hypothèses de départ.

---
