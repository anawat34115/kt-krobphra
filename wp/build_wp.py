# KT กรอบพระไทยแลนด์ — Elementor native builder (widgets only, no custom CSS/JS)
# Output: site/wp-build/*.json (served by Vercel with CORS so the WP admin can fetch + import them)
import json, os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "build"))
from shared import SHOP, STEPS, REVIEWS
import kt_site as K

random.seed(20261117)
ASSET = "https://kt-krobphra.vercel.app/assets"
OUT = os.path.join(HERE, "..", "site", "wp-build")

BG = '#0E0C09'; SF = '#17140F'; LN = '#2A251C'; TX = '#EFE7D6'; MU = '#A59C88'
GD = '#D6B06A'; GDD = '#9C7A3C'; ON = '#16120A'; GH = '#E6C484'
HEAD = 'Noto Serif Thai'; BODY = 'IBM Plex Sans Thai'
MENU = "%e0%b9%80%e0%b8%a1%e0%b8%99%e0%b8%b9%e0%b8%ab%e0%b8%a5%e0%b8%b1%e0%b8%81"

_ids = set()
def nid():
    while True:
        i = '%07x' % random.getrandbits(28)
        if i not in _ids:
            _ids.add(i); return i
def D(t, r=None, b=None, l=None, unit='px'):
    r = t if r is None else r; b = t if b is None else b; l = r if l is None else l
    return {"unit": unit, "top": str(t), "right": str(r), "bottom": str(b), "left": str(l), "isLinked": (t == r == b == l)}
def S(v, unit='px'): return {"unit": unit, "size": v, "sizes": []}
def GAP(v, r=None):
    r = v if r is None else r
    return {"column": str(v), "row": str(r), "isLinked": v == r, "unit": "px", "size": v}
def L(url):
    ext = "on" if url.startswith("http") else ""
    return {"url": url, "is_external": ext, "nofollow": "", "custom_attributes": ""}
def typo(fam, size, weight, lh=None, ls=None, tab=None, mob=None, pre='typography'):
    d = {f"{pre}_typography": "custom", f"{pre}_font_family": fam, f"{pre}_font_weight": str(weight), f"{pre}_font_size": S(size)}
    if tab: d[f"{pre}_font_size_tablet"] = S(tab)
    if mob: d[f"{pre}_font_size_mobile"] = S(mob)
    if lh: d[f"{pre}_line_height"] = S(lh, 'em')
    if ls is not None: d[f"{pre}_letter_spacing"] = S(ls)
    return d
def W(kind, s): return {"id": nid(), "elType": "widget", "widgetType": kind, "settings": s, "elements": []}
def C(s, ch=None, tag=None):
    base = {"content_width": "full", "flex_direction": "column", "padding": D(0)}
    base.update(s)
    if tag: base["html_tag"] = tag
    return {"id": nid(), "elType": "container", "settings": base, "elements": ch or [], "isInner": True}
def IMG(path): return {"url": f"{ASSET}/{path}", "id": "", "alt": "", "source": "library"}
def FA(v, lib='fa-solid'): return {"value": v, "library": lib}

def H(text, tag, color, size, weight=600, fam=HEAD, lh=1.35, ls=0, tab=None, mob=None, align='start', extra=None, link=None):
    s = {"title": text, "header_size": tag, "title_color": color, "align": align}
    s.update(typo(fam, size, weight, lh, ls, tab, mob))
    if link: s["link"] = L(link)
    if extra: s.update(extra)
    return W('heading', s)
def P(html, color=MU, size=17, tab=16, mob=16, align='start', extra=None, lh=1.75):
    s = {"editor": html, "text_color": color, "align": align}
    s.update(typo(BODY, size, 400, lh, 0, tab, mob))
    if extra: s.update(extra)
    return W('text-editor', s)
def EYE(t, align='start'): return H(t, 'p', GD, 13, 500, BODY, 1.4, 1.6, None, None, align)
def BTN(text, url, variant='gold', icon=None, extra=None, small=False):
    s = {"text": text, "link": L(url), "text_padding": D(12, 20) if small else D(18, 24), "border_radius": D(8),
         "border_border": "solid", "border_width": D(1), "_element_width": "auto",
         "background_background": "classic", "button_background_hover_background": "classic"}
    s.update(typo(BODY, 15 if small else 16, 600, 1.25, 0))
    if icon: s.update({"selected_icon": icon, "icon_align": "row", "icon_indent": S(8)})
    if variant == 'gold':
        s.update({"background_color": GD, "button_text_color": ON, "border_color": GD,
                  "hover_color": ON, "button_background_hover_color": GH, "button_hover_border_color": GH})
    else:
        s.update({"background_color": "rgba(0,0,0,0)", "button_text_color": TX, "border_color": LN,
                  "hover_color": GD, "button_background_hover_color": "rgba(0,0,0,0)", "button_hover_border_color": GD})
    if extra: s.update(extra)
    return W('button', s)
def CHAT(label="ส่งขนาดพระ/แบบที่ชอบ เพื่อประเมินราคา", extra=None):
    return BTN(label, SHOP["chat"], 'gold', FA('fab fa-facebook-messenger', 'fa-brands'), extra)
def SHOPEE(label="สั่งใน Shopee"): return BTN(label, SHOP["shopee"], 'line', FA('fas fa-store'))
def ROW(ch, gap=16, wrap=True, justify=None, align='center', extra=None):
    s = {"flex_direction": "row", "flex_wrap": "wrap" if wrap else "nowrap", "flex_gap": GAP(gap), "flex_align_items": align, "width": S(100, '%')}
    if justify: s["flex_justify_content"] = justify
    if extra: s.update(extra)
    return C(s, ch)
def IMGW(path, alt_w=None, radius=8, extra=None, link=None, lightbox=False):
    s = {"image": IMG(path), "image_size": "full", "width": S(100, '%'), "image_border_radius": D(radius),
         "image_border_border": "solid", "image_border_width": D(1), "image_border_color": LN}
    if link: s.update({"link_to": "custom", "link": L(link)})
    if lightbox: s.update({"link_to": "file", "open_lightbox": "yes"})
    if extra: s.update(extra)
    return W('image', s)

def band(children, bg=BG, pad=(96, 64, 56), anchor=None, top=True, extra=None, gap=48):
    inner = C({"content_width": "boxed", "boxed_width": S(1200), "flex_gap": GAP(gap), "flex_gap_mobile": GAP(32),
               "padding": D(0, 24), "padding_mobile": D(0, 16), "width": S(100, '%')}, children)
    s = {"flex_align_items": "center", "background_background": "classic", "background_color": bg,
         "padding": D(pad[0], 0), "padding_tablet": D(pad[1], 0), "padding_mobile": D(pad[2], 0)}
    if top: s.update({"border_border": "solid", "border_width": D(1, 0, 0, 0), "border_color": LN})
    if anchor: s["_element_id"] = anchor
    if extra: s.update(extra)
    e = C(s, [inner], 'section'); e['isInner'] = False; return e

def headrow(eye, h2, p=None):
    left = C({"flex_gap": GAP(12), "width": S(55, '%'), "width_tablet": S(100, '%'), "width_mobile": S(100, '%')},
             [EYE(eye), H(h2, 'h2', TX, 40, 600, HEAD, 1.35, 0, 34, 28)])
    ch = [left]
    if p: ch.append(C({"width": S(40, '%'), "width_tablet": S(100, '%'), "width_mobile": S(100, '%')}, [P(p, MU, 17, 16, 16)]))
    return ROW(ch, 24, True, 'space-between', 'flex-end')

def pills(items):
    out = []
    for t, u in items:
        out.append(BTN(t, u, 'line', None, {"text_padding": D(8, 16), "border_radius": D(999), "button_text_color": MU,
                                             **typo(BODY, 14, 400, 1.4, 0)}, True))
    return ROW(out, 8)

def page_head(crumb, h1, lead):
    c = C({"flex_gap": GAP(16), "width": S(100, '%'), "max_width": S(820)}, [
        P(f'<a href="/">หน้าแรก</a> / {crumb}', MU, 13, 13, 13),
        H(h1, 'h1', TX, 48, 600, HEAD, 1.35, 0, 40, 30),
        P(lead, MU, 18, 17, 16)])
    return band([c], BG, (72, 56, 40), top=False,
                extra={"background_background": "gradient", "background_color": "#1E1A12", "background_color_b": BG,
                       "background_gradient_type": "radial", "background_gradient_position": "top right",
                       "background_color_stop": S(0, '%'), "background_color_b_stop": S(70, '%')})

def steps_row():
    cols = []
    for i, (t, d) in enumerate(STEPS):
        cols.append(C({"flex_gap": GAP(8), "width": S(31, '%'), "width_tablet": S(100, '%'), "width_mobile": S(100, '%'),
                       "padding": D(24, 0, 0, 0), "border_border": "solid", "border_width": D(1, 0, 0, 0), "border_color": GDD}, [
            H(f'ขั้นที่ {i+1}', 'p', GD, 14, 600, BODY, 1.4, 1.6), H(t, 'h3', TX, 22, 600, HEAD, 1.4), P(d, MU, 16, 16, 16)]))
    return ROW(cols, 48, True, None, 'stretch', {"flex_gap_tablet": GAP(32)})

def contact_block(h2="มาที่ร้าน หรือทักแชทได้เลย", anchor="contact"):
    def item(dt, dd):
        return C({"flex_gap": GAP(4)}, [H(dt, 'p', GD, 13, 500, BODY, 1.4, 1.6), P(dd, TX, 18, 18, 17, lh=1.6)])
    a = ''
    left = C({"flex_gap": GAP(24), "width": S(48, '%'), "width_tablet": S(100, '%'), "width_mobile": S(100, '%')}, [
        EYE('ติดต่อ'), H(h2, 'h2', TX, 40, 600, HEAD, 1.35, 0, 34, 28),
        item('ที่อยู่', SHOP["addr"]),
        item('โทร', f'<a {a} href="{SHOP["tel_href"]}">{SHOP["tel"]}</a> · <a {a} href="{SHOP["tel2_href"]}">{SHOP["tel2"]}</a> · <a {a} href="{SHOP["tel3_href"]}">{SHOP["tel3"]}</a>'),
        item('เวลาเปิด', SHOP["hours"]),
        item('หน้าร้าน', f'<a {a} href="{SHOP["gmaps"]}" target="_blank" rel="noopener">{SHOP["store"]}</a>'),
        ROW([BTN('ทักแชท Facebook', SHOP["chat"], 'gold', FA('fab fa-facebook-messenger', 'fa-brands')),
             BTN('Shopee', SHOP["shopee"], 'line', FA('fas fa-store')),
             BTN('TikTok', SHOP["tiktok"], 'line', FA('fab fa-tiktok', 'fa-brands'))], 16)])
    mp = W('google_maps', {"address": "13.6534902,100.2648441", "zoom": S(17), "height": S(440), "height_mobile": S(320),
                           "_border_radius": D(8), "_border_border": "solid", "_border_width": D(1), "_border_color": LN})
    right = C({"width": S(48, '%'), "width_tablet": S(100, '%'), "width_mobile": S(100, '%')}, [mp])
    return band([ROW([left, right], 48, True, 'space-between', 'flex-start')], BG, anchor=anchor)

def cta_band():
    c = C({"flex_align_items": "center", "flex_gap": GAP(16), "width": S(100, '%')}, [
        H('มีพระอยากเลี่ยม ส่งรูปมาให้ช่างดูได้เลย', 'h2', TX, 36, 600, HEAD, 1.4, 0, 30, 26, 'center'),
        P('ถ่ายรูปพระด้านหน้าและด้านหลัง บอกงบที่ตั้งไว้ ช่างแจ้งราคาก่อนเริ่มงานทุกครั้ง', MU, 17, 17, 16, 'center',
          {"_element_width": "initial", "_element_custom_width": S(560), "_element_custom_width_mobile": S(100, '%')}),
        ROW([CHAT(), SHOPEE('ดูร้านใน Shopee')], 16, True, 'center', 'center', {"_margin": D(16, 0, 0, 0)})])
    return band([c], BG, (72, 64, 56), extra={"background_background": "gradient", "background_color": BG, "background_color_b": "#221D13",
                                              "background_gradient_type": "radial", "background_gradient_position": "bottom center",
                                              "background_color_stop": S(60, '%'), "background_color_b_stop": S(100, '%')})

def card(img, title, desc, url):
    return C({"width": S(31.5, '%'), "width_tablet": S(100, '%'), "width_mobile": S(100, '%'), "background_background": "classic",
              "background_color": SF, "border_border": "solid", "border_width": D(1), "border_color": LN, "border_radius": D(8),
              "link": L(url), "flex_gap": GAP(0)}, [
        IMGW(f'img/wp/{img}', radius=0, extra={"image_border_border": "", "height": S(240), "object-fit": "cover"}),
        C({"padding": D(20), "flex_gap": GAP(8)}, [H(title, 'h3', TX, 22, 600, HEAD, 1.4, link=url), P(desc, MU, 15, 15, 15)])])

def note(title, body):
    return C({"padding": D(20, 24), "background_background": "classic", "background_color": SF, "border_border": "solid",
              "border_width": D(1, 1, 1, 2), "border_color": LN, "border_radius": D(8), "flex_gap": GAP(4), "width": S(100, '%')},
             [H(title, 'p', TX, 17, 600, BODY, 1.5), P(body, MU, 16, 16, 15)])

# ---------------------------------------------------------------- header / footer (HFE templates)
def header():
    logo = W('image', {"image": IMG('logo/kt-mark-192.png'), "image_size": "full", "width": S(44), "link_to": "custom", "link": L('/'),
                       "_element_width": "auto"})
    name = H('กรอบพระไทยแลนด์', 'p', TX, 17, 600, HEAD, 1.3, 0, None, 15, 'start', {"_element_width": "auto"}, '/')
    brand = C({"flex_direction": "row", "flex_wrap": "nowrap", "flex_wrap_mobile": "nowrap", "flex_align_items": "center",
               "flex_gap": GAP(12), "width": S(24, '%'), "width_tablet": S(50, '%'), "width_mobile": S(60, '%')}, [logo, name])
    nav = W('navigation-menu', {"menu": MENU, "layout": "horizontal", "navmenu_align": "right", "dropdown": "tablet",
                                "resp_align": "left", "full_width_dropdown": "yes", "hamburger_align": "right",
                                "padding_horizontal_menu_item": S(10), "padding_vertical_menu_item": S(8), "menu_space_between": S(4),
                                **typo(BODY, 15, 500, 1.4, 0, None, None, 'menu_typography'),
                                "color_menu_item": MU, "color_menu_item_hover": GD, "color_menu_item_active": GD,
                                "color_dropdown_item": TX, "background_color_dropdown_item": SF,
                                "color_dropdown_item_hover": GD, "background_color_dropdown_item_hover": "#201C15",
                                "color_dropdown_item_active": GD, "background_color_dropdown_item_active": "#201C15",
                                **typo(BODY, 16, 500, 1.4, 0, None, None, 'dropdown_typography'),
                                "padding_horizontal_dropdown_item": S(16), "padding_vertical_dropdown_item": S(14),
                                "distance_from_menu": S(16), "dropdown_divider_border": "solid", "divider_border_color": LN,
                                "toggle_color": TX, "toggle_background_color": "rgba(0,0,0,0)", "toggle_hover_color": GD,
                                "toggle_size": S(22), "toggle_border_width": S(1), "toggle_border_radius": S(8),
                                "_element_width": "auto", "_flex_grow": "1"})
    call = BTN(SHOP["tel"], SHOP["tel_href"], 'line', FA('fas fa-phone-alt'), {"hide_mobile": "hidden-mobile"}, True)
    right = C({"flex_direction": "row", "flex_wrap": "nowrap", "flex_wrap_mobile": "nowrap", "flex_align_items": "center",
               "flex_justify_content": "flex-end", "flex_gap": GAP(16), "width": S(74, '%'), "width_tablet": S(48, '%'), "width_mobile": S(38, '%')},
              [nav, call])
    row = C({"content_width": "boxed", "boxed_width": S(1200), "flex_direction": "row", "flex_wrap": "nowrap", "flex_wrap_mobile": "nowrap",
             "flex_justify_content": "space-between", "flex_align_items": "center", "width": S(100, '%'),
             "padding": D(12, 24), "padding_mobile": D(10, 16)}, [brand, right])
    e = C({"flex_align_items": "center", "background_background": "classic", "background_color": BG,
           "border_border": "solid", "border_width": D(0, 0, 1, 0), "border_color": LN, "z_index": 20}, [row], 'header')
    e['isInner'] = False
    return e

def footer():
    a = ''
    top = ROW([W('image', {"image": IMG('logo/kt-mark-192.png'), "image_size": "full", "width": S(88), "_element_width": "auto"}),
               C({"flex_gap": GAP(4), "_element_width": "auto", "width": S(70, '%'), "width_mobile": S(100, '%')}, [
                   H(SHOP["name"], 'p', TX, 17, 600, HEAD, 1.4),
                   P(f'{SHOP["addr"]}<br>โทร <a {a} href="{SHOP["tel_href"]}">{SHOP["tel"]}</a> · {SHOP["hours"]}', MU, 15, 15, 14, lh=1.7)])], 24)
    links = W('icon-list', {"view": "inline", "icon_list": [{"text": t, "link": L(u), "selected_icon": {"value": "", "library": ""}, "_id": nid()} for u, t in K.NAV],
                            "space_between": S(20), "text_color": MU, "text_color_hover": GD,
                            **typo(BODY, 15, 400, 1.6, 0, None, None, 'icon_typography')})
    copy = P(f'© 2569 {SHOP["name"]}', MU, 14, 14, 13)
    fab = W('button', {"text": "", "link": L(SHOP["chat"]), "selected_icon": FA('fab fa-facebook-messenger', 'fa-brands'),
                       "background_background": "classic", "background_color": GD, "button_text_color": ON,
                       "text_padding": D(16), "border_radius": D(999), **typo(BODY, 24, 600, 1, 0),
                       "_position": "fixed", "_offset_orientation_h": "end", "_offset_x_end": S(16), "_offset_orientation_v": "end",
                       "_offset_y_end": S(16), "_z_index": 30, "hide_desktop": "hidden-desktop",
                       "_box_shadow_box_shadow_type": "yes", "_box_shadow_box_shadow": {"horizontal": 0, "vertical": 8, "blur": 24, "spread": 0, "color": "rgba(0,0,0,0.5)"}})
    e = band([top, links, copy, fab], BG, (56, 48, 40), gap=24)
    e['settings']['html_tag'] = 'footer'
    return e

# ---------------------------------------------------------------- pages
def home():
    h1 = 'เลี่ยมกรอบพระ<br>ลายสั่งทำโดย'
    trust = W('icon-list', {"view": "inline", "icon_list": [
        {"text": "ก่อตั้งปี 2533", "selected_icon": FA('fas fa-certificate'), "_id": nid()},
        {"text": "ช่างทองสองรุ่น", "selected_icon": FA('fas fa-hand-sparkles'), "_id": nid()},
        {"text": "งานเสร็จ 7–14 วัน", "selected_icon": FA('fas fa-truck'), "_id": nid()}],
        "space_between": S(24), "icon_color": GD, "icon_size": S(16), "text_color": MU, "text_indent": S(8),
        **typo(BODY, 14, 400, 1.6, 0, None, None, 'icon_typography'), "_margin": D(16, 0, 0, 0)})
    left = C({"flex_gap": GAP(24), "width": S(54, '%'), "width_tablet": S(100, '%'), "width_mobile": S(100, '%')}, [
        EYE('กรอบพระงานพรีเมี่ยม · กระทุ่มแบน สมุทรสาคร'),
        C({"flex_gap": GAP(0), "width": S(100, '%')}, [H(h1, 'h1', TX, 58, 600, HEAD, 1.3, 0, 46, 32),
                                                        H('ทีมช่างทองหลวง', 'p', GD, 58, 600, HEAD, 1.3, 0, 46, 32)]),
        P(f'กรอบพระงานพรีเมี่ยม {SHOP["services"]} ส่งรูปพระมาให้ช่างดู แจ้งราคาก่อนเริ่มงานทุกครั้ง', MU, 18, 17, 16),
        ROW([CHAT(), BTN('ดูผลงานแยกตามทรง', '#shapes', 'line')], 16), trust])
    tag = C({"padding": D(12, 16), "background_background": "classic", "background_color": SF, "border_border": "solid",
             "border_width": D(1), "border_color": LN, "border_radius": D(8), "flex_gap": GAP(0), "width": S(100, '%')},
            [H('งานจริงจากร้าน', 'p', TX, 15, 600, HEAD, 1.5), P('ทุกงานซ่อม ลายสั่งทำ', MU, 13, 13, 13, lh=1.5)])
    right = C({"flex_gap": GAP(12), "width": S(40, '%'), "width_tablet": S(60, '%'), "width_mobile": S(100, '%'), "max_width": S(440),
               "_flex_order_tablet": "start", "_flex_order_mobile": "start"}, [IMGW('img/wp/p02.jpg'), tag])
    hero = band([ROW([left, right], 48, True, 'space-between', 'center', {"flex_justify_content_tablet": "center"})], BG, (96, 64, 48), top=False,
                extra={"background_background": "gradient", "background_color": BG, "background_color_b": "#2A2214",
                       "background_gradient_type": "radial", "background_gradient_position": "top right",
                       "background_color_stop": S(55, '%'), "background_color_b_stop": S(100, '%')})
    tiles = []
    for g in K.GROUPS:
        for sid, name, ph, _, _ in g[3]:
            tiles.append(C({"width": S(23.5, '%'), "width_tablet": S(31.5, '%'), "width_mobile": S(48, '%'), "background_background": "classic",
                            "background_color": SF, "border_border": "solid", "border_width": D(1), "border_color": LN, "border_radius": D(8),
                            "link": L(f'/products/#{sid}'), "flex_gap": GAP(0)}, [
                IMGW(f'img/wp/{ph}', radius=0, extra={"image_border_border": ""}),
                C({"padding": D(12, 16, 16, 16), "padding_mobile": D(10, 12, 12, 12), "flex_gap": GAP(2)}, [
                    H(g[1], 'p', GD, 12, 500, BODY, 1.4, 1),
                    H(name, 'h3', TX, 17, 600, HEAD, 1.4, 0, None, 15, link=f'/products/#{sid}')])]))
    shapes = band([headrow('ผลงานจริง แยกตามทรง', 'เลือกทรงกรอบที่ใช่', 'รูปทั้งหมดเป็นงานจริงจากโต๊ะช่างของร้าน กดที่ทรงเพื่อดูขนาดและผลงานเพิ่ม'),
                   pills([(g[1], f'/products/#{g[0]}') for g in K.GROUPS]),
                   ROW(tiles, 16, True, None, 'stretch', {"flex_gap_mobile": GAP(8)})], BG, anchor='shapes', gap=32)
    steps = band([headrow('งานซ่อม · ลายสั่งทำ', 'สั่งทำง่าย 3 ขั้นตอน', 'ไม่ต้องเดินทางมาร้าน เริ่มจากส่งรูปพระทางแชท'), steps_row(),
                  ROW([CHAT(), BTN('วิธีวัดขนาดพระ', '/custom/', 'line')], 16)], BG, anchor='repair')
    quote = H(SHOP["tag"], 'p', GD, 20, 500, HEAD, 1.6, 0, None, 18, 'start',
              {"_padding": D(0, 0, 0, 24), "_border_border": "solid", "_border_width": D(0, 0, 0, 2), "_border_color": GD})
    about = band([ROW([C({"width": S(40, '%'), "width_tablet": S(100, '%'), "width_mobile": S(100, '%'), "max_width": S(480)}, [IMGW('img/wp/p06.jpg')]),
                       C({"flex_gap": GAP(24), "width": S(54, '%'), "width_tablet": S(100, '%'), "width_mobile": S(100, '%'), "flex_align_items": "flex-start"}, [
                           EYE('เกี่ยวกับเรา'), H('งานช่างทองสองรุ่น<br>ตั้งแต่ปี 2533', 'h2', TX, 40, 600, HEAD, 1.35, 0, 34, 28), quote,
                           P('เริ่มจากคุณพ่อและคุณแม่ที่เคยเป็นช่างทองและพนักงานขายในร้านทอง วันนี้รุ่นลูกสานต่อด้วยฝีมือช่างทองหลวง ผสมเทคนิคโบราณเข้ากับเครื่องมือสมัยใหม่', MU, 17, 16, 16),
                           BTN('อ่านเรื่องของร้าน', '/about/', 'line')])], 56, True, 'space-between', 'center')], BG, anchor='about')
    clips = []
    for i in range(1, 5):
        clips.append(C({"width": S(23.5, '%'), "width_tablet": S(48, '%'), "width_mobile": S(48, '%'), "min_height": S(360), "min_height_mobile": S(240),
                        "flex_justify_content": "center", "flex_align_items": "center", "flex_gap": GAP(12),
                        "background_background": "gradient", "background_color": "#1E1A13", "background_color_b": BG, "background_gradient_angle": S(180, 'deg'),
                        "border_border": "solid", "border_width": D(1), "border_color": LN, "border_radius": D(8), "link": L(SHOP["tiktok"])}, [
            W('icon', {"selected_icon": FA('fas fa-play-circle'), "primary_color": GD, "size": S(40), "align": "center"}),
            H(f'คลิป TikTok {i}', 'p', MU, 14, 400, BODY, 1.4, 0, None, None, 'center')]))
    tiktok = band([headrow('TikTok', 'ดูคลิปงานจากโต๊ะช่าง', f'<a href="/works/">ดูผลงานและรีวิวทั้งหมด →</a>'),
                   ROW(clips, 16, True, None, 'stretch', {"flex_gap_mobile": GAP(8)})], BG)
    return [hero, shapes, steps, about, tiktok, contact_block()]

def sizes_toggle(sid):
    d = K.SIZES.get(sid)
    if not d:
        return P(f'<b>ขนาด:</b> ทำตามขนาดองค์พระ ส่งรูปพระพร้อมไม้บรรทัดให้ช่างประเมินได้', MU, 16, 16, 15)
    th = "".join(f'<th>{c}</th>' for c in d["cols"])
    tr = "".join("<tr>" + "".join(f'<td>{c}</td>' for c in r) + "</tr>" for r in d["rows"])
    table = f'<table><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table>'
    return W('toggle', {"tabs": [{"tab_title": f'ดูตารางขนาด ({len(d["rows"])} พิมพ์) · หน่วยมิลลิเมตร', "tab_content": table, "_id": nid()}],
                        "selected_icon": FA('fas fa-plus'), "selected_active_icon": FA('fas fa-minus'), "title_html_tag": "div",
                        "border_width": S(1), "border_color": LN, "title_background": SF, "title_color": GD, "tab_active_color": GD,
                        "icon_color": GD, "icon_active_color": GD, **typo(BODY, 15, 500, 1.5, 0, None, None, 'title_typography'),
                        "title_padding": D(12, 16), "content_background_color": SF, "content_color": TX, "content_padding": D(0, 16, 16, 16),
                        **typo(BODY, 15, 400, 1.5, 0, None, None, 'content_typography')})

def gallery(sid, name, files):
    return W('image-gallery', {"wp_gallery": [{"id": "", "url": f'{ASSET}/img/w/{f}'} for f in files], "thumbnail_size": "full",
                               "gallery_columns": "4", "gallery_link": "file", "open_lightbox": "yes",
                               "image_spacing": "custom", "image_spacing_custom": S(8),
                               "image_border_border": "solid", "image_border_width": D(1), "image_border_color": LN, "image_border_radius": D(6)})

def products():
    groups = []
    for gid, gname, gdesc, items in K.GROUPS:
        rows = []
        for sid, name, ph, desc, opts in items:
            right = [H(name, 'h3', TX, 26, 600, HEAD, 1.35, 0, None, 24), P(desc, MU, 17, 16, 16)]
            if opts:
                right.append(ROW([H(o, 'span', GD, 14, 400, BODY, 1.4, 0, None, None, 'start',
                                    {"_element_width": "auto", "_padding": D(6, 12), "_border_border": "solid", "_border_width": D(1),
                                     "_border_color": GDD, "_border_radius": D(6)}) for o in opts], 8))
            right.append(sizes_toggle(sid))
            fs = K.GAL.get(sid, [])
            if fs:
                right.append(H(f'ผลงานที่เคยทำ ({len(fs)} รูป)', 'p', TX, 15, 500, BODY, 1.5))
                right.append(gallery(sid, name, fs[:8]))
                if len(fs) > 8:
                    right.append(H(f'ผลงานเพิ่มเติม ({len(fs) - 8} รูป)', 'p', GD, 15, 500, BODY, 1.5))
                    right.append(gallery(sid, name, fs[8:]))
            right.append(ROW([CHAT(), SHOPEE()], 12, extra={"_margin": D(8, 0, 0, 0)}))
            rows.append(C({"flex_direction": "row", "flex_wrap": "wrap", "flex_gap": GAP(32), "flex_gap_mobile": GAP(20), "width": S(100, '%'),
                           "padding": D(32, 0), "border_border": "solid", "border_width": D(1, 0, 0, 0), "border_color": LN, "_element_id": sid}, [
                C({"width": S(28, '%'), "width_tablet": S(36, '%'), "width_mobile": S(100, '%'), "max_width_mobile": S(420)}, [IMGW(f'img/wp/{ph}')]),
                C({"flex_gap": GAP(16), "width": S(66, '%'), "width_tablet": S(58, '%'), "width_mobile": S(100, '%')}, right)]))
        groups.append(C({"flex_gap": GAP(8), "width": S(100, '%'), "_element_id": gid, "padding": D(24, 0, 0, 0)}, [
            H(gname, 'h2', TX, 34, 600, HEAD, 1.35, 0, 30, 26), P(gdesc, MU, 17, 16, 16, extra={"_margin": D(0, 0, 24, 0)})] + rows))
    head = page_head("สินค้า", "รวม 8 ทรงกรอบพระยอดนิยม<br>ที่ลูกค้าเลือกมากที่สุด",
                     "ทุกภาพเป็นผลงานจริงที่ทางร้านเคยทำ สนใจงานสั่ง แนบแบบที่ชอบ เพื่อประเมินราคาที่ใกล้เคียงที่สุด<br>"
                     f'<b>#วัดขนาดพระ</b> สูง × กว้าง × หนา ระบุตัวเลขหน่วย ซม. (ขนาดพระเป๊ะๆ ไม่เผื่อกันน้ำ) หรือสั่งซื้อใน Shopee')
    body = band([pills([(g[1], f'#{g[0]}') for g in K.GROUPS])] + groups, BG, (0, 0, 0), top=False, gap=32)
    body['settings'].update({"padding": D(0, 0, 72, 0), "padding_tablet": D(0, 0, 56, 0), "padding_mobile": D(0, 0, 48, 0)})
    return [head, body, cta_band()]

def custom():
    ol = "".join(f'<li><b>{b}</b> {t}</li>' for b, t in [
        ("ถ่ายรูปพระด้านหน้าและด้านหลัง", "ในที่แสงสว่าง ให้เห็นขอบพระชัด"),
        ("วางไม้บรรทัดข้างองค์พระ", "แล้วถ่ายอีกรูป ช่างจะกะขนาดจากรูปได้"),
        ("ถ้าวัดได้ ให้วัดเป็นมิลลิเมตร", "ความกว้าง ความสูง และความหนาตรงจุดที่หนาที่สุด"),
        ("บอกเนื้อกรอบและงบที่ตั้งไว้", "เช่น เงิน ทอง หรือนาก ช่างแนะนำแบบที่เหมาะให้")])
    measure = band([ROW([
        C({"flex_gap": GAP(16), "width": S(48, '%'), "width_tablet": S(100, '%'), "width_mobile": S(100, '%')}, [
            EYE('วัดขนาดพระ'), H('ส่งขนาดมาให้ช่างแบบนี้', 'h2', TX, 34, 600, HEAD, 1.35, 0, 30, 26),
            P(f'<ol>{ol}</ol>', MU, 17, 16, 16)]),
        C({"flex_gap": GAP(16), "width": S(46, '%'), "width_tablet": S(100, '%'), "width_mobile": S(100, '%'), "flex_align_items": "flex-start"}, [
            note('ไม่สะดวกวัดเอง?', f'นำพระมาที่หน้าร้าน {SHOP["store"]} ช่างวัดให้ที่ร้าน หรือส่งพระทางไปรษณีย์ ช่างวัดขนาดแล้วส่งกลับให้ถึงบ้าน'),
            note('ระยะเวลา', 'งานเสร็จประมาณ 7–14 วัน ขึ้นกับลายและเนื้อโลหะ'), CHAT(extra={"_margin": D(8, 0, 0, 0)})])],
        48, True, 'space-between', 'flex-start')], BG)
    mats = ROW([card(ph, name, desc, f'/products/#{sid}') for sid, name, ph, desc, _ in K.GROUPS[2][3]], 24, True, None, 'stretch')
    matb = band([headrow('เนื้อกรอบ', 'งานสั่งทำที่รับ', 'ทุกงานทำเฉพาะองค์ ตามพิมพ์และขนาดพระจริง'), mats,
                 note('รับซ่อมกรอบทุกชนิด', 'เปลี่ยนห่วง ขัดเงา ซ่อมกรอบหลวมหรือชำรุด ทั้งทอง เงิน นาก และกรอบพลาสติกกันน้ำ')], BG, gap=32)
    steps = band([headrow('ขั้นตอน', 'สั่งทำง่าย 3 ขั้นตอน', 'ช่างแจ้งราคาและระยะเวลาก่อนเริ่มงานทุกครั้ง'), steps_row()], BG, (24, 24, 16), top=False)
    steps['settings'].update({"padding": D(24, 0, 96, 0), "padding_tablet": D(16, 0, 64, 0), "padding_mobile": D(8, 0, 56, 0)})
    return [page_head("งานสั่งทำ", "งานซ่อม · ลายสั่งทำ", "วัดขนาดพระแล้วขึ้นกรอบเฉพาะองค์ ทั้งกรอบนาก กรอบทอง และลายตามแบบ รวมถึงซ่อมกรอบทุกชนิด"),
            steps, measure, matb, cta_band()]

def works():
    wg = W('image-gallery', {"wp_gallery": [{"id": "", "url": f'{ASSET}/img/{p}'} for p in K.WORKS], "thumbnail_size": "medium_large",
                             "gallery_columns": "4", "gallery_link": "file", "open_lightbox": "yes", "image_spacing": "custom",
                             "image_spacing_custom": S(16), "image_border_radius": D(8)})
    rg = W('image-gallery', {"wp_gallery": [{"id": "", "url": f'{ASSET}/img/{r}'} for r in REVIEWS], "thumbnail_size": "medium_large",
                             "gallery_columns": "3", "gallery_link": "file", "open_lightbox": "yes", "image_spacing": "custom",
                             "image_spacing_custom": S(16), "image_border_radius": D(8)})
    b1 = band([headrow('ผลงาน', 'งานจากโต๊ะช่างของเรา', f'ดูแยกตามทรงได้ที่ <a href="/products/">หน้าสินค้า</a>'), wg], BG, gap=32, top=False)
    b1['settings'].update({"padding": D(24, 0, 96, 0), "padding_tablet": D(16, 0, 64, 0), "padding_mobile": D(8, 0, 56, 0)})
    b2 = band([headrow('รีวิว', 'ลูกค้าพูดถึงเรา', 'แคปจากแชทลูกค้าจริง'), rg], BG, anchor='reviews', gap=32)
    return [page_head("ผลงาน · รีวิว", "ผลงานและรีวิวจากลูกค้า", "งานจริงจากโต๊ะช่างของร้าน และเสียงจากลูกค้าที่ส่งพระมาเลี่ยมกับเรา"), b1, b2, cta_band()]

def about():
    facts = ROW([C({"padding": D(14, 16), "background_background": "classic", "background_color": SF, "border_border": "solid", "border_width": D(1),
                    "border_color": LN, "border_radius": D(8), "flex_gap": GAP(2), "width": S(31, '%'), "width_mobile": S(100, '%')},
                   [H(b, 'p', GD, 22, 600, HEAD, 1.3), P(s, MU, 13, 13, 13, lh=1.5)])
                 for b, s in [("2533", "ปีที่ก่อตั้งร้าน"), ("2 รุ่น", "ช่างทองในครอบครัว"), ("ทอง เงิน นาก", "รับทำทุกเนื้อโลหะ")]], 12, True, None, 'stretch')
    quote = H(SHOP["tag"], 'p', GD, 20, 500, HEAD, 1.6, 0, None, 18, 'start',
              {"_padding": D(0, 0, 0, 24), "_border_border": "solid", "_border_width": D(0, 0, 0, 2), "_border_color": GD})
    craft = band([ROW([C({"width": S(40, '%'), "width_tablet": S(100, '%'), "width_mobile": S(100, '%'), "max_width": S(480)}, [IMGW('img/wp/p06.jpg')]),
                       C({"flex_gap": GAP(16), "width": S(54, '%'), "width_tablet": S(100, '%'), "width_mobile": S(100, '%')}, [
                           EYE('เรื่องของเรา'), quote,
                           P('KT กรอบพระไทยแลนด์ เป็นแบรนด์ร้านเลี่ยมพระของคนไทย เริ่มจากคุณพ่อและคุณแม่ที่เคยเป็นช่างทองและพนักงานขายในร้านทอง ก่อตั้งร้านขึ้นในปี 2533', MU, 17, 16, 16),
                           P('วันนี้รุ่นลูกสานต่อด้วยฝีมือช่างทองหลวง ผสมเทคนิคช่างทองโบราณเข้ากับเครื่องมือและเทคโนโลยีสมัยใหม่ ทุกลวดลายจึงเป็นทั้งการอนุรักษ์งานช่างไทยและงานศิลปะที่มีคุณค่า', MU, 17, 16, 16),
                           facts])], 56, True, 'space-between', 'center')], BG, top=False)
    craft['settings'].update({"padding": D(24, 0, 96, 0), "padding_tablet": D(16, 0, 64, 0), "padding_mobile": D(8, 0, 56, 0)})
    svc = band([headrow('สิ่งที่เรารับทำ', 'ครบเรื่องกรอบพระในร้านเดียว', SHOP["services"]),
                ROW([card('p18.jpg', 'กรอบสำเร็จ', 'กรอบเงินทุกทรงยอดนิยม หลายขนาด', '/products/'),
                     card('p19.jpg', 'งานสั่งทำ', 'กรอบนาก กรอบทอง ลายตามแบบ เฉพาะองค์', '/custom/'),
                     card('p05.jpg', 'งานซ่อม', 'เปลี่ยนห่วง ขัดเงา ซ่อมกรอบทุกชนิด', '/custom/')], 24, True, None, 'stretch')], BG, gap=32)
    return [page_head("เกี่ยวกับเรา", "งานช่างทองสองรุ่น ตั้งแต่ปี 2533", "KT กรอบพระไทยแลนด์ แบรนด์ร้านเลี่ยมพระของคนไทย"),
            craft, svc, contact_block("แวะมาคุยกับช่างที่ร้าน")]

def articles():
    arts = []
    for a, t, ex, pts in K.ARTICLES:
        ul = "".join(f'<li>{x}</li>' for x in pts)
        arts.append(C({"padding": D(32), "padding_mobile": D(24, 20), "background_background": "classic", "background_color": SF,
                       "border_border": "solid", "border_width": D(1), "border_color": LN, "border_radius": D(8), "flex_gap": GAP(12),
                       "width": S(100, '%'), "_element_id": a}, [
            H(t, 'h2', TX, 26, 600, HEAD, 1.4, 0, None, 22), P(ex, GD, 17, 16, 16),
            P(f'<ul>{ul}</ul>', MU, 16, 16, 16)]))
    b = band([pills([(t, f'#{a}') for a, t, _, _ in K.ARTICLES]),
              C({"flex_gap": GAP(24), "width": S(100, '%'), "max_width": S(820)}, arts)], BG, top=False, gap=32)
    b['settings'].update({"padding": D(24, 0, 96, 0), "padding_tablet": D(16, 0, 64, 0), "padding_mobile": D(8, 0, 56, 0)})
    return [page_head("บทความ", "บทความเรื่องกรอบพระ", "ความรู้จากช่าง เรื่องเลือกกรอบ เนื้อโลหะ และการดูแล"), b, cta_band()]

def contact():
    return [page_head("ติดต่อ", "ติดต่อร้าน", "ทักแชท โทร หรือแวะมาที่หน้าร้านได้ทุกวัน"), contact_block("ช่องทางติดต่อ")]

def tpl(title, content, kind='page'):
    for e in content: e['isInner'] = False
    return {"version": "0.4", "title": title, "type": kind, "content": content, "page_settings": {"hide_title": "yes"}}

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    pages = {"header": tpl("KT Header", [header()], "section"), "footer": tpl("KT Footer", [footer()], "section"),
             "home": tpl("KT Home", home()), "products": tpl("KT Products", products()), "custom": tpl("KT Custom", custom()),
             "works": tpl("KT Works", works()), "about": tpl("KT About", about()), "articles": tpl("KT Articles", articles()),
             "contact": tpl("KT Contact", contact())}
    for k, v in pages.items():
        s = json.dumps(v, ensure_ascii=False)
        open(os.path.join(OUT, k + ".json"), "w", encoding="utf-8").write(s)
        print(k, len(s))
