from pathlib import Path
from playwright.sync_api import sync_playwright
import subprocess,json,sys
p=Path(__file__).resolve().parent
with sync_playwright() as w:
 b=w.chromium.launch()
 for n in ([int(v) for v in sys.argv[1].split(",")] if len(sys.argv)>1 else [7]):
  page=b.new_page(viewport={'width':1080,'height':1350},device_scale_factor=1)
  page.goto((p/f'slides/slide-{n:02d}.html').as_uri(),wait_until='networkidle');page.evaluate('document.fonts.ready')
  assert page.evaluate('[...document.images].every(i=>i.complete&&i.naturalWidth>0)')
  out=p/f'render/out/slide-{n:02d}.mp4'
  proc=subprocess.Popen(['ffmpeg','-v','error','-y','-f','image2pipe','-vcodec','png','-framerate','30','-i','-','-c:v','libx264','-profile:v','high','-pix_fmt','yuv420p','-crf','16','-preset','fast','-movflags','+faststart','-an',str(out)],stdin=subprocess.PIPE)
  for frame in range(120):
   t=frame/30;page.evaluate('(t)=>Object.values(window.__timelines).forEach(tl=>tl.time(t,false))',t)
   proc.stdin.write(page.screenshot())
  proc.stdin.close();assert proc.wait()==0
  print(f'{n:02}: 120 frames encoded',flush=True);page.close()
 b.close()
