# Présentation V1 expérimentale — sources et preuves

Le propriétaire a délégué le choix visuel le 10 octobre 2026. Manrope, les palettes par rôle et la composition documentaire sont retenus pour les supports du système. Ce langage ne prescrit aucun style aux productions des agents.

Ce lot poursuit la carte 01 : trois supports utiles sont intégrés au produit, avec leurs sources, SVG clair/sombre, HTML et équivalents écrits. Les anciennes révisions du journal et des notes sont conservées exactement dans `avant/`. La V1 reste expérimentale ; le nettoyage ne crée ni nouvelle règle de design ni acceptation automatique.

## Lecture

- `trace.md` explique les choix, les défauts observés et leurs corrections.
- `preuves/verification.json` porte 76 parcours réussis, le navigateur, l’empreinte des trois pages et l’arrêt du serveur de mesure.
- Les trois rapports `preuves/gate-a-*.json` gardent les réserves de couverture : aucune conformité exhaustive n’est revendiquée.
- `connexions-reexamen.json` couvre les 27 sources des neuf connexions : le journal changé est relu, 26 autres textes servis sont identiques.
- `verification-controle.json` montre trois mutations refusées : cible absente, ancre absente et sortie périmée. La baseline est valide.
- `conservation.json` rattache les huit originaux à leur commit de base et à leurs empreintes.
- `validation-complete.log` conserve l’exécution du paquet et des distributions ; son résultat final fait foi pour cette observation, pas la seule présence du fichier.

## Limites

76 parcours ne prouvent pas la compréhension par un nouveau public, une préférence humaine, un gain esthétique général ou une conformité d’accessibilité exhaustive. Les observations portent sur Chromium et des viewports émulés. Lecteur d’écran, Firefox, Safari, téléphone réel et performance utilisateur restent hors preuve.

Le titre mobile trop petit et l’absence d’un retour dessiné dans la boucle ont été corrigés après inspection. `avant-retouche/`, `preuves-avant-retouche/` et les journaux correspondants gardent cette version. L’ajout du retour ne crée aucune nouvelle règle : il projette le diagnostic déjà présent dans la section propriétaire.

Le premier lecteur de captures bloquait sur une capture SVG en pleine page ; il a été corrigé pour ouvrir et capturer le SVG à sa taille native. Les passages interrompus et leurs captures partielles restent identifiés comme tels. Le premier build échouait parce que la copie du nouveau validateur précédait la création de son dossier ; l’ordre a été corrigé. Les échecs ne sont pas attribués au paquet final.

Concurrents et anglais restent reportés. Les originaux U6, leurs juges et le prototype Folio demeurent conservés ; ce lot n’est pas une nouvelle comparaison indépendante.

## Livraison du lot

Le commit produit `213cfbaf8867142eb834c834311adb0fa626d8fe` est poussé sur `feat/presentation-v1`. La [PR 2](https://github.com/Palolo875/DESIGN-GOVERNANCE1/pull/2) est ouverte en brouillon ; elle n’est pas fusionnée. `main` reste au commit de base `4e1f9cc20a9887d570a720934ca5b1752c78971a`. Les CI 55 et 56 ont démarré sur le commit produit ; leur observation datée est dans `livraison.json`. Les résultats locaux sont complets.

Le [catalogue livré](produit/supports/README.md) relie les trois pages et leurs fichiers. Depuis ce dossier, on peut rejouer le contrôle des supports avec `python3 produit/scripts/validate_supports.py` et la décision avec `python3 produit/gouvernance/outils/validate_run_card.py --strict run-card.json`. Le lecteur Playwright `verifier-supports.py` accepte `DG_SUPPORTS_REPO` pointant vers le dossier `produit/` ; il nécessite Chromium et Playwright 1.56.0. Les journaux originaux conservent les chemins de la machine qui les a produits.
