from shared import *

CSS = """
:root{--bg:#0E0C09;--surface:#17140F;--line:#2A251C;--text:#EFE7D6;--muted:#A59C88;--gold:#D6B06A;--gold-deep:#9C7A3C;
--f-head:"Noto Serif Thai",serif;--f-body:"IBM Plex Sans Thai",sans-serif;--ease:cubic-bezier(.16,1,.3,1)}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--text);font:400 16px/1.75 var(--f-body);-webkit-font-smoothing:antialiased}
a{color:inherit}img,svg{max-width:100%}
.wrap{max-width:1200px;margin:0 auto;padding-inline:24px}
h1,h2,h3{font-family:var(--f-head);font-weight:600;line-height:1.35;margin:0}
.eyebrow{font:500 13px/1.4 var(--f-body);letter-spacing:.12em;color:var(--gold);margin:0 0 16px}
.btn{display:inline-flex;align-items:center;gap:8px;height:56px;padding:0 24px;border-radius:8px;font:600 16px var(--f-body);text-decoration:none;transition:background .3s var(--ease),color .3s var(--ease),transform .3s var(--ease)}
.btn-gold{background:var(--gold);color:#16120A}.btn-gold:hover{background:#E6C484}
.btn-line{border:1px solid var(--line);color:var(--text)}.btn-line:hover{border-color:var(--gold);color:var(--gold)}
.btn:focus-visible,a:focus-visible{outline:2px solid var(--gold);outline-offset:3px}
.btn i{font-size:20px}
.skip{position:absolute;left:-999px}.skip:focus{left:16px;top:16px;background:var(--gold);color:#000;padding:8px 16px;z-index:99}

/* header */
header.site{position:sticky;top:0;z-index:20;background:rgba(14,12,9,.88);backdrop-filter:blur(8px);border-bottom:1px solid var(--line)}
.nav{display:flex;align-items:center;justify-content:space-between;height:72px;gap:16px}
.brand{display:flex;align-items:center;gap:12px;text-decoration:none}
.brand .mark{width:40px;height:40px;border-radius:50%;border:1.5px solid var(--gold);display:grid;place-items:center;font:600 14px var(--f-head);color:var(--gold)}
.brand b{font:600 17px var(--f-head);color:var(--text)}
.nav ul{display:flex;gap:32px;list-style:none;margin:0;padding:0;font-size:15px;color:var(--muted)}
.nav ul a{text-decoration:none}.nav ul a:hover{color:var(--gold)}
.nav .call{height:40px;font-size:14px;padding:0 16px}
@media(max-width:960px){.nav ul{display:none}}

/* hero */
.hero{position:relative;overflow:hidden;padding-block:96px 120px;--mx:65%;--my:35%}
.hero::before{content:"";position:absolute;inset:0;background:radial-gradient(520px 420px at var(--mx) var(--my),rgba(214,176,106,.22),transparent 70%);pointer-events:none;transition:background .2s}
.hero .grid{position:relative;display:grid;grid-template-columns:1.05fr .95fr;gap:48px;align-items:center}
.hero h1{font-size:clamp(30px,5.2vw,60px);font-weight:600}
.hero h1 em{display:inline-block}
.hero h1 em{font-style:normal;color:var(--gold)}
.hero p.lead{color:var(--muted);font-size:18px;max-width:30em;margin:24px 0 40px}
.hero .ctas{display:flex;flex-wrap:wrap;gap:16px}
.hero .trust{display:flex;flex-wrap:wrap;gap:8px 24px;margin-top:40px;color:var(--muted);font-size:14px}
.hero .trust span{display:inline-flex;align-items:center;gap:8px}.hero .trust i{color:var(--gold);font-size:18px}
.case{position:relative;aspect-ratio:4/5;max-width:440px;justify-self:center;width:100%}
.case .shelf{position:absolute;left:4%;right:4%;bottom:6%;height:14px;border-radius:2px;background:linear-gradient(#3a3226,#1a1611);box-shadow:0 1px 0 rgba(255,255,255,.08) inset}
.case .glow{position:absolute;left:10%;right:10%;bottom:8%;height:40%;background:radial-gradient(closest-side,rgba(214,176,106,.25),transparent);filter:blur(8px)}
.case .frame{position:absolute;left:18%;width:64%;bottom:9%;filter:drop-shadow(0 24px 32px rgba(0,0,0,.6))}
.case .tag{position:absolute;right:0;top:12%;background:var(--surface);border:1px solid var(--line);border-radius:8px;padding:12px 16px;font-size:13px;color:var(--muted);line-height:1.5}
.case .tag b{display:block;color:var(--text);font:600 15px var(--f-head)}
.stagger>*{animation:rise .9s var(--ease) both}.stagger>*:nth-child(2){animation-delay:.12s}.stagger>*:nth-child(3){animation-delay:.24s}.stagger>*:nth-child(4){animation-delay:.36s}
@keyframes rise{from{opacity:0;transform:translateY(16px)}}
@media(max-width:860px){.hero{padding-block:56px 72px}.hero .grid{grid-template-columns:1fr}.case{max-width:320px;order:-1}}

/* sections */
section.block{padding-block:96px;border-top:1px solid var(--line)}
@media(max-width:860px){section.block{padding-block:56px}}
.head-row{display:flex;justify-content:space-between;align-items:end;gap:24px;flex-wrap:wrap;margin-bottom:48px}
.head-row h2{font-size:clamp(28px,3.4vw,40px)}
.head-row p{color:var(--muted);max-width:28em;margin:0}

.cats{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}
@media(max-width:960px){.cats{grid-template-columns:repeat(2,1fr)}}
@media(max-width:520px){.cats{gap:8px}.cat .body{padding:16px}.cat h3{font-size:19px}.cat p{font-size:14px}}
@media(max-width:520px){.brand b{font-size:15px}.nav .call{width:40px;padding:0;justify-content:center}.nav .call .t{display:none}}
.brand b,.nav .btn{white-space:nowrap}

.cat{position:relative;display:flex;flex-direction:column;background:var(--surface);border:1px solid var(--line);border-radius:8px;overflow:hidden;text-decoration:none;transition:border-color .3s var(--ease)}
.cat:hover{border-color:var(--gold-deep)}
.cat .pic{position:relative;aspect-ratio:1/1;display:grid;place-items:center;background:radial-gradient(60% 55% at 50% 0%,rgba(214,176,106,.18),transparent 70%)}
.cat .pic::after{content:"";position:absolute;left:0;right:0;top:0;height:2px;background:linear-gradient(90deg,transparent,var(--gold),transparent);opacity:.6}
.cat .frame{width:48%;transition:transform .5s var(--ease)}
.cat:hover .frame{transform:translateY(-6px)}
.cat .body{padding:24px;display:flex;flex-direction:column;gap:8px;flex:1}
.cat h3{font-size:22px}
.cat p{margin:0;color:var(--muted);font-size:15px}
.cat .go{margin-top:auto;padding-top:16px;display:flex;align-items:center;gap:8px;color:var(--gold);font-size:14px;font-weight:500}

.steps{display:grid;grid-template-columns:repeat(3,1fr);gap:48px;counter-reset:s;list-style:none;margin:0;padding:0}
@media(max-width:860px){.steps{grid-template-columns:1fr;gap:32px}}
.steps li{border-top:1px solid var(--gold-deep);padding-top:24px}
.steps .n{font:600 14px var(--f-body);color:var(--gold);letter-spacing:.12em}
.steps h3{font-size:22px;margin:8px 0}
.steps p{margin:0;color:var(--muted)}
.steps-cta{margin-top:48px}

.gal{display:grid;grid-template-columns:repeat(6,1fr);grid-auto-rows:160px;gap:16px}
.gal figure{margin:0;position:relative;border-radius:8px;overflow:hidden;background:var(--surface);border:1px solid var(--line);display:grid;place-items:center}
.gal figure:nth-child(1){grid-column:span 3;grid-row:span 2}.gal figure:nth-child(2){grid-column:span 3}
.gal figure:nth-child(3){grid-column:span 2}.gal figure:nth-child(4){grid-column:span 1;grid-row:span 2}
.gal figure:nth-child(5){grid-column:span 2;grid-row:span 1}.gal figure:nth-child(6){grid-column:span 2}
.gal .frame{height:78%;width:auto}
.gal figcaption{position:absolute;left:8px;bottom:8px;font-size:12px;color:var(--muted);background:rgba(14,12,9,.7);padding:2px 8px;border-radius:4px}
@media(max-width:760px){.gal{grid-template-columns:repeat(2,1fr);grid-auto-rows:180px}.gal figure{grid-column:auto!important;grid-row:auto!important}.gal figure:nth-child(1){grid-column:span 2!important}}

.craft{display:grid;grid-template-columns:5fr 7fr;gap:56px;align-items:center}
@media(max-width:860px){.craft{grid-template-columns:1fr;gap:32px}}
.craft .photo{aspect-ratio:4/5;border-radius:8px;background:repeating-linear-gradient(135deg,#17140F 0 16px,#1B1812 16px 32px);border:1px solid var(--line);display:grid;place-items:center;color:var(--muted);text-align:center;font-size:14px;padding:24px}
.craft .photo i{font-size:48px;color:var(--gold-deep);display:block;margin-bottom:8px}
.craft h2{font-size:clamp(28px,3.4vw,40px);margin-bottom:24px}
.craft blockquote{margin:0 0 24px;padding-left:24px;border-left:2px solid var(--gold);font:500 20px/1.6 var(--f-head);color:var(--gold)}
.craft p{color:var(--muted);margin:0 0 16px}
.todo{display:inline-block;background:rgba(214,176,106,.12);color:var(--gold);border:1px dashed var(--gold-deep);border-radius:4px;padding:2px 8px;font-size:14px}

.social{display:grid;grid-template-columns:7fr 5fr;gap:48px}
@media(max-width:960px){.social{grid-template-columns:1fr}}
.clips{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}
@media(max-width:520px){.clips{grid-template-columns:repeat(2,1fr)}}
.clip{aspect-ratio:9/16;border-radius:8px;background:linear-gradient(180deg,#1E1A13,#0E0C09);border:1px solid var(--line);position:relative;display:grid;place-items:center;text-decoration:none}
.clip i{font-size:40px;color:var(--gold)}
.clip span{position:absolute;left:8px;right:8px;bottom:8px;font-size:12px;color:var(--muted)}
.reviews{display:grid;gap:16px}
.review{background:var(--surface);border:1px solid var(--line);border-radius:8px;padding:24px}
.review .sk{height:10px;border-radius:4px;background:#2A251C;margin-bottom:8px}
.review .sk.s{width:60%}
.review small{color:var(--muted);font-size:13px}
.social h3{font-size:22px;margin-bottom:24px;display:flex;align-items:center;gap:8px}

.contact{display:grid;grid-template-columns:1fr 1fr;gap:48px}
@media(max-width:860px){.contact{grid-template-columns:1fr}}
.contact dl{margin:0 0 40px;display:grid;gap:24px}
.contact dt{color:var(--gold);font-size:13px;letter-spacing:.12em;margin-bottom:4px}
.contact dd{margin:0;font-size:18px}
.contact dd a{text-decoration:none}.contact dd a:hover{color:var(--gold)}
.map{border:1px solid var(--line);border-radius:8px;overflow:hidden;min-height:360px}
.map iframe{width:100%;height:100%;min-height:360px;border:0;filter:grayscale(.6) invert(.9) hue-rotate(180deg) contrast(.9)}

footer{border-top:1px solid var(--line);padding-block:40px;color:var(--muted);font-size:14px}
footer .wrap{display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap}
.fab{position:fixed;right:16px;bottom:16px;z-index:30;width:56px;height:56px;border-radius:50%;background:var(--gold);color:#16120A;display:grid;place-items:center;font-size:26px;box-shadow:0 8px 24px rgba(0,0,0,.5)}
@media(min-width:861px){.fab{display:none}}
"""

def build():
    cats = "".join(
        f'<a class="cat reveal" href="#" data-link="shopee"><div class="pic">{frame(s, m)}</div>'
        f'<div class="body"><h3>{t}</h3><p>{d}</p><span class="go">ดูสินค้าใน Shopee <i class="ph ph-arrow-up-right"></i></span></div></a>'
        for s, m, t, d in CATS)
    steps = "".join(
        f'<li class="reveal"><span class="n">ขั้นที่ {i+1}</span><h3>{t}</h3><p>{d}</p></li>'
        for i, (t, d) in enumerate(STEPS))
    gal = "".join(f'<figure class="reveal">{frame(s, m)}<figcaption>ภาพตัวอย่าง</figcaption></figure>' for s, m in GALLERY)
    clips = "".join(f'<a class="clip reveal" href="{SHOP["tiktok"]}" target="_blank" rel="noopener"><i class="ph-fill ph-play-circle"></i><span>คลิป TikTok {i}</span></a>' for i in range(1, 5))
    rev = "".join('<div class="review reveal"><div class="sk"></div><div class="sk"></div><div class="sk s"></div><small>รอรีวิวจริงจากลูกค้าของร้าน</small></div>' for _ in range(3))

    return f"""<!doctype html>
<html lang="th">
<head>
{HEAD_COMMON}
<title>KT กรอบพระไทยแลนด์ · เลี่ยมกรอบพระ กรอบทอง กรอบเงิน · ดราฟต์ 1</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Thai:wght@400;500;600&family=Noto+Serif+Thai:wght@500;600&display=swap">
<style>{CSS}{REVEAL_CSS}</style>
</head>
<body>
<a class="skip" href="#main">ข้ามไปเนื้อหา</a>
{draft_bar(1, "ตู้โชว์ร้านทอง", "#D6B06A", "#16120A")}
{svg_defs()}
<header class="site"><div class="wrap nav">
  <a class="brand" href="#"><span class="mark">KT</span><b>{SHOP["name"]}</b></a>
  <nav aria-label="เมนูหลัก"><ul><li><a href="#products">สินค้า</a></li><li><a href="#repair">งานซ่อม/สั่งทำ</a></li><li><a href="#works">ผลงาน</a></li><li><a href="#about">เกี่ยวกับเรา</a></li><li><a href="#contact">ติดต่อ</a></li></ul></nav>
  <a class="btn btn-line call" href="{SHOP["tel_href"]}"><i class="ph ph-phone"></i><span class="t">{SHOP["tel"]}</span></a>
</div></header>

<main id="main">
<section class="hero" id="hero"><div class="wrap grid">
  <div class="stagger">
    <p class="eyebrow">กรอบพระงานพรีเมี่ยม · กระทุ่มแบน สมุทรสาคร</p>
    <h1>เลี่ยมกรอบพระ<br>ด้วยฝีมือ<em>ช่างทองหลวง</em></h1>
    <p class="lead">กรอบพระงานพรีเมี่ยม {SHOP["services"]} ส่งรูปพระมาให้ช่างดู แจ้งราคาก่อนเริ่มงานทุกครั้ง</p>
    <div class="ctas">
      <a class="btn btn-gold" href="{SHOP["chat"]}" target="_blank" rel="noopener"><i class="ph ph-camera"></i>ส่งรูปพระ ขอประเมินราคา</a>
      <a class="btn btn-line" href="#products">ดูสินค้า</a>
    </div>
  </div>
  <div class="case" aria-hidden="true">
    <div class="glow"></div><div class="shelf"></div>
    {frame("arch", "g")}
    <div class="tag"><b>งานทองตามพิมพ์</b>ภาพวาดตัวอย่าง</div>
  </div>
</div></section>

<section class="block" id="products"><div class="wrap">
  <div class="head-row reveal"><div><p class="eyebrow">สินค้า</p><h2>เลือกกรอบตามแบบที่ใช่</h2></div><p>ดูสินค้าทั้งหมดและสั่งซื้อได้ที่ร้าน Shopee ของเรา</p></div>
  <div class="cats">{cats}</div>
</div></section>

<section class="block" id="repair"><div class="wrap">
  <div class="head-row reveal"><div><p class="eyebrow">งานซ่อม · ลายสั่งทำ</p><h2>สั่งทำง่าย 3 ขั้นตอน</h2></div><p>ไม่ต้องเดินทางมาร้าน เริ่มจากส่งรูปพระทางแชท</p></div>
  <ol class="steps">{steps}</ol>
  <div class="steps-cta reveal"><a class="btn btn-gold" href="{SHOP["chat"]}" target="_blank" rel="noopener"><i class="ph ph-camera"></i>ส่งรูปพระ ขอประเมินราคา</a></div>
</div></section>

<section class="block" id="works"><div class="wrap">
  <div class="head-row reveal"><div><p class="eyebrow">ผลงาน</p><h2>งานจากโต๊ะช่างของเรา</h2></div><p>{PH}</p></div>
  <div class="gal">{gal}</div>
</div></section>

<section class="block" id="about"><div class="wrap craft">
  <div class="photo reveal"><div><i class="ph ph-hammer"></i>รูปทีมช่างที่โต๊ะทำงาน<br>(รอรูปจริงจากร้าน)</div></div>
  <div class="reveal">
    <p class="eyebrow">เกี่ยวกับเรา</p>
    <h2>ทีมช่างทองหลวง</h2>
    <blockquote>{SHOP["tag"]}</blockquote>
    <p><span class="todo">ประวัติร้านและจุดเด่นของช่าง รอข้อมูลจากร้าน</span></p>
    <a class="btn btn-line" href="{SHOP["fb"]}" target="_blank" rel="noopener"><i class="ph ph-facebook-logo"></i>ดูเพจ Facebook</a>
  </div>
</div></section>

<section class="block"><div class="wrap social">
  <div><h3 class="reveal"><i class="ph ph-tiktok-logo"></i>คลิปงานจาก TikTok</h3><div class="clips">{clips}</div></div>
  <div><h3 class="reveal"><i class="ph ph-chat-circle-text"></i>รีวิวจากลูกค้า</h3><div class="reviews">{rev}</div></div>
</div></section>

<section class="block" id="contact"><div class="wrap contact">
  <div class="reveal">
    <p class="eyebrow">ติดต่อ</p>
    <h2 style="font-size:clamp(28px,3.4vw,40px);margin-bottom:40px">มาที่ร้าน หรือทักแชทได้เลย</h2>
    <dl>
      <div><dt>ที่อยู่</dt><dd>{SHOP["addr"]}</dd></div>
      <div><dt>โทร</dt><dd><a href="{SHOP["tel_href"]}">{SHOP["tel"]}</a> · <a href="{SHOP["tel2_href"]}">{SHOP["tel2"]}</a> · <a href="{SHOP["tel3_href"]}">{SHOP["tel3"]}</a></dd></div>
      <div><dt>เวลาเปิด</dt><dd>{SHOP["hours"]}</dd></div>
      <div><dt>หน้าร้าน</dt><dd><a href="{SHOP["gmaps"]}" target="_blank" rel="noopener">{SHOP["store"]}</a></dd></div>
    </dl>
    <div style="display:flex;flex-wrap:wrap;gap:16px">
      <a class="btn btn-gold" href="{SHOP["chat"]}" target="_blank" rel="noopener"><i class="ph ph-messenger-logo"></i>ทักแชท Facebook</a>
      <a class="btn btn-line" href="#" data-link="shopee"><i class="ph ph-storefront"></i>Shopee</a>
      <a class="btn btn-line" href="{SHOP["tiktok"]}" target="_blank" rel="noopener"><i class="ph ph-tiktok-logo"></i>TikTok</a>
    </div>
  </div>
  <div class="map reveal"><iframe title="แผนที่ร้าน KT กรอบพระไทยแลนด์" src="{SHOP["map_embed"]}" loading="lazy"></iframe></div>
</div></section>
</main>

<footer><div class="wrap"><span>© 2569 {SHOP["name"]} · {SHOP["addr"]}</span><span>ดราฟต์โดย ApeDev</span></div></footer>
<a class="fab" href="{SHOP["chat"]}" target="_blank" rel="noopener" aria-label="ทักแชทส่งรูปพระ"><i class="ph-fill ph-messenger-logo"></i></a>
{REVEAL_JS}
<script>
(function(){{
  var h=document.getElementById('hero');
  if(!h||window.matchMedia('(prefers-reduced-motion: reduce)').matches||!window.matchMedia('(pointer:fine)').matches)return;
  h.addEventListener('pointermove',function(e){{var r=h.getBoundingClientRect();h.style.setProperty('--mx',((e.clientX-r.left)/r.width*100)+'%');h.style.setProperty('--my',((e.clientY-r.top)/r.height*100)+'%');}});
}})();
</script>
</body>
</html>"""
