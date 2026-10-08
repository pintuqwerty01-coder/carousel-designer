from pathlib import Path
from playwright.sync_api import sync_playwright
import json
p=Path(__file__).resolve().parent;canonical=json.loads((p/'source-content.json').read_text())['slides'];report=[]
with sync_playwright() as w:
 b=w.chromium.launch();page=b.new_page(viewport={'width':1080,'height':1350})
 for i in [1,4]:
  page.goto((p/f'slides/slide-{i:02}.html').as_uri(),wait_until='networkidle');page.evaluate('document.fonts.ready');s=page.locator('.sl').nth(i-1);text=' '.join(s.inner_text().split()).casefold()
  for line in canonical[i-1]['copy']:
   for part in line.replace('**','').replace('✓ ','').split('·'):assert ' '.join(part.split()).casefold() in text,(i,part)
  cd=page.context.new_cdp_session(page);cd.send('DOM.enable');cd.send('CSS.enable');root=cd.send('DOM.getDocument');checks=[]
  for sel,family in ([('.big','Poppins'),('.hd','Preahvihear'),('.bd','Poppins')] if i==1 else [('.hd','Preahvihear'),('.bd','Poppins'),('.wi','Poppins')]):
   q=cd.send('DOM.querySelector',{'nodeId':root['root']['nodeId'],'selector':f'.sl:nth-child({i}) {sel}'});font=cd.send('CSS.getPlatformFontsForNode',{'nodeId':q['nodeId']})['fonts'];assert any(x['isCustomFont'] and family in x['familyName'] for x in font),(sel,font);checks.append({'selector':sel,'fonts':font})
  report.append({'slide':i,'copy':'exact','fonts':checks})
 (p/'proof/copy-font-validation.json').write_text(json.dumps(report,indent=2))
 h='<style>@page{size:1080px 1350px;margin:0}body{margin:0}img{display:block;width:1080px;height:1350px;break-after:page}img:last-child{break-after:auto}</style>'+''.join(f'<img src="stills/slide-{i:02}.png">' for i in [1,4]);(p/'review.html').write_text(h);page.goto((p/'review.html').as_uri(),wait_until='networkidle');page.pdf(path=str(p/'two-slide-review.pdf'),prefer_css_page_size=True,print_background=True)
 page.set_viewport_size({'width':1104,'height':699});page.add_style_tag(content='body{display:flex;gap:12px;padding:12px;background:#03161b}img{width:540px;height:675px}');page.screenshot(path=str(p/'two-slide-preview.png'),full_page=True);b.close()
print('Two-slide PDF, overview, exact-copy and actual-font checks complete.')
