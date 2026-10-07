"""Replace baked 3D mascots with reconstructed photo plates and articulated original 2D ART bot."""
from pathlib import Path
import shutil
p=Path(__file__).resolve().parent;js=(p/'actors-2d.js').read_text()
for n in range(1,7):
 shutil.copy2(p/f'artwork/clean-{n:02d}.png',p/f'slides/assets/clean-{n:02d}.png')
 f=p/f'slides/slide-{n:02d}.html';s=f.read_text()
 if 'id="hero-2d"' in s:continue
 s=s.replace(f'assets/art-{n:02d}.png',f'assets/clean-{n:02d}.png').replace('assets/approved-cover.png','assets/clean-01.png')
 css='\n#hero-2d{position:absolute;inset:0;width:1080px;height:1350px;z-index:5;image-rendering:auto;pointer-events:none}\n'
 if n==1:css+=' .cover-lettering{position:absolute;inset:0;width:1080px;height:1350px;object-fit:cover;mask-image:linear-gradient(180deg,black 560px,transparent 590px,transparent 1085px,black 1110px);z-index:1}'
 s=s.replace('</style>',css+'</style>',1)
 if n==1:s=s.replace('<div class="handle">','<img class="cover-lettering" src="assets/approved-cover.png"><div class="handle">',1)
 s=s.replace('<div class="handle">','<canvas id="hero-2d" width="1080" height="1350"></canvas><div class="handle">',1)
 s=s.replace('render();\nwindow.__timelines',js+f'\ntl.to({{}},{{duration:4,onUpdate:()=>renderArtActors({n},tl.time())}},0);renderArtActors({n},0);\nrender();\nwindow.__timelines')
 f.write_text(s)
# Preserve closing layouts, palette and copy, with the same flat mascot identity.
for n in (7,8,9):
 f=p/f'slides/slide-{n:02d}.html';s=f.read_text()
 if 'closing-flat' in s:continue
 s=s.replace('render();\nwindow.__timelines',f'''
const closingHolder=document.querySelector('.mascot');closingHolder.innerHTML='<canvas id="closing-flat" width="330" height="280" style="width:330px;height:280px;image-rendering:auto"></canvas>';
const cc=document.getElementById('closing-flat').getContext('2d');
drawBot(cc,{5 if n in (7,8) else 40},{25 if n==7 else 35},10,{{dark:{str(n!=8).lower()},halo:true,eyes:'happy',mouth:'smile',bulb:'aqua',armL:'down',armR:'{ "wave1" if n==7 else "hold" if n==8 else "reach" }',flip:{str(n==9).lower()}}});
{ "vMug(cc,190,204,0);" if n==8 else "" }
render();\nwindow.__timelines''')
 f.write_text(s)
print('Six articulated 2D scenes built; closing layouts retained with flat mascot')
