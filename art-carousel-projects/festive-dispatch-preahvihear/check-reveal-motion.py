from pathlib import Path
from playwright.sync_api import sync_playwright
import json,subprocess
p=Path(__file__).resolve().parent
with sync_playwright() as w:
 b=w.chromium.launch();page=b.new_page(viewport={'width':1080,'height':1350})
 page.goto((p/'slides/slide-07.html').as_uri(),wait_until='networkidle');page.evaluate('document.fonts.ready')
 frames=[];copy=[]
 for t in [0,1,2]:
  page.evaluate('(t)=>Object.values(window.__timelines).forEach(tl=>tl.time(t,false))',t)
  points=page.evaluate('''() => {const r=document.querySelector('.brand-clock').getBoundingClientRect();return [...document.querySelectorAll('.brand-clock .hand')].map(e=>{const pt=new DOMPoint(40,40).matrixTransform(e.getScreenCTM());return {x:pt.x,y:pt.y,cx:r.x+r.width/2,cy:r.y+r.height/2};});}''')
  assert all(abs(pt['x']-pt['cx'])<.5 and abs(pt['y']-pt['cy'])<.5 for pt in points),(t,points)
  frames.append(page.screenshot(clip={'x':894,'y':54,'width':82,'height':82}))
  copy.append(page.screenshot(clip={'x':84,'y':180,'width':912,'height':670}))
  page.screenshot(path=str(p/f'proof/clock-{t}.png'),clip={'x':874,'y':34,'width':122,'height':122})
 assert frames[0]!=frames[1] and frames[1]!=frames[2]
 assert copy[0]==copy[1]==copy[2]
 errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
 page.set_content('<video id="v" controls autoplay muted src="'+(p/'render/out/slide-07.mp4').as_uri()+'"></video>')
 # Navigate to local file through runner so the video is served via HTTP.
 (p/'proof/reveal-playback.html').write_text('<video id="v" controls autoplay muted src="../render/out/slide-07.mp4"></video>')
 page.goto((p/'proof/reveal-playback.html').as_uri(),wait_until='networkidle')
 page.wait_for_function('v.readyState>=2&&v.videoWidth===1080&&v.videoHeight===1350')
 page.wait_for_timeout(500);assert page.evaluate('v.currentTime')>0;assert not errors
 b.close()
info=json.loads(subprocess.check_output(['ffprobe','-v','error','-select_streams','v:0','-show_entries','stream=width,height,r_frame_rate,nb_frames,pix_fmt,duration','-of','json',str(p/'render/out/slide-07.mp4')]))['streams'][0]
assert info['width']==1080 and info['height']==1350 and info['r_frame_rate']=='30/1' and info['nb_frames']=='120' and float(info['duration'])==4 and info['pix_fmt']=='yuv420p',info
print('Clock hands visibly sweep; all copy stationary; four-second MP4 decoded and played')
