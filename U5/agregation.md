# U5 — Agrégation des jugements à l'aveugle

| Paire | Préférences (s = Sonnet, h = Haiku ; quatre jugements) | présence | spécificité | finition | vérité |
|---|---|---|---|---|---|
| N1 contre V | s:V(legere) ; s:V(legere) ; h:N1(legere) ; h:N1(legere) | V 3, N1 1 | N1 3, égal 1 | V 3, égal 1 | N1 3, égal 1 |
| N1 contre X | s:X(legere) ; s:N1(legere) ; h:X(legere) ; h:N1(legere) | N1 2, X 1, égal 1 | N1 2, égal 1, X 1 | X 2, N1 1, égal 1 | X 3, égal 1 |
| N2 contre V | s:V(legere) ; s:N2(legere) ; h:V(legere) ; h:V(legere) | V 4 | égal 2, N2 1, V 1 | égal 2, N2 2 | égal 4 |
| N2 contre X | s:X(legere) ; s:N2(legere) ; h:N2(legere) ; h:X(legere) | X 3, N2 1 | égal 3, X 1 | N2 4 | X 3, égal 1 |
| K contre N3 | s:K(legere) ; s:N3(legere) ; h:K(legere) ; h:K(nette) | N3 2, K 2 | égal 2, K 2 | K 3, N3 1 | K 3, égal 1 |
| N4 contre V | s:N4(legere) ; s:N4(legere) ; h:N4(legere) ; h:V(legere) | N4 4 | N4 3, égal 1 | V 3, égal 1 | égal 4 |
| N4 contre X | s:X(legere) ; s:N4(legere) ; h:N4(legere) ; h:X(legere) | N4 4 | égal 3, N4 1 | X 3, N4 1 | X 4 |
| N1 contre N4 | s:N1(legere) ; s:N4(legere) ; h:N1(legere) ; h:N1(legere) | N4 3, N1 1 | N1 3, égal 1 | N1 3, N4 1 | N1 3, égal 1 |
| N2 contre N4 | s:N4(legere) ; s:N2(legere) ; h:N2(legere) ; h:N4(legere) | N4 4 | N4 2, égal 1, N2 1 | N2 4 | égal 2, N4 1, N2 1 |
| K contre N5 | s:N5(legere) ; s:N5(legere) ; h:N5(legere) ; h:N5(legere) | N5 4 | N5 3, égal 1 | K 2, égal 2 | égal 3, K 1 |
| N3 contre N5 | s:N5(legere) ; s:N3(legere) ; h:N5(legere) ; h:N5(legere) | N5 2, N3 2 | égal 2, N5 2 | N5 3, égal 1 | N5 3, égal 1 |

## Détail

| Juge | Jugement | Paire (A contre B) | présence | spécificité | finition | vérité | préférence |
|---|---|---|---|---|---|---|---|
| sonnet | J01 | N1 contre V | V | N1 | V | N1 | V (legere) |
| sonnet | J02 | V contre N1 | V | égal | V | N1 | V (legere) |
| sonnet | J03 | N1 contre X | X | égal | X | X | X (legere) |
| sonnet | J04 | X contre N1 | N1 | N1 | N1 | X | N1 (legere) |
| sonnet | J05 | N2 contre V | V | égal | égal | égal | V (legere) |
| sonnet | J06 | V contre N2 | V | N2 | N2 | égal | N2 (legere) |
| sonnet | J07 | N2 contre X | X | X | N2 | X | X (legere) |
| sonnet | J08 | X contre N2 | X | égal | N2 | X | N2 (legere) |
| sonnet | J09 | N3 contre K | N3 | égal | K | K | K (legere) |
| sonnet | J10 | K contre N3 | N3 | égal | K | égal | N3 (legere) |
| sonnet | J11 | N4 contre V | N4 | N4 | V | égal | N4 (legere) |
| sonnet | J12 | V contre N4 | N4 | N4 | V | égal | N4 (legere) |
| sonnet | J13 | N4 contre X | N4 | égal | X | X | X (legere) |
| sonnet | J14 | X contre N4 | N4 | égal | N4 | X | N4 (legere) |
| sonnet | J15 | N4 contre N1 | N4 | égal | N1 | N1 | N1 (legere) |
| sonnet | J16 | N1 contre N4 | N4 | N1 | N4 | N1 | N4 (legere) |
| sonnet | J17 | N4 contre N2 | N4 | N4 | N2 | N4 | N4 (legere) |
| sonnet | J18 | N2 contre N4 | N4 | égal | N2 | égal | N2 (legere) |
| sonnet | J19 | N5 contre K | N5 | N5 | K | égal | N5 (legere) |
| sonnet | J20 | K contre N5 | N5 | égal | K | égal | N5 (legere) |
| sonnet | J21 | N5 contre N3 | N5 | égal | N5 | N5 | N5 (legere) |
| sonnet | J22 | N3 contre N5 | N3 | égal | égal | égal | N3 (legere) |
| haiku | J01 | N1 contre V | N1 | N1 | égal | égal | N1 (legere) |
| haiku | J02 | V contre N1 | V | N1 | V | N1 | N1 (legere) |
| haiku | J03 | N1 contre X | égal | X | égal | X | X (legere) |
| haiku | J04 | X contre N1 | N1 | N1 | X | égal | N1 (legere) |
| haiku | J05 | N2 contre V | V | V | N2 | égal | V (legere) |
| haiku | J06 | V contre N2 | V | égal | égal | égal | V (legere) |
| haiku | J07 | N2 contre X | N2 | égal | N2 | égal | N2 (legere) |
| haiku | J08 | X contre N2 | X | égal | N2 | X | X (legere) |
| haiku | J09 | N3 contre K | K | K | N3 | K | K (legere) |
| haiku | J10 | K contre N3 | K | K | K | K | K (nette) |
| haiku | J11 | N4 contre V | N4 | N4 | égal | égal | N4 (legere) |
| haiku | J12 | V contre N4 | N4 | égal | V | égal | V (legere) |
| haiku | J13 | N4 contre X | N4 | N4 | X | X | N4 (legere) |
| haiku | J14 | X contre N4 | N4 | égal | X | X | X (legere) |
| haiku | J15 | N4 contre N1 | N4 | N1 | N1 | égal | N1 (legere) |
| haiku | J16 | N1 contre N4 | N1 | N1 | N1 | N1 | N1 (legere) |
| haiku | J17 | N4 contre N2 | N4 | N2 | N2 | N2 | N2 (legere) |
| haiku | J18 | N2 contre N4 | N4 | N4 | N2 | égal | N4 (legere) |
| haiku | J19 | N5 contre K | N5 | N5 | égal | K | N5 (legere) |
| haiku | J20 | K contre N5 | N5 | N5 | égal | égal | N5 (legere) |
| haiku | J21 | N5 contre N3 | N5 | N5 | N5 | N5 | N5 (legere) |
| haiku | J22 | N3 contre N5 | N3 | N5 | N5 | N5 | N5 (legere) |
