from pathlib import Path
import json,shutil,importlib.util,re
p=Path(__file__).resolve().parent;root=p.parent;(p/'images/cut').mkdir(parents=True,exist_ok=True)
# Generated assets are retained unchanged in images/cut.
c=json.loads((root/'reference-transit/content.json').read_text());c['slides'][2].update(y=220);c['slides'][4].update(w=640);c['slides'][5].update(y=200);c['slides'][6].update(body_top=640,line_top=1045,sign_top=1140);c['slides'][7].update(x=440,w=590,y=210)
c['objects']=[{'id':id,'image':image+'.png','slide':n,'x':x,'y':y,'w':w,'float':False,'moment':moment} for id,image,n,x,y,w,moment in [
 ('cover-pallet','cover-pallet',1,770,300,650,{'type':'none'}),('pickup','pickup',3,550,850,690,{'type':'none'}),('stall-truck','truck',4,-180,850,760,{'type':'drive','dx':90,'at':.2,'dur':1.0}),('checkpoint','checkpoint',5,715,460,530,{'type':'none'}),('phone','phone',6,-90,850,720,{'type':'none'}),('outcome-truck','truck',8,-200,885,580,{'type':'drive','dx':30,'at':.3,'dur':1.4})]]
(p/'content.json').write_text(json.dumps(c,indent=2));shutil.copy(root/'source-content.json',p/'source-content.json')
spec=importlib.util.spec_from_file_location('kit','/workspace/art-carousel-style2-kit/scripts/build.py');kit=importlib.util.module_from_spec(spec);spec.loader.exec_module(kit)
origcover=kit.t_cover;kit.TEMPLATES['cover']=lambda s,c:origcover(s,c).replace('width:640px','width:720px',1).replace('width:640px','width:600px',1)
origreveal=kit.t_reveal;kit.TEMPLATES['reveal']=lambda s,c:origreveal(s,c).replace('width:660px;font-size:55','width:850px;font-size:55').replace('width:640px;font-size:27.5','width:850px;font-size:29').replace('width:760px;font-family','width:940px;font-family').replace('width:660px;font-size:23','width:940px;font-size:25')
origcta=kit.t_cta;kit.TEMPLATES['cta']=lambda s,c:origcta(s,c).split('<div class="icons tx">')[0]
kit.main(p)
css='''#o-cover-pallet img{transform:scaleX(-1)}#o-checkpoint img{transform:scaleX(-1)}.big{word-spacing:10px}.clockUnit{position:absolute;left:799px;top:250px;width:160px;height:160px;z-index:4}.clockUnit img{width:160px;height:160px}.clockUnit svg{position:absolute;left:20px;top:18px;width:120px;height:120px;filter:drop-shadow(0 0 2px #ffaa40)}.clockUnit line{transform-origin:60px 60px}.clockGlow{position:absolute;inset:7px;border:2px solid #ffb45c;border-radius:5px;opacity:0;box-shadow:0 0 20px #ffb45c}.moment{position:absolute;z-index:4;pointer-events:none}.pickupFlag{width:64px;height:130px;border:3px solid #ffb45c;border-radius:3px;box-shadow:0 0 12px #ffb45c;opacity:0}.scan{width:4px;height:185px;background:linear-gradient(transparent,#ffb45c,transparent);box-shadow:0 0 12px #ffb45c;opacity:0}.callSignal path{stroke:#ffb45c;stroke-width:4;fill:none;stroke-linecap:round;stroke-dasharray:90;stroke-dashoffset:90}.callSignal{width:140px;height:90px;opacity:0}.stall-lamp{position:absolute;z-index:4;left:565px;top:1210px;width:14px;height:14px;border-radius:50%;background:#ffb24b;box-shadow:0 0 24px #ffb24b;opacity:0}'''
extras={1:'<div class="clockUnit"><img src="assets/img/clock.png"><div class="clockGlow"></div><svg viewBox="0 0 120 120"><line id="hour" x1="60" y1="60" x2="60" y2="31" stroke="#ffc36b" stroke-width="4" stroke-linecap="round"/><line id="minute" x1="60" y1="60" x2="60" y2="18" stroke="#ffc36b" stroke-width="3" stroke-linecap="round"/><circle cx="60" cy="60" r="4" fill="#ffcf80"/></svg></div>',3:'<div class="moment pickupFlag" style="left:923px;top:963px"></div>',4:'<div class="stall-lamp" id="stall-lamp"></div>',5:'<div class="moment scan" style="left:906px;top:877px"></div>',6:'<svg class="moment callSignal" style="left:305px;top:976px" viewBox="0 0 140 90"><path d="M10 74 Q34 60 22 36"/><path d="M34 80 Q65 52 47 21"/><path d="M65 85 Q101 45 72 6"/></svg>'}
logic="""const minute=document.getElementById('minute'),hour=document.getElementById('hour');if(minute){const u=eio(cl((t-.4)/1.7));minute.style.transform=`rotate(${60+35*u}deg)`;hour.style.transform=`rotate(${305+35*u/12}deg)`;document.querySelector('.clockGlow').style.opacity=t>1.7&&t<2.6?Math.sin((t-1.7)/.9*Math.PI)*.7:0;}const flag=document.querySelector('.pickupFlag');if(flag)flag.style.opacity=cl((t-.8)/.4)*.75;const scan=document.querySelector('.scan');if(scan){const u=cl((t-.5)/1.4);scan.style.transform=`translateX(${u*120}px)`;scan.style.opacity=t>.5&&t<1.9?Math.sin(u*Math.PI)*.85:0;}const call=document.querySelector('.callSignal');if(call){call.style.opacity=t>.6&&t<2.3?1:0;[...call.querySelectorAll('path')].forEach((e,i)=>e.style.strokeDashoffset=90*(1-eio(cl((t-.7-i*.15)/.5))));}const lamp=document.getElementById('stall-lamp');if(lamp)lamp.style.opacity=cl((t-1.35)/.3)*.85;"""
for i in range(1,10):
 f=p/'slides'/f'slide-{i:02}.html';s=f.read_text();own={o['id'] for o in c['objects'] if o['slide']==i}
 s=re.sub(r'<div class="flt" id="o-([^\"]+)"[^>]*>.*?</div>',lambda m:m[0] if m[1] in own else '',s,flags=re.S)
 s=s.replace('</style>',css+'</style>');s=s.replace('r = o.rot + 0.25 * Math.sin(TAU * t * 2)','r = o.rot')
 if i in extras:s=s.replace('\n</div>\n<script>\nconst SLIDE',extras[i]+'\n</div>\n<script>\nconst SLIDE',1)
 s=s.replace('function R(t) {','function R(t) {'+logic)
 if i==3:s=s.replace('</style>','.foot{left:200px}</style>')
 f.write_text(s)
# The approved slide is retained exactly, including its rendered motion.
shutil.copy(root/'reference-transit/slides/slide-04.html',p/'slides/slide-04.html')
(p/'render/out').mkdir(parents=True,exist_ok=True);shutil.copy(root/'reference-transit/render/out/slide-04.mp4',p/'render/out/slide-04.mp4')
(p/'.gitignore').write_text('render/assets/\nrender/index.html\nrender/meta.json\npreview-all-slides.jpg\n__pycache__/\n')
print(p)


def patch_story(p):
 c=json.loads((p/'content.json').read_text());motions={'cover-pallet':{'type':'drive','dx':22,'at':.2,'dur':1.0},'pickup':{'type':'drive','dx':-45,'at':.2,'dur':1.0},'checkpoint':{'type':'clock_sweep','degrees':75,'at':.4,'dur':1.7}}
 for o in c['objects']:
  if o['id'] in motions:o['moment']=motions[o['id']]
 c['objects']=[o for o in c['objects'] if o['id']!='update-envelope'];c['objects'].append({'id':'update-envelope','image':'envelope.png','slide':6,'x':340,'y':915,'w':290,'float':False,'moment':{'type':'drive','dx':85,'at':.65,'dur':1.0}})
 (p/'content.json').write_text(json.dumps(c,indent=2))
 for n in [1,3,5,6]:
  f=p/'slides'/f'slide-{n:02}.html';s=f.read_text()
  if n in [1,3]:
   id='cover-pallet' if n==1 else 'pickup';d=json.dumps({k:v for k,v in motions[id].items() if k!='type'})
   s=s.replace(f'id="o-{id}"',f'id="o-{id}" data-drive=\'{d}\'',1)
   if n==1:s=s.replace('if(minute){','if(minute){document.querySelector(\'.clockUnit\').style.transform=`translateX(${22*eio(cl((t-.2)/1.0))}px)`;')
   else:s=s.replace("if(flag)flag.style.opacity=cl((t-.8)/.4)*.75;", "if(flag){flag.style.transform=`translateX(${-45*eio(cl((t-.2)/1.0))}px)`;flag.style.opacity=cl((t-1.35)/.3)*.75;}")
  if n==5:
   s=re.sub(r'<div class="moment scan"[^>]*></div>','',s)
   clock='<svg class="moment" style="left:735px;top:572px;width:120px;height:120px;filter:drop-shadow(0 0 2px #ffaa40)" viewBox="0 0 120 120"><line id="checkpoint-hour" x1="60" y1="60" x2="60" y2="34" stroke="#ffc36b" stroke-width="4" stroke-linecap="round" style="transform-origin:60px 60px"/><line id="checkpoint-minute" x1="60" y1="60" x2="60" y2="18" stroke="#ffc36b" stroke-width="3" stroke-linecap="round" style="transform-origin:60px 60px"/><circle cx="60" cy="60" r="4" fill="#ffcd80"/></svg>'
   s=s.replace('\n</div>\n<script>\nconst SLIDE',clock+'\n</div>\n<script>\nconst SLIDE',1)
   s=s.replace('function R(t) {','function R(t) {const cm=document.getElementById(\'checkpoint-minute\'),ch=document.getElementById(\'checkpoint-hour\');if(cm){const cu=eio(cl((t-.4)/1.7));cm.style.transform=`rotate(${60+75*cu}deg)`;ch.style.transform=`rotate(${305+75*cu/12}deg)`;}')
  if n==6:
   s=re.sub(r'<svg class="moment callSignal".*?</svg>','',s,flags=re.S)
   envelope='''<div class="flt" id="o-update-envelope" data-rot="0" data-ph="0" data-float="0" data-drive='{"dx":85,"at":0.65,"dur":1.0}' style="position:absolute;left:340px;top:915px;width:290px;z-index:4"><img src="assets/img/envelope.png" style="display:block;width:100%;filter:drop-shadow(0 12px 14px rgba(0,0,0,.2))"></div>'''
   s=s.replace('\n</div>\n<script>\nconst SLIDE',envelope+'\n</div>\n<script>\nconst SLIDE',1)
  f.write_text(s)
patch_story(p)
