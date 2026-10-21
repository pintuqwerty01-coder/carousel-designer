"""Export selected final frames without overwriting the approved opening."""
import functools,http.server,threading,pathlib,json,sys
from playwright.sync_api import sync_playwright
P=pathlib.Path(__file__).resolve().parent
class Quiet(http.server.SimpleHTTPRequestHandler):
 def log_message(self,*args):pass
server=http.server.ThreadingHTTPServer(('127.0.0.1',0),functools.partial(Quiet,directory=str(P/'slides')))
threading.Thread(target=server.serve_forever,daemon=True).start()
selected={int(x) for x in sys.argv[1].split(',')} if len(sys.argv)>1 else set(range(1,10))
with sync_playwright() as pw:
 b=pw.chromium.launch(executable_path='/usr/bin/chromium');pg=b.new_page(viewport={'width':1080,'height':1350})
 for n,s in enumerate(json.loads((P/'content.json').read_text())['slides'],1):
  if n not in selected:continue
  pg.goto(f'http://127.0.0.1:{server.server_port}/slide-{n:02}.html');pg.evaluate('document.fonts.ready')
  pg.evaluate('(t)=>Object.values(window.__timelines).forEach(tl=>tl.seek(t,false))',s['duration']);pg.evaluate('document.fonts.ready')
  pg.screenshot(path=str(P/'stills'/f'slide-{n:02}.png'));print('still',n,flush=True)
 b.close()
server.shutdown()
