from pathlib import Path
import threading,http.server,json
from playwright.sync_api import sync_playwright
P=Path(__file__).resolve().parent
handler=lambda *a,**k:http.server.SimpleHTTPRequestHandler(*a,directory=str(P/'slides'),**k)
srv=http.server.ThreadingHTTPServer(('127.0.0.1',0),handler)
threading.Thread(target=srv.serve_forever,daemon=True).start()
(P/'stills').mkdir(exist_ok=True)
audit=[]
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox'])
 page=b.new_page(viewport={'width':1080,'height':1350},device_scale_factor=1)
 for n in [1,4]:
  page.goto(f'http://127.0.0.1:{srv.server_port}/slide-{n:02}.html');page.evaluate('document.fonts.ready')
  page.screenshot(path=str(P/'stills'/f'slide-{n:02}.png'))
  c=page.context.new_cdp_session(page);c.send('DOM.enable');c.send('CSS.enable');root=c.send('DOM.getDocument')['root']['nodeId']
  fonts={}
  for selector in ['.headline','.body','.prompt','.footer']:
   node=c.send('DOM.querySelector',{'nodeId':root,'selector':selector})['nodeId'];fonts[selector]=c.send('CSS.getPlatformFontsForNode',{'nodeId':node})['fonts']
  audit.append({'slide':n,'fonts':fonts,'images_loaded':page.evaluate('Array.from(document.images).every(i=>i.complete&&i.naturalWidth>0)'),'copy_bottom':page.locator('.copy').bounding_box()})
 b.close()
(P/'audit.json').write_text(json.dumps(audit,indent=2))
srv.shutdown()
