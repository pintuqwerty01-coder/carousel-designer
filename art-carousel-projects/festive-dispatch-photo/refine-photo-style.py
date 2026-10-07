from pathlib import Path
p=Path(__file__).resolve().parent
fontcss='''
/* Revision 5: fixed typography within each text role; no synthetic font styles. */
.photo-h,.photo-h em,.photo-h span{font-family:"Preahvihear",sans-serif;font-weight:400;font-style:normal;font-synthesis:none}
.photo-pain,.photo-whatif,.photo-result,.setup-next,.reveal-body,.reveal-sign{font-family:"Poppins",sans-serif;font-weight:500;font-style:normal;font-synthesis:none}
.photo-pain *, .photo-whatif *, .photo-result *, .reveal-body *, .reveal-sign *{font-family:inherit;font-weight:inherit;font-style:inherit;font-synthesis:none}
.source-arrow{display:inline-block;width:24px;height:26px;vertical-align:middle;position:relative;color:transparent;font-size:0;line-height:0}
.source-arrow:after{content:"";position:absolute;left:0;top:6px;width:24px;height:16px;background:currentColor}
.source-arrow svg{position:absolute;left:0;top:4px;width:24px;height:20px;color:#1A1A1A}
'''
for n in range(2,8):
 f=p/f'slides/slide-{n:02d}.html';s=f.read_text()
 if 'Revision 5: fixed typography' in s:continue
 css=fontcss
 if n==7:
  css+='''
.slide.aqua{background:#1A1A1A;color:white}
.photo-h{color:white}.logo{background:transparent}
.reveal-body,.reveal-sign{color:#DEDEDE}
.reveal-body .em{background:transparent;color:#04ADC3;padding:0}
.handle,.count{color:white!important}
.system-rail{background:#FFFFFF;border-color:#FFFFFF;box-shadow:none}
.node{background:#DDF3F7;box-shadow:none}
.orbital{background:#1A1A1A;border-color:white;box-shadow:0 0 0 10px #04ADC3}
.hub-lines{z-index:1}.hub-lines path{stroke:#04ADC3}
.system-rail{z-index:0}.node{z-index:2}.orbital{z-index:2}.mascot{z-index:3}
'''
 s=s.replace('</style>',css+'</style>',1)
 if n in (3,4,5,6):
  s=s.replace('<span>→ ','<span><span class="source-arrow">→<svg viewBox="0 0 24 20" aria-hidden="true"><path d="M2 10h19m-7-6 7 6-7 6" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></span> ')
 s=s.replace('drawTrail(TRX, 1080, 7, 9, 1 - Math.pow(1 - k, 3), false, true)','drawTrail(TRX, 1080, 7, 9, 1 - Math.pow(1 - k, 3), true, false)')
 f.write_text(s)
print('Slides 02–07 typography locked; reveal contrast revised; 08 and 09 unchanged')
