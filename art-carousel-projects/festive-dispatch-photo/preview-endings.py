from pathlib import Path
from playwright.sync_api import sync_playwright
p=Path(__file__).resolve().parent
(p/'last-three.html').write_text('<!doctype html><style>body{margin:0;padding:16px;display:flex;gap:16px;background:#1a1a1a}img{width:540px;height:675px}</style>'+''.join(f'<img src="stills/slide-{n:02d}.png">' for n in (7,8,9)))
with sync_playwright() as w:
 b=w.chromium.launch();page=b.new_page(viewport={'width':1684,'height':707});page.goto((p/'last-three.html').as_uri(),wait_until='networkidle');page.screenshot(path=str(p/'proof/last-three.png'));b.close()
