from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import ImageReader
ROOT=Path(__file__).resolve().parent
OUT=ROOT/'delivery'
BEATS=[
('00:00–00:01.30','ONE CONTAINER','The exact title is present from frame one. A single blue container is the hero object; ART enters with the tablet.','00.8'),
('00:01.30–00:02.40','FIRST CALLS','ART stops to check the tablet. Numbered 3D handsets begin to land around the same container.','02.5'),
('00:02.40–00:04.60','THE CHASE GROWS','More handsets appear around the container, building a visible count without seven floating text cards.','04.3'),
('00:04.60–00:05.65','SEVEN ON ONE','The seventh handset lands. All seven calls are readable at once, visually tied to one container.','05.5'),
('00:05.65–00:06.75','ART REACTS','Only after the seventh call, the same 3D ART mascot changes into the stressed pose with a short recoil.','05.9'),
('00:06.75–00:10.00','READABLE HOLD','The original supporting copy fills the clear left margin. The title, seven handsets, one container and mascot remain visible.','09.5'),
]
W,H=1200,1340
im=Image.new('RGB',(W,H),'#041821');d=ImageDraw.Draw(im)
font=ImageFont.truetype(str(ROOT/'assets/Poppins-Bold.ttf'),42)
small=ImageFont.truetype(str(ROOT/'assets/Poppins-Regular.ttf'),17)
cap=ImageFont.truetype(str(ROOT/'assets/Poppins-Bold.ttf'),20)
d.text((46,38),'SEVEN CALLS. ONE CONTAINER.',font=font,fill='white')
d.text((46,96),'Slide 1 / 10-second motion storyboard',font=small,fill='#39e4ed')
for i,(time,title,desc,shot) in enumerate(BEATS):
 col,row=i%2,i//2;x=46+col*575;y=155+row*390
 img=Image.open(OUT/f'proof-{shot}s.jpg').convert('RGB');img.thumbnail((236,305))
 d.rounded_rectangle((x-8,y-8,x+550,y+365),radius=12,outline='#1e8091',width=2)
 im.paste(img,(x,y))
 tx=x+251
 d.text((tx,y+3),time,font=small,fill='#41e9f0')
 d.text((tx,y+48),title,font=cap,fill='white')
 import textwrap
 for n,line in enumerate(textwrap.wrap(desc,26)):
  d.text((tx,y+85+n*26),line,font=small,fill='#dce9eb')
im.save(OUT/'ART-seven-calls-slide-01-storyboard-v9.jpg',quality=92)
c=canvas.Canvas(str(OUT/'ART-seven-calls-slide-01-storyboard-v9.pdf'),pagesize=(W,H))
c.drawImage(ImageReader(im),0,0,width=W,height=H)
c.save()
print('Storyboard exported')
