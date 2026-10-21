# Réservé à l'évaluateur — ce que chaque brief met à l'épreuve

Ce dossier n'est jamais donné à l'agent. Les caractères attendus sont des **propositions à valider** par l'évaluateur avant le premier run ; une fois validés, ils ne changent plus pendant l'état de référence. Ils sont aussi écrits en JSON, au format de `ACTION/RECETTE-CARACTERE`, dans `caractere-N.json`.

| Brief | Ce qui le rend discriminant | Pièges attendus | Caractère attendu proposé |
|---|---|---|---|
| 1. Théâtre de la Halle | Expression et typographie pour un lieu modeste ; six spectacles très différents à hiérarchiser | Grand titre centré et six cartes égales ; esthétique « culture » générique ; billetterie qui disparaît | Typographie dominante, foyer distribué entre les spectacles, intensité marquée, compression modérée |
| 2. Suivi des interventions | Densité utile, hiérarchie par urgence, états, lecture sur téléphone avec des gants | Tableau sans hiérarchie ; urgence noyée ; couleur seule pour dire le statut ; aucun état vide ni d'erreur | Plan (aplats de statut) et typographie, compression, foyer unique sur l'urgence et le retard, retenue |
| 3. Mutuelle | Protection de la personne : résilier aussi visible et aussi court que modifier ; étapes claires ; erreurs | Résiliation cachée ou rallongée ; questionnaire présenté comme obligatoire ; culpabilisation | Typographie, respiration, foyer unique sur l'étape en cours, retenue |
| 4. Article | Lecture longue, typographie éditoriale ; photo annoncée mais absente | Mise en page de page d'accueil ; texte coupé ou réécrit ; image inventée sans le dire | Typographie, respiration, foyer unique sur le titre puis le texte, retenue |
| 5. Fromagerie | Moyens absents : aucune photo ; monde du sujet ; trois marchés à trouver vite | Photos de banque génériques ; image générée présentée comme réelle ; horaires difficiles à lire | Typographie ou matière du sujet (pas d'image fournie), compression modérée, foyer distribué entre « où » et « quoi » |
| 6. Eau de Saint-Aubin | Choix et honnêteté des graphiques ; contexte des écarts ; lecteurs peu habitués | Axe tronqué qui exagère ; quartier stigmatisé ; sécheresse présentée comme réussite ; légende absente | Plan et typographie, respiration, foyer unique sur la lecture principale, retenue |

## Ce qu'on regarde en plus, brief par brief

- **Théâtre :** la billetterie externe reste trouvable ; le tarif réduit est lisible ; les publics (« dès 8 ans ») sont visibles.
- **Interventions :** la panne avec une personne bloquée dans la cabine (INT-2611) est la première chose vue ; un technicien trouve sa prochaine intervention en un geste ; les filtres ont un état « aucune intervention ».
- **Mutuelle :** le nombre d'étapes et de clics pour résilier comparé à celui pour modifier ; le questionnaire reste facultatif ; la date d'effet est annoncée avant l'envoi.
- **Article :** le texte est complet et non réécrit ; la citation et les deux chiffres ressortent ; l'absence de photo est traitée honnêtement.
- **Fromagerie :** pas d'image présentée comme réelle ; l'avertissement sur le lait cru est présent.
- **Eau :** l'axe des ordonnées part de zéro ou l'échelle est explicitée ; la fuite, la sécheresse et les compteurs sont annotés sans jugement ; la comparaison départementale est lisible.

## Utilisation avec la recette de caractère

Retirer la clé `_statut` une fois la proposition validée. Pour un foyer `unique`, ajouter à la déclaration, production par production, le sélecteur de l'objet de preuve (`proof`), puisqu'il dépend du HTML produit. Sans lui, le foyer n'est pas relevé.
