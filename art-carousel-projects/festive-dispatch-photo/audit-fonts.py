from pathlib import Path
from playwright.sync_api import sync_playwright
import json
p=Path(__file__).resolve().parent
with sync_playwright() as w:
 b=w.chromium.launch();page=b.new_page(viewport={'width':1080,'height':1350})
 for n in range(2,10):
  page.goto((p/f'slides/slide-{n:02d}.html').as_uri(),wait_until='networkidle');page.evaluate('document.fonts.ready')
  c=page.context.new_cdp_session(page);c.send('DOM.enable');c.send('CSS.enable');root=c.send('DOM.getDocument')['root']['nodeId']
  for selector in ['.photo-h','.photo-h em','.photo-pain','.photo-whatif','.photo-result','.reveal-body','.benefit p','.cta-body']:
   node=c.send('DOM.querySelector',{'nodeId':root,'selector':selector})['nodeId']
   if node:
    info=c.send('CSS.getPlatformFontsForNode',{'nodeId':node})['fonts']
    print(n,selector,[(f['familyName'],f['glyphCount'],f['isCustomFont']) for f in info])
    if selector.startswith('.photo-h'):assert all(f['familyName']=='Preahvihear' and f['isCustomFont'] for f in info),(n,selector,info)
    elif n<=7:assert all(f['familyName']=='Poppins Medium' and f['isCustomFont'] for f in info),(n,selector,info)
  c.detach()
 b.close()
