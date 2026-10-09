# Maintenance

Pour qui fait évoluer le système : d’où vient chaque distribution, comment la préparer et la valider. Rien ici n’est nécessaire pour utiliser le système.

| Fichier | Contenu |
|---|---|
| [`evolution.md`](evolution.md) | Recette d’une modification, promotion et dépréciation des routes, cycle de vie, anciens alias |
| [`versions.md`](versions.md) | Version, révision et contenu de la version |

<!-- origine:README.md -->
## Source de vérité et distributions

Le dépôt GitHub est la **source de vérité**. La distribution Local est un export dérivé : même arborescence et même README, sans les outils de préparation ni l’intégration continue. Elle ne doit pas être modifiée à la main.

Depuis la distribution GitHub, préparez la livraison :

```bash
python3 scripts/preparer_livraison.py
```

Cette commande compile le noyau, exécute les contrôles du package et construit les deux distributions reproductibles, sans envoi ni déploiement.

| Option | Résultat |
|---|---|
| `--empreintes` | Affiche les empreintes SHA256 des archives. |
| `--log CHEMIN` ou `--journal CHEMIN` | Conserve la sortie détaillée des contrôles dans un fichier `.log` ; les deux options sont équivalentes. Par défaut : `.logs/preparer_livraison.log`. |
| `--require-browser` | Exige l’exécution des tests de pages et fait échouer la préparation si le navigateur est indisponible. |

Sans navigateur, les tests de pages restent `NOT-VERIFIED`. Les limites des contrôles restent visibles même lorsque la préparation réussit.

Dans l’export Local, utilisez `python3 scripts/validate_all.py`, avec `--require-browser` si ces essais sont exigés. Cet export ne contient pas la commande de préparation.

Le budget décrit dans `maintenance/versions.md` concerne le fichier `SKILL.md` complet, mesuré en octets UTF-8. Le même contrôle est exécuté lors de la compilation et de la validation des distributions. Il borne la taille chargée ; il ne mesure ni la charge cognitive ni le coût complet d’un run.

### Reprendre une préparation interrompue

Un verrou `.distribution.lock` bloque un second build. `owner.txt`, lorsqu’il existe, indique PID, début UTC et dossier ; ces indices peuvent être absents sur un ancien verrou et ne suffisent pas à prouver qu’un processus est arrêté. Dans le même environnement, inspectez le PID et sa commande (`ps -p PID -o pid,ppid,lstart,args`), les builds de ce dossier et le job ou la session qui les lance. Un PID peut être réutilisé. Tant que l’absence de build actif n’est pas établie, conservez le verrou ; son ancienneté ne justifie aucune suppression.

Avant toute reprise, conservez à part les archives, `dist`, `.dist.previous`, `.archives.previous` et le journal s’ils existent. Si `.archives.previous` existe, ou si `dist` et `.dist.previous` coexistent, le script s’arrête : comparez les inventaires et empreintes, identifiez la dernière livraison complète à l’aide du journal, puis conservez cette livraison et les autres exemplaires dans des dossiers distincts. Ne promouvez pas un mélange de versions et ne supprimez pas une sauvegarde pour forcer le build. Une sauvegarde `.dist.previous` seule est restaurée par le script ; elle ne prouve pas à elle seule l’état des archives.

Lorsque le build est confirmé inactif et les sauvegardes identifiées, retirez uniquement `owner.txt` puis le dossier de verrou vide (`rmdir` refuse un contenu inattendu). Relancez `python3 scripts/preparer_livraison.py` ; le succès exige les contrôles et les exports complets. Si la situation reste ambiguë, conservez les fichiers et le diagnostic pour le mainteneur. Aucun verrou ni backup n’est effacé automatiquement selon son âge.

Pour produire seulement les deux archives, exécutez :

```bash
bash scripts/build_distributions.sh
```

Le build régénère les distributions de travail dans `dist/` et écrit les archives déterministes suivantes à la racine du dépôt :

```text
Design_Governance_V1_GITHUB.zip
Design_Governance_V1_LOCAL.zip
```

Les modifications doivent être apportées aux sources du dépôt, puis vérifiées par les contrôles et le build. Les archives et exports ne sont pas des sources normatives indépendantes.

<!-- origine:README.md -->
## Validation

Utilisez Python **3.10 ou plus récent**. Les contrôles documentaires et machine utilisent la bibliothèque standard Python. La recette de rendu et les tests qui ouvrent des pages nécessitent en plus **Playwright et son navigateur Chromium** ; sans eux, ces tests restent `NOT-VERIFIED`. La construction des archives nécessite Bash, `zip` et les outils Unix utilisés par `scripts/build_distributions.sh` ; elle a été contrôlée sous Linux.

Les tests JavaScript sur DOM simulés utilisent un runtime Node déjà disponible ; son absence laisse cette partie `NOT-VERIFIED`. `python3 scripts/test_check_render.py --skip-browser` exécute seulement les tests synthétiques et les DOM simulés, sans ouvrir de page ni installer de dépendance.

La projection machine comprend aussi les contrats de production : `DOMAIN_FRAME`, `RESEARCH_BRIEF` et les contrats de direction créative, de réalité UI/UX et d’évaluation. Ils sont illustrés dans `gouvernance/schemas/examples/` et contrôlés par `gouvernance/outils/validate_contracts.py`.

| Commande | Fonction |
|---|---|
| `python3 scripts/validate_design_governance.py` | Contrôle l’inventaire, les liens Markdown relatifs, le vocabulaire structuré et les conventions du package. |
| `python3 gouvernance/outils/validate_run_card.py` | Exécute la suite intégrée de validation des projections et des fixtures `RUN_CARD`. |
| `python3 gouvernance/outils/validate_run_card.py chemin/run.json` | Valide un fichier JSON ciblé et échoue s’il est absent, malformé ou sémantiquement invalide. |
| `python3 gouvernance/outils/validate_contracts.py --type production_contracts chemin/contrat.json` | Valide un contrat ciblé, y compris hors du package ; sans `--type`, la famille est détectée par les clés racines. |
| `python3 scripts/validate_reading_map.py` | Vérifie la carte de lecture, ses propriétaires, ses locators et sa frontière non normative. |
| `python3 scripts/read_route.py --connexions` | Affiche le sommaire des connexions situées ; ajouter un identifiant comme `C03` pour lire condition, contributions, limites et sources résolues. |
| `python3 scripts/test_audit_regressions.py` | Exécute les régressions de navigation, de capacités et de conditions de façade ; ne mesure ni la compréhension utilisateur ni la qualité esthétique. |
| `python3 scripts/validate_all.py` | Exécute les contrôles documentaires, machine, CLI, fixtures négatives, compilation et reproductibilité des distributions. |
| `python3 scripts/validate_all.py --lecture-seule` | Exécute les mêmes contrôles sans construire ni écrire : `dist/` et les archives ne sont pas touchés ; build et reproductibilité restent `NOT-VERIFIED`. |

Les chemins `chemin/run.json` et `chemin/contrat.json` sont des exemples à remplacer par ceux de vos fichiers. Pour exécuter les contrôles intégrés du package :

```bash
python3 scripts/validate_design_governance.py
python3 gouvernance/outils/validate_run_card.py
python3 scripts/validate_all.py
```

Ces contrôles vérifient la forme du package, de ses projections et de ses distributions, ainsi que la liste close des conditions de façade ; une divergence hors de cette liste n’est pas détectée. Ils ne remplacent ni l’observation d’un rendu, ni un test utilisateur, ni une vérification d’accessibilité exécutée, ni une mesure de performance, ni une preuve d’adoption. Une projection `RUN_CARD` valide reste une trace structurée ; elle ne transforme pas une cible de conformité, une capture ou une validation CLI en preuve de résultat.

Une `RUN_CARD` validée atteste la forme de la projection et les invariants de la liste close ; elle n’atteste ni la réalité des observations, ni la justesse des jugements, ni la qualité perceptuelle. La liste exacte vit en un seul lieu : la frontière de validation d’`ACTION/RUN_CARD`.

<!-- origine:READING_MAP.md -->
## Résolution des routes

Les noms de route sont des locators documentaires. Pour les résoudre, utiliser le fichier propriétaire, puis son titre exact. Un renvoi qui ne résout pas doit être déclaré obsolète, conceptuel ou `NOT-VERIFIED`; il ne doit jamais être traité comme une instruction active par supposition.

| Préfixe | Propriétaire |
|---|---|
| `DIRECTION/*` | `DIRECTION.md` |
| `ACTION/*` | `ACTION.md` |
| `SAVOIR/*` | `SAVOIR.md` |
| `BIBLIOTHEQUE/*` | `BIBLIOTHEQUE.md` |
| `CHANGELOG/*` | `CHANGELOG.md` |
| `RUN_CARD` | `gouvernance/schemas/run_card.schema.json`, exemple et validateur |

`RUN_CARD` est un **adaptateur machine**, pas un locator Markdown résolvable par `scripts/read_route.py`. Pour l’inspecter ou le valider, utiliser le schéma, l’exemple et `gouvernance/outils/validate_run_card.py`; ne pas l’invoquer comme une route documentaire.
