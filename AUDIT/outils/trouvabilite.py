#!/usr/bin/env python3
"""Audit : trouvabilité. Pour chaque besoin, des termes qu'un agent emploierait ; succès si --trouver renvoie une route attendue.

Usage : trouvabilite.py SORTIE.json
"""
import json, re, subprocess, sys
REPO = "/home/user/DESIGN-GOVERNANCE1"
B = [  # (besoin, routes attendues (préfixes), termes)
 ("contraste du texte", ["ACTION/GATE-A", "SAVOIR/CRAFT"], ["contraste", "contrast", "lisibilité"]),
 ("texte posé sur une photo", ["SAVOIR/CRAFT", "SAVOIR/STATE", "ACTION/GATE-A"], ["texte sur image", "texte sur photo", "overlay", "voile"]),
 ("choisir une police", ["SAVOIR/TYPE", "SAVOIR/CRAFT"], ["typographie", "police", "font", "fonte"]),
 ("construire une palette", ["SAVOIR/CRAFT"], ["palette", "couleur", "color"]),
 ("mode sombre", ["SAVOIR/CRAFT"], ["dark mode", "mode sombre", "thème sombre"]),
 ("adapter au mobile", ["ACTION/UI-UX-REALITY", "SAVOIR/STATE", "SAVOIR/CONTEXT"], ["mobile", "responsive", "petit écran"]),
 ("état vide", ["ACTION/UI-UX-REALITY", "SAVOIR/STATE"], ["état vide", "empty", "vide"]),
 ("bouton désactivé", ["ACTION/UI-UX-REALITY", "SAVOIR/STATE"], ["désactivé", "disabled", "inactif"]),
 ("message d'erreur de formulaire", ["SAVOIR/STATE", "ACTION/UI-UX-REALITY"], ["erreur", "formulaire", "validation"]),
 ("focus clavier", ["ACTION/GATE-A", "SAVOIR/CONTEXT"], ["focus", "clavier", "keyboard"]),
 ("taille des cibles tactiles", ["ACTION/GATE-A"], ["cible", "target size", "tactile"]),
 ("lecteur d'écran", ["ACTION/GATE-A", "SAVOIR/CONTEXT"], ["lecteur d'écran", "screen reader", "aria"]),
 ("animation et mouvement réduit", ["SAVOIR/CONTEXT", "SAVOIR/STATE", "ACTION/GATE-A"], ["animation", "motion", "mouvement"]),
 ("performance et poids", ["SAVOIR/TECH", "SAVOIR/CONTEXT"], ["performance", "poids", "chargement"]),
 ("multilingue", ["SAVOIR/CONTEXT", "SAVOIR/TYPE"], ["multilingue", "traduction", "localisation"]),
 ("faux témoignages", ["DIRECTION/EXTERNAL-START", "SAVOIR/INTEGRITY", "DIRECTION/FIRST-OBJECT"], ["témoignage", "avis", "testimonial"]),
 ("logos de clients", ["BIBLIOTHEQUE/SELECT", "DIRECTION/EXTERNAL-START"], ["logos", "logo clients", "preuve sociale"]),
 ("contenu d'exemple", ["DIRECTION/EXTERNAL-START", "DIRECTION/FIRST-OBJECT"], ["exemple", "placeholder", "lorem"]),
 ("photo ou image d'illustration", ["SAVOIR/SOURCE", "SAVOIR/DESIGN-ATLAS"], ["photo", "image", "banque d'images"]),
 ("illustration", ["SAVOIR/SOURCE", "SAVOIR/STYLE", "SAVOIR/DESIGN-ATLAS"], ["illustration", "dessin"]),
 ("icônes", ["SAVOIR/STATE", "BIBLIOTHEQUE/MICRO"], ["icône", "icon", "pictogramme"]),
 ("grain et texture", ["BIBLIOTHEQUE/MODIFIER", "BIBLIOTHEQUE/SELECT", "SAVOIR/DESIGN-ATLAS"], ["grain", "texture", "bruit"]),
 ("grille de mise en page", ["BIBLIOTHEQUE/GRID"], ["grille", "grid", "colonnes"]),
 ("rangée de cartes", ["BIBLIOTHEQUE/SELECT"], ["cartes", "cards", "trois cartes"]),
 ("premier écran", ["DIRECTION/FIRST-OBJECT", "SAVOIR/CRAFT"], ["premier écran", "hero", "above the fold"]),
 ("page de tarifs", ["BIBLIOTHEQUE/SELECT", "DIRECTION/EXTERNAL-START"], ["tarif", "prix", "pricing"]),
 ("graphique de données", ["BIBLIOTHEQUE/MICRO", "SAVOIR/DESIGN-ATLAS", "SAVOIR/STATE"], ["graphique", "chart", "courbe"]),
 ("chiffres alignés", ["SAVOIR/STATE", "SAVOIR/TYPE"], ["chiffres", "tabular", "tabulaire"]),
 ("ombres et élévation", ["ACTION/GATE-C", "SAVOIR/CRAFT"], ["ombre", "shadow", "élévation"]),
 ("coins arrondis", ["SAVOIR/STATE"], ["arrondi", "radius", "coins"]),
 ("espacement", ["SAVOIR/CRAFT", "SAVOIR/STATE"], ["espacement", "spacing", "marge"]),
 ("densité d'information", ["SAVOIR/CRAFT", "ACTION/GATE-C"], ["densité", "dense", "chargé"]),
 ("éviter le générique", ["SAVOIR/TOOLS", "SAVOIR/CRAFT", "ACTION/ANTI-SLOP", "BIBLIOTHEQUE/SELECT"], ["slop", "générique", "convergence"]),
 ("tendance du moment", ["SAVOIR/TOOLS"], ["tendance", "trend", "vague"]),
 ("capture du rendu", ["ACTION/VISUAL_PROOF", "ACTION/GATE-A"], ["capture", "screenshot", "check_render"]),
 ("hiérarchie visuelle", ["SAVOIR/CRAFT", "ACTION/GATE-C"], ["hiérarchie", "hierarchy", "foyer"]),
 ("données d'enfants", ["SAVOIR/CONTEXT", "SAVOIR/INTEGRITY", "DIRECTION/DOMAIN-FRAME"], ["enfant", "mineur", "données personnelles"]),
 ("navigation du site", ["BIBLIOTHEQUE/MODIFIER"], ["navigation", "menu", "nav"]),
 ("ton et microcopie", ["SAVOIR/STATE", "SAVOIR/CRAFT"], ["microcopie", "ton", "rédaction"]),
 ("design system et tokens", ["BIBLIOTHEQUE/COMPONENTS", "SAVOIR/SYSTEM"], ["token", "design system", "composant"]),
]
res = []
for besoin, attendu, termes in B:
    for t in termes:
        out = subprocess.run([sys.executable, f"{REPO}/scripts/read_route.py", "--trouver", t, *sys.argv[2:]], capture_output=True, text=True, cwd=REPO).stdout
        locs = []
        for line in out.splitlines():
            m = re.match(r"^((?:DIRECTION|ACTION|SAVOIR|BIBLIOTHEQUE)/\S+)\s", line)
            if m and m.group(1) not in locs:
                locs.append(m.group(1))
        n = re.search(r"(\d+) ligne\(s\) normative\(s\), (\d+) route", out)
        hit = [i for i, l in enumerate(locs) if any(l == a or l.startswith(a + "/") for a in attendu)]
        res.append({"besoin": besoin, "terme": t, "lignes": int(n.group(1)) if n else 0, "routes": len(locs),
                    "trouve": bool(hit), "rang": (hit[0] + 1) if hit else None, "premieres": locs[:3]})
json.dump(res, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
