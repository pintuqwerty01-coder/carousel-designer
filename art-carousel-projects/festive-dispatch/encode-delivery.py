"""Convert rendered masters to browser-compatible delivery MP4s, then verify."""
import json,pathlib,subprocess
project=pathlib.Path(__file__).resolve().parent
files=sorted((project/'render/out').glob('slide-??.mp4'))
if not files:raise SystemExit('No rendered slides found')
for f in files:
 tmp=f.with_name(f.stem+'-delivery.mp4')
 subprocess.run(['ffmpeg','-v','error','-y','-i',str(f),'-c:v','libx264','-profile:v','high','-pix_fmt','yuv420p','-crf','16','-preset','fast','-movflags','+faststart','-an',str(tmp)],check=True)
 meta=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_entries','stream=codec_name,profile,pix_fmt,width,height,r_frame_rate:format=duration','-of','json',str(tmp)]))
 s=meta['streams'][0]
 assert (s['codec_name'],s['profile'],s['pix_fmt'],s['width'],s['height'],s['r_frame_rate'])==('h264','High','yuv420p',1080,1350,'30/1'),meta
 assert meta['format']['duration']=='4.000000',meta
 tmp.replace(f)
 print(f.name,'delivery format verified')
