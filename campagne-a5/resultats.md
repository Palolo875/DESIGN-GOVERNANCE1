# Campagne A5 — résultats (2026-10-23)

Protocole : `PROTOCOLE-A5.md`. Huit briefs, un run par condition (A avec le système, B sans), agents Sonnet 5.5 en effort moyen. Jugement à l'aveugle (X/Y tirés au sort ; clé levée après les deux jugements).

## Jugements (préférence d'ensemble, ramenée à la condition)

| Brief | Juge agent (Sonnet 5.5, effort élevé) | Personne qui pilote |
|---|---|---|
| 1 Boulangerie | A | non noté |
| 2 Prise de rendez-vous kiné | A | A |
| 3 Pilotage d'incidents | A | B |
| 4 Fiche produit Brume | A | B (préférence visuelle) |
| 5 Article long | A (écart faible) | B (préférence visuelle) |
| 6 Festival | A | non noté |
| 7 Retouche « plus chaleureux » | A | non noté |
| 8 Bouton de système de design | A | non noté |

Juge agent, par question : A préféré sur 6 à 8 briefs selon la question, jamais B (égalités sur le bouton surtout).

## Règle de décision fixée avant les runs

Un gain s'affirme si A est préféré sur au moins six paires sur huit par chacun des juges, sans dégradation des mesures objectives.
- Juge agent : 8/8 pour A ; mesures objectives sans dégradation. Condition remplie pour ce juge.
- Personne : 4 briefs notés, A sur 1, B sur 3. Condition non remplie.
- **Conclusion : aucun gain affirmé.** Les deux juges divergent ; c'est le résultat principal.

## Mesures objectives

| | A (avec) | B (sans) |
|---|---|---|
| Jetons par run | 140 000 à 162 000 (moyenne ≈ 153 000) | 87 000 à 98 000 (moyenne ≈ 92 000) |
| Durée par run | 2,7 à 5,9 min | 0,6 à 2,2 min |
| Appels d'outils | 16 à 22 | 4 à 7 |
| RETURN de `check_render.py` (rendu final) | 1 (article ; faux positif possible signalé par l'agent) | 2 (fiche produit : chevauchement ; bouton : mouvement réduit) |
| Réserves | 1 à 3 | 1 à 4 |

Coût du jugement agent : ≈ 172 000 jetons.

## Mobilisation (journal, runs A)

- Tronc du mode lu dans tous les runs (DIRECTION, STANDARD, ITER, SYSTÈME, avec `SAVOIR/SYSTEM` en SYSTÈME : A19 effectif).
- Routes ajoutées pendant les corrections, lues quand leur signal était là : inventaire du sujet `CFT-01` (1-A, 4-A, A17), écriture `CFT-06` (1-A à 6-A), `SAVOIR/TYPE-VOIX` (5-A, 6-A, A14), brief vague `EXTERNAL-START` (1-A, 4-A à 6-A).
- Routes proposées par la recette sous chaque réserve visibles dans le journal (A1).
- Classement : le pilotage d'incidents a été classé `STANDARD` (attendu `DIRECTION` dans le protocole) ; défendable, à discuter.

## Lecture

- La divergence des juges peut venir d'un biais du juge agent : il est de la même famille que les agents producteurs et récompense peut-être les pages plus riches en fonctions, en explications et en marquage « exemple » que produit la condition A. La personne qui pilote préfère B sur le visuel de l'article et de la fiche produit, et sur le pilotage d'incidents.
- Le tirage X/Y a mis A en Y sur 7 briefs sur 8. Le juge agent a pourtant choisi X quand X était A (brief 3) : un biais de position pur n'explique pas ses choix, mais le tirage déséquilibré reste une limite.
- Limites déclarées : un run par condition (variance non mesurée), un seul juge humain, non indépendant, et partiel (4 briefs) ; juge agent de la même famille ; petits effectifs.

## Suites proposées

- Faire juger les quatre briefs restants par la personne, et si possible par un second humain, avant toute conclusion sur Q1 et Q3.
- Q2 (mobilisation) : le journal montre que les routes attendues sont lues ; A2 (signaux manqués) reste à mesurer par une personne.
- Coût : la condition A coûte ≈ 1,7 fois plus de jetons et 3 à 4 fois plus de temps ; le gain qui le justifierait n'est pas établi.
- Examiner le faux positif de chevauchement signalé en 5-A (recette de rendu, sommaire replié).
