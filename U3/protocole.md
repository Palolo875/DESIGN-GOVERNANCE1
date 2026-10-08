# U3 — Protocole de mesure (figé avant le premier run)

**Base :** paquet `R2026-10-08-CORRECTIONS`, commit `01be58d`, copie figée par `git archive` dans `U3/paquet/`.
**Producteur :** sous-agent Opus 5.5 (alias `opus` de l'outil Agent), contexte neuf, un run à la fois (D12, D13).
**Juges :** Sonnet 5.5 (principal) et Haiku 5.5 (second avis), en contexte neuf, sur captures seules ; puis le propriétaire, sur planche anonymisée.

## Briefs

| Brief | Texte remis à l'agent |
|---|---|
| B2 | « Il me faut une landing page pour notre SaaS de facturation. » |
| B3 | « Il me faut un site pour mon école de natation pour enfants. » (D14) |
| B1 | « Améliore le contraste du bouton secondaire de cette page sans changer sa structure. » (page fournie `avant.html`) |

## Ordre des runs (conditions alternées)

R1 B2 sans · R2 B2 avec · R3 B2 sans · R4 B2 avec · R5 B3 sans · R6 B3 avec · R7 B1 avec.

## Consigne commune (mot pour mot, `{…}` remplacés)

> Tu réponds à une demande de design. La personne a écrit : « {brief} »
> Personne ne pourra répondre à tes questions pendant ce travail : livre dans ce tour, comme tu le ferais pour elle.
> Livrable : une page HTML autonome, `{dossier}/index.html` (CSS et JS dans le fichier ; polices et images externes autorisées par URL). N'écris rien hors de `{dossier}`.
> {bloc système ou rien}
> N'ouvre aucun fichier hors de {périmètre}.
> Tu peux utiliser tes outils, y compris un navigateur sans tête (Playwright et Chromium sont installés) pour regarder ton rendu.
> Termine par la réponse exacte que tu donnerais à la personne.

**Bloc système (condition « avec ») :** « Tu travailles avec Design Governance V1, installé dans `{paquet}`. Commence par lire `{paquet}/skills/design-governance-practice/SKILL.md` et applique-le ; ses commandes `python3 scripts/…` s'exécutent depuis `{paquet}`. »
**Périmètre :** « `{dossier}` » (sans) ; « `{dossier}` et `{paquet}` » (avec).
**B1 :** « La page est `{dossier}/index.html` ; modifie-la sur place. » remplace la ligne « Livrable ».

## Limites connues, déclarées avant la mesure

- Le périmètre de lecture est une consigne, pas un bac à sable : l'agent « sans » pourrait techniquement lire le dépôt. Les transcriptions sont vérifiées après coup.
- B1 ressemble à l'exemple LITE de `examples.md` (contraste du bouton secondaire). B1 n'a pas de condition « sans » : il mesure la proportion (le système reste-t-il léger ?), pas un écart.
- N = 1 ou 2 par cellule : la mesure décrit, elle ne prouve pas.
- Le modèle réellement servi derrière l'alias `opus` n'est pas attesté par l'outil ; il est déclaré tel quel.
