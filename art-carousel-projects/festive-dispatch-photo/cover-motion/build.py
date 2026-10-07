from pathlib import Path
import importlib.util
p=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('kit','/workspace/art-carousel-kit/scripts/build.py');b=importlib.util.module_from_spec(spec);spec.loader.exec_module(b)
css='''
.photo,.clear{position:absolute;inset:0;width:1080px;height:1350px;object-fit:fill}.clear{clip-path:polygon(600px 690px,1080px 690px,1080px 1105px,600px 1105px)}
#mascot{position:absolute;left:367px;top:294px;width:640px;height:799px;transform-origin:72% 96%;image-rendering:auto;clip-path:polygon(35% 50%,100% 50%,100% 100%,35% 100%)}.handle,.count,#trail{display:none}
'''
inner='<img class="photo" src="assets/approved-cover.png"><img class="clear" src="assets/cover-clear.png"><img id="mascot" src="assets/cover-mascot.png">'
js="""
document.fonts.load('40px Preahvihear');document.fonts.load('600 40px Poppins');
const group=document.getElementById('mascot');
tl.to({}, {duration:4,onUpdate:()=>{const t=tl.time();const S=Math.floor(t*8)/8;const envelope=Math.min(1,S/.4)*Math.max(0,Math.min(1,(3.25-S)/.7));const sway=Math.sin(S*4.2)*envelope;group.style.transform=`translate(${Math.round(sway*3)}px,${Math.round(-Math.abs(sway)*4)}px) rotate(${sway*1.8}deg)`;}},0);
"""
(p/'slides/slide-01.html').write_text(b.page('matching-cover-01','dark',inner,css,None,'scene',js,1,9,'@arealtimetech',True,b.LIB,{}))
