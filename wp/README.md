# KT → WordPress (Hostinger staging)

Staging: https://storied-bisque-tiger-20.hostingersite.com (to be pointed at krobphrathailand.com)

Stack: Hello Elementor theme · Elementor 4.4 (free) · Elementor Header & Footer Builder (HFE) · Yoast SEO · LiteSpeed Cache

| WP id | page | template json |
|---|---|---|
| 8 | หน้าแรก (front page) | home |
| 9 | /products/ | products |
| 10 | /custom/ | custom |
| 11 | /works/ | works |
| 12 | /about/ | about |
| 13 | /articles/ | articles |
| 14 | /contact/ | contact |
| 23 | HFE Header (entire site) | header |
| 25 | HFE Footer (entire site) | footer |

Menu: "Main Menu" (slug main-menu, id 3). Kit: dark bg, gold links, IBM Plex Sans Thai body.

## Rebuild
1. `python3 wp/build_wp.py` → `site/wp-build/*.json` (served by Vercel with CORS)
2. Deploy Vercel, then in the page's Elementor editor: import_template (base64 JSON) → requestTemplateContent → convert every non-ASCII string to HTML entities → document/elements/import → save/publish.

## Host gotchas (Hostinger)
- Saves lose JSON backslashes: Thai (\uXXXX) turns into "u0e01…" and escaped quotes break the whole page. Fix: before saving, convert all non-ASCII text in settings to `&#NNNN;` entities.
- Inline `style="…"` or `<a href=…>` inside text, together with an image in the same save → page saved empty. Keep text HTML attribute-free; links go through widget link controls.
- Menu slug must be ASCII (Thai slug is %-encoded and also gets mangled).
