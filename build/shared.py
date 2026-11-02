# Shared content + SVG illustrations for the 3 KT drafts.

SHOP = {
    "name": "KT กรอบพระไทยแลนด์",
    "tag": "ทุกงานซ่อม ลายสั่งทำ โดยทีมช่างทองหลวง",
    "addr": "1324/2 ต.ตลาดกระทุ่มแบน อ.กระทุ่มแบน จ.สมุทรสาคร 74110",
    "store": "ตี๋เล็กเลี่ยมพระ ตลาดกระทุ่มแบน",
    "tel2": "098 793 9353",
    "tel3": "062 662 6459",
    "tel3_href": "tel:0626626459",
    "tel2_href": "tel:0987939353",
    "hours": "เปิดทุกวัน 08:00–20:00 น.",
    "fb2": "https://www.facebook.com/tlr168",
    "gmaps": "https://maps.app.goo.gl/PxamyNC1pdzEWy1V8",
    "services": "รับสั่งทำ ซื้อ ซ่อม กรอบพระ ทอง เงิน นาก พลาสติก และเครื่องประดับทุกชนิด",
    "tel": "062 589 9383",
    "tel_href": "tel:0625899383",
    "fb": "https://www.facebook.com/krobphrathailand",
    "chat": "https://m.me/krobphrathailand",
    "shopee": "https://shopee.co.th/lhim5555",
    "tiktok": "https://www.tiktok.com/@lhimbing",
    "map_embed": "https://maps.google.com/maps?q=13.6534902,100.2648441&z=17&output=embed",
}

CATS = [
    ("tear", "g", "กรอบทอง", "งานทองตามพิมพ์พระ ขึ้นงานตามงบที่ตั้งไว้"),
    ("round", "s", "กรอบเงิน", "กรอบเงินลายสวย ใส่ได้ทุกวัน"),
    ("sema", "n", "กรอบนาก", "สีนากอมชมพู งานละเอียดแบบช่างโบราณ"),
    ("arch", "p", "กรอบพลาสติกกันน้ำ", "เลี่ยมกันน้ำ ทนทาน ราคาเข้าถึงง่าย"),
]

STEPS = [
    ("ส่งรูปพระ", "ถ่ายรูปพระด้านหน้า-หลัง แล้วส่งทางแชท Facebook หรือ TikTok บอกงบที่ตั้งไว้ได้เลย"),
    ("ช่างประเมินราคา", "ช่างดูพิมพ์และขนาด แจ้งราคา ลาย และระยะเวลาให้ก่อนเริ่มงาน ขึ้นงานตามงบได้"),
    ("ช่างลงมือทำ", "มาส่งพระที่หน้าร้าน หรือส่งพระทางไปรษณีย์ ช่างวัดขนาดแล้วส่งกลับให้ถึงบ้าน"),
]

GALLERY = [("arch", "g"), ("tear", "n"), ("round", "s"), ("sema", "g"), ("arch", "p"), ("round", "g")]

PH = "ภาพวาดตัวอย่าง · รอรูปจริงจากร้าน"


def svg_defs():
    """Gradients + one <symbol> per frame shape and metal."""
    shapes = {
        "arch": "M40 250 L40 96 Q40 26 100 26 Q160 26 160 96 L160 250 Z",
        "tear": "M100 22 C146 84 170 150 166 196 Q160 250 100 250 Q40 250 34 196 C30 150 54 84 100 22 Z",
        "round": "M100 46 A102 102 0 1 1 99.9 46 Z",
        "sema": "M100 24 Q150 46 164 116 Q172 184 140 250 L60 250 Q28 184 36 116 Q50 46 100 24 Z",
    }
    # round: circle centered (100,148) r=102 -> use circle element instead of path
    out = ['<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>',
           '<linearGradient id="mg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#F7E6A8"/><stop offset=".35" stop-color="#D1A24A"/><stop offset=".62" stop-color="#8E6526"/><stop offset="1" stop-color="#E8CB80"/></linearGradient>',
           '<linearGradient id="mn" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#F6D3BE"/><stop offset=".4" stop-color="#C08066"/><stop offset=".65" stop-color="#7E4936"/><stop offset="1" stop-color="#E9B49A"/></linearGradient><linearGradient id="mp" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#F4FAFC" stop-opacity=".9"/><stop offset=".5" stop-color="#B9CBD2" stop-opacity=".55"/><stop offset="1" stop-color="#E6F0F3" stop-opacity=".85"/></linearGradient><linearGradient id="ms" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#F5F5F3"/><stop offset=".4" stop-color="#B4B4B6"/><stop offset=".65" stop-color="#6F6F74"/><stop offset="1" stop-color="#DCDCDF"/></linearGradient>',
           '<radialGradient id="clay" cx=".45" cy=".35" r=".8"><stop offset="0" stop-color="#6A5A45"/><stop offset=".7" stop-color="#3A3127"/><stop offset="1" stop-color="#211C16"/></radialGradient>',
           '</defs>']
    figure = ('<g fill="#8A7558" opacity=".55">'
              '<circle cx="100" cy="98" r="11"/><circle cx="100" cy="83" r="5"/>'
              '<ellipse cx="100" cy="138" rx="26" ry="30"/><ellipse cx="100" cy="166" rx="42" ry="12"/>'
              '<rect x="62" y="182" width="76" height="8" rx="2"/><rect x="56" y="194" width="88" height="8" rx="2"/><rect x="50" y="206" width="100" height="8" rx="2"/></g>')
    for name, d in shapes.items():
        for m, grad in (("g", "mg"), ("s", "ms"), ("n", "mn"), ("p", "mp")):
            if name == "round":
                outer = f'<circle cx="100" cy="148" r="100" fill="url(#{grad})"/>'
                inner = '<circle cx="100" cy="148" r="84" fill="url(#clay)"/>'
                fig = f'<g transform="translate(18 14) scale(.82)">{figure}</g>'
            else:
                outer = f'<path d="{d}" fill="url(#{grad})"/>'
                inner = f'<path d="{d}" fill="url(#clay)" transform="translate(100 140) scale(.84) translate(-100 -140)"/>'
                fig = figure
            ring = f'<circle cx="100" cy="{40 if name=="round" else 14}" r="11" fill="none" stroke="url(#{grad})" stroke-width="6"/>'
            out.append(f'<symbol id="f-{name}-{m}" viewBox="0 0 200 260">{ring}{outer}{inner}{fig}'
                       f'<path d="M70 60 Q100 40 130 60" stroke="#fff" stroke-opacity=".25" stroke-width="3" fill="none"/></symbol>')
    out.append('</svg>')
    return "".join(out)


def frame(shape, metal, cls="frame", label=None):
    lab = f' aria-label="{label}"' if label else ' aria-hidden="true"'
    role = ' role="img"' if label else ''
    return f'<svg class="{cls}" viewBox="0 0 200 260"{role}{lab}><use href="#f-{shape}-{metal}"/></svg>'


HEAD_COMMON = """<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex">
<meta name="description" content="KT กรอบพระไทยแลนด์ รับเลี่ยมกรอบพระ กรอบทอง กรอบเงิน งานซ่อมและลายสั่งทำ โดยทีมช่างทองหลวง กระทุ่มแบน สมุทรสาคร">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<script src="https://unpkg.com/@phosphor-icons/web@2.1.1"></script>"""

REVEAL_JS = """<script>
(function(){
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (reduce || !('IntersectionObserver' in window)) return;
  document.documentElement.classList.add('js-reveal');
  var io = new IntersectionObserver(function(es){ es.forEach(function(e){ if(e.isIntersecting){ e.target.classList.add('in'); io.unobserve(e.target);} }); }, {rootMargin:'0px 0px -8% 0px'});
  document.querySelectorAll('.reveal').forEach(function(el){ io.observe(el); });
})();
</script>"""

REVEAL_CSS = """
.js-reveal .reveal{opacity:0;transform:translateY(24px);transition:opacity .8s cubic-bezier(.16,1,.3,1),transform .8s cubic-bezier(.16,1,.3,1)}
.js-reveal .reveal.in{opacity:1;transform:none}
@media (prefers-reduced-motion: reduce){*{animation:none!important;transition:none!important}}
"""


def draft_bar(n, name, bg, fg):
    return (f'<div style="background:{bg};color:{fg};font:500 13px/1.4 system-ui,sans-serif;padding:8px 16px;'
            f'display:flex;gap:8px 16px;flex-wrap:wrap;justify-content:center;align-items:center;text-align:center">'
            f'<span>ดราฟต์แบบที่ {n}/3 · {name} · ภาพเป็นภาพวาดตัวอย่าง รอรูปจริงจากร้าน</span>'
            f'<a href="../" style="color:inherit;text-decoration:underline">ดูแบบอื่น</a></div>')
