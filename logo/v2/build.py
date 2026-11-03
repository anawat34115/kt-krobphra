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


# ---------- A · Luxury 3 adaptation: gold brush ring + calligraphic Thai + red KT seal
def logo_A(bg=True):
    body, br = brush_ring(600, 520, 330, 74, 118, 318, seed=3)
    inner = f"""
<g filter="url(#glowG)">{ring_svg(body, br, 'url(#gA)', gap_lines(600,520,330,74,118,318,3,14))}</g>
<g filter="url(#emboss)" fill="url(#gAt)" font-family="Charmonman" font-weight="700" text-anchor="middle">
  <text x="585" y="505" font-size="150">กรอบพระ</text>
  <text x="625" y="640" font-size="100">ไทยแลนด์</text>
</g>
<g transform="translate(845 760) rotate(-4)">
  <rect x="-30" y="-30" width="60" height="60" rx="7" fill="#A3241B"/>
  <rect x="-25" y="-25" width="50" height="50" rx="4" fill="none" stroke="#F3D9C4" stroke-width="1.6" opacity=".8"/>
  <text x="0" y="11" text-anchor="middle" font-family="Cinzel" font-size="30" fill="#F7E4D2">KT</text>
</g>
<text x="600" y="955" text-anchor="middle" font-family="Cinzel" font-size="34" letter-spacing="9" fill="url(#gAt)">KT · THAI AMULET FRAMES</text>
<g fill="#C99A3E"><path d="M600 990 l7 8 -7 8 -7 -8z"/><rect x="470" y="997" width="105" height="1.5"/><rect x="625" y="997" width="105" height="1.5"/></g>
"""
    return page(inner, grad("gA", GOLD) + grad("gAt", GOLD, 0, 300, 0, 1000), bg)


# ---------- B · Modern 2 adaptation: chrome brush ring + bold sans Thai + diamond
def logo_B(bg=True):
    body, br = brush_ring(600, 540, 345, 46, 200, 330, seed=11, n_bristle=16)
    inner = f"""
<g filter="url(#glowS)">{ring_svg(body, br, 'url(#gB)', gap_lines(600,540,345,46,200,330,11,8))}</g>
<g filter="url(#emboss)" fill="url(#gBt)" font-family="Kanit" text-anchor="middle">
  <text x="600" y="530" font-size="136" font-weight="700" letter-spacing="1">กรอบพระ</text>
  <text x="600" y="640" font-size="86" font-weight="500" letter-spacing="4">ไทยแลนด์</text>
</g>
<text x="600" y="730" text-anchor="middle" font-family="Cinzel" font-size="22" letter-spacing="7" fill="#C9CBD0">KT · THAI AMULET FRAMES</text>
<g transform="translate(600 886)" filter="url(#glowS)"><path d="M0 -30 L18 0 L0 30 L-18 0Z" fill="#111" /><path d="M0 -24 L13 0 L0 24 L-13 0Z" fill="url(#gB)"/></g>
"""
    return page(inner, grad("gB", SILVER) + grad("gBt", SILVER, 0, 380, 0, 680), bg)


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
