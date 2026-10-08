# U4 — Paris (2026-10-08)

Classement du propriétaire en U3 confirmé : B2 **V > M > X > T** ; B3 **K > P**. Choix des paris délégué par le propriétaire.

## Diagnostic qui fonde les paris (mesures sur les pages U3, `U3/outils/densite.py`)

| Page | Mentions « exemple » | Mots < 14 px | Mots par écran |
|---|---|---|---|
| M (sans) | 0 | 13 % | 139 |
| T (sans) | 1 | 21 % | 157 |
| V (avec) | 15 | 23 % | 161 |
| X (avec) | 16 | 19 % | 218 |
| P (sans) | 0 | 7 % | 169 |
| K (avec) | 14 | 2 % | 178 |

## Paris retenus

| Pari | Cause visée | Changement | Commit |
|---|---|---|---|
| P1 Marquage proportionné | Sur-marquage (≈ 15 mentions par page) | Mention globale discrète, plus mentions locales seulement là où le visiteur pourrait agir sur une valeur fausse ; marquage TRUTH précisé comme interne | `9f921c1` |
| P3 Premier regard | Finition perdue 12/20 ; « je ne sais pas où regarder » (X) | Sur la première capture, nommer ce que l'œil lit en premier puis en second ; retirer ou regrouper si deux foyers se disputent le regard | `9f921c1` |
| P4 Défilement avant capture (correction d'outil) | Incident R5 | `check_render` fait défiler la page avant de mesurer et de capturer ; test B27 | `83b995f` |

**Reporté :** P2 (registre et chaleur sans photo). Une seule page à l'appui (K), avec des signaux contraires (P jugé trop « enfant dessiné »).

## U5 — protocole proposé (frugal)

- Base : `9f921c1`. Même consigne que U3, même producteur (Opus 5.5).
- Runs : B2 avec ×2 (N1, N2), B3 avec ×1 (N3). Pas de nouvelle condition « sans » : celles de U3 servent de référence.
- Relevés : mentions « exemple », densité, recette ; routes ouvertes ; usage effectif de P3 dans la trace.
- Juges (Sonnet 5.5, Haiku 5.5), à l'aveugle, deux ordres : nouveau contre ancien « avec » (N1 et N2 contre V et X ; N3 contre K), soit 5 paires × 2 ordres × 2 juges = 20 jugements.
- Propriétaire en dernier : planche anonyme mêlant anciens et nouveaux « avec ».
- Critère de décision : P1 et P3 sont gardés si la finition et la lisibilité progressent sans perte de présence, de spécificité ni de vérité ; sinon retirés (git revert de `9f921c1`).
