from pathlib import Path
from playwright.sync_api import sync_playwright
p=Path(__file__).resolve().parent;(p/'proof/timing').mkdir(exist_ok=True)
with sync_playwright() as w:
 b=w.chromium.launch()
 for n in range(1,7):
  page=b.new_page(viewport={'width':360,'height':450});page.goto((p/f'slides/slide-{n:02d}.html').as_uri(),wait_until='networkidle');page.evaluate('document.fonts.ready');page.add_style_tag(content='html,body{width:360px;height:450px}.slide{transform:scale(.3333333333);transform-origin:0 0}')
  for i,t in enumerate([0,.125,.5,1.125,1.625,2.125,2.5,3.125,3.9]):
   page.evaluate('(t)=>Object.values(window.__timelines).forEach(tl=>tl.time(t,false))',t);page.screenshot(path=str(p/f'proof/timing/{n:02d}-{i}.png'))
  page.close()
  gallery=p/f'proof/sheet-{n:02d}.html';gallery.write_text('<!doctype html><meta charset="utf-8"><style>body{margin:0;padding:12px;background:#1a1a1a;color:white;font:20px Arial;display:grid;grid-template-columns:repeat(3,360px);gap:12px}figure{margin:0}img{width:360px;height:450px}figcaption{padding:7px}</style>'+''.join(f'<figure><img src="timing/{n:02d}-{i}.png"><figcaption>{t:g}s</figcaption></figure>' for i,t in enumerate([0,.125,.5,1.125,1.625,2.125,2.5,3.125,3.9])))
  page=b.new_page(viewport={'width':1128,'height':1518});page.goto(gallery.as_uri(),wait_until='networkidle');page.screenshot(path=str(p/f'proof/sheet-{n:02d}.png'),full_page=True);page.close();print(f'{n:02}: nine-frame actor sheet captured',flush=True)
 b.close()
