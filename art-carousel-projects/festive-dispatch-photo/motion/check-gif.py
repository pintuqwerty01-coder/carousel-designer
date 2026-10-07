from pathlib import Path
from playwright.sync_api import sync_playwright
from PIL import Image,ImageChops
import io
p=Path(__file__).resolve().parent
(p/'gif-preview.html').write_text('<!doctype html><meta charset="utf-8"><style>body{margin:0;background:#1a1a1a}img{width:1080px;height:675px}</style><img src="first-two-actions.gif" alt="Cover carries a parcel; setup sorts the order queue">')
with sync_playwright() as w:
 b=w.chromium.launch();page=b.new_page(viewport={'width':1080,'height':675});page.goto((p/'gif-preview.html').as_uri(),wait_until='load');assert page.evaluate('document.images[0].complete&&document.images[0].naturalWidth===1080');a=Image.open(io.BytesIO(page.screenshot())).convert('RGB');page.wait_for_timeout(1500);bb=Image.open(io.BytesIO(page.screenshot())).convert('RGB');assert ImageChops.difference(a,bb).getbbox() is not None;print('First-two GIF decodes and visibly animates in Chromium',flush=True);b.close()
