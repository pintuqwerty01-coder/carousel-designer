from pathlib import Path
import importlib.util,json,shutil
p=Path(__file__).resolve().parent;root=p.parent;(p/'images/cut').mkdir(parents=True,exist_ok=True);shutil.copy(root/'source-content.json',p/'source-content.json');c=json.loads((root/'content.json').read_text());c['slides']=c['slides'][:1];c['palette']=['dark'];c['slides'][0].update(big_top=150,q_top=815,q_size=56,sub_top=1120,arrow=[600,1100]);c['objects']=[{'id':'detect-delay','image':'detect-delay.png','slide':1,'x':650,'y':520,'w':470,'float':False,'moment':{'type':'none'}}];(p/'content.json').write_text(json.dumps(c,indent=2))
spec=importlib.util.spec_from_file_location('style2',Path('/workspace/art-carousel-style2-kit/scripts/build.py'));kit=importlib.util.module_from_spec(spec);spec.loader.exec_module(kit);kit.HANDS='';cover=kit.t_cover;kit.TEMPLATES['cover']=lambda s,c:cover(s,c).replace('width:640px','width:720px',1).replace('width:640px','width:600px',1);kit.main(p)
f=p/'slides/slide-01.html';s=f.read_text().replace('01/01','01/09').replace('@arealtimetech</div></div>','@arealtimetech</div><div class="arw">&rarr;</div></div>').replace('</style>','.big{word-spacing:10px}</style>');f.write_text(s)
(p/'.gitignore').write_text('preview-all-slides.jpg\n')
(p/'README.md').write_text('''# Cover visual preview — spot the delay early

Direct PNG preview only; no ZIP or production animation. The prior truck-message concept was rejected. This uses one photoreal cut-out group: an aqua magnifying glass enlarges a clock associated with the delivery truck. It represents early detection of a delivery delay.

Preserve the supplied Style 2 cover typography, narrow column, original dark gradient and light effects, single edge-crossing object group, exact script and frame. 108px Poppins hook and 56px Preahvihear pride-led question. No added marketing labels, real brands, product screens, people, sirens or continuous floating. The longer title uses a 720px hook column to keep the brand size and readable line breaks.

Review the visual before authoring the story motion. The clock inside the lens gives the animation a concrete focal point. Do not build the other slides from this unapproved candidate.
''');print('Direct cover visual prepared.')
