from pathlib import Path
from playwright.sync_api import sync_playwright
import json,subprocess,sys
p=Path(__file__).resolve().parent;src=json.loads((p.parent/'source-content.json').read_text())['slides'];reports=[]
with sync_playwright() as w:
 b=w.chromium.launch();page=b.new_page(viewport={'width':1080,'height':1350})
 for name in [f'slide-{i:02}' for i in range(1,10)]:
  n=int(name[-2:]);page.goto((p/f'{name}.html').as_uri(),wait_until='networkidle');page.evaluate('document.fonts.ready')
  text=' '.join(page.locator('body').inner_text().split()).casefold()
  for line in src[n-1]['copy']:
   for part in line.replace('**','').replace('✓ ','').split('·'):assert ' '.join(part.split()).casefold() in text,(name,part)
  rects=page.evaluate('''()=>[...document.querySelectorAll('.tx')].flatMap(e=>{let w=document.createTreeWalker(e,NodeFilter.SHOW_TEXT),a=[],n;while(n=w.nextNode()){if(!n.textContent.trim())continue;let r=document.createRange();r.selectNodeContents(n);a.push(...[...r.getClientRects()].map(x=>({left:x.left,right:x.right,top:x.top,bottom:x.bottom})));}return a})''')
  assert all(r['left']>=55 and r['right']<=1040 and r['bottom']<=1230 for r in rects),(name,rects)
  assert page.evaluate('[...document.images].every(x=>x.complete&&x.naturalWidth>0)')
  page.evaluate('Object.values(window.__timelines).forEach(x=>x.seek(3))');page.screenshot(path=str(p/f'{name}.png'));reports.append({'name':name,'copy':'exact','bounds':rects})
 (p/'validation.json').write_text(json.dumps(reports,indent=2))
 html='<style>@page{size:1080px 1350px;margin:0}body{margin:0}img{display:block;width:1080px;height:1350px;break-after:page}img:last-child{break-after:auto}</style>'+''.join(f'<img src="{x}.png">' for x in [f'slide-{i:02}' for i in range(1,10)])
 (p/'review.html').write_text(html);page.goto((p/'review.html').as_uri(),wait_until='networkidle');page.pdf(path=str(p/'carousel-review.pdf'),prefer_css_page_size=True,print_background=True)
 page.set_viewport_size({'width':1128,'height':1386});page.add_style_tag(content='body{display:grid;grid-template-columns:repeat(3,360px);gap:12px;padding:12px;background:#03161B}img{width:360px;height:450px}');page.screenshot(path=str(p/'all-slides.png'),full_page=True)
 if '--stills-only' in sys.argv:
  b.close();sys.exit(0)
 for name in [f'slide-{i:02}' for i in range(1,10)]:
  page.set_viewport_size({'width':1080,'height':1350});page.goto((p/f'{name}.html').as_uri(),wait_until='networkidle');page.evaluate('document.fonts.ready');frames=p/f'frames-{name}';frames.mkdir(exist_ok=True);bounds=[]
  for i in range(120):
   page.evaluate('(t)=>Object.values(window.__timelines).forEach(x=>x.seek(t))',i/30)
   if i in [0,119]:bounds.append(page.evaluate('''()=>[...document.querySelectorAll('.tx')].map(e=>{let r=e.getBoundingClientRect();return [r.left,r.top,r.right,r.bottom]})'''))
   page.screenshot(path=str(frames/f'{i:03}.jpg'),type='jpeg',quality=96)
   if i%40==0:print(name,i,'/120',flush=True)
  assert bounds[0]==bounds[1]
  subprocess.run(['ffmpeg','-v','error','-y','-framerate','30','-i',str(frames/'%03d.jpg'),'-c:v','libx264','-preset','fast','-crf','18','-pix_fmt','yuv420p','-movflags','+faststart',str(p/f'{name}.mp4')],check=True)
  print(name,'rendered',flush=True)
 b.close()
print('Nine individual videos rendered.',flush=True)
