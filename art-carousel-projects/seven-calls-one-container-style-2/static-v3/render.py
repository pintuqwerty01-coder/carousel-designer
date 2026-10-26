from pathlib import Path
import http.server,threading,json,subprocess,zipfile,sys
from playwright.sync_api import sync_playwright
from PIL import Image
V=Path(__file__).resolve().parent;D=V/'delivery';T=V/'proof';content=json.loads((V/'content.json').read_text())['slides']
class Quiet(http.server.SimpleHTTPRequestHandler):
 def __init__(self,*a,**k):super().__init__(*a,directory=str(V),**k)
 def log_message(self,*a):pass
srv=http.server.ThreadingHTTPServer(('127.0.0.1',0),Quiet);threading.Thread(target=srv.serve_forever,daemon=True).start();audit=[];selected={int(x) for x in sys.argv[1:] if x.isdigit()}
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-gpu']);page=b.new_page(viewport={'width':1080,'height':1350},device_scale_factor=1)
 for s in content:
  n=s['n']
  if selected and n not in selected:continue
  page.goto(f'http://127.0.0.1:{srv.server_port}/slides/slide-{n:02}.html');page.evaluate('document.fonts.ready');page.evaluate('Promise.all(Array.from(document.images).map(i=>i.decode()))');page.emulate_media(media='screen')
  for sel,key in [('.headline','headline'),('.body','body'),('.closing','closing')]:assert ' '.join(page.locator(sel).inner_text().split())==' '.join(s[key]),(n,key)
  assert page.locator('.headline span,.body span,.closing span').evaluate_all('(els)=>els.every(e=>e.scrollWidth<=e.clientWidth)'),n
  boxes=page.locator('.copy,.headline,.body,.closing,.intro-brand,.footer,.cta').evaluate_all('(els)=>els.map(e=>({name:e.className,x:e.getBoundingClientRect().x,right:e.getBoundingClientRect().right,y:e.getBoundingClientRect().y,bottom:e.getBoundingClientRect().bottom,overflow:e.scrollWidth>e.clientWidth}))')
  for box in boxes:assert box['x']>=63 and box['right']<=1017 and box['bottom']<=1300 and not box['overflow'],(n,box)
  c=page.context.new_cdp_session(page);c.send('DOM.enable');c.send('CSS.enable');root=c.send('DOM.getDocument')['root']['nodeId'];fonts=[]
  for sel in ['.headline','.body','.closing','.footer','.meta','.meet','.cta strong','.giant-word','.ghost']:
   for node in c.send('DOM.querySelectorAll',{'nodeId':root,'selector':sel})['nodeIds']:
    fs=c.send('CSS.getPlatformFontsForNode',{'nodeId':node})['fonts'];assert all(f['isCustomFont'] and (f['familyName']=='Preahvihear' or f['familyName'].startswith('Poppins')) for f in fs),(n,sel,fs);fonts.extend(fs)
  page.pdf(path=str(T/f'slide-{n:02}.pdf'),width='1080px',height='1350px',print_background=True,margin=dict(top='0',bottom='0',left='0',right='0'))
  subprocess.run(['pdftoppm','-singlefile','-scale-to-x','1080','-scale-to-y','1350','-png',str(T/f'slide-{n:02}.pdf'),str(T/f'slide-{n:02}')],check=True)
  im=Image.open(T/f'slide-{n:02}.png').convert('RGB');assert im.size==(1080,1350);im.save(D/f'ART-seven-calls-slide-{n:02}-static-v3.jpg',quality=98,subsampling=0)
  audit.append(dict(slide=n,copy_matches=True,fonts=fonts,boxes=boxes));print(f'Slide {n}: copy, fonts and margins verified',flush=True)
 b.close()
srv.shutdown()
if selected and (V/'audit.json').exists():audit=sorted([a for a in json.loads((V/'audit.json').read_text()) if a['slide'] not in selected]+audit,key=lambda a:a['slide'])
(V/'audit.json').write_text(json.dumps(audit,indent=2))
if '--partial' in sys.argv:sys.exit(0)
subprocess.run(['pdfunite']+[str(T/f'slide-{n:02}.pdf') for n in range(1,9)]+[str(D/'ART-seven-calls-design-static-v3.pdf')],check=True)
board=Image.new('RGB',(1728,1080),'#031B23')
for i in range(8):board.paste(Image.open(T/f'slide-{i+1:02}.png').resize((432,540)),((i%4)*432,(i//4)*540))
board.save(D/'ART-seven-calls-overview-v3.jpg',quality=96)
with zipfile.ZipFile(D/'ART-seven-calls-design-static-v3.zip','w',zipfile.ZIP_DEFLATED) as z:
 for f in sorted(D.iterdir()):
  if f.suffix in ['.pdf','.jpg']:z.write(f,f.name)
 for n in range(1,9):z.write(T/f'slide-{n:02}.png',f'PNG/slide-{n:02}.png')
print('Full eight-slide static carousel exported',flush=True)
