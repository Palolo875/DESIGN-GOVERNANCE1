# Brief 2 — Suivi des interventions

## Demande

Le service maintenance d'un parc d'ascenseurs a besoin de l'écran de suivi des interventions du jour, utilisé par trois techniciens et un chef d'équipe.

Livrable : l'écran en HTML (un fichier, données intégrées ou lues depuis `interventions.csv`), avec ses états utiles.

## Contenu fourni

Les données sont fictives. Elles sont à utiliser telles quelles.

### Le service

- **Entreprise :** Ascenseurs Rhône Maintenance (fictive), agence de Lyon Sud
- **Chef d'équipe :** Nathalie Roux
- **Techniciens :** Karim Benali, Sophie Lambert, Théo Girard
- **Jour affiché :** mardi 20 octobre 2026 ; l'écran est consulté à **10 h 30**
- **Usage :** le chef d'équipe sur un écran de bureau ; les techniciens sur leur téléphone, entre deux interventions, souvent avec des gants ou en mouvement

### Les interventions

Le fichier `interventions.csv` contient les quarante interventions du jour, une par ligne :

| Colonne | Contenu |
|---|---|
| `id` | Identifiant de l'intervention |
| `heure_prevue` | Heure prévue d'arrivée sur place |
| `adresse` | Adresse du bâtiment |
| `batiment` | Type de bâtiment |
| `appareil` | Identifiant de l'ascenseur |
| `type` | Panne, Entretien périodique, Contrôle réglementaire, Réparation planifiée |
| `priorite` | Haute, Normale, Basse |
| `statut` | À faire, En cours, Terminée, En retard |
| `technicien` | Technicien affecté |
| `note` | Précision éventuelle |

### Ce que le service demande

- **Deux filtres :** par technicien et par statut.
- Le chef d'équipe doit voir d'un coup d'œil ce qui est en retard et ce qui est urgent.
- Chaque technicien doit retrouver vite **sa prochaine intervention** et son adresse.
- Prévoir l'affichage quand un filtre ne donne **aucune intervention**, et quand les données **ne se chargent pas**.
