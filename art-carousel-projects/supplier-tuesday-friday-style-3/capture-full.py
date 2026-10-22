from pathlib import Path
import threading,http.server,json
from playwright.sync_api import sync_playwright
P=Path(__file__).resolve().parent
class Quiet(http.server.SimpleHTTPRequestHandler):
 def __init__(self,*a,**k):super().__init__(*a,directory=str(P/'slides'),**k)
 def log_message(self,*a):pass
srv=http.server.ThreadingHTTPServer(('127.0.0.1',0),Quiet);threading.Thread(target=srv.serve_forever,daemon=True).start()
(P/'stills').mkdir(exist_ok=True);audit=[];copy=json.loads((P/'content.json').read_text())['slides']
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-gpu','--disable-dev-shm-usage']);page=b.new_page(viewport={'width':1080,'height':1350},device_scale_factor=1)
 for n in range(1,9):
  page=b.new_page(viewport={'width':1080,'height':1350},device_scale_factor=1)
  page.goto(f'http://127.0.0.1:{srv.server_port}/slide-{n:02}.html');page.evaluate('document.fonts.ready');page.locator('.photo').evaluate('(i)=>i.decode()')
  page.evaluate('new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))')
  page.screenshot()
  page.wait_for_timeout(200)
  page.screenshot(path=str(P/'stills'/f'slide-{n:02}.png'))
  c=page.context.new_cdp_session(page);c.send('DOM.enable');c.send('CSS.enable');root=c.send('DOM.getDocument')['root']['nodeId'];fonts={}
  for selector in ['.headline','.body','.prompt','.footer','.scene-label','.result','.brand-cta span','.prop-text small','.prop-text p','.prop-text strong','.prop-text em','.sent']:
   ids=c.send('DOM.querySelectorAll',{'nodeId':root,'selector':selector})['nodeIds']
   for j,node in enumerate(ids):
    f=c.send('CSS.getPlatformFontsForNode',{'nodeId':node})['fonts'];assert all(x['familyName']=='Preahvihear' and x['isCustomFont'] for x in f),(n,selector,f);fonts[selector+str(j)]=f
  assert ' '.join(page.locator('.body').inner_text().split())==' '.join(' '.join(copy[n-1]['body']).split())
  assert page.evaluate('Array.from(document.images).every(i=>i.complete&&i.naturalWidth>0)')
  boxes=page.locator('.copy,.scene-label,.result,.brand-cta').evaluate_all('(els)=>els.map(e=>({class:e.className,x:e.getBoundingClientRect().x,y:e.getBoundingClientRect().y,right:e.getBoundingClientRect().right,bottom:e.getBoundingClientRect().bottom,overflow:e.scrollWidth>e.clientWidth}))')
  for box in boxes:
   if box['right']==0:continue
   assert box['x']>=83 and box['right']<=997 and box['bottom']<=1220 and not box['overflow'],(n,box)
  audit.append({'slide':n,'fonts':fonts,'body_matches_canonical':True,'images_loaded':True,'boxes':boxes})
  page.close()
 b.close()
(P/'audit-full-v3.json').write_text(json.dumps(audit,indent=2));srv.shutdown();print('8 slides captured: fonts, body copy, safe bounds and images verified')
