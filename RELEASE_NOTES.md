# Notes de version — Design Governance V1.0.0

**Statut :** V1.0.0, révision `R2026-10-22.3` du 22 octobre 2026 ; une expérimentation maintenue, à utiliser en pilote avec revue humaine.

## Ce que permet la V1

Transformer une demande en proposition de design composée, crédible et observable, puis l’améliorer à partir du rendu réel ; ou juger et analyser un existant. Le système relie direction, typographie, couleur, structure, contenu, interaction et qualité du produit. Les techniques de mouvement et de mobile se choisissent selon le travail ; une interface Web mobile ne prouve pas un fonctionnement natif.

L’agent lit un noyau commun (la skill, 30 864 octets UTF-8), classe le travail, lit le tronc de son mode puis charge les détails nécessaires au moment utile. Les sections propriétaires font foi à leur emplacement actuel ; guides et cartes les rendent plus faciles à trouver. La gouvernance sert le risque, la preuve, la décision et la reprise. Le langage visuel des documents n’impose aucun style aux productions des agents.

Le savoir de fabrication arrive aussi au moment où il sert : trois cartes de moment (avant le build, après une capture, avant de proposer) et, sous les signaux des recettes, le geste lié du tableau de craft. Un registre local des choix rend visible d’un run à l’autre la répétition des polices et des palettes ; un spécimen compare des voix sur le vrai titre ; une planche demande à une personne une correction nommée sur la dernière finition. Leur statut d’essai est tenu dans [la fiche de version](maintenance/versions.md#sections-à-lessai).

Le contenu détaillé du paquet est décrit dans [ce que contient le système](maintenance/versions.md).

## Installer et utiliser

Suivre [l’installation de la skill](README.md#installer-la-skill-dans-un-agent), puis entrer par le niveau utile : [utiliser](guides/1-utiliser.md), [comprendre](guides/2-comprendre.md), [maîtriser](guides/3-maitriser.md), ou [faire évoluer le système](maintenance/README.md). L’agent garde accès au paquet entier, avec Python 3.10 ou plus récent ; les tests de rendu demandent Playwright et Chromium.

La première proposition oriente la suite ; la valider ne vaut pas l’accepter. Une acceptation demandée passe par les preuves, les limites et la trace complète applicables. Les codes de route et les adresses lisibles désignent les mêmes sections.

## Contrôles inclus

La validation couvre inventaire, liens, références, noyau compilé, projections machine, carte de lecture, lecteur de routes et fraîcheur des cartes. Dans le dépôt GitHub, elle reconstruit aussi les deux distributions et vérifie leur reproductibilité ; l’export Local contrôle le paquet exporté, sans les outils de construction.

```sh
python3 scripts/validate_all.py --require-browser
```

Sans navigateur, les tests de pages restent non vérifiés ; l’option ci-dessus les exige. Dans le dépôt GitHub, le workflow exécute ces contrôles avec les tests navigateur sur chaque commit ; son résultat se lit sur le commit livré. Une CI verte ne prouve pas une qualité esthétique générale. <!-- références:github -->

## Ce que le validateur atteste

Une validation du paquet ou d’une `RUN_CARD` confirme les contrôles exécutés et la forme de la trace ; la frontière exacte est dans `ACTION/RUN_CARD`.

## Limites de la V1

**Efficacité : `NOT-VERIFIED`.** Aucune mesure comparative n’établit l’effet du système ; le détail de ce qui est vérifié est dans [la fiche de version](maintenance/versions.md#ce-qui-est-vérifié-ce-qui-ne-lest-pas). L’installation est vérifiée avec Claude Code et Codex ; les autres agents compatibles avec le format Agent Skills restent à vérifier.
