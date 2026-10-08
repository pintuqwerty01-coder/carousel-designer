from pathlib import Path
from playwright.sync_api import sync_playwright
import json
p=Path(__file__).resolve().parent;source=json.loads((p/'source-content.json').read_text())['slides'];result=[]
with sync_playwright() as w:
 b=w.chromium.launch();page=b.new_page(viewport={'width':1080,'height':1350})
 for n in [1,4]:
  page.goto((p/f'slides/slide-{n:02}.html').as_uri(),wait_until='networkidle');page.evaluate('document.fonts.ready');body=' '.join(page.locator('body').inner_text().split()).casefold()
  for line in source[n-1]['copy']:
   for part in line.replace('**','').replace('✓ ','').split('·'):assert ' '.join(part.split()).casefold() in body,(n,part)
  rects=page.evaluate('''()=>[...document.querySelectorAll('.tx')].flatMap(e=>{let r=document.createRange();r.selectNodeContents(e);return [...r.getClientRects()].map(x=>({left:x.left,right:x.right,bottom:x.bottom}))})''')
  assert all(r['left']>=83 and r['right']<=997 and r['bottom']<=1220 for r in rects),(n,rects)
  c=page.context.new_cdp_session(page);c.send('DOM.enable');c.send('CSS.enable');root=c.send('DOM.getDocument')['root']['nodeId']
  for sel,font in [('.big','Poppins'),('.hd','Preahvihear'),('.bd','Poppins'),('.pill','Poppins'),('.diagram text','Poppins')]:
   for node in c.send('DOM.querySelectorAll',{'nodeId':root,'selector':sel})['nodeIds']:
    fonts=c.send('CSS.getPlatformFontsForNode',{'nodeId':node})['fonts'];assert fonts and all(x['familyName'].startswith(font) and x['isCustomFont'] for x in fonts),(n,sel,fonts);result.append({'slide':n,'selector':sel,'fonts':fonts})
  c.detach();print(n,'revised copy, glyph bounds and fonts passed')
 b.close()
(p/'proof/font-validation.json').write_text(json.dumps(result,indent=2))
