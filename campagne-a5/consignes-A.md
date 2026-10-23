# Consignes du run — condition A (avec le système)

- Utilise le système Design Governance V1. Son paquet est `/home/user/DESIGN-GOVERNANCE1` ; sa skill est `SKILL.md` à la racine. Lis-la en entier d'abord, puis suis-la comme ta procédure : classer, charger ce que la ligne du mode et les signaux demandent (`python3 scripts/read_route.py …`), construire, observer le rendu, corriger, tenir la trace.
- Exécute toute commande du paquet depuis `/home/user/DESIGN-GOVERNANCE1`, préfixée du journal de mobilisation, par exemple :
  `cd /home/user/DESIGN-GOVERNANCE1 && DG_JOURNAL=DOSSIER_DU_RUN/journal.jsonl python3 scripts/read_route.py --mode DIRECTION`
  (même préfixe pour `check_render.py` et `check_caractere.py`).
- Ne modifie aucun fichier du paquet.
- Travaille uniquement dans ton dossier de run. Livre `index.html`, autonome (CSS et JS dans le fichier ; aucune ressource externe), et la trace que le système demande dans `trace.md`. Tes captures éventuelles vont dans ce dossier.
- Personne ne répondra à des questions : fais des hypothèses nommées et construis.
- Ne regarde aucun autre dossier de la campagne.
- Réponse finale, huit lignes au plus : chemin du livrable, mode choisi, ce qui manque pour la vraie version.
