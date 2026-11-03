"""Logo round 2: brush-ring style (client refs: Luxury 3 + Modern 2).
Builds standalone SVG/HTML for 3 options, rendered by render.js."""
import math, random, pathlib

OUT = pathlib.Path(__file__).parent
FONTS = (OUT.parent / "fonts").resolve()


def brush_ring(cx, cy, R, W, a0, sweep, seed, n_bristle=22):
    """Return SVG path data for a brush-stroke ring (body + dry bristles)."""
    rnd = random.Random(seed)
    N = 240
    def w_at(t):
        head = min(1.0, t / 0.05) ** 0.5
        tail = (1 - t) ** 0.55
        wob = 1 + 0.06 * math.sin(t * 19 + seed) + 0.04 * math.sin(t * 41)
        return W * head * tail * wob
    outer, inner = [], []
    for i in range(N + 1):
        t = i / N
        a = math.radians(a0 + sweep * t)
        w = w_at(t) * 0.86
        r = R + 2.5 * math.sin(t * 7 + seed)
        outer.append((cx + (r + w / 2) * math.cos(a), cy + (r + w / 2) * math.sin(a)))
        inner.append((cx + (r - w / 2) * math.cos(a), cy + (r - w / 2) * math.sin(a)))
    pts = outer + inner[::-1]
    body = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts) + "Z"
    # bristles: thin arcs that run past the body into the dry tail
    bristles = []
    for k in range(n_bristle):
        off = rnd.uniform(-0.5, 0.5)
        t1 = rnd.uniform(0.0, 0.08)
        t2 = rnd.uniform(0.80, 1.0)
        sw = rnd.uniform(1.2, 4.2)
        seg = []
        for i in range(60 + 1):
            t = t1 + (t2 - t1) * i / 60
            a = math.radians(a0 + sweep * t)
            r = R + 2.5 * math.sin(t * 7 + seed) + off * W * (1 - t) ** 0.4
            seg.append((cx + r * math.cos(a), cy + r * math.sin(a)))
        d = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in seg)
        bristles.append((d, sw, rnd.uniform(0.45, 0.95)))
    return body, bristles


GOLD = [("0", "#7A5518"), (".22", "#F7E6A6"), (".42", "#C99A3E"), (".6", "#FFF1C2"), (".8", "#A77A2B"), ("1", "#E9C877")]
SILVER = [("0", "#5E6064"), (".22", "#F5F6F8"), (".42", "#9EA1A6"), (".6", "#FFFFFF"), (".8", "#6E7176"), ("1", "#D9DBDF")]


def grad(id_, stops, x1=0, y1=0, x2=1200, y2=1200):
    s = "".join(f'<stop offset="{o}" stop-color="{c}"/>' for o, c in stops)
    return f'<linearGradient id="{id_}" gradientUnits="userSpaceOnUse" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}">{s}</linearGradient>'


_mid = [0]
def ring_svg(body, bristles, fill, gaps=()):
    _mid[0] += 1; m = f"m{_mid[0]}"
    b = "".join(f'<path d="{d}" fill="none" stroke="#fff" stroke-width="{sw:.1f}" stroke-linecap="round" opacity="{op:.2f}"/>' for d, sw, op in bristles)
    g = "".join(f'<path d="{d}" fill="none" stroke="#000" stroke-width="{sw:.1f}" stroke-linecap="round"/>' for d, sw in gaps)
    return (f'<mask id="{m}" maskUnits="userSpaceOnUse" x="0" y="0" width="1200" height="1200"><path d="{body}" fill="#fff"/>{b}{g}</mask>'
            f'<g filter="url(#rough)"><rect width="1200" height="1200" fill="{fill}" mask="url(#{m})"/></g>')


def gap_lines(cx, cy, R, W, a0, sweep, seed, n=10):
    rnd = random.Random(seed + 99); out = []
    for k in range(n):
        off = rnd.uniform(-0.38, 0.38); t1 = rnd.uniform(0.25, 0.7); t2 = min(1.0, t1 + rnd.uniform(0.15, 0.5))
        seg = []
        for i in range(41):
            t = t1 + (t2 - t1) * i / 40; a = math.radians(a0 + sweep * t)
            r = R + 2.5 * math.sin(t * 7 + seed) + off * W * (1 - t) ** 0.4
            seg.append((cx + r * math.cos(a), cy + r * math.sin(a)))
        out.append(("M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in seg), rnd.uniform(1.0, 3.2)))
    return out


FONT_CSS = f"""
@font-face{{font-family:Charm;font-weight:700;src:url(file://{FONTS}/Charm-Bold.ttf)}}
@font-face{{font-family:Charm;font-weight:400;src:url(file://{FONTS}/Charm-Regular.ttf)}}
@font-face{{font-family:Kanit;font-weight:700;src:url(file://{FONTS}/Kanit-Bold.ttf)}}
@font-face{{font-family:Kanit;font-weight:600;src:url(file://{FONTS}/Kanit-SemiBold.ttf)}}
@font-face{{font-family:Kanit;font-weight:500;src:url(file://{FONTS}/Kanit-Medium.ttf)}}
@font-face{{font-family:Charmonman;font-weight:700;src:url(file://{FONTS}/Charmonman-Bold.ttf)}}
@font-face{{font-family:Cinzel;src:url(file://{FONTS}/Cinzel.ttf)}}
"""

DEFS_COMMON = """
<filter id="rough" x="-10%" y="-10%" width="120%" height="120%">
  <feTurbulence type="fractalNoise" baseFrequency="0.035 0.09" numOctaves="2" seed="7" result="n"/>
  <feDisplacementMap in="SourceGraphic" in2="n" scale="7"/>
</filter>
<filter id="glowG" x="-20%" y="-20%" width="140%" height="140%">
  <feGaussianBlur in="SourceAlpha" stdDeviation="14" result="b"/>
  <feFlood flood-color="#E2B65A" flood-opacity=".35"/><feComposite in2="b" operator="in" result="g"/>
  <feMerge><feMergeNode in="g"/><feMergeNode in="SourceGraphic"/></feMerge>
</filter>
<filter id="glowS" x="-20%" y="-20%" width="140%" height="140%">
  <feGaussianBlur in="SourceAlpha" stdDeviation="12" result="b"/>
  <feFlood flood-color="#FFFFFF" flood-opacity=".22"/><feComposite in2="b" operator="in" result="g"/>
  <feMerge><feMergeNode in="g"/><feMergeNode in="SourceGraphic"/></feMerge>
</filter>
<filter id="emboss" x="-5%" y="-5%" width="110%" height="110%">
  <feDropShadow dx="0" dy="3" stdDeviation="2.5" flood-color="#000" flood-opacity=".75"/>
</filter>
<radialGradient id="bg" cx="50%" cy="45%" r="70%"><stop offset="0" stop-color="#26221C"/><stop offset=".6" stop-color="#110F0C"/><stop offset="1" stop-color="#070605"/></radialGradient>
<filter id="grain"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="2" seed="3"/><feColorMatrix values="0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 .05 0"/></filter>
"""


def page(svg_inner, extra_defs, bg=True):
    bgl = '<rect width="1200" height="1200" fill="url(#bg)"/><rect width="1200" height="1200" filter="url(#grain)"/>' if bg else ""
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{FONT_CSS}
html,body{{margin:0;background:{'#000' if bg else 'transparent'}}}svg{{display:block}}</style></head><body>
<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="1200" viewBox="0 0 1200 1200"><defs>{DEFS_COMMON}{extra_defs}</defs>{bgl}{svg_inner}</svg></body></html>"""


def _bez(p0, p1, p2, p3, n):
    out = []
    for i in range(n):
        t = i / n; u = 1 - t
        out.append((u**3*p0[0]+3*u*u*t*p1[0]+3*u*t*t*p2[0]+t**3*p3[0], u**3*p0[1]+3*u*u*t*p1[1]+3*u*t*t*p2[1]+t**3*p3[1]))
    return out


def _arch_pts(l, r, bot, sh, peak, ctrl):
    """Sample a Thai arch (ซุ้ม) outline: straight sides + ogee top."""
    cx = (l + r) / 2; pts = []
    pts += [(l, bot - (bot - sh) * i / 20) for i in range(20)]
    pts += _bez((l, sh), (l, sh - ctrl), (cx - (r - l) * .15, sh - ctrl * .9), (cx, peak), 30)
    pts += _bez((cx, peak), (cx + (r - l) * .15, sh - ctrl * .9), (r, sh - ctrl), (r, sh), 30)
    pts += [(r, sh + (bot - sh) * i / 20) for i in range(21)]
    return pts


def _arch_d(*a):
    l, r, bot, sh, peak, ctrl = a; cx = (l + r) / 2
    return (f"M{l},{bot} L{l},{sh} C{l},{sh-ctrl} {cx-(r-l)*.15},{sh-ctrl*.9} {cx},{peak} "
            f"C{cx+(r-l)*.15},{sh-ctrl*.9} {r},{sh-ctrl} {r},{sh} L{r},{bot} Z")


# ---------- A · กรอบพระทรงซุ้ม (ทอง) + KT ข้างใน
def logo_A(bg=True):
    outer = (430, 770, 760, 430, 175, 120)
    mid = (452, 748, 738, 436, 210, 112)
    inner = (474, 726, 716, 442, 245, 104)
    beads = _arch_pts(463, 737, 727, 439, 228, 108)[::3]
    bead_svg = "".join(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4.2"/>' for x, y in beads)
    inner_svg = f"""
<g filter="url(#glowG)">
  <path d="{_arch_d(*outer)} {_arch_d(*inner)}" fill="url(#gA)" fill-rule="evenodd"/>
  <path d="{_arch_d(*mid)}" fill="none" stroke="#3A2A10" stroke-width="18" opacity=".55"/>
  <g fill="url(#gA)">{bead_svg}</g>
  <path d="{_arch_d(*inner)}" fill="url(#velvet)"/>
  <path d="{_arch_d(*inner)}" fill="none" stroke="url(#gA)" stroke-width="2"/>
  <!-- ห่วง + ยอดบัว -->
  <circle cx="600" cy="128" r="24" fill="none" stroke="url(#gA)" stroke-width="9"/>
  <path d="M600 150 C588 162 586 172 600 182 C614 172 612 162 600 150Z" fill="url(#gA)"/>
  <!-- ฐาน -->
  <path d="M410 760 H790 L770 792 H430Z" fill="url(#gA)"/>
  <rect x="440" y="798" width="320" height="6" rx="3" fill="url(#gA)"/>
  <!-- กนกหัวไหล่ -->
  <g fill="none" stroke="url(#gA)" stroke-width="5" stroke-linecap="round">
    <path d="M430 420 C395 410 385 375 405 360 C420 350 432 365 422 375"/>
    <path d="M770 420 C805 410 815 375 795 360 C780 350 768 365 778 375"/>
  </g>
</g>
<g filter="url(#emboss)" fill="url(#gAt)" text-anchor="middle">
  <text x="600" y="610" font-family="Cinzel" font-size="168" letter-spacing="-6">KT</text>
  <path d="M600 650 l8 9 -8 9 -8 -9z"/>
  <text x="600" y="948" font-family="Charmonman" font-weight="700" font-size="104">กรอบพระไทยแลนด์</text>
</g>
<text x="600" y="1015" text-anchor="middle" font-family="Cinzel" font-size="28" letter-spacing="11" fill="#D8B66A">THAI AMULET FRAMES</text>
"""
    vel = '<radialGradient id="velvet" cx="50%" cy="45%" r="60%"><stop offset="0" stop-color="#2A241C"/><stop offset="1" stop-color="#0A0806"/></radialGradient>'
    return page(inner_svg, grad("gA", GOLD, 300, 100, 900, 820) + grad("gAt", GOLD, 0, 450, 0, 960) + vel, bg)


# ---------- B · กรอบพระทรงหยดน้ำ (เงิน ลายเส้น) + KT ข้างใน
def logo_B(bg=True):
    drop = "M600 230 C705 285 770 410 770 530 C770 665 695 750 600 750 C505 750 430 665 430 530 C430 410 495 285 600 230Z"
    sc = lambda k: f'transform="translate(600 520) scale({k}) translate(-600 -520)"'
    inner_svg = f"""
<g filter="url(#glowS)">
  <path d="{drop}" fill="none" stroke="url(#gB)" stroke-width="16"/>
  <path d="{drop}" {sc(.9)} fill="none" stroke="url(#gB)" stroke-width="3.3"/>
  <path d="{drop}" {sc(.84)} fill="none" stroke="url(#gB)" stroke-width="1.6" stroke-dasharray="2 9" stroke-linecap="round"/>
  <circle cx="600" cy="180" r="27" fill="none" stroke="url(#gB)" stroke-width="10"/>
  <rect x="588" y="203" width="24" height="26" rx="5" fill="url(#gB)"/>
  <path d="M600 742 l14 18 -14 18 -14 -18z" fill="url(#gB)"/>
</g>
<g filter="url(#emboss)" fill="url(#gBt)" text-anchor="middle" font-family="Kanit">
  <text x="600" y="590" font-size="176" font-weight="700" letter-spacing="2">KT</text>
</g>
<g filter="url(#emboss)" fill="url(#gBn)" text-anchor="middle" font-family="Kanit">
  <text x="600" y="905" font-size="104" font-weight="700" letter-spacing="2">กรอบพระไทยแลนด์</text>
</g>
<text x="600" y="975" text-anchor="middle" font-family="Cinzel" font-size="28" letter-spacing="11" fill="#C9CBD0">THAI AMULET FRAMES</text>
"""
    return page(inner_svg, grad("gB", SILVER, 300, 150, 900, 800) + grad("gBt", SILVER, 0, 440, 0, 600) + grad("gBn", SILVER, 0, 800, 0, 915), bg)


# ---------- C · hybrid: gold ring with KT monogram, Thai name below (Modern 2 layout in gold)
def logo_C(bg=True):
    body, br = brush_ring(600, 430, 250, 48, 205, 325, seed=21, n_bristle=18)
    inner = f"""
<g filter="url(#glowG)">{ring_svg(body, br, 'url(#gC)', gap_lines(600,430,250,48,205,325,21,8))}</g>
<g filter="url(#emboss)" fill="url(#gCt)" text-anchor="middle">
  <text x="600" y="500" font-family="Cinzel" font-size="210" letter-spacing="-6">KT</text>
  <path d="M600 548 l9 10 -9 10 -9 -10z"/>
  <text x="600" y="825" font-family="Kanit" font-weight="600" font-size="112" letter-spacing="3">กรอบพระไทยแลนด์</text>
</g>
<text x="600" y="900" text-anchor="middle" font-family="Cinzel" font-size="32" letter-spacing="12" fill="#D8B66A">THAI AMULET FRAMES</text>
"""
    return page(inner, grad("gC", GOLD) + grad("gCt", GOLD, 0, 280, 0, 860), bg)


if __name__ == "__main__":
    for name, fn in [("A", logo_A), ("B", logo_B), ("C", logo_C)]:
        (OUT / f"logo-{name}.html").write_text(fn(True))
        (OUT / f"logo-{name}-transparent.html").write_text(fn(False))
    print("ok")
