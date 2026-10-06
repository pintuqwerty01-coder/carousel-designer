import json,pathlib,re,html
from playwright.sync_api import sync_playwright
p=pathlib.Path(__file__).resolve().parent
content=json.loads((p/'content.json').read_text())
with sync_playwright() as w:
 b=w.chromium.launch(executable_path='/usr/bin/chromium')
 page=b.new_page()
 for slide in content['slides']:
  n=slide['number']
  if n==1:continue
  text=(p/'slides'/f'slide-{n:02d}.html').read_text()
  # Parse HTML locally without navigation; check each original line's visible text.
  page.set_content(text,wait_until='domcontentloaded')
  visible=page.locator('body').inner_text()
  norm=lambda s:re.sub(r'\s+',' ',s).strip()
  for line in slide['copy']:
   assert norm(line.replace('**','')) in norm(visible),(n,line)
  print(f'{n:02d}: all source lines retained')
 b.close()
