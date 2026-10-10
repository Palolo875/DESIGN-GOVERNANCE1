# Gouvernance — adaptée au travail, utile selon le besoin

Ce module aide à vérifier une affirmation, protéger un risque, permettre une reprise ou préparer une acceptation. Ses contrôles et sa trace s’adaptent au contexte ; ils ne sont pas un formulaire à remplir systématiquement. L’agent réutilise les éléments déjà présents et n’ajoute que ceux qui servent la décision.

| Situation | Gouvernance utile |
|---|---|
| Proposition exploratoire | Trace légère, limites visibles et vérifications applicables ; pas de RUN_CARD ni d’acceptation implicite. |
| Correction locale | Preuve ciblée sur le changement et ses effets ; la forme courte LITE suffit si ses conditions sont remplies. |
| Travail persistant, partagé, audité ou soumis à acceptation | Trace complète, preuves et clôture adaptées ; RUN_CARD selon `ACTION/HANDOFF` et `ACTION/CLOSE-PACKAGE`. |
| Risque critique ou affirmation non vérifiée | Protection et preuve adaptées au risque ; capacité absente déclarée, jamais remplacée par une formalité ou une validation documentaire. |

Le niveau de trace suit [la règle propriétaire](../agent/repondre.md). Alléger la formalité ne supprime aucune preuve applicable. Montrer une proposition ne vaut pas accepter un produit.

Les sections de ce module viennent d’`ACTION.md`, de `DIRECTION.md` et de `BIBLIOTHEQUE.md` ; leurs anciennes adresses restent valables.

| Fichier | Contenu |
|---|---|
| [`principes.md`](principes.md) | Relation ou contrat, registres à ne pas mélanger, portée d’action |
| [`statuts.md`](statuts.md) | États, issues et verdicts d’un travail |
| [`travail.md`](travail.md) | Conditions de départ, fiche de travail |
| [`verification.md`](verification.md) | Contrats de décision, vérification en contexte, dérogation |
| [`cloture.md`](cloture.md) | Dossier de clôture, test de sortie, clôture de direction |
| [`structure.md`](structure.md) | Contrats de structure et test de sortie des formes |
| [`schemas/`](schemas/run_card.schema.json) | Schémas de la fiche de travail et des contrats, exemples et fichiers de test |
| `outils/` | `validate_run_card.py` (fiches) et `validate_contracts.py` (contrats) : `python3 gouvernance/outils/validate_run_card.py chemin/vers/fiche.json` |
