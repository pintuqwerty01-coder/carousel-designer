from pathlib import Path
from playwright.sync_api import sync_playwright
import json
p=Path(__file__).resolve().parent
report=[]
with sync_playwright() as w:
 b=w.chromium.launch();page=b.new_page(viewport={'width':1080,'height':1350})
 for n in range(1,10):
  page.goto((p/f'slides/slide-{n:02d}.html').as_uri(),wait_until='networkidle');page.evaluate('document.fonts.ready')
  result=page.evaluate('''() => {
  const rect=r=>({left:r.left,top:r.top,right:r.right,bottom:r.bottom,width:r.width,height:r.height});
  const textRects=e=>{const walker=document.createTreeWalker(e,NodeFilter.SHOW_TEXT);let node,items=[];while(node=walker.nextNode()){if(!node.textContent.trim())continue;let el=node.parentElement;if(el.closest('.source-symbol')||parseFloat(getComputedStyle(el).fontSize)===0)continue;const range=document.createRange();range.selectNodeContents(node);items.push(...[...range.getClientRects()].filter(r=>r.width>0&&r.height>0).map(rect));}return items;};
  const boxes=[...document.querySelectorAll('.cover-cta,.setup-next,.setup-topics,.photo-whatif,.photo-result,.benefit,.cta-dm')].map(e=>({class:e.className,box:rect(e.getBoundingClientRect()),textRects:textRects(e),text:e.innerText,iconRects:[...e.querySelectorAll('svg')].map(s=>rect(s.getBoundingClientRect()))}));
  const blocks=[...document.querySelectorAll('.cover-h,.cover-sub,.cover-note,.photo-h,.photo-pain,.photo-whatif,.photo-result,.setup-next,.setup-topics,.reveal-body,.reveal-ease,.reveal-sign,.summary-end,.cta-body,.cta-dm,.cta-save,.engagement')].map(e=>({class:e.className,box:rect(e.getBoundingClientRect())}));
  const mascot=document.querySelector('.mascot');
  return {boxes,blocks,mascot:mascot?rect(mascot.getBoundingClientRect()):null,topicCount:document.querySelectorAll('.setup-topic').length,benefitCount:document.querySelectorAll('.benefit').length,checkCount:document.querySelectorAll('.photo-result .source-symbol').length,extraWords:document.querySelectorAll('.scene-word,.brand-clock').length};
  }''')
  for box in result['boxes']:
   bounds=box['box'];assert box['textRects'],(n,box)
   for r in box['textRects']:
    assert r['left']>=bounds['left']+15 and r['right']<=bounds['right']-15,(n,'horizontal padding',box)
    assert r['top']>=bounds['top']+7 and r['bottom']<=bounds['bottom']-7,(n,'vertical padding',box)
   for r in box['iconRects']:
    assert r['left']>=bounds['left'] and r['right']<=bounds['right'] and r['top']>=bounds['top'] and r['bottom']<=bounds['bottom'],(n,'icon outside box',box)
  def overlap(a,b):return min(a['right'],b['right'])>max(a['left'],b['left'])+1 and min(a['bottom'],b['bottom'])>max(a['top'],b['top'])+1
  for i,a in enumerate(result['blocks']):
   for b1 in result['blocks'][i+1:]:assert not overlap(a['box'],b1['box']),(n,'text blocks overlap',a,b1)
   if result['mascot']:assert not overlap(a['box'],result['mascot']),(n,'copy overlaps mascot',a,result['mascot'])
  assert result['extraWords']==0,n
  if n==2:assert result['topicCount']==4,n
  if n==8:assert result['benefitCount']==4,n
  if n in (3,4,5,6):
   symbols=page.locator('.photo-result .source-symbol').all_text_contents();assert symbols==['✓','·','✓'],(n,symbols)
  if n==9:
   labels=page.locator('.engagement').inner_text();assert all(t in labels for t in ['Like the post','Leave a comment','Save & share it']),labels
  report.append({'slide':n,'boxes':result['boxes'],'status':'passed'})
  print(f'{n:02}: box padding, icon containment, hierarchy and point counts passed',flush=True)
 b.close()
(p/'proof/box-validation.json').write_text(json.dumps(report,indent=2))
