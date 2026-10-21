"""Build the first Style 1 motion studies from approved copy, without changing it."""
import json, pathlib, shutil, html

P=pathlib.Path(__file__).resolve().parent
K=P.parents[1]/'art-carousel-kit'
C=json.loads((P/'content.json').read_text())
A=P/'slides'/'assets'
A.mkdir(parents=True,exist_ok=True)
shutil.copytree(K/'assets'/'kit',A,dirs_exist_ok=True)
lib='\n'.join((K/'assets'/'kit'/'js'/f).read_text() for f in ['pixelbot.js','props-vector.js','scenes-library.js'])
lib+='\n'+(P/'scenes.js').read_text()
css=(K/'assets'/'shared.css').read_text()+'''
body {background:white;} #root {position:relative;width:1080px;height:1350px;overflow:hidden;}
.slide {background:white;} .topline {position:absolute;top:80px;left:84px;right:84px;display:flex;align-items:center;gap:17px;font:600 21px Poppins;letter-spacing:3px;}
.marker {width:12px;height:12px;background:#04ADC3;border-radius:50%;} .topline .rule {height:2px;background:#DDF3F7;flex:1;margin-left:20px;}
.col {top:152px;gap:32px;} h1 {font:400 88px/1.24 Preahvihear;letter-spacing:-2px;} .hl {background:linear-gradient(transparent 61%,#9BE3EC 61%,#9BE3EC 94%,transparent 94%);box-decoration-break:clone;}
.body {font:400 36px/1.55 Poppins;color:#4B5052;} .stage {position:absolute;left:84px;top:620px;width:912px;height:520px;background:#F3F9FA;border:2px solid #DCECEF;border-radius:32px;overflow:hidden;}
#scene {position:absolute;inset:0;width:912px;height:520px;} .stage:before {content:'';position:absolute;left:0;right:0;bottom:0;height:62px;background:#E6F0F1;}
.handle {bottom:92px;font-size:23px;color:#747E81;} .count {position:absolute;right:84px;bottom:92px;font:500 23px Poppins;letter-spacing:3px;color:#747E81;}
#trail {position:absolute;bottom:0;left:0;width:1080px;height:80px;}
.branch h1 {font-size:84px;} .panels {position:absolute;left:84px;top:510px;width:912px;display:grid;grid-template-columns:1fr 1fr;gap:24px;}
.panel {height:638px;border:2px solid #BBDDE2;background:#F0F9FA;border-radius:28px;padding:30px 27px;} .panel:last-child {background:#FFF9EC;border-color:#EADCB9;}
.panel h2 {font:600 33px/1.35 Poppins;letter-spacing:-.4px;} .panel p {font:400 28px/1.45 Poppins;margin-top:18px;max-width:365px;}
.branch .stage {top:690px;height:458px;border:0;background:transparent;border-radius:0;}
.branch .stage:before {display:none;} .branch #scene {height:500px;width:912px;} .branch .body {display:none;}
.cover {background:#1A1A1A;color:white;} .cover .topline {color:white;} .cover h1 {font-size:92px;line-height:1.22;} .cover .hl {background:none;color:#04ADC3;} .cover .body {color:#D7DDDF;font-size:34px;}
.cover .stage {background:#263235;border-color:#35464B;top:650px;height:500px;} .cover .stage:before {background:#334147;} .cover .handle,.cover .count {color:#BCC8CB;}
'''
for i,key,title in [(1,'hero','Low stock.<br>Next order,<br><span class="hl">handled.</span>'),(2,'chasing','Stop chasing<br><span class="hl">stock.</span>'),(5,'paths','Your limit.<br><span class="hl">Two clear paths.</span>')]:
    s=C['slides'][i-1];sid=f'slide-{i:02d}'
    body='<br>'.join(html.escape(x) for x in s.get('body',[]))
    panels=''
    if i==5:
        panels='<div class="panels">'+''.join('<section class="panel"><h2>'+html.escape(p['headline']).replace('amount limit','amount limit')+'</h2><p>'+html.escape(p['body'])+'</p></section>' for p in s['panels'])+'</div>'
    doc=f'''<!doctype html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=1080,height=1350"><script src="assets/gsap.min.js"></script><style>{css}</style></head>
<body><div id="root" data-composition-id="{sid}" data-start="0" data-duration="4" data-width="1080" data-height="1350" data-fps="30"><div class="clip slide {'branch' if i==5 else 'cover' if i==1 else ''}" data-start="0" data-duration="4">
<div class="topline"><span class="marker"></span>ART<span class="rule"></span></div>
<div class="col"><h1>{title}</h1><p class="body">{body}</p></div>{panels}
<div class="stage"><canvas id="scene" width="912" height="520"></canvas></div>
<div class="handle">@arealtimetech</div><div class="count">{i:02d} / 08</div><canvas id="trail" width="1080" height="80"></canvas></div></div>
<script>{lib}
const st={{t:0}},c=document.getElementById('scene').getContext('2d'),tr=document.getElementById('trail').getContext('2d');
function render(){{c.clearRect(0,0,912,520);{key}(c,st.t,Math.min(31,Math.floor(st.t*8)));tr.clearRect(0,0,1080,80);tr.save();tr.translate(0,26);drawTrail(tr,1080,{i},8,eOut(st.t/.8),false,false);tr.restore();}}
const tl=gsap.timeline({{paused:true}});tl.to(st,{{t:4,duration:4,ease:'none',onUpdate:render}},0);window.__timelines={{'{sid}':tl}};render();
</script></body></html>'''
    (P/'slides'/f'{sid}.html').write_text(doc)
    print('built',sid)
