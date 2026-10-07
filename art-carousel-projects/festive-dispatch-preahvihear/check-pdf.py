from pathlib import Path
from playwright.sync_api import sync_playwright
p=Path(__file__).resolve().parent
pages=list((p/'proof/pdf-pages').glob('page-*.png'));assert len(pages)==9
html='<style>body{margin:0;padding:12px;background:#1a1a1a;display:grid;grid-template-columns:repeat(3,360px);gap:12px}img{width:360px;height:450px}</style>'+''.join(f'<img src="pdf-pages/page-{n}.png">' for n in range(1,10))
(p/'proof/pdf-review.html').write_text(html)
with sync_playwright() as w:
 b=w.chromium.launch();page=b.new_page(viewport={'width':1128,'height':1386})
 page.goto((p/'proof/pdf-review.html').as_uri(),wait_until='networkidle')
 assert page.evaluate('[...document.images].every(i=>i.complete&&i.naturalWidth===360&&i.naturalHeight===450)')
 page.screenshot(path=str(p/'proof/exported-pdf-overview.png'),full_page=True);b.close()
print('All nine actual exported PDF pages decoded and review proof captured')
