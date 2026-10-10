# Changelog — Design Governance V1.0.0

**Version expérimentale :** `V1.0.0`  
**Statut expérimental :** Design Governance V1.0.0 est une expérimentation maintenue.  
**Date de V1.0.0 :** 2026-10-01\
**Révision :** `R2026-10-10-PHASE5`

**Usage recommandé :** pilote contrôlé, supervision humaine et preuve adaptée au risque

## Phase 5 — noyau commun et lecture utile — 2026-10-10

Le noyau commun charge les protections et l’activation utiles à tous les chemins. La table des modes et les détails de fabrication restent dans leurs sources, lus au moment utile. Le registre du compilateur classe chaque bloc comme commun ou servi par une route : un bloc absent, orphelin, incomplet ou sans renvoi fait échouer la compilation. Aucun savoir de détail n’est supprimé pour réduire la skill.

`python3 scripts/read_route.py --mode MODE` sert une seule ligne de la table propriétaire `DIRECTION/CHARGE`, après classification ; il ne choisit pas le mode et conserve ses conditions de preuve et de trace. Le lecteur ne replie un bloc que si son texte complet est effectivement présent dans la section compilée de la skill ; une skill absente ou périmée ne masque pas la source.

L’atelier d’édition est servi par `ACTION/ATELIER-EDITION` dans le produit ; les conditions formelles, preuves et exceptions B1b restent dans la gouvernance. Le traitement des assets moyens rejoint `SAVOIR/SOURCE`. Des sous-routes ciblées servent la composition, la singularité et la repasse sans ouvrir leur chapitre entier. Les anciens locators restent valides.

La skill passe de 44 437 à 18 852 octets UTF-8. Cette mesure concerne le fichier complet ; les caractères de routes servis et le coût réel d’un run restent des mesures distinctes. La réduction du chargement ne prouve pas un gain de qualité, qui reste `NOT-VERIFIED`.

## Finalisation de la refonte — 2026-10-09

Le contrôle des références opérationnelles couvre les extensions courantes, les noms historiques retirés sans extension et les scripts des commandes Python et shell simples. Les options de module ou de code en ligne, les arguments utilisateur, les exemples explicites et les blocs de code ne sont pas traités comme des fichiers à livrer. Les tests couvrent les refus, les chemins valides et les portées des distributions.

Le dossier des sections conservées devient `V1/sections/`. Son contenu, ses codes historiques et l’autorité des sections restent inchangés ; les manifests, liens, lecteur, compilation et préparation de livraison utilisent le chemin courant. Les anciennes dispositions physiques restent reconnues par le lecteur et le compilateur lorsqu’elles sont présentes. Pour reprendre un ancien chemin direct, utiliser le sommaire courant ou le code historique de la section. Le principe de gouvernance utile rejoint la règle de trace dans sa source, et la skill est régénérée.

La CI hébergée est attestée pour `df5aa46` (run 45) et `d2c4d01` (run 46) dans les release notes. Les nouvelles modifications exigent leur validation propre ; l’effet sur la qualité des rendus reste non établi.

## Correctif de recette — 2026-10-09

La mise en pratique sur Maison Lisière a révélé un faux retour de la recette de rendu : les contrôles placés dans un dialogue fermé ou un conteneur `display:none` étaient inspectés comme rendus, puis déclarés sans nom. Le contrôle des candidats DOM exclut désormais les descendants d’un ancêtre non rendu. Deux pages de régression couvrent ces cas ; les contrôles effectivement rendus restent inspectés. Cette correction de mesure ne modifie aucune règle de design et ne constitue pas une preuve d’efficacité du système.

## V1.0.0 — Version initiale expérimentale (2026-10-01)

Design Governance V1.0.0 est un cadre de direction, de création, de jugement et de vérification du design pour agents. Il transforme un brief en proposition composée et spécifique, puis en travail vérifiable, avec une trace proportionnée au risque.

- **Sources normatives.** Les sections propriétaires font autorité à leur emplacement actuel. Les cinq responsabilités historiques sont DIRECTION (classer, diriger, charger), ACTION (preuves, gates, statuts, sorties), SAVOIR (critique et craft), BIBLIOTHEQUE (routes de structure) et CHANGELOG (versions et évolution, dans `maintenance/versions.md` et `maintenance/evolution.md`). Les guides, le glossaire et la carte de lecture en dérivent sans créer de règle.
- **Noyau de fabrication.** Les gestes de structure, de composition, de typographie, de couleur, de contenu et de boucle d’édition sont balisés dans leurs sources et compilés dans la skill `design-governance-practice` (`scripts/build_core.py`). `DIRECTION/CHARGE` est la seule liste de chargement ; les autres tables en sont des vues.
- **Direction avant fabrication.** Prise de brief minimale (`DIRECTION/EXTERNAL-START` : au plus trois demandes, en un seul échange, sur le contenu réel, la marque, l’asset principal ou la route autorisée, et la destination si elle est incertaine), Creative Boot avec `MODAL` / `PARTI`, premier objet de preuve, marqueurs de vague datés (`[VEILLE 2026-09]`) pour nommer la convergence sans l’interdire.
- **Proposition et trace graduée.** Par défaut, le run s’arrête à une proposition, en trace légère ; la première proposition vaut checkpoint, sauf action irréversible ou coûteuse. La trace complète (Gate B, paquet de clôture et projection selon `ACTION/CLOSE-PACKAGE`) s’impose si le run est persistant, partagé, audité ou si une acceptation est demandée. La forme courte LITE peut être complète sans RUN_CARD selon `ACTION/HANDOFF`. Valider une proposition n’est pas l’accepter.
- **Vérité du contenu.** Une destination réelle sans contenu reçoit des exemples marqués, pas des emplacements vides ; l’action principale reste fonctionnelle avec une valeur d’exemple marquée ; les fonctions affirmées d’un produit fictif sont marquées comme exemples.
- **Ancre graduée.** On explore sans ancre avec une limite déclarée ; une direction identitaire n’est acceptée qu’avec une ancre, observée ou fournie pour un produit réel ; sans ancre, la direction reste `EXPLORATORY` ; `FAIL-ASSUMED` est réservé à un échec connu.
- **Interfaces.** `ACTION/UI-UX-REALITY` est chargé avant la fabrication d’une surface UI/UX nouvelle ou substantiellement modifiée ; toute exigence UI/UX déclarée est couverte (`OBSERVED`, `NOT-VERIFIED` ou `N/A-JUSTIFIED`).
- **Entrées.** Une personne entre par `guides/commencer.md`, lié depuis le README, en quatre questions, sans mode à choisir ; un opérateur par le guide `guides/equipe.md` ; un agent par la skill (noyau et `DIRECTION/CHARGE`).
- **Projection machine.** Schéma `RUN_CARD`, contrats de production, cadre de domaine et brief de recherche, avec exemples et fixtures positives et négatives ; profil strict pour les fichiers locaux.
- **Contrôles.** `scripts/validate_all.py` contrôle l’inventaire, les liens, le vocabulaire structuré, les gardes de propriété et le noyau compilé, les contrats machine, la carte de lecture et la liste close des conditions de façade (`validate_reading_map.py`), le lecteur de routes et la reproductibilité des distributions GitHub et Local. Une divergence hors de cette liste close n’est pas détectée.
- **Budget de chargement.** Le fichier `SKILL.md` complet (métadonnées, noyau compilé et contenu hors noyau) est borné à 46 000 octets UTF-8. Le contrôle commun de `scripts/build_core.py` refuse une compilation excessive avant écriture et contrôle chaque distribution via la validation structurelle ; la construction directe contrôle aussi la source canonique avant staging. Au-delà du budget, retirer une redondance ou déplacer un détail vers une route en conservant son activation, sans supprimer un plancher protégé pour satisfaire la taille. Ce budget ne mesure ni la charge cognitive ni le coût complet d’un run.
- **Recherche.** La recherche littérale de routes s’active selon `DIRECTION/CHARGE` ; elle distingue les sources normatives des guides et ne prouve pas l’absence d’un savoir.
- **Préparation.** `scripts/preparer_livraison.py`, réservé à la distribution GitHub, prépare les exports, conserve le journal des contrôles et expose leurs limites, sans publication distante. Les options `--log` et `--journal` désignent le même journal et restent compatibles. <!-- références:github -->
- **Recette de rendu.** `scripts/check_render.py` est une recette de rendu à part, optionnelle : elle exige un navigateur et ne rend aucun verdict global. `validate_all.py` exécute ses tests de comportement (`scripts/test_check_render.py`) ; sans navigateur, la partie qui ouvre des pages est déclarée `NOT-VERIFIED`, jamais réussie ; `--require-browser` fait échouer le contrôle si cette preuve est indisponible.
- **Efficacité.** `NOT-VERIFIED`. Aucune mesure comparative n’établit l’effet du système sur la qualité des rendus ; les runs pratiques orientent sans prouver.

## Autorité et maintenance

Une règle fait foi dans sa section propriétaire, à son emplacement actuel. DIRECTION, ACTION, SAVOIR, BIBLIOTHEQUE et CHANGELOG désignent les cinq responsabilités historiques réparties dans les dossiers du paquet, selon le registre `LIEUX` de `scripts/read_route.py`. Les guides d’entrée et les cartes dérivées orientent la lecture sans créer de règle concurrente. Le schéma `RUN_CARD` et ses validateurs définissent les projections machine dans leur périmètre.

Le lecteur projette les identifiants structurels documentés vers leur titre ou leur section porteuse ; `LAYER/*` reste chez `BIBLIOTHEQUE/COMPONENTS`. Ce raccourci est compatible avec les locators existants, conserve le refus d’un nom absent ou ambigu et ne crée pas de route normative. Sa vérification relève des régressions du lecteur, distinctes du jugement esthétique.

Toute évolution doit identifier une source normative unique, un propriétaire, le périmètre concerné, la compatibilité, la preuve attendue, la limite, la prochaine revue et la procédure de retour. Une évolution ne devient une règle transversale qu’après décision explicite du propriétaire du corpus.

L’historique de conception et de travail n’est pas livré avec cette distribution. Il n’est pas requis pour lire, utiliser ou valider V1.

## Limites de la version

Une validation de package ou de `RUN_CARD` confirme uniquement les contrôles exécutés. Elle ne remplace ni l’observation d’un rendu, ni un test utilisateur, ni une vérification d’accessibilité exécutée, ni une mesure de performance, ni une preuve d’adoption.

La version reste expérimentale. Toute conclusion d’usage doit préciser ce qui a été observé, par quelle méthode, dans quel scope et avec quelle limite.
