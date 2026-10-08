from pathlib import Path
from playwright.sync_api import sync_playwright
import json
p=Path(__file__).resolve().parent
(p/'stills').mkdir(exist_ok=True);(p/'proof').mkdir(exist_ok=True)
with sync_playwright() as w:
 b=w.chromium.launch();page=b.new_page(viewport={'width':1080,'height':1350});reports=[]
 for n in [1,4]:
  page.goto((p/f'slides/slide-{n:02}.html').as_uri(),wait_until='networkidle');page.evaluate('document.fonts.ready');page.evaluate('Object.values(window.__timelines).forEach(t=>t.seek(3,false))')
  data=page.evaluate('''()=>{let r=[...document.querySelectorAll('.tx')].map(e=>({text:e.innerText,rect:e.getBoundingClientRect()})).filter(x=>x.rect.right>0&&x.rect.left<1080);return r.map(x=>({text:x.text,left:x.rect.left,top:x.rect.top,right:x.rect.right,bottom:x.rect.bottom}))}''')
  for x in data:assert x['left']>=40 and x['right']<=1050 and x['bottom']<=1250,(n,x)
  for i,a in enumerate(data):
   for v in data[i+1:]:assert min(a['right'],v['right'])<=max(a['left'],v['left']) or min(a['bottom'],v['bottom'])<=max(a['top'],v['top']),(n,a,v)
  assert page.evaluate('[...document.images].every(x=>x.complete&&x.naturalWidth>0)')
  page.screenshot(path=str(p/f'stills/slide-{n:02}.png'));reports.append({'slide':n,'text':data,'assets':'loaded'})
 (p/'proof/layout.json').write_text(json.dumps(reports,indent=2))
 html='''<style>@page{size:1080px 1350px;margin:0}body{margin:0}img{display:block;width:1080px;height:1350px;break-after:page}img:last-child{break-after:auto}</style>'''+''.join(f'<img src="../stills/slide-{n:02}.png">' for n in [1,4])
 (p/'proof/review.html').write_text(html);page.goto((p/'proof/review.html').as_uri(),wait_until='networkidle');page.pdf(path=str(p/'first-two-proof.pdf'),prefer_css_page_size=True,print_background=True)
 page.set_viewport_size({'width':1128,'height':720});page.add_style_tag(content='body{display:flex;gap:24px;padding:12px;background:#08303A}img{width:540px;height:675px}');page.screenshot(path=str(p/'proof/first-two.png'),full_page=True)
 b.close()
print('Cover and transit proof ready; assets and text bounds verified.')
