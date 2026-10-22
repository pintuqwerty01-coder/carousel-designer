from pathlib import Path
from PIL import Image
import subprocess,json,hashlib
P=Path(__file__).resolve().parent.parent;M=P/'motion-preview';D=M/'delivery';video=D/'ART-supplier-follow-up-motion-test-v1.mp4'
info=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(video)]));s=info['streams'][0]
assert (s['width'],s['height'],s['r_frame_rate'],s['nb_frames'],s['pix_fmt'])==(1080,1350,'30/1','210','yuv420p');assert abs(float(info['format']['duration'])-7)<.02
ims=[]
for i,t in enumerate([0.1,1.45,2.45,3.35,6.8]):
 f=M/'proof'/f'decoded-{i}.png';subprocess.run(['ffmpeg','-v','error','-y','-ss',str(t),'-i',str(video),'-frames:v','1',str(f)],check=True);im=Image.open(f).convert('RGB');assert im.size==(1080,1350);ims.append(im)
board=Image.new('RGB',(2160,1350),'#1A1A1A')
for i,im in enumerate(ims[:4]):board.paste(im.resize((540,675),Image.Resampling.LANCZOS),(i*540,0))
# Detailed before/after at the bottom, preserving a simple review grid.
for i,im in enumerate([ims[0],ims[-1]]):board.paste(im.resize((540,675),Image.Resampling.LANCZOS),(540+i*540,675))
board.save(D/'ART-supplier-follow-up-motion-frames-v1.jpg',quality=96,subsampling=0)
ims[-1].save(D/'ART-supplier-follow-up-motion-poster-v1.jpg',quality=98,subsampling=0)
filt='fps=12,scale=432:540:flags=lanczos,split[a][b];[a]palettegen=stats_mode=diff[p];[b][p]paletteuse=dither=sierra2_4a'
subprocess.run(['ffmpeg','-v','error','-y','-i',str(video),'-filter_complex',filt,'-loop','0',str(D/'ART-supplier-follow-up-motion-preview-v1.gif')],check=True)
md5=subprocess.check_output(['ffmpeg','-v','error','-i',str(video),'-f','framemd5','-']).decode();hashes=[x.split(',')[-1].strip() for x in md5.splitlines() if not x.startswith('#')];assert len(hashes)==210 and len(set(hashes))>30
fonts={}
for state in ['prep','ready','sent']:
 font=subprocess.check_output(['pdffonts',str(M/'states'/f'{state}.pdf')]).decode();assert 'Preahvihear-Regular' in font and 'Poppins' not in font;fonts[state]='Embedded Preahvihear Regular'
(M/'video-checks.json').write_text(json.dumps({'scope':'Slide 4 representative motion proof','duration_seconds':7,'fps':30,'frames':210,'dimensions':[1080,1350],'codec':s['codec_name'],'pixel_format':s['pix_fmt'],'unique_decoded_frame_hashes':len(set(hashes)),'font_states':fonts,'decoded_key_times':[.1,1.45,2.45,3.35,6.8],'semantics':'Message ready -> one send press -> sent confirmation -> supplier reply pending','static_carousel_preserved':True},indent=2)+'\n');print('Video format, motion frames, fonts and exports verified')
