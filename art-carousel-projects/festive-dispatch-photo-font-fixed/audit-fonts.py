from pathlib import Path
from playwright.sync_api import sync_playwright
import json
p=Path(__file__).resolve().parent
report=[]
with sync_playwright() as w:
 b=w.chromium.launch();page=b.new_page(viewport={'width':1080,'height':1350})
 for n in range(2,10):
  page.goto((p/f'slides/slide-{n:02d}.html').as_uri(),wait_until='networkidle');page.evaluate('document.fonts.ready')
  c=page.context.new_cdp_session(page);c.send('DOM.enable');c.send('CSS.enable');root=c.send('DOM.getDocument')['root']['nodeId']
  selectors=['.photo-h','.photo-h em','.photo-pain','.photo-whatif','.photo-result','.setup-next','.reveal-body','.reveal-body strong','.reveal-sign','.benefit p','.summary-end','.cta-body','.cta-dm','.cta-save','.handle','.count','.kicker']
  for selector in selectors:
   nodes=c.send('DOM.querySelectorAll',{'nodeId':root,'selector':selector})['nodeIds']
   for node in nodes:
    info=c.send('CSS.getPlatformFontsForNode',{'nodeId':node})['fonts']
    expected='Preahvihear' if selector.startswith('.photo-h') else 'Poppins Medium'
    # Emoji only: intentional platform emoji, not substitute fonts for words.
    allowed=[f for f in info if f['familyName']==expected and f['isCustomFont']]
    other=[f for f in info if f not in allowed]
    assert not other or (selector in ['.setup-next','.reveal-sign'] and sum(f['glyphCount'] for f in other)<=1),(n,selector,info)
    assert allowed,(n,selector,info)
    report.append({'slide':n,'selector':selector,'fonts':info})
  c.detach();print(f'{n:02}: actual rendered heading/body fonts passed',flush=True)
 b.close()
(p/'proof/font-validation.json').write_text(json.dumps(report,indent=2))
