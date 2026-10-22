from pathlib import Path
from PIL import Image
import zipfile,json,shutil
P=Path(__file__).resolve().parent;D=P/'delivery-v5';D.mkdir(exist_ok=True)
ims=[]
for n in range(1,9):
 im=Image.open(P/'stills'/f'slide-{n:02}.png').convert('RGB');assert im.size==(1080,1350);ims.append(im)
 im.save(D/f'ART-supplier-delay-slide-{n:02}-v5.jpg',quality=98,subsampling=0)
import subprocess
subprocess.run(['pdfunite']+[str(P/'print-pages'/f'slide-{n:02}.pdf') for n in range(1,9)]+[str(D/'ART-supplier-delay-style3-full-v5.pdf')],check=True)
board=Image.new('RGB',(2160,1350),'#1A1A1A')
for i,im in enumerate(ims):board.paste(im.resize((540,675),Image.Resampling.LANCZOS),((i%4)*540,(i//4)*675))
board.save(D/'ART-supplier-delay-overview-v5.jpg',quality=96,subsampling=0)
with zipfile.ZipFile(D/'ART-supplier-delay-full-v5.zip','w',zipfile.ZIP_DEFLATED) as z:
 for f in sorted(D.iterdir()):
  if f.suffix in ['.jpg','.pdf']:z.write(f,f.name)
 for n in range(1,9):z.write(P/'stills'/f'slide-{n:02}.png',f'PNG/slide-{n:02}.png')
