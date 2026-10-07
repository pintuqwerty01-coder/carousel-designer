from pathlib import Path
import re
p=Path(__file__).resolve().parent
css='''
/* User typography rule: Preahvihear throughout, including body copy and footer. */
body,body * {font-family:"Preahvihear",sans-serif!important;font-weight:400!important;font-style:normal!important;font-synthesis:none!important;}
.photo-pain {font-size:27px;line-height:1.42;}
.photo-whatif {font-size:27px;line-height:1.42;}
.photo-result {font-size:25px;line-height:1.4;}
.setup-next {font-size:32px;}
.reveal-body {font-size:27px;line-height:1.48;}
.reveal-sign {font-size:25px;line-height:1.48;}
.benefit p {font-size:30px;line-height:1.4;}
.summary-end {font-size:30px;line-height:1.4;}
.cta-body {font-size:34px;line-height:1.4;}
.cta-dm {font-size:32px;line-height:1.4;}
.cta-save {font-size:27px;line-height:1.4;}
.handle {font-size:24px;}.count {font-size:22px;}.kicker {font-size:21px;}
.copy-symbol {display:inline-block;vertical-align:middle;width:22px;height:22px;position:relative;margin-right:5px;}
.copy-symbol svg {width:100%;height:100%;display:block;background:none;padding:0;border-radius:0;}
.setup-next .copy-symbol{width:34px;height:34px;margin-left:10px;margin-right:0;vertical-align:-7px}.setup-next .copy-symbol img{display:block;width:100%;height:100%}
.copy-symbol .source-symbol {position:absolute;opacity:0;width:0;height:0;font-size:0!important;overflow:hidden;}
'''
def symbol(char,paths):
 return f'<span class="copy-symbol"><span class="source-symbol">{char}</span><svg aria-hidden="true" viewBox="0 0 24 24">{paths}</svg></span>'
check=symbol('✓','<path d="m4 12 5 5 11-12" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>')
arrow=symbol('→','<path d="M3 12h18m-7-7 7 7-7 7" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>')
finger='<span class="copy-symbol"><span class="source-symbol">👇</span><img src="assets/point-down.svg" alt="" aria-hidden="true"></span>'
lamp=symbol('🪔','<path d="M3 14q9 13 18 0z" fill="#FFD166"/><path d="M12 14q-6-4 0-12 6 8 0 12z" fill="#F27A7A"/>')
for n in range(1,10):
 f=p/f'slides/slide-{n:02d}.html';s=f.read_text()
 if 'User typography rule' in s:continue
 if n==1:
  # Replace baked cover lettering with actual brand-font HTML over a cleaned photographic plate.
  s=s.replace('<img class="photo" src="assets/approved-cover.png">','''<img class="photo" src="assets/cover-no-text.png"><div class="cover-h">Festive season<br>orders are coming.<br>Can your<br><em>dispatch keep up?</em></div><div class="cover-sub">Diwali orders don't wait for anyone.</div><div class="cover-cta">Swipe to see where the rush usually breaks '''+arrow+'''</div>''')
  extra='''.handle,.count,#trail{display:block}.handle,.count{color:white!important}.cover-h{position:absolute;left:84px;right:84px;top:84px;color:white;font-size:84px;line-height:1.08;letter-spacing:-.01em}.cover-h em{color:#04ADC3}.cover-sub{position:absolute;left:84px;right:84px;top:470px;color:white;font-size:32px;line-height:1.4}.cover-cta{position:absolute;left:84px;right:84px;top:1108px;border-radius:99px;background:#04ADC3;color:#1A1A1A;padding:20px 28px;font-size:32px;line-height:1.4}.cover-cta .copy-symbol{margin-left:8px}'''
 else:extra=''
 s=s.replace('</style>',css+extra+'</style>',1)
 s=s.replace('<b>✓</b>','<b>'+check+'</b>').replace('👇',finger) if n==2 else s.replace('<b>✓</b>','<b>'+check+'</b>')
 if n==7:s=s.replace('🪔',lamp)
 # Ensure font readiness requests use the actual full-carousel face.
 s=s.replace("document.fonts.load('600 40px Poppins')","document.fonts.load('40px Preahvihear')")
 f.write_text(s)
