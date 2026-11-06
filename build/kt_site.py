"""Real multi-page site (design 1 · ตู้โชว์ร้านทอง) for Vercel, until it moves to WordPress.
Pages: / · /products/ · /custom/ · /works/ · /about/ · /articles/ · /contact/
Asset paths are root-absolute (/assets/...) so every page shares one header."""
import os
from shared import SHOP, STEPS, REVIEWS, REVEAL_JS, REVEAL_CSS
from v1 import CSS as BASE_CSS

ROOT = os.path.join(os.path.dirname(__file__), "..", "site")
DOMAIN = "https://kt-krobphra.vercel.app"

# ---- ทรงสินค้า (จากลูกค้า 3 พ.ย. ข้อ 6) · photo = รูปชั่วคราวจนกว่าจะได้รูปแยกทรงจากร้าน
GROUPS = [
    ("silver", "กรอบเงิน", "กรอบเงินแท้ทุกทรงยอดนิยม เลือกตามพิมพ์พระ แต่ละทรงมีหลายขนาด", [
        ("egg", "ทรงไข่", "p08.jpg", "มีหลายขนาด แยกตามความกว้างและความสูงขององค์พระ", []),
        ("round", "ทรงกลม", "p05.jpg", "สำหรับเหรียญกลมและพระทรงกลมทุกขนาด", []),
        ("somdej", "ทรงสมเด็จ · สี่เหลี่ยม", "p18.jpg", "พระสมเด็จ พระผงสี่เหลี่ยม พระพิมพ์สี่เหลี่ยม", []),
        ("thaowes", "ทรงท้าวเวส", "p03.jpg", "สำหรับพระพิมพ์ท้าวเวสสุวรรณ", []),
        ("sema", "ทรงเสมา", "p07.jpg", "เหรียญเสมาและพระทรงใบเสมา", []),
        ("rooplor", "ทรงรูปหล่อ", "p01.jpg", "พระรูปหล่อ พระกริ่ง ทั้งแบบลอยองค์", []),
    ]),
    ("other", "ทรงอื่นๆ", "ทรงเฉพาะที่ร้านทำบ่อย ปรับรายละเอียดได้ตามองค์พระ", [
        ("phorung", "ทรงพ่อรุ่ง", "p02.jpg", "มีตัวเลือกให้ปรับตามชอบ",
         ["เก็บห่วง แบบ 1 / แบบ 2", "ยกซุ้ม / ไม่ยกซุ้ม", "ขัดเงา", "พิมพ์ใหญ่ / กลาง / เล็ก / พัดยศ-หยดน้ำ"]),
        ("tao", "ทรงเต่า", "p12.jpg", "กรอบรูปเต่าสำหรับพระพิมพ์เต่า ลายละเอียดรอบตัว", []),
        ("other", "งานตามสั่งทรงอื่นๆ", "p06.jpg", "ทรงที่ไม่มีในรายการ ส่งรูปพระมาให้ช่างดูได้", []),
    ]),
    ("custom", "งานสั่งทำ", "วัดขนาดพระแล้วขึ้นงานเฉพาะองค์ ทั้งนาก ทอง และลายตามแบบที่ต้องการ", [
        ("nak", "กรอบนาก", "p19.jpg", "สีนากอมชมพู งานละเอียดแบบช่างโบราณ", []),
        ("gold", "กรอบทอง", "p11.jpg", "ขึ้นงานทองตามพิมพ์พระและตามงบที่ตั้งไว้", []),
        ("design", "งานตามแบบ", "p13.jpg", "มีแบบในใจ ส่งรูปตัวอย่างมา ช่างทำลายให้ตามแบบ", []),
    ]),
]
SHAPES = [s for g in GROUPS for s in g[3]]
WORKS = ["p02.jpg", "p14.jpg", "p12.jpg", "p15.jpg", "p20.jpg", "p07.jpg", "p16.jpg", "p01.jpg",
         "p17.jpg", "p11.jpg", "p18.jpg", "p19.jpg", "p08.jpg", "p03.jpg", "p05.jpg", "p13.jpg"]

NAV = [("/", "หน้าแรก"), ("/products/", "สินค้า"), ("/custom/", "งานสั่งทำ"), ("/works/", "ผลงาน · รีวิว"),
       ("/about/", "เกี่ยวกับเรา"), ("/articles/", "บทความ"), ("/contact/", "ติดต่อ")]

ARTICLES = [
    ("choose", "เลือกกรอบพระให้พอดีกับองค์พระ",
     "กรอบที่ดีต้องพอดีกับพิมพ์พระ ไม่หลวมจนองค์พระขยับ และไม่คับจนกดขอบพระ",
     ["เริ่มจากดูทรงของพระก่อน เช่น ทรงไข่ ทรงกลม ทรงสมเด็จ หรือทรงเสมา แล้วเลือกกรอบทรงเดียวกัน",
      "วัดความกว้าง ความสูง และความหนาขององค์พระเป็นมิลลิเมตร ถ้าวัดเองไม่สะดวก ถ่ายรูปพระคู่กับไม้บรรทัดส่งมาให้ช่างดูได้",
      "พระเก่าหรือพระที่ขอบไม่เรียบ ควรให้ช่างวัดและขึ้นกรอบเฉพาะองค์ เพื่อให้กรอบกระชับและปลอดภัยกับองค์พระ"]),
    ("metal", "ทอง เงิน หรือนาก ต่างกันอย่างไร",
     "แต่ละเนื้อโลหะให้สี น้ำหนัก และงบต่างกัน เลือกตามการใช้งานและความชอบ",
     ["กรอบเงิน: สีขาวสว่าง ราคาเข้าถึงง่าย ใส่ได้ทุกวัน มีหลายทรงให้เลือก",
      "กรอบทอง: สีทองเหลืองอร่าม ทนทาน ขึ้นงานตามงบได้ เหมาะกับพระองค์สำคัญ",
      "กรอบนาก: สีทองอมชมพู เป็นงานช่างโบราณที่หาทำยาก ให้ความรู้สึกเก่าแก่และมีคุณค่า",
      "ไม่แน่ใจว่าแบบไหนเหมาะ ส่งรูปพระพร้อมงบที่ตั้งไว้มาทางแชท ช่างแนะนำให้ได้"]),
    ("care", "ดูแลกรอบพระให้สวยนาน",
     "ดูแลง่ายๆ ไม่กี่ข้อ กรอบพระก็เงางามและปกป้ององค์พระได้นาน",
     ["เช็ดด้วยผ้านุ่มแห้งหลังใส่ทุกครั้ง โดยเฉพาะหลังโดนเหงื่อ",
      "หลีกเลี่ยงน้ำหอม สเปรย์ และสารเคมีโดยตรง เพราะทำให้โลหะหมองเร็ว",
      "ตรวจห่วงและตะขอเป็นระยะ ถ้าห่วงสึกหรือหลวม นำมาให้ช่างซ่อมก่อนพระหล่นหาย",
      "กรอบหมองหรือมีรอย ร้านรับขัดเงาและซ่อมกรอบทุกชนิด"]),
]

EXTRA_CSS = """
.brand img{width:44px;height:44px;display:block}
.nav ul{gap:24px;font-size:14.5px}.nav ul a[aria-current=page]{color:var(--gold)}
@media(max-width:1120px){.nav ul{gap:16px;font-size:14px}}
.menu{display:none;position:relative}
.menu summary{list-style:none;cursor:pointer;width:40px;height:40px;border:1px solid var(--line);border-radius:8px;display:grid;place-items:center;font-size:22px}
.menu summary::-webkit-details-marker{display:none}
.menu ul{display:grid!important;position:absolute;right:0;top:48px;min-width:220px;background:var(--surface);border:1px solid var(--line);border-radius:8px;padding:8px!important;gap:0!important}
.menu ul a{display:block;padding:12px 16px;border-radius:6px;font-size:16px}.menu ul a:hover{background:#201C15}
@media(max-width:960px){.menu{display:block}.nav>nav{display:none}.nav .right{display:flex;gap:8px;align-items:center}}
.nav .right{display:flex;gap:8px;align-items:center}
.page-head{padding-block:72px 48px;position:relative;overflow:hidden}
.page-head::before{content:"";position:absolute;inset:0;background:radial-gradient(520px 320px at 70% 0%,rgba(214,176,106,.16),transparent 70%);pointer-events:none}
.page-head h1{font-size:clamp(30px,4.4vw,48px);position:relative}
.page-head p.lead{color:var(--muted);font-size:18px;max-width:36em;margin:16px 0 0;position:relative}
.crumbs{font-size:13px;color:var(--muted);margin-bottom:16px;position:relative}.crumbs a{text-decoration:none}.crumbs a:hover{color:var(--gold)}
/* shape tiles (home) */
.shapes{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}
@media(max-width:960px){.shapes{grid-template-columns:repeat(3,1fr)}}
@media(max-width:620px){.shapes{grid-template-columns:repeat(2,1fr);gap:10px}}
.shape{position:relative;display:block;aspect-ratio:4/5;border-radius:8px;overflow:hidden;border:1px solid var(--line);text-decoration:none;background:var(--surface)}
.shape img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;transition:transform .6s var(--ease)}
.shape:hover img{transform:scale(1.05)}.shape:hover{border-color:var(--gold-deep)}
.shape .lbl{position:absolute;left:0;right:0;bottom:0;padding:40px 14px 14px;background:linear-gradient(transparent,rgba(8,7,5,.92));display:flex;justify-content:space-between;align-items:end;gap:8px}
.shape .lbl b{font:600 17px/1.35 var(--f-head)}.shape .lbl small{display:block;font-size:12px;color:var(--gold);letter-spacing:.08em}
.shape .lbl i{color:var(--gold);font-size:18px;flex:none}
.group-tabs{display:flex;flex-wrap:wrap;gap:8px;margin:-24px 0 32px}
.group-tabs a{padding:8px 16px;border:1px solid var(--line);border-radius:999px;font-size:14px;text-decoration:none;color:var(--muted)}.group-tabs a:hover{border-color:var(--gold);color:var(--gold)}
/* products */
.pgroup+.pgroup{margin-top:72px}
.pgroup>h2{font-size:clamp(26px,3vw,34px)}.pgroup>p{color:var(--muted);margin:8px 0 32px;max-width:40em}
.prod{display:grid;grid-template-columns:320px 1fr;gap:32px;padding:32px 0;border-top:1px solid var(--line);scroll-margin-top:96px}
@media(max-width:760px){.prod{grid-template-columns:1fr;gap:20px}}
.prod .main{aspect-ratio:4/5;border-radius:8px;overflow:hidden;border:1px solid var(--line);background:var(--surface)}
.prod .main img{width:100%;height:100%;object-fit:cover;display:block}
@media(max-width:760px){.prod .main{aspect-ratio:1/1;max-width:420px}}
.prod h3{font-size:26px;margin-bottom:8px}.prod .desc{color:var(--muted);margin:0 0 20px}
.opts{display:flex;flex-wrap:wrap;gap:8px;list-style:none;padding:0;margin:0 0 20px}
.opts li{font-size:14px;padding:6px 12px;border:1px solid var(--gold-deep);border-radius:6px;color:var(--gold)}
.sizes{width:100%;border-collapse:collapse;font-size:15px;margin:0 0 20px}
.sizes caption{text-align:left;font:600 15px var(--f-body);color:var(--text);margin-bottom:8px}
.sizes th,.sizes td{border:1px solid var(--line);padding:8px 12px;text-align:left}.sizes th{color:var(--muted);font-weight:500;background:var(--surface)}
.thumbs{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin:0 0 24px}
.thumbs img{width:100%;aspect-ratio:1;object-fit:cover;border-radius:6px;border:1px solid var(--line);display:block}
.thumbs .more{aspect-ratio:1;border-radius:6px;border:1px dashed var(--line);display:grid;place-items:center;font-size:12px;color:var(--muted);text-align:center;padding:8px}
.prod .acts{display:flex;flex-wrap:wrap;gap:12px}
/* works */
.wgrid{columns:4 220px;column-gap:16px}
.wgrid img{width:100%;display:block;border-radius:8px;border:1px solid var(--line);margin-bottom:16px;break-inside:avoid}
.rgrid{columns:3 260px;column-gap:16px}.rgrid img{width:100%;display:block;border-radius:8px;margin-bottom:16px;break-inside:avoid}
/* custom */
.measure{display:grid;grid-template-columns:1fr 1fr;gap:48px;align-items:start}
@media(max-width:860px){.measure{grid-template-columns:1fr;gap:32px}}
.measure ol{margin:0;padding-left:20px;display:grid;gap:12px;color:var(--muted)}.measure ol b{color:var(--text)}
.note{border:1px solid var(--line);border-left:2px solid var(--gold);background:var(--surface);border-radius:8px;padding:20px 24px;color:var(--muted)}
.note b{color:var(--text)}
.mats{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
@media(max-width:760px){.mats{grid-template-columns:1fr}}
.mat{display:block;border:1px solid var(--line);border-radius:8px;overflow:hidden;background:var(--surface);text-decoration:none}
.mat img{width:100%;aspect-ratio:4/3;object-fit:cover;display:block}.mat div{padding:20px}.mat h3{font-size:22px;margin-bottom:6px}.mat p{margin:0;color:var(--muted);font-size:15px}
/* articles */
.arts{display:grid;gap:24px;max-width:820px}
.art{border:1px solid var(--line);border-radius:8px;background:var(--surface);padding:32px;scroll-margin-top:96px}
.art h2{font-size:26px;margin-bottom:8px}.art .ex{color:var(--gold);margin:0 0 16px}.art ul{margin:0;padding-left:20px;display:grid;gap:10px;color:var(--muted)}
.toc{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:32px}
.cta-band{border-top:1px solid var(--line);padding-block:72px;text-align:center;position:relative;overflow:hidden}
.cta-band::before{content:"";position:absolute;inset:0;background:radial-gradient(480px 240px at 50% 100%,rgba(214,176,106,.16),transparent 70%)}
.cta-band h2{font-size:clamp(26px,3.2vw,36px);position:relative}.cta-band p{color:var(--muted);margin:12px auto 32px;max-width:32em;position:relative}
.cta-band .ctas{display:flex;flex-wrap:wrap;gap:16px;justify-content:center;position:relative}
footer .flogo{width:88px;height:auto}
footer .wrap{align-items:center}
footer nav ul{display:flex;flex-wrap:wrap;gap:8px 20px;list-style:none;margin:0;padding:0}footer nav a{text-decoration:none}footer nav a:hover{color:var(--gold)}
.foot-top{display:flex;gap:24px;align-items:center;flex-wrap:wrap}
"""


def img(name, alt, cls="", eager=False):
    lazy = 'fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'
    c = f' class="{cls}"' if cls else ""
    return f'<img{c} src="/assets/img/{name}" alt="{alt}" {lazy}>'


def btn_chat(label="ส่งรูปพระ ขอประเมินราคา"):
    return f'<a class="btn btn-gold" href="{SHOP["chat"]}" target="_blank" rel="noopener"><i class="ph ph-camera"></i>{label}</a>'


def header(cur):
    links = "".join(f'<li><a href="{h}"{" aria-current=page" if h == cur else ""}>{t}</a></li>' for h, t in NAV)
    return f"""<header class="site"><div class="wrap nav">
  <a class="brand" href="/" aria-label="{SHOP["name"]} หน้าแรก"><img src="/assets/logo/kt-mark-96.png" alt="" width="44" height="44"><b>{SHOP["name"]}</b></a>
  <nav aria-label="เมนูหลัก"><ul>{links}</ul></nav>
  <div class="right">
    <a class="btn btn-line call" href="{SHOP["tel_href"]}" aria-label="โทร {SHOP["tel"]}"><i class="ph ph-phone"></i><span class="t">{SHOP["tel"]}</span></a>
    <details class="menu"><summary aria-label="เปิดเมนู"><i class="ph ph-list"></i></summary><ul>{links}</ul></details>
  </div>
</div></header>"""


def footer():
    links = "".join(f'<li><a href="{h}">{t}</a></li>' for h, t in NAV)
    return f"""<footer><div class="wrap">
  <div class="foot-top"><img class="flogo" src="/assets/logo/kt-mark-192.png" alt="{SHOP["name"]}" width="88" height="88" loading="lazy">
    <div><b style="color:var(--text)">{SHOP["name"]}</b><br>{SHOP["addr"]}<br>โทร <a href="{SHOP["tel_href"]}">{SHOP["tel"]}</a> · {SHOP["hours"]}</div></div>
  <nav aria-label="เมนูท้ายเว็บ"><ul>{links}</ul></nav>
</div><div class="wrap" style="margin-top:24px"><span>© 2569 {SHOP["name"]}</span></div></footer>
<a class="fab" href="{SHOP["chat"]}" target="_blank" rel="noopener" aria-label="ทักแชทส่งรูปพระ"><i class="ph-fill ph-messenger-logo"></i></a>"""


def cta_band():
    return f"""<section class="cta-band"><div class="wrap">
  <h2>มีพระอยากเลี่ยม ส่งรูปมาให้ช่างดูได้เลย</h2>
  <p>ถ่ายรูปพระด้านหน้าและด้านหลัง บอกงบที่ตั้งไว้ ช่างแจ้งราคาก่อนเริ่มงานทุกครั้ง</p>
  <div class="ctas">{btn_chat()}<a class="btn btn-line" href="{SHOP["shopee"]}" target="_blank" rel="noopener"><i class="ph ph-storefront"></i>ดูร้านใน Shopee</a></div>
</div></section>"""


def page(path, title, desc, body, cur):
    url = DOMAIN + path
    return f"""<!doctype html>
<html lang="th">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website"><meta property="og:title" content="{title}"><meta property="og:description" content="{desc}">
<meta property="og:image" content="{DOMAIN}/assets/logo/og-image.jpg"><meta property="og:url" content="{url}"><meta property="og:locale" content="th_TH">
<link rel="icon" href="/favicon.ico" sizes="any"><link rel="icon" type="image/png" href="/assets/logo/favicon-32.png"><link rel="apple-touch-icon" href="/assets/logo/apple-touch-icon.png">
<meta name="theme-color" content="#0E0C09">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Thai:wght@400;500;600&family=Noto+Serif+Thai:wght@500;600&display=swap">
<script src="https://unpkg.com/@phosphor-icons/web@2.1.1"></script>
<style>{BASE_CSS}{EXTRA_CSS}{REVEAL_CSS}</style>
</head>
<body>
<a class="skip" href="#main">ข้ามไปเนื้อหา</a>
{header(cur)}
<main id="main">
{body}
</main>
{footer()}
{REVEAL_JS}
</body>
</html>"""


def head(crumb, h1, lead):
    return f"""<section class="page-head"><div class="wrap">
  <p class="crumbs"><a href="/">หน้าแรก</a> / {crumb}</p>
  <h1>{h1}</h1><p class="lead">{lead}</p>
</div></section>"""


def steps_html():
    return "".join(f'<li class="reveal"><span class="n">ขั้นที่ {i+1}</span><h3>{t}</h3><p>{d}</p></li>' for i, (t, d) in enumerate(STEPS))


def contact_block(h2="มาที่ร้าน หรือทักแชทได้เลย"):
    return f"""<section class="block" id="contact"><div class="wrap contact">
  <div class="reveal">
    <p class="eyebrow">ติดต่อ</p>
    <h2 style="font-size:clamp(28px,3.4vw,40px);margin-bottom:40px">{h2}</h2>
    <dl>
      <div><dt>ที่อยู่</dt><dd>{SHOP["addr"]}</dd></div>
      <div><dt>โทร</dt><dd><a href="{SHOP["tel_href"]}">{SHOP["tel"]}</a> · <a href="{SHOP["tel2_href"]}">{SHOP["tel2"]}</a> · <a href="{SHOP["tel3_href"]}">{SHOP["tel3"]}</a></dd></div>
      <div><dt>เวลาเปิด</dt><dd>{SHOP["hours"]}</dd></div>
      <div><dt>หน้าร้าน</dt><dd><a href="{SHOP["gmaps"]}" target="_blank" rel="noopener">{SHOP["store"]}</a></dd></div>
    </dl>
    <div style="display:flex;flex-wrap:wrap;gap:16px">
      <a class="btn btn-gold" href="{SHOP["chat"]}" target="_blank" rel="noopener"><i class="ph ph-messenger-logo"></i>ทักแชท Facebook</a>
      <a class="btn btn-line" href="{SHOP["shopee"]}" target="_blank" rel="noopener"><i class="ph ph-storefront"></i>Shopee</a>
      <a class="btn btn-line" href="{SHOP["tiktok"]}" target="_blank" rel="noopener"><i class="ph ph-tiktok-logo"></i>TikTok</a>
    </div>
  </div>
  <div class="map reveal"><iframe title="แผนที่ร้าน {SHOP["name"]}" src="{SHOP["map_embed"]}" loading="lazy"></iframe></div>
</div></section>"""


# ------------------------------------------------------------------ pages
def home():
    tiles = "".join(
        f'<a class="shape reveal" href="/products/#{sid}">{img(ph, "กรอบพระ" + name + " งานจริงจากร้าน")}'
        f'<span class="lbl"><span><small>{g[1]}</small><b>{name}</b></span><i class="ph ph-arrow-right"></i></span></a>'
        for g in GROUPS for sid, name, ph, _, _ in g[3])
    tabs = "".join(f'<a href="/products/#{g[0]}">{g[1]}</a>' for g in GROUPS)
    clips = "".join(f'<a class="clip reveal" href="{SHOP["tiktok"]}" target="_blank" rel="noopener"><i class="ph-fill ph-play-circle"></i><span>คลิป TikTok {i}</span></a>' for i in range(1, 5))
    body = f"""
<section class="hero" id="hero"><div class="wrap grid">
  <div class="stagger">
    <p class="eyebrow">กรอบพระงานพรีเมี่ยม · กระทุ่มแบน สมุทรสาคร</p>
    <h1>เลี่ยมกรอบพระ<br>ด้วยฝีมือ<em>ช่างทองหลวง</em></h1>
    <p class="lead">กรอบพระงานพรีเมี่ยม {SHOP["services"]} ส่งรูปพระมาให้ช่างดู แจ้งราคาก่อนเริ่มงานทุกครั้ง</p>
    <div class="ctas">{btn_chat()}<a class="btn btn-line" href="#shapes">ดูผลงานแยกตามทรง</a></div>
    <div class="trust"><span><i class="ph ph-seal-check"></i>ก่อตั้งปี 2533</span><span><i class="ph ph-hand"></i>ช่างทองสองรุ่น</span><span><i class="ph ph-truck"></i>งานเสร็จ 7–14 วัน</span></div>
  </div>
  <div class="case" aria-hidden="true">
    <div class="glow"></div><div class="shelf"></div>
    {img("p02.jpg", "", "frame photo", True)}
    <div class="tag"><b>งานจริงจากร้าน</b>ทุกงานซ่อม ลายสั่งทำ</div>
  </div>
</div></section>

<section class="block" id="shapes"><div class="wrap">
  <div class="head-row reveal"><div><p class="eyebrow">ผลงานจริง แยกตามทรง</p><h2>เลือกทรงกรอบที่ใช่</h2></div><p>รูปทั้งหมดเป็นงานจริงจากโต๊ะช่างของร้าน กดที่ทรงเพื่อดูขนาดและผลงานเพิ่ม</p></div>
  <div class="group-tabs reveal">{tabs}</div>
  <div class="shapes">{tiles}</div>
</div></section>

<section class="block" id="repair"><div class="wrap">
  <div class="head-row reveal"><div><p class="eyebrow">งานซ่อม · ลายสั่งทำ</p><h2>สั่งทำง่าย 3 ขั้นตอน</h2></div><p>ไม่ต้องเดินทางมาร้าน เริ่มจากส่งรูปพระทางแชท</p></div>
  <ol class="steps">{steps_html()}</ol>
  <div class="steps-cta reveal" style="display:flex;flex-wrap:wrap;gap:16px">{btn_chat()}<a class="btn btn-line" href="/custom/">วิธีวัดขนาดพระ</a></div>
</div></section>

<section class="block" id="about"><div class="wrap craft">
  {img("p06.jpg", "อะไหล่กรอบพระและห่วงบนโต๊ะช่าง", "photo reveal craftimg")}
  <div class="reveal">
    <p class="eyebrow">เกี่ยวกับเรา</p>
    <h2>งานช่างทองสองรุ่น<br>ตั้งแต่ปี 2533</h2>
    <blockquote>{SHOP["tag"]}</blockquote>
    <p>เริ่มจากคุณพ่อและคุณแม่ที่เคยเป็นช่างทองและพนักงานขายในร้านทอง วันนี้รุ่นลูกสานต่อด้วยฝีมือช่างทองหลวง ผสมเทคนิคโบราณเข้ากับเครื่องมือสมัยใหม่</p>
    <a class="btn btn-line" href="/about/">อ่านเรื่องของร้าน</a>
  </div>
</div></section>

<section class="block"><div class="wrap">
  <div class="head-row reveal"><div><p class="eyebrow">TikTok</p><h2>ดูคลิปงานจากโต๊ะช่าง</h2></div><p><a href="/works/" style="color:var(--gold)">ดูผลงานและรีวิวทั้งหมด →</a></p></div>
  <div class="clips" style="grid-template-columns:repeat(4,1fr)">{clips}</div>
</div></section>

{contact_block()}"""
    return page("/", f"{SHOP['name']} · เลี่ยมกรอบพระ กรอบทอง กรอบเงิน กรอบนาก กระทุ่มแบน",
                "KT กรอบพระไทยแลนด์ รับเลี่ยมกรอบพระ กรอบเงิน กรอบทอง กรอบนาก งานซ่อมและลายสั่งทำ โดยทีมช่างทองหลวง ตั้งแต่ปี 2533 กระทุ่มแบน สมุทรสาคร",
                body, "/")


def products():
    secs = []
    for gid, gname, gdesc, items in GROUPS:
        rows = []
        for sid, name, ph, desc, opts in items:
            o = f'<ul class="opts">{"".join(f"<li>{x}</li>" for x in opts)}</ul>' if opts else ""
            rows.append(f"""<article class="prod reveal" id="{sid}">
  <div class="main">{img(ph, "กรอบพระ" + name)}</div>
  <div>
    <h3>{name}</h3><p class="desc">{desc}</p>{o}
    <table class="sizes"><caption>ขนาดที่มี</caption><thead><tr><th>ขนาด</th><th>กว้าง × สูง (มม.)</th></tr></thead>
      <tbody><tr><td colspan="2"><span class="todo">รอตารางขนาดจากร้าน</span></td></tr></tbody></table>
    <p style="margin:0 0 8px;font-size:15px;color:var(--text)">ผลงานที่เคยทำ</p>
    <div class="thumbs"><div class="more">รูปผลงานทรง{name.replace("ทรง","")}<br>รอเพิ่มจากร้าน</div></div>
    <div class="acts">{btn_chat("ส่งรูปพระ ถามขนาด")}<a class="btn btn-line" href="{SHOP["shopee"]}" target="_blank" rel="noopener"><i class="ph ph-storefront"></i>สั่งใน Shopee</a></div>
  </div>
</article>""")
        secs.append(f'<div class="pgroup" id="{gid}"><h2 class="reveal">{gname}</h2><p class="reveal">{gdesc}</p>{"".join(rows)}</div>')
    tabs = "".join(f'<a href="#{g[0]}">{g[1]}</a>' for g in GROUPS)
    body = head("สินค้า", "สินค้า · กรอบพระทุกทรง", "เลือกตามทรงพระ ดูขนาดและผลงานจริงของแต่ละทรง สั่งซื้อได้ใน Shopee หรือส่งรูปพระมาถามช่างก่อนก็ได้") + \
        f'<section class="block" style="border-top:0;padding-top:0"><div class="wrap"><div class="group-tabs" style="margin-top:0">{tabs}</div>{"".join(secs)}</div></section>' + cta_band()
    return page("/products/", f"สินค้า กรอบพระทุกทรง · {SHOP['name']}",
                "กรอบพระเงิน ทรงไข่ ทรงกลม ทรงสมเด็จ ท้าวเวส เสมา รูปหล่อ ทรงพ่อรุ่ง ทรงเต่า และงานสั่งทำกรอบนาก กรอบทอง จาก KT กรอบพระไทยแลนด์",
                body, "/products/")


def custom():
    mats = "".join(f'<a class="mat reveal" href="/products/#{sid}">{img(ph, name)}<div><h3>{name}</h3><p>{desc}</p></div></a>'
                   for sid, name, ph, desc, _ in GROUPS[2][3])
    body = head("งานสั่งทำ", "งานซ่อม · ลายสั่งทำ", "วัดขนาดพระแล้วขึ้นกรอบเฉพาะองค์ ทั้งกรอบนาก กรอบทอง และลายตามแบบ รวมถึงซ่อมกรอบทุกชนิด") + f"""
<section class="block" style="border-top:0;padding-top:24px"><div class="wrap">
  <div class="head-row reveal"><div><p class="eyebrow">ขั้นตอน</p><h2>สั่งทำง่าย 3 ขั้นตอน</h2></div><p>ช่างแจ้งราคาและระยะเวลาก่อนเริ่มงานทุกครั้ง</p></div>
  <ol class="steps">{steps_html()}</ol>
</div></section>
<section class="block"><div class="wrap measure">
  <div class="reveal">
    <p class="eyebrow">วัดขนาดพระ</p>
    <h2 style="font-size:clamp(26px,3vw,34px);margin-bottom:24px">ส่งขนาดมาให้ช่างแบบนี้</h2>
    <ol>
      <li><b>ถ่ายรูปพระด้านหน้าและด้านหลัง</b> ในที่แสงสว่าง ให้เห็นขอบพระชัด</li>
      <li><b>วางไม้บรรทัดข้างองค์พระ</b> แล้วถ่ายอีกรูป ช่างจะกะขนาดจากรูปได้</li>
      <li><b>ถ้าวัดได้ ให้วัดเป็นมิลลิเมตร</b> ความกว้าง ความสูง และความหนาตรงจุดที่หนาที่สุด</li>
      <li><b>บอกเนื้อกรอบและงบที่ตั้งไว้</b> เช่น เงิน ทอง หรือนาก ช่างแนะนำแบบที่เหมาะให้</li>
    </ol>
  </div>
  <div class="reveal">
    <div class="note"><b>ไม่สะดวกวัดเอง?</b><br>นำพระมาที่หน้าร้าน {SHOP["store"]} ช่างวัดให้ที่ร้าน หรือส่งพระทางไปรษณีย์ ช่างวัดขนาดแล้วส่งกลับให้ถึงบ้าน <span class="todo">รอร้านยืนยันเรื่องส่งไปรษณีย์</span></div>
    <div class="note" style="margin-top:16px"><b>ระยะเวลา</b><br>งานเสร็จประมาณ 7–14 วัน ขึ้นกับลายและเนื้อโลหะ</div>
    <div style="margin-top:24px">{btn_chat()}</div>
  </div>
</div></section>
<section class="block"><div class="wrap">
  <div class="head-row reveal"><div><p class="eyebrow">เนื้อกรอบ</p><h2>งานสั่งทำที่รับ</h2></div><p>ทุกงานทำเฉพาะองค์ ตามพิมพ์และขนาดพระจริง</p></div>
  <div class="mats">{mats}</div>
  <div class="note reveal" style="margin-top:24px"><b>รับซ่อมกรอบทุกชนิด</b><br>เปลี่ยนห่วง ขัดเงา ซ่อมกรอบหลวมหรือชำรุด ทั้งทอง เงิน นาก และกรอบพลาสติกกันน้ำ</div>
</div></section>""" + cta_band()
    return page("/custom/", f"งานซ่อม ลายสั่งทำ วิธีวัดขนาดพระ · {SHOP['name']}",
                "สั่งทำกรอบพระเฉพาะองค์ กรอบนาก กรอบทอง งานตามแบบ ซ่อมกรอบพระ พร้อมวิธีวัดขนาดพระส่งให้ช่าง งานเสร็จ 7–14 วัน",
                body, "/custom/")


def works():
    w = "".join(f'<a href="/products/" class="reveal">{img(p, "ผลงานกรอบพระจากร้าน KT")}</a>' for p in WORKS)
    r = "".join(img(x, "รีวิวจากลูกค้าร้าน KT กรอบพระไทยแลนด์", "reveal") for x in REVIEWS)
    body = head("ผลงาน · รีวิว", "ผลงานและรีวิวจากลูกค้า", "งานจริงจากโต๊ะช่างของร้าน และเสียงจากลูกค้าที่ส่งพระมาเลี่ยมกับเรา") + f"""
<section class="block" style="border-top:0;padding-top:24px"><div class="wrap">
  <div class="head-row reveal"><div><p class="eyebrow">ผลงาน</p><h2>งานจากโต๊ะช่างของเรา</h2></div><p>ดูแยกตามทรงได้ที่ <a href="/products/" style="color:var(--gold)">หน้าสินค้า</a></p></div>
  <div class="wgrid">{w}</div>
</div></section>
<section class="block" id="reviews"><div class="wrap">
  <div class="head-row reveal"><div><p class="eyebrow">รีวิว</p><h2>ลูกค้าพูดถึงเรา</h2></div><p>แคปจากแชทลูกค้าจริง</p></div>
  <div class="rgrid">{r}</div>
</div></section>""" + cta_band()
    return page("/works/", f"ผลงานและรีวิว · {SHOP['name']}", "รวมผลงานกรอบพระจริงและรีวิวจากลูกค้าของ KT กรอบพระไทยแลนด์", body, "/works/")


def about():
    body = head("เกี่ยวกับเรา", "งานช่างทองสองรุ่น ตั้งแต่ปี 2533", "KT กรอบพระไทยแลนด์ แบรนด์ร้านเลี่ยมพระของคนไทย") + f"""
<section class="block" style="border-top:0;padding-top:24px"><div class="wrap craft">
  {img("p06.jpg", "อะไหล่กรอบพระและห่วงบนโต๊ะช่าง", "photo reveal craftimg")}
  <div class="reveal">
    <p class="eyebrow">เรื่องของเรา</p>
    <blockquote>{SHOP["tag"]}</blockquote>
    <p>KT กรอบพระไทยแลนด์ เป็นแบรนด์ร้านเลี่ยมพระของคนไทย เริ่มจากคุณพ่อและคุณแม่ที่เคยเป็นช่างทองและพนักงานขายในร้านทอง ก่อตั้งร้านขึ้นในปี 2533</p>
    <p>วันนี้รุ่นลูกสานต่อด้วยฝีมือช่างทองหลวง ผสมเทคนิคช่างทองโบราณเข้ากับเครื่องมือและเทคโนโลยีสมัยใหม่ ทุกลวดลายจึงเป็นทั้งการอนุรักษ์งานช่างไทยและงานศิลปะที่มีคุณค่า</p>
    <ul class="facts">
      <li><b>2533</b><span>ปีที่ก่อตั้งร้าน</span></li>
      <li><b>2 รุ่น</b><span>ช่างทองในครอบครัว</span></li>
      <li><b>ทอง เงิน นาก</b><span>รับทำทุกเนื้อโลหะ</span></li>
    </ul>
  </div>
</div></section>
<section class="block"><div class="wrap">
  <div class="head-row reveal"><div><p class="eyebrow">สิ่งที่เรารับทำ</p><h2>ครบเรื่องกรอบพระในร้านเดียว</h2></div><p>{SHOP["services"]}</p></div>
  <div class="mats">
    <a class="mat reveal" href="/products/">{img("p18.jpg", "กรอบเงิน")}<div><h3>กรอบสำเร็จ</h3><p>กรอบเงินทุกทรงยอดนิยม หลายขนาด</p></div></a>
    <a class="mat reveal" href="/custom/">{img("p19.jpg", "กรอบนาก")}<div><h3>งานสั่งทำ</h3><p>กรอบนาก กรอบทอง ลายตามแบบ เฉพาะองค์</p></div></a>
    <a class="mat reveal" href="/custom/">{img("p05.jpg", "งานซ่อมกรอบ")}<div><h3>งานซ่อม</h3><p>เปลี่ยนห่วง ขัดเงา ซ่อมกรอบทุกชนิด</p></div></a>
  </div>
</div></section>""" + contact_block("แวะมาคุยกับช่างที่ร้าน")
    return page("/about/", f"เกี่ยวกับเรา · {SHOP['name']}", "ประวัติร้าน KT กรอบพระไทยแลนด์ ร้านเลี่ยมพระของคนไทย ก่อตั้งปี 2533 สานต่องานช่างทองหลวงสองรุ่น", body, "/about/")


def articles():
    toc = "".join(f'<a href="#{a}">{t}</a>' for a, t, _, _ in ARTICLES)
    arts = "".join(f'<article class="art reveal" id="{a}"><h2>{t}</h2><p class="ex">{ex}</p><ul>{"".join(f"<li>{x}</li>" for x in pts)}</ul></article>'
                   for a, t, ex, pts in ARTICLES)
    body = head("บทความ", "บทความเรื่องกรอบพระ", "ความรู้จากช่าง เรื่องเลือกกรอบ เนื้อโลหะ และการดูแล") + \
        f'<section class="block" style="border-top:0;padding-top:24px"><div class="wrap"><div class="group-tabs toc" style="margin-top:0">{toc}</div><div class="arts">{arts}</div></div></section>' + cta_band()
    return page("/articles/", f"บทความเรื่องกรอบพระ · {SHOP['name']}", "วิธีเลือกกรอบพระให้พอดีองค์ ทอง เงิน นาก ต่างกันอย่างไร และวิธีดูแลกรอบพระให้สวยนาน", body, "/articles/")


def contact():
    body = head("ติดต่อ", "ติดต่อร้าน", "ทักแชท โทร หรือแวะมาที่หน้าร้านได้ทุกวัน") + contact_block("ช่องทางติดต่อ")
    return page("/contact/", f"ติดต่อ · {SHOP['name']}", f"ติดต่อ KT กรอบพระไทยแลนด์ {SHOP['addr']} โทร {SHOP['tel']} เปิดทุกวัน 08:00–20:00 น.", body, "/contact/")


def sitemap():
    urls = "".join(f"<url><loc>{DOMAIN}{h}</loc></url>" for h, _ in NAV)
    return f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>'


def build_all(write):
    write("index.html", home())
    write("products/index.html", products())
    write("custom/index.html", custom())
    write("works/index.html", works())
    write("about/index.html", about())
    write("articles/index.html", articles())
    write("contact/index.html", contact())
    write("sitemap.xml", sitemap())
