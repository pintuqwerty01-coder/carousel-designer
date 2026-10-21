"""Render variable-duration compositions and verify every native master."""
import json,pathlib,shutil,subprocess,os
P=pathlib.Path(__file__).resolve().parent
K=P.parents[1]/'art-carousel-kit'
r=P/'render';(r/'out').mkdir(parents=True,exist_ok=True)
for f in ['package.json','hyperframes.json']:shutil.copyfile(K/'assets/render'/f,r/f)
shutil.copytree(P/'slides/assets',r/'assets',dirs_exist_ok=True)
(r/'meta.json').write_text(json.dumps({'id':P.name,'name':P.name}))
env=dict(os.environ,npm_config_cache='/workspace/art-carousel-npm-cache',HYPERFRAMES_BROWSER_PATH='/usr/bin/chromium')
for n,s in enumerate(json.loads((P/'content.json').read_text())['slides'],1):
 shutil.copyfile(P/'slides'/f'slide-{n:02}.html',r/'index.html')
 for args in [['lint'],['render','--quality','delivery','--fps','30','--crf','0','--output',f'out/slide-{n:02}.mp4']]:
  result=subprocess.run(['npx','--yes','hyperframes@0.8.55']+args,cwd=r,env=env,capture_output=True,text=True)
  if result.returncode:raise RuntimeError(result.stdout+result.stderr)
 video=r/'out'/f'slide-{n:02}.mp4'
 info=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(video)]));v=info['streams'][0]
 assert (v['width'],v['height'],int(v['nb_frames']))==(1080,1350,s['duration']*30)
 assert float(info['format']['duration'])==s['duration']
 print(f"Slide {n:02}: lint passed; 1080x1350, 30fps, {s['duration']}s",flush=True)
