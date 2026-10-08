# U3 — Résultats de la mesure de référence

**Base :** `R2026-10-08-CORRECTIONS` (commit `01be58d`). Producteur Opus 5.5 ; juges Sonnet 5.5 et Haiku 5.5 (attestés par les transcriptions) ; propriétaire en dernier, à l'aveugle.

## Clé (révélée après le classement du propriétaire)

| Lettre | Run | Brief | Condition |
|---|---|---|---|
| M | R1 | B2 facturation | sans |
| V | R2 | B2 facturation | avec |
| T | R3 | B2 facturation | sans |
| X | R4 | B2 facturation | avec |
| P | R5 | B3 natation | sans |
| K | R6 | B3 natation | avec |

## Classement du propriétaire (2026-10-08)

- B2 : **V > M > X > T** (confirmé le 2026-10-08).
- B3 : **K > P**.
- Commentaires (résumés fidèlement) : M a un hero plus crédible que T, plus scannable, un meilleur contraste perçu et un bon pied de page, mais des cartes de fonctionnalités peu aimées ; T a plus de diagrammes mais il est moins lisible. X a le hero le plus travaillé, mais V est plus propre et moins encombré en défilant, avec un meilleur « trajet d'une facture » ; X est chargé de cartes et on ne sait pas où regarder sur ordinateur ; le pied de page de V est plus présent. K est clair, ordonné et va à l'essentiel, mais ses couleurs sont pâles et peu vivantes ; P est plus vivant et illustratif mais mal exécuté pour un site censé être professionnel, trop centré sur l'enfant dessiné.

## Comparaison par paires « avec » contre « sans »

| Paire | Sonnet (2 ordres) | Haiku (2 ordres) | Propriétaire |
|---|---|---|---|
| V (avec) / M (sans) | avec, avec | avec, avec | avec |
| X (avec) / M (sans) | avec, avec | avec, avec | **sans** |
| V (avec) / T (sans) | avec, avec | avec, avec | avec |
| X (avec) / T (sans) | avec, avec | avec, avec | avec |
| K (avec) / P (sans) | avec, avec | avec, avec | avec |

Juges : 20 préférences sur 20 pour « avec », cohérentes entre les deux ordres. Propriétaire : 4 paires sur 5 pour « avec ».

## Par critère (juges, 20 jugements)

| Critère | avec | sans | égal |
|---|---|---|---|
| présence | 20 | 0 | 0 |
| spécificité | 20 | 0 | 0 |
| vérité | 20 | 0 | 0 |
| finition | 2 | 12 | 6 |

## Relevés objectifs

Voir `releves.md`. En bref :
- **Recette** : trois des trois runs « sans » ont un RETURN de contraste (3,99:1 ; 4,34:1 ; bouton principal à 2,57:1), deux ont un lien sans nom candidat ; aucun run « avec » n'a de RETURN de contraste ; R6 (avec) a six champs sans nom candidat.
- **Convergence** : les deux B2 « sans » ont le même concept (facture tamponnée « PAYÉE », titre « Facturez en deux minutes. Soyez payé sans… », fond papier, titres à empattements), qui correspond au signal de `SAVOIR/TOOLS/CONVERGENCE` et à la vague 2. Les deux B2 « avec » ont deux concepts différents (tableau d'encours ; suivi d'une facture au curseur), et R4 écarte nommément la facture tamponnée.
- **Vérité** : les runs « avec » marquent les contenus d'exemple sur la page ; les runs « sans » présentent prix, conformité et hébergement comme réels (sans faux avis ni faux logos).
- **Proportion** : R7 (retouche) reste `LITE`, change une ligne CSS, charge cinq routes.
- **Coût** : « avec » ≈ 2 fois les jetons (188 000 à 195 000 contre 92 000 à 111 000) et 2 fois le temps (9,5 à 11,6 min contre 4,2 à 5,9).

## Lecture

1. **Ce que le système apporte, de façon convergente (juges et propriétaire)** : un point de vue, la spécificité au métier, la vérité des contenus d'exemple, moins de défauts objectifs (contraste), et des concepts différents d'un run à l'autre au lieu du concept modal.
2. **Ce qu'il coûte ou affaiblit** : la finition et la lisibilité. Les juges donnent la finition à « sans » (12 contre 2). Le propriétaire le dit aussi : X est encombré, on ne sait pas où regarder ; K est pâle, peu vivant. Défauts récurrents des runs « avec » relevés par les juges : densité, petit texte gris, mentions « exemple » répétées qui alourdissent, hero sans image (natation), journal coupé dans sa carte (X).
3. **Le désaccord X / M** porte précisément sur ce point : le propriétaire préfère la page plus scannable et lisible, même générique.

## Limites

- N = 1 ou 2 par cellule : la mesure décrit, elle ne prouve pas.
- L'aveugle est imparfait : les mentions « exemple » visibles distinguent les pages « avec ». Le critère « vérité » les favorise par construction.
- Juges de la même famille que le producteur (biais possible d'auto-préférence).
- Classement B2 du propriétaire à confirmer (« V, M, V, XT »).
- Incident de capture corrigé (R5, contenu révélé au défilement ; voir `releves.md`).
