# U1b — Fiche d'inventaire n°6 : les outils exécutables

**Base :** commit `d90869c`. **Lecture intégrale :** `check_render.py` (578 lignes), `build_core.py` (170), `preparer_livraison.py` (209) ; `read_route.py` (455) lu en entier pendant U1. **Testé :** `check_render` sur deux pages réelles (U1, test T-16) et sur une page chargeant une police externe (ci-dessous). **Angle :** ce que le système sait réellement **exécuter**.

## 1. Vue d'ensemble

| Outil | Taille | Sert à | Utilisé pendant un run ? |
|---|---|---|---|
| `check_render.py` | 38 Ko | **Observer** un rendu HTML dans un vrai navigateur | Oui, si l'agent pense à le lancer (renvoi depuis GATE-A seulement) |
| `read_route.py` | 23 Ko | **Accéder** au savoir : lire une route, chercher un terme, lister les connexions | Oui, le noyau le demande |
| `build_core.py` | 8 Ko | **Compiler** le noyau de la skill depuis les sources, sous un budget | Non, maintenance |
| `preparer_livraison.py` | 13 Ko | **Livrer** : compiler, tout valider, construire les archives, produire les copies Markdown | Non, maintenance |

Les validateurs (210 Ko) et les tests (77 Ko) font l'objet d'une fiche à part.

## 2. `check_render.py` : le seul outil d'observation

**Ce qu'il fait** (vérifié par lecture et par exécution). Il ouvre la page dans Chromium sans interface, à plusieurs largeurs (par défaut 390, 768 et 1440 px), puis rend **11 contrôles** :

| Contrôle | Méthode | Statuts possibles |
|---|---|---|
| Débordement horizontal | Largeur de défilement contre largeur visible, éléments fautifs nommés | PASS, RETURN |
| Défilement horizontal interne | Conteneurs et feuilles ouvertes | PASS, réserve, RETURN |
| Erreurs JavaScript au chargement | Erreurs de page et de console | PASS, RETURN |
| **Contraste du texte** | Couleurs effectives converties en sRGB, superposition des fonds, seuils WCAG 4,5:1 ou 3:1 selon la taille et la graisse | PASS, réserve, RETURN |
| Nom accessible des contrôles | Candidat tiré du DOM (pas un calcul AccName complet) | PASS, réserve, RETURN |
| Taille des cibles | WCAG 2.2, critère 2.5.8, avec l'exception d'espacement (cercle de 24 px) | PASS, réserve |
| Structure du document | `alt` des images, `lang`, titre | PASS, RETURN |
| Un seul titre de niveau 1 | Comptage des h1 visibles | PASS, réserve |
| **Parcours clavier** | Tabulation réelle ; un indicateur de focus est un *changement* de style ; candidats non atteints listés | PASS, réserve |
| Mouvement réduit | Préférence « reduce » activée, animations encore en cours | PASS, réserve, RETURN |
| Objet de preuve au premier écran | Sélecteur fourni avec `--proof` : présence, surface, opacité, intersection avec l'écran | PASS, réserve, RETURN, non vérifié |

**Sa rigueur :** chaque contrôle qui ne peut pas conclure rend une **réserve, jamais un PASS**. Il produit une provenance (empreinte de l'artefact, méthode, date, largeurs) et des codes de sortie exploitables : 0 sans RETURN, 1 avec RETURN, 2 si non exécutable. Il ne simule jamais une preuve si le navigateur manque. Il est couvert par 125 cas de test, dont 26 avec un vrai navigateur (tous passent, U1).

**Ses options, dont deux ne sont documentées nulle part** (vérifié par recherche dans tout le dépôt) :

| Option | Effet | Documentée ? |
|---|---|---|
| `--widths` | Largeurs observées | Oui (aide du script) |
| `--proof SELECTEUR` | Contrôle de l'objet de preuve | Oui (ACTION l. 818) |
| `--json FICHIER` | Résultats et provenance en JSON | Oui |
| **`--click SELECTEUR`** (répétable) | **Observer un autre état** (menu ouvert, erreur, onglet) | **Non**, seulement dans l'aide du script |
| **`--allow-external`** | **Laisser charger polices et images hébergées ailleurs** | **Non**, seulement dans l'aide du script |
| `--wait-ms`, `--tab-stops` | Attente après chargement ; borne du parcours clavier | Aide seulement |

**Test fait pour cette fiche :** une page qui charge la police Fraunces depuis Google Fonts.
- Sans option : **2 requêtes bloquées**, le rendu est jugé avec la police de repli.
- Avec `--allow-external` : **0 requête bloquée**, et la police est effectivement chargée (vérifié dans le navigateur : `Fraunces : loaded`).

Le constat C39 est donc à corriger : le blocage est le **comportement par défaut**, et une option existe pour l'éviter. Le vrai défaut est qu'elle n'est expliquée nulle part.

**Ce qu'il ne fait pas :**
1. **Aucune capture d'écran**, alors qu'il a déjà la page ouverte dans un vrai navigateur. Les « captures desktop et mobile entières » et la « vue de masses » exigées par ACTION ne sont donc produites par aucun outil du paquet.
2. **Aucun jugement perceptuel**, et c'est voulu : ni hiérarchie, ni foyer, ni direction (« ne valide ni la direction visuelle, ni l'utilisabilité »).
3. Pas de contraste des éléments non textuels (bordures, icônes), pas de contraste sur image ou dégradé (réserve déclarée), pas de contrôle du contenu (exemples marqués, chiffres cohérents).
4. **Web seulement** : rien pour un document, une présentation ou une image.

**Accès :** `check_render` n'apparaît **pas** dans le noyau (0 occurrence). L'agent ne le découvre qu'en lisant `ACTION/GATE-A`, puis la section « Contrôles applicables ».

## 3. `read_route.py` : l'accès au savoir

**Ce qu'il fait** (lu en entier en U1, testé en U1) :
- **Lire une route** : résolution en trois étapes (table de READING_MAP, préfixe de titre, sous-titre), ambiguïtés refusées, sous-blocs qui ont leur propre locator exclus. Les identifiants structurels (`GRID/AXIAL`…) sont des raccourcis vers BIBLIOTHEQUE.
- **Chercher un terme** (`--trouver`) : littéral, sans accents ni casse, sans synonymes ; indique la route la plus précise qui contient chaque occurrence ; `--guides` ajoute les guides de `V1/official/` (mais pas le README ni les références de la skill, C25).
- **Connexions** (`--connexions`) : sommaire des 9 connexions de READING_MAP, puis une entrée avec ses sources résolues ; refuse un index dont la révision diffère du CHANGELOG.

**Rigueur :** refuse un fichier non UTF-8, un locator en double, un propriétaire incohérent. Couvert par 50 tests.

**Limites :**
- aucune sélection automatique de ce qui est pertinent (déclaré en tête du script) ;
- la recherche ne connaît pas les synonymes (« trop froid » ne mène pas à la table des émotions) ;
- les sous-routes n'existent que là où il y a des sous-titres (le découpage par profil de GATE-A est impossible).

## 4. `build_core.py` : la compilation du noyau

**Ce qu'il fait :** assemble 42 blocs balisés des sources dans un **registre de 8 sections ordonnées** (l. 34-59) ; vérifie que chaque bloc est ouvert, fermé et unique ; refuse d'écrire si `SKILL.md` dépasse **46 000 octets** ; `--check` signale toute différence entre la skill et sa compilation.

**Potentiel déjà présent mais inutilisé :** une **projection de colonnes** (`project`, l. 101-111) permet de ne garder que certaines colonnes d'un tableau dans le noyau. Les 42 blocs ont tous `None` : elle n'a jamais servi.

**Coût d'un changement d'ordre ou de contenu du noyau :** modifier la liste de 8 entrées (quelques lignes), recompiler, valider.

## 5. `preparer_livraison.py` : la livraison

**Ce qu'il fait :** compile le noyau, lance `validate_all` (contrôles, tests, construction des archives GitHub et Local, reproductibilité), puis en option écrit les deux copies Markdown (complète et documents seuls), **vérifie leur restauration à l'octet près** et affiche les empreintes. Il refuse de s'exécuter hors de la distribution GitHub et garde un journal.

**Limite déjà relevée :** le script de restauration qu'il embarque dans la copie écrase sans avertir et suit les liens symboliques internes (C10, tests T-01 à T-05).

## 6. Ce que le système sait exécuter, en résumé

| Capacité | Outil | État |
|---|---|---|
| Observer les fautes objectivables d'une page web | `check_render` | **Solide et testé** ; deux options utiles non documentées ; pas de capture |
| Retrouver un savoir par route ou par mot exact | `read_route` | **Solide** ; pas de synonymes ; guides partiellement couverts |
| Garder le noyau fidèle aux sources et sous budget | `build_core` | **Solide** ; projection inutilisée |
| Livrer des archives reproductibles | `preparer_livraison` | **Solide** ; restauration permissive (C10) |
| Produire des captures, des vues de perception, comparer avant/après en images | — | **Aucun outil** |
| Observer un document, une présentation, une image | — | **Aucun outil** |
| Vérifier le contenu (exemples marqués, chiffres cohérents) | — | **Aucun outil** |
| Juger la qualité perceptuelle ou fournir un regard extérieur | — | **Aucun outil** (voulu pour le jugement ; absent pour le regard extérieur) |

## 7. Observations à verser au registre

| Observation | Preuve | Lien |
|---|---|---|
| **Correction de C39** : le blocage des ressources externes est le comportement par défaut ; `--allow-external` le lève (testé : 2 → 0 requêtes bloquées, police chargée) | Test ci-dessus | C39 révisé |
| `--click` (observer un autre état) et `--allow-external` ne sont documentés que dans l'aide du script | `git grep` sur tout le dépôt | Nouveau |
| `check_render` est absent du noyau (0 occurrence) | `SKILL.md` | Nouveau |
| `check_render` ouvre déjà un vrai navigateur mais ne prend aucune capture, alors qu'ACTION exige des captures | `check_render.py` l. 279-365 ; ACTION l. 724-731 | Lien avec la fiche n°5 |

## 8. En une phrase

Le système possède **quatre outils sobres, rigoureux et bien testés**. Le plus précieux pour la qualité, `check_render`, observe honnêtement les fautes objectivables d'une page web, mais il est **absent du noyau**, a **deux options utiles non documentées**, et **ne produit aucune des images** que le reste du système demande à l'agent de regarder.
