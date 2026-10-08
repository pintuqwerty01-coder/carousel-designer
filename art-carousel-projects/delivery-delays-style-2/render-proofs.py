from pathlib import Path
from playwright.sync_api import sync_playwright
import subprocess,json
p=Path(__file__).resolve().parent
out=p/'render/out';out.mkdir(parents=True,exist_ok=True)
reports=[]
with sync_playwright() as w:
 b=w.chromium.launch();page=b.new_page(viewport={'width':1080,'height':1350},device_scale_factor=1)
 for n in [1,4]:
  frames=p/f'render/frames-{n:02}';frames.mkdir(exist_ok=True)
  page.goto((p/f'slides/slide-{n:02}.html').as_uri(),wait_until='networkidle');page.evaluate('document.fonts.ready')
  bounds=[]
  for i in range(120):
   page.evaluate('(t)=>Object.values(window.__timelines).forEach(x=>x.seek(t,false))',i/30)
   if i in [0,119]:bounds.append(page.evaluate('''()=>[...document.querySelectorAll('.tx')].map(e=>e.getBoundingClientRect()).filter(r=>r.right>0&&r.left<1080).map(r=>[r.left,r.top,r.right,r.bottom])'''))
   page.screenshot(path=str(frames/f'{i:03}.png'))
   if i%40==0:print(f'{n:02}: {i}/120 frames',flush=True)
  assert bounds[0]==bounds[1],(n,'text geometry moved')
  mp4=out/f'slide-{n:02}.mp4'
  subprocess.run(['ffmpeg','-v','error','-y','-framerate','30','-i',str(frames/'%03d.png'),'-c:v','libx264','-crf','19','-preset','fast','-pix_fmt','yuv420p','-movflags','+faststart',str(mp4)],check=True)
  probe=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_entries','stream=width,height,r_frame_rate:format=duration','-of','json',str(mp4)]))
  st=probe['streams'][0];assert (st['width'],st['height'],st['r_frame_rate'])==(1080,1350,'30/1');assert float(probe['format']['duration'])==4
  reports.append({'slide':n,'video':probe,'text_bounds_unchanged':True});print(f'{n:02}: video verified',flush=True)
 b.close()
(p/'proof/video-validation.json').write_text(json.dumps(reports,indent=2))
