import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from shared import svg_defs, frame
import v1, v2, v3

ROOT = os.path.join(os.path.dirname(__file__), "..", "site")

INDEX = """<!doctype html>
<html lang="th">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex">
<title>KT กรอบพระไทยแลนด์ · เลือกแบบหน้าแรก</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Thai:wght@400;500;600&family=Noto+Serif+Thai:wght@600&display=swap">
<style>
:root{--bg:#0E0C09;--card:#17140F;--line:#2A251C;--text:#EFE7D6;--muted:#A59C88;--gold:#D6B06A}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--text);font:400 16px/1.7 "IBM Plex Sans Thai",sans-serif}
.wrap{max-width:1120px;margin:0 auto;padding:56px 24px 80px}
h1{font:600 clamp(28px,4vw,40px)/1.35 "Noto Serif Thai",serif;margin:0 0 8px}
.sub{color:var(--muted);margin:0 0 40px;max-width:40em}
.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:24px}
@media(max-width:860px){.grid{grid-template-columns:1fr}}
a.opt{display:flex;flex-direction:column;text-decoration:none;color:inherit;background:var(--card);border:1px solid var(--line);border-radius:8px;overflow:hidden;transition:border-color .3s}
a.opt:hover,a.opt:focus-visible{border-color:var(--gold);outline:none}
.sw{height:200px;display:grid;place-items:center;position:relative}
.sw svg{height:150px}
.sw .chips{position:absolute;left:16px;bottom:16px;display:flex;gap:8px}
.sw .chips i{width:20px;height:20px;border-radius:50%;border:1px solid rgba(255,255,255,.3)}
.body{padding:24px;display:grid;gap:8px;flex:1}
.body b{font:600 20px "Noto Serif Thai",serif}
.body span{color:var(--muted);font-size:15px}
.tag{justify-self:start;font-size:12px;color:#16120A;background:var(--gold);padding:2px 10px;border-radius:999px}
.go{margin-top:8px;color:var(--gold);font-weight:500}
footer{color:var(--muted);font-size:14px;margin-top:48px}
</style>
</head>
<body>
DEFS
<div class="wrap">
  <h1>KT กรอบพระไทยแลนด์ · แบบหน้าแรก 3 แบบ</h1>
  <p class="sub">ทุกแบบใช้โครงหน้าเดียวกัน ต่างกันที่อารมณ์และการจัดวาง ภาพสินค้าและรีวิวเป็นของจริงที่ร้านส่งมา</p>
  <div class="grid">
    <a class="opt" href="v1-showcase/"><div class="sw" style="background:radial-gradient(60% 70% at 50% 30%,rgba(214,176,106,.25),#0E0C09)">F1<div class="chips"><i style="background:#0E0C09"></i><i style="background:#D6B06A"></i><i style="background:#EFE7D6"></i></div></div>
      <div class="body"><span class="tag">แนะนำ</span><b>1 · ตู้โชว์ร้านทอง</b><span>พื้นดำ ไฟส่องสีทอง กรอบพระเด่นเหมือนวางในตู้กระจก ตรงกับโทนเพจของร้าน</span><span class="go">ดูแบบนี้ →</span></div></a>
    <a class="opt" href="v2-heritage/"><div class="sw" style="background:#4A0F12">F2<div class="chips"><i style="background:#4A0F12"></i><i style="background:#E4BC62"></i><i style="background:#F5EAD3"></i></div></div>
      <div class="body"><b>2 · ช่างหลวง</b><span>แดงชาดกับทองคำเปลว ลายประจำยามคั่นหัวข้อ ให้ความรู้สึกงานช่างไทยโบราณ</span><span class="go">ดูแบบนี้ →</span></div></a>
    <a class="opt" href="v3-modern/"><div class="sw" style="background:#0B0B0C">F3<div class="chips"><i style="background:#0B0B0C"></i><i style="background:#CBB58C"></i><i style="background:#F3EFE8"></i></div></div>
      <div class="body"><b>3 · จิวเวลรีสมัยใหม่</b><span>ดำกับทองแชมเปญ ตัวอักษรใหญ่นำ เรียบหรูแบบร้านเครื่องประดับ</span><span class="go">ดูแบบนี้ →</span></div></a>
  </div>
  <footer>ดราฟต์โดย ApeDev · 2 พ.ย. 2569</footer>
</div>
</body>
</html>"""


def write(path, html):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(html)
    print(path, len(html))


idx = (INDEX.replace("DEFS", svg_defs())
       .replace("F1", frame("arch", "g")).replace("F2", frame("tear", "g")).replace("F3", frame("sema", "g")))
write("index.html", idx)
write("v1-showcase/index.html", v1.build())
write("v2-heritage/index.html", v2.build())
write("v3-modern/index.html", v3.build())
