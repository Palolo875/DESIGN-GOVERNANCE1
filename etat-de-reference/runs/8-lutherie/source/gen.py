"""Génère projet/site/index.html. Lancer : python3 gen.py"""
import html
from pathlib import Path
import violon

OUT = Path(__file__).resolve().parent.parent / "site" / "index.html"
NNBSP = " "  # espace fine insécable avant ; : ? !
TEL = "01 99 00 41 27"
TEL_HREF = "tel:+33199004127"
MAIL = "contact@atelier-fontanes.example"


def fr(s):
    for p in (" :", " ;", " ?", " !"):
        s = s.replace(p, NNBSP + p[1])
    return s


PIECES = [
    dict(id="chevilles", n=1, side="d", pt=(39, 74), cy=74,
         symptome="Une cheville glisse ou force",
         titre="Ajuster les chevilles",
         texte="Une cheville qui glisse a pris du jeu dans le chevillier ; une cheville qui force a gonflé avec l’humidité. On la nettoie, on la savonne, et si elle est usée on en tourne une neuve à la mesure du trou.",
         delai="Sur place, ou une semaine s’il faut une cheville neuve",
         prix="15 à 90 €"),
    dict(id="touche", n=2, side="d", pt=(6, 300), cy=252,
         symptome="Une corde frise, ça grésille",
         titre="Contrôler la touche et le sillet",
         texte="Le grésillement vient souvent d’une touche creusée par le jeu, d’un sillet trop bas ou d’une pièce décollée qui vibre. On cherche la cause avec vous avant de toucher à quoi que ce soit ; un dressage de touche se fait à l’atelier.",
         delai="Diagnostic sur place ; dressage en 3 à 5 jours",
         prix="Diagnostic gratuit ; dressage 80 à 160 €"),
    dict(id="chevalet", n=3, side="d", pt=(21, 430), cy=398,
         symptome="Le chevalet penche vers la touche",
         titre="Redresser ou refaire le chevalet",
         texte="À chaque accord, les cordes tirent le haut du chevalet vers la touche. Redressé à temps, il se garde ; voilé, il se remplace par un chevalet taillé aux pieds de votre table et à la courbe de votre touche.",
         delai="Redressage sur place ; chevalet neuf en une semaine",
         prix="Redressage offert ; chevalet neuf 90 à 160 €"),
    dict(id="ame", n=4, side="d", pt=(15, 443), cy=468,
         symptome="Le son s’est fermé depuis l’automne",
         titre="Régler l’âme",
         texte="L’âme est une baguette d’épicéa coincée entre la table et le fond, sous le pied droit du chevalet. Quand le chauffage sèche le bois, elle bouge et le son se ferme. On la déplace par l’ouïe, au dixième de millimètre, et vous jouez entre chaque essai.",
         delai="Environ 45 minutes, en votre présence",
         prix="40 à 70 €"),
    dict(id="fissure", n=5, side="g", pt=(-44, 336), cy=336,
         symptome="Une fissure est apparue sur la table",
         titre="Recoller une fissure",
         texte="Les fissures de table s’ouvrent surtout l’hiver. Il faut les refermer vite, avant que la saleté n’y entre : on ouvre la table, on recolle à la colle de peau et on pose des taquets à l’intérieur.",
         delai="3 à 6 semaines selon la fissure",
         prix="Sur devis, à partir de 250 €"),
    dict(id="bord", n=6, side="g", pt=(-104, 500), cy=500,
         symptome="Ça bourdonne quand je joue fort",
         titre="Recoller un bord décollé",
         texte="Un bord de table ou de fond s’est décollé des éclisses : l’instrument bourdonne sur certaines notes. On recolle à la colle de peau, qui se défait proprement le jour où l’instrument devra être ouvert.",
         delai="1 à 3 jours",
         prix="40 à 120 €"),
]
DEFAUT = "ame"

TAILLES = [
    ("1/16", 230, "moins de 43 cm", 16), ("1/10", 240, "43 à 46 cm", 16),
    ("1/8", 255, "46 à 49 cm", 16), ("1/4", 280, "49 à 53 cm", 16),
    ("1/2", 310, "53 à 57 cm", 18), ("3/4", 335, "57 à 60 cm", 18),
    ("4/4", 356, "60 cm et plus", 22),
]


def callouts():
    out = []
    for p in PIECES:
        cx = 132 if p["side"] == "d" else -132
        px, py = p["pt"]
        ex = cx - 12 if p["side"] == "d" else cx + 12
        out.append(
            f'<g class="repere" data-repere="{p["id"]}">'
            f'<line x1="{ex}" y1="{p["cy"]}" x2="{px}" y2="{py}" class="fil"/>'
            f'<circle cx="{px}" cy="{py}" r="2.4" class="point"/>'
            f'<circle cx="{px}" cy="{py}" r="10" class="halo"/>'
            f'<circle cx="{cx}" cy="{p["cy"]}" r="12" class="pastille"/>'
            f'<text x="{cx}" y="{p["cy"] + 4.6}" text-anchor="middle" class="num">{p["n"]}</text>'
            f"</g>"
        )
    return "".join(out)


def cotes():
    y0, y1 = violon.BODY_TOP, violon.BODY_TOP + 356
    return f"""
    <g class="cote">
      <line x1="-162" y1="{y0}" x2="-162" y2="{y1}"/>
      <line x1="-168" y1="{y0}" x2="-120" y2="{y0}" class="rappel"/>
      <line x1="-168" y1="{y1}" x2="-104" y2="{y1}" class="rappel"/>
      <path d="M-162,{y0} l-3,8 h6 Z M-162,{y1} l-3,-8 h6 Z" class="fleche"/>
      <text transform="translate(-167 {(y0 + y1) / 2}) rotate(-90)" text-anchor="middle">caisse 356</text>
      <line x1="-104" y1="607" x2="104" y2="607"/>
      <path d="M-104,607 l8,-3 v6 Z M104,607 l-8,-3 v6 Z" class="fleche"/>
      <text x="0" y="621" text-anchor="middle">208</text>
    </g>"""


def plan_svg():
    y = violon.BODY_TOP
    return f"""<svg class="plan-svg" viewBox="-176 -6 352 634" role="img" aria-labelledby="plan-titre plan-desc">
  <title id="plan-titre">Plan d’un violon vu de face</title>
  <desc id="plan-desc">Dessin schématique d’un violon entier, avec ses cotes principales en millimètres et six repères numérotés : chevilles, touche, chevalet, âme, table et bord.</desc>
  <use href="#violon-g"/>
  <path class="fissure" d="M-40,{y+92} l-3,10 l2,9 l-4,12 l1,10 l-3,9"/>
  <circle class="ame" cx="15" cy="{y+206}" r="3.4"/>
  {cotes()}
  {callouts()}
</svg>"""


def boutons():
    out = []
    for p in PIECES:
        sel = "true" if p["id"] == DEFAUT else "false"
        out.append(
            f'<li><button type="button" class="symptome" data-piece="{p["id"]}" aria-pressed="{sel}" aria-controls="fiche-{p["id"]}">'
            f'<span class="n" aria-hidden="true">{p["n"]}</span><span class="t">{html.escape(fr(p["symptome"]))}</span></button></li>'
        )
    return "\n".join(out)


def fiches():
    out = []
    for p in PIECES:
        hidden = "" if p["id"] == DEFAUT else " data-cache"
        sujet = html.escape(f"{p['titre']} (violon)")
        out.append(f"""<article class="fiche" id="fiche-{p['id']}"{hidden}>
  <p class="fiche-renvoi">Repère {p['n']} sur le plan</p>
  <h3>{html.escape(fr(p['titre']))}</h3>
  <p>{html.escape(fr(p['texte']))}</p>
  <dl>
    <div><dt>Délai</dt><dd>{html.escape(fr(p['delai']))}</dd></div>
    <div><dt>Prix indicatif</dt><dd>{html.escape(fr(p['prix']))} <span class="ex">exemple</span></dd></div>
  </dl>
  <p class="fiche-actions"><a class="btn" href="mailto:{MAIL}?subject={sujet}">Écrire à l’atelier à ce sujet</a>
  <a class="lien" href="{TEL_HREF}">ou appeler le {TEL}</a></p>
</article>""")
    return "\n".join(out)


def tailles():
    out = []
    for frac, L, bras, prix in TAILLES:
        out.append(f"""<li style="--l:{L}">
  <svg class="t-debout" viewBox="-112 -4 224 604" aria-hidden="true" focusable="false"><use href="#violon-g"/></svg>
  <svg class="t-couche" viewBox="-4 -112 604 224" aria-hidden="true" focusable="false"><use href="#violon-g" transform="matrix(0 1 1 0 0 0)"/></svg>
  <div class="t-texte">
    <p class="t-frac">{frac}</p>
    <p class="t-mesure"><span>caisse</span> {L} mm</p>
    <p class="t-mesure"><span>bras</span> {bras}</p>
    <p class="t-prix">{prix} € / mois</p>
  </div>
</li>""")
    return "\n".join(out)


CSS = """
@font-face{font-family:"Libre Caslon Text";src:url(fonts/caslon-400.woff2) format("woff2");font-weight:400;font-style:normal;font-display:swap}
@font-face{font-family:"Libre Caslon Text";src:url(fonts/caslon-400i.woff2) format("woff2");font-weight:400;font-style:italic;font-display:swap}
@font-face{font-family:"Libre Caslon Text";src:url(fonts/caslon-700.woff2) format("woff2");font-weight:700;font-style:normal;font-display:swap}
@font-face{font-family:"IBM Plex Sans";src:url(fonts/plex-400.woff2) format("woff2");font-weight:400;font-style:normal;font-display:swap}
@font-face{font-family:"IBM Plex Sans";src:url(fonts/plex-400i.woff2) format("woff2");font-weight:400;font-style:italic;font-display:swap}
@font-face{font-family:"IBM Plex Sans";src:url(fonts/plex-500.woff2) format("woff2");font-weight:500;font-style:normal;font-display:swap}
@font-face{font-family:"IBM Plex Sans";src:url(fonts/plex-600.woff2) format("woff2");font-weight:600;font-style:normal;font-display:swap}
@font-face{font-family:"IBM Plex Sans Condensed";src:url(fonts/plexcond-500.woff2) format("woff2");font-weight:500;font-style:normal;font-display:swap}
@font-face{font-family:"IBM Plex Sans Condensed";src:url(fonts/plexcond-600.woff2) format("woff2");font-weight:600;font-style:normal;font-display:swap}

:root{
  --papier:#f3f4f1; --papier-2:#e6e8e3; --blanc:#fbfbf9;
  --encre:#1d1a17; --encre-2:#55504a; --trait:#6c716d;
  --ebene:#1d1a17; --erable:#e8d6b0; --corde:#dcd8cf;
  --vernis:#9a4f22; --vernis-clair:#c9772f; --vernis-fonce:#5b2a12; --vernis-texte:#8a3d14;
  --nuit:#1d1a17; --nuit-texte:#ecebe6; --nuit-2:#b9b4aa;
  --serif:"Libre Caslon Text", Georgia, "Times New Roman", serif;
  --sans:"IBM Plex Sans", "Helvetica Neue", Arial, sans-serif;
  --cond:"IBM Plex Sans Condensed", "Arial Narrow", "IBM Plex Sans", sans-serif;
  --gouttiere:clamp(16px, 4vw, 48px);
}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--papier);color:var(--encre);font:400 17px/1.55 var(--sans);font-feature-settings:"kern"}
img,svg{display:block}
a{color:inherit}
:focus-visible{outline:2px solid var(--encre);outline-offset:3px}
.cadre{max-width:1360px;margin:0 auto;padding:0 var(--gouttiere)}
.defs{position:absolute;width:0;height:0;overflow:hidden}

/* note de maquette */
.note-maquette{background:var(--encre);color:var(--nuit-texte);font-size:14px;line-height:1.4}
.note-maquette p{margin:0;padding:8px 0}

/* en-tête */
.tete{border-bottom:1px solid #c9ccc6}
.tete .cadre{display:flex;align-items:center;gap:32px;min-height:68px;flex-wrap:wrap}
.marque{font:400 22px/1 var(--serif);text-decoration:none;margin-right:auto}
.tete nav ul{display:flex;gap:28px;list-style:none;margin:0;padding:0}
.tete nav a{text-decoration:none;font-size:15px;padding:12px 0;display:inline-block}
.tete nav a:hover{text-decoration:underline;text-underline-offset:4px}
.btn{display:inline-flex;align-items:center;min-height:44px;padding:10px 18px;background:var(--encre);color:var(--papier);text-decoration:none;font-weight:500;font-size:16px;border-radius:2px}
.btn:hover{background:#3a332c}
.lien{font-size:16px;text-underline-offset:4px;display:inline-flex;align-items:center;min-height:44px}
.ex{font:italic 400 13px/1 var(--sans);color:var(--encre-2);border-bottom:1px dotted currentColor;white-space:nowrap;vertical-align:.1em}

/* scène 1 : plan et diagnostic */
.scene{display:grid;grid-template-columns:minmax(0,1fr) minmax(300px,440px) minmax(0,1fr);
  grid-template-areas:"intro plan tete-d" "intro plan liste" "intro plan fiche";grid-template-rows:auto auto 1fr;
  column-gap:clamp(24px,3.4vw,56px);padding-top:clamp(28px,4vw,56px);padding-bottom:clamp(48px,6vw,88px)}
.intro{grid-area:intro;align-self:start;padding-top:8px}
.lieu{margin:0 0 20px;font-size:15px;color:var(--encre-2)}
h1{font:400 clamp(54px,5.8vw,84px)/.95 var(--serif);letter-spacing:-.015em;margin:0 0 24px}
h1 .sous{display:block;font-style:italic;font-size:.34em;letter-spacing:0;line-height:1.2;margin-top:12px;color:var(--encre-2)}
.lead{font:400 clamp(20px,1.7vw,24px)/1.4 var(--serif);margin:0 0 24px;max-width:24em;text-wrap:balance}
.depot{margin:0 0 28px;max-width:30em}
.actions{display:flex;flex-wrap:wrap;gap:8px 20px;align-items:center}

.plan{grid-area:plan;margin:0}
.plan-svg{width:100%;height:auto;overflow:visible}
.plan figcaption{font:500 13px/1.4 var(--cond);color:var(--encre-2);margin-top:8px;text-align:center}
.cote line{stroke:var(--trait);stroke-width:.8}
.cote .rappel{stroke-width:.5;stroke-dasharray:2 2}
.cote .fleche{fill:var(--trait)}
.cote text{font:500 11px var(--cond);fill:var(--encre-2)}
.repere .fil{stroke:var(--encre);stroke-width:.8}
.repere .point{fill:var(--encre)}
.repere .halo{fill:none;stroke:var(--blanc);stroke-width:2;opacity:0}
.repere .pastille{fill:var(--papier);stroke:var(--encre);stroke-width:1.2}
.repere .num{font:600 14px var(--cond);fill:var(--encre)}
.repere.actif .pastille{fill:var(--encre)}
.repere.actif .num{fill:var(--papier)}
.repere.actif .fil{stroke-width:1.6}
.repere.actif .halo{opacity:1}
.repere.survol .pastille{stroke-width:2.4}
.fissure{fill:none;stroke:var(--ebene);stroke-width:1.3;opacity:0}
.plan.montre-fissure .fissure{opacity:1}
.ame{fill:none;stroke:var(--blanc);stroke-width:1.1;stroke-dasharray:1.6 1.4;opacity:.75}
.plan.montre-ame .ame{opacity:1;stroke-width:1.6}

.diag-tete{grid-area:tete-d;padding-top:8px}
.diag-tete h2{margin:0 0 8px}
.consigne{margin:0 0 16px;color:var(--encre-2);font-size:16px}
h2{font:400 clamp(32px,3.2vw,48px)/1.06 var(--serif);letter-spacing:-.01em;text-wrap:balance}
.symptomes{grid-area:liste;list-style:none;margin:0 0 20px;padding:0;border-top:1px solid var(--encre)}
.symptome{all:unset;box-sizing:border-box;display:flex;gap:14px;align-items:center;width:100%;min-height:44px;padding:7px 4px;border-bottom:1px solid #c3c6c0;cursor:pointer;font:400 16px/1.3 var(--sans)}
.symptome .n{flex:none;width:26px;height:26px;border:1.2px solid var(--encre);border-radius:50%;display:grid;place-items:center;font:600 14px/1 var(--cond)}
.symptome:hover .t{text-decoration:underline;text-underline-offset:4px}
.symptome[aria-pressed="true"]{font-weight:600}
.symptome[aria-pressed="true"] .n{background:var(--encre);color:var(--papier)}
.symptome:focus-visible{outline:2px solid var(--encre);outline-offset:2px}
.fiches{grid-area:fiche}
.fiche{background:var(--blanc);border:1px solid var(--encre);padding:22px 24px 20px;box-shadow:4px 4px 0 var(--papier-2)}
.fiche + .fiche{margin-top:16px}
.fiche[data-cache]{display:none}
.fiche-renvoi{margin:0 0 4px;font:500 13px/1.3 var(--cond);color:var(--encre-2)}
.fiche h3{font:400 30px/1.1 var(--serif);margin:0 0 12px}
.fiche p{margin:0 0 16px}
.fiche dl{display:grid;grid-template-columns:1fr 1fr;gap:12px 24px;margin:0 0 18px;padding-top:14px;border-top:1px solid #d3d5cf}
.fiche dt{font:500 13px/1.3 var(--cond);color:var(--encre-2);margin-bottom:2px}
.fiche dd{margin:0;font-weight:500;font-variant-numeric:tabular-nums}
.fiche-actions{display:flex;flex-wrap:wrap;gap:4px 18px;align-items:center;margin:0!important}
.precision{font-size:14px;color:var(--encre-2);margin:12px 0 0}

/* scène 2 : louer */
.louer{background:var(--papier-2);padding:clamp(56px,7vw,104px) 0}
.louer-tete{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,1fr);gap:24px clamp(24px,4vw,72px);align-items:end;margin-bottom:clamp(32px,4vw,56px)}
.louer-tete h2{margin:0}
.louer-tete p{margin:0;max-width:32em}
.tailles{list-style:none;margin:0;padding:0 0 0;display:grid;grid-template-columns:repeat(7,minmax(0,1fr));gap:12px;align-items:end;border-bottom:1px solid var(--encre)}
.tailles li{display:flex;flex-direction:column;align-items:center}
.t-debout{height:calc(var(--l) / 356 * clamp(220px, 26vw, 380px));width:auto;margin-bottom:14px}
.t-couche{display:none}
.t-texte{width:100%;border-top:1px solid var(--encre);padding:10px 0 14px;text-align:center}
.t-texte p{margin:0}
.t-frac{font:400 30px/1.1 var(--serif)}
.t-mesure{font:500 14px/1.45 var(--cond);font-variant-numeric:tabular-nums}
.t-mesure span{color:var(--encre-2)}
.t-prix{font-weight:600;font-size:15px;margin-top:6px!important;font-variant-numeric:tabular-nums}
.louer-pied{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,1fr);gap:24px clamp(24px,4vw,72px);margin-top:28px}
.conditions{margin:0;padding:0;list-style:none}
.conditions li{padding:8px 0;border-bottom:1px solid #c3c6c0}
.louer-pied .note{margin:0;color:var(--encre-2);font-size:15px}

/* scène 3 : commander */
.commander{padding:clamp(56px,7vw,104px) 0}
.commander .cadre{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.15fr);gap:40px clamp(32px,5vw,96px);align-items:start}
.commander h2{margin:0 0 20px}
.etiquette-scene{background:var(--vernis-fonce);padding:clamp(28px,4vw,56px);display:grid;place-items:center;margin:28px 0 10px}
.etiquette{background:#f1ead8;color:#2a211a;width:min(100%,420px);aspect-ratio:2.6/1;padding:6px;box-shadow:0 1px 0 rgba(0,0,0,.25)}
.etiquette-in{border:1px solid #2a211a;outline:1px solid #2a211a;outline-offset:-5px;height:100%;display:grid;place-content:center;text-align:center;padding:8px 14px}
.etiquette .e1{font:400 clamp(20px,2.2vw,26px)/1.1 var(--serif);margin:0}
.etiquette .e2{font:italic 400 clamp(14px,1.4vw,17px)/1.3 var(--serif);margin:4px 0 0}
.legende{font-size:14px;color:var(--encre-2);margin:0}
.etapes{list-style:none;margin:0 0 28px;padding:0;counter-reset:e}
.etapes li{display:grid;grid-template-columns:44px minmax(0,1fr) auto;gap:4px 16px;padding:14px 0;border-bottom:1px solid #c3c6c0;counter-increment:e;align-items:baseline}
.etapes li::before{content:counter(e);font:400 26px/1 var(--serif);color:var(--vernis-texte)}
.etapes strong{font-weight:600}
.etapes .duree{font:500 14px var(--cond);color:var(--encre-2);white-space:nowrap}
.prix-neuf{display:flex;flex-wrap:wrap;gap:8px 32px;margin:0 0 24px;padding:0;list-style:none}
.prix-neuf li span{display:block;font:500 13px var(--cond);color:var(--encre-2)}
.prix-neuf li strong{font:400 24px/1.2 var(--serif)}

/* scène 4 : venir */
.venir{background:var(--nuit);color:var(--nuit-texte);padding:clamp(56px,7vw,104px) 0 40px}
.venir :focus-visible{outline-color:var(--nuit-texte)}
.venir .ex{color:var(--nuit-2)}
.venir-grille{display:grid;grid-template-columns:minmax(0,1.2fr) minmax(0,1fr) minmax(0,1fr);gap:40px clamp(24px,4vw,64px)}
.venir h2{margin:0 0 16px;color:var(--nuit-texte)}
.venir .phrase{font:italic 400 clamp(22px,2vw,28px)/1.35 var(--serif);margin:0;max-width:18em}
.venir h3{font:500 13px/1.3 var(--cond);color:var(--nuit-2);margin:0 0 10px;font-weight:500}
.venir address{font-style:normal;margin:0 0 16px}
.horaires{margin:0;display:grid;grid-template-columns:auto 1fr;gap:6px 18px;font-variant-numeric:tabular-nums}
.horaires dt{color:var(--nuit-2)}
.horaires dd{margin:0}
.venir .btn{background:var(--nuit-texte);color:var(--nuit)}
.venir .btn:hover{background:#fff}
.venir p{margin:0 0 14px}
.colophon{margin-top:clamp(48px,6vw,88px);padding-top:20px;border-top:1px solid #4a443d;font-size:14px;color:var(--nuit-2);display:flex;flex-wrap:wrap;gap:8px 32px;justify-content:space-between}
.colophon p{margin:0;max-width:60em}

@media (prefers-reduced-motion:no-preference){
  .repere .pastille,.repere .num,.fissure,.ame{transition:fill .15s, opacity .2s}
}

/* tablette */
@media (max-width:1099px){
  .scene{grid-template-columns:minmax(220px,300px) minmax(0,1fr);grid-template-areas:"intro intro" "tete-d tete-d" "plan liste" "plan fiche";grid-template-rows:auto auto auto 1fr}
  .intro{margin-bottom:40px}
  .tailles{gap:6px}
  .venir-grille{grid-template-columns:1fr 1fr}
  .venir-grille > :first-child{grid-column:1 / -1}
}
/* téléphone */
@media (max-width:699px){
  body{font-size:16px}
  .tete .cadre{gap:4px 16px;padding-top:10px}
  .tete nav{order:3;width:100%}
  .tete nav ul{gap:22px}
  .tete .btn{padding:8px 14px;font-size:15px}
  .scene{grid-template-columns:118px minmax(0,1fr);column-gap:16px;grid-template-areas:"intro intro" "tete-d tete-d" "plan liste" "fiche fiche"}
  .plan figcaption{display:none}
  .cote{display:none}
  .plan-svg{width:150%;margin-left:-25%}
  .repere .pastille,.repere .num,.repere .fil{display:none}
  .repere.actif .halo{stroke:var(--blanc);stroke-width:4;r:16}
  .repere .point{r:4}
  .symptome{font-size:15px;gap:10px}
  .fiche{padding:18px 16px}
  .fiche dl{grid-template-columns:1fr}
  .louer-tete,.louer-pied{grid-template-columns:1fr}
  .tailles{grid-template-columns:1fr;gap:0;border-bottom:0}
  .tailles li{display:grid;grid-template-columns:minmax(0,1fr) 128px;align-items:center;gap:12px;border-top:1px solid #c3c6c0;padding:10px 0}
  .t-debout{display:none}
  .t-couche{display:block;width:calc(var(--l) / 356 * 100%);height:auto}
  .t-texte{border:0;padding:0;text-align:left}
  .t-frac{font-size:24px}
  .commander .cadre{grid-template-columns:1fr}
  .etapes li{grid-template-columns:34px minmax(0,1fr)}
  .etapes .duree{grid-column:2}
  .venir-grille{grid-template-columns:1fr}
}
"""

JS = """
(function(){
  var plan=document.querySelector('.plan');
  var boutons=[].slice.call(document.querySelectorAll('[data-piece]'));
  function choisir(id){
    boutons.forEach(function(b){b.setAttribute('aria-pressed', b.dataset.piece===id ? 'true':'false');});
    [].forEach.call(document.querySelectorAll('.fiche'),function(f){
      if(f.id==='fiche-'+id){f.removeAttribute('data-cache');}else{f.setAttribute('data-cache','');}
    });
    [].forEach.call(document.querySelectorAll('.repere'),function(r){r.classList.toggle('actif', r.dataset.repere===id);});
    plan.classList.toggle('montre-fissure', id==='fissure');
    plan.classList.toggle('montre-ame', id==='ame');
  }
  boutons.forEach(function(b){
    b.addEventListener('click',function(){
      choisir(b.dataset.piece);
      var f=document.getElementById('fiche-'+b.dataset.piece), r=f.getBoundingClientRect();
      if(r.top > window.innerHeight - 140){
        var calme=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
        f.scrollIntoView({block:'nearest', behavior: calme ? 'auto' : 'smooth'});
      }
    });
    b.addEventListener('mouseenter',function(){var r=document.querySelector('[data-repere="'+b.dataset.piece+'"]'); if(r) r.classList.add('survol');});
    b.addEventListener('mouseleave',function(){var r=document.querySelector('[data-repere="'+b.dataset.piece+'"]'); if(r) r.classList.remove('survol');});
  });
  choisir('""" + DEFAUT + """');
})();
"""


def page():
    hidden_defs = f'<svg class="defs" aria-hidden="true" focusable="false"><defs><g id="violon-g">{violon.violin_parts("v")}</g></defs></svg>'
    return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Atelier Fontanes — lutherie du quatuor (maquette)</title>
<meta name="description" content="Maquette de site pour un atelier de lutherie : réglages, réparations, location et instruments neufs. Contenus d’exemple.">
<style>{CSS}</style>
</head>
<body>
<!--
Trace : voir ../reponse.md, section « Trace » (proposition exploratoire ; contenus d’exemple marqués). Source : généré par travail/gen.py et travail/violon.py.
-->
{hidden_defs}
<div class="note-maquette"><div class="cadre"><p>{fr("Maquette : le nom, l’adresse, le téléphone, les horaires, les délais et les tarifs sont des exemples à remplacer.")}</p></div></div>
<header class="tete">
  <div class="cadre">
    <a class="marque" href="#reparer">Atelier Fontanes</a>
    <nav aria-label="Sections"><ul>
      <li><a href="#reparer">Réparer</a></li><li><a href="#louer">Louer</a></li>
      <li><a href="#commander">Commander</a></li><li><a href="#venir">Venir</a></li>
    </ul></nav>
    <a class="btn" href="{TEL_HREF}">{TEL}</a>
  </div>
</header>
<main>
<section class="scene cadre" id="reparer" aria-labelledby="titre-atelier">
  <div class="intro">
    <p class="lieu">8, passage des Tanneurs, Lyon 1<sup>er</sup> <span class="ex">adresse d’exemple</span></p>
    <h1 id="titre-atelier">Atelier Fontanes<span class="sous">violons, altos, violoncelles</span></h1>
    <p class="lead">{fr("On\u00a0les\u00a0règle, on\u00a0les\u00a0répare, on\u00a0les\u00a0loue, et\u00a0on\u00a0en\u00a0fait\u00a0ici, à\u00a0la\u00a0main.")}</p>
    <p class="depot">{fr("Déposez votre instrument sans rendez-vous, du mardi au samedi : on l’écoute devant vous, et le devis est gratuit avant tout travail.")} <span class="ex">exemple</span></p>
    <div class="actions">
      <a class="btn" href="{TEL_HREF}">Appeler l’atelier</a>
      <a class="lien" href="#venir">Adresse et horaires</a>
    </div>
  </div>

  <figure class="plan">
    {plan_svg()}
    <figcaption>{fr("Violon entier, vu de face. Cotes courantes en millimètres.")}</figcaption>
  </figure>

  <div class="diag-tete">
    <h2 id="titre-diag">{fr("Qu’est-ce qui ne va pas ?")}</h2>
    <p class="consigne">{fr("Choisissez ce que vous entendez ou voyez : le numéro renvoie au plan.")}</p>
  </div>
  <ul class="symptomes" aria-labelledby="titre-diag">
{boutons()}
  </ul>
  <div class="fiches" aria-live="polite">
{fiches()}
    <p class="precision">{fr("Tarifs donnés pour un violon ou un alto ; pour un violoncelle, comptez à peu près le double.")} <span class="ex">exemple</span></p>
  </div>
</section>

<section class="louer" id="louer" aria-labelledby="titre-louer">
  <div class="cadre">
    <div class="louer-tete">
      <h2 id="titre-louer">{fr("Louer pour un enfant : la taille suit le bras, pas l’âge")}</h2>
      <p>{fr("Un 1/2 n’est pas la moitié d’un violon : sa caisse mesure 310 mm, contre 356 pour un entier. Mesurez le bras tendu, du cou au creux de la main ; on confirme toujours à l’essai, l’instrument en place.")}</p>
    </div>
    <ol class="tailles" aria-label="Tailles de violon, du plus petit au plus grand">
{tailles()}
    </ol>
    <div class="louer-pied">
      <ul class="conditions">
        <li>{fr("Trois mois minimum, puis au mois ; caution de 150 €.")} <span class="ex">exemple</span></li>
        <li>{fr("Quand l’enfant grandit, on change de taille sans frais.")} <span class="ex">exemple</span></li>
        <li>{fr("Un réglage d’automne compris, au moment où le bois bouge.")} <span class="ex">exemple</span></li>
      </ul>
      <p class="note">{fr("Longueurs de bras et de caisse : repères courants, qui varient d’un fabricant à l’autre. Altos de 33 à 41 cm et violoncelles de 1/4 à 4/4 : demandez à l’atelier.")}</p>
    </div>
  </div>
</section>

<section class="commander" id="commander" aria-labelledby="titre-commander">
  <div class="cadre">
    <div>
      <h2 id="titre-commander">Un instrument fait ici</h2>
      <p>{fr("On choisit ensemble le modèle, le bois et la voix. Le reste prend du temps : chaque étape attend que la précédente soit sèche.")}</p>
      <div class="etiquette-scene" aria-hidden="true">
        <div class="etiquette"><div class="etiquette-in">
          <p class="e1">Atelier Fontanes</p>
          <p class="e2">fecit Lugduni, anno 2026 — n° 31</p>
        </div></div>
      </div>
      <p class="legende">{fr("L’étiquette, collée à l’intérieur de la caisse, se lit par l’ouïe. Texte et numéro d’exemple.")}</p>
    </div>
    <div>
      <ol class="etapes">
        <li><span><strong>Essai</strong> {fr(": vous jouez plusieurs modèles à l’atelier.")}</span><span class="duree">un rendez-vous</span></li>
        <li><span><strong>Bois</strong> {fr(": épicéa pour la table, érable pour le fond, choisis avec vous.")}</span><span class="duree">même rendez-vous</span></li>
        <li><span><strong>Caisse et volute en blanc</strong>, avant tout vernis.</span><span class="duree">environ 5 mois</span></li>
        <li><span><strong>Vernis</strong>, couche après couche, et séchage.</span><span class="duree">environ 2 mois</span></li>
        <li><span><strong>Montage et premier réglage</strong>, avec vous.</span><span class="duree">une séance</span></li>
        <li><span><strong>Second réglage</strong>{fr(", offert, après six mois de jeu.")}</span><span class="duree">six mois après</span></li>
      </ol>
      <ul class="prix-neuf">
        <li><span>Violon</span><strong>à partir de 8 500 €</strong></li>
        <li><span>Alto</span><strong>à partir de 9 500 €</strong></li>
        <li><span>Violoncelle</span><strong>sur devis</strong></li>
      </ul>
      <p class="precision">{fr("Délais et prix d’exemple, à remplacer par ceux de l’atelier.")}</p>
      <p><a class="btn" href="mailto:{MAIL}?subject=Commande%20d%E2%80%99un%20instrument">Demander un rendez-vous d’essai</a></p>
    </div>
  </div>
</section>

<section class="venir" id="venir" aria-labelledby="titre-venir">
  <div class="cadre">
    <div class="venir-grille">
      <div>
        <h2 id="titre-venir">{fr("Venir à l’atelier")}</h2>
        <p class="phrase">{fr("Apportez l’instrument : on l’écoute avant d’y toucher.")}</p>
      </div>
      <div>
        <h3>Adresse <span class="ex">exemple</span></h3>
        <address>8, passage des Tanneurs<br>69001 Lyon</address>
        <p>{fr("Cordes, colophane, sourdines et étuis en vente sur place.")}</p>
        <p><a class="btn" href="{TEL_HREF}">{TEL}</a></p>
        <p><a class="lien" href="mailto:{MAIL}">{MAIL}</a></p>
      </div>
      <div>
        <h3>Horaires <span class="ex">exemple</span></h3>
        <dl class="horaires">
          <dt>Mar. – ven.</dt><dd>9 h 30 – 12 h 30, 14 h – 18 h 30</dd>
          <dt>Samedi</dt><dd>10 h – 17 h</dd>
          <dt>Lundi</dt><dd>sur rendez-vous</dd>
          <dt>Fermé</dt><dd>le dimanche et en août</dd>
        </dl>
      </div>
    </div>
    <footer class="colophon">
      <p>{fr("Atelier Fontanes est un nom d’exemple ; adresse, numéro (plage réservée à la fiction), courriel, horaires, délais et tarifs sont à remplacer.")}</p>
      <p>{fr("Plan du violon dessiné pour ce site. Polices : Libre Caslon Text et IBM Plex, licence SIL OFL 1.1.")}</p>
    </footer>
  </div>
</section>
</main>
<script>{JS}</script>
</body>
</html>
"""


if __name__ == "__main__":
    OUT.write_text(page(), encoding="utf-8")
    print(OUT)
