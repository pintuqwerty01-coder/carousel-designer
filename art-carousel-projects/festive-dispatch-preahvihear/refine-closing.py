from pathlib import Path
p=Path(__file__).resolve().parent
common='''
/* Closing sequence: shared ink foundation, white cards, restrained aqua accents. */
.slide {background:#1A1A1A!important;color:#FFFFFF;}
.slide .handle,.slide .count {color:#FFFFFF!important;}
.photo-h {top:188px;color:#FFFFFF;}
.photo-h em {color:#04ADC3;}
.closing-rule {position:absolute;left:84px;right:84px;top:155px;height:2px;background:rgba(255,255,255,.18);}
.closing-rule:before {content:"";display:block;width:96px;height:4px;background:#04ADC3;transform:translateY(-1px);}
'''
styles={
7:''' .photo-h{font-size:49px}.reveal-body{color:#DEDEDE;top:390px}.reveal-body .em{color:#04ADC3;background:none;padding:0}.reveal-sign{color:white;top:727px}.system-rail{border:1px solid rgba(255,255,255,.24);border-radius:28px;background:#FFFFFF;top:914px}.node{border-radius:24px;box-shadow:none;background:#FFFFFF;border:1px solid #DDF3F7}.orbital{background:#1A1A1A;border:8px solid #FFFFFF;box-shadow:none;border-radius:28px}.hub-lines{z-index:3}.hub-lines path{stroke:#04ADC3;stroke-width:3;stroke-dasharray:none}.system-rail{z-index:2}.orbital{z-index:4}.mascot{z-index:5}.node:nth-child(1){top:34px}.node:nth-child(4){top:34px}.logo{top:54px}''',
8:''' .photo-h{font-size:68px}.benefits{top:380px}.benefit,.benefit:nth-child(even){width:912px;margin-left:0;background:#FFFFFF;border-radius:28px;height:126px;margin-bottom:20px;border-left:6px solid #04ADC3}.benefit p,.benefit:nth-child(even) p{color:#1A1A1A;left:148px;top:40px;font-size:30px}.benefit svg{background:#FFFFFF;border-radius:20px;width:86px;height:86px}.benefits:before{display:none}.summary-end{top:1028px;color:#FFFFFF;width:650px;border-left:4px solid #04ADC3;font-size:29px;padding-left:24px}.mascot{top:946px!important}''',
9:''' .photo-h{font-size:68px}.cta-body{top:369px;color:#DEDEDE;font-size:32px}.calendar{top:529px;left:94px;transform:rotate(-3deg);border-radius:28px;box-shadow:8px 10px 0 rgba(255,255,255,.16)}.calendar:before{background:#FFFFFF;border-bottom:6px solid #04ADC3;border-radius:28px 28px 0 0}.calendar svg circle{fill:#2B907F}.calendar svg>path{stroke:#FFFFFF}.cta-arrow{top:554px}.mascot{top:694px!important}.cta-dm{top:998px;background:#FFFFFF;color:#1A1A1A;border-radius:28px;border-left:6px solid #04ADC3;padding:24px;font-size:31px;line-height:1.4}.cta-save{top:1151px;font-size:24px}.save-icon{top:1155px}'''}
for n in (7,8,9):
 f=p/f'slides/slide-{n:02d}.html';s=f.read_text()
 if 'Closing sequence: shared ink foundation' in s:continue
 s=s.replace('</style>',common+styles[n]+'</style>',1)
 s=s.replace('<div class="h-display photo-h">','<div class="closing-rule"></div><div class="h-display photo-h">',1)
 if n==7:
  s=s.replace('false, true); TRX.restore();','true, false); TRX.restore();')
  s=s.replace('M96 95Q240 10 456 135M246 220L456 135M666 220L456 135M816 95Q680 10 456 135','M148 95Q240 10 456 135M308 220L456 135M606 220L456 135M762 95Q680 10 456 135')
 if n==8:s=s.replace('</style>', '.benefit p .copy-symbol svg{width:100%;height:100%;background:none;border-radius:0;padding:0}</style>',1)
 f.write_text(s)
