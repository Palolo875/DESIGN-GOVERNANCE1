# Mesures U6

Six productions distinctes ; chiffres descriptifs, sans significativité ni effet général établi.

| Page | Version | Brief | Minutes observées | Caractères servis | Union par clé | Parcours du coordinateur |
|---|---|---|---:|---:|---:|---|
| F | ancien | B2, répétition 1 | 16,8 | 198 085 | 192 085 | 24 PASS, 0 FAIL |
| A | nouveau | B2, répétition 1 | 15,5 | 193 209 | 193 209 | 27 PASS, 3 FAIL |
| C | nouveau | B2, répétition 2 | 18,8 | 205 094 | 205 094 | 27 PASS, 0 FAIL |
| E | ancien | B2, répétition 2 | 18,7 | 219 803 | 205 020 | 27 PASS, 0 FAIL |
| D | nouveau | B4, répétition 1 | 145,1 (interruption ; non comparable) | 187 860 | 187 860 | 30 PASS, 0 FAIL |
| B | ancien | B4, répétition 1 | 16,7 | 187 225 | 184 673 | 39 PASS, 0 FAIL |

Le nombre de contrôles dépend du parcours implémenté ; il n'est pas une note comparative de qualité. Les échecs bruts restent comptés même si une copie est corrigée ensuite.

| Paire avant → après | Variation du temps | Variation de l'union de caractères | Variation des caractères servis avec répétitions |
|---|---:|---:|---:|
| F → A | -7,4 % | +0,6 % | -2,5 % |
| E → C | +0,1 % | +0,0 % | -6,7 % |
| B → D | non comparable (interruption) | +1,7 % | +0,3 % |

Les caractères décrivent les textes servis par le lecteur DG, en-têtes inclus. L'union est calculée par clé de requête : elle ne supprime pas les recouvrements sémantiques entre des routes différentes. Les lectures techniques directes et les autres instructions ne sont pas comptées. Aucun compteur de jetons API n'est disponible.

Le repère avant premier HTML utilise l'existence de `index.html` ; il ne date pas toute la préparation ou le début effectif de la production. Les cibles initiales de lecture restent non validées par cette mesure. La durée part du dernier marqueur valide du coordinateur et termine à réception de la livraison, outils et attente de service compris, contrôles du coordinateur exclus.

Le défaut observé sur une page n'établit pas une disparition de règle ou une régression causée par la refonte. La validation stricte de RUN_CARD vérifie sa structure ; les parcours doivent être exécutés séparément.
