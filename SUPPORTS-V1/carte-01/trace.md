# Première proposition de carte — V1 expérimentale

10 octobre 2026. Le propriétaire a demandé les diagrammes d’abord, puis le nettoyage éditorial. Ce lot présente la carte et son langage visuel avant extension. Les travaux restent séparés du produit sur `refonte`.

Mode DIRECTION : hypothèse de direction des supports, sans adoption identitaire. Décision : placer le design au centre tout en rendant les entrées et l’autorité compréhensibles. Risque : faire passer une carte de responsabilités pour un ordre d’exécution, ou présenter la gouvernance comme facultative. Preuve minimale : contenu rattaché aux sources, carte claire/sombre, lecture étroite, clavier, contrastes et exports inspectés. Arrêt : proposition complète, vérifiée et disponible pour discussion.

## Avant construction

Base produit : `4e1f9cc20a9887d570a720934ca5b1752c78971a`. Sources d’architecture inspectées : README, `design/README.md`, `gouvernance/README.md`, `V1/sections/README.md`, guide pour commencer et flux de la skill. Les six publics viennent de la table d’entrée du README. Les sections propriétaires conservent leur autorité à leur emplacement actuel ; cette carte reste une vue dérivée.

Promesse : comprendre où entrer et quel rôle joue chaque partie. Objet : carte de responsabilités reliées, avec un grand domaine Design et quatre matières nommées. Geste : choisir son entrée, lire le point de départ puis ouvrir la source. La sélection met en évidence des parties sans retirer le contexte. Sur téléphone, les mêmes responsabilités se recomposent en blocs lisibles ; aucune carte minuscule n’est imposée.

Parti : un atlas documentaire, avec bordures nettes, axes de lecture, titres de rôle et espaces maîtrisés. Les couleurs distinguent les domaines ; leur nom et leur fonction portent aussi l’information. Le cœur Design possède une masse plus forte que les accès. La maintenance entretient l’ensemble ; elle n’est pas une dernière étape du travail. Les relations avec la gouvernance sont réciproques et décrites selon le risque, la décision et la reprise.

Alternative plausible : une liste linéaire de parties, déjà présente dans le README. Elle est commode pour retrouver un fichier, mais rend moins visible le centre du système et les responsabilités reliées. L’équivalent textuel conservera cette qualité de lecture. Une comparaison typographique portera sur le vrai titre de la carte : Manrope et une voix serif existante, avec même contenu et même scope ; choix après observation.

Route de fabrication : SVG et HTML, sans asset illustratif. Manrope et Instrument Serif proviennent des fontes OFL déjà fournies dans nos essais ; licences conservées. La voix finale concerne les supports documentaires, pas les rendus que le système aide à créer. Pas de bibliothèque d’interface ni de dépendance réseau. Le générateur utilise Python standard ; le navigateur Playwright/Chromium déjà installé sert à l’observation.

État du support : proposition exploratoire. L’architecture est observée dans le dépôt ; la direction visuelle est une hypothèse fabriquée par le coordinateur. Aucun test de compréhension avec des personnes ni lecteur d’écran humain n’est annoncé. Les animations ne sont pas nécessaires à cette carte.

Sources de méthode lues : skill locale, arbre START, ligne DIRECTION, RUN-DIRECTION, CREATIVE-BOOT, VISUAL_TARGET, FIRST-OBJECT, TYPE, FIRST-RENDER et UI-UX-REALITY. Observation et clôture seront mobilisées à leur moment utile.

## Après observation

### Portée de la preuve

Médium : page Web et SVG autonome. Portée : état initial à 1440, 1280, 1024, 768, 390 et 320 px, clair et sombre ; six choix de public ; thème, clavier, équivalent textuel et export sélectionné. WCAG 2.2 AA sert de base aux contrôles ciblés, sans déclaration de conformité globale. Méthode : parcours automatisés dans Chromium 151.0.7922.173 et inspection des captures par le coordinateur. Budget : page sans ressource externe ni animation ; performance réseau et INP non mesurées. Couverture : émulation du viewport, aucun participant, lecteur d’écran ou téléphone réel. Prochaine preuve : comprendre avec une personne si elle trouve la bonne entrée et distingue carte et section propriétaire.

### Résultats

Le passage final donne 27 réussites, aucun échec. `preuves/verification.json` porte l’empreinte complète du HTML, le navigateur, les périmètres et l’arrêt du serveur. Toutes les cibles de public sont résolues au commit Git produit exact, et non selon le seul contenu de la branche extraite. Les variantes claire et sombre, la sélection d’agent et son SVG exporté ont été ouvertes. Les SVG autonomes ont été rouverts et capturés. La licence embarquée a été comparée au texte original OFL.

Le texte SVG a un contraste minimal calculé de 5,65:1 en clair et 7,07:1 en sombre, selon les couleurs peintes et le fond direct. Les boîtes des textes restent dans les bornes horizontales de leur groupe. Les contrôles natifs, détails et liens conservent leurs noms et un parcours clavier ; une inspection automatisée des noms ne remplace pas un lecteur d’écran.

La recette Gate A du produit a été exécutée séparément à 320, 390, 768 et 1440 px, avec la recommandation de point de départ comme objet de preuve. Aucun `RETURN` au passage final ; les réserves de couverture restent visibles dans `preuves/gate-a.log`. Le complément SVG résout la mesure des glyphes SVG peints, pas les autres réserves de la recette. Le premier appel utilisait par erreur `#system-map`, absent : résultat conservé à part, puis commande corrigée avec `.recommendation`, sans changement de l’artefact.

La reconstruction des six sorties est identique à leurs empreintes observées. Les fontes sont fournies localement et sous OFL. Sans JavaScript, la carte, le texte et les sources restent accessibles ; les commandes dépendant du script sont désactivées.

### Ce qui a changé

Le premier passage avait des erreurs dans le lecteur de captures et une hypothèse incorrecte sur le focus de `select_option`. Le second a montré deux défauts de reflow réels : le texte agrandi faisait dépasser la page à 390 et 320 px. Les règles de composition du produit ont été corrigées : colonnes réductibles, retour des métadonnées à la ligne et matières recomposées selon la taille du texte. Le test n’ajoute aucune règle de grille ou de retour à la ligne pour cacher ces défauts. Les échecs et captures sont conservés.

Le bandeau mobile a été compacté, le titre réparti en deux phrases équilibrées et le dernier mot isolé supprimé. La paire `preuves-deuxieme-essai/390-titre-sans.png` / `preuves/390-titre-sans.png` montre cette retouche à contenu constant. Les captures du texte agrandi montrent la correction de reflow. L’ajout final de la licence SVG est non visuel ; les contrôles et captures ont été régénérés sur cette version.

Les captures du titre Manrope et Instrument Serif ont été comparées à 390 et 1440 px. Manrope est proposé pour la continuité documentaire avec les labels et les descriptions ; Instrument Serif donne un titre plus éditorial. Les deux sont conservés. La sélection reste une hypothèse d’auteur à discuter, sans adoption d’identité ni préférence humaine mesurée.

### Clôture de ce lot

Verdict : `EXPLORATORY`. Direction partiellement tenue : la carte est complète, les relations et l’autorité sont explicites, mais la compréhension et l’identité attendent un regard extérieur. V : preuve visuelle avec réserve ; U : non vérifié ; A : preuve ciblée avec réserve ; T : construction et parcours observés avec réserve de plateforme. Le défaut dominant restant est la compréhension réelle de cette densité documentaire par une personne découvrant le système.

La gouvernance appliquée à ce lot sert sa reprise : trace des choix, fichiers sources, périmètre des preuves et projection structurée. Elle ne transforme pas la proposition en identité acceptée. Arrêt de la retouche : première carte disponible pour la discussion prévue, avant l’extension aux autres supports. Nettoyage public et intégration restent ouverts.

Commandes de preuve exécutées sur le produit figé :

```sh
DG_SOURCE_REPO=/workspace/DESIGN-GOVERNANCE1 /workspace/cloud-setup/design-governance/venv/bin/python /workspace/carte-systeme-v1/verifier.py
/workspace/cloud-setup/design-governance/venv/bin/python scripts/check_render.py /workspace/carte-systeme-v1/index.html --browser-executable /usr/bin/chromium --serve-local --widths 320,390,768,1440 --proof '.recommendation' --json /workspace/carte-systeme-v1/preuves/gate-a.json --captures /workspace/carte-systeme-v1/preuves/gate-a
python3 gouvernance/outils/validate_run_card.py /workspace/carte-systeme-v1/run-card.json --strict
```
