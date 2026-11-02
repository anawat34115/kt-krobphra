from shared import *

PRAJAM = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='40' height='40' viewBox='0 0 40 40'%3E"
          "%3Cg fill='none' stroke='%23E4BC62' stroke-width='1.2'%3E"
          "%3Cellipse cx='20' cy='11' rx='4' ry='7'/%3E%3Cellipse cx='20' cy='29' rx='4' ry='7'/%3E"
          "%3Cellipse cx='11' cy='20' rx='7' ry='4'/%3E%3Cellipse cx='29' cy='20' rx='7' ry='4'/%3E"
          "%3Ccircle cx='20' cy='20' r='2.5' fill='%23E4BC62'/%3E%3Cpath d='M0 0 L4 0 L0 4Z M40 0 L36 0 L40 4Z M0 40 L4 40 L0 36Z M40 40 L36 40 L40 36Z' fill='%23E4BC62'/%3E"
          "%3C/g%3E%3C/svg%3E")

THAI_NUM = ["๑", "๒", "๓"]

CSS = """
:root{--lac:#4A0F12;--lac-deep:#2E0709;--leaf:#E4BC62;--leaf-deep:#B8903A;--cream:#F5EAD3;--cream-2:#EBDDBF;--ink:#2A1A12;--ink-2:#6B5444;
--f-head:"Chonburi",serif;--f-body:"Sarabun",sans-serif;--ease:cubic-bezier(.16,1,.3,1)}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:var(--lac);color:var(--cream);font:400 17px/1.75 var(--f-body);-webkit-font-smoothing:antialiased}
a{color:inherit}svg{max-width:100%}
.wrap{max-width:1160px;margin:0 auto;padding-inline:24px}
h1,h2,h3{font-family:var(--f-head);font-weight:400;line-height:1.4;margin:0}
.kicker{font:600 14px var(--f-body);color:var(--leaf);letter-spacing:.08em;margin:0 0 16px;display:flex;align-items:center;gap:12px}
.kicker::before{content:"";width:32px;height:1px;background:currentColor}
.band{height:24px;background:url("PRAJAM") center/24px 24px repeat-x;opacity:.7;border-block:1px solid rgba(228,188,98,.5)}
.btn{display:inline-flex;align-items:center;gap:8px;height:56px;padding:0 28px;border-radius:999px;font:600 16px var(--f-body);text-decoration:none;transition:background .3s var(--ease),color .3s var(--ease)}
.btn i{font-size:20px}
.btn-leaf{background:var(--leaf);color:var(--lac-deep)}.btn-leaf:hover{background:#F0CD7E}
.btn-ghost{border:1.5px solid var(--leaf);color:var(--leaf)}.btn-ghost:hover{background:rgba(228,188,98,.12)}
.btn-ink{border:1.5px solid var(--lac);color:var(--lac)}.btn-ink:hover{background:var(--lac);color:var(--cream)}
a:focus-visible{outline:2px solid var(--leaf);outline-offset:3px}
.skip{position:absolute;left:-999px}.skip:focus{left:16px;top:16px;background:var(--leaf);color:#000;padding:8px 16px;z-index:99}

header.site{position:sticky;top:0;z-index:20;background:var(--lac-deep);border-bottom:1px solid rgba(228,188,98,.35)}
.nav{display:flex;align-items:center;justify-content:space-between;height:72px;gap:16px}
.brand{display:flex;align-items:center;gap:12px;text-decoration:none}
.brand .mark{width:44px;height:44px;border-radius:50%;background:var(--lac);border:1.5px solid var(--leaf);box-shadow:0 0 0 3px var(--lac-deep),0 0 0 4px rgba(228,188,98,.5);display:grid;place-items:center;font:16px var(--f-head);color:var(--leaf)}
.brand b{font:18px var(--f-head);color:var(--cream);font-weight:400}
.nav ul{display:flex;gap:28px;list-style:none;margin:0;padding:0;font-size:16px}
.nav ul a{text-decoration:none;color:rgba(245,234,211,.8)}.nav ul a:hover{color:var(--leaf)}
.nav .btn{height:44px;padding:0 20px;font-size:15px}
@media(max-width:960px){.nav ul{display:none}}

.hero{padding-block:80px 96px;position:relative;overflow:hidden}
.hero .grid{display:grid;grid-template-columns:7fr 5fr;gap:56px;align-items:center}
.hero h1{font-size:clamp(34px,4.8vw,56px);color:var(--cream)}
.hero h1 span{color:var(--leaf)}
.hero .lead{font-size:19px;color:rgba(245,234,211,.82);max-width:30em;margin:24px 0 40px}
.hero .ctas{display:flex;gap:16px;flex-wrap:wrap}
.niche{position:relative;aspect-ratio:3/4;max-width:400px;width:100%;justify-self:center;border-radius:200px 200px 8px 8px;background:radial-gradient(70% 60% at 50% 40%,#6B1A1E,var(--lac-deep));
  box-shadow:inset 0 0 0 2px var(--leaf),inset 0 0 0 10px var(--lac-deep),inset 0 0 0 11px rgba(228,188,98,.6);display:grid;place-items:center}
.niche .frame{width:58%;filter:drop-shadow(0 20px 24px rgba(0,0,0,.5))}
.niche small{position:absolute;bottom:24px;font-size:12px;color:rgba(245,234,211,.6)}
.stagger>*{animation:rise .9s var(--ease) both}.stagger>*:nth-child(2){animation-delay:.12s}.stagger>*:nth-child(3){animation-delay:.24s}.stagger>*:nth-child(4){animation-delay:.36s}
@keyframes rise{from{opacity:0;transform:translateY(16px)}}
@media(max-width:860px){.hero{padding-block:48px 64px}.hero .grid{grid-template-columns:1fr}.niche{max-width:280px;order:-1}}

section.block{padding-block:96px}
@media(max-width:860px){section.block{padding-block:56px}}
.light{background:var(--cream);color:var(--ink)}
.light .kicker{color:var(--leaf-deep)}
.light h2{color:var(--lac)}
.title{display:grid;gap:8px;margin-bottom:48px;max-width:36em}
.title h2{font-size:clamp(28px,3.4vw,40px)}
.title p{margin:0;color:var(--ink-2)}
.dark .title p{color:rgba(245,234,211,.75)}

.cats{display:grid;grid-template-columns:repeat(2,1fr);gap:24px}
@media(max-width:640px){.cats{grid-template-columns:1fr}}
.cat{display:grid;grid-template-columns:180px 1fr;gap:24px;align-items:center;padding:24px;background:#FBF4E4;border:1px solid var(--cream-2);border-radius:8px;text-decoration:none;transition:border-color .3s var(--ease)}
.cat:hover{border-color:var(--leaf-deep)}
.cat .pic{aspect-ratio:3/4;border-radius:90px 90px 4px 4px;background:var(--lac);box-shadow:inset 0 0 0 2px var(--leaf);display:grid;place-items:center}
.cat .frame{width:60%}
.cat h3{font-size:24px;color:var(--lac)}
.cat p{margin:8px 0 16px;color:var(--ink-2)}
.cat .go{font-weight:600;color:var(--lac);display:inline-flex;gap:8px;align-items:center}
@media(max-width:520px){.cat{grid-template-columns:112px 1fr;gap:16px;padding:16px}.cat h3{font-size:20px}.cat p{font-size:15px;margin:4px 0 8px}}
@media(max-width:520px){.brand b{font-size:15px}}
.brand b,.nav .btn{white-space:nowrap}

.timeline{list-style:none;margin:0;padding:0;display:grid;gap:0;max-width:760px}
.timeline li{display:grid;grid-template-columns:72px 1fr;gap:24px;padding-bottom:40px;position:relative}
.timeline li:not(:last-child)::before{content:"";position:absolute;left:35px;top:72px;bottom:8px;width:1px;background:rgba(228,188,98,.45)}
.timeline .num{width:72px;height:72px;border-radius:50%;border:1.5px solid var(--leaf);display:grid;place-items:center;font:30px var(--f-head);color:var(--leaf)}
.timeline h3{font-size:24px;margin:8px 0}
.timeline p{margin:0;color:rgba(245,234,211,.8)}

.strip{display:grid;grid-auto-flow:column;grid-auto-columns:minmax(220px,1fr);gap:16px;overflow-x:auto;padding-bottom:16px;scroll-snap-type:x mandatory}
.strip figure{margin:0;scroll-snap-align:start;aspect-ratio:3/4;border-radius:8px;background:var(--lac);box-shadow:inset 0 0 0 1px var(--leaf-deep);display:grid;place-items:center;position:relative}
.strip .frame{width:56%}
.strip figcaption{position:absolute;bottom:12px;font-size:12px;color:rgba(245,234,211,.65)}

.craft{display:grid;grid-template-columns:7fr 5fr;gap:56px;align-items:center}
@media(max-width:860px){.craft{grid-template-columns:1fr;gap:32px}}
.craft .quote{font:clamp(24px,2.6vw,32px)/1.5 var(--f-head);color:var(--leaf);margin:0 0 24px}
.craft p{color:rgba(245,234,211,.8)}
.craft .photo{aspect-ratio:1;border-radius:8px;border:1px solid var(--leaf-deep);background:url("PRAJAM") center/40px 40px,var(--lac-deep);display:grid;place-items:center;text-align:center;font-size:14px;color:rgba(245,234,211,.75);padding:24px}
.craft .photo div{background:var(--lac-deep);padding:16px 24px;border-radius:8px}
.craft .photo i{font-size:40px;color:var(--leaf);display:block}
.todo{display:inline-block;border:1px dashed var(--leaf);border-radius:4px;padding:2px 8px;font-size:15px;color:var(--leaf)}
.light .todo{color:var(--leaf-deep);border-color:var(--leaf-deep)}

.social{display:grid;grid-template-columns:1fr 1fr;gap:48px}
@media(max-width:860px){.social{grid-template-columns:1fr}}
.social h3{font-size:24px;color:var(--lac);margin-bottom:24px}
.clips{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.clip{aspect-ratio:9/16;border-radius:8px;background:linear-gradient(180deg,#5B1418,var(--lac-deep));display:grid;place-items:center;color:var(--leaf);text-decoration:none;position:relative}
.clip i{font-size:40px}.clip span{position:absolute;bottom:8px;font-size:12px;color:rgba(245,234,211,.7)}
.review{border-top:1px solid var(--cream-2);padding-block:24px}
.review .sk{height:10px;border-radius:4px;background:var(--cream-2);margin-bottom:8px}.review .sk.s{width:55%}
.review small{color:var(--ink-2)}

.contact{display:grid;grid-template-columns:5fr 7fr;gap:48px}
@media(max-width:860px){.contact{grid-template-columns:1fr}}
.contact dl{display:grid;gap:24px;margin:0 0 40px}
.contact dt{font-weight:600;color:var(--leaf);font-size:14px}
.contact dd{margin:0;font-size:19px}
.contact dd a{text-decoration:none}
.map{border-radius:8px;overflow:hidden;box-shadow:0 0 0 2px var(--leaf);min-height:380px}
.map iframe{width:100%;height:100%;min-height:380px;border:0}
footer{background:var(--lac-deep);padding-block:40px;font-size:14px;color:rgba(245,234,211,.7)}
footer .wrap{display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap}
""".replace("PRAJAM", PRAJAM)


def build():
    cats = "".join(
        f'<a class="cat reveal" href="#" data-link="shopee"><div class="pic">{frame(s, m)}</div>'
        f'<div><h3>{t}</h3><p>{d}</p><span class="go">ดูใน Shopee <i class="ph ph-arrow-right"></i></span></div></a>'
        for s, m, t, d in CATS)
    steps = "".join(
        f'<li class="reveal"><span class="num">{THAI_NUM[i]}</span><div><h3>{t}</h3><p>{d}</p></div></li>'
        for i, (t, d) in enumerate(STEPS))
    gal = "".join(f'<figure>{frame(s, m)}<figcaption>ภาพตัวอย่าง</figcaption></figure>' for s, m in GALLERY)
    clips = "".join(f'<a class="clip reveal" href="{SHOP["tiktok"]}" target="_blank" rel="noopener"><i class="ph-fill ph-play-circle"></i><span>คลิป {i}</span></a>' for i in range(1, 4))
    rev = "".join('<div class="review reveal"><div class="sk"></div><div class="sk"></div><div class="sk s"></div><small>รอรีวิวจริงจากลูกค้าของร้าน</small></div>' for _ in range(3))

    return f"""<!doctype html>
<html lang="th">
<head>
{HEAD_COMMON}
<title>KT กรอบพระไทยแลนด์ · เลี่ยมกรอบพระ กรอบทอง กรอบเงิน · ดราฟต์ 2</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Chonburi&family=Sarabun:wght@400;500;600&display=swap">
<style>{CSS}{REVEAL_CSS}</style>
</head>
<body>
<a class="skip" href="#main">ข้ามไปเนื้อหา</a>
{draft_bar(2, "ช่างหลวง", "#E4BC62", "#2E0709")}
{svg_defs()}
<header class="site"><div class="wrap nav">
  <a class="brand" href="#"><span class="mark">KT</span><b>{SHOP["name"]}</b></a>
  <nav aria-label="เมนูหลัก"><ul><li><a href="#products">สินค้า</a></li><li><a href="#repair">งานซ่อม/สั่งทำ</a></li><li><a href="#works">ผลงาน</a></li><li><a href="#about">เกี่ยวกับเรา</a></li><li><a href="#contact">ติดต่อ</a></li></ul></nav>
  <a class="btn btn-ghost" href="{SHOP["tel_href"]}"><i class="ph ph-phone"></i>โทร</a>
</div></header>

<main id="main">
<section class="hero"><div class="wrap grid">
  <div class="stagger">
    <p class="kicker">ร้านกรอบพระ กระทุ่มแบน สมุทรสาคร</p>
    <h1>กรอบพระงานช่าง<br><span>ทองหลวง</span><br>ทุกองค์ทำด้วยมือ</h1>
    <p class="lead">กรอบพระงานพรีเมี่ยม {SHOP["services"]} ส่งรูปพระมาให้ช่างดู แจ้งราคาก่อนเริ่มงานทุกครั้ง</p>
    <div class="ctas">
      <a class="btn btn-leaf" href="{SHOP["chat"]}" target="_blank" rel="noopener"><i class="ph ph-camera"></i>ส่งรูปพระ ขอประเมินราคา</a>
      <a class="btn btn-ghost" href="#products">ดูสินค้า</a>
    </div>
  </div>
  <div class="niche" aria-hidden="true">{frame("tear", "g")}<small>ภาพวาดตัวอย่าง</small></div>
</div></section>
<div class="band" aria-hidden="true"></div>

<section class="block light" id="products"><div class="wrap">
  <div class="title reveal"><p class="kicker">สินค้า</p><h2>กรอบพระหลากแบบ เลือกได้ตามพิมพ์</h2><p>ดูสินค้าทั้งหมดและสั่งซื้อได้ที่ร้าน Shopee</p></div>
  <div class="cats">{cats}</div>
</div></section>
<div class="band" aria-hidden="true"></div>

<section class="block dark" id="repair"><div class="wrap">
  <div class="title reveal"><p class="kicker">งานซ่อม · ลายสั่งทำ</p><h2>สั่งทำกับช่างได้ใน 3 ขั้นตอน</h2><p>เริ่มได้จากที่บ้าน ส่งรูปพระทางแชทก่อน</p></div>
  <ol class="timeline">{steps}</ol>
  <a class="btn btn-leaf reveal" href="{SHOP["chat"]}" target="_blank" rel="noopener"><i class="ph ph-camera"></i>ส่งรูปพระ ขอประเมินราคา</a>
</div></section>

<section class="block light" id="works"><div class="wrap">
  <div class="title reveal"><p class="kicker">ผลงาน</p><h2>ผลงานจากโต๊ะช่าง</h2><p>{PH}</p></div>
  <div class="strip" tabindex="0" aria-label="แกลเลอรีผลงาน เลื่อนดูด้านข้าง">{gal}</div>
</div></section>
<div class="band" aria-hidden="true"></div>

<section class="block dark" id="about"><div class="wrap craft">
  <div class="reveal">
    <p class="kicker">เกี่ยวกับเรา</p>
    <p class="quote">“{SHOP["tag"]}”</p>
    <p><span class="todo">ประวัติร้านและจุดเด่นของช่าง รอข้อมูลจากร้าน</span></p>
    <a class="btn btn-ghost" href="{SHOP["fb"]}" target="_blank" rel="noopener"><i class="ph ph-facebook-logo"></i>ดูเพจ Facebook</a>
  </div>
  <div class="photo reveal"><div><i class="ph ph-hammer"></i>รูปทีมช่าง (รอรูปจริงจากร้าน)</div></div>
</div></section>

<section class="block light"><div class="wrap social">
  <div><h3 class="reveal">คลิปงานจาก TikTok</h3><div class="clips">{clips}</div></div>
  <div><h3 class="reveal">รีวิวจากลูกค้า</h3>{rev}</div>
</div></section>
<div class="band" aria-hidden="true"></div>

<section class="block dark" id="contact"><div class="wrap contact">
  <div class="reveal">
    <p class="kicker">ติดต่อร้าน</p>
    <dl>
      <div><dt>ที่อยู่</dt><dd>{SHOP["addr"]}</dd></div>
      <div><dt>โทร</dt><dd><a href="{SHOP["tel_href"]}">{SHOP["tel"]}</a> · <a href="{SHOP["tel2_href"]}">{SHOP["tel2"]}</a> · <a href="{SHOP["tel3_href"]}">{SHOP["tel3"]}</a></dd></div>
      <div><dt>เวลาเปิด</dt><dd>{SHOP["hours"]}</dd></div>
      <div><dt>หน้าร้าน</dt><dd><a href="{SHOP["gmaps"]}" target="_blank" rel="noopener">{SHOP["store"]}</a></dd></div>
    </dl>
    <div style="display:flex;flex-wrap:wrap;gap:16px">
      <a class="btn btn-leaf" href="{SHOP["chat"]}" target="_blank" rel="noopener"><i class="ph ph-messenger-logo"></i>ทักแชท</a>
      <a class="btn btn-ghost" href="#" data-link="shopee">Shopee</a>
      <a class="btn btn-ghost" href="{SHOP["tiktok"]}" target="_blank" rel="noopener">TikTok</a>
    </div>
  </div>
  <div class="map reveal"><iframe title="แผนที่ร้าน" src="{SHOP["map_embed"]}" loading="lazy"></iframe></div>
</div></section>
</main>
<footer><div class="wrap"><span>© 2569 {SHOP["name"]}</span><span>ดราฟต์โดย ApeDev</span></div></footer>
{REVEAL_JS}
</body>
</html>"""
