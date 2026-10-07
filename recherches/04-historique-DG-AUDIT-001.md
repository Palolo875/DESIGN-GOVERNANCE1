## Rapport : lecture de l'archive V1.1.1 et de l'audit DG-AUDIT-001

Racine : `/tmp/claude-0/-home-user-DESIGN-GOVERNANCE1/d50555cc-e888-5d84-bb8b-64d228442ef5/scratchpad/historique/kit/` (notée `kit/`). J'ai seulement lu les fichiers ; aucun script de l'archive n'a été exécuté. Pour compter les lignes du CSV, j'ai utilisé mes propres scripts, placés dans `scratchpad/tools/`. **F** signale un fait relevé dans un fichier. **I** signale mon interprétation. **⚑** signale une alerte sur la convergence, le slop ou le poids de la gouvernance sur la création.

---

### 1. Méthode d'audit : plan maître et protocole v2

**F — Ossature**
- Le protocole (`kit/audit/sources/Protocole_maitre_audit_Design_Governance_v2.md`) compte 15 phases, de 0 à 14 (§10 à §24) :
  - préparer ;
  - baseline ;
  - lecture complète en quatre passages A–D (§12) ;
  - rôles (neuf rôles, §13) ;
  - contrats (sept contrats, §14) ;
  - architecture de l'information (§15) ;
  - capacité positive (§16) ;
  - boucles (§17) ;
  - multi-perspectives (douze perspectives, §18) ;
  - tests de résistance (vingt scénarios, §19) ;
  - classer (§20) ;
  - décider (§21) ;
  - corriger (§22) ;
  - valider en cinq couches (§23) ;
  - clôturer (§24).
- D'autres éléments structurent la méthode :
  - deux familles de conclusions séparées, contrat et efficacité (§3.1 et §3.2) ;
  - cinq niveaux de profondeur (§4) ;
  - cinq échelles : intra-fichier, interface, chaîne, système, release (§6) ;
  - une protection contre la bureaucratisation (§32).
- Le plan maître (`kit/audit/reports/Plan_Maitre_Audit_Design_Governance-1.md`) applique ce protocole au profil `DEEP` sur la baseline B01 (« Baseline active »), et reprend les phases dans « Les quinze phases du protocole ».

**F — Couverture de vos quatre axes**

**(a) Organisation et lecture : couvert explicitement.**
- §15 « Phase 5 — Auditer l'architecture de l'information » prévoit six sous-axes :
  - Façade ;
  - Hiérarchie ;
  - Chargement conditionnel ;
  - Navigation ;
  - Charge cognitive (« nombre de taxonomies ; termes à retenir ; décisions simultanées ; répétitions ; … profondeur de navigation ; nombre de concepts nécessaires avant la première action ») ;
  - Façade contre source.
- §6.1 demande si le fichier « contient-il des répétitions utiles ou accidentelles ? ses chemins courts fonctionnent-ils ? ».
- §7.7 s'intitule « La duplication doit avoir une fonction ».
- §12, Passages A et C, couvre la hiérarchie et l'usage simulé.
- §23 « 13.1 Validation textuelle » vérifie notamment les termes.
- Dans le plan, « Phase 5 » ajoute la matrice de nécessité des 60 sources.

**(b) Capacités et ressources : couvert de façon partielle.**
- La qualité esthétique est couverte :
  - §16 « Phase 6 », avec dix dimensions : Présence, Point de vue, Spécificité, Composition, Matière et type, Désirabilité située, Résolution, Retenue, Habitabilité, Transfert ;
  - §18, perspective 1 « Création visuelle ».
- La disponibilité apparaît de trois façons :
  - §14 « Escalade » (« une capacité n'est pas disponible ? ») ;
  - scénarios §19 « Asset absent » et « Runtime différent » ;
  - « Transfert » pour l'adaptation.
- La mobilisation effective n'existe que comme signal de run :
  - §28 « Micro-runs » : « nombre de modules réellement chargés » ;
  - §29 : « modules systématiquement contournés », « qualité perçue par plusieurs reviewers », « différence avec une baseline sans le protocole ».
- **I :** la mobilisation effective est prévue, mais seulement après la stabilisation. Le plan, dans « Après la stabilisation documentaire », la renvoie à un « audit d'efficacité séparé ». L'efficacité a été classée ESCALATED (« Tableau de bord »).
- **I :** aucune rubrique ne porte sur les ressources au sens de skills, outils ou assets disponibles pour l'agent. Elles n'apparaissent qu'à travers « Matière et type » et « capacité ».

**(c) Fiabilité : couvert largement.**
- Protections :
  - §7.4 « Positif et défensif restent liés » ;
  - rôle « Garde-fou » au §13.
- Contrats : §14.
- Preuves :
  - §3.2 ;
  - §7.5 « Une justification n'est pas une preuve ».
- Clôtures : §24 et §31.
- Handoffs :
  - §6.2 (« une décision change-t-elle de sens pendant le handoff ? ») ;
  - §18, perspective 7 ;
  - §26, Niveau C « handoff agentique ».
- Restauration : couverte seulement de façon indirecte :
  - « rollback » dans la perspective 10 (§18) ;
  - patch « réversible » (§22) ;
  - scénario « État critique… récupération » (§19).
- **I :** la restauration d'un état antérieur du système n'est pas un axe en soi. La section « Architecture anti-perte de contexte » du plan concerne la reprise de l'audit, pas celle du système audité.

**(d) Relations entre fichiers : couvert explicitement.**
- §6.2 « Audit d'interface » (DIRECTION → ACTION, schéma → validateur, source → distribution).
- §6.5 « Audit de release ou distribution ».
- §26, Niveau B « Interfaces ».
- Phase 0 : champs « CONSUMERS / DEPENDENCIES » (§10).
- §23 : « 13.3 Validation machine » (« build ; compilation ») et « 13.4 Validation de distribution ».
- §5 : les guides apparaissent dans le profil STANDARD (« guide consommé par plusieurs acteurs »).
- Dans le plan, la « Phase 2 » a lu les distributions GitHub et Local (60/60 et 56/56), et la « Phase 4 » couvre l'unité 4.09 (sources/façades → manifeste → distributions).

---

### 2. Familles de constats, répartition création / gouvernance, rejets et reports

**F — Registre de référence**
- Fichier : `kit/audit/data/DG_AUDIT_001_Phase10_05_REGISTRE_CONSOLIDE_158.csv`.
- 158 fiches : 14 Majeures, 87 Significatives, 48 Mineures, 9 Observations, 0 Bloquante (recalculé, conforme à 10.05 §2).
- Échelles : 82 Interface, 24 Outil, 9 Distribution, 12 Système.

**F — Pré-tri en familles**
- Source : `Audit_Phase10_00_PRETRI_Familles_Causes_Lots.md` §2, sur 157 fiches, dont 53 non triables (famille « Z »).

| Famille | Contenu | Fiches | Gravité |
|---|---|---|---|
| A | Oracles PASS sans validation | 18 | Majeur |
| D | Façade qui affaiblit le propriétaire | 11 | Majeur |
| C | Accès CLI | 4 | |
| I | CI | 1 | |
| E | RUN_CARD vérifie la forme et non la réalité | 28 | |
| F | Rejet à tort ou exemple incohérent | 6 | |
| B | Erreurs brutes | 8 | |
| H | Ordre interne | 7 | |
| J | Éditorial | 5 | |
| **G** | **« Frontières normatives liées à la capacité créative »** | **16** | **reportée « Après 6.02 »** |

- La consolidation (`Audit_Phase10_05_CONSOLIDATION_Registre_Arbitrages.md` §5) remplace ces familles par 20 grappes et 2 lots.
- Constat principal (10.05 §2) : 12 des 14 Majeurs ont la même forme, « la prose protège, mais la projection machine accepte ce que la prose interdit ».

**F — Comptage création / gouvernance (colonne PERSPECTIVE)**

| Perspective | Perspective principale | Toutes mentions |
|---|---|---|
| « 1 Création » | 18 | 21 |
| 9 Gouvernance | 41 | 50 |
| 6 Preuve | 37 | 51 |
| 7 Agentique | 18 | |
| 10 Production | 12 | |

- Les 21 fiches « Création » se répartissent en 1 Majeure (F-DIR-027, ancres), 14 Significatives, 3 Mineures et 3 Observations.

**I — Ce qui touche vraiment la qualité créative**
- Parmi ces 21, plusieurs sont en fait formelles : F-DIR-023, F-DIR-020, F-RC-001, F-ACT-036, F-DIR-027.
- Environ 12 à 15 fiches touchent le résultat créatif :
  - F-SAV-002, F-SAV-006, F-BIB-005 (grappe C7 « Homogénéisation et ablation ») ;
  - F-PC-001 ;
  - F-DIR-009 ;
  - F-OM-002 ;
  - F-SAV-008 ;
  - F-DIR-012 ;
  - F-DIR-025 ;
  - F-ACT-025 (quota d'action ou de polish) ;
  - F-QS-002 (craft → DIRECTION) ;
  - F-ACT-006 (« slop procédural »).
- **Les 140 et quelques autres fiches portent sur la cohérence formelle, la machine, les façades et la distribution.**
- **⚑ :** l'audit a surtout mesuré la cohérence entre textes et projection machine. La qualité esthétique ne représente qu'environ 10 % du registre.

**F — Rejets et reports**
- Aucune fiche n'a été rejetée. Les 149 fiches des lots A à E ont toutes été « CORRIGER » (`Audit_Phase11_23_CLOTURE_Phase11_Conformite.md` §2.1).
- Les 9 observations (lot F, colonne DECISION « OBSERVATION — pas de patch ; test futur ») sont restées sans correctif. Quatre concernent la création ou la portée :
  - F-OM-002 (« un axe à la fois ») ;
  - F-SAV-008 (motion narrative exclue) ;
  - F-DIR-004 (portée web ↔ print, spatial, vidéo) ;
  - F-DIR-044 (catégories de lecture non exclusives, « à reprendre avec les pilotes »).
- 11.23 §3.3 ajoute deux observations, OBS-F-1 (`maxItems = 3` des directions, « sans source ») et OBS-F-2.
- Écarts de gravité (10.05 §3) :
  - 33 fiches abaissées et 3 relevées ;
  - 4 fiches passées en Observation, donc sans obligation de patch (F-DIR-022, F-DIR-044, F-ACT-035, F-SAV-008) ;
  - l'auditeur admet un « biais possible : l'auditeur seul peut pencher vers l'indulgence ».
- **⚑ (10.05 §3) :** « F-SAV-002 passerait Majeur si la convergence "neutres + accent" était confirmée N ≥ 3 fois par un observateur indépendant. »
- Écart mineur : 10.05 §5 annonce A1 = 4, A2 = 3 et E2 = 20, alors que le CSV donne 5, 4 et 18. Deux mineures ont été rattachées à A1 et A2 ; le CSV fait foi.

---

### 3. Décisions de l'owner : gouvernance, proportion, craft

**F — 11.00** (`Audit_Phase11_00_DECISIONS_Owner_Sortie_Phase10.md`)
- L'owner (« Junior ») accepte les 8 abaissements.
- **D-ACT-1 = c. Mixte** : seuls les invariants déterministes et à fort risque passent en machine. Le reste est déclaré « forme seule ».
- **D-FAC-1 = c** : façades bornées, marquées « voir propriétaire », avec un test de cohérence au build.
- Une PATCH-DECISION par grappe.
- **I :** l'owner a choisi de ne pas transformer toute la prose en contrôle machine. C'est une limite volontaire au poids de la gouvernance.

**F — 11.10 C3 Proportion** (`Audit_Phase11_10_PATCH_DECISION_C3_Proportion.md`)
- Défaut commun (en-tête) : « une forme prévue pour le cas lourd s'applique au cas léger ».
- Le quota de « deux changements structurels » par direction n'avait aucune source. Il contredisait :
  - ACTION 903 (« aucun quota de variantes ») ;
  - SAVOIR 279 ;
  - BIBLIOTHEQUE 237 (« un seul levier »).
- Décision (§4.2) : le quota est retiré (`minItems` 2 → 1). Deux invariants d'authenticité sont ajoutés (directions distinctes, changements non dupliqués). Si aucune alternative plausible n'existe, l'ensemble créatif « n'est pas produit : aucune direction n'est fabriquée pour l'atteindre » (T-8).
- §4.1 : DERIVE passe de 15 lignes à un démarrage avec 5 notions.
- §4.3 : deux sorties nommées (réponse visible, handoff) remplacent cinq listes concurrentes.
- §8 « Limite déclarée » : la réduction de charge « reste une hypothèse tant qu'un run réel ne l'a pas mesurée ».
- **⚑ :** la B01 exigeait de fabriquer des variantes, ce qui produit de la diversité simulée. C'est reconnu et corrigé. F-PC-001 a été « portée dans sept unités ».

**F — 11.17 D1 Frontière du jugement de craft** (`Audit_Phase11_17_PATCH_DECISION_D1_Frontiere_jugement_craft.md`)
- L'inventaire (§2) recense **huit formes de jugement de craft, de G1 à G8**.
- Un run DIRECTION pouvait produire « deux revues… et trois grilles qui ne nomment pas les mêmes défauts dominants ».
- 6.02b : « cinq grilles mobilisées pour un seul objet » (tableau d'en-tête).
- Décision (§4) : « une revue, une grille de dimensions, un gate ». Il reste CFT-00, la Creative Quality Review, le contrat positif (devenu une vue déclarée) et Gate C. Les grilles G4 et G6 sont supprimées par fusion.
- §5 « Limite » : l'unification « ne garantit pas que la revue juge juste ».
- **⚑ :** la gouvernance du craft pesait sur le processus créatif à travers ces grilles multiples.

**F — 11.23 Clôture** (`Audit_Phase11_23_CLOTURE_Phase11_Conformite.md`)
- 22 PATCH-DECISION.
- Liste close : 92 lignes, 82 invariants actifs.
- LCF : 21 entrées.
- 22 harnais : 40 témoins et 300 cas, dont 297 rouges sur B01.
- K6 (§5) : « aucun score, un quota retiré ».
- §3.4 : 16 limites déclarées, résumées ainsi : « une garde… prouve une forme, pas un effet ».
- §4.6 : épreuves exigées, dont « Imitation : C6 » et « Mesure M, avec et sans DG, sur au moins trois briefs : C7 ».
- §8 : « Aucune efficacité n'est établie par la phase 11 ».
- **I :** le dispositif d'outillage a beaucoup grossi (liste close, LCF, harnais), en contraste avec la retenue revendiquée au §32 du protocole.

---

### 4. Capacité créative, charge cognitive, coût de lecture (phases 5 à 7)

Dossier : `kit/reference/B01_transfert/03_Rapports/03_Phases_3_a_9/`.

**F — 5.02** (`Audit_Phase5_02_…Sections_Usage_Charge.md`)
- §3 : le CLI extrait le bloc parent entier :
  - `DIRECTION/START` : 125 lignes / 12 646 caractères, alors que la skill demande « arbre seulement » ;
  - `SAVOIR/CRAFT` : 181 lignes ;
  - `BIBLIOTHEQUE/SELECT` : 94 lignes.
- Un cas conditionnel cumule « 400 lignes et 40 914 caractères » avant ACTION.
- Six locators refusés (titres présents mais non indexés).
- §5 « Limites » : aucun lecteur humain, aucune mesure en tokens.

**F — 5.04** (`Audit_Phase5_04_…Synthese_Six_Axes.md`)
- §2, axe Charge cognitive : les volumes « créent une hypothèse de surcharge ».
- Les six axes convergent vers une « sélectivité à deux étages » (bon propriétaire, puis seule section utile).
- §4 : « ne pas traiter la seule densité de règles comme qualité visuelle ».

**F — 6.01** (`Audit_Phase6_01_…Premier_Objet_Dix_Dimensions.md`)
- §1 : les deux exemples canoniques sont « illustratifs ». Le premier est une scène sonore simulée. Le second est un JSON avec « 3 opérateurs sur 4 » non authentifiés. Aucun n'atteint « observé sur rendu ».
- §5 : la prescription « ne prouve pas que le système produit effectivement de meilleurs objets ».
- §4 « Friction » : F-PC-001 force une direction en trop, et F-BIB-005 peut imposer « une signature spatiale forcée ».

**F — 6.02** (`Audit_Phase6_02_…Pilotes_Preparation_Observation.md`)
- Les pilotes HTML ont été construits par l'auditeur.
- §3 : l'ouverture `file:` a été refusée. Aucune capture n'a été faite et aucune dimension n'a reçu de « PASS ».
- §4 : pas de groupe de comparaison ni d'exécutant indépendant.

**F — 7.01** (`Audit_Phase7_01_…Boucles_…One_Shot.md`)
- §4 : un `decision_change` du type « J'ai écrit une explication supplémentaire seulement » est **accepté** par le validateur.
- §5 : « Aucun one-shot de cet audit n'est qualifié de réussi ».
- La cardinalité de production « peut forcer une direction de plus ».

**F — Résumés du plan maître sur les épreuves sur objet**
Rapports source non relus, conformément à votre consigne ; les citations viennent des lignes 127 à 130 du plan.
- 6.02b : observateur unique non humain, « réserve forte en spécificité ».
- 9.06 : « convergence implicite non couverte (renforce F-SAV-002) ».
- **⚑ 9.08 :** « run DG : … mais **présence/désirabilité inférieures à la baseline** (jugement unique) ». Autres éléments de 9.08 :
  - « surcharge résiduelle mesurée : START = 80 % de la route LITE » ;
  - « HANDOFF 9/13 N/A » ;
  - « Convergence : neutres + accent vert des deux côtés (F-SAV-002, N=1) ».
- **I :** c'est le seul signal direct que la gouvernance a dégradé le résultat créatif. Il reste fragile : N = 1, un seul juge, aucun observateur indépendant.

**⚑ Les exemples et les gabarits comme vecteurs de convergence**
- 10.00 §3F affirme : « Les exemples (F-EX, F-MP) **sont copiés par les agents**. Un claim mal formé dans un exemple se reproduit. » **I :** c'est posé comme un postulat, sans mesure dans les fichiers lus.
- Le plan (ligne 150, résumé de 11.13 C6) indique que les 4 exemples de `examples.md` contredisaient les règles.
- Le plan (ligne 151, résumé de 11.14 C7) indique : « 363 renforce la pente du modèle » (probable), « la correction réduit la convergence » (hypothétique).
- La grappe C7 cible la prescription palette « neutres + accent » de F-SAV-002. La recommandation du CSV ajoute « une question de convergence (cette palette est-elle le défaut ?) ».
- L'épreuve d'imitation a été rejouée en R.02 : « imitation 0/2 » (plan, Tableau de bord, ligne 33).

---

### 5. Lignée des versions

**F — Pièces de lignée**
- `kit/reference/B01_transfert/00_LIRE_DABORD.md` : archive au 25 septembre 2026 ; B01 = compilation `Design_Governance_V1.0.md` (SHA `016e6002…`), extraite en 60 fichiers ; état arrêté à la phase 9.05, 157 fiches provisoires.
- `kit/package/V1/official/CHANGELOG.md` donne la séquence :
  - **V1.0.0**, 19 septembre 2026 : « baseline expérimentale ». L'efficacité, la charge cognitive et la « qualité perceptuelle produite » sont `NOT-VERIFIED`.
  - **V1.1.0** : produite par la candidate B03 après la phase 12. Elle apporte l'autorité du schéma, la migration RUN_CARD, `SEED`, deux sorties canoniques, une « palette sans répartition imposée » et le premier objet relié à CFT-00.
  - **V1.1.1**, 26 septembre 2026 : construite sur B04, c'est le « Retour d'audit ». Les changements sont textuels et de façade (LCF de 21 à 42), sans changement de schéma, plus un erratum sur la phrase « façades alignées ».
- Le tableau de bord du plan donne les étapes de statut :
  - Phase 14 : `AUDIT-RETURN` ;
  - R.01 à R.03 ;
  - statut final `AUDIT-PASS-WITH-RESERVATION` avec 9 réserves, dont « efficacité NOT-VERIFIED », « F-DIR-044/coût » et « coût d'un run ».
- B02 (V1.0.1) a été gelée comme hypothèse.
- Chaque version du CHANGELOG répète : « L'efficacité sur des runs réels reste `NOT-VERIFIED` ».

---

### Synthèse des alertes ⚑

1. **Convergence esthétique**
   - La prescription « neutres + accent » (F-SAV-002) a été observée des deux côtés en 9.08 (N = 1).
   - Une convergence implicite n'était pas couverte (9.06).
   - Le passage en Majeur était conditionné à N ≥ 3 confirmations indépendantes, qui n'ont jamais été obtenues.
2. **Exemples copiés**
   - L'audit postule que les exemples sont copiés (10.00 §3F) et a constaté qu'ils contredisaient les règles (C6).
   - L'épreuve d'imitation a donné 0/2.
3. **Gouvernance qui pèse sur la création**
   - Le seul signal est le run 9.08 : présence et désirabilité inférieures à la baseline sans DG (jugement unique).
   - Des quotas fabriquaient de la diversité (F-PC-001).
   - Il y avait huit formes de jugement du craft (D1).
   - Le START servi représente 80 % de la route LITE.
   - Le validateur accepte une simple rationale comme itération.
4. **Biais de l'audit**
   - Environ 10 % des fiches portent sur la création.
   - Il n'y a eu ni observateur indépendant, ni mesure avec et sans DG sur trois briefs (C7), ni aucune efficacité `FULL`.
   - Les corrections ont ajouté beaucoup de dispositifs de contrôle : 82 invariants, 42 conditions de façade, 300 cas.