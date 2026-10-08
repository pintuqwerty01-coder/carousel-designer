from pathlib import Path
import json,shutil,importlib.util,re
p=Path(__file__).resolve().parent;root=p.parent
(p/'images/cut').mkdir(parents=True,exist_ok=True)
assets={'pickup':'exec-247d0e73-0e49-4227-a835-0a0b3d879651.png','transit':'exec-9cd9368b-728a-4078-a438-baa91ed9c85c.png','arrival':'exec-dce08835-e567-4384-95b8-64ceb9206950.png','update':'exec-ae193aa5-d24b-4328-b484-8789acd4e221.png'}
# Generated assets are retained in images/cut; rebuilding never changes them.
c=json.loads((root/'content.json').read_text());c['objects']=[]
for i in range(2,6):
 s=c['slides'][i];s.update(x=64,y=175,w=900);s['ghost']={'side':'right','offset':-20,'top':440};s.pop('blob',None)
 if i==2:s.update(x=200,w=820)
 if i==3:s['blob']=[-80,80,1200,730]
 if i==4:s['giant']='ARRIVAL'
c['slides'][1].update(x=64,y=180,w=820)
c['slides'][6].update(body_top=670,line_top=1060,sign_top=1150)
c['slides'][7].update(x=64,y=170,w=920,hd_size=62)
for id,slide,x,y,w in [('pickup',3,330,790,820),('transit',4,200,795,950),('arrival',5,330,790,820),('update',6,350,825,800),('setup-dock',2,530,850,620),('outcome-dock',8,-80,865,650),('outcome-call',8,650,905,500),('cta-call',9,690,975,440)]:
 image={'setup-dock':'pickup','outcome-dock':'pickup','outcome-call':'update','cta-call':'update'}.get(id,id)
 c['objects'].append({'id':id,'image':image+'.png','slide':slide,'x':x,'y':y,'w':w,'float':False,'moment':{'type':'none'}})
(p/'content.json').write_text(json.dumps(c,indent=2));shutil.copy(root/'source-content.json',p/'source-content.json')
spec=importlib.util.spec_from_file_location('kit','/workspace/art-carousel-style2-kit/scripts/build.py');kit=importlib.util.module_from_spec(spec);spec.loader.exec_module(kit)
orig=kit.t_reveal
kit.TEMPLATES['reveal']=lambda s,ctx:orig(s,ctx).replace('width:660px;font-size:55','width:940px;font-size:55').replace('width:640px;font-size:27.5','width:850px;font-size:29').replace('width:760px;font-family','width:940px;font-family').replace('width:660px;font-size:23','width:940px;font-size:25')
origcta=kit.t_cta
kit.TEMPLATES['cta']=lambda s,ctx:origcta(s,ctx).split('<div class="icons tx">')[0]
kit.main(p)
css='.moment{position:absolute;z-index:4;pointer-events:none}.detect{height:8px;border-radius:8px;background:#ffae45;box-shadow:0 0 20px #ffae45;opacity:0}.routeDot{width:16px;height:16px;border-radius:50%;background:#36c2d4;box-shadow:0 0 15px #36c2d4}.callWave{border:3px solid #ffb45c;border-radius:50%;opacity:0}.inspection{width:3px;height:160px;background:linear-gradient(transparent,#04adc3,transparent);box-shadow:0 0 16px #04adc3;opacity:0}.sl .layer{z-index:2}.bg-aqua .stops{column-gap:30px;grid-template-columns:300px 300px}.task .hd{line-height:1.2}.task .res{flex-direction:row;gap:16px}.task .res span{white-space:nowrap}.sz .wi{line-height:1.45}.sz .bd{line-height:1.45}'
# Keep each image group grounded; story accents refer to actual object features.
extras={3:'<div class="moment detect" id="pickup-flag" style="left:677px;top:883px;width:112px"></div>',4:'<div class="moment routeDot" id="stalled-route" style="left:200px;top:1200px"></div>',5:'<div class="moment inspection" id="inspection" style="left:650px;top:1074px"></div>',6:'<div class="moment callWave" id="call-wave" style="left:774px;top:1031px;width:30px;height:30px"></div>'}
logic="""const pf=document.getElementById('pickup-flag');if(pf){pf.style.opacity=t>.7&&t<1.5?Math.sin((t-.7)/.8*Math.PI)*.7:0;}const sr=document.getElementById('stalled-route');if(sr){const u=eio(cl((t-.4)/1.2));sr.style.transform=`translate(${u*550}px,${-u*45}px)`;sr.style.background=t>1.6?'#ffae45':'#36c2d4';sr.style.boxShadow=t>1.6?'0 0 14px #ffae45':'0 0 14px #36c2d4';}const ins=document.getElementById('inspection');if(ins){const u=cl((t-.5)/1.4);ins.style.transform=`translateX(${u*200}px)`;ins.style.opacity=t>.5&&t<1.9?Math.sin(u*Math.PI)*.7:0;}const cw=document.getElementById('call-wave');if(cw){const u=cl((t-.8)/1.1);cw.style.transform=`scale(${1+u*2})`;cw.style.opacity=t>.8&&t<1.9?Math.sin(u*Math.PI)*.6:0;}"""
for i in range(2,10):
 f=p/'slides'/f'slide-{i:02}.html';s=f.read_text().replace('</style>',css+'</style>')
 # Place unique accents inside the currently visible slide, never a neighbouring scene.
 if i in extras:
  e=extras[i]
  s=s.replace('\n</div>\n<script>\nconst SLIDE',e+'\n</div>\n<script>\nconst SLIDE',1)
 s=s.replace('function R(t) {','function R(t) {'+logic)
 f.write_text(s)
# Keep edge-crossing objects on their own slide: no fragments over the next slide's text.
for i in range(2,10):
 f=p/'slides'/f'slide-{i:02}.html';s=f.read_text();own={o['id'] for o in c['objects'] if o['slide']==i}
 s=re.sub(r'<div class="flt" id="o-([^\"]+)"[^>]*>.*?</div>',lambda m:m[0] if m[1] in own else '',s,flags=re.S)
 if i==3:s=s.replace('</style>','.foot{left:200px}</style>')
 f.write_text(s)
# Use the approved warehouse cover rather than the old kit cover.
shutil.copy(root/'dock-preview/slides/assets/dock.png',p/'slides/assets/dock.png')
s=(root/'dock-preview/slides/slide-01.html').read_text()
s=s.replace('.clock{position:absolute;left:925px;top:416px;width:122px;height:122px;border-radius:50%;background:radial-gradient(circle,#17333b,#071c21);border:6px solid #647b7d;box-shadow:0 5px 14px #0009}', '.clock{position:absolute;left:911px;top:400px;width:150px;height:150px;background:none;border:0;box-shadow:none}.clock>img{position:absolute;width:100%;height:100%;object-fit:contain}.clock svg{position:absolute;left:20px;top:20px;filter:drop-shadow(0 0 2px #ffae45)}')
s=s.replace('<div class="clock"><div class="halo">','<div class="clock"><img src="assets/clock.png"><div class="halo">')
s=s.replace('<g stroke="#b4c8cb" stroke-width="2">','<g stroke="transparent" stroke-width="2">')
s=s.replace('stroke="#dce8e9"','stroke="#ffc36b"').replace('stroke="#36c2d4"','stroke="#ffc36b"').replace("t>1.65?'#ffaa40':'#36c2d4'","'#ffc36b'")
s=s.replace('rim.style.opacity=f','rim.style.opacity=f*.25')
(p/'slides/slide-01.html').write_text(s)
(p/'.gitignore').write_text('render/assets/\nrender/index.html\nrender/meta.json\npreview-all-slides.jpg\n')
(p/'README.md').write_text('# Delivery delays — completed Style 2 review\n\nApproved warehouse cover direction with corrected loading geometry and amber realistic clock. Remaining slides use supply-chain 3D scenes and the guide palette rhythm; no mascot or floating. Exact script preserved. Motion: clock sweep, setup sequence, pickup flag, stalled route, consignment inspection, call signal, ART hands, outcome ticks, CTA glow.\n\nReview deliverables: nine direct MP4s in render/out; nine PNGs in stills; PDF contact proof. Previous versions retained separately.\n')
print(p)
