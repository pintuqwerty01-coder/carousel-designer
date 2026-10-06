import importlib.util,pathlib,re,json,shutil,html
p=pathlib.Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('kit','/workspace/art-carousel-kit/scripts/build.py');b=importlib.util.module_from_spec(spec);spec.loader.exec_module(b)
src=(p/'source-script.md').read_text().split('## Instagram carousel (9 slides)')[1].split('### Caption')[0]
parts=re.findall(r'\*\*Slide (\d+):[^\n]+\n(.*?)(?=\n---|\Z)',src,re.S)
slides={int(n):[line.strip() for line in body.strip().splitlines() if line.strip()] for n,body in parts}
def plain(s):return s.replace('**','')
lib=b.LIB+'\n'+(p/'scenes.js').read_text()
out=p/'slides';out.mkdir(exist_ok=True);shutil.copytree(b.KIT,out/'assets',dirs_exist_ok=True)
(p/'content.json').write_text(json.dumps({'status':'DRAFT REVIEW — not approved for publication','handle':'@arealtimetech','slides':[{'number':n,'copy':lines} for n,lines in slides.items()]},ensure_ascii=False,indent=2))
for n,lines in slides.items():
 if n==1:continue
 opts={};js='';dark=False
 if n in (3,4,5,6):
  c={'n':n-2,'of':4,'label':['Orders','Stock','Paperwork','Dispatch'][n-3],'scene':['festiveOrders','festiveStock','festivePaperwork','festiveDispatch'][n-3],'headline':plain(lines[0]),'pain':plain(lines[1]),'whatif':plain(lines[2]),'outcome':[plain(lines[3])]}
  theme,css,inner,key,canvas,js,dark=b.task(c)
  css+='\n.tk-h{font-size:62px}.tk-pain{font-size:29px;line-height:1.35}.tk-col{gap:18px}.tk-whatif{font-size:29px;line-height:1.35}.chip{font-size:26px;line-height:1.3}.chip svg{display:none}\n'
 elif n==7:
  theme='dark';dark=True;key='festiveReveal';canvas='scene'
  css='.logo{position:absolute;left:84px;top:76px;width:320px}.logo img{width:100%}.review-col{top:235px;gap:24px}.review-h{font-size:54px;line-height:1.2}.review-body{font:400 30px/1.4 Poppins;color:#CFCFCF}.review-sign{font:500 27px/1.4 Poppins;max-width:650px}#scene{position:absolute;inset:0}'
  inner=f'<div class="logo" id="logo"><img src="assets/brand/logo-on-dark.png" alt="ART"/></div><div class="col review-col"><div class="h-display review-h">{b.hl(plain(lines[0]))}</div><div class="review-body">{b.rich(lines[1])}</div><div class="review-sign">{html.escape(plain(lines[2]))}</div></div><canvas id="scene" width="1080" height="1350"></canvas>'
  js='tl.fromTo("#logo",{opacity:0,scale:.96},{opacity:1,scale:1,duration:.8},0);'
 elif n in (2,8):
  theme='light';key='festiveSetup' if n==2 else 'festiveOutcome';canvas='scene';opts={'done':n==8}
  css='.review-col{top:100px;gap:26px}.review-h{font-size:70px;line-height:1.2}.review-body{font:500 33px/1.4 Poppins;color:#3D3D3D}.stage{position:relative;width:912px;height:420px;border-radius:26px;background:#EEF9FB;overflow:hidden}.stage canvas{width:912px;height:420px}.result{padding:14px 20px;border-radius:16px;background:linear-gradient(135deg,#41A486,#1C5E55);color:white;font:600 30px/1.3 Poppins}.results{display:grid;grid-template-columns:1fr 1fr;gap:16px}'
  if n==2: body=f'<div class="review-body">{html.escape(plain(lines[1]))}</div><div class="review-body">{html.escape(plain(lines[2]))}</div>'
  else:body='<div class="results">'+''.join(f'<div class="result">{html.escape(plain(x))}</div>' for x in lines[1:5])+'</div>'
  inner=f'<div class="col review-col"><div class="h-display review-h">{html.escape(plain(lines[0]))}</div>{body}<div class="stage"><canvas id="scene" width="912" height="420" data-scale="1.25"></canvas></div>'+(f'<div class="review-body">{html.escape(plain(lines[5]))}</div>' if n==8 else '')+'</div>'
 else:
  theme='aqua';key='festiveCTA';canvas='scene'
  css='.review-col{top:125px;gap:35px}.review-h{font-size:88px;line-height:1.2}.review-body{font:500 38px/1.4 Poppins}.review-save{font:500 31px/1.4 Poppins;max-width:510px}.card{position:absolute;right:84px;bottom:150px;width:352px;height:300px;background:white;border-radius:28px;overflow:hidden}'
  inner=f'<div class="col review-col"><div class="h-display review-h">{html.escape(plain(lines[0]))}</div><div class="review-body">{html.escape(plain(lines[1]))}</div><div class="review-body">{html.escape(plain(lines[2]))}</div><div class="review-save">{html.escape(plain(lines[3]))}</div></div><div class="card"><canvas id="scene" width="352" height="300"></canvas></div>'
 (out/f'slide-{n:02d}.html').write_text(b.page(f'slide-{n:02d}',theme,inner,css,key,canvas,js,n,9,'@arealtimetech',dark,lib,opts))
 print('Built',n)
(p/'caption.txt').write_text((p/'source-script.md').read_text().split('### Caption\n')[1].split('**Production notes:**')[0].strip()+'\n')
