# Notes de version — Design Governance V1.0.0

**Statut expérimental :** Design Governance V1.0.0 est une expérimentation maintenue.
**Usage recommandé :** pilote avec revue humaine.  
**Version initiale :** 1 octobre 2026.  
**Révision :** `R2026-10-14-REVUE`, 14 octobre 2026.

## Ce que permet la V1

Transformer une demande en proposition de design composée, crédible et observable, puis l’améliorer à partir du rendu réel. Le système relie direction, typographie, couleur, structure, contenu, interaction et qualité du produit. Les techniques de mouvement et de mobile se choisissent selon le travail ; une interface Web mobile ne prouve pas un fonctionnement natif.

L’agent lit un noyau commun, classe le travail puis charge les détails nécessaires au moment utile. Les sections propriétaires font foi à leur emplacement actuel ; guides et cartes les rendent plus faciles à trouver. La gouvernance sert le risque, la preuve, la décision et la reprise.

## Ce qui change dans cette révision

Cette révision traite les constats de la revue du système (carnet conservé sur `refonte`). Elle ne crée ni mode, ni gate, ni statut, ni champ de schéma.

- **Installation.** La recette crée les dossiers, met la skill à jour sans sous-dossier imbriqué et distingue la copie, l’accès au paquet et le chargement par l’hôte. Les références de la skill citent des chemins depuis la racine du paquet ; un contrôle refuse tout lien qui sortirait de la skill copiée.
- **Profil strict des fiches de travail.** `?` ou `inconnu` ne valent plus adresse d’artefact ; un fragment ou une requête (`exemple: page.html#hero`) ne masque plus un fichier absent.
- **Contrats.** Une même exigence UI/UX ne peut plus porter deux statuts contradictoires au même locator.
- **Recette de rendu.** Un contrôle remis visible sous un parent masqué garde son nom ; la couleur qui remplit réellement le texte (`-webkit-text-fill-color`) est évaluée, et un texte peint par son fond reste en réserve.
- **Contrôles du paquet.** L’en-tête de la skill refuse une valeur lue en YAML comme nul, booléen, nombre ou date. Le journal de préparation reste sous `.logs/` ou hors du paquet.
- **Cartes.** Leur version vient du manifeste ; une relation qui ne correspond plus au dessin est refusée ; la double ponctuation des pieds de carte disparaît.
- **Consignes précisées.** La première scène et l’alternative écartée valent pour une demande de fabrication ; un jugement ou une analyse se conclut sans scène imposée, et la réponse omet les rubriques sans contenu. Montrer une proposition ne rend pas un run persistant ni partagé. L’état vide conçu peut accueillir une première utilisation réelle ; l’arrêt d’un one-shot `DIRECTION` suit le tour d’atelier ; « une décision par écran » vaut pour un parcours guidé ; la densité d’un canevas opérationnel suit la tâche ; la boucle d’équipe modifie le rendu quand un défaut le justifie.
- **Renvois.** Les gestes de finition pointent vers leurs routes ; les emplacements du savoir, la revue en six points et le classement d’un brief flou sont précisés.

La skill complète mesure 19 705 octets UTF-8 pour cette révision. Le langage visuel des documents n’impose aucun style aux productions des agents.

## Installer et utiliser

Suivre [l’installation de la skill](README.md#installer-la-skill-dans-un-agent), puis choisir l’entrée adaptée : [commencer](guides/commencer.md), [designer](guides/designer.md), [équipe](guides/equipe.md) ou [maintenance](maintenance/README.md). L’agent garde accès au paquet entier, avec Python 3.10 ou plus récent ; les tests de rendu demandent Playwright et Chromium.

La première proposition oriente la suite ; la valider ne vaut pas l’accepter. Une acceptation demandée passe par les preuves, les limites et la trace complète applicables. Les codes historiques et adresses lisibles désignent toujours les mêmes sections.

## Contrôles inclus

La validation couvre inventaire, liens, références, noyau compilé, projections machine, carte de lecture, lecteur de routes et fraîcheur des supports. Dans le dépôt GitHub, elle reconstruit aussi les deux distributions et vérifie leur reproductibilité ; l’export Local contrôle le paquet exporté, sans les outils de construction.

```sh
python3 scripts/validate_all.py --require-browser
```

Sans navigateur, les tests de pages restent non vérifiés ; l’option ci-dessus les exige. Les limites de la recette et de la validation documentaire restent explicites.

La [CI 59](https://github.com/Palolo875/DESIGN-GOVERNANCE1/actions/runs/38096660032) a réussi sur `5a5f56357d829150ac5a1863c3c40f35c4c3bafa`, la révision précédente. Elle n’atteste pas cette révision, qui a sa propre exécution sur son commit ; une CI verte ne prouve pas une qualité esthétique générale. Le workflow GitHub exige les tests navigateur. <!-- références:github -->

## Ce que le validateur atteste

Une `RUN_CARD` validée atteste la forme de la projection et les invariants de la liste close. Elle ne prouve ni la réalité des observations, ni la justesse des jugements, ni les droits et données, ni la qualité perceptuelle. La frontière exacte reste dans `ACTION/RUN_CARD`.

## Limites de la V1

**Efficacité : `NOT-VERIFIED`.** Aucune mesure comparative n’établit l’effet général du système sur la qualité, la variété ou le coût des rendus. Le noyau plus court borne le chargement initial ; il ne mesure ni la charge cognitive ni le coût complet d’un run.

Les contrôles automatisés ne remplacent pas un jugement visuel, une tâche représentative, une observation de lecteur d’écran ou une mesure de performance. La compréhension des cartes par de nouveaux utilisateurs reste à vérifier. Les contrôles de plateformes non exécutés restent non vérifiés.

Voir [le journal des versions](maintenance/versions.md) et [la présentation du paquet](README.md). L’historique de travail n’est pas nécessaire à l’installation ou à l’usage de cette V1.
