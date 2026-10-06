import pathlib,json,shutil,importlib.util,html
p=pathlib.Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('kit','/workspace/art-carousel-kit/scripts/build.py');b=importlib.util.module_from_spec(spec);spec.loader.exec_module(b)
source=json.loads(pathlib.Path('/workspace/art-carousel-projects/festive-dispatch/content.json').read_text())
slides=[x for x in source['slides'] if x['number'] in (3,4,5,6)]
(p/'content.json').write_text(json.dumps({'status':'Concept C — four-slide motion-poster experiment; exact source copy','handle':'@arealtimetech','slides':slides},indent=2,ensure_ascii=False))
out=p/'slides';out.mkdir(exist_ok=True);shutil.copytree(b.KIT,out/'assets',dirs_exist_ok=True)
lib=b.LIB+'\n'+(p/'scenes.js').read_text()
for s in slides:
 n=s['number'];lines=[x.replace('**','') for x in s['copy']];label=['Orders','Stock','Paperwork','Dispatch'][n-3]
 css='''
.poster-rule{position:absolute;left:0;top:0;width:20px;height:1350px;background:#04ADC3}
.kicker{position:absolute;top:66px;left:84px;right:84px;display:flex;justify-content:space-between;align-items:center;color:#04ADC3;font:600 24px/1 Poppins;letter-spacing:.12em;text-transform:uppercase}
.kicker b{color:#1A1A1A;font:400 40px/1 Preahvihear;letter-spacing:0}
.poster-h{position:absolute;left:84px;right:84px;top:128px;font-size:61px;line-height:1.12}
.poster-pain{position:absolute;left:84px;right:84px;top:348px;font:400 27px/1.35 Poppins;color:#3D3D3D}
.poster-art{position:absolute;left:0;top:484px;width:1080px;height:420px;background:#1A1A1A;overflow:hidden;clip-path:polygon(0 0,96% 0,100% 10%,100% 100%,4% 100%,0 90%)}
.poster-art canvas{width:1080px;height:420px;image-rendering:auto}
.poster-whatif{position:absolute;left:84px;right:84px;top:939px;font:600 28px/1.35 Poppins;padding-left:22px;border-left:6px solid #04ADC3}
.poster-outcome{position:absolute;left:84px;right:84px;top:1111px;font:600 26px/1.35 Poppins;color:#1A1A1A;padding-top:14px;border-top:2px solid #DDF3F7}
.poster-outcome::before{content:'';display:inline-block;width:9px;height:9px;border-radius:50%;background:#2B907F;margin-right:14px}
'''
 # The outcome itself is a result element: retain the green tick and avoid green decoration.
 css=css.replace(".poster-outcome::before{content:'';display:inline-block;width:9px;height:9px;border-radius:50%;background:#2B907F;margin-right:14px}","")
 inner=f'''<div class="poster-rule"></div><div class="kicker"><span>{label}</span><b>{n-2}/4</b></div><div class="h-display poster-h">{html.escape(lines[0])}</div><div class="poster-pain">{html.escape(lines[1])}</div><div class="poster-art stage"><canvas id="scene" width="1080" height="420" data-scale="1"></canvas></div><div class="col poster-whatif">{html.escape(lines[2])}</div><div class="poster-outcome">{html.escape(lines[3])}</div>'''
 key=['posterOrders','posterStock','posterPaperwork','posterDispatch'][n-3]
 (out/f'slide-{n:02d}.html').write_text(b.page(f'poster-{n:02d}','light',inner,css,key,'scene','',n,9,'@arealtimetech',False,lib,{}))
 print('Built motion poster',n)
