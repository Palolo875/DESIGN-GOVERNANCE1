# Savoir — système de design

Tokens et composants partagés.

<!-- origine:SAVOIR.md -->
# SAVOIR/SYSTEM — tokens et composants

[REQUIS PAR LE MODULE — blast radius partagé, token ou primitive] Sépare tokens primitifs — mesures, palette, familles — et tokens sémantiques — surface, texte, action, danger, élévation.

Documente le comportement des tokens et composants, pas seulement leurs noms. Lorsqu’un token, composant, convention, format ou comportement affecte plusieurs consumers, plusieurs surfaces ou une source de vérité partagée, signale à `DIRECTION/START` l’effet partagé. START classe en `SYSTÈME` si la décision partagée est l’objet direct du run ; si elle découle d’une décision de direction, la direction est traitée d’abord et le run système dépendant ouvert ensuite, sauf décisions inséparables (`DIRECTION/START/TREE`).

`DIRECTION/START` et `ACTION/RUN-SYSTEM` restent les autorités de classification et d’exécution ; `SAVOIR/SYSTEM` décrit le jugement technique et systémique.

Quand plusieurs consumers existent — fichier de design, web, mobile, thèmes ou documentation — évalue un format interopérable, des modes et une source de vérité. La décision précise impact, semanticité, thème, owner, consumers, migration, rollback, fallback, coût de maintenance, méthode et scope de non-régression, résultat, limite et prochaine revue.

Lorsque des tokens doivent circuler entre outils, le format du W3C Design Tokens Community Group (version stable 2025.10, couleurs OKLCH et Display P3 comprises) est un choix interopérable par défaut [VEILLE 2026-10]. La stack existante prime. Toute fondation de composants est choisie pour accessibilité, maintenance, conventions et capacité à adapter tokens et états. Une primitive accessible peut protéger les comportements sans imposer la direction visuelle.

**Identité dans la durée.** [MÉTHODE] Statut `PILOT` (`maintenance/evolution.md`). Quand une identité doit tenir sur plusieurs écrans, supports ou versions, nomme son élément signature (forme, objet du produit, couleur, voix typographique ou comportement) et ses états : où il apparaît, sous quelles formes, à quelle échelle, et ce qui ne change jamais. Pendant qu’un élément s’installe, garde sa forme constante et fais varier son usage ; une fois connu, sa forme peut jouer (Romaniuk, Ehrenberg-Bass Institute). Sa force se mesure auprès de personnes du public, élément montré sans nom ni logo : les professionnels surestiment la notoriété de leurs éléments et en sous-estiment l’unicité (Brus et al., *Journal of Brand Management*, 2025). Sans ce test, la force d’un élément reste une hypothèse ; un test de singularité fait par l’agent (`SAVOIR/FRAME`) ne la remplace pas. Revue avant 2027-04.

N’empile pas plusieurs bibliothèques concurrentes sans raison de compatibilité ou migration. Un framework ou un kit n’est jamais la direction créative du produit.

Le contrat de composant partagé est défini par `BIBLIOTHEQUE/COMPONENTS`. SAVOIR en garde le jugement : tokens primitifs et sémantiques, modes, interopérabilité et maintenance ; `ACTION/RUN-SYSTEM` conserve l’impact, les consumers, la migration, le rollback, la preuve et le verdict.

---
