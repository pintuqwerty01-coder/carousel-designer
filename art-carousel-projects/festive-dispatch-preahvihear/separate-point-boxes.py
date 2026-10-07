from pathlib import Path
import re
p=Path('/workspace/art-carousel-projects/festive-dispatch-preahvihear')
sep=r'<span class="copy-symbol separator-dot">.*?</span><svg.*?</svg></span>'
for n in range(1,10):
 f=p/f'slides/slide-{n:02}.html';s=f.read_text()
 if n in (3,4,5,6):
  m=re.search(r'<div class="photo-result">(.*?)</div>',s); parts=re.split(sep,m[1])
  assert len(parts)==2
  s=s[:m.start()]+ '<div class="photo-result">'+ '<span class="point-box">'+parts[0].strip()+'</span> <span class="source-symbol">·</span> <span class="point-box">'+parts[1].strip()+'</span></div>'+s[m.end():]
 if n in (2,9):
  cls='setup-topics' if n==2 else 'engagement';m=re.search(r'<div class="'+cls+r'">(.*?)</div>',s)
  inner=re.sub(sep,'<span class="source-symbol">·</span>',m[1])
  if n==9:inner=inner.replace('<span><span class="copy-symbol">','<span class="engagement-box"><span class="copy-symbol">')
  s=s[:m.start()]+f'<div class="{cls}">'+inner+'</div>'+s[m.end():]
 css='''
/* Individually boxed points */
.setup-topics{display:grid;grid-template-columns:1fr 1fr 1.25fr 1.2fr;gap:14px;padding:0;background:none;border:0;border-radius:0;top:1090px;font-size:24px;line-height:1.4}
.setup-topics>.source-symbol,.photo-result>.source-symbol,.engagement>.source-symbol{position:absolute}
.setup-topic{display:flex;align-items:center;justify-content:center;gap:9px;padding:22px 17px;background:rgba(26,26,26,.94);border:1px solid rgba(255,255,255,.38);border-top:4px solid #04ADC3;border-radius:20px;min-height:90px;box-sizing:border-box}
.setup-topic:nth-of-type(3){border-top-color:#2B907F}.setup-topic:nth-of-type(5){border-top-color:#FFD166}.setup-topic:nth-of-type(7){border-top-color:#FFFFFF}
.photo-result{display:grid;grid-template-columns:1fr 1fr;gap:18px;padding:0;background:none;border-radius:0;top:1106px;font-size:24px;line-height:1.35;min-height:90px}
.point-box{display:flex;align-items:center;justify-content:center;gap:11px;background:white;color:#1A1A1A;border-radius:24px;padding:20px;box-sizing:border-box;min-height:90px;border-left:5px solid #2B907F}
.point-box:last-child{border-left:0;border-right:5px solid #04ADC3}.point-box .copy-symbol{flex:none;width:24px;height:24px;margin:0}
.engagement{top:1158px;display:grid;grid-template-columns:1fr 1.13fr 1.1fr;gap:14px;font-size:20px;line-height:1.4}
.engagement-box{display:flex;align-items:center;justify-content:center;gap:9px;min-height:60px;padding:14px 17px;border:1px solid #626262;border-radius:18px;background:#242424;box-sizing:border-box}
.engagement-box .copy-symbol{flex:none;margin:0;width:22px;height:22px}.engagement-box:first-child{border-color:#F27A7A}.engagement-box:last-child{border-color:#04ADC3}
.benefit{border-left:0;border:1px solid #DEDEDE;box-shadow:inset 6px 0 #04ADC3}.benefit:nth-child(2){box-shadow:inset 6px 0 #2B907F}.benefit:nth-child(3){box-shadow:inset 6px 0 #FFD166}.benefit:nth-child(4){box-shadow:inset 6px 0 #04ADC3}
'''
 s=s.replace('</style>',css+'</style>');f.write_text(s)
f=p/'audit-boxes.py';s=f.read_text().replace('.setup-topics,.photo-whatif,.photo-result,.benefit,.cta-dm\')','.setup-topic,.photo-whatif,.point-box,.benefit,.cta-dm,.engagement-box\')');f.write_text(s)
