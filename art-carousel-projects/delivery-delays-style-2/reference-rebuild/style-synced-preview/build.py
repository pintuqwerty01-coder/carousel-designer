from pathlib import Path
import importlib.util,json,shutil
p=Path(__file__).resolve().parent;root=p.parent;(p/'images/cut').mkdir(parents=True,exist_ok=True);shutil.copy(root/'source-content.json',p/'source-content.json');c=json.loads((root/'content.json').read_text());c['slides']=c['slides'][:1];c['palette']=['dark'];c['slides'][0].update(big_top=150,q_top=815,q_size=56,sub_top=1120,arrow=[600,1100]);c['objects']=[{'id':'truck-hero','image':'truck-hero.png','slide':1,'x':800,'y':200,'w':540,'float':False,'moment':{'type':'drive','dx':-28,'at':.2,'dur':.7}}];(p/'content.json').write_text(json.dumps(c,indent=2))
spec=importlib.util.spec_from_file_location('style2',Path('/workspace/art-carousel-style2-kit/scripts/build.py'));kit=importlib.util.module_from_spec(spec);spec.loader.exec_module(kit);kit.HANDS='';cover=kit.t_cover;kit.TEMPLATES['cover']=lambda s,c:cover(s,c).replace('width:640px','width:720px',1)
obj=kit.object_html
def object_html(o,sx,imgdir,project):
 h,a=obj(o,sx,imgdir,project)
 h=h[:-6]+'''<div id="early-alert" style="position:absolute;left:173px;top:360px;width:76px;height:60px;opacity:0;transform-origin:50% 100%;filter:drop-shadow(0 9px 12px rgba(0,0,0,.35))"><svg width="76" height="60" viewBox="0 0 76 60"><path d="M12 2 H64 Q74 2 74 12 V39 Q74 49 64 49 H29 L14 59 V49 H12 Q2 49 2 39 V12 Q2 2 12 2Z" fill="#04ADC3" stroke="#DEFAFF" stroke-width="2"/><rect x="14" y="14" width="36" height="23" rx="3" fill="none" stroke="white" stroke-width="2.5"/><path d="M16 16 L32 27 L48 16" fill="none" stroke="white" stroke-width="2.5"/><circle cx="59" cy="15" r="12" fill="#E9FCFF"/><path d="M59 7 V15 L65 18" fill="none" stroke="#038DA0" stroke-width="2.5" stroke-linecap="round"/></svg></div></div>'''
 return h,a
kit.object_html=object_html;kit.JS=kit.JS.replace('r = o.rot + 0.25 * Math.sin(TAU * t * 2);','y=0; r=o.rot;')
kit.JS=kit.JS.replace('function R(t) {','''function R(t) {
 const alert=document.getElementById('early-alert');if(alert){const u=eio(cl((t-.95)/.48));alert.style.opacity=u;alert.style.transform=`translate(${-34*u}px,${-72*u}px) scale(${.65+.35*u})`;}
''');kit.main(p)
f=p/'slides/slide-01.html';s=f.read_text().replace('01/01','01/09').replace('@arealtimetech</div></div>','@arealtimetech</div><div class="arw">&rarr;</div></div>').replace('</style>','.big{word-spacing:10px}</style>');f.write_text(s)
(p/'.gitignore').write_text('render/*\n!render/out/\nrender/out/*\n!render/out/slide-01.mp4\npreview-all-slides.jpg\n')
(p/'README.md').write_text('''# Style 2 — title-synchronised cover preview

The supplied MD's narrow left cover column, 108px Poppins bold hook, 56px Preahvihear pride-led question, supporting subline, original dark blue-green gradients, lens flare, streaks, bokeh, dashed curved swipe arrow, counter and arrow-box frame are retained. Only the headline column widens slightly to 720px to fit the supplied longer title without changing its type size.

One photoreal ivory/aqua truck crosses the right edge. It rolls 28px toward the viewer/left from 0.2 to 0.9s and then stops. From 0.95 to 1.43s one message bubble with a clock cue emerges from the cab and settles. This signals a delivery stall triggering early awareness. It uses the guide's drive and message-bubble story vocabulary, not a multi-object communication diagram or stock-inspection scan.

Exact cover script unchanged. No logo, product screens, human figures, sirens or extra copy. Generic continuous bobbing/rocking is disabled per prior user feedback; the purposeful message emergence is the story action. Ambient lights and arrow animate as prescribed in the MD.

Single four-second cover preview for review; not a final nine-slide set or approved production. The other candidate directions remain historical experiments.
''');print('Style-synchronised single-hero preview prepared.')
