# Journal des versions — Design Governance V1.0.0

**Version expérimentale :** `V1.0.0`
**Statut expérimental :** Design Governance V1.0.0 est une expérimentation maintenue.  
**Version initiale :** 1 octobre 2026.  
**Révision :** `R2026-10-11-CORRECTIFS`, 11 octobre 2026.  
**Usage recommandé :** pilote avec revue humaine et preuves adaptées au risque.

## V1.0.0 — présentation expérimentale

Cette révision rend le paquet plus facile à parcourir : trois cartes reliées aux sections propriétaires, un journal public court et des notes de version centrées sur l’usage. Les supports ont un équivalent écrit, des variantes claire et sombre, une lecture mobile et des sources régénérables.

Le cœur conserve direction, savoir, formes et qualité du produit. L’agent lit le noyau, classe le travail, puis charge les détails utiles depuis l’unique table des modes. La gouvernance adapte la trace et les preuves au risque, à la décision et à la reprise. Aucun mode, gate, statut, schéma ou contrat d’acceptation n’est ajouté ou retiré par cette présentation.

Les codes historiques et les adresses lisibles restent compatibles. Le journal est accessible par `maintenance/versions` et `CHANGELOG`. Les distributions GitHub et Local gardent la même arborescence ; Local est un export dérivé. Après mise à jour du paquet, recopier la skill dans l’agent.

**Efficacité : `NOT-VERIFIED`.** Les créations et jugements exploratoires orientent le travail ; aucune mesure comparative n’établit une amélioration générale de qualité, de variété ou de coût. Une validation du paquet ne remplace ni une observation du rendu ni une tâche utilisateur.

Les révisions restent résumées ci-dessous pour les personnes qui ne disposent que du paquet. Le détail du chantier et les preuves de fabrication sont conservés dans la branche documentaire `refonte`.

## Révisions en bref

| Révision | Changement principal |
|---|---|
| `R2026-10-11-CORRECTIFS` | Police réduite, lecture Markdown et images adaptées au thème sur GitHub, alias SYSTEME, titres du noyau précisés et historique succinct rétabli. |
| `R2026-10-10-PRESENTATION` | Trois cartes générées, journal et notes publics nettoyés, travaux conservés hors produit. |
| `R2026-10-10-PRATIQUE` | Moments de lecture, premier objet, alternatives situées et techniques de mobile/mouvement précisés ; skill de 18 960 octets. |
| `R2026-10-10-PHASE5` | Noyau commun et détails chargés au moment utile ; skill de 18 852 octets. |
| `R2026-10-09-COHERENCE` | Autorité clarifiée, références corrigées, gouvernance adaptée et sections conservées renommées. |
| `R2026-10-09-REFONTE` | Entrées par public, rangement du système et arborescence GitHub/Local unifiée. |
| `R2026-10-08-ACCES-MATIERE` | Activation du savoir, lecteur de routes et structure d’une page renforcés après U5. |
| `R2026-10-08-CORRECTIONS` | Corrections de l’audit complet, sans nouvelle mesure de rendu. |
| `R2026-10-04-AUDIT2-FIXES` | Corrections du second audit interne, constats F07 à F10 et R01 à R04. |
| `R2026-10-04-AUDIT-FIXES` | Corrections du premier audit interne, constats F01 à F06. |
| `V1.0.0`, 1 octobre 2026 | Version initiale expérimentale. |

## Contrats de maintenance conservés

- **Budget de chargement.** Le fichier `SKILL.md` complet (métadonnées, noyau compilé et contenu hors noyau) est borné à 46 000 octets UTF-8. Le contrôle commun de `scripts/build_core.py` refuse une compilation excessive avant écriture et contrôle chaque distribution via la validation structurelle ; la construction directe contrôle aussi la source canonique avant staging. Au-delà du budget, retirer une redondance ou déplacer un détail vers une route en conservant son activation, sans supprimer un plancher protégé pour satisfaire la taille. Ce budget ne mesure ni la charge cognitive ni le coût complet d’un run.

## Portée des contrôles

La validation couvre la cohérence documentaire et technique, dont la liste close des conditions de façade. Une divergence hors de cette liste n’est pas détectée. Le contrôle des supports vérifie leur fraîcheur et leurs cibles ; il ne juge pas le rendu. Les tests de pages exigent un navigateur et restent non vérifiés lorsqu’ils ne sont pas exécutés.

## Autorité et maintenance

Une règle fait foi dans sa section propriétaire, à son emplacement actuel. DIRECTION, ACTION, SAVOIR, BIBLIOTHEQUE et CHANGELOG désignent les cinq responsabilités historiques réparties dans les dossiers du paquet, selon le registre `LIEUX` de `scripts/read_route.py`. Les guides d’entrée et les cartes dérivées orientent la lecture sans créer de règle concurrente. Le schéma `RUN_CARD` et ses validateurs définissent les projections machine dans leur périmètre.

Le lecteur projette les identifiants structurels documentés vers leur titre ou leur section porteuse ; `LAYER/*` reste chez `BIBLIOTHEQUE/COMPONENTS`. Ce raccourci est compatible avec les locators existants, conserve le refus d’un nom absent ou ambigu et ne crée pas de route normative. Sa vérification relève des régressions du lecteur, distinctes du jugement esthétique.

Toute évolution doit identifier une source normative unique, un propriétaire, le périmètre concerné, la compatibilité, la preuve attendue, la limite, la prochaine revue et la procédure de retour. Une évolution ne devient une règle transversale qu’après décision explicite du propriétaire du corpus.

L’historique de conception et de travail n’est pas livré avec cette distribution. Il n’est pas requis pour lire, utiliser ou valider V1.

## Limites de la version

Une validation de package ou de `RUN_CARD` confirme uniquement les contrôles exécutés. Elle ne remplace ni l’observation d’un rendu, ni un test utilisateur, ni une vérification d’accessibilité exécutée, ni une mesure de performance, ni une preuve d’adoption.

La version reste expérimentale. Toute conclusion d’usage doit préciser ce qui a été observé, par quelle méthode, dans quel scope et avec quelle limite.
