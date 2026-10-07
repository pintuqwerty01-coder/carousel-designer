import pathlib,importlib.util,json
p=pathlib.Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('kit','/workspace/art-carousel-kit/scripts/build.py');b=importlib.util.module_from_spec(spec);spec.loader.exec_module(b)
source=json.loads(pathlib.Path('/workspace/art-carousel-projects/festive-dispatch/content.json').read_text())
(p/'content.json').write_text(json.dumps({**source,'slides':[s for s in source['slides'] if s['number'] in [1,3]]},indent=2))
lib=b.LIB+'''\nObject.assign(SCENES_DYN,{realCover(c,t,S){
const x=700,y=790,u=10;
const lean=S<12?((S%4<2)?-0.025:0.025):0;
c.save();c.translate(x+120,y+230);c.rotate(lean);c.translate(-x-120,-y-230);
vShadow(c,x+120,y+240,170,0,true);
drawBot(c,x,y,u,{legs:'stand',armL:'out',armR:'reach',eyes:S<12?'wide':S<23?'focus':'happy',mouth:S<12?'wobble':S<23?'flat':'smile',bulb:S<12?'red':S<23?'yellow':'aqua',dark:true,halo:true});
function box(bx,by){c.fillStyle='#CBA575';c.strokeStyle='#1A1A1A';c.lineWidth=2.5;c.beginPath();c.roundRect(bx,by,64,58,4);c.fill();c.stroke();c.fillStyle='#E7D0AB';c.fillRect(bx+26,by+1,12,55);}
box(x-38,y+144);box(x+206,y+144);
c.restore();if(S<12)vSweat(c,x+172,y+54,t,.7);
}});'''
css='''
.art{position:absolute;inset:0;overflow:hidden}.art img{width:1080px;height:1350px;object-fit:cover;transform-origin:60% 60%}
.shade{position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.35),rgba(0,0,0,.15) 42%,transparent 65%,rgba(0,0,0,.25))}
#scene{position:absolute;inset:0;z-index:10}.cv-col{top:90px;gap:20px;z-index:20}.cv-h{font-size:87px;line-height:1.08;color:white}.cv-h em{color:#04ADC3;font-style:normal}.cv-sub{font:500 35px/1.4 Poppins;color:white}
.cv-swipe{position:absolute;left:84px;top:1108px;z-index:30;background:#04ADC3;color:#1A1A1A;border-radius:999px;padding:20px 28px;font:600 27px/1.2 Poppins;display:flex;gap:12px}
'''
inner='''<div class="art"><img id="artimg" src="assets/cover-art.png"></div><div class="shade"></div><canvas id="scene" width="1080" height="1350"></canvas><div class="col cv-col"><div class="h-display cv-h">Festive season<br>orders are coming.<br>Can your<br><em>dispatch keep up?</em></div><div class="cv-sub">Diwali orders don't wait for anyone.</div></div><div class="cv-swipe">Swipe to see where the rush usually breaks <span id="arr">→</span></div>'''
js='''tl.fromTo('#artimg',{scale:1},{scale:1.05,duration:4,ease:'none'},0);tl.to('#arr',{x:8,duration:.3,yoyo:true,repeat:3,ease:'sine.inOut'},2.6);'''
(p/'slides/slide-01.html').write_text(b.page('realistic-01','dark',inner,css,'realCover','scene',js,1,9,'@arealtimetech',True,lib,{}))
