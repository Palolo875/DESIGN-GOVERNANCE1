# Notes de version — Design Governance V1.0.0

**Statut expérimental :** Design Governance V1.0.0 est une expérimentation maintenue.
**Usage recommandé :** pilote avec revue humaine.  
**Version initiale :** 1 octobre 2026.  
**Révision :** `R2026-10-11-CORRECTIFS`, 11 octobre 2026.

## Ce que permet la V1

Transformer une demande en proposition de design composée, crédible et observable, puis l’améliorer à partir du rendu réel. Le système relie direction, typographie, couleur, structure, contenu, interaction et qualité du produit. Les techniques de mouvement et de mobile se choisissent selon le travail ; une interface Web mobile ne prouve pas un fonctionnement natif.

L’agent lit un noyau commun, classe le travail puis charge les détails nécessaires au moment utile. Les sections propriétaires font foi à leur emplacement actuel ; guides et cartes les rendent plus faciles à trouver. La gouvernance sert le risque, la preuve, la décision et la reprise.

## Ce qui change dans cette présentation

- Trois [cartes du système](supports/README.md) : responsabilités, parcours d’un travail et boucle créer/apprendre. HTML, SVG clair/sombre et équivalents écrits sont générés depuis les mêmes contenus.
- Le journal public et cette fiche présentent la V1 et sa compatibilité. Le récit du chantier, les anciennes révisions et les preuves restent conservés sur `refonte`.
- Le contrôle des supports refuse une sortie périmée ou une cible locale absente. Les supports sont livrés dans les deux distributions.
- Manrope est réduite aux caractères des supports et compressée en WOFF2 ; les pages et les SVG restent autonomes. La couverture et le poids sont contrôlés.
- Les entrées GitHub mènent aux textes Markdown ; les images suivent le thème clair ou sombre. Le journal garde une ligne par révision dans les deux paquets.
- Le lecteur accepte `--mode SYSTEME` comme alias de `--mode SYSTÈME`. Les titres 5 et 6 du noyau deviennent « Situer l’interface » et « Typographie », sans changer leurs consignes.

Les consignes du noyau restent identiques ; seuls deux titres sont précisés. La skill complète mesure 18 971 octets UTF-8 pour cette révision, contre 18 960 dans PRATIQUE et 18 852 dans PHASE5. Les règles de design, les modes, gates, statuts et schémas sont conservés. Le langage visuel des documents n’impose aucun style aux productions des agents.

## Installer et utiliser

Suivre [l’installation de la skill](README.md#installer-la-skill-dans-un-agent), puis choisir l’entrée adaptée : [commencer](guides/commencer.md), [designer](guides/designer.md), [équipe](guides/equipe.md) ou [maintenance](maintenance/README.md). L’agent garde accès au paquet entier, avec Python 3.10 ou plus récent ; les tests de rendu demandent Playwright et Chromium.

La première proposition oriente la suite ; la valider ne vaut pas l’accepter. Une acceptation demandée passe par les preuves, les limites et la trace complète applicables. Les codes historiques et adresses lisibles désignent toujours les mêmes sections.

## Contrôles inclus

La validation couvre inventaire, liens, références, noyau compilé, projections machine, carte de lecture, lecteur de routes, fraîcheur des supports et reproductibilité des distributions.

```sh
python3 scripts/validate_all.py --require-browser
```

Sans navigateur, les tests de pages restent non vérifiés ; l’option ci-dessus les exige. Les limites de la recette et de la validation documentaire restent explicites.

Les [CI 55](https://github.com/Palolo875/DESIGN-GOVERNANCE1/actions/runs/38092791148) et [56](https://github.com/Palolo875/DESIGN-GOVERNANCE1/actions/runs/38092813117) ont réussi sur `213cfbaf8867142eb834c834311adb0fa626d8fe`, avant ces correctifs. Elles attestent ce commit précis. Cette révision exige ses propres contrôles ; une CI verte ne prouve pas une qualité esthétique générale. Le workflow GitHub exige les tests navigateur. <!-- références:github -->

## Ce que le validateur atteste

Une `RUN_CARD` validée atteste la forme de la projection et les invariants de la liste close. Elle ne prouve ni la réalité des observations, ni la justesse des jugements, ni les droits et données, ni la qualité perceptuelle. La frontière exacte reste dans `ACTION/RUN_CARD`.

## Limites de la V1

**Efficacité : `NOT-VERIFIED`.** Aucune mesure comparative n’établit l’effet général du système sur la qualité, la variété ou le coût des rendus. Le noyau plus court borne le chargement initial ; il ne mesure ni la charge cognitive ni le coût complet d’un run.

Les contrôles automatisés ne remplacent pas un jugement visuel, une tâche représentative, une observation de lecteur d’écran ou une mesure de performance. La compréhension des cartes par de nouveaux utilisateurs reste à vérifier. Les contrôles de plateformes non exécutés restent non vérifiés.

Voir [le journal des versions](maintenance/versions.md) et [la présentation du paquet](README.md). L’historique de travail n’est pas nécessaire à l’installation ou à l’usage de cette V1.
