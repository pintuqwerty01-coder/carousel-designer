from pathlib import Path
from playwright.sync_api import sync_playwright
import json
p=Path(__file__).resolve().parent;reports=[]
with sync_playwright() as w:
 b=w.chromium.launch();page=b.new_page(viewport={'width':1080,'height':1350})
 for name in [f'slide-{i:02}' for i in range(1,10)]:
  page.goto((p/f'{name}.html').as_uri(),wait_until='networkidle');page.evaluate('document.fonts.ready');c=page.context.new_cdp_session(page);c.send('DOM.enable');c.send('CSS.enable');root=c.send('DOM.getDocument')['root']['nodeId']
  for sel,font in [('.big','Poppins'),('.hd','Preahvihear'),('.bd','Poppins'),('.result','Poppins')]:
   for node in c.send('DOM.querySelectorAll',{'nodeId':root,'selector':sel})['nodeIds']:
    f=c.send('CSS.getPlatformFontsForNode',{'nodeId':node})['fonts'];assert f and all(x['familyName'].startswith(font) and x['isCustomFont'] for x in f),(name,sel,f);reports.append({'name':name,'selector':sel,'fonts':f})
  blocks=page.evaluate('''()=>[...document.querySelectorAll('.tx')].map(e=>{let r=e.getBoundingClientRect();return {left:r.left,top:r.top,right:r.right,bottom:r.bottom}})''')
  for i,a in enumerate(blocks):
   for z in blocks[i+1:]:assert min(a['right'],z['right'])<=max(a['left'],z['left']) or min(a['bottom'],z['bottom'])<=max(a['top'],z['top']),(name,'text blocks overlap',a,z)
  c.detach();print(name,'actual fonts and text separation passed',flush=True)
 b.close()
(p/'font-validation.json').write_text(json.dumps(reports,indent=2))
