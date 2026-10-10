# Correctifs de présentation V1 — 11 octobre 2026

Les remarques ont été confrontées à `main` (`4e1f9cc`) et à PR 2 (`213cfba`). La police entière et les liens GitHub vers du code HTML étaient des défauts confirmés. L’alias sans accent était refusé. Deux titres du noyau étaient devenus trop larges après son allègement. Le journal court ne permettait pas de retracer les révisions dans le paquet seul.

## Changements et preuves

- Police WOFF2 réduite aux 69 caractères utilisés : 10 980 octets, graisses 200–800 conservées. Source, licence, versions et couverture livrées ; deux reconstructions identiques vérifiées. `poids-apres.json` donne les neuf poids : environ 29 ko par SVG, 69–71 ko par HTML, réduction cumulée de 86,5 %.
- `contours-police.json` : 690 comparaisons de contours et avances, aux dix graisses examinées, sont identiques à la police d’origine. Les captures ne sont pas identiques pixel par pixel ; `comparaison-pixels.json` conserve leurs différences ponctuelles. Les trois exemples quantifiés affectent 0,010 %, 0,011 % et 0,022 % des pixels. Aucune compréhension utilisateur ou conformité exhaustive n’en est déduite.
- Le README et les deux autres présentations ouvrent les textes Markdown. Le catalogue explique les liens HTML locaux. Le moteur Markdown de GitHub conserve le `picture` ; `picture.json` vérifie ses six sélections de thème dans Chromium. GitHub Pages n’est pas nécessaire pour lire le paquet.
- `SYSTEME` sert exactement la même ligne canonique et les mêmes conditions que `SYSTÈME` : 85 tests du lecteur réussis. Les titres du noyau sont précisés dans le registre puis compilés ; les consignes sont identiques après retrait des lignes de titre. Skill actuelle : 18 971 octets ; 18 960 correspond à PRATIQUE et 18 852 à PHASE5, mesure historique légitime.
- Une ligne par révision revient dans le journal. Le budget, l’autorité et le contrat de maintenance sont conservés. Les 27 locators des neuf connexions sont réexaminés, couvrant 43 contributions ; le journal changé est relu.
- `preuves/verification.json` : 76 contrôles des trois cartes réussis. `mutations-police.json` : couverture périmée, police altérée et police complète refusées avec le diagnostic attendu.

## Lecture de l’agent : ce qui est réellement établi

`lecture-u6.json` relit les six journaux d’U6. Dans les trois productions de `6e5a8c2`, la ligne DIRECTION ainsi que composition, singularité, typographie, gestes et atelier ont été servis. Tous les événements DG enregistrés précèdent le premier HTML. Les clés prouvent le texte servi par le lecteur instrumenté, pas nécessairement la syntaxe exacte d’une commande shell ni le moment d’une décision de design.

U6 comparait `99caa027` à `6e5a8c2`, sur deux briefs et six productions. Les lectures anticipées ne démontrent pas l’amélioration de `3b79b3a`, ni un comportement robuste chez un agent pressé ou installé sans le paquet. La skill dit explicitement que le repli sans sources ne constitue pas un run conforme. Une comparaison ciblée actuelle reste distincte de ces observations : aucun nouvel essai indépendant n’est attribué à cette relecture. Concurrents et anglais restent reportés.

Les originaux des fichiers modifiés sont dans `avant/`. Le lot de présentation précédent et ses captures complètes restent dans `SUPPORTS-V1/lot-02/` sur `refonte`. Les preuves de distributions et de CI sont enregistrées après leur exécution, avec le SHA précis. La PR reste révisable et aucune fusion n’est effectuée par ces correctifs.

## Résultat local final

La validation complète avec navigateur passe, y compris les deux constructions et leur reproductibilité. Les 42 captures comparées gardent les mêmes dimensions ; les différences affectent au plus 0,025 % des pixels dans cet échantillon (`differences-pixels.json`). Les archives et le paquet Local exact sont conservés ici.
