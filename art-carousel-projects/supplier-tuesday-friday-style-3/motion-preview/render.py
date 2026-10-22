from pathlib import Path
import threading,http.server,subprocess,json,sys
from playwright.sync_api import sync_playwright
P=Path(__file__).resolve().parent.parent;M=P/'motion-preview'
class Quiet(http.server.SimpleHTTPRequestHandler):
 def __init__(self,*a,**k):super().__init__(*a,directory=str(P),**k)
 def log_message(self,*a):pass
srv=http.server.ThreadingHTTPServer(('127.0.0.1',0),Quiet);threading.Thread(target=srv.serve_forever,daemon=True).start();url=f'http://127.0.0.1:{srv.server_port}/motion-preview/'
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-gpu']);page=b.new_page(viewport={'width':1080,'height':1350},device_scale_factor=1)
 for state in ['prep','ready','sent']:
  page.goto(url+f'states/{state}.html');page.evaluate('document.fonts.ready');page.evaluate('Promise.all(Array.from(document.images).map(i=>i.decode()))');page.emulate_media(media='screen');page.pdf(path=str(M/'states'/f'{state}.pdf'),width='1080px',height='1350px',print_background=True,margin={'top':'0','bottom':'0','left':'0','right':'0'})
  subprocess.run(['pdftoppm','-scale-to-x','1080','-scale-to-y','1350','-singlefile','-png',str(M/'states'/f'{state}.pdf'),str(M/'assets'/state)],check=True)
 page.goto(url+'index.html?capture');page.evaluate('Promise.all(Array.from(document.images).map(i=>i.decode()))')
 for t in [0,1.5,2.45,3.3,6.8]:
  page.evaluate('(t)=>setTime(t)',t);page.screenshot(path=str(M/'proof'/f'frame-{t:.2f}.png'))
 if '--video' in sys.argv:
  out=M/'delivery/ART-supplier-follow-up-motion-test-v1.mp4';cmd=['ffmpeg','-v','error','-y','-f','image2pipe','-vcodec','png','-framerate','30','-i','-','-c:v','libx264','-profile:v','high','-pix_fmt','yuv420p','-crf','16','-preset','fast','-movflags','+faststart','-an',str(out)]
  proc=subprocess.Popen(cmd,stdin=subprocess.PIPE)
  for frame in range(210):
   page.evaluate('(t)=>setTime(t)',frame/30);proc.stdin.write(page.screenshot())
   if frame%60==0:print(f'{frame}/210 frames',flush=True)
  proc.stdin.close();assert proc.wait()==0;print(out,flush=True)
 b.close()
srv.shutdown()
