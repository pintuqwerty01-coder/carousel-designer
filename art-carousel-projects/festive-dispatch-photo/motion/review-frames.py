from pathlib import Path
from playwright.sync_api import sync_playwright
p=Path(__file__).resolve().parent
(p/'proof/frames.html').write_text('<!doctype html><meta charset="utf-8"><style>body{margin:0;padding:16px;background:#1a1a1a;color:white;font:20px Arial;display:grid;grid-template-columns:repeat(3,360px);gap:16px}figure{margin:0}img{width:360px;height:450px}figcaption{padding:8px}</style>'+''.join(f'<figure><img src="{n:02d}-action.png"><figcaption>Slide {n:02d} — camera at 1.7s</figcaption></figure>' for n in range(1,7)))
with sync_playwright() as w:
 b=w.chromium.launch();page=b.new_page(viewport={'width':1144,'height':1020});page.goto((p/'proof/frames.html').as_uri(),wait_until='networkidle');page.screenshot(path=str(p/'proof/action-overview.png'),full_page=True);b.close()
