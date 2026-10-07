import pathlib,importlib.util,shutil,json,html
p=pathlib.Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('kit','/workspace/art-carousel-kit/scripts/build.py');b=importlib.util.module_from_spec(spec);spec.loader.exec_module(b)
source=json.loads((p/'content.json').read_text());out=p/'slides';out.mkdir(exist_ok=True);shutil.copytree(b.KIT,out/'assets',dirs_exist_ok=True)
for f in (p/'artwork').glob('*.png'):shutil.copy2(f,out/'assets'/f.name)
def icon(kind):
 shapes={
 'orders':'<rect x="24" y="18" width="48" height="58" rx="4" fill="white"/><path d="M35 32h26M35 43h26M35 54h18"/><path d="M12 64h18l8 10h24l8-10h18v22H12z" fill="#04ADC3"/>',
 'stock':'<path d="M18 32l32-16 32 16v44L50 92 18 76z" fill="#04ADC3"/><path d="M18 32l32 16 32-16M50 48v44M34 24l32 16"/>',
 'paperwork':'<rect x="22" y="10" width="58" height="80" rx="5" fill="white"/><path d="M34 28h30M34 40h30M34 52h20"/><circle cx="70" cy="74" r="17" fill="#2B907F" stroke="none"/><path d="M60 74l7 7 13-15" stroke="white"/>',
 'dispatch':'<rect x="25" y="8" width="50" height="86" rx="8" fill="white"/><path d="M40 17h20M44 86h12"/><rect x="31" y="35" width="38" height="29" rx="3" fill="#04ADC3"/><path d="M31 35l19 16 19-16"/>'}
 return '<svg viewBox="0 0 100 100" fill="none" stroke="#1A1A1A" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">'+shapes[kind]+'</svg>'
common='''
.photo{position:absolute;inset:0;width:1080px;height:1350px;object-fit:cover}
.header{position:absolute;left:0;top:0;width:1080px;height:420px;background:#1A1A1A;border-bottom:3px solid #04ADC3}
.footer{position:absolute;left:0;top:1108px;bottom:0;width:1080px;background:#1A1A1A}
.kicker{position:absolute;left:84px;top:48px;border-radius:999px;padding:12px 22px;background:white;color:#1A1A1A;font:500 23px/1 Poppins}.kicker b{color:#04ADC3;padding-right:12px}
.photo-h{position:absolute;left:84px;right:84px;top:106px;font-size:62px;line-height:1.12;color:white}.photo-h em{color:#04ADC3;font-style:normal}
.photo-pain{position:absolute;left:84px;right:84px;top:274px;font:500 27px/1.36 Poppins;color:#DEDEDE}
.photo-whatif{display:block;z-index:10;position:absolute;left:84px;right:84px;top:948px;background:#04ADC3;border-radius:30px;padding:19px 25px;font:600 27px/1.35 Poppins;color:#1A1A1A}
.photo-result{position:absolute;left:84px;right:84px;top:1130px;min-height:62px;border-radius:999px;background:white;padding:15px 23px;font:600 25px/1.35 Poppins;color:#1A1A1A;display:flex;gap:14px;align-items:center}
.photo-result .check{flex:none;width:34px;height:34px;background:#2B907F;color:white;border-radius:50%;display:flex;align-items:center;justify-content:center}
.handle,.count{color:white!important;text-shadow:none}
.mascot{position:absolute;overflow:hidden}.mascot img{position:absolute;max-width:none}
'''
def mascot(name,x,y,w,h):
 # Analyse alpha only to fit each generated cutout; source images stay unchanged.
 from PIL import Image
 im=Image.open(p/'artwork'/f'{name}-mascot.png');a=im.getchannel('A');box=a.point(lambda v:255 if v>128 else 0).getbbox();l,t,r,bt=box
 k=min(w/(r-l),h/(bt-t));iw,ih=im.size
 return f'<div class="mascot" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px"><img src="assets/{name}-mascot.png" style="width:{iw*k}px;height:{ih*k}px;left:{-l*k+(w-(r-l)*k)/2}px;top:{-t*k}px"></div>'
accents={3:'multiple places?',4:'mid-rush?',5:'stacking up at the end of the day?',6:'calls piling up?'}
for slide in source['slides']:
 n=slide['number'];lines=[x.replace('**','') for x in slide['copy']];css=common;theme='dark';dark=True
 if n==1:
  inner='<img class="photo" src="assets/approved-cover.png">';css='.photo{position:absolute;inset:0;width:1080px;height:1350px;object-fit:cover}.handle,.count,#trail{display:none}'
 elif n in (2,3,4,5,6):
  inner=f'<img class="photo" src="assets/art-{n:02d}.png"><div class="header"></div><div class="footer"></div>'
  if n!=2:
   css+=' .photo{top:-72px}'
   if n==3:css+=' .photo{top:20px}'
   if n==5:css+=' .photo{top:-52px}.header{height:450px}.photo-pain{top:326px}'
   label=['ORDERS','STOCK','PAPERWORK','DISPATCH'][n-3];a=accents[n];h=html.escape(lines[0]).replace(html.escape(a),('<br>' if n in (3,6) else '')+'<em>'+html.escape(a)+'</em>')
   inner+=f'<div class="kicker"><b>{n-2}/4</b>{label}</div><div class="h-display photo-h">{h}</div><div class="photo-pain">{html.escape(lines[1])}</div><div class="photo-whatif">{html.escape(lines[2])}</div><div class="photo-result"><span class="check"><svg viewBox="0 0 34 34" width="34" height="34"><circle cx="17" cy="17" r="17" fill="#2B907F"/><path d="M9 17l6 6 11-13" fill="none" stroke="white" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg></span><span>{html.escape(lines[3])}</span></div>'
  else:
   css+=' .header{height:450px}.photo-h{top:80px;font-size:68px}.photo-pain{top:284px;font-size:30px;line-height:1.4}.setup-next{position:absolute;left:84px;top:1000px;border-radius:999px;background:#04ADC3;color:#1A1A1A;padding:18px 28px;font:600 32px/1.2 Poppins}'
   inner+=f'<div class="h-display photo-h">{html.escape(lines[0])}</div><div class="photo-pain">{html.escape(lines[1])}</div><div class="setup-next">{html.escape(lines[2])}</div>'
 elif n==7:
  theme='aqua';dark=False
  css+=' .handle,.count{color:#1A1A1A!important}.logo{position:absolute;top:58px;left:84px;width:220px}.photo-h{top:235px;font-size:51px;color:#1A1A1A}.reveal-body{position:absolute;left:84px;right:84px;top:445px;font:400 28px/1.43 Poppins;color:#1A1A1A}.reveal-body .em{color:#1A1A1A;background:white;padding:0 3px}.reveal-sign{position:absolute;left:84px;right:380px;top:790px;font:500 27px/1.4 Poppins;color:#1A1A1A}.system-rail{position:absolute;left:84px;top:987px;width:640px;height:172px;background:#1A1A1A;border-radius:32px;display:flex;align-items:center;justify-content:space-around}.node{width:118px;height:118px;border-radius:22px;background:white;padding:13px;position:relative}.node:not(:last-child):after{content:"";position:absolute;left:118px;top:55px;width:42px;height:4px;background:#04ADC3}.node svg{width:92px;height:92px}.link{position:absolute;left:720px;top:1068px;width:64px;border-top:4px solid #1A1A1A}.orbital{position:absolute;left:761px;top:974px;width:217px;height:217px;border:3px solid #1A1A1A;border-radius:50%}'
  inner=f'<img class="logo" src="assets/brand/logo-on-dark.png"><div class="h-display photo-h">{html.escape(lines[0])}</div><div class="reveal-body">{b.rich(slide["copy"][1])}</div><div class="reveal-sign">{html.escape(lines[2])}</div><div class="system-rail">'+''.join(f'<div class="node">{icon(k)}</div>' for k in ['orders','stock','paperwork','dispatch'])+'</div><div class="link"></div><div class="orbital"></div>'+mascot('reveal',746,929,250,280)
 elif n==8:
  theme='light';dark=False
  css+=' .handle,.count{color:#1A1A1A!important}.photo-h{top:82px;font-size:68px;color:#1A1A1A}.benefits{position:absolute;left:84px;right:84px;top:320px;display:grid;grid-template-columns:1fr 1fr;gap:22px}.benefit{height:264px;border-radius:26px;background:#1A1A1A;padding:24px;position:relative}.benefit svg{width:92px;height:92px;background:#DDF3F7;border-radius:18px;padding:8px}.benefit p{position:absolute;left:24px;right:24px;top:145px;color:white;font:600 28px/1.35 Poppins}.summary-end{position:absolute;left:84px;top:982px;width:656px;background:#04ADC3;border-radius:26px;padding:22px;font:600 30px/1.35 Poppins;color:#1A1A1A}.benefit p b{color:#41A486}'
  h=html.escape(lines[0]).replace('nothing slips.','<em>nothing slips.</em>')
  inner=f'<div class="h-display photo-h">{h}</div><div class="benefits">'+''.join(f'<div class="benefit">{icon(k)}<p><b>✓</b>{html.escape(l[1:])}</p></div>' for k,l in zip(['orders','stock','paperwork','dispatch'],lines[1:5]))+'</div>'+f'<div class="col summary-end">{html.escape(lines[5])}</div>'+mascot('solution',764,929,230,280)
 else:
  css+=' .photo-h{top:84px;font-size:76px}.cta-body{position:absolute;left:84px;right:84px;top:310px;font:500 34px/1.4 Poppins;color:#DEDEDE}.message{position:absolute;left:112px;top:470px;width:510px;height:400px;transform:rotate(-4deg)}.message svg{width:100%;height:100%}.cta-dm{position:absolute;left:84px;right:84px;top:990px;background:#04ADC3;border-radius:28px;padding:24px;font:600 32px/1.3 Poppins;color:#1A1A1A}.cta-save{position:absolute;left:132px;right:84px;top:1140px;font:500 27px/1.35 Poppins;color:white}.save-icon{position:absolute;left:84px;top:1142px;width:30px;height:40px;background:#04ADC3;clip-path:polygon(0 0,100% 0,100% 100%,50% 76%,0 100%)}'
  h=html.escape(lines[0]).replace('Diwali','<em>Diwali</em>')
  bubble='<svg viewBox="0 0 510 400"><path d="M45 10h420a30 30 0 0130 30v275a30 30 0 01-30 30H167l-76 45v-45H45a30 30 0 01-30-30V40a30 30 0 0130-30z" fill="#04ADC3"/><rect x="106" y="87" width="300" height="191" rx="19" fill="white"/><path d="M112 98l144 112 144-112" fill="none" stroke="#1A1A1A" stroke-width="12" stroke-linejoin="round"/></svg>'
  inner=f'<div class="h-display photo-h">{h}</div><div class="cta-body">{html.escape(lines[1])}</div><div class="message">{bubble}</div>'+mascot('cta',650,675,330,280)+f'<div class="cta-dm">{html.escape(lines[2])}</div><div class="save-icon"></div><div class="col cta-save">{html.escape(lines[3])}</div>'
 (out/f'slide-{n:02d}.html').write_text(b.page(f'photo-v2-{n:02d}',theme,inner,css,None,'scene',"document.fonts.load('40px Preahvihear');document.fonts.load('600 40px Poppins');",n,9,'@arealtimetech',dark,b.LIB,{}))
 print('Built static',n)
