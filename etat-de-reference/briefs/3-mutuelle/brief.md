# Brief 3 — Mutuelle des Trois Rivières

## Demande

Une mutuelle veut le parcours en ligne pour modifier ou résilier son contrat santé.

Livrable : les écrans du parcours, en HTML (un ou plusieurs fichiers), avec leurs états (étape en cours, erreur de saisie, confirmation).

## Contenu fourni

Les informations ci-dessous sont fictives, règles comprises : elles valent pour ce test seulement. Elles sont à utiliser telles quelles.

### La mutuelle

- **Nom :** Mutuelle des Trois Rivières (fictive)
- **Espace adhérent :** l'adhérent est déjà connecté quand le parcours commence.
- **Service adhérents :** 09 00 00 00 00, du lundi au vendredi, de 9 h à 18 h · contact@trois-rivieres.example

### L'adhérent connecté (fictif)

- **Nom :** Camille Moreau
- **Numéro d'adhérent :** TR-204-58817
- **Formule actuelle :** Confort, depuis le 1er mars 2024
- **Bénéficiaires couverts :** Camille Moreau, et Léo Moreau (enfant, né en 2015)
- **Prélèvement :** le 5 de chaque mois, sur le compte se terminant par 4412

### Les deux formules

| | Essentielle | Confort |
|---|---|---|
| Cotisation mensuelle (un adulte) | 38,40 € | 61,90 € |
| Cotisation mensuelle (par enfant) | 12,10 € | 19,80 € |
| Consultation chez un généraliste | 100 % de la base de remboursement | 150 % |
| Hospitalisation, chambre particulière | non couverte | 60 € par jour, 30 jours par an |
| Optique (par an) | 100 € | 250 € |
| Dentaire, prothèses | 125 % de la base | 250 % de la base |
| Médecines douces | non couvertes | 4 séances par an, 30 € chacune |

### Règles de modification

- Le changement de formule prend effet le **1er du mois suivant** la demande.
- Un passage de Confort à Essentielle ne peut se faire qu'**une fois par année civile**.
- La cotisation du mois en cours reste due au tarif actuel.

### Règles de résiliation

- L'adhérent peut résilier **à tout moment après un an d'adhésion**. Camille Moreau remplit cette condition.
- La résiliation prend effet **un mois après** la réception de la demande.
- Aucun frais ni pénalité.
- La mutuelle doit proposer de **confirmer ou d'annuler** la résiliation avant l'envoi définitif. Un justificatif de nouvelle couverture n'est **pas** exigé.
- Après l'envoi, l'adhérent reçoit un **accusé de réception** par courriel avec la date d'effet.

### Ce que la mutuelle souhaite aussi

- Proposer, sans l'imposer, un court questionnaire facultatif sur la raison du départ (prix, garanties, déménagement, autre).
- Rappeler qu'un changement de formule existe, sans bloquer la résiliation.
