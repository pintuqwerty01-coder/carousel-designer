from pathlib import Path
from playwright.sync_api import sync_playwright
p=Path(__file__).resolve().parent
with sync_playwright() as w:
 b=w.chromium.launch()
 for n in range(7,10):
  page=b.new_page(viewport={'width':1080,'height':1350},device_scale_factor=1)
  page.goto((p/f'slides/slide-{n:02d}.html').as_uri(),wait_until='networkidle')
  page.evaluate('document.fonts.ready')
  page.evaluate('Object.values(window.__timelines).forEach(t=>t.progress(1,false));0')
  page.wait_for_timeout(500)
  page.screenshot(path=str(p/f'stills/slide-{n:02d}.png'))
  print(f'{n:02}: fresh-page static capture',flush=True)
  page.close()
 b.close()
