from pathlib import Path
from playwright.sync_api import sync_playwright
from PIL import Image,ImageChops
import io,json,re
p=Path(__file__).resolve().parent;source=json.loads((p.parent/'content.json').read_text());norm=lambda s:re.sub(r'\s+',' ',s).strip()
report=[]
with sync_playwright() as w:
 b=w.chromium.launch()
 for n in range(1,7):
  page=b.new_page(viewport={'width':1080,'height':1350});errs=[];page.on('pageerror',lambda e:errs.append(str(e)))
  page.goto((p/f'slides/slide-{n:02d}.html').as_uri(),wait_until='networkidle');page.evaluate('document.fonts.ready')
  assert page.locator('#hero-2d').count()==1
  assert page.locator('.camera-window').count()==0
  assert page.locator('.photo').get_attribute('src')==f'assets/clean-{n:02d}.png'
  frames=[];states=[]
  for t in [0,.125,.5,1.125,1.625,2.125,2.5,3.125,3.9]:
   page.evaluate('(t)=>Object.values(window.__timelines).forEach(tl=>tl.time(t,false))',t)
   states.append(page.evaluate('window.__actorState'))
   frames.append(Image.open(io.BytesIO(page.screenshot())).convert('RGB'))
  assert not errs,(n,errs)
  assert len(set(s['armR'] for s in states))>=2,(n,'Arm did not articulate')
  assert len(set(s['eyes'] for s in states))>=2,(n,'Expression did not change')
  assert ImageChops.difference(frames[0].crop((0,500,1080,1100)),frames[4].crop((0,500,1080,1100))).getbbox(),(n,'No visible animation')
  # Static text and photo must be invariant once the character and brand trail are hidden.
  page.add_style_tag(content='#hero-2d,#trail{visibility:hidden!important}')
  still=[]
  for t in (0,3.9):
   page.evaluate('(t)=>Object.values(window.__timelines).forEach(tl=>tl.time(t,false))',t)
   still.append(Image.open(io.BytesIO(page.screenshot())).convert('RGB'))
  assert ImageChops.difference(*still).getbbox() is None,(n,'Background or text moved')
  if n>1:
   text=norm(page.locator('body').inner_text())
   for line in source['slides'][n-1]['copy']:assert norm(line.replace('**','')) in text,(n,line)
  report.append({'slide':n,'arm_poses':sorted(set(s['armR'] for s in states)),'expressions':sorted(set(s['eyes'] for s in states)),'x_span':max(s['x'] for s in states)-min(s['x'] for s in states),'states':states})
  print(f'{n:02}: articulated arms and expressions; visible scene animation; stationary photograph and text; no JS errors',flush=True);page.close()
 # Cover and setup must not share the same initial pose or action pattern.
 a=report[0]['states'][0];bstate=report[1]['states'][0]
 assert a['legs']!=bstate['legs'] and a['armR']!=bstate['armR']
 assert report[0]['x_span']>200 and report[1]['x_span']==0
 b.close()
(p/'proof/actor-validation.json').write_text(json.dumps(report,indent=2))
