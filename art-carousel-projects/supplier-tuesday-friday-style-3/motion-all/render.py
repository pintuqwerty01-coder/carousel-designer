from pathlib import Path
import threading,http.server,subprocess,sys,concurrent.futures
from playwright.sync_api import sync_playwright
P=Path(__file__).resolve().parent.parent;M=P/'motion-all'
class Quiet(http.server.SimpleHTTPRequestHandler):
 def __init__(self,*a,**k):super().__init__(*a,directory=str(P),**k)
 def log_message(self,*a):pass
srv=http.server.ThreadingHTTPServer(('127.0.0.1',0),Quiet);threading.Thread(target=srv.serve_forever,daemon=True).start();url=f'http://127.0.0.1:{srv.server_port}/motion-all/'
def run(n):
 nn=f'{n:02}'
 with sync_playwright() as p:
  b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-gpu']);page=b.new_page(viewport={'width':1080,'height':1350},device_scale_factor=1)
  if '--states' in sys.argv:
   for state in ['prep','ready','final']:
    page.goto(url+f'states/{nn}-{state}.html');page.evaluate('document.fonts.ready');page.evaluate('Promise.all(Array.from(document.images).map(i=>i.decode()))');page.emulate_media(media='screen');pdf=M/f'states/{nn}-{state}.pdf';page.pdf(path=str(pdf),width='1080px',height='1350px',print_background=True,margin=dict(top='0',bottom='0',left='0',right='0'));subprocess.run(['pdftoppm','-scale-to-x','1080','-scale-to-y','1350','-singlefile','-png',str(pdf),str(M/f'assets/{nn}-{state}')],check=True);pdf.unlink()
  page.goto(url+f'slide-{nn}.html?capture');page.evaluate('Promise.all(Array.from(document.images).map(i=>i.decode()))')
  for t in [0,1.8,3.4,6.8]:
   page.evaluate('(t)=>setTime(t)',t);page.screenshot(path=str(M/f'proof/{nn}-{t:.1f}.png'))
  if '--video' in sys.argv:
   out=M/f'delivery/ART-supplier-delay-slide-{nn}.mp4';proc=subprocess.Popen(['ffmpeg','-v','error','-y','-f','image2pipe','-vcodec','png','-framerate','30','-i','-','-c:v','libx264','-profile:v','high','-pix_fmt','yuv420p','-crf','16','-preset','fast','-threads','2','-movflags','+faststart','-an',str(out)],stdin=subprocess.PIPE)
   for frame in range(210):
    page.evaluate('(t)=>setTime(t)',frame/30);proc.stdin.write(page.screenshot())
   proc.stdin.close();assert proc.wait()==0
  b.close();print(f'Slide {nn} complete',flush=True)
nums=[int(x) for x in sys.argv[1:] if x.isdigit()] or [1,2,3,5,6,7,8]
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:list(pool.map(run,nums))
srv.shutdown()
