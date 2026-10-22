from pathlib import Path
import threading,http.server,subprocess
from playwright.sync_api import sync_playwright
P=Path(__file__).resolve().parent
class Quiet(http.server.SimpleHTTPRequestHandler):
 def __init__(self,*a,**k):super().__init__(*a,directory=str(P/'slides'),**k)
 def log_message(self,*a):pass
srv=http.server.ThreadingHTTPServer(('127.0.0.1',0),Quiet);threading.Thread(target=srv.serve_forever,daemon=True).start()
T=P/'print-pages';T.mkdir(exist_ok=True)
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-gpu']);page=b.new_page(viewport={'width':1080,'height':1350})
 for n in range(1,9):
  page.goto(f'http://127.0.0.1:{srv.server_port}/slide-{n:02}.html');page.evaluate('document.fonts.ready');page.evaluate('Promise.all(Array.from(document.images).map(i=>i.decode()))');page.emulate_media(media='screen');page.pdf(path=str(T/f'slide-{n:02}.pdf'),width='1080px',height='1350px',print_background=True,margin={'top':'0','bottom':'0','left':'0','right':'0'})
  subprocess.run(['pdftoppm','-scale-to-x','1080','-scale-to-y','1350','-f','1','-singlefile','-png',str(T/f'slide-{n:02}.pdf'),str(P/'stills'/f'slide-{n:02}')],check=True,stdout=subprocess.DEVNULL)
 b.close()
srv.shutdown();print('Rendered all slides through PDF print pipeline')
