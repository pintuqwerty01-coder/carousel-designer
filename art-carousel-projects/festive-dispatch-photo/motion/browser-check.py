from pathlib import Path
from playwright.sync_api import sync_playwright
p=Path(__file__).resolve().parent
(p/'playback.html').write_text('<!doctype html><body style="background:#1a1a1a;color:white;font-family:sans-serif"><h1>Festive dispatch — first six motion slides</h1>'+''.join(f'<video controls muted playsinline preload="metadata" style="width:270px" src="render/out/slide-{n:02d}.mp4"></video>' for n in range(1,7)))
with sync_playwright() as w:
 b=w.chromium.launch();page=b.new_page();page.goto((p/'playback.html').as_uri(),wait_until='networkidle')
 for n in range(6):
  data=page.evaluate('''async n=>{const v=document.querySelectorAll('video')[n];await v.play();await new Promise(r=>setTimeout(r,250));v.pause();return [v.videoWidth,v.videoHeight,v.duration,v.currentTime,v.error&&v.error.message]}''',n)
  assert data[0:3]==[1080,1350,4] and data[3]>0 and data[4] is None,data
  print(f'{n+1:02}: Chromium video playback and decoded dimensions OK',flush=True)
 b.close()
