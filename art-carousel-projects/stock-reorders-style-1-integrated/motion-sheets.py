"""Nine evenly spaced moments per slide, including the final pose."""
import functools,http.server,threading,pathlib,json,io
from playwright.sync_api import sync_playwright
from PIL import Image,ImageDraw
P=pathlib.Path(__file__).resolve().parent
class Quiet(http.server.SimpleHTTPRequestHandler):
 def log_message(self,*args):pass
server=http.server.ThreadingHTTPServer(('127.0.0.1',0),functools.partial(Quiet,directory=str(P/'slides')))
threading.Thread(target=server.serve_forever,daemon=True).start()
with sync_playwright() as pw:
 b=pw.chromium.launch(executable_path='/usr/bin/chromium');pg=b.new_page(viewport={'width':1080,'height':1350})
 for n,s in enumerate(json.loads((P/'content.json').read_text())['slides'],1):
  pg.goto(f'http://127.0.0.1:{server.server_port}/slide-{n:02}.html');pg.evaluate('document.fonts.ready')
  sheet=Image.new('RGB',(972,1275),'white');d=ImageDraw.Draw(sheet)
  for j in range(9):
   t=.1+(s['duration']-.2)*j/8
   pg.evaluate('(t)=>Object.values(window.__timelines).forEach(tl=>tl.seek(t,false))',t)
   im=Image.open(io.BytesIO(pg.screenshot())).convert('RGB').resize((324,405),Image.Resampling.LANCZOS)
   x=(j%3)*324;y=(j//3)*425;sheet.paste(im,(x,y+20));d.text((x+8,y+3),f'{t:.2f}s',fill='black')
  sheet.save(P/'proof'/f'sheet-{n:02}.png');print('sheet',n,flush=True)
 b.close()
server.shutdown()
