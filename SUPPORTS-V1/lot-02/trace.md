# Présentation V1 expérimentale — deuxième lot

Le propriétaire délègue le choix visuel : Manrope, palettes par rôle et composition documentaire sont retenus pour les supports. Le premier atlas reste conservé sur refonte. Concurrents et anglais demeurent reportés.

Mode DIRECTION pour les diagrammes, avec une retouche de présentation du produit. Décision : expliquer le parcours et la boucle sans ajouter de règle, puis rendre la V1 présentable. Risque : transformer une vue simplifiée en chemin rigide, rendre la gouvernance facultative ou perdre une règle de maintenance au nettoyage. Preuve minimale : mêmes responsabilités et routes, trois supports lisibles en clair/sombre et mobile, sources et texte communs, distributions reproductibles, documentation opérationnelle valide. Arrêt : supports intégrés et contrôles exécutés, avec les limites d’usage conservées.

Avant modification : sept fichiers de présentation et de distribution sont copiés à l’octet près dans avant/, avec leurs empreintes. Le noyau, les règles métier, les routes, les modes, les gates, les schémas et les protections restent dans leurs sections propriétaires. Le journal est une source normative de maintenance : son contrat de budget et d’évolution est conservé, pas supprimé pour raccourcir.

Sources mobilisées : skill locale, arbre de classement, ligne DIRECTION, boucle de création, flux de décision, premier objet, sections de gouvernance, validation structurelle et distributions. La carte d’ensemble vient du lot carte-01 ; les deux autres vues sont construites sur le contenu actuel. Les diagrammes seront des projections pour les personnes, pas de nouvelles routes de l’agent.

Hypothèse : le langage documentaire déjà observé sert mieux ces relations qu’une série d’illustrations distinctes. La délégation autorise le choix du support ; elle ne constitue ni test de compréhension ni preuve d’efficacité esthétique du système.

## Après observation et clôture du lot

Les trois pages finales passent 76 parcours dans Chromium 151.0.7922.173. Les captures, exports SVG rouverts, licences, textes agrandis et absence de script sont observés ; leurs empreintes sont dans preuves/verification.json. Trois recettes Gate A ne relèvent aucun RETURN et conservent leurs réserves de couverture. La validation complète avec navigateur, compilation, CLI, fixtures, distributions et reproductibilité termine par FULL VALIDATION PASSED. Les deux archives et le snapshot Local sont conservés avec leurs empreintes dans livraison.json. La skill est identique à celle du commit de base.

La première instrumentation de capture SVG bloquait avec full_page ; la capture à la taille native résout ce défaut de mesure. Les passages interrompus restent distincts d’un run achevé. Le premier build copiait le nouveau contrôle avant de créer scripts/ dans le staging : ordre corrigé, puis validation complète rejouée.

L’inspection de la capture à 320 px a révélé un titre trop petit : la suppression de la variante serif avait laissé un sélecteur partagé avec le paragraphe. Le sélecteur a été séparé, le titre retrouvé et les parcours rejoués. La boucle sombre avait des étapes claires mais aucun retour dessiné ; le retour vers le diagnostic est ajouté depuis la décision, avec sa condition. La paire avant/finale garde le même canvas et montre cette relation. Les 76 contrôles passent sur ces nouveaux artefacts ; les observations précédentes restent conservées.

Les neuf connexions citent 27 sources. Le journal changé a été relu et ses contrats conservés ; les 26 autres textes servis sont identiques. Seule la métadonnée de révision de l’index a été synchronisée, ses neuf entrées restant identiques. Les anciennes présentations sont conservées à l’octet près dans avant/. Les sauts Markdown et le texte original de licence sont identifiés dans hygiene.json. Aucun espace inattendu n’est présent.

Médium : Web HTML et SVG. Portée : trois pages, six largeurs et deux thèmes, états de sélection, clavier, texte agrandi, sans script et SVG autonome. Base des contrôles ciblés : WCAG 2.2 AA, sans certification globale. Méthode : automatisation et inspection du coordinateur. Budget : aucune dépendance réseau ni motion nécessaire ; INP et performances utilisateurs non mesurés. Compréhension, lecteur d’écran, autres navigateurs et matériel réel restent hors preuve. Prochaine preuve : tâche de découverte adaptée au public.

Clôture exploratoire : les supports et le paquet sont présentables, les contraintes techniques observées sont couvertes ; l’efficacité générale et l’usage réel restent non vérifiés. La direction documentaire est retenue par délégation, sans transformer ce choix en preuve humaine. Concurrents et anglais demeurent reportés.

## Livraison révisable

Le lot est enregistré au commit `213cfbaf8867142eb834c834311adb0fa626d8fe` et proposé dans la [PR 2](https://github.com/Palolo875/DESIGN-GOVERNANCE1/pull/2), en brouillon. Les deux CI ont démarré sur ce SHA. Aucune fusion ni publication de version n’est effectuée. Le dossier complet est conservé sur `refonte` dans `SUPPORTS-V1/lot-02/`.
