"""Génère la coupe schématique d'un violon au droit du chevalet (unités : mm)."""
import math, sys
W = 62.0      # demi-largeur de la table au droit du chevalet (approché)
H_T = 16.0    # voûte de table
H_F = 15.0    # voûte de fond
T_T = 2.8     # épaisseur table
T_F = 3.6     # épaisseur fond
RIB = 31.0    # hauteur d'éclisse
OV = 2.5      # débord des tables sur les éclisses
def h(x, H):  # profil de voûte (approché), nul au bord
    u = min(abs(x) / W, 1.0)
    return H * (math.cos(math.pi * u / 2) ** 1.6)
def f(v): return f"{v:.2f}"
def pts(fn, x0, x1, n=60):
    return [(x0 + (x1 - x0) * i / n, fn(x0 + (x1 - x0) * i / n)) for i in range(n + 1)]
def poly(points): return " ".join(("M" if i == 0 else "L") + f(x) + " " + f(y) for i, (x, y) in enumerate(points))
def plate(x0, x1, outer, inner):
    top = pts(outer, x0, x1); bot = pts(inner, x1, x0)
    return poly(top + bot) + " Z"
t_out = lambda x: -T_T - h(x, H_T)
t_in = lambda x: -h(x, H_T)
b_in = lambda x: RIB + h(x, H_F)
b_out = lambda x: RIB + T_F + h(x, H_F)
OUIE = (29.0, 35.0)  # ouïes coupées par le plan (approché)
table = " ".join([plate(-W, -OUIE[1], t_out, t_in), plate(-OUIE[0], OUIE[0], t_out, t_in), plate(OUIE[1], W, t_out, t_in)])
fond = plate(-W, W, b_out, b_in)
rx = W - OV
eclisses = f"M{f(-rx)} 0 h1.2 v{RIB} h-1.2 Z M{f(rx-1.2)} 0 h1.2 v{RIB} h-1.2 Z"
# contre-éclisses (haut et bas, des deux côtés)
ce = []
for s in (-1, 1):
    xi = s * (rx - 1.2) if s > 0 else -rx + 1.2
    d = -s  # vers l'intérieur
    ce.append(f"M{f(xi)} {f(0.2)} l{f(d*2.2)} 0 l{f(-d*2.2)} 6.5 Z")
    ce.append(f"M{f(xi)} {f(RIB-0.2)} l{f(d*2.2)} 0 l{f(-d*2.2)} -6.5 Z")
contre = " ".join(ce)
# barre d'harmonie sous le pied gauche (sol)
bx, bw, bh = -17.0, 5.2, 11.0
barre = f"M{f(bx-bw/2)} {f(t_in(bx-bw/2))} L{f(bx+bw/2)} {f(t_in(bx+bw/2))} L{f(bx+bw/2)} {f(t_in(bx)+bh)} L{f(bx-bw/2)} {f(t_in(bx)+bh)} Z"
# âme sous le pied droit (mi), Ø 6
ax, aw = 17.0, 6.0
ame = f"M{f(ax-aw/2)} {f(t_in(ax-aw/2))} L{f(ax+aw/2)} {f(t_in(ax+aw/2))} L{f(ax+aw/2)} {f(b_in(ax+aw/2))} L{f(ax-aw/2)} {f(b_in(ax-aw/2))} Z"
# chevalet : pieds de 13 à 20,5 mm, hauteur ~33 mm, haut en arc
fy = lambda x: t_out(x)
top_c = t_out(0) - 33.0
R = 42.0  # rayon de l'arc supérieur (approché)
def arc_y(x): return top_c + (R - math.sqrt(R * R - x * x))
legL = [(-20.5, fy(-20.5)), (-13.0, fy(-13.0))]
legR = [(13.0, fy(13.0)), (20.5, fy(20.5))]
che = []
che.append(f"M{f(-20.5)} {f(fy(-20.5))}")
che.append(f"L{f(-13.0)} {f(fy(-13.0))}")
che.append(f"C{f(-11)} {f(fy(-13)-5)} {f(-6)} {f(fy(-13)-7)} {f(-4)} {f(fy(-13)-6.5)}")  # entre les pieds
che.append(f"Q0 {f(fy(0)-6)} 4 {f(fy(13)-6.5)}")
che.append(f"C6 {f(fy(13)-7)} 11 {f(fy(13)-5)} 13 {f(fy(13))}")
che.append(f"L20.5 {f(fy(20.5))}")
che.append(f"C19.5 {f(fy(20.5)-8)} 17 {f(fy(20.5)-12)} 17.2 {f(fy(20.5)-16)}")  # taille (reins)
che.append(f"C19 {f(fy(20.5)-19)} 20.5 {f(arc_y(20)+4)} 20.6 {f(arc_y(20.6))}")
xs = [20.6 - i * 41.2 / 30 for i in range(31)]
che.append(" ".join(f"L{f(x)} {f(arc_y(x))}" for x in xs))
che.append(f"C-20.5 {f(arc_y(20)+4)} -19 {f(fy(-20.5)-19)} -17.2 {f(fy(-20.5)-16)}")
che.append(f"C-17 {f(fy(-20.5)-12)} -19.5 {f(fy(-20.5)-8)} -20.5 {f(fy(-20.5))} Z")
# cœur (évidement central)
cy = fy(0) - 20
coeur = f"M0 {f(cy+3)} C-3.5 {f(cy)} -3 {f(cy-4.5)} 0 {f(cy-3)} C3 {f(cy-4.5)} 3.5 {f(cy)} 0 {f(cy+3)} Z"
chevalet = " ".join(che) + " " + coeur
cordes = [(-16.5, "sol", 0.9), (-5.5, "ré", 0.8), (5.5, "la", 0.7), (16.5, "mi", 0.5)]
def cordes_svg():
    out = []
    for x, n, r in cordes:
        y = arc_y(x) - r * 1.1
        out.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(r*1.6)}"/>')
    return "".join(out)
# repères : (numéro, partie, position du repère, point visé)
reps = [
    (1, "cordes", (30, -66), (16.5, arc_y(16.5) - 1.5)),
    (2, "chevalet", (-36, -54), (-10, fy(0) - 22)),
    (3, "table", (-74, -20), (-46, t_out(-46) + 1.2)),
    (4, "ouie", (52, -34), (32, t_out(32) + 1.4)),
    (5, "barre", (-74, 8), (-17, t_in(-17) + 6)),
    (6, "ame", (74, 6), (20, 12)),
    (7, "eclisse", (-74, 30), (-rx + 0.6, 22)),
    (8, "contre", (74, 30), (rx - 2.2, 26)),
    (9, "fond", (36, 60), (30, b_out(30) - 1.5)),
]
def reperes_svg():
    out = []
    for n, part, (mx, my), (tx, ty) in reps:
        dx, dy = tx - mx, ty - my
        d = math.hypot(dx, dy); r = 4.3
        sx, sy = mx + dx / d * r, my + dy / d * r
        out.append(f'<g class="rep" data-rep="{part}"><line x1="{f(sx)}" y1="{f(sy)}" x2="{f(tx)}" y2="{f(ty)}"/>'
                   f'<circle class="pt" cx="{f(tx)}" cy="{f(ty)}" r="0.9"/>'
                   f'<circle class="bulle" cx="{f(mx)}" cy="{f(my)}" r="{r}"/>'
                   f'<text x="{f(mx)}" y="{f(my)}" dy="0.36em">{n}</text></g>')
    return "".join(out)
svg = f'''<svg class="coupe" viewBox="-82 -74 164 142" role="img" aria-labelledby="coupe-titre coupe-desc" xmlns="http://www.w3.org/2000/svg">
<title id="coupe-titre">Coupe schématique d’un violon au droit du chevalet</title>
<desc id="coupe-desc">Vue en coupe : les quatre cordes passent sur le chevalet, posé sur la table voûtée en épicéa. Sous le pied gauche, la barre d’harmonie est collée sous la table ; sous le pied droit, l’âme, une baguette d’épicéa de six millimètres, tient la table et le fond sans colle. Les éclisses en érable relient la table et le fond.</desc>
<g class="bois">
<path class="part fond" data-part="fond" d="{fond}"/>
<path class="part eclisse" data-part="eclisse" d="{eclisses}"/>
<path class="part contre" data-part="contre" d="{contre}"/>
<path class="part table" data-part="table" d="{table}"/>
<path class="part barre" data-part="barre" d="{barre}"/>
<path class="part ame" data-part="ame" d="{ame}"/>
<path class="part chevalet" data-part="chevalet" d="{chevalet}" fill-rule="evenodd"/>
<g class="part cordes" data-part="cordes">{cordes_svg()}</g>
<path class="part ouie" data-part="ouie" d="M{f(-OUIE[1])} {f(t_out(-OUIE[1]))} L{f(-OUIE[0])} {f(t_out(-OUIE[0]))} M{f(OUIE[0])} {f(t_out(OUIE[0]))} L{f(OUIE[1])} {f(t_out(OUIE[1]))}"/>
</g>
<g class="reperes">{reperes_svg()}</g>
</svg>'''
sys.stdout.write(svg)
