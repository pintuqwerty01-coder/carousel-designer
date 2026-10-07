from pathlib import Path
from playwright.sync_api import sync_playwright
import json
p=Path(__file__).resolve().parent
report=[]
with sync_playwright() as w:
 b=w.chromium.launch();page=b.new_page(viewport={'width':1080,'height':1350})
 for n in range(1,10):
  page.goto((p/f'slides/slide-{n:02d}.html').as_uri(),wait_until='networkidle');page.evaluate('document.fonts.ready')
  c=page.context.new_cdp_session(page);c.send('DOM.enable');c.send('CSS.enable');root=c.send('DOM.getDocument')['root']['nodeId']
  selectors=['.cover-note','.setup-topic','.reveal-ease','.engagement-box','.scene-word','.cover-h','.cover-h em','.cover-sub','.cover-cta','.photo-h','.photo-h em','.photo-pain','.photo-whatif','.point-box','.setup-next','.reveal-body','.reveal-body strong','.reveal-sign','.benefit p','.summary-end','.cta-body','.cta-dm','.cta-save','.handle','.count','.kicker']
  for selector in selectors:
   nodes=c.send('DOM.querySelectorAll',{'nodeId':root,'selector':selector})['nodeIds']
   for node in nodes:
    info=c.send('CSS.getPlatformFontsForNode',{'nodeId':node})['fonts']
    expected='Preahvihear'
    # Emoji only: intentional platform emoji, not substitute fonts for words.
    allowed=[f for f in info if f['familyName']==expected and f['isCustomFont']]
    other=[f for f in info if f not in allowed]
    assert not other,(n,selector,info)
    assert allowed,(n,selector,info)
    report.append({'slide':n,'selector':selector,'fonts':info})
  rectangles=page.evaluate('''() => {
 const selectors=['.cover-note','.setup-topic','.reveal-ease','.engagement-box','.scene-word','.cover-h','.cover-sub','.cover-cta','.photo-h','.photo-pain','.photo-whatif','.point-box','.setup-next','.reveal-body','.reveal-sign','.benefit p','.summary-end','.cta-body','.cta-dm','.cta-save'];
 return selectors.flatMap(s=>[...document.querySelectorAll(s)].map(e=>{const range=document.createRange();range.selectNodeContents(e);const box=e.getBoundingClientRect();return {selector:s,box:{left:box.left,right:box.right,top:box.top,bottom:box.bottom},text:[...range.getClientRects()].filter(r=>r.width>0&&r.height>0).map(r=>({left:r.left,right:r.right,top:r.top,bottom:r.bottom}))};}));
}''')
  for item in rectangles:
   assert all(r['left']>=83 and r['right']<=997 and r['bottom']<=1221 for r in item['text']),(n,item)
   assert all(r['right']<=item['box']['right']+1 for r in item['text']),(n,item)
  pairs=[('.photo-h','.photo-pain'),('.photo-h','.reveal-body'),('.reveal-body','.reveal-sign'),('.photo-whatif','.point-box'),('.cta-dm','.cta-save'),('.cover-h','.cover-sub'),('.cover-sub','.cover-note'),('.reveal-body','.reveal-ease'),('.reveal-ease','.reveal-sign'),('.cta-save','.engagement-box')]
  boxes={r['selector']:r['box'] for r in rectangles}
  for first,second in pairs:
   if first in boxes and second in boxes:assert boxes[first]['bottom']+8<=boxes[second]['top'],(n,first,second,boxes)
  c.detach();print(f'{n:02}: actual rendered heading/body fonts passed',flush=True)
 b.close()
(p/'proof/font-validation.json').write_text(json.dumps(report,indent=2))
