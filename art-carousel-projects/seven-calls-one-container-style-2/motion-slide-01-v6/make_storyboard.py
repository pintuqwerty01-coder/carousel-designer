from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import ImageReader
ROOT=Path(__file__).resolve().parent
OUT=ROOT/'delivery'
BEATS=[
('00:00–00:01.35','ESTABLISH','Title and suspended container are visible from frame one. ART takes two clear steps in from the left with the tablet.','00.7'),
('00:01.35–00:01.85','CHECK','ART stops under the container and looks down at the tablet. The scene gets a short breath before calls begin.','01.5'),
('00:01.85–00:03.40','FIRST UPDATES','Booking, Packing List and Pickup arrive in order. Each card repeats the same blue container thumbnail; the container marker pulses on arrival.','02.4'),
('00:03.40–00:05.55','PILEUP','Delay Update, Truck Timing, Loading Window and Customs Check fill the two sides. ART stays planted, checking the tablet.','05.4'),
('00:05.55–00:06.80','REACTION','On the seventh call, ART compresses, recoils and changes to the stressed 3D pose. The cards clear into seven call symbols around the same container.','05.8'),
('00:06.80–00:10.00','COVER HOLD','The supporting copy appears and holds. Title, one container, seven calls and ART remain legible through the last frame.','09.5'),
]
W,H=1200,1340
im=Image.new('RGB',(W,H),'#041821');d=ImageDraw.Draw(im)
font=ImageFont.truetype(str(ROOT/'assets/Poppins-Bold.ttf'),42)
small=ImageFont.truetype(str(ROOT/'assets/Poppins-Regular.ttf'),17)
cap=ImageFont.truetype(str(ROOT/'assets/Poppins-Bold.ttf'),20)
d.text((46,38),'ONE CONTAINER. SEVEN CALLS.',font=font,fill='white')
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
im.save(OUT/'ART-seven-calls-slide-01-storyboard-v6.jpg',quality=92)
c=canvas.Canvas(str(OUT/'ART-seven-calls-slide-01-storyboard-v6.pdf'),pagesize=(W,H))
c.drawImage(ImageReader(im),0,0,width=W,height=H)
c.save()
print('Storyboard exported')
