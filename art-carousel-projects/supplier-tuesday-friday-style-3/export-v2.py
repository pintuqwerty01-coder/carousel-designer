from pathlib import Path
from PIL import Image
import zipfile
P=Path(__file__).resolve().parent;D=P/'delivery-v2';D.mkdir(exist_ok=True)
ims=[]
for n in [1,4]:
 im=Image.open(P/'stills'/f'slide-{n:02}.png').convert('RGB');assert im.size==(1080,1350);ims.append(im)
 im.save(D/f'ART-supplier-delay-slide-{n:02}-v2.jpg',quality=98,subsampling=0)
ims[0].save(D/'ART-supplier-delay-style3-proof-v2.pdf',save_all=True,append_images=ims[1:],resolution=72,quality=100,subsampling=0)
board=Image.new('RGB',(2160,1350));board.paste(ims[0],(0,0));board.paste(ims[1],(1080,0));board.save(D/'ART-supplier-delay-proof-overview-v2.jpg',quality=95,subsampling=0)
with zipfile.ZipFile(D/'ART-supplier-delay-proof-v2.zip','w',zipfile.ZIP_DEFLATED) as z:
 for f in sorted(D.iterdir()):
  if f.suffix in ['.jpg','.pdf']:z.write(f,f.name)
