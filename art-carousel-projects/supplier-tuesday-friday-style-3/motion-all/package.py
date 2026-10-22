from pathlib import Path
import subprocess,json,hashlib,zipfile
from PIL import Image,ImageDraw
M=Path(__file__).resolve().parent;D=M/'delivery';P=M.parent
checks=[];sheet=Image.new('RGB',(1080,2*365),'#eee');draw=ImageDraw.Draw(sheet)
for n in range(1,9):
 v=D/f'ART-supplier-delay-slide-{n:02}.mp4';j=json.loads(subprocess.check_output(['ffprobe','-v','error','-count_frames','-show_streams','-of','json',str(v)]));s=j['streams'][0];assert(s['width'],s['height'],s['r_frame_rate'],int(s['nb_read_frames']))==(1080,1350,'30/1',210)
 hashes=subprocess.check_output(['ffmpeg','-v','error','-i',str(v),'-f','framemd5','-']).decode();unique=len(set(l.split(',')[-1].strip() for l in hashes.splitlines() if not l.startswith('#')));assert unique>30
 for t in [0,1.8,6.8]:subprocess.run(['ffmpeg','-v','error','-y','-ss',str(t),'-i',str(v),'-frames:v','1',str(M/f'proof/decoded-{n:02}-{t}.jpg')],check=True)
 im=Image.open(M/f'proof/decoded-{n:02}-6.8.jpg').resize((270,338));x=(n-1)%4*270;y=(n-1)//4*365;sheet.paste(im,(x,y+25));draw.text((x+10,y+5),f'Slide {n}',fill='black');checks.append(dict(slide=n,width=1080,height=1350,fps=30,frames=210,duration=7,distinct_decoded_frames=unique))
sheet.save(D/'ART-supplier-delay-overview.jpg',quality=95)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(D/'ART-supplier-delay-approved-static.pdf')==sha(P/'delivery-v6/ART-supplier-delay-style3-full-v6.pdf')
assert sha(D/'ART-supplier-delay-slide-04.mp4')==sha(P/'motion-preview/delivery/ART-supplier-follow-up-motion-test-v1.mp4')
(M/'video-checks.json').write_text(json.dumps(checks,indent=2))
concat=M/'concat.txt';concat.write_text(''.join(f"file '{(D/f'ART-supplier-delay-slide-{n:02}.mp4').resolve()}'\n" for n in range(1,9)))
subprocess.run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',str(concat),'-c','copy','-movflags','+faststart',str(D/'ART-supplier-delay-full-motion-v1.mp4')],check=True);concat.unlink()
with zipfile.ZipFile(D/'ART-supplier-delay-all-slides-and-approved-PDF.zip','w',compression=zipfile.ZIP_DEFLATED) as z:
 for n in range(1,9):
  v=D/f'ART-supplier-delay-slide-{n:02}.mp4';z.write(v,v.name)
 for name in ['ART-supplier-delay-approved-static.pdf','ART-supplier-delay-overview.jpg']:z.write(D/name,name)
print(json.dumps(checks),flush=True)
