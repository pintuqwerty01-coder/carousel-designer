from pathlib import Path
from playwright.sync_api import sync_playwright
import json
p=Path(__file__).resolve().parent
reports=[]
with sync_playwright() as w:
 b=w.chromium.launch();page=b.new_page(viewport={'width':1080,'height':1350})
 for x in 'abc':
  page.goto((p/f'option-{x}.html').as_uri(),wait_until='networkidle');page.evaluate('document.fonts.ready')
  assert page.evaluate('[...document.images].every(x=>x.complete&&x.naturalWidth>0)')
  rects=page.evaluate('''()=>[...document.querySelectorAll('.tx')].flatMap(e=>{let r=document.createRange();r.selectNodeContents(e);return [...r.getClientRects()].map(x=>({left:x.left,right:x.right,bottom:x.bottom}))})''')
  assert all(r['left']>=83 and r['right']<=997 and r['bottom']<=1220 for r in rects),(x,rects)
  body=' '.join(page.locator('body').inner_text().split()).casefold()
  for t in ['Catch delivery delays before your customer does.','Your team already handles the unexpected. What if you heard first?','Delays start small. Swipe to see where.']:assert t.casefold() in body,(x,t)
  c=page.context.new_cdp_session(page);c.send('DOM.enable');c.send('CSS.enable');root=c.send('DOM.getDocument')['root']['nodeId']
  for sel,font in [('.big','Poppins'),('.hd','Preahvihear'),('.bd','Poppins')]:
   for n in c.send('DOM.querySelectorAll',{'nodeId':root,'selector':sel})['nodeIds']:
    fonts=c.send('CSS.getPlatformFontsForNode',{'nodeId':n})['fonts'];assert fonts and all(f['familyName'].startswith(font) and f['isCustomFont'] for f in fonts),(x,fonts)
  c.detach();page.screenshot(path=str(p/f'option-{x}.png'));reports.append({'option':x,'copy':'exact','fonts':'verified','glyph_bounds':rects});print(x,'copy, fonts and bounds passed',flush=True)
 (p/'validation.json').write_text(json.dumps(reports,indent=2))
 html='<style>@page{size:1080px 1350px;margin:0}body{margin:0}img{display:block;width:1080px;height:1350px;break-after:page}img:last-child{break-after:auto}</style>'+''.join(f'<img src="option-{x}.png">' for x in 'abc')
 (p/'review.html').write_text(html);page.goto((p/'review.html').as_uri(),wait_until='networkidle');page.pdf(path=str(p/'concept-options.pdf'),prefer_css_page_size=True,print_background=True)
 page.set_viewport_size({'width':1320,'height':562});page.add_style_tag(content='body{display:flex;gap:12px;padding:12px;background:#03161B}img{width:424px;height:530px}');page.screenshot(path=str(p/'compare.png'),full_page=True)
 b.close()
