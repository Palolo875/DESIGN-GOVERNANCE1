# Projection machine-readable

Cette projection sert au transport entre agents, scripts ou handoffs. Elle ne crée pas de contrat concurrent : `ACTION.md` reste la source d’autorité. La forme courte LITE sans RUN_CARD reste une trace complète selon `ACTION/HANDOFF` et `ACTION/CLOSE-PACKAGE` ; elle est hors de cette projection. Une demande de projection structurée conserve le schéma et le validateur.

La forme de référence ci-dessous est présentée en YAML pour la lecture. Une version JSON contrôlable et son schéma sont fournis dans `gouvernance/schemas/` :

- `gouvernance/schemas/run_card.schema.json` décrit les champs et les valeurs admises ;
- `gouvernance/schemas/run_card.example.json` est une projection valide ;
- `gouvernance/schemas/fixtures/` contient des cas valides et invalides ;
- `gouvernance/outils/validate_run_card.py` exécute le contrôle structurel et les invariants sémantiques V1 sans dépendance externe.

```yaml
run_card:
  id: DIRECTION-PREMIUM-001
  owner: design-owner
  date_version: "2026-08-29 / V1"
  mode: DIRECTION
  decision: "Décision dominante à prendre ou vérifier."
  decision_intent: "Décision que le run doit permettre de trancher."
  risk:
    level: normal
    statement: "Risque principal : ce qui coûterait cher si c’était faux."
    critical_protection: null
  sources:
    - DIRECTION/START
    - ACTION/RUN_CARD
  direction:
    thesis: "Position visuelle située."
    anti_direction:
      - "Pattern générique refusé."
    first_object: "Objet qui matérialise la décision."
    identity_stake: normal
  anchors:
    - role: direction
      type: observed
      source: "URL ou référence réellement ouverte"
      date: "2026-08-29"
      scope: "axe ou décision calibré"
      retained:
        - "relation réellement extraite"
      rejected:
        - "surface ou motif copié"
      transformation: "Reformulation en choix propre au produit."
      transformation_status: transformed
      limitation: "Ne prouve ni efficacité ni droit de réemploi."
  artifact:
    locator: "chemin-ou-url-local"
    scope: "Périmètre observé."
    version: "2026-08-29 / V1"
    rights_status: not_applicable
  trace_locator: "ticket-ou-chemin-de-run"
  next_proof: "Preuve suivante attendue."
  capability_profile:
    available:
      - "navigateur/capture disponible"
    unavailable:
      - "préférence humaine non observée"
    not_required:
      - "participant non requis pour cette passe"
    basis:
      - capability: "navigateur/capture disponible"
        kind: tool_result
        detail: "Résultat d’outil qui atteste la capacité."
  proof:
    observed:
      - "Observation réellement obtenue dans le scope déclaré."
    not_verified:
      - "Propriété non observée dans le scope."
    provenance:
      artifact_locator: "chemin-ou-url-local"
      artifact_version: "2026-08-29 / V1"
      method: "Méthode d’inspection ou de test."
      observed_at: "2026-08-29"
      capability: "navigateur/capture disponible"
  decision_change:
    outcome: CHANGED
    value: "Décision effectivement changée, confirmée ou abandonnée."
    evidence: "Artefact ou observation qui l’établit."
  creative_close:
    presence: "Présence effectivement produite dans le scope inspecté."
    signature: "Élément spécifique qui distingue la proposition."
    craft_detail: "Détail ou état révélant le niveau de craft observé."
    dominant_defect: "Défaut créatif restant prioritaire."
    next_polish_action: "Prochaine action de polish ciblée."
  profile_decision:
    phase: observed
    decision: "Décision réellement modifiée par le profil."
    dials: "Dials relevés, abaissés ou inchangés."
    counterindication: "Situation où le profil devient nuisible."
    evidence: "Capture, observation ou preuve montrant son effet."
  closure:
    state: CLOSED
    direction_status: HELD
    issue: null
    verdict: ACCEPTED-WITH-RESERVATION
    limitations:
      - "Limite restante."
    axes:
      V: PASS
      U: NOT-VERIFIED
      A: NOT-VERIFIED
      T: PASS
    reservations:
      - owner: design-owner
        scope: "Périmètre de la réserve."
        date_version: "2026-08-29 / V1"
        impact: "Effet de la limite sur la livraison."
        next_proof: "Preuve qui lèvera la réserve."
        review_date: "2026-09-12"
        exit_condition: "Condition observable de sortie."
    b1b:
      status: DONE
      pair:
        before_locator: "capture-avant-edition"
        after_locator: "capture-apres-edition"
        decision: "Décision de craft comparée."
        outcome: confirmed
```

Préserver les distinctions entre `STATE`, `ISSUE`, `VERDICT`, statut de direction, `GATE`, `AXIS` et `DECISION-CHANGE`. Le `closure.verdict` global utilise uniquement les six valeurs d’ACTION. Les axes (`closure.axes`) prennent uniquement `PASS`, `PASS-WITH-RESERVATION`, `RETURN`, `NOT-VERIFIED` ou `N/A-JUSTIFIED` ; `NOT-OBSERVED` qualifie une conséquence décisionnelle (`decision_change.outcome`), jamais un axe. Aucune de ces valeurs ne devient un verdict global. `null` ne signifie ni réussite ni preuve absente ; il n’est admis que là où le schéma l’admet (`ACTION/RUN_CARD`) ; ailleurs, un champ facultatif sans valeur est omis.

`CLOSED` signifie que la trace et les artefacts sont persistés. Pour un verdict `ACCEPTED` ou `ACCEPTED-WITH-RESERVATION`, `proof.provenance` est obligatoire et doit identifier l’artefact, sa version, la méthode et la date d’observation. Pour une RUN_CARD `DIRECTION` clôturée, `creative_close` est obligatoire et doit contenir `presence`, `signature`, `craft_detail`, `dominant_defect` et `next_polish_action`. Lorsqu’une route `SAVOIR/STYLE` est activée, `profile_decision` peut transporter la phase, la décision, les dials, la contre-indication et la preuve de son effet ; s’il est présent, ses cinq champs sont obligatoires (`phase`, `decision`, `dials`, `counterindication`, `evidence`). Il peut coexister avec `RETURN`, `EXPLORATORY` ou une issue déclarée ; un axe ou une preuve peut rester `NOT-VERIFIED`. Il ne doit jamais être interprété comme un verdict positif.

Lorsqu’un risque est `critical`, `critical_protection` est un objet structuré qui identifie le contrôle, son owner, son scope, l’action en cas d’échec (`RETURNED`, `BLOCKED` ou `ESCALATED`), le locator de la preuve attendue et son `result` (`PASS`, `FAIL` ou `NOT-VERIFIED`, qui interdit `ACCEPTED`). Un `FAIL-ASSUMED` se sérialise dans `closure.exception` (`ACTION/OVERRIDE`). Un texte générique, un placeholder ou une promesse non localisable ne constitue pas une protection critique. Pour un verdict accepté, le locator de provenance doit également correspondre au locator de l’artefact déclaré ; cette cohérence ne prouve toutefois pas que l’artefact existe ou que la méthode a effectivement été exécutée.

Ne jamais introduire `SELF-DECLARED`, `ATLAS-PASS`, `POLISHED`, `SLOP-FREE` ou un score esthétique. Valider les clés avec le script fourni lorsque la projection est utilisée, mais ne jamais traiter cette projection comme une preuve ou une clôture automatique.

Une `RUN_CARD` validée atteste la forme de la projection et les invariants de la liste close ; elle n’atteste ni la réalité des observations, ni la justesse des jugements, ni la qualité perceptuelle. La liste exacte vit en un seul lieu : la frontière de validation d’`ACTION/RUN_CARD`.

