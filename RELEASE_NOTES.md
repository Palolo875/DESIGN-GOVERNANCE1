# Release notes — Design Governance V1.0.0

**Statut expérimental :** Design Governance V1.0.0 est une expérimentation maintenue.  
**Date de V1.0.0 :** 2026-10-01\
**Usage recommandé :** pilote contrôlé, supervision humaine et preuve adaptée au risque

## Révision R2026-10-08-CORRECTIONS

Corrections faites sans run de mesure, à partir d’un audit complet du paquet, pour que la mesure comparative porte sur une version cohérente. La prise de brief construit dans le même tour ; `DIRECTION/CHARGE` est la seule liste de chargement, complète, et `LITE` se charge plus léger. Un seul bloc d’exécution courte (`ACTION/FAST-PATH`) et un seul jeu d’axes de position. Le noyau gagne l’absolu 4, le piège de conformité et la nuance du premier contact, perd ses répétitions de la boucle d’édition, suit l’ordre d’exécution et reste sous sa taille précédente (43 110 octets).

`check_render --captures` écrit une capture pleine page par largeur sans rien écraser ; ses options et limites (contraste non textuel non mesuré) sont documentées. Le profil strict contrôle les captures de la paire B1b ; la restauration Markdown n’écrit que dans un dossier vide ; `--trouver --guides` couvre le README et les références de la skill ; la CI exécute les tests de pages. L’exemple de brief flou ne fournit plus d’objet à recopier.

Compatibilité : V1.0.0, 69 fichiers GitHub et 63 Local ; aucun nouveau mode, gate, statut ni champ RUN_CARD. Les anciens blocs FAST-PATH de SAVOIR et de BIBLIOTHEQUE deviennent `SAVOIR/JUGEMENT-COURT` et `BIBLIOTHEQUE/AVANT-SELECTION`. Une carte stricte dont une capture B1b locale manque est désormais refusée. **Efficacité : toujours `NOT-VERIFIED`** ; aucun effet sur la qualité des rendus n’est revendiqué.

## Révision précédente R2026-10-04-AUDIT2-FIXES

Les quatre constats F07–F10 du second audit sont corrigés. Le contraste expose sa couverture DOM ; valeurs courantes, placeholders affichés et textes natifs détectés hors calcul conservent une réserve. Un défaut calculé conserve RETURN. L’objet de preuve distingue présence, surface, opacité cumulée et intersection sur les deux axes ; découpes et anciennes mesures incomplètes sont réservées. Son PASS reste borné au CSS et au rectangle, sans certifier pixels, occlusion ou pertinence.

Le profil strict refuse les familles HTTP(S) `example.com`, `example.org`, `example.net` et `.invalid`, avec sous-domaines et point final, pour artefact et trace ; il ne teste pas la disponibilité réseau d’une URL admise. La restauration Markdown refuse chemins non canoniques, destinations équivalentes et collisions fichier/dossier avant écriture, en conservant empreintes et inventaire. Les copies antérieures canoniques restent lisibles par le restaurateur corrigé ; une ancienne copie embarque son ancien code et ne reçoit pas rétroactivement ce correctif.

R01–R04 sont traités dans les supports existants : détails datés et carte des moyens sortis du noyau compilé avec déclencheurs et protections conservés ; fiche d’asset et calibration reliées à la ressource accessible et à l’intervention ; traduction production/observation pour six familles de médiums ; métadonnées de verrou et reprise manuelle documentée. Le verrou et les backups ne sont jamais effacés automatiquement selon leur âge. Le noyau complet mesure 43 201 / 46 000 octets UTF-8, soit 2 799 octets de marge ; cette marge n’est pas une mesure de charge cognitive.

Compatibilité : V1.0.0, 69 fichiers GitHub et 63 Local ; aucun nouveau mode, gate, statut, champ RUN_CARD ni dépendance. La sortie JSON propre à la recette ajoute `contrast_coverage` et `proof_observations`, en conservant `keyboard_coverage`. Les consommateurs de ce JSON doivent tolérer ces clés ; les anciennes mesures incomplètes sont réservées. Le profil strict devient volontairement plus restrictif pour les locators de démonstration.

Les cas ajoutés sont vérifiés sans navigateur, sur mesures synthétiques, code JavaScript livré et DOM simulés, cartes strictes et restaurations réelles dans des dossiers temporaires. Les cas de navigateur restent NOT-VERIFIED s’ils ne sont pas exécutés. Les protections F01–F06 sont conservées ; aucun nouveau run de design ni gain esthétique, de diversité ou d’usage n’est revendiqué. La CI livrée est distincte de son exécution distante, non vérifiée ici.

## Révision précédente R2026-10-04-AUDIT-FIXES

Les six constats de l’audit interne du 4 octobre sont traités : contraste sous opacité de groupe réservé, noms candidats DOM distingués du nom accessible calculé, parcours clavier avec inventaire actif et raison d’arrêt, frontière LITE / ITER explicite, exception de trace complète LITE sans RUN_CARD propagée, et clôtures Markdown de longueur variable lues de façon commune. Les résumés touchés et le noyau compilé sont mis à jour depuis les passages corrigés.

La recette conserve une réserve lorsque sa méthode ne peut pas conclure. La présence d’un candidat de nom DOM ne vaut plus preuve du nom accessible calculé ; la couverture clavier concerne les candidats du périmètre actif et les arrêts observés, sans certifier la visibilité du focus ou toute navigation alternative. Sa sortie JSON ajoute `keyboard_coverage` ; ce résultat de recette est distinct du schéma RUN_CARD, inchangé. Les anciennes mesures sans méthode ou couverture sont réservées.

Les régressions ajoutées portent sur calculs et DOM simulés, cas Markdown valides et mutations des résumés (LCF-55 et LCF-56). Des cas navigateur sont également définis ; ils restent `NOT-VERIFIED` si Playwright ou Chromium manquent. Aucun navigateur n’est installé par les tests, aucun run de design n’est requis et aucun gain esthétique n’est revendiqué par ces corrections. Le budget du noyau complet reste de 46 000 octets UTF-8.

Les capacités de mobilisation précédentes sont conservées :

La carte dérivée contient neuf connexions situées : contexte, typographie, assets, récupération, réemploi, changement partagé, ambition de construction, cohérence de l’ensemble et adaptation au médium. Chaque entrée relie condition et décision, sources propriétaires, intervention et effet attendu, contre-indication et alternative, moyens et limites, observation et réexamen. `read_route.py --connexions` affiche leur sommaire ; un identifiant expose une entrée et ses sources résolues. Le lecteur refuse un index périmé, incomplet ou non résolu ; il ne reconnaît pas automatiquement les conditions applicables et ne génère pas de snapshot.

Un renvoi conditionnel court est compilé depuis DIRECTION. ACTION précise la composition de la vue à partir de la trace existante, y compris hors JSON, et la révision des contributions touchées par un changement. Fabrication, capacité d’observation et autorité restent distinctes ; les contrôles applicables ne disparaissent pas avec une suggestion facultative. La préparation peut activer une intention positive avant observation d’un défaut. Les exemples restent documentaires : aucun nouveau run de design ni rendu n’a été produit pour cette révision.

Trois résumés sont alignés : héritage structurel distinct de non-applicabilité, RUN_CARD liée au niveau de trace et au mode, `risk_coverage` présent dans le gabarit de domaine. Quatre conditions de façade (LCF-51 à LCF-54), avec mutations négatives, protègent ces corrections et le relais d’activation. Les contrôles de l’index et de la CLI portent sur forme, provenance et erreurs ; ils ne prouvent ni pertinence située ni gain esthétique.

BIBLIOTHEQUE rend plus explicite la traduction d’une intention visuelle en responsabilité structurelle, levier de construction et effet attendu. `SELECT` propose six relations conditionnelles ; `CONTRACTS` précise comment calibrer localement espace, objet, typographie, image, matière et comportement. Un relais compact est compilé dans le noyau agent ; DIRECTION, SAVOIR et la carte de lecture renvoient aux propriétaires existants.

Cette révision ne crée aucun style, route canonique, mode, gate, statut ou champ machine. Une structure héritée peut être calibrée sans nouvelle sélection. Les paramètres restent situés dans le projet et ne deviennent pas des tokens partagés par défaut. Les parcours bornés vérifient l’exploitation des ressources ; ils ne démontrent pas un gain esthétique. La prochaine preuve attendue est une réalisation complète avec comparaison des effets attendus et observés.

Le lecteur accepte désormais les identifiants structurels documentés, seuls ou préfixés par `BIBLIOTHEQUE/`. Il renvoie au titre exact ou à la section porteuse d’une ligne de table ; `LAYER/*` reste porté par `BIBLIOTHEQUE/COMPONENTS`. Les identifiants absents, ambigus ou présents seulement dans un exemple de code restent refusés. Sept régressions ciblées protègent cette résolution. Un héritage doit aussi nommer sa source retrouvable ; sans source, la structure est présentée comme hypothèse nouvelle.

### Contrôles et capacités conservés

Six parcours bornés ont été simulés : découverte, première composition de budget, intervention de finesse, affiche expressive, preuve incomplète et migration d’un token partagé. Cette revue par un agent familier du corpus n’est ni aveugle ni une étude utilisateur. Les rendus observés sont vectoriels ; les essais HTML dans un navigateur restent `NOT-VERIFIED`.

Deux corrections antérieures sont conservées : la validation des liens contrôle aussi les sections du même document et ignore les titres présents seulement dans un exemple de code ; une capacité ne peut plus être simultanément disponible, indisponible ou non requise. Les 16 régressions associées et les quatre mutations de mobilisation sont exécutées par `validate_all.py` dans les deux distributions. Elles ne prouvent aucun gain esthétique général.

**Compatibilité.** Version, formats et champs V1.0.0 conservés ; `RUN_CARD` inchangée. Le schéma du contrat conditionnel `creative_direction_set` conserve au moins deux positions distinctes et retire `maxItems: 3`, sans imposer ce contrat aux autres runs. Les contrats auparavant valides restent valides ; une ancienne copie du validateur refuse encore un contrat de plus de trois positions et doit être mise à jour. Les cartes dont un même libellé de capacité apparaît dans plusieurs catégories restent refusées, dans tous les états ; corriger le classement selon les moyens réels. La comparaison retire seulement les espaces périphériques et ne reconnaît pas les synonymes. Les résultats et les artefacts de l’audit sont conservés hors distribution.

Les clarifications de présentation sont conservées : commande de construction, dépendances, inventaire des schémas, renvois, chemins d’exemple et formulations de recherche. La configuration CI livrée reste distinguée de son exécution, non vérifiée pour cette révision.

La préparation conserve les options équivalentes `--log` et `--journal`. Le budget du fichier `SKILL.md` complet est contrôlé par une même fonction lors de la compilation et de la validation de chaque distribution ; un dépassement bloque aussi la construction directe des archives.

`read_route.py --trouver` retrouve littéralement un terme dans les sources normatives et la route qui le sert ; le noyau active cette recherche quand la route utile est inconnue. `preparer_livraison.py` prépare la livraison en une commande, sans envoi ni déploiement.

Elle conserve l’activation de la finesse : le paquet relie le défaut de finesse à un geste concret, à sa condition d’usage et à sa réinspection. Le vocabulaire de `SAVOIR/STATE` est compilé dans la skill et activé par la revue, le chargement et la preuve : le système guide désormais aussi l’intervention précise, dont un bord de 1 px CSS ou un alignement optique lorsque le rendu le justifie.

Les gestes ne constituent pas un style obligatoire : palettes multicolores, vides expressifs, matières diverses et détails multiples restent recevables. Les formats machine restent compatibles avec V1.0.0.

Vérification locale : compilation, intégrité, lecture des routes, renvois, contrats, régressions ciblées et distributions reproductibles. La partie navigateur du test de rendu est `NOT-VERIFIED` quand le runtime requis n’est pas disponible. Aucun gain esthétique réel n’est encore attesté ; les contrôles n’autorisent pas à le revendiquer. L’historique des révisions de travail, avec leur portée et leur procédure de retour, est tenu hors distribution.

## Présentation

Design Governance aide un agent à produire un travail de design dirigé, construit et soigné dès la première proposition, puis à l’améliorer avec la personne qui le demande.

L’agent lit un **noyau de fabrication**, compilé depuis les sources normatives, puis charge ce que la ligne de son mode dans `DIRECTION/CHARGE` demande. Il construit une première proposition composée et tient une **trace proportionnée** : légère par défaut, complète si le run est persistant, partagé, audité ou si une acceptation est demandée.

## Points clés

- **Direction avant fabrication.** Prise de brief minimale, Creative Boot (`MODAL` / `PARTI`), premier objet de preuve et signaux de convergence nommés.
- **Proposition par défaut.** La première proposition vaut checkpoint, sauf action irréversible ou coûteuse. Valider n’est pas accepter : l’acceptation pour un vrai produit se demande et passe en trace complète.
- **Vérité du contenu.** Exemples marqués plutôt qu’emplacements vides ; action principale fonctionnelle avec une valeur d’exemple marquée ; fonctions d’un produit fictif marquées comme exemples.
- **Ancre graduée.** Explorer sans ancre avec une limite déclarée ; accepter une direction identitaire avec une ancre, observée ou fournie ; `FAIL-ASSUMED` réservé à un échec connu.
- **Interfaces.** Réalité UI/UX chargée avant fabrication ; toute exigence UI/UX déclarée est couverte.
- **Projection machine.** Schéma `RUN_CARD` et contrats de production, avec exemples et fixtures.

Le détail est dans [`V1/official/CHANGELOG.md`](V1/official/CHANGELOG.md).

## Contenu

| Élément | Fonction |
|---|---|
| `V1/official/` | Sources normatives, guides d’entrée, glossaire et carte de lecture (`ORCHESTRATION_MAP.md` est un pointeur vers elle) |
| `skills/design-governance-practice/` | Couche d’activation : noyau de fabrication compilé, références conditionnelles |
| `schemas/` | Projections machine, exemples et fixtures de contrôle |
| `scripts/` | Validateurs, compilation du noyau, runner global et construction des distributions |

## Parcours

**Pour une personne qui fait une demande :** la section « Commencer » du README du package. Elle n’a pas de mode à choisir.

**Pour un agent :**

```text
lire la skill (noyau de fabrication) → classer avec DIRECTION/START
→ charger la ligne de son mode dans DIRECTION/CHARGE → construire la première proposition
→ boucle d’édition → réponse visible et trace légère (trace complète si le run est persistant, partagé, audité ou à accepter)
```

**Pour un opérateur :** le guide [`V1/official/QUICKSTART.md`](V1/official/QUICKSTART.md).

## Contrôles inclus

Le package contrôle :

- son inventaire, ses liens et son vocabulaire structuré ;
- ses gardes de propriété et son noyau compilé ;
- ses contrats machine, avec leurs fixtures positives et négatives ;
- sa carte dérivée et son lecteur de routes ;
- la reproductibilité de ses distributions.

Ces contrôles établissent la cohérence documentaire et technique du package. Ils ne remplacent ni une observation de rendu, ni un test utilisateur, ni une vérification d’accessibilité exécutée, ni une mesure de performance, ni une preuve d’adoption.

Pour vérifier le package :

```bash
python3 scripts/validate_all.py
```

Le [workflow livré](.github/workflows/validate.yml) configure Linux (`ubuntu-latest`), Python 3.11 et Playwright 1.56.0 avec Chromium ; il exige les tests de pages (`--require-browser`). Sa présence n’atteste pas son exécution : l’exécution CI de cette révision est `NOT-VERIFIED`. Les contrôles locaux sont décrits ci-dessus.

## Ce que le validateur atteste

Une `RUN_CARD` validée atteste la forme de la projection et les invariants de la liste close.

Elle n’atteste pas :

- que les observations ont eu lieu ;
- la justesse des jugements ;
- la réalité des droits et des données ;
- la qualité perceptuelle.

La frontière exacte est écrite dans `ACTION/RUN_CARD`.

## Limites déclarées

- **Efficacité : `NOT-VERIFIED`.** Aucune mesure comparative n’établit l’effet de la révision actuelle sur la qualité des rendus ; les runs pratiques orientent sans prouver.
- **Convergence.** Le système nomme le modal et demande de justifier ce qui est repris ; il ne garantit pas à lui seul une direction différente.
- **Taille et coût.** Le budget borne le fichier `SKILL.md` complet en octets UTF-8. Il ne mesure ni la charge cognitive, ni les lectures conditionnelles, ni les tokens ou le temps nécessaires au run complet. Aucune mesure actuelle de ce coût n’est établie.
- **Plateformes.** macOS et Windows n’ont pas été observés.
- **Champs libres.** Les placeholders n’y sont pas filtrés globalement.
