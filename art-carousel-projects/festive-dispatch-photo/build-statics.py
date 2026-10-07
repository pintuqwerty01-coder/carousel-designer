import pathlib,importlib.util,shutil,json,html
p=pathlib.Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('kit','/workspace/art-carousel-kit/scripts/build.py');b=importlib.util.module_from_spec(spec);spec.loader.exec_module(b)
source=json.loads((p/'content.json').read_text());out=p/'slides';out.mkdir(exist_ok=True);shutil.copytree(b.KIT,out/'assets',dirs_exist_ok=True)
for f in (p/'artwork').glob('*.png'):shutil.copy2(f,out/'assets'/f.name)
common='''
.photo{position:absolute;inset:0;width:1080px;height:1350px;object-fit:cover}
.wash{position:absolute;inset:0;background:linear-gradient(180deg,rgba(255,255,255,.98) 0%,rgba(255,255,255,.96) 28%,rgba(255,255,255,.82) 34%,rgba(255,255,255,0) 43%,transparent 67%,rgba(0,0,0,.25) 92%,rgba(0,0,0,.45) 100%)}
.kicker{position:absolute;left:84px;top:58px;border-radius:999px;padding:12px 22px;background:#1A1A1A;color:white;font:500 23px/1 Poppins}.kicker b{color:#04ADC3;padding-right:12px}
.photo-h{position:absolute;left:84px;right:84px;top:116px;font-size:62px;line-height:1.12;color:#1A1A1A}.photo-h em{color:#04ADC3;font-style:normal}
.photo-pain{position:absolute;left:84px;right:84px;top:345px;font:500 27px/1.36 Poppins;color:#1A1A1A}
.photo-whatif{position:absolute;left:84px;right:84px;top:948px;background:#04ADC3;border-radius:30px;padding:19px 25px;font:600 27px/1.35 Poppins;color:#1A1A1A}
.photo-result{position:absolute;left:84px;right:84px;top:1130px;min-height:62px;border-radius:999px;background:white;padding:15px 23px;font:600 25px/1.35 Poppins;color:#1A1A1A;display:flex;gap:14px;align-items:center}
.photo-result .check{flex:none;width:34px;height:34px;background:#2B907F;color:white;border-radius:50%;display:flex;align-items:center;justify-content:center}
.handle,.count{color:white!important;text-shadow:0 1px 4px #000}
'''
accents={3:'multiple places?',4:'mid-rush?',5:'stacking up at the end of the day?',6:'calls piling up?'}
for slide in source['slides']:
 n=slide['number'];lines=[x.replace('**','') for x in slide['copy']]
 if n==1:
  inner='<img class="photo" src="assets/approved-cover.png">';css='.photo{position:absolute;inset:0;width:1080px;height:1350px;object-fit:cover}.handle,.count,#trail{display:none}'
 else:
  css=common+' .slide.light{background:#1A1A1A}';inner=f'<img class="photo" src="assets/art-{n:02d}.png"><div class="wash"></div>'
  if n in (3,4,5,6):
   css+=' .photo{top:-72px}'
   if n!=5:css+=' .photo-pain{top:282px}.wash{background:linear-gradient(180deg,rgba(255,255,255,.98),rgba(255,255,255,.96) 20%,rgba(255,255,255,.85) 29%,transparent 35%,transparent 67%,rgba(0,0,0,.25) 92%,rgba(0,0,0,.45))}'
   if n==3:css+=' .photo{top:20px}'
   label=['ORDERS','STOCK','PAPERWORK','DISPATCH'][n-3];a=accents[n];h=html.escape(lines[0]).replace(html.escape(a),('<br>' if n in (3,6) else '')+'<em>'+html.escape(a)+'</em>')
   inner+=f'<div class="kicker"><b>{n-2}/4</b>{label}</div><div class="h-display photo-h">{h}</div><div class="photo-pain">{html.escape(lines[1])}</div><div class="col photo-whatif">{html.escape(lines[2])}</div><div class="photo-result"><span class="check">✓</span><span>{html.escape(lines[3])}</span></div>'
  elif n==2:
   css+=' .photo-h{top:108px;font-size:68px}.photo-pain{top:392px;font-size:30px;line-height:1.4}.setup-next{position:absolute;left:84px;top:1100px;border-radius:999px;background:#04ADC3;color:#1A1A1A;padding:18px 28px;font:600 32px/1.2 Poppins}.wash{background:linear-gradient(180deg,rgba(255,255,255,.98),rgba(255,255,255,.94) 43%,transparent 56%,transparent 79%,rgba(0,0,0,.4))}'
   inner+=f'<div class="h-display photo-h">{html.escape(lines[0])}</div><div class="photo-pain">{html.escape(lines[1])}</div><div class="setup-next">{html.escape(lines[2])}</div>'
  elif n==7:
   css+=' .wash{background:linear-gradient(180deg,rgba(26,26,26,.96),rgba(26,26,26,.92) 52%,rgba(26,26,26,0) 65%),linear-gradient(90deg,rgba(26,26,26,.7),rgba(26,26,26,.6) 45%,transparent 65%)}.logo{position:absolute;top:58px;left:84px;width:220px}.photo-h{top:235px;font-size:51px;color:white}.reveal-body{position:absolute;left:84px;right:84px;top:445px;font:400 28px/1.43 Poppins;color:white}.reveal-sign{position:absolute;left:84px;right:380px;top:824px;font:500 27px/1.4 Poppins;color:white}'
   inner+=f'<img class="logo" src="assets/brand/logo-on-dark.png"><div class="h-display photo-h">{html.escape(lines[0])}</div><div class="reveal-body">{b.rich(slide["copy"][1])}</div><div class="reveal-sign">{html.escape(lines[2])}</div>'
  elif n==8:
   css+=' .photo-h{top:90px;font-size:66px}.summary{position:absolute;left:84px;right:84px;top:340px;display:grid;grid-template-columns:1fr 1fr;gap:16px}.summary div{background:white;border-radius:22px;padding:18px;font:600 27px/1.35 Poppins;color:#1A1A1A;border-left:6px solid #2B907F}.summary-end{position:absolute;left:84px;right:84px;top:1090px;background:#04ADC3;border-radius:28px;padding:22px;font:600 29px/1.35 Poppins;color:#1A1A1A}.wash{background:linear-gradient(180deg,rgba(255,255,255,.98),rgba(255,255,255,.94) 30%,transparent 51%,transparent 79%,rgba(0,0,0,.4))}'
   inner+=f'<div class="h-display photo-h">{html.escape(lines[0])}</div><div class="summary">'+''.join(f'<div>{html.escape(l)}</div>' for l in lines[1:5])+f'</div><div class="col summary-end">{html.escape(lines[5])}</div>'
  else:
   css+=' .photo-h{top:100px;font-size:76px}.cta-body{position:absolute;left:84px;right:84px;top:358px;font:500 34px/1.4 Poppins;color:#1A1A1A}.cta-dm{position:absolute;left:84px;right:84px;top:1000px;background:#04ADC3;border-radius:28px;padding:24px;font:600 32px/1.3 Poppins;color:#1A1A1A}.cta-save{position:absolute;left:84px;right:84px;top:1145px;font:500 27px/1.35 Poppins;color:white}'
   inner+=f'<div class="h-display photo-h">{html.escape(lines[0])}</div><div class="cta-body">{html.escape(lines[1])}</div><div class="cta-dm">{html.escape(lines[2])}</div><div class="col cta-save">{html.escape(lines[3])}</div>'
 (out/f'slide-{n:02d}.html').write_text(b.page(f'photo-{n:02d}','light',inner,css,None,'scene',"document.fonts.load('40px Preahvihear');document.fonts.load('600 40px Poppins');",n,9,'@arealtimetech',True,b.LIB,{}))
 print('Built static',n)
