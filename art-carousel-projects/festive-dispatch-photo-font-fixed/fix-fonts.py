from pathlib import Path
p=Path(__file__).resolve().parent
css='''
/* Typography correction only: preserve linked revision's photos, copy and layout. */
body {font-family:"Poppins",sans-serif;font-synthesis:none;}
.photo-h,.photo-h em,.photo-h strong {font-family:"Preahvihear",sans-serif;font-weight:400;font-style:normal;}
.photo-pain,.photo-whatif,.photo-result,.setup-next,.reveal-body,.reveal-sign,.benefit p,.summary-end,.cta-body,.cta-dm,.cta-save,.handle,.count,.kicker {font-family:"Poppins",sans-serif;font-weight:500;font-style:normal;}
.reveal-body strong,.reveal-body .em,.kicker b {font-family:inherit;font-weight:inherit;font-style:normal;}
.copy-symbol{display:inline-block;vertical-align:middle;width:22px;height:22px;position:relative;margin-right:5px;}
.copy-symbol svg{width:100%;height:100%;display:block;background:none;padding:0;border-radius:0;}
.copy-symbol .source-symbol{position:absolute;opacity:0;width:0;height:0;font-size:0;overflow:hidden;}
'''
arrow='<span class="copy-symbol"><span class="source-symbol">→</span><svg aria-hidden="true" viewBox="0 0 24 24"><path d="M3 12h18m-7-7 7 7-7 7" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>'
check='<span class="copy-symbol"><span class="source-symbol">✓</span><svg aria-hidden="true" viewBox="0 0 24 24"><path d="m4 12 5 5 11-12" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg></span>'
for n in range(2,10):
 f=p/f'slides/slide-{n:02d}.html';s=f.read_text()
 if 'Typography correction only' in s:continue
 s=s.replace('</style>',css+'</style>',1).replace('<span>→ ','<span>'+arrow+' ').replace('<b>✓</b>','<b>'+check+'</b>')
 f.write_text(s)
