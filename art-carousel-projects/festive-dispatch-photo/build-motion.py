"""Photographic motion: animate the original photograph beneath stationary live typography."""
from pathlib import Path
import shutil
p=Path(__file__).resolve().parent;m=p/'motion'
shutil.copytree(p/'slides/assets',m/'slides/assets',dirs_exist_ok=True)
# Scene-specific camera direction and focal point. Live text is a stationary sibling.
settings={1:(.010,-3,-2,73,69,560,620,1040,1100),2:(.012,3,-2,57,58,450,520,870,935),3:(.014,-4,-2,75,54,450,520,860,935),4:(.010,6,0,18,55,460,530,860,935),5:(.014,-5,-1,75,55,495,545,860,935),6:(.011,-7,1,76,56,455,520,860,935)}
for n in range(1,7):
 s=(p/f'slides/slide-{n:02d}.html').read_text();zoom,x,y,ox,oy,a,b,c,d=settings[n]
 css=f'''\n.camera-window{{position:absolute;inset:0;pointer-events:none;overflow:hidden;mask-image:linear-gradient(180deg,transparent {a}px,black {b}px,black {c}px,transparent {d}px);-webkit-mask-image:linear-gradient(180deg,transparent {a}px,black {b}px,black {c}px,transparent {d}px)}}\n.camera-window .photo{{transform-origin:{ox}% {oy}%;will-change:transform;image-rendering:auto}}\n'''
 s=s.replace('</style>',css+'</style>',1)
 js=f'''
const sourcePhoto=document.querySelector('.photo');
const maskedCover={str(n==1).lower()};
let cameraPhoto=sourcePhoto;
if(maskedCover){{const cameraWindow=document.createElement('div');cameraWindow.className='camera-window';cameraPhoto=sourcePhoto.cloneNode(true);cameraPhoto.removeAttribute('id');cameraWindow.append(cameraPhoto);sourcePhoto.after(cameraWindow);}}
else{{sourcePhoto.style.transformOrigin='{ox}% {oy}%';sourcePhoto.style.willChange='transform';}}
function cameraFrame(t){{const k=.5-.5*Math.cos(Math.PI*Math.min(1,t/4));cameraPhoto.style.transform=`translate(${{({x}*k).toFixed(4)}}px,${{({y}*k).toFixed(4)}}px) scale(${{(1+{zoom}*k).toFixed(6)}})`;}}
tl.to({{}},{{duration:4,onUpdate:()=>cameraFrame(tl.time())}},0);cameraFrame(0);
'''
 s=s.replace('render();\nwindow.__timelines',js+'\nrender();\nwindow.__timelines')
 (m/f'slides/slide-{n:02d}.html').write_text(s)
print('Six photographic camera scenes built: original textures, stationary type, no added moving illustrations')
