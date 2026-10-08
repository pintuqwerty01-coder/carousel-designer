from pathlib import Path
import json,shutil,importlib.util
p=Path(__file__).resolve().parent;root=p.parent;(p/'images/cut').mkdir(parents=True,exist_ok=True)
c=json.loads((root/'content.json').read_text());c['objects']=[{'id':'stall-truck','image':'truck.png','slide':4,'x':-180,'y':850,'w':760,'float':False,'moment':{'type':'drive','dx':90,'at':.2,'dur':1.0}}];s=c['slides'][3];s.update(x=440,y=230,w=580,blob=[250,90,1000,1040],ghost={'side':'left','offset':20,'top':420});(p/'content.json').write_text(json.dumps(c,indent=2));shutil.copy(root/'source-content.json',p/'source-content.json')
spec=importlib.util.spec_from_file_location('kit','/workspace/art-carousel-style2-kit/scripts/build.py');kit=importlib.util.module_from_spec(spec);spec.loader.exec_module(kit);kit.main(p)
f=p/'slides/slide-04.html';s=f.read_text()
# Preserve exact reference column, stacked pills, ghost numeral and dark blob. Grounded one-time stop.
s=s.replace("const ty = O.fl ? fy(O.ph, t) : 0;", "const ty = O.fl ? fy(O.ph, t) : 0;")
s=s.replace('</style>','.stall-lamp{position:absolute;z-index:4;left:565px;top:1210px;width:14px;height:14px;border-radius:50%;background:#ffb24b;box-shadow:0 0 24px #ffb24b;opacity:0}</style>')
s=s.replace('\n</div>\n<script>\nconst SLIDE','<div class="stall-lamp" id="stall-lamp"></div>\n</div>\n<script>\nconst SLIDE',1)
s=s.replace('function R(t) {',"function R(t) {const flag=document.getElementById('stall-lamp');if(flag){flag.style.opacity=cl((t-1.35)/.3)*.85;}")
s=s.replace('eio(cl((t - d.at) / d.dur))','eio(cl((t - d.at) / d.dur))')
s=s.replace('r = o.rot + 0.25 * Math.sin(TAU * t * 2)','r = o.rot')
f.write_text(s)
# A preview for slide 4 only: preserve its number and script.
for other in (p/'slides').glob('slide-*.html'):
 if other!=f:other.unlink()
(p/'.gitignore').write_text('render/assets/\nrender/index.html\nrender/meta.json\npreview-all-slides.jpg\n__pycache__/\n')
(p/'README.md').write_text('# Reference-matched in-transit revision\n\nReplaces the repeated warehouse/platform scenes with a single edge-crossing truck. Original Style 2 right-hand text column, stacked pills, aqua/dark blob and opposite ghost 2. One forward roll then a stop and a single amber detection marker. No floating, no siren, no scenic miniature road. Exact slide 4 copy. Revision preview, not approved.\n')
