from pathlib import Path
import subprocess,json
from PIL import Image,ImageChops
p=Path(__file__).resolve().parent;m=p/'motion';(m/'proof').mkdir(exist_ok=True)
for n in range(1,7):
 f=m/f'render/out/slide-{n:02d}.mp4';meta=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_entries','stream=codec_name,profile,pix_fmt,width,height,r_frame_rate,nb_frames:format=duration','-of','json',str(f)]));s=meta['streams'][0]
 assert (s['codec_name'],s['profile'],s['pix_fmt'],s['width'],s['height'],s['r_frame_rate'],s['nb_frames'])==('h264','High','yuv420p',1080,1350,'30/1','120'),meta
 assert float(meta['format']['duration'])==4
 for name,t in [('first',.1),('action',1.7),('last',3.9)]:
  subprocess.run(['ffmpeg','-v','error','-y','-ss',str(t),'-i',str(f),'-frames:v','1',str(m/f'proof/{n:02d}-{name}.png')],check=True)
 a=Image.open(m/f'proof/{n:02d}-first.png').convert('RGB');b=Image.open(m/f'proof/{n:02d}-last.png').convert('RGB')
 # Encoding can produce tiny quantisation differences; count material changes.
 d=ImageChops.difference(a.crop((84,40,996,440)),b.crop((84,40,996,440))).convert('L');changed=d.point(lambda v:255 if v>40 else 0).histogram()[255]
 assert changed==0,(n,changed)
 print(f'{n:02}: 1080x1350, 30fps, 4s, 120 frames, H264 High/yuv420p; headline changes >40 = {changed}',flush=True)
