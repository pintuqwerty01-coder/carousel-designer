from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import ImageReader
ROOT=Path(__file__).resolve().parent
OUT=ROOT/'delivery'
BEATS=[
('00:00–00:01.35','ENTER','The title is visible immediately. One container waits outside the port operations room as ART enters holding the tablet.','00.7'),
('00:01.35–00:01.80','NOTICE','ART stops and checks the tablet. The wall is clear before the inbound call log appears.','01.5'),
('00:01.80–00:03.40','START OF THE CHASE','Booking, Packing List and Pickup populate one shared call log. Each arrival briefly marks the container visible through the window.','02.4'),
('00:03.40–00:05.55','SEVEN CALLS','Delay Update, Truck Timing, Loading Window and Customs Check complete the log. The count reaches 07 / 07.','05.4'),
('00:05.55–00:06.80','PRESSURE','ART recoils into the existing stressed 3D pose only when the seventh call lands. The log clears for the message.','05.8'),
('00:06.80–00:10.00','COVER HOLD','The exact supporting copy appears. The title, ART and the one container remain in frame for the final readable hold.','09.5'),
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
im.save(OUT/'ART-seven-calls-slide-01-storyboard-v8.jpg',quality=92)
c=canvas.Canvas(str(OUT/'ART-seven-calls-slide-01-storyboard-v8.pdf'),pagesize=(W,H))
c.drawImage(ImageReader(im),0,0,width=W,height=H)
c.save()
print('Storyboard exported')
