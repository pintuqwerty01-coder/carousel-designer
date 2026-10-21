"""Integrated photographic scenes, with canonical Style 1 typography."""
import html,json,pathlib,shutil
P=pathlib.Path(__file__).resolve().parent
K=P.parents[1]/'art-carousel-kit'
C=json.loads((P/'content.json').read_text())
def inr(amount):
 digits=str(amount);tail=digits[-3:];head=digits[:-3];groups=[]
 while head:groups.insert(0,head[-2:]);head=head[:-2]
 return ','.join(groups+[tail])
A=P/'slides'/'assets';A.mkdir(parents=True,exist_ok=True)
shutil.copytree(K/'assets'/'kit',A,dirs_exist_ok=True)
photos={
 'aisle.png':P.parent/'festive-dispatch-realistic/slides/assets/cover-art.png',
 'records.png':P.parent/'festive-dispatch-photo/slides/assets/clean-02.png',
 'shelves.png':P.parent/'festive-dispatch-photo/slides/assets/clean-04.png',
 'incoming.png':P.parent/'festive-dispatch-photo/slides/assets/clean-06.png',
 'review.png':P.parent/'festive-dispatch-photo/slides/assets/clean-03.png',
 'controls.png':P.parent/'festive-dispatch-photo/slides/assets/clean-05.png',
}
for name,source in photos.items():shutil.copy2(source,A/name)
photo_order=['aisle.png','controls.png','records.png','shelves.png','incoming.png','records.png','review.png','incoming.png','controls.png']
logo=(P/'brand/art-original-style2.svg').read_text().replace('</defs>', '<style>path[transform^="matrix(1,0,0,-1,250.92774"] {fill:#1A1A1A;}</style></defs>',1)
lib='\n'.join((K/'assets'/'kit'/'js'/name).read_text() for name in ['pixelbot.js','props-vector.js','scenes-library.js'])+'\n'+(P/'scenes.js').read_text()
css=(K/'assets'/'shared.css').read_text()+'''
html,body {background:#101519;} #root {position:relative;width:1080px;height:1350px;overflow:hidden;}
.slide {background:#101519;color:white;} * {font-synthesis:none;}
.backdrop,.shade {position:absolute;inset:0;width:1080px;height:1350px;}
.backdrop {z-index:0;} .backdrop img {width:100%;height:100%;object-fit:cover;display:block;}
.shade {z-index:1;background:linear-gradient(180deg,rgba(4,12,15,.72) 0%,rgba(4,12,15,.64) 28%,rgba(4,12,15,.34) 50%,rgba(4,12,15,.18) 74%,rgba(4,12,15,.42) 100%);}
.topline {position:absolute;left:84px;right:84px;top:78px;z-index:4;display:flex;align-items:center;gap:17px;font:600 23px/1 Poppins;letter-spacing:3px;}
.brand-dot {width:11px;height:11px;background:#04ADC3;border-radius:50%;}.topline .rule {height:1px;background:rgba(255,255,255,.3);flex:1;margin-left:20px;}
.col {position:absolute;top:156px;left:84px;right:84px;z-index:4;display:flex;flex-direction:column;gap:26px;}
.headline {font:400 86px/1.22 Preahvihear,Poppins,sans-serif;letter-spacing:-.01em;color:white;text-shadow:0 2px 18px rgba(0,0,0,.2);}
.accent {color:#04ADC3;} .body {font:500 32px/1.45 Poppins;color:#F3F6F7;max-width:870px;}
/* Optical hierarchy: one left edge, one copy rhythm, deliberate line breaks. */
.col {top:168px;gap:28px;}
.headline {font-size:80px;line-height:1.2;letter-spacing:-.015em;}
.body {font-size:34px;line-height:1.5;max-width:880px;text-wrap:pretty;}
.s1 .headline,.s5 .headline,.s8 .headline,.s9 .headline {font-size:80px;}
.s8 .col,.s9 .col {text-align:left;align-items:flex-start;}
.edge-fade {position:absolute;inset:0;z-index:3;pointer-events:none;
 background:radial-gradient(ellipse at center,rgba(0,0,0,0) 55%,rgba(0,0,0,.06) 82%,rgba(0,0,0,.12) 100%);}
.closing-brand {position:absolute;left:84px;top:84px;width:200px;height:80px;z-index:4;background:transparent;}
.closing-brand svg {display:block;width:200px;height:auto;}
.s9 .topline {display:none;}.s9 .col {top:244px;gap:24px;}
.s9 .headline {color:#1A1A1A;font-size:80px;line-height:1.2;text-shadow:none;}
.s9 .body {color:#1A1A1A;}
.s9 .shade {background:linear-gradient(180deg,rgba(255,255,255,.96) 0%,rgba(255,255,255,.90) 35%,rgba(255,255,255,.60) 45%,rgba(255,255,255,.04) 67%,rgba(4,12,15,.12) 78%,rgba(4,12,15,.50) 100%);}
.closing-cta {position:absolute;left:84px;right:84px;top:1035px;z-index:4;text-align:center;font:700 58px/1.2 Poppins;color:white;text-shadow:0 2px 10px rgba(0,0,0,.5);}
.approval-state {position:absolute;top:1135px;left:84px;right:84px;z-index:4;text-align:center;font:600 44px/1.2 Poppins;color:#FFD166;text-shadow:0 2px 10px #101519;visibility:hidden;}
.stage {position:absolute;inset:0;z-index:2;pointer-events:none;background:transparent;} #scene {display:block;width:1080px;height:1350px;}
.handle {position:absolute;left:84px;bottom:92px;z-index:4;font:500 23px/1 Poppins;letter-spacing:.02em;color:#F0F4F5;text-shadow:0 1px 4px black;}
.count {position:absolute;right:84px;bottom:92px;z-index:4;font:500 23px/1 Poppins;letter-spacing:3px;color:#F0F4F5;}
#trail {position:absolute;left:0;bottom:0;width:1080px;height:80px;z-index:5;}
.has-panels .body {display:none;}.example-limit {position:absolute;top:440px;left:84px;width:912px;z-index:4;font:500 30px/1.4 Poppins;color:white;display:flex;align-items:center;gap:12px;}
.example-limit:before {content:'';width:7px;height:42px;background:#04ADC3;border-radius:4px;margin-right:10px;}.example-limit strong {font-weight:600;}
.panels {position:absolute;top:530px;left:84px;width:912px;display:grid;grid-template-columns:1fr 1fr;gap:26px;z-index:4;}
.panel {border-radius:20px;background:rgba(255,255,255,.97);padding:26px 28px;height:280px;color:#1A1A1A;box-shadow:0 8px 24px rgba(0,0,0,.10);border-top:5px solid #04ADC3;}
.panel:last-child {border-top-color:#FFD166;}.panel h2 {font:500 28px/1.4 Poppins;letter-spacing:-.2px;}
.amount {font:600 56px/1.2 Poppins;font-variant-numeric:tabular-nums;letter-spacing:-1px;margin-top:15px;}
.panel p {font:400 30px/1.4 Poppins;margin-top:15px;}
'''
headlines=[
 'Your shelves called.<br><span class="accent">ART’s already on it.</span>',
 'Low stock.<br><span class="accent">Next order, handled.</span>',
 'Stop chasing<br><span class="accent">stock.</span>',
 'ART spots what’s<br><span class="accent">running low.</span>',
 'Check first. Reorder<br><span class="accent">what’s needed.</span>',
 'Your limit.<br><span class="accent">Two clear paths.</span>',
 'An exception<br>needs <span class="accent">your call.</span>',
 'Routine orders move.<br><span class="accent">Exceptions reach you.</span>',
 'Stock handled.<br><span class="accent">Time handed back.</span>'
]
for i,s in enumerate(C['slides'],1):
 sid=f'slide-{i:02d}';panels=''
 if i==6:
  ex=C['threshold_example'];panels='<div class="example-limit">Example approval limit: <strong>₹'+inr(ex['approval_limit'])+'</strong></div>'
  panels+='<div class="panels">'+''.join('<section class="panel"><h2>'+html.escape(p['headline'])+'</h2><div class="amount">₹'+inr(ex['automatic_order'] if j==0 else ex['approval_required_order'])+'</div><p>'+html.escape(p['body'])+'</p></section>' for j,p in enumerate(s['panels']))+'</div>'
 body='<br>'.join(html.escape(x) for x in s.get('body',[]))
 closing='<div class="closing-brand">'+logo+'</div><p class="closing-cta">Put ART to work.</p>' if i==9 else ''
 status='<p class="approval-state">Awaiting approval</p>' if i==7 else ''
 doc=f'''<!doctype html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=1080,height=1350"><script src="assets/gsap.min.js"></script><style>{css}</style></head><body>
 <div id="root" data-composition-id="{sid}" data-start="0" data-duration="{s['duration']}" data-width="1080" data-height="1350" data-fps="30"><div class="clip slide s{i} {'has-panels' if i==6 else ''}" data-start="0" data-duration="{s['duration']}">
 <div class="backdrop"><img src="assets/{photo_order[i-1]}" alt="Photorealistic stockroom scene"></div><div class="shade"></div><div class="edge-fade"></div>
 <div class="topline"><span class="brand-dot"></span>{html.escape(C['brand_full_name']) if i in (1,9) else 'ART'}<span class="rule"></span></div>
 <div class="col"><h1 class="headline">{headlines[i-1]}</h1><p class="body">{body}</p></div>{panels}{closing}{status}
 <div class="stage"><canvas id="scene" width="1080" height="1350"></canvas></div>
 <div class="handle">@arealtimetech</div><div class="count">{i:02d} / 09</div><canvas id="trail" width="1080" height="80"></canvas></div></div>
 <script>{lib}
 const st={{t:0}},c=document.getElementById('scene').getContext('2d'),tr=document.getElementById('trail').getContext('2d');
 function render(){{c.clearRect(0,0,1080,1350);SCENES[{i}](c,st.t*4/{s['duration']},Math.floor(st.t*8));tr.clearRect(0,0,1080,80);const approval=document.querySelector('.approval-state');if(approval)approval.style.visibility=st.t>=3.2?'visible':'hidden';for(let j=0;j<9;j++){{tr.fillStyle=j<{i}?'#04ADC3':'rgba(255,255,255,.18)';tr.fillRect(84+j*103,39,88,3);}}}}
 const tl=gsap.timeline({{paused:true}});tl.to(st,{{t:{s['duration']},duration:{s['duration']},ease:'none',onUpdate:render}},0);window.__timelines={{'{sid}':tl}};render();
 </script></body></html>'''
 (P/'slides'/f'{sid}.html').write_text(doc);print('built',sid)
