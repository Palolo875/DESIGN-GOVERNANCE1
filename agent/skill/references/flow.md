# Flux de décision V1

Le flux suivant est une vue de lecture, pas une route supplémentaire :

```mermaid
flowchart LR
  A[Classer] --> B[Protéger]
  B --> C[Cultiver et diriger]
  C --> D[Composer et construire]
  D --> E[Polir et observer]
  E --> F[Vérifier et corriger]
  F --> G[Proposer ou fermer]
  A -. risque critique .-> H[Protection de niveau]
  F -. preuve absente .-> I[NOT-VERIFIED]
  E -. défaut créatif .-> C
  H --> A
  I --> J[Owner et prochaine preuve]
```

En texte : **classer et protéger le run, cultiver et diriger la décision, composer et construire l’artefact, polir et observer le rendu, vérifier et corriger ce qui est observable, puis présenter la proposition (trace légère ; la première proposition vaut checkpoint) ou décider et fermer avec ses limites (trace complète)**. Un risque critique ramène au classement (reclassification) ; une preuve absente reste `NOT-VERIFIED`, avec owner et prochaine preuve. La boucle créative élève le résultat ; la boucle de gouvernance protège le risque, la preuve et la vérité de ce qui peut être affirmé.

Charger `DIRECTION/START` avant un build, une modification, une vérification, une action externe ou une décision persistante. Charger les routes approfondies uniquement si elles peuvent modifier une décision, un artefact, une preuve, une limite ou la prochaine action.

Pour composer plusieurs capacités selon un résultat recherché — direction, beauté située, créativité, usage, preuve, vitesse ou système — consulter, si une personne le demande, la section [« Combinaisons par résultat recherché »](../../../guides/designer.md#combinaisons-par-résultat-recherché) du guide du designer. Cette carte complète le flux sans créer de route supplémentaire.

Pour l’agent, si plusieurs propriétaires peuvent éclairer une relation ouverte, les « Connexions situées » de la carte donnent conditions, leviers, sources et limites ; `python3 scripts/read_route.py --connexions` expose le sommaire, puis un identifiant ouvre une entrée. Cette aide conserve START, CHARGE et les sources propriétaires ; elle ne demande pas à la personne de gérer les routes.
