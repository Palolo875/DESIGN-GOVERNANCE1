"""Génère les parties SVG du violon (plan schématique, unités en mm, axe x=0)."""

BODY_TOP = 237  # haut de la caisse (mm depuis le haut de la volute)

# Demi-contour droit de la caisse, en coordonnées de caisse (y=0 en haut, 356 en bas)
HALF = [
    ((0, 0), (30, 0), (70, 8), (80, 40)),
    ((80, 40), (88, 64), (85, 96), (75, 118)),
    ((75, 118), (73, 124), (77, 130), (83, 134)),
    ((83, 134), (66, 139), (57, 152), (57, 170)),
    ((57, 170), (57, 189), (66, 201), (85, 206)),
    ((85, 206), (80, 212), (82, 218), (89, 227)),
    ((89, 227), (103, 250), (107, 296), (95, 326)),
    ((95, 326), (82, 350), (42, 357), (0, 356)),
]


def _f(v):
    return f"{v:.1f}".rstrip("0").rstrip(".")


def outline(scale=1.0, dy=BODY_TOP, cy=178):
    """Contour fermé complet ; scale autour du centre de caisse (pour le filet)."""
    def t(p):
        x, y = p
        return (x * scale, (y - cy) * scale + cy + dy)

    segs = [tuple(t(p) for p in s) for s in HALF]
    d = f"M{_f(segs[0][0][0])},{_f(segs[0][0][1])}"
    for _, c1, c2, e in segs:
        d += f" C{_f(c1[0])},{_f(c1[1])} {_f(c2[0])},{_f(c2[1])} {_f(e[0])},{_f(e[1])}"
    # côté gauche : segments inversés et miroir
    for s in reversed(segs):
        p0, c1, c2, e = s
        d += f" C{_f(-c2[0])},{_f(c2[1])} {_f(-c1[0])},{_f(c1[1])} {_f(-p0[0])},{_f(p0[1])}"
    return d + " Z"


def fhole(side=1):
    s = side
    y = BODY_TOP
    stem = (f"M{_f(23*s)},{_f(y+151)} C{_f(25*s)},{_f(y+176)} {_f(52*s)},{_f(y+190)} {_f(49*s)},{_f(y+227)}")
    return (
        f'<path d="{stem}" fill="none" stroke="var(--ebene)" stroke-width="3.6" stroke-linecap="round"/>'
        f'<circle cx="{_f(22*s)}" cy="{y+148}" r="4.6" fill="var(--ebene)"/>'
        f'<circle cx="{_f(51*s)}" cy="{y+231}" r="5.6" fill="var(--ebene)"/>'
        f'<path d="M{_f(33*s)},{y+188} l{_f(6*s)},-3 M{_f(38*s)},{y+197} l{_f(6*s)},3" stroke="var(--ebene)" stroke-width="1.4"/>'
    )


def grain():
    lines = []
    x = -108
    i = 0
    while x <= 108:
        w = 0.5 if i % 3 else 0.8
        lines.append(f'<line x1="{_f(x)}" y1="{BODY_TOP}" x2="{_f(x + (0.6 if i % 2 else -0.4))}" y2="{BODY_TOP+356}" stroke-width="{w}"/>')
        x += 3.1 + (i % 4) * 0.6
        i += 1
    return "".join(lines)


def violin_parts(idp="v"):
    """Le violon nu (sans cotes ni repères)."""
    y = BODY_TOP
    body = outline()
    purf = outline(scale=0.955)
    pegs = []
    for side, py in ((-1, 63), (1, 74), (-1, 90), (1, 99)):
        s = side
        pegs.append(
            f'<path d="M{_f(11*s)},{py-2.2} L{_f(34*s)},{py-2.6} L{_f(34*s)},{py+2.6} L{_f(11*s)},{py+2.2} Z" fill="var(--ebene)"/>'
            f'<ellipse cx="{_f(39*s)}" cy="{py}" rx="6.5" ry="8.5" fill="var(--ebene)"/>'
        )
    return f"""
  <defs>
    <radialGradient id="{idp}-vernis" cx="0.5" cy="0.62" r="0.62">
      <stop offset="0" stop-color="var(--vernis-clair)"/>
      <stop offset="0.7" stop-color="var(--vernis)"/>
      <stop offset="1" stop-color="var(--vernis-fonce)"/>
    </radialGradient>
    <clipPath id="{idp}-caisse"><path d="{body}"/></clipPath>
  </defs>
  <g class="instrument">
    <!-- volute et chevillier -->
    <path d="M-12,46 C-13,38 -21,33 -21,21 C-21,9 -12,1 0,1 C12,1 21,9 21,21 C21,33 13,38 12,46 Z" fill="url(#{idp}-vernis)" stroke="var(--ebene)" stroke-width="1.1"/>
    <circle cx="-12.5" cy="22" r="5.2" fill="none" stroke="var(--vernis-fonce)" stroke-width="1.2"/>
    <circle cx="12.5" cy="22" r="5.2" fill="none" stroke="var(--vernis-fonce)" stroke-width="1.2"/>
    <circle cx="-12.5" cy="22" r="1.6" fill="var(--vernis-fonce)"/><circle cx="12.5" cy="22" r="1.6" fill="var(--vernis-fonce)"/>
    <path d="M0,4 L0,44 M-4,6 C-5,20 -5,34 -4,44 M4,6 C5,20 5,34 4,44" fill="none" stroke="var(--vernis-fonce)" stroke-width="0.9"/>
    {''.join(pegs)}
    <path d="M-11,44 L-12.5,108 L12.5,108 L11,44 Z" fill="url(#{idp}-vernis)" stroke="var(--ebene)" stroke-width="1.1"/>
    <path d="M-7,50 L-6,104 L6,104 L7,50 Z" fill="var(--ebene)" opacity="0.85"/>
    <!-- caisse -->
    <path d="{body}" fill="url(#{idp}-vernis)"/>
    <g clip-path="url(#{idp}-caisse)" stroke="var(--vernis-fonce)" opacity="0.28">{grain()}</g>
    <path d="{purf}" fill="none" stroke="var(--ebene)" stroke-width="1" opacity="0.7"/>
    <path d="{body}" fill="none" stroke="var(--ebene)" stroke-width="1.3"/>
    {fhole(1)}{fhole(-1)}
    <!-- touche -->
    <path d="M-12,107 L12,107 L21,{y+137} Q0,{y+143} -21,{y+137} Z" fill="var(--ebene)"/>
    <rect x="-12.5" y="104" width="25" height="4" fill="var(--erable)"/>
    <!-- chevalet -->
    <path d="M-21,{y+197} L-20,{y+192} Q0,{y+188} 20,{y+192} L21,{y+197} Z" fill="var(--erable)" stroke="var(--ebene)" stroke-width="0.8"/>
    <!-- cordier et mentonnière -->
    <path d="M-20,{y+252} Q0,{y+246} 20,{y+252} L11,{y+336} Q0,{y+342} -11,{y+336} Z" fill="var(--ebene)"/>
    <path d="M-58,{y+322} C-60,{y+304} -38,{y+298} -25,{y+306} C-16,{y+313} -17,{y+336} -31,{y+341} C-45,{y+346} -57,{y+338} -58,{y+322} Z" fill="var(--ebene)" opacity="0.8"/>
    <circle cx="0" cy="{y+353}" r="3.4" fill="var(--ebene)"/>
    <!-- cordes -->
    <g stroke="var(--corde)" stroke-width="0.7">
      <line x1="-7.5" y1="106" x2="-16" y2="{y+190}"/><line x1="-2.5" y1="106" x2="-5.4" y2="{y+189}"/>
      <line x1="2.5" y1="106" x2="5.4" y2="{y+189}"/><line x1="7.5" y1="106" x2="16" y2="{y+190}"/>
      <line x1="-16" y1="{y+190}" x2="-12" y2="{y+251}"/><line x1="-5.4" y1="{y+189}" x2="-4" y2="{y+249}"/>
      <line x1="5.4" y1="{y+189}" x2="4" y2="{y+249}"/><line x1="16" y1="{y+190}" x2="12" y2="{y+251}"/>
    </g>
  </g>"""


if __name__ == "__main__":
    print(outline())
