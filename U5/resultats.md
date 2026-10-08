# U5 — Résultats

**Clé :** R = V (U3, défaut), G = X (U3, défaut), Z = K (U3, défaut), J = N1 (défaut + paris), B = N2 (défaut + paris), W = N3 (défaut + paris), H = N4 (plafond), S = N5 (plafond).

## Classement du propriétaire (à l'aveugle)

- Facturation : H (N4 plafond) > R (V) > G (X) > B (N2 paris) > J (N1 paris).
- Natation : S (N5 plafond) > Z (K) > W (N3 paris).

## Juges (Sonnet 5.5 et Haiku 5.5, deux ordres, 44 jugements, tous « légère » sauf un)

| Comparaison | Préférences |
|---|---|
| Paris contre défaut d'origine (N1, N2 contre V, X ; N3 contre K) | paris 8 / 20 |
| N4 plafond contre V, X, N1, N2 | N4 8 / 16 (3-1 contre V ; 2-2 contre X et N2 ; 1-3 contre N1) |
| N5 plafond contre K, N3 | N5 7 / 8 |

Détail par critère : `agregation.md`.

## Décisions

1. **Paris P1 et P3 : retirés.** Critère fixé avant les runs non rempli : le propriétaire place les runs sans paris devant dans les cinq comparaisons ; juges 8/20, finition 7 contre 8, présence en recul. Revert de `9f921c1` (commit `e0e830c`, validate_all vert). P4 (défilement de check_render) conservé.
2. **Plafond : meilleur pour le propriétaire dans les deux demandes**, au prix de +40 à +60 % de jetons et +40 à +85 % de temps. Les juges confirment nettement pour la natation, pas pour la facturation (ils préfèrent N1 à N4, à l'inverse du propriétaire).
3. **Diagnostic :** le problème est l'activation du savoir existant, pas le poids du système. Ce qui a changé les décisions dans les runs plafond, d'après leurs traces : atelier de direction (moment humain, exclusion, contre-choix situé), SAVOIR/TYPE (voix comparées sur le vrai titre), SAVOIR/STYLE (profil et réglages), CFT-05 (palette par rôles), et plusieurs tours d'édition sur capture (B1b). Le chemin par défaut n'ouvre aucune de ces routes.

## Limites

N petit (un run par condition et par demande) ; trois pages réutilisées de U3, reconnaissables par le propriétaire ; juges de la même famille que le producteur ; les juges récompensent le marquage « exemple » que le propriétaire trouve encombrant.
