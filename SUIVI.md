# Suivi : Design Governance (DG) × Taste Skill v2 (TS)

> **Statut du fichier.** Document de travail, **hors paquet**. Il vit sur la branche orpheline `suivi-comparaison-taste-skill`, qui ne contient que ces notes (aucun fichier du paquet, aucun workflow : pas de CI). Il n'est pas dans `scripts/package_manifest.json` et n'a pas vocation à être fusionné dans le système. Raison de la branche orpheline : voir F4 en 4.2.
> **Créé le** 2026-10-14. **Dernière mise à jour :** 2026-10-14 (après la manche 4 : gouvernance, fichiers non équivalents, améliorations livrées sur `ccr-38b0a56f-t8xdo8`).
> **But :** garder le fil de la comparaison (capacité esthétique et design), ses résultats concrets et ce qu'il faut faire ensuite, sans divaguer.

## 0. Règles de ce fichier

1. Tout résultat porte sa preuve : un fichier lu, une commande exécutée ou un chiffre mesuré.
2. Ce qui n'a pas été lu est écrit comme tel (section 2). Aucun verdict sur un fichier non lu.
3. Une affirmation corrigée n'est pas effacée : elle va dans le journal des corrections (section 7).
4. Les chiffres de l'étude de TS viennent d'un panel de **modèles**, pas de personnes : à traiter comme des claims « à revérifier ».
5. Le dépôt TS est sous licence MIT (Copyright 2026 Leonxlnx) : toute reprise de valeurs ou de données cite la source.

## 1. Les deux objets comparés

| | Taste Skill v2 (TS) | Design Governance V1 (DG) |
|---|---|---|
| Source | `github.com/Leonxlnx/taste-skill`, v2.0.0 du 2026-10-13 (CHANGELOG) | ce dépôt, révision `R2026-10-14-REVUE` |
| Nature | art direction pour pages publiques (landing, portfolio, vitrine) ; exclut dashboards et écrans d'application | jugement + preuve pour tout travail de design, y compris produits, systèmes et états |
| Matière | bibliothèque : 20 directions, 48 héros, 172 sections, 56 palettes, 44 systèmes typographiques, 181 sites étudiés | une trentaine de routes (4 supports, 6 grilles, 6 scènes, 9 objets, 7 micro-interfaces), 8 profils de style, 9 dials, tous qualitatifs |
| Outils | `draw.mjs` (tirage), `lint.mjs`, `inspect.mjs`, `assets.mjs` ; Node 22 + Chromium, zéro dépendance | `read_route.py`, `check_render.py` (Playwright), validateurs, schémas `RUN_CARD`, CI |
| Preuve d'efficacité | test publié (`research.md` §11) : la skill ne bat pas la référence sans skill au jugement de modèles (6,6 / 7,1 / 7,5 / 6,9 / 7,7 contre 7,7 / 8,0 / 7,5 / 7,9 / 7,8) ; 0 FAIL à l'inspecteur contre 8 à 13 pour la référence | `NOT-VERIFIED`, déclaré ; aucun test comparatif |

## 2. Périmètre lu et non lu

**Lu (TS).** `SKILL.md` en entier ; `references/` : `copy`, `type`, `colour`, `layout`, `imagery`, `motion`, `critique`, `tells`, `research` §11 + sommaire ; `scripts/` : `inspect`, `lint`, `lib/rules`, `lib/cdp`, en-tête et logique d'aléa de `draw` ; `library/` : un échantillon de chaque fichier ; skills `redesign` et `minimalist` en entier, début de `soft`, `brutalist`, `stitch`, `gpt-taste`, `output`, `image-to-code` ; CHANGELOG.

**Lu (DG).** `README`, `SKILL.md`, `maintenance/versions`, `references/examples` (début), tout `design/` (direction, produit, savoir) sauf la fin de `formes/catalogue.md` (modificateurs, compatibilités) ; `scripts/check_render.py` (en-tête, `open_page`, contrôle du mouvement réduit). Les `sections/` sont essentiellement des fichiers d'orientation (je n'en ai lu que `SAVOIR.md` en tête et la liste des titres de `ACTION.md` ; le contenu normatif porté par les marqueurs `origine:` est dans `design/` et `gouvernance/`).

**Lu à la manche 4 (fichiers non équivalents).**
- TS : `research.md` §1 à §11 en entier (méthode et résultats de l'étude) ; `gpt-taste` (mécanisme d'aléa), `image-to-code` et `stitch` (parties qui servent la comparaison, pas en entier).
- DG : `gouvernance/*` (statuts, vérification, clôture, schémas, `production_contracts.schema.json`, fixtures), `agent/repondre`, `maintenance/evolution`, `design/formes/catalogue.md` en entier.

**Toujours non lu (à ne pas juger).**
- TS : `image-to-code` et `stitch` en entier ; `soft` et `brutalist` au-delà du début ; `probe.mjs`, `assets.mjs` et `draw.mjs` en entier ; `base.css`, `base.js` ; l'essentiel de `library/`.
- DG : `guides/*`, `agent/chemins`, `references/*` sauf `examples`, `scripts/read_route.py` hors usage.

## 3. Manches 1 et 2 : comparaison par catégorie

Légende : **TS** / **DG** = avantage ; **=** = équivalent ou complémentaire.

| # | Catégorie | Verdict | Preuve principale |
|---|---|---|---|
| 1 | Typographie | **TS** en exécution ; **DG** en résilience (locale, zoom, reflow) | TS `type.md` (échelle de 5 tailles, valeurs `clamp()`, mesure 45 à 75 car.) contre DG `typographie.md` (515 mots, aucune valeur) |
| 2 | Couleur | **TS** opérationnel ; **DG** moins dogmatique | TS `colour.md` (sol 70 à 90 %, accent < 5 %) contre DG CFT-05 (rôles, OKLCH, couleur située) |
| 3 | Composition | **TS** actionnable ; **DG** plus large (applications, supports) | TS `layout.md` (marges 16 à 32 px, lignes d'ancrage) contre DG CFT-03 et catalogue |
| 4 | Idée / direction | **=** (TS pour les sites de marque, DG pour les produits) | TS : inventaire de 8 à 12 éléments + test du concurrent + « élément vivant » ; DG : promesse → objet de preuve → geste, modal / parti |
| 5 | Contre la convergence | **TS** : mécanisme externe | TS tire au sort par script ; DG demande au modèle de se reconnaître (`CFT-05` question de convergence) |
| 6 | Contenu et rédaction | **TS** rédaction ; **DG** vérité | TS `copy.md` ; DG `CNT-01`, `EXD-01`, marquage `TRUTH` ; **DG n'a aucun fichier sur l'art d'écrire** |
| 7 | Images et assets | **TS** en pratique ; **DG** en droits | TS : échelle de 6 niveaux, `assets.mjs`, crédits ; DG : 6 routes de production, mais « le paquet n'en contient aucune » source |
| 8 | Mouvement | **TS** esthétique ; **DG** correction | TS `motion.md` (jetons, 10 recettes) ; DG `SAVOIR/TECH` (interruption, rappels périmés) et contrôle du mouvement réduit |
| 9 | Contrôleurs automatiques | **=** voir manche 3 | `inspect.mjs` contre `check_render.py` |
| 10 | Matière : bibliothèque contre catalogue | **TS** nettement | ~540 entrées concrètes (plans avec positions et version mobile) contre ~32 routes en 3 à 5 lignes |
| 11 | Processus de création | **=** | TS : 10 étapes, 30 à 45 min annoncées ; DG : 5 modes, chemin court possible |
| 12 | Critique du rendu | **=** | TS : 14 passes + note + plafonds ; DG : CFT-00, table symptôme → geste, atelier par retrait, sans note |
| 13 | Interfaces / états / accessibilité | **DG** | TS v2 exclut les écrans d'application ; DG : états, récupération d'erreur, clavier, cibles |
| 14 | Preuve de l'effet | **TS** a mesuré (résultat défavorable publié) | `research.md` §11 |

**Convergences indépendantes (à garder en tête).**
- Même règle de vérité : contenu d'exemple attendu, preuve inventée interdite.
- Même diagnostic de la « vague crème + brun + rouille » (DG `CONVERGENCE` vague 2 ; TS `tells.md` vague 3). TS la fait échouer au contrôle (le `lint` contient des teintes de la marque Claude) ; DG choisit de la « nommer, jamais interdire ».
- « Retirer plutôt qu'ajouter » (DG `ATELIER-EDITION` ; TS : « ne remplis jamais le vide par un autre ornement »).
- « Masque le logo » / « lis sans le texte » (DG `ATELIER-EDITION`, test de style ; TS passes 1 et 3).

**Les autres skills de TS contredisent sa v2.** `redesign` recommande Geist/Outfit/Satoshi (flaggées « police par défaut » par le `lint` v2), grain, dégradés maillés, ombres teintées et verre (interdits en v2) ; `minimalist` met un filet de 1 px sur chaque carte et des étiquettes majuscules espacées (échecs v2) ; `gpt-taste` demande de « simuler » un script Python avec une graine déduite du texte (faux aléatoire, remplacé en v2 par un vrai script). Seule la v2 par défaut est adossée à une étude. Ne pas mélanger.

## 4. Manche 3 : mesures

Environnement : Node 22.22, Chromium 141 (`/opt/pw-browsers`, exécuté en root, donc enveloppe `--no-sandbox` pour TS), Playwright 1.56.0 (la version de votre CI) pour `check_render.py`. Pages de test et résultats bruts dans `essais/` ; commandes dans `essais/LISEZMOI.md`.

### 4.1 Détection : même page, deux contrôleurs

Deux pages d'atelier de vélos : une **non conforme** (défauts volontaires des deux familles) et une **saine** (corrigée). Résultat global :

| Page | TS (`lint` + `inspect`) | DG (`check_render.py`) |
|---|---|---|
| Non conforme | 16 FAIL, 9 WARN (inspect) ; 15 FAIL, 6 WARN (lint) | 3 RETURN (débordement, contraste, structure) ; réserves : noms, clavier |
| Saine | **2 FAIL**, 2 WARN | 0 RETURN ; réserve « noms » (toujours) ; `--proof` non fourni |

Détail par défaut :

| Défaut volontaire | TS | DG |
|---|---|---|
| Titre de 15 mots (5 lignes à 1440 et 768 px, 10 lignes à 390 px) | FAIL | non contrôlé |
| Eyebrow, monospace, numérotation 01/02/03, emoji, filet, dégradé, ombres, verre, nav « pilule » | FAIL / WARN | non contrôlé |
| Palette crème + terracotta | FAIL `palette-claude` | non contrôlé |
| Langue marketing (« seamless », « Get started ») | WARN (lint) | non contrôlé |
| 1 seule image réelle ; pas de point focal | FAIL | non contrôlé |
| Corps 13 px, texte 11 px | FAIL / WARN | non contrôlé |
| 3 textes sous 4,5:1 (1,98 ; 2,85 ; 3,71) | **1 sur 3** (FAIL seulement sous 2,6:1) | **3 sur 3** RETURN |
| Débordement horizontal (bloc de 900 px) | à 768 px seulement ; **390 px non vu** | 390 et 768 px |
| Image sans `alt`, `lang` absent, titre vide | non vu | RETURN |
| Bouton icône sans nom accessible | non vu | **réserve** (« candidat hors couverture ») |
| `outline: none` sur les boutons | non vu | réserve (« aucun changement de style au focus ») |
| Cible de 20 px | non vu | PASS (exception d'espacement WCAG 2.5.8) |
| Animation d'entrée qui ignore `prefers-reduced-motion` | non vu | **non vu** (PASS) |

Lecture : les deux contrôleurs sont **complémentaires et quasi disjoints**. TS voit la composition et le style maison ; DG voit l'accessibilité et la robustesse. TS ne voit aucun des défauts d'accessibilité testés (alt, lang, nom, focus) ; DG ne voit aucun défaut de composition ou de style.

Les 2 FAIL de TS sur la page « saine » sont légitimes selon ses règles : titre « Votre vélo repart ce soir » cassé en 3 lignes dans une colonne étroite (« Votre vélo / repart / ce soir », cassure réellement médiocre) ; paragraphe de contact en grand corps compté comme titre à 390 px. Ma page « saine » était saine pour DG et l'accessibilité, pas pour TS. Les 2 WARN sont : aucune vidéo, et « peu de mouvement » (13 éléments mobiles sur 16 attendus), alors que la page a un mouvement volontairement mesuré : c'est l'effet du quota de TS.

### 4.2 Trouvailles sur `check_render.py` (à transmettre au mainteneur)

- **F1 (vérifié par test ; corrigé en manche 4, voir 5.3).** Le contrôle « Mouvement réduit respecté » ne compte que les animations encore `running` après chargement + attente (`--wait-ms`) + défilement complet (`scripts/check_render.py:375` et `:433`). Une animation d'entrée de **0,8 s** qui ignore `prefers-reduced-motion` donne **PASS**, avec `--wait-ms 1500` comme avec `--wait-ms 100` ; la même animation à **8 s** donne `PASS-WITH-RESERVATION`. Piste : enregistrer les animations dès le début du chargement sous émulation `reduce` (écouteur `animationstart` injecté avant la page), comme le fait le `MOTION_RECORDER` de TS (`inspect.mjs:67`).
- **F2 (à discuter, choix de conception).** Un bouton sans texte, sans `aria-label` ni `title`, contenant un SVG sans `<title>` donne une réserve (« candidat hors couverture »), pas un RETURN, parce que tout SVG rend le candidat incertain. Un cas négatif conclusif pourrait être un RETURN. **Traité en manche 4** (voir 5.3).
- **F3 (observation sur TS, pas sur DG).** `inspect.mjs` n'a pas vu le débordement à 390 px (`horizontalOverflow=0`) alors que `check_render.py` le voit. Cause probable, **non vérifiée** : l'émulation mobile avec `width=device-width` laisse Chromium élargir la fenêtre de mise en page pour contenir le bloc de 900 px.

- **F4 (vérifié par test).** `scripts/validate_design_governance.py` refuse tout fichier absent de `scripts/package_manifest.json` (`fichier inattendu dans le package : …`), et la CI exécute ce contrôle à chaque push de n'importe quelle branche (`on: push`). Ajouter un simple fichier de notes au dépôt fait donc échouer `validate_all.py` (testé avec `--require-browser`). D'où la branche orpheline sans fichier du paquet.

### 4.3 Ce que chaque système fait charger à l'agent (brief : atelier de vélos)

Sources : mots comptés sur les fichiers et sur la sortie réelle de `read_route.py` (DG) et de `draw.mjs --seed 42` (TS). Les octets sont donnés car le français coûte plus de jetons par mot que l'anglais ; **aucun chiffre de jetons n'est mesuré**.

| Niveau | DG | TS |
|---|---|---|
| Minimum | **3 714 mots** (26 Ko) : `SKILL.md` + ligne du mode + arbre de départ | **9 363 mots** (56 Ko) : `SKILL.md` + tirage de 3 options + fiche de direction complète |
| Exigé par le processus | n/d | 12 774 mots (75 Ko) : + `copy.md` et `critique.md` (cités aux étapes 2, 5, 8) |
| Typique, brief flou | **7 854 mots** (54 Ko) : + `EXTERNAL-START`, `COMPOSITION`, `SINGULARITE`, `ATELIER-EDITION`, `CFT-00`, `SAVOIR/STATE` | 18 852 mots (114 Ko) : + `imagery.md` et `motion.md` |
| Étendu (tout ce que le fichier cite) | 16 766 mots (115 Ko) | 28 466 mots (168 Ko) |
| Sortie d'un passage de contrôle | `check_render` : 531 mots (non conforme), 419 (saine) | `inspect` : 1 075 mots (non conforme), 361 (saine), plus des captures par largeur |

Lecture : à contexte comparable, **DG charge environ 2,4 fois moins que TS** (7 854 contre 18 852 mots au niveau « typique »). La différence tient à ce que TS livre une fiche de direction concrète de 4 019 mots (typographie avec lien de chargement, palette, plans de héros et de sections) que DG ne produit pas. C'est un échange : moins de contexte, moins de matière. TS annonce 30 à 45 minutes et quelques centaines de milliers de jetons par build ; DG n'annonce aucun coût.

### 4.4 Exemple de ce que donne le tirage de TS

`draw.mjs --sector other --brief "Atelier de réparation de vélos à Gand" --seed 42 --options 3` propose `borrowed-category`, `one-motif` et `dense-tiles`. La fiche `one-motif` (176 lignes) fixe : le héros « Striped card beside the room », Libre Franklin / Source Serif 4, la palette « Swapping pastels », 5 sections avec leurs plans, mouvement « Slow crossfade », jeu de photos « Mountain ». À noter : la police, décrite comme adaptée aux « essais, rapports annuels, archives et finance », tombe sur un atelier de vélos. Le tirage est aléatoire dans le secteur ; avec `other` (secteur vague) l'adéquation n'est pas garantie, et la règle de TS interdit de re-tirer un créneau « pour le confort » (`--redraw` seulement pour une contrainte de marque ou un asset absent). Fichiers : `essais/resultats/ts_draw_*.txt`.

## 5. Manche 4 : gouvernance, fichiers non équivalents, améliorations

### 5.1 Gouvernance : DG contre le rapport final et les contrôles de TS

Sources : DG `gouvernance/*`, `agent/repondre`, `production_contracts.schema.json` ; TS `SKILL.md` étapes 5 et 10, `critique.md`, `draw.mjs`, `credits.json`, `history.json`.

**Équivalent des deux côtés.**
- Déclarer ce qui n'a pas été exécuté (TS : rapport des contrôles non exécutés ; DG : `NOT-VERIFIED`, capacités déclarées).
- Rapport final avec limites et contenu d'exemple à remplacer.
- Règles d'arrêt (TS : plafonds et passes ; DG : sorties `RETURN`).
- Réserve sur l'auto-évaluation (TS : note avec plafonds ; DG : la revue indépendante B3 est étiquetée, jamais présumée).

**Seulement dans DG.**
Quatre registres (observation, interprétation, décision, persistance) ; statuts STATE ×7, ISSUE ×6, VERDICT ×6, DIRECTION-STATUS ×4 ; cycle de vie des réserves (7 attributs) ; fraîcheur des preuves ; protection du critique ; droits ; étiquettes d'indépendance du relecteur (B3) ; profil de capacité ; schéma `RUN_CARD` avec 20 fixtures ; frontière de validation ; cycle de vie des routes (SEED, PILOT, ADOPTED, DEPRECATED, ABANDONED) ; recette `ACTION/MAINTENANCE` (sans quota, avec « échappatoire théâtrale », « run réel », propriétaire, revue, retour arrière).

**Seulement dans TS.**
Porte de sortie appliquée par un outil (code de retour, pas un conseil) ; graine et journal de re-tirage ; `credits.json` pour les images ; `history.json` contre la répétition entre projets ; un test publié, défavorable à TS.

**Faiblesses de DG relevées.**
- Vocabulaire lourd (beaucoup de statuts et de registres à retenir).
- Automatisation limitée à la porte A : B et C reposent sur le jugement du modèle.
- Bénéfice non démontré : aucun test comparatif. Et le contrat d'évaluation ne le permet pas encore : `EVALUATION_CASE` (dans `production_contracts.schema.json`) a `brief, domain, available_capabilities, expected_depth, artifact, observations, task_results, accessibility_results, visual_review, corrections, final_limits`, mais **aucun champ de bras de comparaison, de référence sans skill ni de relecture à l'aveugle**. Un protocole A/B demande donc d'abord d'étendre ce contrat (ou de le tenir hors paquet).

Lecture : la gouvernance de DG est plus riche et plus honnête sur ce qu'elle ne sait pas ; celle de TS est plus **exécutoire** (un outil refuse de conclure). Les deux idées ne s'excluent pas, mais seule la seconde manque à DG hors porte A.

### 5.2 Fichiers non équivalents : ce que chacun apporte

| Fichier | Ce qu'il fait | Équivalent / apport pour DG |
|---|---|---|
| TS `research.md` §1 à §11 | Étude sur 247 sites de galerie, 21 relecteurs modèles ; parmi les critères mesurables, 82 classés « high » et 23 « weak » ; panel 90 / 29 (chiffres repris de `research.md`, non recalculés) | Source des valeurs de départ importées (voir 5.3). Limite : panel de modèles, sites de galerie (biais de sélection) |
| TS `image-to-code` | Image d'abord, puis code ; lutte contre la dérive entre la maquette et le code | Proche de `LOST-IN-BUILD` et `ANCHOR-GENERATED` de DG ; rien à importer, DG est plus fin sur la perte |
| TS `stitch` | Fichier `DESIGN.md` comme source de vérité du style | Pourrait nourrir les 4 champs de `REUSE-CHALLENGE` ; à étudier, pas fait |
| TS `gpt-taste` | Demande de « simuler » un script avec une graine déduite du texte | À ne pas imiter : faux aléa, contraire à N2 |
| DG `gouvernance/*` | Voir 5.1 | Aucun équivalent chez TS |
| DG `maintenance/evolution` | Cycle de vie des routes, recette de maintenance | Aucun équivalent chez TS (TS versionne par CHANGELOG) |

### 5.3 Améliorations livrées sur `ccr-38b0a56f-t8xdo8`

Deux commits, poussés, **sans pull request** (non demandée) : `8d91faf` (contrôleur) et `e0ab48b` (savoir). `SKILL.md` inchangé (20 246 octets sur un budget de 46 000), aucun bloc `noyau` modifié.

| Réf. | Changement | Statut | Preuve |
|---|---|---|---|
| F1 | `check_render.py` enregistre les animations dès le début du chargement sous mouvement réduit (`MOTION_RECORDER_JS`) ; infinie → RETURN, finie → réserve avec nombre et déplacements, aucune → « aucune animation démarrée » | corrigé | pages de test `animcourte`, `animgardee`, `animopacite`, `animinfinie`, `transitionjs` |
| F2 | Nom accessible des SVG : `<title>` lu ; forme seule sans autre nom → candidat vide, non incertain → RETURN ; `text`, `tspan`, `textpath`, `use`, `image`, `foreignobject`, `a`, ARIA interne et `canvas` restent incertains (réserve) | corrigé (choix de conception à valider) | pages `iconesvg`, `iconesvgtitre`, `iconesvgtexte` |
| B3 partiel | Option `--mesures` : relevés de composition (lignes et taille du titre, corps, tailles et familles distinctes, mesure, médias, centrage, fonds de sections, mots, écrans), **sans seuil ni verdict**, jamais lus par `interpret`, hors du résultat par défaut | livré, optionnel | page `mesures.html`, cas A47 à A52 |
| N1 partiel | `POINTS-DE-DEPART` (dans `design/savoir/gout-et-tendances.md`) : 16 lignes (typographie, composition, couleur, motifs, mouvement), marquées `[VEILLE 2026-10]`, avec source commune (étude TS v2.0.0, MIT, lue le 2026-10-14, n = 248 / 247, 21 relecteurs modèles), limites et ligne de revue (avant 2027-04) | livré en veille, pas en règle | `test_starting_points_and_writing_routes_are_reachable_and_dated` |
| N3 | `CFT-06 — écriture et contenu` : argument avant page, budget de titre (caractères par ligne ≈ largeur ÷ (taille × k), k ≈ 0,40 / 0,50 / 0,58), formes de titre, proposition d'appui et actions, preuve sans invention, formules génériques comme « signaux d'enquête », micro-typographie française, contrat réduit | **PILOT** | accessible par `read_route.py` (`SAVOIR/CRAFT/CFT-06`) |
| N5 | = F1 | corrigé | voir F1 |

**Validation (rejouée le 2026-10-14 sur `e0ab48b`).** `python scripts/validate_all.py --require-browser` : « FULL VALIDATION PASSED — package, RUN_CARD, build et reproductibilité » ; membres des archives = manifeste (GitHub et Local) ; arbre propre. Tests de `check_render` : A 79 / C 65 / B 51 = **195** (161 avant : +12 mouvement, +12 SVG, +10 mesures).

**Limites déclarées (aussi dans `maintenance/versions.md`, « Pilotes en cours »).** Les deux routes et l'option `--mesures` ont été exercées sur des pages de test seulement, jamais sur un vrai brief. Aucun gain n'est démontré : `ADOPTED` exige un gain observé. Les valeurs de `POINTS-DE-DEPART` viennent de modèles relecteurs sur des sites de galerie. Aucune interdiction ni aucun quota n'a été ajouté (D1 à D4 restent ouverts).

### 5.4 Bilan : où en est la capacité esthétique, où en est la gouvernance

- **Capacité esthétique.** L'écart de **méthode** se réduit (valeurs de départ datées, écriture, relevés mesurables). L'écart de **matière** reste entier : TS a ~540 entrées concrètes et un tirage ; DG a ~32 routes courtes. Aucun des deux n'a prouvé qu'il fait mieux qu'un modèle sans skill (TS l'a testé et perd ; DG ne l'a pas testé).
- **Gouvernance.** DG est plus complète et plus prudente ; TS est plus exécutoire. Ce qui manque à DG : une porte de sortie appliquée par un outil au-delà de la porte A, et un contrat d'évaluation comparatif.
- **Contrôleurs.** Quasi disjoints (4.1) ; les corrections F1 et F2 comblent deux trous de DG, `--mesures` prépare le troisième sans y toucher.

## 6. À garder en tête pour la suite

**Nécessaire**
- **N1.** *(partiel, voir 5.3)* Valeurs de départ en typographie, couleur, mise en page et mouvement, étiquetées « point de départ adaptable », importées avec le format de claim de `SAVOIR/TOOLS` (source, date, limite) et non comme règles.
- **N2.** Vrai tirage externe de directions, par script avec historique anti-répétition. Jamais simulé dans le prompt (leçon de `gpt-taste`). Un script Python irait avec votre pile.
- **N3.** *(fait en PILOT, voir 5.3)* Un fichier d'écriture (absent de DG).
- **N4.** *(bloqué : `EVALUATION_CASE` sans bras de comparaison, voir 5.1)* Mesurer : protocole A/B de TS `research.md` §11 (6 briefs, rendus anonymisés, version figée), TS comme troisième bras, juges humains.
- **N5 (manche 3).** *(fait, voir 5.3)* Corriger F1 (mouvement réduit invisible pour les animations courtes).

**Bon**
- **B1.** Inventaire du sujet, test du concurrent, « élément vivant », branchés sur `FIRST-OBJECT`.
- **B2.** Plans (géométrie desktop et mobile) pour les scènes et objets de DG, en gardant « choisir, éviter, preuve ».
- **B3.** *(partiel : `--mesures`, sans réserve ni seuil, voir 5.3)* Signaux esthétiques dans le contrôleur, en réserve (jamais RETURN) : lignes de titre, nombre de tailles, taille du corps, mesure, vraies images, écrans vides, texte couvert, point focal, familles de teinte « vague ». Les mesures de manche 3 montrent que les deux contrôleurs sont quasi disjoints : l'ajout comblerait un vrai trou.
- **B4.** Outil d'images libres de droits avec crédits enregistrés.
- **B5.** Les 14 passes de TS comme consignes d'observation dans CFT-00, sans note.
- **B6.** Jetons et recettes de mouvement, par profil de surface (vitrine contre application).
- **B7.** Le style maison de TS comme profil `STYLE` avec contre-indications, pas comme règles universelles.
- **B8 (nouveau).** Rendre la charge de contexte visible : DG a déjà une ligne de mode de 115 à 292 mots ; garder cet avantage (environ 2,4 fois moins de lecture que TS) en important de la matière **par route**, pas dans le noyau.

**Principes à trancher (décision de l'utilisateur)**
- **D1.** Interdits et planchers mesurés (TS) contre « aucun quota, aucun interdit universel » (DG). Proposition : par profil de surface, en réserve.
- **D2.** Mouvement obligatoire (quota de 8 éléments, TS) contre mouvement seulement s'il sert (DG). La page « saine » de la manche 3 reçoit un WARN de TS pour un mouvement mesuré.
- **D3.** Image réelle d'abord (TS : plancher de 4) contre `SANS-ASSET` à égalité (DG).
- **D4.** Style maison contre pluralité esthétique.

**À ne pas importer :** la note avec plafonds comme verdict ; le quota d'éléments animés hors vitrine ; les listes de polices « à utiliser » (elles deviennent la vague suivante) ; les personas (« agence à 150 k$ »).

## 7. Journal des corrections

| Quand | J'avais dit | Réalité | Preuve |
|---|---|---|---|
| Manche 1 | Taste Skill v2 a trois « dials » | Les dials sont dans `taste-skill-v2-experimental` ; la v2 par défaut n'en a pas | CHANGELOG, README |
| Manche 1 | « Pas de preuve publiée » chez TS | Un test est publié, au résultat défavorable à TS | `research.md` §11 |
| Manche 1 | TS manque de garde-fous sur la vérité du contenu | Faux : « Proof is never invented », crédits, rapport des contrôles non exécutés | `SKILL.md` étapes 5 et 10 |
| Manche 2 | Contraste de TS « lenient » | FAIL sous 2,6:1, WARN sous le seuil requis | `lib/rules.mjs:95-97` |
| Manche 2 | Tous les rendus de TS ont un air de famille | Les interdits sont communs, mais le tirage varie direction, palette, typographie | `draw.mjs`, `library/` |
| Manche 2 | TS ne couvre ni états ni applications | La v2 non ; `redesign` oui (mais contredit la v2) | `redesign-skill` |
| Manche 3 | (hypothèse de travail, non publiée) le PASS du mouvement réduit vient du délai d'attente `--wait-ms` | Faux : `--wait-ms 100` donne aussi PASS ; c'est la durée de l'animation face au moment de la mesure (la page est chargée, attendue, entièrement défilée, puis seules les animations encore `running` comptent) | test 0,8 s / 8 s |
| Manche 4 | Message de commit : « 7 / 9 / 7 tests ajoutés » | 12 / 12 / 10 (161 → 195) | comptage sur `test_check_render.py` ; recommit (reset doux, `--force-with-lease` sur ma propre branche) |
| Manche 4 | Texte de `POINTS-DE-DEPART` avec le mot « violet » et l'expression « question de convergence » | Refusé par `validate_reading_map` (LCF-46, vocabulaire de vague hors lignes `[VEILLE 20…]`) et `validate_structure` (FIDELITY : « question de convergence » exige « police de titre ») | reformulé en « marqueurs de vague » |
| Manche 4 | Chemins d'outils externes entre accents graves dans le texte ajouté | `validate_design_governance` exige que tout chemin opérationnel en accents graves existe | passé en texte brut |
| Manche 4 | Borne de mesure de ligne de ma page de test | écart d'un cran, la mesure réelle de la page est de 48 caractères | assertion corrigée sur la valeur mesurée |

## 8. Prochaines étapes (par ordre)

1. **Décision sur la branche `ccr-38b0a56f-t8xdo8`** (2 commits, CI-équivalent vert) : ouvrir une PR, la relire d'abord, ou la laisser telle quelle. Aucune PR n'est ouverte.
2. **Trancher D1 à D4** (interdits et quotas ; mouvement obligatoire ou non ; image réelle d'abord ; style maison). Rien n'a été ajouté sur ces points.
3. **Gagner le statut `ADOPTED`** : faire tourner `CFT-06`, `POINTS-DE-DEPART` et `--mesures` sur de vrais briefs, avec le gain observé que la recette exige ; sinon laisser en PILOT / VEILLE, ou retirer (retour arrière documenté).
4. **Étendre `EVALUATION_CASE`** (ou un contrat parallèle hors paquet) avec bras de comparaison, référence sans skill et relecture à l'aveugle ; puis seulement le protocole A/B (N4) : DG, TS, référence ; juges humains.
5. **Prototypes restants, un par un et seulement si l'étape 2 le permet** : tirage N2 (script Python, historique anti-répétition) ; plans B2 ; images libres B4 ; passes B5 ; jetons de mouvement B6 ; style maison B7 ; signaux esthétiques en réserve dans `check_render` (suite de B3).
6. **Lire ce qui reste non lu** (section 2) avant tout jugement sur ces fichiers.
