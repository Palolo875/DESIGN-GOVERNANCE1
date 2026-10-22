# État de référence — dossier de travail

Hors paquet. Il accompagne `../protocole-etat-de-reference.md`, qui décrit la méthode et tient le journal.

| Dossier | Contenu |
|---|---|
| `briefs/N-nom/` | Le brief donné tel quel à l'agent (`brief.md`) et ses données |
| `evaluateur/` | Ce que chaque brief met à l'épreuve, pièges attendus, caractères attendus validés (`caractere-N.json`) ; jamais donné à l'agent |
| `productions/<ID>/` | Une production par identifiant anonyme : `artefact/` (la page évaluée, commentaires HTML retirés et gardés dans `commentaires-retires.txt`), `captures/`, sorties des recettes, `reponse.md` de l'agent ; avec le système, `journal.jsonl` et `fiche-mobilisation.txt` |
| `runs/N-nom/` | Run instrumenté hors évaluation aveugle (condition C) : site, captures, réponse et trace de l'agent, journal et fiche de mobilisation, planche, et `analyse.md` (pièges, mobilisation, défauts d'outils révélés) |
| `evaluation-aveugle/` | Sept paires en deux passages, `LISEZ-MOI.md` et `evaluation.csv` à remplir |

**À ne pas ouvrir avant l'évaluation :** `productions/` révèle la condition (seules les productions avec le système ont un journal). La clé qui relie les codes de l'évaluation aux productions n'est pas dans ce dossier.

Les outils qui ont produit ce dossier sont dans `../outils/` : `traiter_production.py` (mesures et rangement anonyme) et `dossier_aveugle.py` (paires et passages).

Tout est fictif : lieux, organisations, personnes, chiffres et règles. Seuls les trois marchés du brief 5 sont des lieux réels ; la fromagerie et ses emplacements sont inventés.
