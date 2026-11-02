from shared import *

CSS = """
:root{--night:#0B0B0C;--night-2:#151514;--ivory:#F3EFE8;--ivory-2:#E4DED3;--champ:#CBB58C;--stone:#8D877C;--ink:#151412;
--f-head:"Bai Jamjuree",sans-serif;--f-body:"Anuphan",sans-serif;--ease:cubic-bezier(.32,.72,0,1)}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:var(--night);color:var(--ivory);font:400 16px/1.75 var(--f-body);-webkit-font-smoothing:antialiased}
a{color:inherit}svg{max-width:100%}
.wrap{max-width:1280px;margin:0 auto;padding-inline:24px}
h1,h2,h3{font-family:var(--f-head);margin:0}
.label{font:500 12px var(--f-head);letter-spacing:.24em;text-transform:uppercase;color:var(--champ)}
.btn{display:inline-flex;align-items:center;gap:12px;height:56px;padding:0 32px;font:500 15px var(--f-head);letter-spacing:.04em;text-decoration:none;border:1px solid currentColor;transition:background .4s var(--ease),color .4s var(--ease)}
.btn-champ{background:var(--champ);border-color:var(--champ);color:var(--night)}.btn-champ:hover{background:transparent;color:var(--champ)}
.btn-line:hover{background:var(--ivory);color:var(--night)}
.light .btn-line:hover{background:var(--ink);color:var(--ivory)}
a:focus-visible{outline:2px solid var(--champ);outline-offset:3px}
.skip{position:absolute;left:-999px}.skip:focus{left:16px;top:16px;background:var(--champ);color:#000;padding:8px 16px;z-index:99}

header.site{position:sticky;top:0;z-index:20;background:rgba(11,11,12,.9);backdrop-filter:blur(8px)}
.nav{display:flex;align-items:center;justify-content:space-between;height:72px;gap:16px;border-bottom:1px solid #26251F}
.brand{font:600 18px var(--f-head);letter-spacing:.02em;text-decoration:none}
.brand span{color:var(--champ)}
.nav ul{display:flex;gap:32px;list-style:none;margin:0;padding:0;font:500 14px var(--f-head);letter-spacing:.06em}
.nav ul a{text-decoration:none;color:var(--stone)}.nav ul a:hover{color:var(--ivory)}
.nav .btn{height:40px;padding:0 20px;font-size:13px}
@media(max-width:960px){.nav ul{display:none}}
.brand,.nav .btn{white-space:nowrap}
@media(max-width:520px){.brand{font-size:15px}.nav .btn{padding:0 12px}}

.hero{position:relative;padding-block:72px 96px;overflow:hidden}
.hero .big{font:300 clamp(56px,12.5vw,184px)/1.02 var(--f-head);letter-spacing:-.01em;position:relative;z-index:2}
.hero .big b{font-weight:500;color:var(--champ)}
.hero .art{position:absolute;right:6%;top:40px;width:clamp(180px,26vw,360px);z-index:1;opacity:.95}
.hero .art .frame{width:100%;filter:drop-shadow(0 32px 40px rgba(0,0,0,.7))}
.hero .art small{display:block;text-align:center;font-size:12px;color:var(--stone)}
.hero .row{display:grid;grid-template-columns:1fr auto;gap:32px;align-items:end;margin-top:56px;padding-top:32px;border-top:1px solid #26251F;position:relative;z-index:2}
.hero .row p{margin:0;max-width:34em;color:#BDB6A9;font-size:17px}
.hero .ctas{display:flex;gap:16px;flex-wrap:wrap}
@media(max-width:860px){.hero{padding-block:40px 56px}.hero .art{position:relative;right:auto;top:auto;margin:0 auto 24px;width:200px}.hero .row{grid-template-columns:1fr}}
.stagger>*{animation:rise 1s var(--ease) both}.stagger>*:nth-child(2){animation-delay:.12s}.stagger>*:nth-child(3){animation-delay:.24s}
@keyframes rise{from{opacity:0;transform:translateY(24px)}}

section.block{padding-block:120px}
@media(max-width:860px){section.block{padding-block:64px}}
.light{background:var(--ivory);color:var(--ink)}
.light .label{color:#8C7650}
.sec-head{display:grid;grid-template-columns:1fr 2fr;gap:32px;margin-bottom:56px}
.sec-head h2{font:300 clamp(32px,4.4vw,56px)/1.2 var(--f-head)}
@media(max-width:860px){.sec-head{grid-template-columns:1fr;gap:16px}}

.rows{border-top:1px solid var(--ivory-2)}
.rowc{display:grid;grid-template-columns:64px 1fr 1fr 120px 40px;gap:24px;align-items:center;padding-block:32px;border-bottom:1px solid var(--ivory-2);text-decoration:none;transition:padding .5s var(--ease)}
.rowc .no{font:500 14px var(--f-head);color:var(--stone)}
.rowc h3{font:400 clamp(24px,3vw,36px) var(--f-head)}
.rowc p{margin:0;color:#6A645A}
.rowc .thumb{width:120px;aspect-ratio:1;background:var(--night);display:grid;place-items:center;transform:scale(.9);opacity:.85;transition:transform .5s var(--ease),opacity .5s var(--ease)}
.rowc .thumb .frame{width:52%}
.rowc i{font-size:24px;transition:transform .5s var(--ease)}
.rowc:hover{padding-inline:16px}.rowc:hover .thumb{transform:scale(1);opacity:1}.rowc:hover i{transform:translate(4px,-4px)}
@media(max-width:760px){.rowc{grid-template-columns:72px 1fr 24px;gap:16px}.rowc .no,.rowc p{display:none}.rowc .thumb{order:-1;width:72px}}

.steps{display:grid;grid-template-columns:repeat(3,1fr);gap:0;list-style:none;margin:0;padding:0;border-top:1px solid #26251F}
.steps li{padding:40px 32px 40px 0;border-right:1px solid #26251F}
.steps li+li{padding-left:32px}.steps li:last-child{border-right:0}
.steps .n{font:200 72px/1 var(--f-head);color:var(--champ)}
.steps h3{font:500 22px var(--f-head);margin:24px 0 8px}
.steps p{margin:0;color:#A9A296}
@media(max-width:860px){.steps{grid-template-columns:1fr}.steps li,.steps li+li{padding:32px 0;border-right:0;border-bottom:1px solid #26251F}}

.gal{display:grid;grid-template-columns:repeat(3,1fr);gap:4px}
.gal figure{margin:0;aspect-ratio:1;background:#E9E3D8;display:grid;place-items:center;position:relative}
.gal figure:nth-child(even){background:#DDD5C7}
.gal .frame{height:64%;width:auto}
.gal figcaption{position:absolute;left:12px;bottom:8px;font-size:12px;color:#8C857A}
@media(max-width:640px){.gal{grid-template-columns:repeat(2,1fr)}}

.craft{display:grid;grid-template-columns:1fr 1fr;gap:72px;align-items:center}
@media(max-width:860px){.craft{grid-template-columns:1fr;gap:40px}}
.craft .q{font:300 clamp(28px,3.4vw,44px)/1.35 var(--f-head);margin:24px 0}
.craft .q b{font-weight:500;color:var(--champ)}
.craft .photo{aspect-ratio:4/5;background:linear-gradient(160deg,#1C1B19,#0B0B0C);border:1px solid #26251F;display:grid;place-items:center;text-align:center;color:var(--stone);font-size:14px}
.craft .photo i{font-size:40px;color:var(--champ);display:block;margin-bottom:8px}
.todo{display:inline-block;border:1px dashed var(--champ);padding:2px 8px;font-size:14px;color:var(--champ)}
.light .todo{border-color:#8C7650;color:#8C7650}

.social{display:grid;grid-template-columns:3fr 2fr;gap:56px}
@media(max-width:960px){.social{grid-template-columns:1fr}}
.clips{display:grid;grid-template-columns:repeat(4,1fr);gap:8px}
@media(max-width:520px){.clips{grid-template-columns:repeat(2,1fr)}}
.clip{aspect-ratio:9/16;background:var(--night);color:var(--champ);display:grid;place-items:center;text-decoration:none;position:relative}
.clip i{font-size:36px}.clip span{position:absolute;left:12px;bottom:8px;font-size:12px;color:var(--stone)}
.review{padding-block:24px;border-bottom:1px solid var(--ivory-2)}
.review .sk{height:8px;background:var(--ivory-2);margin-bottom:8px}.review .sk.s{width:50%}
.review small{color:#8C857A}
.social h3{font:500 14px var(--f-head);letter-spacing:.2em;text-transform:uppercase;margin-bottom:24px;color:#8C7650}

.contact{display:grid;grid-template-columns:1fr 1fr;gap:56px}
@media(max-width:860px){.contact{grid-template-columns:1fr}}
.contact h2{font:300 clamp(32px,4.4vw,56px)/1.2 var(--f-head);margin:16px 0 40px}
.contact dl{display:grid;grid-template-columns:120px 1fr;gap:16px 24px;margin:0 0 40px}
.contact dt{color:var(--stone);font:500 13px var(--f-head);letter-spacing:.14em}
.contact dd{margin:0}.contact dd a{text-decoration:none}
.map{min-height:380px;filter:grayscale(1) contrast(.9)}
.map iframe{width:100%;height:100%;min-height:380px;border:0}
footer{padding-block:40px;border-top:1px solid #26251F;color:var(--stone);font-size:13px}
footer .wrap{display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap}
"""


def build():
    rows = "".join(
        f'<a class="rowc reveal" href="#" data-link="shopee"><span class="no">0{i+1}</span><h3>{t}</h3><p>{d}</p>'
        f'<span class="thumb">{frame(s, m)}</span><i class="ph ph-arrow-up-right"></i></a>'
        for i, (s, m, t, d) in enumerate(CATS))
    steps = "".join(
        f'<li class="reveal"><span class="n">{i+1}</span><h3>{t}</h3><p>{d}</p></li>'
        for i, (t, d) in enumerate(STEPS))
    gal = "".join(f'<figure class="reveal">{frame(s, m)}<figcaption>ภาพตัวอย่าง</figcaption></figure>' for s, m in GALLERY)
    clips = "".join(f'<a class="clip reveal" href="{SHOP["tiktok"]}" target="_blank" rel="noopener"><i class="ph ph-play"></i><span>คลิป {i}</span></a>' for i in range(1, 5))
    rev = "".join('<div class="review reveal"><div class="sk"></div><div class="sk"></div><div class="sk s"></div><small>รอรีวิวจริงจากลูกค้าของร้าน</small></div>' for _ in range(3))

    return f"""<!doctype html>
<html lang="th">
<head>
{HEAD_COMMON}
<title>KT กรอบพระไทยแลนด์ · เลี่ยมกรอบพระ กรอบทอง กรอบเงิน · ดราฟต์ 3</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Anuphan:wght@400;500&family=Bai+Jamjuree:wght@200;300;400;500;600&display=swap">
<style>{CSS}{REVEAL_CSS}</style>
</head>
<body>
<a class="skip" href="#main">ข้ามไปเนื้อหา</a>
{draft_bar(3, "จิวเวลรีสมัยใหม่", "#CBB58C", "#0B0B0C")}
{svg_defs()}
<header class="site"><div class="wrap nav">
  <a class="brand" href="#">KT <span>กรอบพระไทยแลนด์</span></a>
  <nav aria-label="เมนูหลัก"><ul><li><a href="#products">สินค้า</a></li><li><a href="#repair">สั่งทำ</a></li><li><a href="#works">ผลงาน</a></li><li><a href="#about">เกี่ยวกับเรา</a></li><li><a href="#contact">ติดต่อ</a></li></ul></nav>
  <a class="btn btn-line" href="{SHOP["tel_href"]}">{SHOP["tel"]}</a>
</div></header>

<main id="main">
<section class="hero"><div class="wrap">
  <div class="art" aria-hidden="true">{frame("sema", "g")}<small>ภาพวาดตัวอย่าง</small></div>
  <div class="stagger">
    <p class="label">กรอบพระ · ทอง · เงิน · สั่งทำ</p>
    <h1 class="big">กรอบพระ<br><b>งานช่าง</b><br>ทองหลวง</h1>
  </div>
  <div class="row reveal">
    <p>รับเลี่ยมกรอบพระทุกพิมพ์ งานซ่อม และลายสั่งทำเฉพาะองค์ ที่กระทุ่มแบน สมุทรสาคร ส่งรูปพระมาให้ช่างดู แจ้งราคาก่อนเริ่มงานทุกครั้ง</p>
    <div class="ctas"><a class="btn btn-champ" href="{SHOP["chat"]}" target="_blank" rel="noopener">ส่งรูปพระ ขอประเมินราคา <i class="ph ph-arrow-right"></i></a></div>
  </div>
</div></section>

<section class="block light" id="products"><div class="wrap">
  <div class="sec-head reveal"><p class="label">สินค้า</p><h2>เลือกกรอบ แล้วสั่งซื้อที่ Shopee</h2></div>
  <div class="rows">{rows}</div>
</div></section>

<section class="block" id="repair"><div class="wrap">
  <div class="sec-head reveal"><p class="label">งานซ่อม · ลายสั่งทำ</p><h2>สั่งทำกับช่าง ใน 3 ขั้นตอน</h2></div>
  <ol class="steps">{steps}</ol>
  <div class="reveal" style="margin-top:56px"><a class="btn btn-champ" href="{SHOP["chat"]}" target="_blank" rel="noopener">ส่งรูปพระ ขอประเมินราคา <i class="ph ph-arrow-right"></i></a></div>
</div></section>

<section class="block light" id="works"><div class="wrap">
  <div class="sec-head reveal"><p class="label">ผลงาน</p><h2>จากโต๊ะช่างของเรา</h2></div>
  <div class="gal">{gal}</div>
  <p style="color:#8C857A;font-size:14px;margin-top:16px">{PH}</p>
</div></section>

<section class="block" id="about"><div class="wrap craft">
  <div class="photo reveal"><div><i class="ph ph-hammer"></i>รูปทีมช่าง<br>(รอรูปจริงจากร้าน)</div></div>
  <div class="reveal">
    <p class="label">เกี่ยวกับเรา</p>
    <p class="q">ทุกงานซ่อม ลายสั่งทำ<br>โดย<b>ทีมช่างทองหลวง</b></p>
    <p><span class="todo">ประวัติร้านและจุดเด่นของช่าง รอข้อมูลจากร้าน</span></p>
    <a class="btn btn-line" href="{SHOP["fb"]}" target="_blank" rel="noopener" style="margin-top:24px">ดูเพจ Facebook</a>
  </div>
</div></section>

<section class="block light"><div class="wrap social">
  <div><h3 class="reveal">TikTok</h3><div class="clips">{clips}</div></div>
  <div><h3 class="reveal">รีวิวจากลูกค้า</h3>{rev}</div>
</div></section>

<section class="block" id="contact"><div class="wrap contact">
  <div class="reveal">
    <p class="label">ติดต่อ</p>
    <h2>แวะมาที่ร้าน หรือทักแชทได้เลย</h2>
    <dl>
      <dt>ที่อยู่</dt><dd>{SHOP["addr"]}</dd>
      <dt>โทร</dt><dd><a href="{SHOP["tel_href"]}">{SHOP["tel"]}</a></dd>
      <dt>เวลาเปิด</dt><dd><span class="todo">รอข้อมูลเวลาเปิด-ปิด</span></dd>
      <dt>ออนไลน์</dt><dd><a href="{SHOP["fb"]}" target="_blank" rel="noopener">Facebook</a> · <a href="#" data-link="shopee">Shopee</a> · <a href="{SHOP["tiktok"]}" target="_blank" rel="noopener">TikTok</a></dd>
    </dl>
    <a class="btn btn-champ" href="{SHOP["chat"]}" target="_blank" rel="noopener">ทักแชท Facebook <i class="ph ph-arrow-right"></i></a>
  </div>
  <div class="map reveal"><iframe title="แผนที่ร้าน" src="{SHOP["map_embed"]}" loading="lazy"></iframe></div>
</div></section>
</main>
<footer><div class="wrap"><span>© 2569 {SHOP["name"]}</span><span>ดราฟต์โดย ApeDev</span></div></footer>
{REVEAL_JS}
</body>
</html>"""
