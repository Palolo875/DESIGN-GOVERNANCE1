# Suivi des travaux

Ce fichier suit le cap du système, les constats relevés, les actions ouvertes et les décisions prises. Il n’est pas normatif : une règle fait foi dans sa section propriétaire. Il vit seul sur la branche `suivi`, séparée du paquet : ni la validation ni les distributions n’y touchent.

Mettre à jour une ligne quand son statut change ; ajouter une entrée datée sous « Décisions » quand un choix est fait.

## Cap

Retenu comme cap de travail le 2026-10-22 ; son inscription dans le README reste à faire (A7).

| Niveau | Contenu |
|---|---|
| **Utilité** | Aider une personne ou un agent à transformer une demande en réalisation de design pertinente, avec une vraie direction, construite et soignée dès la première proposition, puis améliorée à partir du rendu réel ; analyser et corriger un existant. |
| **Objectif** | Obtenir un niveau élevé plus régulièrement, avec moins d’oublis, de tâtonnements et de reprises inutiles : esthétique, identité, usage et solidité de l’exécution. |
| **Hypothèse à éprouver** | Q1 : le système oriente-t-il les choix ? Q2 : mobilise-t-il les bons moyens ? Q3 : conduit-il au niveau visé ? Chaque question se juge par comparaison avec un travail fait sans lui, sur des demandes comparables. |

Filtre pour toute évolution : quelle question sert-elle, et comment le saura-t-on ? La capitalisation des enseignements d’un run à l’autre est une direction de travail, pas une capacité acquise.

## Constats

Relevés le 2026-10-22 sur `main` au commit `c77a8bc`.

| ID | Constat | Mesure ou source |
|---|---|---|
| C1 | Le tronc DIRECTION est presque plein : 34 331 caractères sur 35 000 (98 %), marge 669. `DIRECTION/VISUAL_TARGET` en occupe 9 209. | `read_route.py --tronc DIRECTION` |
| C2 | `ACTION/GATE-A` (8 073 caractères) est lue par quatre modes sur cinq et occupe 23 % de chaque budget de tronc. | `read_route.py --tronc MODE` |
| C3 | Le sommaire annonce « 110 routes » pour 74 routes distinctes : un fichier qui héberge plusieurs responsabilités y est listé plusieurs fois. | `read_route.py --sommaire`, lignes dédoublonnées |
| C4 | 25 routes ne sont citées ni par le noyau ni par `DIRECTION/CHARGE`. La plupart le sont à dessein (catalogue des formes, atteint par `BIBLIOTHEQUE/SELECT`). À examiner : `ACTION/STRUCTURED-PROOF`, `ACTION/RECETTE-RENDU`, `SAVOIR/CONTEXT`. | Recherche des codes dans `SKILL.md` et la ligne de `CHARGE` |
| C5 | La mobilisation est presque entièrement tirée : une route n’est lue que si l’agent reconnaît son signal. Les signaux les plus importants (« motif générique », « finesse sans geste concret », « direction faible ») décrivent des défauts que l’agent voit mal en lui-même. | Tableau des signaux du noyau, section 10 |
| C6 | Le journal de mobilisation voit les lectures et les appels, pas un problème non reconnu. Il ne voit que `read_route.py` et les recettes : un fichier ouvert directement n’y apparaît pas. | `scripts/journal_mobilisation.py` |
| C7 | `check_caractere.py` nomme les routes à lire pour chaque signal ; `check_render.py` ne renvoie qu’à `ACTION/GATE-A`. | Codes de route cités dans les deux scripts |
| C8 | Onze éléments sont à l’essai, aucun adopté ni éprouvé sur un run de design complet. Revue avant 2027-04. | `maintenance/versions.md`, « Sections à l’essai » |
| C9 | Efficacité `NOT-VERIFIED` : aucune comparaison avec et sans le système. | `maintenance/versions.md` |
| C10 | Le paquet pèse environ 700 k de texte pour 660 k de code et 140 k de JSON (octets, hors images, cartes et polices). | Taille des fichiers par dossier |

## Actions

Statuts : `À FAIRE`, `EN COURS`, `FAIT`, `À DÉCIDER`, `ABANDONNÉ`.

| ID | Action | Sert | Statut | Fin quand |
|---|---|---|---|---|
| A1 | Faire pousser les routes par `check_render.py` : chaque défaut relevé nomme la route qui le traite (contraste vers `SAVOIR/CRAFT/CFT-05`, texte sur image vers `SAVOIR/CRAFT/CFT-03`, textes tronqués ou titre déséquilibré vers `SAVOIR/TYPE`). | Q2 (C5, C7) | `À FAIRE` | La sortie et le journal portent la route proposée ; tests du paquet verts. |
| A2 | Mesurer la reconnaissance des signaux : sur chaque run de la campagne, une personne note les signaux présents ; on les compare aux routes lues. | Q2 (C5, C6) | `À FAIRE` | Un taux de signaux manqués par signal, sur au moins cinq runs. |
| A3 | Rattacher certaines lectures à un moment plutôt qu’à un signal, par exemple `SAVOIR/CRAFT/CFT-00` après le premier rendu en DIRECTION. | Q1, Q3 (C5) | `À DÉCIDER` | Arbitrage avec le budget du tronc DIRECTION (C1). |
| A4 | Corriger le décompte du sommaire pour annoncer les routes distinctes. | Cohérence (C3) | `À FAIRE` | Le sommaire annonce 74 routes ; test du lecteur ajouté. |
| A5 | Campagne d’évaluation : cinq à dix briefs contrastés, runs avec et sans le système, journal activé (`DG_JOURNAL`), rendus jugés par des personnes. | Q1, Q2, Q3 (C8, C9) | `À FAIRE` | Protocole écrit, puis résultats avec point de départ, observation et limite (contrat de gain réel). |
| A6 | Redonner de la marge au tronc DIRECTION, par exemple en séparant dans `DIRECTION/VISUAL_TARGET` ce qui doit être lu à chaque run de ce qui peut l’être sur signal. | Q1 (C1) | `À DÉCIDER` | Marge rendue sans retirer de contrainte bloquante du tronc. |
| A7 | Inscrire le cap : version courte en tête du README, texte complet relié depuis le README et la fiche de version. | Cap | `À FAIRE` | README et fiche à jour ; validation verte. |
| A8 | Examiner les trois routes atteintes seulement en cascade (C4) : faut-il un signal, un renvoi plus direct, ou rien ? | Q2 (C4) | `À FAIRE` | Décision notée pour chacune. |

## Décisions

- **2026-10-22.** Création de ce fichier de suivi, sur une branche à part (`suivi`) pour ne pas entrer dans le paquet ; une copie de travail reste dans la session.
- **2026-10-22.** Le texte de mission est retenu comme cap de travail, en trois niveaux : utilité, objectif, hypothèse à éprouver (voir « Cap »).
