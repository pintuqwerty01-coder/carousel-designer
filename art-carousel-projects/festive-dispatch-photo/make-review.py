from pathlib import Path
import json,re
from playwright.sync_api import sync_playwright
p=Path(__file__).resolve().parent
source=json.loads((p/'content.json').read_text());norm=lambda s:re.sub(r'\s+',' ',s).strip()
with sync_playwright() as w:
 b=w.chromium.launch();page=b.new_page(viewport={'width':1080,'height':1350})
 for s in source['slides']:
  n=s['number'];page.goto((p/f'slides/slide-{n:02d}.html').as_uri());page.wait_for_timeout(300)
  page.evaluate('document.fonts.ready')
  assert page.evaluate('[...document.images].every(i=>i.complete && i.naturalWidth>0)'),f'Image missing on {n}'
  if n!=1:
   text=norm(page.locator('body').inner_text())
   for line in s['copy']:assert norm(line.replace('**','')) in text,(n,line)
   rects=page.evaluate("[...document.querySelectorAll('.photo-h,.photo-pain,.photo-whatif,.photo-result,.reveal-body,.reveal-sign,.summary,.benefits,.summary-end,.cta-body,.cta-dm,.cta-save,.setup-next')].map(e=>({class:e.className,top:e.offsetTop,bottom:e.offsetTop+e.offsetHeight,left:e.offsetLeft,right:e.offsetLeft+e.offsetWidth}))")
   assert all(r['bottom']<=1220 and r['left']>=84 and r['right']<=996 for r in rects),(n,rects)
  print(f'{n:02}: images loaded; copy and text bounds OK' if n!=1 else '01: exact approved raster cover; image loaded',flush=True)
 cards=''.join(f'<figure><img src="stills/slide-{n:02d}.png"><figcaption>{n:02d}/09</figcaption></figure>' for n in range(1,10))
 (p/'review.html').write_text('<!doctype html><meta charset="utf-8"><title>Festive dispatch — static review</title><style>body{margin:0;padding:20px;background:#1A1A1A;font:20px Arial;color:white}main{display:grid;grid-template-columns:repeat(3,540px);gap:18px}figure{margin:0}img{width:540px;height:675px;display:block}figcaption{padding:10px 0} @media print{body{padding:0;background:white}main{display:block}figure{break-after:page}img{width:1080px;height:1350px}figcaption{display:none}@page{size:1080px 1350px;margin:0}}</style><main>'+cards+'</main>')
 page.set_viewport_size({'width':1696,'height':2200});page.goto((p/'review.html').as_uri());page.wait_for_timeout(300)
 assert page.evaluate('[...document.images].every(i=>i.complete&&i.naturalWidth>0)')
 page.screenshot(path=str(p/'proof/all-slides.png'),full_page=True)
 page.pdf(path=str(p/'static-review.pdf'),print_background=True,prefer_css_page_size=True)
 b.close()
