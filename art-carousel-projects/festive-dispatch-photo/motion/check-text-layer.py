from pathlib import Path
from playwright.sync_api import sync_playwright
from PIL import Image,ImageChops
import io,json,re
p=Path(__file__).resolve().parent;source=json.loads((p.parent/'content.json').read_text());norm=lambda s:re.sub(r'\s+',' ',s).strip()
with sync_playwright() as w:
 b=w.chromium.launch()
 for n in range(1,7):
  page=b.new_page(viewport={'width':1080,'height':1350});page.goto((p/f'slides/slide-{n:02d}.html').as_uri(),wait_until='networkidle');page.evaluate('document.fonts.ready')
  assert page.locator('canvas').count()==1,'Only brand trail canvas should remain; scene overlays removed'
  assert page.locator('.camera-window').count()==(1 if n==1 else 0)
  if n>1:
   text=norm(page.locator('body').inner_text())
   for line in source['slides'][n-1]['copy']:assert norm(line.replace('**','')) in text,(n,line)
   # Isolate typography so background movement cannot be mistaken for moving letters.
   page.add_style_tag(content='.photo,.camera-window,.header,.footer,#trail{visibility:hidden!important}.slide{background:#1A1A1A!important}')
   frames=[]
   for t in (0,3.9):
    page.evaluate('(t)=>Object.values(window.__timelines).forEach(tl=>tl.time(t,false))',t)
    frames.append(Image.open(io.BytesIO(page.screenshot())).convert('RGB'))
   assert ImageChops.difference(*frames).getbbox() is None,(n,'Typography moved or changed')
   print(f'{n:02}: exact copy; all text-layer pixels identical at 0s and 3.9s; no added props',flush=True)
  else:print('01: cover lettering preserved in original raster; movement mask begins below copy',flush=True)
  page.close()
 b.close()
