from playwright.sync_api import sync_playwright
from PIL import Image,ImageChops
from pathlib import Path
p=Path('/workspace/art-carousel-projects/festive-dispatch')
with sync_playwright() as w:
 b=w.chromium.launch();pg=b.new_page(viewport={'width':1080,'height':1350});pg.goto((p/'slides/slide-03.html').as_uri());pg.wait_for_timeout(800)
 for t,name in [(.1,'a'),(3.9,'b')]:
  pg.evaluate(f'Object.values(window.__timelines).forEach(tl=>tl.seek({t},false));0');pg.screenshot(path=str(p/'proof'/f'static-{name}.png'))
 b.close()
a=Image.open(p/'proof/static-a.png').crop((0,0,1080,400));b=Image.open(p/'proof/static-b.png').crop((0,0,1080,400))
assert ImageChops.difference(a,b).getbbox() is None
print('Uncompressed headline region is identical at 0.1s and 3.9s')
