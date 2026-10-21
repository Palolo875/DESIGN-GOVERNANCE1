# État de référence — protocole

Version 1 · 21-10-2026 · Junior (Kamel). Document de travail, hors paquet. Il sert l'étape 4 du plan de suivi de l'outil de jugement esthétique.

## But

Savoir, avant toute réécriture, ce que le système apporte aux productions et pourquoi. Pour chaque production, on observe :
- le résultat, sur des axes séparés ;
- ce qui a été mobilisé ou manqué, grâce au journal de mobilisation.

Le résultat attendu n'est pas un score global. C'est une base pour décider quoi conserver, déplacer, renforcer, simplifier ou retirer.

**Ce que l'état de référence ne prouve pas :** une amélioration générale des pages. Avec peu de briefs et un seul évaluateur, il calibre ; il ne valide pas.

## Les six briefs

Chaque brief a un texte fixe, donné tel quel à l'agent, et une **fiche de contenu** préparée une fois puis réutilisée à l'identique : textes, chiffres et données. Aucune image n'est fournie, sauf mention contraire. Ce qui rend le brief discriminant est écrit pour l'évaluateur, jamais pour l'agent.

| N° | Brief donné à l'agent | Contenu fourni | Ce qui rend le cas discriminant | Mode attendu |
|---|---|---|---|---|
| 1 | « Le Théâtre de la Halle, salle de quartier de 180 places, veut la page de sa saison : six spectacles, un tarif unique, la billetterie reste sur un site externe. » | Six fiches de spectacle (titre, dates, durée, trois lignes de présentation), adresse, tarif, lien de billetterie | Expression et typographie ; forte pente vers la trame modale (grand titre centré, cartes égales) | DIRECTION |
| 2 | « Le service maintenance d'un parc d'ascenseurs a besoin de l'écran de suivi des interventions du jour, utilisé par trois techniciens et un chef d'équipe. » | Quarante interventions (adresse, appareil, statut, priorité, technicien, heure), quatre statuts, deux filtres demandés | Densité, hiérarchie, états (vide, erreur, retard), lisibilité en usage | STANDARD |
| 3 | « Une mutuelle veut le parcours en ligne pour modifier ou résilier son contrat santé. » | Deux formules, conditions de résiliation, délais, données d'un adhérent fictif | Protection de la personne (refuser aussi visible qu'accepter), clarté des étapes, erreurs | STANDARD |
| 4 | « Un média local publie un long article sur la rénovation du pont de la Clé ; il faut la page de l'article. » | Article de 1 200 mots, deux chiffres clés, une citation, une légende | Lecture longue, typographie éditoriale, mise en page qui sert le texte | DIRECTION |
| 5 | « La fromagerie Brunet, présente sur trois marchés, veut une page simple : où la trouver, ce qu'il y a en ce moment. » | Horaires et lieux des marchés, six produits du moment ; **aucune photo** | Moyens absents : photographie, monde du sujet, recours aux collections ouvertes ou limite déclarée | DIRECTION |
| 6 | « La commune de Saint-Aubin veut montrer à ses habitants la consommation d'eau des deux dernières années, par quartier. » | 24 mois × 3 quartiers, une moyenne départementale | Choix et honnêteté des graphiques, lecture des données, accessibilité | STANDARD |

Pour chaque brief, l'évaluateur écrit d'avance un **caractère attendu** : densité, matière, foyer, intensité, au format de la déclaration de `ACTION/RECETTE-CARACTERE`. Il sert de référence commune aux deux conditions, puisque la condition sans système ne déclare rien.

## Conditions

| Condition | Description |
|---|---|
| **A — sans le système** | Même modèle, même version, mêmes outils (navigateur, réseau, dossier de travail), même brief, même fiche de contenu ; skill non installée |
| **B — système actuel** | Identique, avec la skill en révision `R2026-10-21` et `DG_JOURNAL` activé |
| C — système modifié (plus tard) | Identique à B, avec la version issue des ajustements de l'étape 7 |

Les deux conditions ont exactement le même accès au réseau ; ce choix est noté une fois pour toutes. Chaque production démarre dans une session neuve, sans mémoire des précédentes.

**Volume.** On fait deux productions par brief et par condition, soit 24 productions pour A et B. On passe à trois productions seulement si la variance entre deux productions d'une même condition rend la comparaison illisible.

## Ce qu'on recueille pour chaque production

| Élément | Comment | Condition |
|---|---|---|
| Artefact HTML | Dossier de la production | A, B |
| Captures 390 et 1440 px | `check_render.py --captures` | A, B |
| Recette de rendu | `check_render.py --json` | A, B |
| Fidélité au caractère attendu | `check_caractere.py` avec la déclaration de l'évaluateur | A, B |
| Fidélité au caractère déclaré par le run | `check_caractere.py` avec la déclaration de l'agent | B |
| Trace du run | Fichier de trace ou en-tête du livrable | B (A : réponse de l'agent) |
| Journal et fiche de mobilisation | `DG_JOURNAL`, puis `journal_mobilisation.py` | B |
| Effort | Durée, nombre de tours, reprises ; lectures et caractères lus d'après le journal | A, B |

## Évaluation à l'aveugle

1. **Anonymiser.** Chaque production reçoit un identifiant tiré au hasard. L'évaluateur ne voit que les captures, et l'artefact ouvert dans un navigateur, sans trace ni commentaire d'en-tête.
2. **Par paires.** Pour un même brief, on compare une production A et une production B, dans un ordre tiré au hasard. La même paire est présentée une seconde fois, ordre inversé, plus tard dans la session.
3. **Par axe, séparément.** Pour chaque axe, on note « la première », « la seconde » ou « équivalentes », avec une phrase de raison.

| Axe | Question posée à l'évaluateur |
|---|---|
| Fidélité à l'intention | Laquelle rend le mieux le caractère attendu ? |
| Qualité de réalisation | Laquelle est la mieux construite : hiérarchie, typographie, espacement, états, finition ? |
| Spécificité au projet | Sans le nom et les données, laquelle pourrait le moins appartenir à cinquante autres produits ? |
| Adéquation à l'usage | Laquelle sert le mieux la tâche de la personne visée ? |

Les défauts objectivables viennent de la recette de rendu et ne demandent pas d'aveugle. La **diversité entre projets** se lit par condition, sur les six briefs : palettes, polices de titre, trames et objets de preuve qui reviennent d'un brief à l'autre, plus les six champs de `REUSE-CHALLENGE` dans les traces de B.

## Lecture de la mobilisation

Pour chaque production B, la fiche de mobilisation se complète en trois temps :

1. **Conséquences.** Pour chaque lecture ou appel, la conséquence observée dans la trace et l'artefact : choix de composition, correction visible, contrainte protégée, option écartée, limite identifiée, ou aucune.
2. **Manques.** Ce qui aurait dû être sollicité, avec sa cause : route jamais ouverte, déclencheur mal formulé, problème non reconnu, moyen absent ou en échec.
3. **Lien avec l'évaluation.** Pour chaque axe où B perd ou fait jeu égal, on cherche dans la fiche ce qui explique l'écart, en suivant le tableau « Du diagnostic à la correction » du plan.

L'explication de l'agent dans sa trace est un indice, pas une preuve : elle se confronte à l'artefact.

## Tableau de restitution

| Brief | Production | Condition (révélée après) | Fidélité | Réalisation | Spécificité | Usage | Défauts (recette) | Effort | Mobilisé utile | Manques | Cause retenue |
|---|---|---|---|---|---|---|---|---|---|---|---|

On lit ensuite :
- les axes où B gagne, perd ou fait jeu égal, brief par brief ;
- les lectures et appels associés aux gains ;
- les lectures fréquentes sans conséquence observée ;
- les manques récurrents et leurs causes ;
- la diversité de A et de B sur les six briefs.

## Rangement

Le dossier de travail reste hors paquet :

```text
etat-de-reference/
  briefs/            textes des briefs, fiches de contenu, caractères attendus
  productions/       un dossier par identifiant anonyme : artefact, captures, sorties des recettes, trace, journal
  correspondance.csv identifiant → brief, condition, numéro (fermé jusqu'à la fin de l'évaluation)
  evaluation.csv     notes par paire et par axe
  restitution.md     tableau de restitution et lecture
```

## Points à trancher avant de lancer

- **Modèle et version :** le même pour A et B, noté avec la date.
- **Réseau :** autorisé pour les deux conditions (plus réaliste, avec le risque de sources variables) ou coupé pour les deux (plus comparable). Recommandation : autorisé, et ressources consultées notées par l'évaluateur.
- **Fiches de contenu :** préparées (dossier `etat-de-reference/`) ; caractères attendus à valider.

## Journal

| Date | Événement | Détail |
| --- | --- | --- |
| 21-10-2026 | Productions arrêtées à 15 | Sur décision de Junior (coût), arrêt après le brief 4 : briefs 1 à 3 complets (2 A, 2 B), brief 4 avec 2 A et 1 B (R4B2 interrompue par la limite, abandonnée ; R4B1 reprise et terminée). Briefs 5 et 6 non produits. Dossier d'évaluation à l'aveugle : 7 paires, deux passages ; clé dans `cle-aveugle.csv`. |
| 21-10-2026 | Recette de rendu corrigée | Un défilement doux de la page (`scroll-behavior: smooth`) faisait mesurer `--in-frame` en cours de défilement (constaté par R1B2) ; une page locale suivie de paramètres était refusée. Corrigé sur la branche (fce5735). Les dix productions déjà traitées ont été re-mesurées : statuts inchangés, le traitement n'employant pas `--in-frame`. Les agents B ont travaillé avec la version d'origine. |
| 21-10-2026 | Briefs 1 et 2 produits | Huit productions traitées (deux A et deux B par brief). R2B2 laisse un dossier `_atelier/` (sources, captures, sorties de la recette) à côté de la page : le dossier d'évaluation ne reprendra que la page et ses ressources, pour que rien ne trahisse la condition. Brief 3 lancé. |
| 21-10-2026 | Productions en cours | Pilote (brief 1, A et B) : chaîne validée ; la trace en commentaire HTML est retirée de la copie évaluée et gardée à part ; les fichiers de données restent à côté de la page. R1B2, R2B1 et R2B2 interrompues par la limite de session puis reprises dans la même session, sans perte de contexte : à garder en tête à la lecture. Vagues réduites à trois productions pour ménager la limite. |
| 21-10-2026 | Fiches de contenu préparées | Six `brief.md` avec contenu fourni, `interventions.csv` (40 interventions, dont une personne bloquée en cabine), `consommation-eau.csv` (24 mois × 3 quartiers et moyenne départementale), article de 1 174 mots ; dossier `evaluateur/` avec pièges attendus et caractères attendus proposés, à valider |
| 21-10-2026 | Protocole créé | Six briefs contrastés, conditions A et B, deux productions par brief et par condition, évaluation à l'aveugle par paires sur quatre axes, fiches de mobilisation pour B |
