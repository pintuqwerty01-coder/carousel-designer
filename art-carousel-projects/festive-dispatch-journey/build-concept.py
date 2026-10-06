import pathlib,json,shutil,importlib.util,html
p=pathlib.Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('kit','/workspace/art-carousel-kit/scripts/build.py');b=importlib.util.module_from_spec(spec);spec.loader.exec_module(b)
source=json.loads(pathlib.Path('/workspace/art-carousel-projects/festive-dispatch/content.json').read_text())
slides=[x for x in source['slides'] if x['number'] in (3,4)]
(p/'content.json').write_text(json.dumps({'status':'Design concept B; exact draft copy; two-slide prototype','handle':'@arealtimetech','slides':slides},indent=2,ensure_ascii=False))
out=p/'slides';out.mkdir(exist_ok=True);shutil.copytree(b.KIT,out/'assets',dirs_exist_ok=True)
lib=b.LIB+'\n'+(p/'scenes.js').read_text()
for s in slides:
 n=s['number'];lines=[x.replace('**','') for x in s['copy']];label='Orders' if n==3 else 'Stock'
 css='''
.j-kicker{position:absolute;left:84px;right:84px;top:76px;display:flex;gap:20px;align-items:center;font:600 24px/1 Poppins;letter-spacing:.12em;color:#04ADC3;text-transform:uppercase}
.j-kicker b{background:#1A1A1A;color:white;border-radius:999px;padding:13px 20px;font-weight:500;letter-spacing:0}
.j-head{position:absolute;top:145px;left:84px;right:84px;font-size:72px;line-height:1.18}
.j-pain{position:absolute;top:345px;left:84px;right:84px;font:400 29px/1.4 Poppins;color:#3D3D3D}
.j-art{position:absolute;left:0;top:485px;width:1080px;height:440px;overflow:hidden}
.j-art canvas{width:1080px;height:440px;image-rendering:auto}
.j-whatif{position:absolute;top:946px;left:84px;right:84px;border-left:6px solid #04ADC3;padding-left:22px;font:600 29px/1.35 Poppins}
.j-result{position:absolute;left:84px;right:84px;top:1100px;color:white;background:linear-gradient(135deg,#41A486,#1C5E55);padding:15px 22px;border-radius:14px;font:600 25px/1.3 Poppins;box-shadow:0 4px 12px #17333118}
'''
 inner=f'''<div class="j-kicker"><b>{n-2}/4</b><span>{label}</span></div><div class="h-display j-head">{html.escape(lines[0])}</div><div class="j-pain">{html.escape(lines[1])}</div><div class="j-art stage"><canvas id="scene" width="1080" height="440" data-scale="1"></canvas></div><div class="col j-whatif">{html.escape(lines[2])}</div><div class="j-result">{html.escape(lines[3])}</div>'''
 key='journeyOrders' if n==3 else 'journeyStock'
 (out/f'slide-{n:02d}.html').write_text(b.page(f'journey-{n:02d}','light',inner,css,key,'scene','',n,9,'@arealtimetech',False,lib,{}))
 print('Built new concept',n)
