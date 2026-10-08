from pathlib import Path
import json,importlib.util,shutil
p=Path(__file__).resolve().parent;root=p.parent;(p/'images/cut').mkdir(parents=True,exist_ok=True);shutil.copy(root/'source-content.json',p/'source-content.json');c=json.loads((root/'content.json').read_text());c['slides']=c['slides'][:1];c['palette']=['dark'];c['slides'][0].update(big_top=150,q_top=650,q_size=48,sub_top=960,arrow=[160,1100]);c['objects']=[{'id':'delay-story','image':'delay-team-customer.png','slide':1,'x':590,'y':600,'w':500,'float':False,'moment':{'type':'none'}}];(p/'content.json').write_text(json.dumps(c,indent=2))
spec=importlib.util.spec_from_file_location('style2',Path('/workspace/art-carousel-style2-kit/scripts/build.py'));kit=importlib.util.module_from_spec(spec);spec.loader.exec_module(kit);kit.HANDS='';cover=kit.t_cover
kit.TEMPLATES['cover']=lambda s,c:cover(s,c).replace('width:640px','width:960px',1).replace('width:640px','width:520px',1).replace('Catch delivery delays','Catch delivery<br>delays').replace(' before your customer does.','<br>before your<br>customer does.')
obj=kit.object_html
def object_html(o,sx,imgdir,project):
 html,after=obj(o,sx,imgdir,project)
 extra='''<svg id="early-route" viewBox="0 0 500 674" style="position:absolute;inset:0;width:100%;height:674px;overflow:visible;pointer-events:none"><path id="early-line" d="M450 285 C400 335,200 360,175 495" fill="none" stroke="#36C2D4" stroke-width="3" stroke-dasharray="380" stroke-dashoffset="380" opacity=".65"/><circle id="delay-ring" cx="450" cy="285" r="34" fill="none" stroke="#E3AE59" stroke-width="3" opacity="0"/></svg><div id="early-envelope" style="position:absolute;left:0;top:0;width:40px;height:30px;opacity:0;filter:drop-shadow(0 0 8px rgba(54,194,212,.65))"><svg viewBox="0 0 40 30" width="40" height="30"><rect x="1" y="1" width="38" height="28" rx="4" fill="#36C2D4" stroke="#E8FCFF" stroke-width="2"/><path d="M2 3 L20 17 L38 3" fill="none" stroke="white" stroke-width="2"/></svg></div><div id="team-received" style="position:absolute;left:143px;top:463px;width:64px;height:64px;border-radius:50%;background:#04ADC3;border:2px solid #E9FCFF;opacity:0;transform:scale(.8);box-shadow:0 0 22px rgba(4,173,195,.4)"><svg width="64" height="64" viewBox="0 0 64 64"><rect x="14" y="20" width="36" height="26" rx="4" fill="none" stroke="white" stroke-width="3"/><path d="M16 23 L32 35 L48 23" fill="none" stroke="white" stroke-width="3"/></svg></div>'''
 return html[:-6]+extra+'</div>',after
kit.object_html=object_html
js='''
 const route=document.getElementById('early-line'),packet=document.getElementById('early-envelope'),ring=document.getElementById('delay-ring'),received=document.getElementById('team-received');
 if(route){const u=eio(cl((t-.9)/1.05)),len=route.getTotalLength();route.style.strokeDasharray=len;route.style.strokeDashoffset=len*(1-u);const pt=route.getPointAtLength(len*u);packet.style.transform=`translate(${pt.x-20}px,${pt.y-15}px)`;packet.style.opacity=t>=.9&&t<2.1?Math.min(cl((t-.9)/.12),cl((2.1-t)/.15)):0;const a=cl((t-.45)/.65);ring.style.opacity=t>=.45&&t<1.1?Math.sin(a*Math.PI)*.9:0;ring.setAttribute('r',25+20*a);const v=eio(cl((t-1.95)/.3));received.style.opacity=v;received.style.transform=`scale(${.82+.18*v})`;}
'''
kit.JS=kit.JS.replace('function R(t) {','function R(t) {'+js);kit.main(p)
f=p/'slides/slide-01.html';v=f.read_text().replace('01/01','01/09').replace('@arealtimetech</div></div>','@arealtimetech</div><div class="arw">&rarr;</div></div>').replace('</style>','.big{word-spacing:10px}</style>');f.write_text(v)
(p/'.gitignore').write_text('render/*\n!render/out/\nrender/out/*\n!render/out/slide-01.mp4\npreview-all-slides.jpg\n')
(p/'README.md').write_text('''# Title-specific cover preview — Team hears first

Exact title and script retained. The stopped truck and checkpoint clock show a delivery delay. At 0.45s the clock receives one restrained amber emphasis; at 0.9s an envelope alert travels to the operations briefcase, arriving around 1.95s. The customer telephone stays quiet throughout. This illustrates early awareness, rather than goods inspection or a generic scan.

Style 2 fonts, dark palette, original ambient lighting, counter, footer and swipe arrow retained. Cover layout adjusted to a wider four-line hook with a lower text column beside the story. No float, bobbing, rocking, sirens, added marketing copy or product screens. Icons are illustrative communication symbols, not product UI.

Single experimental preview only. Review the animation before applying this direction to other slides. The previous scan and earlier cover proofs are superseded candidates, not approval.
''')
print('Title-specific cover prepared.')
