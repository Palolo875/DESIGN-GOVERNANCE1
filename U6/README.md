# Suite de phase 5 : kit U6 prêt, comparaison non exécutée

Les versions avant `99caa027` et après `6e5a8c2` sont copiées et contrôlées par empreintes. Les six dossiers de production sont vides. Le protocole est figé avant les résultats ; le choix du mode d'exécution est en attente. Aucun résultat esthétique, coût réel de production ou verdict de propriétaire n'est déclaré.

Le plan prévoit quatre pages de facturation (deux par version), puis deux pages d'atelier vélo avec rendez-vous (une par version). Les mêmes moyens sont fournis aux producteurs. Lire `protocole.md` pour les critères et les limites. `protocole.json` contient la correspondance privée des versions : ne jamais le transmettre aux juges.

## Exécution par le coordinateur

1. Obtenir le choix explicite des agents séparés ou des essais fournis depuis un outil extérieur. Dans cet environnement, le lancement de sous-agents demande une instruction explicite. Si l'outil ou le modèle change, réviser et figer cette seule déclaration de protocole avant le premier run ; conserver la version précédente. Ne pas mélanger des témoins produits par un autre modèle.
2. Vérifier `sha256sum -c PROTOCOLE-SHA256SUMS` et `sha256sum -c CONTROLES-SHA256SUMS`, puis les manifestes des six paquets et des moyens. Pour utiliser ailleurs le kit, adapter les chemins avant génération et conserver cette révision explicitement ; les consignes actuelles ciblent `/workspace/remesure-phase5`.
3. Exécuter `run-01` à `run-06` dans cet ordre, avec six contextes neufs et la même configuration. Chaque producteur reçoit uniquement son `runs/run-NN/consigne.txt`, son paquet, son dossier de livrable et les moyens communs. Le coordinateur conserve les identifiants, les heures de début/fin, les interventions et les dépassements dans un journal distinct. Aucun résultat n'est remplacé ou supprimé pour améliorer la comparaison.
4. Après chaque run, vérifier les actions du `functional-tests.json` du producteur dans un nouveau contexte, en conservant les observations réelles. Puis lancer les captures ci-dessous. Un défaut reste visible et rapporté ; ne pas réécrire le livrable avant jugement.

```sh
/workspace/cloud-setup/design-governance/venv/bin/python capturer.py runs/run-01/livrable runs/run-01/audit-final
python mesurer.py
```

Répéter les captures pour chaque run ; la mesure de lecture agrège tous les journaux disponibles. `capturer.py` utilise Chromium sur un serveur HTTP temporaire lié à `127.0.0.1`, puis ferme le serveur. Il refuse d'écraser des preuves. Il capture les premières scènes et les pages entières sur trois largeurs, observe les erreurs, les requêtes, le clavier et des indices d'accessibilité. Ses observations automatiques ne suffisent pas à vérifier le parcours principal, la vérité du contenu ou l'accessibilité complète.

5. Quand les six audits indépendants existent, préparer les captures anonymisées :

```sh
python anonymiser.py jugements
```

Le script refuse une capture manquante ou modifiée et un livrable changé depuis les mesures. Chaque juge reçoit uniquement son dossier `jugements/juge-N`. Les deux ordres sont inversés ; ces juges de la même famille constituent une comparaison descriptive avec aveugle imparfait. Le coordinateur garde les résultats séparés jusqu'à leur consolidation.

6. Présenter ensuite la galerie anonyme et les limites techniques au propriétaire. Son jugement reste requis sur R1 à R4 et R9 ; une préférence d'agent ne clôt pas ces critères. Actualiser le plan avec les résultats effectivement obtenus, les divergences et les points restant ouverts.

## Mesures et limites

`lire.py` journalise les caractères servis, les plages et les répétitions ; `mesurer.py` calcule également leur union. Cette instrumentation n'atteste pas la compréhension par le modèle. Le repère « avant production » est la première existence d'`index.html`, ce qui doit rester explicite. Les en-têtes du lecteur sont inclus : cette mesure ne se confond pas avec les recettes mécaniques précédentes qui les excluaient.

La durée est celle du coordinateur, outils et attente de service compris. Les jetons API restent non mesurés tant qu'aucun compteur fiable n'est disponible. Six pages, deux briefs et deux répétitions ne permettent pas d'établir un effet général ou une significativité.

## Contrôle du dispositif

Le contrôleur a été exécuté sur deux fixtures techniques séparées, chacune en 1440, 390 et 320 px. La fixture valide ne présente ni débordement ni erreur de script. La fixture défectueuse est détectée pour débordement étroit, erreur JavaScript, demande externe bloquée, champ sans libellé, image sans texte alternatif et ancre absente. Les captures de test ont été inspectées. Voir `autoverification/bilan.json` ; ces tests vérifient le contrôleur, aucun résultat du système de design.

La source du produit reste propre sur `fix/refonte-gouvernance`, commit `6e5a8c2`. Le kit se trouve hors dépôt ; il ne modifie ni la PR ni l'environnement cloud enregistré.
