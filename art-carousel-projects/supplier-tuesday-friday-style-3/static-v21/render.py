from pathlib import Path
import threading,http.server,subprocess,json,zipfile,sys
from playwright.sync_api import sync_playwright
from PIL import Image
V=Path(__file__).resolve().parent;P=V.parent;D=V/'delivery';T=V/'proof';copy=json.loads((V/'content.json').read_text())['slides']
class Quiet(http.server.SimpleHTTPRequestHandler):
 def __init__(self,*a,**k):super().__init__(*a,directory=str(P),**k)
 def log_message(self,*a):pass
srv=http.server.ThreadingHTTPServer(('127.0.0.1',0),Quiet);threading.Thread(target=srv.serve_forever,daemon=True).start();audit=[];selected={int(x) for x in sys.argv[1:] if x.isdigit()}
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-gpu']);page=b.new_page(viewport={'width':1080,'height':1350},device_scale_factor=1)
 for n,s in enumerate(copy,1):
  if selected and n not in selected:continue
  page.goto(f'http://127.0.0.1:{srv.server_port}/static-v21/slides/slide-{n:02}.html');page.evaluate('document.fonts.ready');page.evaluate('Promise.all(Array.from(document.images).map(i=>i.decode()))');page.emulate_media(media='screen')
  for sel,key in [('.headline','headline'),('.body','body'),('.scene-label','scene_label')]:
   if s[key] is None:
    assert page.locator(sel).count()==0;continue
   expected=' '.join(s[key]) if isinstance(s[key],list) else s[key];assert ' '.join(page.locator(sel).inner_text().split())==' '.join(expected.split()),(n,key)
  if s.get('prop_copy'):
   actual=' '.join(page.locator('.prop-text').inner_text().split())
   for phrase in s['prop_copy']:assert phrase in actual,(n,phrase,actual)
  if n==3:
   assert page.locator('.thread-status').evaluate('(e)=>e.getBoundingClientRect().bottom<=e.closest(".mobile-redesign").getBoundingClientRect().bottom-8')
   assert page.locator('.mobile-redesign p,.mobile-redesign h2').evaluate_all('(els)=>els.every(e=>e.scrollWidth<=e.clientWidth)')
  if n==2:assert page.locator('.intro-brand .meet').inner_text()==s['kicker'] and page.locator('.intro-brand .brand-logo').count()==1
  if n==2:
   assert page.locator('.copy').evaluate('(e)=>Array.from(e.children).map(x=>x.className).join(",")=="intro-brand,body,headline"')
   for phrase in s['screen_copy']:assert phrase in page.locator('.tablet-ui').inner_text()
  if s.get('pipeline'):
   assert page.locator('.stage h2').all_inner_texts()==[x[0] for x in s['pipeline']]
   assert page.locator('.stage p').all_inner_texts()==[x[1] for x in s['pipeline']]
  if n==7:assert page.locator('.closing-kicker').inner_text()==s['kicker']
  if s['prompt'] is not None:assert page.locator('.prompt').inner_text()==s['prompt']
  else:assert page.locator('.prompt').count()==0
  assert page.locator('.result').all_inner_texts()==s['results']
  if n==5:assert page.locator('.quote strong').all_inner_texts()==['A','B','C']
  assert [' '.join(x.split()) for x in page.locator('.rule p').all_inner_texts()]==s['rules']
  if s['cta']:assert ' '.join(page.locator('.brand-cta span').inner_text().split())==s['cta']
  if s.get('pipeline'):assert page.locator('.stage h2,.stage p').evaluate_all('(els)=>els.every(e=>e.scrollWidth<=e.clientWidth)')
  boxes=page.locator('.copy,.headline,.body,.prompt,.scene-label,.result,.brand-cta,.prop-text,.rule,.quote,.closing-kicker,.pipeline,.stage,.intro-brand').evaluate_all('(els)=>els.map(e=>({class:e.className,x:e.getBoundingClientRect().x,y:e.getBoundingClientRect().y,right:e.getBoundingClientRect().right,bottom:e.getBoundingClientRect().bottom,overflow:e.scrollWidth>e.clientWidth}))')
  for box in boxes:
   if box['right']==0:continue
   assert box['x']>=83 and box['right']<=997 and box['bottom']<=1220 and (not box['overflow'] or box['class']=='stage'),(n,box)
  c=page.context.new_cdp_session(page);c.send('DOM.enable');c.send('CSS.enable');root=c.send('DOM.getDocument')['root']['nodeId'];fonts=[]
  for sel in ['.headline','.body','.prompt','.scene-label','.result','.brand-cta span','.footer','.prop-text small','.prop-text strong','.prop-text em','.prop-text p','.sent','.rule p','.quote small','.quote strong','.closing-kicker','.pad-redesign h2 span','.pad-alert span','.pad-action','.mobile-redesign h2','.mobile-redesign header i','.chat-message>span','.thread-status span','.intro-brand .meet','.tablet-ui h2','.tablet-ui p','.stage h2','.stage p','.impact-pad h2','.pad-caption']:
   for node in c.send('DOM.querySelectorAll',{'nodeId':root,'selector':sel})['nodeIds']:
    fs=c.send('CSS.getPlatformFontsForNode',{'nodeId':node})['fonts'];assert all(f['familyName']=='Preahvihear' and f['isCustomFont'] for f in fs),(n,sel,fs);fonts.extend(fs)
  pdf=T/f'slide-{n:02}.pdf';page.pdf(path=str(pdf),width='1080px',height='1350px',print_background=True,margin=dict(top='0',bottom='0',left='0',right='0'))
  subprocess.run(['pdftoppm','-scale-to-x','1080','-scale-to-y','1350','-singlefile','-png',str(pdf),str(T/f'slide-{n:02}')],check=True)
  im=Image.open(T/f'slide-{n:02}.png').convert('RGB');assert im.size==(1080,1350);im.save(D/f'ART-supplier-follow-through-slide-{n:02}-v21.jpg',quality=98,subsampling=0)
  audit.append(dict(slide=n,copy_matches=True,font='Preahvihear custom font',boxes=boxes));print(f'Slide {n}: copy, fonts, bounds verified',flush=True)
 b.close()
srv.shutdown()
if selected and (V/'audit.json').exists():
 audit=sorted([a for a in json.loads((V/'audit.json').read_text()) if a['slide'] not in selected]+audit,key=lambda a:a['slide'])
(V/'audit.json').write_text(json.dumps(audit,indent=2))
if '--partial' in sys.argv:sys.exit(0)
subprocess.run(['pdfunite']+[str(T/f'slide-{n:02}.pdf') for n in range(1,8)]+[str(D/'ART-supplier-follow-through-static-v21.pdf')],check=True)
# compact 4-by-2 overview
board=Image.new('RGB',(2160,1350),'#1a1a1a')
for i in range(7):board.paste(Image.open(T/f'slide-{i+1:02}.png').resize((540,675)),((i%4)*540,(i//4)*675))
board.save(D/'ART-supplier-follow-through-overview-v21.jpg',quality=96,subsampling=0)
with zipfile.ZipFile(D/'ART-supplier-follow-through-static-v21.zip','w',zipfile.ZIP_DEFLATED) as z:
 for f in sorted(D.iterdir()):
  if f.suffix in ['.jpg','.pdf']:z.write(f,f.name)
 for n in range(1,8):z.write(T/f'slide-{n:02}.png',f'PNG/slide-{n:02}.png')
print('Complete static delivery exported',flush=True)
