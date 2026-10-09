# Phase 1 — Synthèse de l’audit fichier par fichier

**Date :** 9 octobre 2026.
**Base :** commit `9681d4e`. Rien n’a été modifié dans le système.
**Statut :** proposition. Les dispositions de la section 4 attendent ta validation avant la phase 2.

## Méthode

- **Mesures par outil**, dans `AUDIT2/outils/` avec leurs données dans `AUDIT2/donnees/` :
  - `mesures.py` : taille, titres, codes, phrases, répétitions, contrôles ;
  - `chemins.py` : ce que lit l’agent selon le chemin ;
  - `dependances.py` ;
  - `trouvabilite2.py`.
- **Huit fiches de lecture complète** (`AUDIT2/fiches/01` à `08`), écrites par des sous-agents qui suivaient la [consigne commune](consigne-fiche.md), la charte et les grilles.
- **Un second jeu de recherche** : 50 besoins et 150 formulations, bâtis sans voir les synonymes du lecteur.
- **Vérifications par échantillon** : au moins une affirmation de chaque fiche, contrôlée par moi dans les fichiers (section 7).

**Limites.**
- Les parts « design / gouvernance » sont des estimations faites à la main, section par section.
- L’audit de variété repose sur une seule page par condition (N = 1) et sur les pages déjà produites en U3 et U5.
- Les fiches de lecture ont été rédigées par un modèle plus léger, d’où les vérifications par échantillon.

---

## 1. L’essentiel en dix points

1. **Le savoir de design est solide et rien n’est à jeter sur le fond.** Les huit fiches le disent, chacune pour son fichier. Le problème est la forme, la place et le mélange.
2. **Design et gouvernance sont mêlés dans chaque gros fichier.** Estimations des fiches :
   - DIRECTION : environ 43 000 caractères de design et de produit, 45 000 de gouvernance, 13 000 mixtes ;
   - ACTION : environ 40 % de qualité produit et 60 % de gouvernance ;
   - BIBLIOTHEQUE : environ 40 000 de formes, 30 000 à 35 000 de contrats et de cycle de vie ;
   - SAVOIR : environ un tiers de gouvernance (preuves, champs, délégation).

   Aujourd’hui, le chemin de design ne se lit pas sans la gouvernance (critère S9 : non).
3. **La qualité « produit pro » est enfouie dans la gouvernance.** Le premier rendu, la réalité UI/UX, l’accessibilité (14 contrôles), la preuve visuelle et le craft sur rendu sont rangés dans ACTION, au milieu de la fiche de run et de la clôture. `GATE-A` est à environ 80 % du contrôle produit.
4. **Ce que lit l’agent ne suit pas l’effort demandé.**

   | Chemin | Lecture totale (skill comprise) | Dont design |
   |---|---|---|
   | Petite correction | ~59 000 caractères | 0 |
   | Page nouvelle | ~103 000 | ~24 000 |
   | Produit livré | ~138 000 | ~24 000 |
   | Routes conditionnelles de direction, en plus | ~99 000 | |

   La skill (43 000 caractères) est lue entière à chaque run, quel que soit le mode.
5. **Les résultats convergent vers un second attracteur.** Le système écarte bien le cliché de chaque domaine, mais les pages se ressemblent entre elles :
   - Zilla Slab dans 4 pages de facturation sur 5 ;
   - Barlow Condensed et le concept « profondeur » dans les 3 pages de natation.

   Causes probables (fiche 08) :
   - la liste datée des tendances sert de liste noire, et l’agent prend l’option voisine ;
   - un mot donné en exemple dans la skill, « mécane », est repris dans 4 traces sur 5 ;
   - sur une demande vague, la seule « situation » lisible est celle du domaine.

   Les runs qui mobilisaient tout convergent autant que les autres. **Mon ajout récent, « signaux de page », pourrait renforcer cet effet** (hypothèse H13, à vérifier).
6. **Environ 250 phrases sont verrouillées mot pour mot par les validateurs.** Elles représentent à peu près la moitié des quelque 490 contrôles. Elles bloqueraient la phase de langue : changer un seul mot fait échouer un contrôle. Elles servent aussi d’inventaire des règles, à reprendre dans la table de correspondance avant tout retrait.
7. **La recherche échoue sur des phrases humaines : 3 formulations sur 150 trouvent la bonne route.** Le lecteur cherche l’expression exacte. « police » fonctionne ; « quelle police choisir » ne trouve rien. L’ancien jeu de test (98 sur 121) n’utilisait que des mots-clés.
8. **Il n’y a qu’une porte d’entrée, celle du débutant.** La section « Commencer » du README est bonne (2 262 caractères, sans code), mais elle est précédée de jargon et suivie de 19 000 caractères de maintenance. Rien n’existe pour le designer ni pour l’équipe ; la carte des sujets n’est écrite qu’en codes.
9. **L’historique de travail est livré avec le produit.**
   - Les notes de version sont à 67 % un historique de révisions, avec des identifiants d’audit internes.
   - La section « Autorité et maintenance » du CHANGELOG est surtout un journal de décisions : 10 800 de ses 11 900 caractères.
   - `ORCHESTRATION_MAP.md` n’est plus qu’un renvoi.
10. **Des défauts d’usage concrets.**
    - Installer la skill dans le dossier de l’export, comme le README le suggère, fait échouer la validation (vérifié).
    - `validate_all.py` écrit dans `dist/` et dans les zip : ce n’est pas un contrôle en lecture seule.
    - Le moteur de schéma est copié trois fois, et la liste des fichiers tenue à quatre endroits.

## 2. Grille du système : valeurs de départ

| # | Critère | Valeur de départ |
|---|---|---|
| S1 | Portes par public | 1 sur 4 (débutant, dans le README) |
| S2 | Lecture de l’agent | 59 000 / 103 000 / 138 000 caractères (petite correction / page / produit livré) |
| S3 | Entrée débutant | 2 262 caractères, sans code, mais à 1 067 caractères du haut du README, après un paragraphe de jargon |
| S4 | Trouvabilité | Jeu 1 (mots-clés) : 98 sur 121. Jeu 2 (phrases humaines) : 3 sur 150, et 3 besoins sur 50 |
| S5 | Navigation | 71 routes sur 71 atteignables (audit précédent) |
| S6 | Vocabulaire | 30 à 56 codes pour 1 000 mots dans les sources, 89 dans READING_MAP ; trois systèmes de titres ; 13 titres de niveau 1 dans SAVOIR |
| S7 | Rien de perdu | Les listes « Savoir à protéger » des fiches amorcent la table de correspondance |
| S8 | Contrôles | ~490 : ~252 phrases verrouillées, ~112 de structure, ~122 de gouvernance |
| S9 | Gouvernance séparable | Non |
| S10 | Opérable | Python seul : oui. Installation dans l’export : échoue. Contrôle en lecture seule : absent |
| S11 | Deux langues | Français seul |
| S12 | Supports visuels | Un diagramme Mermaid (gouvernance sur 6 nœuds sur 10, sans légende) ; carte externe |
| S13 | Taille | ~611 000 caractères de documents (en caractères, pas en octets) ; 7 334 lignes de scripts |

## 3. Constats transversaux, par gravité

| # | Constat | Gravité | Preuve | Phase |
|---|---|---|---|---|
| T1 | Design, produit et gouvernance mêlés dans chaque gros fichier | importante | fiches 01 à 04 | 2, puis 3 |
| T2 | Le chemin court ne lit que de la gouvernance ; la page lit 24 000 caractères de design sur 103 000 | importante | `donnees/chemins.json` | 2 (cibles), puis 5 |
| T3 | ~250 phrases verrouillées par les validateurs | bloquante pour la phase 4 | fiche 07 ; `mesures.json` | 2 (contrôles cibles), puis 3 |
| T4 | Jargon et codes ; titres incohérents | importante | `mesures.md` ; fiches 01, 03, 04 | 2 (vocabulaire), puis 4 |
| T5 | Redites. Par exemple : la répartition des propriétaires redite au moins 8 fois, « pas de PASS par défaut » 9 fois, « une capture ne prouve pas » 21 fois, README et QUICKSTART | importante | fiches 01, 02, 03, 06 | 3 et 4 |
| T6 | Convergence des résultats : liste noire, mot d’exemple, objet évident du domaine, gabarits et exemples recopiables | importante (fond) | fiches 08, 04, 05, 06 | 5 |
| T7 | Recherche par expression exacte | importante | `donnees/trouvabilite-jeu2-resultats.json` | 3 (outils) |
| T8 | Une seule porte ; README à six rôles | importante | fiche 06 | 2, puis 3 |
| T9 | Historique et journal de décisions livrés avec le produit ; fichier-pointeur | moyenne | fiche 06 | 3 (lot 1) |
| T10 | Installation dans l’export qui casse la validation | moyenne | vérifié le 9 octobre | 3 (outils) |
| T11 | Outillage dupliqué ; `validate_all` qui écrit ; 22 fichiers de test redondants | moyenne | fiche 07 | 3 (outils) |
| T12 | Schéma unique, peu clair, sans identité visuelle | moyenne | fiche 05 | 6 |
| T13 | Skill lue en entier à chaque run ; `COMP-VOCABULAIRE` en fait 18 %, pour un usage ponctuel | importante | fiche 05 | 5 |

## 4. Dispositions proposées par fichier

Chaque disposition renvoie au détail de sa fiche. **Fond intouché** veut dire qu’on change la place et la forme, pas ce qui est enseigné.

| Fichier | Disposition proposée | Ce qu’il faut traiter avec |
|---|---|---|
| `DIRECTION.md` | **Scinder** en trois parts. (1) La direction créative (boot, domaine, cible visuelle, premier objet, atelier, boucle, et le standard de qualité visuelle aujourd’hui caché dans la Constitution) va au design. (2) Le classement, les modes et le chargement vont à l’entrée de l’agent. (3) Les preuves, la protection et les absolus de gouvernance vont au module. On retire les redites (récapitulatif de protection, double de FAST-PATH, section « 0. Classification ») et trois étiquettes jamais employées. Fond intouché. | 15 blocs de noyau ; ~60 phrases verrouillées ; découpage par titre dans `validate_reading_map.py` |
| `ACTION.md` | **Scinder** en deux. (1) Un module « qualité du rendu », dans le chemin de design : premier rendu, réalité UI/UX, preuve visuelle, Gate A (contrôles et profils), Gate C, passe créative, polish, atelier, checkpoint, sortie et trace légère. (2) Un module de gouvernance facultatif : statuts, préconditions, fiche de run, runs, clôture, override, B1b formel, B2-B3, B5-B6, maintenance. On fusionne les doublons (chemin minimal ×5, premier rendu ×4, « pas de PASS par défaut » ×9, ROUTING face à CHARGE, ANTI-SLOP dans GATE-C). | 4 blocs de noyau qui renvoient au module ; 10 marqueurs de concept ; 3 contrôles de lecture |
| `SAVOIR.md` | **Garder tout le fond** et le réorganiser en livre de référence : titres cohérents, routage déplacé, chapitres nommés en clair. On extrait vers le module ce qui relève de la gouvernance (claims, délégation, champs de preuve). Les valeurs recopiables (liseré 1 px, formule de rayon, recettes de composition non datées) sont un changement de fond : à traiter en phase 5. | 18 blocs de noyau ; LCF-46, 48, 49 et 50 ; titres lus par `read_route.py` |
| `BIBLIOTHEQUE.md` | **Scinder** : un catalogue de formes lisible (41 formes), et à part les contrats, le contrôle structurel et le cycle de vie. Les fixations (sept axes fermés, table d’intentions, matrice de compatibilité, ordre modal écrit en toutes lettres) sont un changement de fond : phase 5. | 5 blocs de noyau ; 14 phrases verrouillées ; titres de route |
| `SKILL.md` | **Phase 5 seulement.** Ordre de lecture ; chemins selon l’effort ; `COMP-VOCABULAIRE` en route à la demande ; consigne de langue ; mécanismes de variété ; retrait du mot d’exemple « mécane ». | `build_core.py` ; plafond de 46 000 octets ; ~30 phrases verrouillées |
| `references/examples.md` | **Réécrire ou retirer en phase 5.** Les exemples sont recopiables, et `SIMULATED` n’est défini nulle part (vérifié). | LCF-26 et LCF-41 (via machine_projection) |
| `references/flow.md` | **Refaire en phase 6**, ou retirer. | 4 phrases verrouillées |
| `references/canonical_minimum.md`, `machine_projection.md` | **Garder et fusionner les doublons.** `machine_projection.md` part dans le module de gouvernance. | LCF-26, LCF-41 |
| `README.md` | **Scinder** : une entrée courte (ce que c’est, les quatre portes, installer, limites) et un document de maintenance. | 56 phrases verrouillées ; balises ENT-01 et CST-01 ; README de l’export généré par `build_distributions.sh` |
| `RELEASE_NOTES.md` | **Réduire** à un journal des versions court. L’historique va dans le dépôt, hors produit. | 14 phrases verrouillées |
| `CHANGELOG.md` | **Séparer** le normatif (version, budget, règle d’évolution, cycle de vie des routes, alias) du journal de décisions, qui sort du produit. | lecture de la version et de la révision par les scripts |
| `QUICKSTART.md` | **Devenir un vrai démarrage court**, selon le public. L’exemple complet recopiable (§9) est à retirer ou à rendre abstrait (phase 5, car il touche l’agent). | 39 phrases verrouillées |
| `GLOSSAIRE.md` | **Réduire** après le vocabulaire de la phase 2. | 16 phrases verrouillées |
| `READING_MAP.md` | **Séparer ses trois cartes.** (1) Sujets : à garder, en noms clairs. (2) Connexions C01 à C09 : du savoir déguisé en carte, à rattacher à leurs propriétaires ou à garder (décision). (3) Combinaisons : orchestration, à garder pour le designer. | 48 phrases verrouillées ; MAP-01 et SUJ-01 ; `read_route.py --connexions` |
| `ORCHESTRATION_MAP.md` | **Retirer.** | 5 citations ou contrôles à adapter |
| `V1/official/README.md` | **Fusionner** dans les portes d’entrée. | 8 phrases verrouillées |
| `read_route.py`, `check_render.py`, `build_core.py` et leurs tests | **Garder.** Le lecteur doit savoir chercher des phrases ; les messages de `check_render` sont à réécrire en clair ; leurs règles d’honnêteté sont conservées. | — |
| Validateurs | **Réduire** les phrases verrouillées après la table de correspondance. Garder les contrôles de structure. Ajouter un mode de contrôle en lecture seule. Un seul moteur de schéma ; une seule liste de fichiers. | mutations rouges pour chaque contrôle gardé |
| `schemas/`, `validate_run_card.py`, `validate_contracts.py` | **Module de gouvernance**, ensemble. Les 22 fichiers de test invalides se réduisent à environ 7. Six points du cœur deviennent conditionnels. | 24 conditions de façade |

## 5. Ce que l’audit change au plan

1. **Avant de ranger, il faut traiter les verrous.** La phase 3 commence par la table de correspondance, puis transforme les phrases verrouillées en contrôles de présence de la règle à sa nouvelle place. Sinon, chaque déplacement casse des dizaines de contrôles.
2. **Les blocs de noyau sont le nœud du problème.** Ils relient les sources à la skill. Un bloc qui change de fichier doit changer de propriétaire dans `build_core.py`. On peut les déplacer en phase 3 sans changer leur texte : la skill reste alors identique à l’octet près, ce qu’un contrôle peut vérifier.
3. **La convergence passe en tête de la phase 5.** C’est un défaut de fond, qui touche le comportement de l’agent ; il n’est pas corrigé pendant le rangement. Ma proposition pour la phase 5 : revoir l’usage de la liste des tendances, retirer les mots d’exemple et les valeurs recopiables, et ajouter un moyen de varier entre deux runs d’une même demande. Cela renforce l’intérêt de la petite mesure (deux runs sur une même demande).
4. **La recherche par phrases** devient un lot d’outils de la phase 3. C’est un changement d’outil, sans effet sur le contenu.

## 6. Décisions pour toi

1. **Le principe des scissions** : séparer design et produit d’un côté, gouvernance de l’autre, dans DIRECTION, ACTION, BIBLIOTHEQUE et une partie de SAVOIR. D’accord ?
2. **L’export « Local »** : garder deux distributions (dépôt complet et export compact), ou n’en garder qu’une ? Six scripts et le build en dépendent.
3. **Les connexions C01 à C09** (READING_MAP) : du savoir à rattacher à ses fichiers propriétaires, ou une aide de navigation à garder telle quelle ?
4. **La copie Markdown produite par `preparer_livraison.py`** : la garder ou la retirer ?
5. **Les corrections de fond repérées** (convergence, exemples, valeurs recopiables) : tu confirmes qu’elles attendent la phase 5 ?

## 7. Vérifications faites par moi, par échantillon

| Fiche | Affirmation contrôlée | Résultat |
|---|---|---|
| 01 | Le standard de qualité visuelle est dans la Constitution (`DIRECTION.md:104`) | confirmé |
| 02 | Le bloc SORTIE cite `N/A-JUSTIFIED` (`ACTION.md:46`) | confirmé |
| 03 | LCF-49 lit `# SAVOIR/DESIGN-ATLAS` avec un seul dièse ; « Règles d’or » et « Méthodologie » sont rattachées à INTEGRITY | confirmé (`validate_reading_map.py:561` ; `SAVOIR.md:969-1050`) |
| 04 | N4 et N5 ont choisi le même couple de tension | confirmé (`N4-trace.md:16`, `N5-TRACE.md:77`) |
| 05 | `SIMULATED` n’est défini nulle part | confirmé (une seule occurrence, dans `examples.md`) |
| 06 | Le QUICKSTART contient un exemple complet recopiable | confirmé (`QUICKSTART.md:197`) |
| 07 | Le dépôt est intact après les essais du sous-agent | confirmé (git propre ; sa copie temporaire a été supprimée) |
| 08 | Zilla Slab dans 4 pages de facturation sur 5 ; Barlow Condensed dans 3 sur 3 ; « mécane » dans `SKILL.md:161` | confirmé |
| Moi | Installation dans l’export, puis validation : échec, « fichier inattendu » | reproduit |
