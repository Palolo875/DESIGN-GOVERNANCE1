# Folio : essai pratique Web mobile

Ouvrir `index.html` avec un serveur local. Le fichier embarque ses fontes et licences ; il ne fait aucune requête externe. Il s’agit d’un brouillon illustratif, sans compte, envoi ni conformité comptable.

```sh
python3 -m http.server 8080 --bind 127.0.0.1
```

Puis consulter http://127.0.0.1:8080/index.html. Le navigateur cloud fourni bloque `file://` ; les mesures utilisent HTTP local.

## Sources et reproduction

`index.template.html` est la source ; `construire.py` reconstruit `index.html` depuis `fonts/`. Python 3 suffit à cette reconstruction. L’empreinte doit rester celle des preuves si les entrées ne changent pas.

Les trois scripts de mesure utilisent Playwright 1.56.0 et Chromium `/usr/bin/chromium` (151.0.7922.173 lors de la mesure). Ils ouvrent et arrêtent leur serveur local, puis réécrivent les preuves correspondantes : conserver les résultats historiques avant une nouvelle exécution.

```sh
python3 -m pip install -r requirements.txt
python3 construire.py
python3 verifier.py
python3 comparer.py
python3 qualite.py
```

Le verdict de comparaison est rédigé après inspection des images, dans `trace.md` et le rapport joint ; `comparer.py` ne prétend pas produire ce jugement. Le premier passage échoué est conservé dans `preuves-premier-essai/`. Les réserves de Gate A restent dans ses deux JSON. `run-card.json` est une projection de clôture exploratoire, pas une acceptation.

Voir [la trace](trace.md), [les parcours](preuves/parcours.json), [la paire comparée](preuves/comparaison/comparaison.json) et [les mesures complémentaires](preuves/complement-qualite.json). Les noms, le montant et le taux de TVA sont des exemples.
