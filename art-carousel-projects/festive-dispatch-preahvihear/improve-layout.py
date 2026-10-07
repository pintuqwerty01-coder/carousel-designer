from pathlib import Path
import html,json,re
p=Path(__file__).resolve().parent
content=json.loads((p/'content.json').read_text())
def rich(t):return re.sub(r'\*\*(.*?)\*\*',r'<em>\1</em>',html.escape(t))
styles={
1:''' .cover-h{font-size:80px;line-height:1.12;letter-spacing:-.015em}.cover-sub{top:386px;font-size:39px;line-height:1.35}.cover-note{top:530px;font-size:30px;line-height:1.4}.cover-cta{top:1100px;font-size:30px;padding:24px 28px;line-height:1.35}''',
2:''' .photo-h{top:80px;font-size:68px;line-height:1.14}.photo-pain{top:288px;font-size:30px;line-height:1.4}.setup-next{top:997px;font-size:28px;padding:20px 28px}.setup-topics{top:1103px;display:flex;align-items:center;justify-content:space-between;gap:12px;font-size:26px;line-height:1.45;padding:22px 24px}.setup-topic{white-space:nowrap}.topic-number{color:#04ADC3}''',
7:''' .photo-h{top:188px;font-size:54px;line-height:1.12}.reveal-body{top:408px;font-size:30px;line-height:1.4}.reveal-intro{display:block;margin-bottom:16px}.reveal-ease{top:678px;font-size:32px;line-height:1.4}.reveal-sign{top:756px;font-size:25px;line-height:1.4}.scene-word{top:849px;font-size:100px}''',
8:''' .photo-h{top:188px;font-size:62px;line-height:1.12}.benefits{top:380px}.benefit{height:118px;margin-bottom:18px}.summary-end{top:976px;font-size:31px;line-height:1.4;width:650px}.mascot{top:916px!important}''',
9:''' .photo-h{top:188px;font-size:66px;line-height:1.12}.cta-body{top:372px;font-size:31px;line-height:1.4}.calendar{top:504px;left:94px;transform:rotate(-3deg) scale(.87);transform-origin:top left}.cta-arrow{top:526px}.mascot{top:624px!important}.cta-dm{top:942px;font-size:30px;line-height:1.4;padding:24px}.cta-save{top:1104px;font-size:24px;line-height:1.4}.save-icon{top:1108px;width:24px;height:32px}.engagement{top:1168px;font-size:23px;line-height:1.4}'''}
task=''' .photo-h{top:108px;font-size:64px;line-height:1.14}.photo-pain{top:286px;font-size:30px;line-height:1.4}.header{--fade-start:374px}.photo-whatif{top:auto;bottom:268px;font-size:29px;line-height:1.35;padding:24px 26px;border-radius:28px}.photo-result{top:1110px;min-height:74px;font-size:26px;line-height:1.35;padding:18px 24px;border-radius:24px;display:block}.photo-result .copy-symbol{vertical-align:middle}.photo-result .copy-symbol.separator-dot{margin:0 9px}'''
for n in range(1,10):
 f=p/f'slides/slide-{n:02d}.html';s=f.read_text()
 if 'Placement refinement for revised script' in s:continue
 if n in (3,4,5,6,8,9):
  h=rich(content['slides'][n-1]['copy'][0]).replace('<em>','<br><em>',1)
  s,count=re.subn(r'(<div class="h-display photo-h">).*?</div>',lambda m:m[1]+h+'</div>',s,count=1,flags=re.S);assert count==1
 if n==2:
  dot='<span class="copy-symbol separator-dot"><span class="source-symbol">·</span><svg aria-hidden="true" viewBox="0 0 4 4"><circle cx="2" cy="2" r="1.6" fill="currentColor"/></svg></span>'
  topics=(' '+dot+' ').join(f'<span class="setup-topic"><span class="topic-number">{i}</span> {label}</span>' for i,label in enumerate(['Orders','Stock','Paperwork','Dispatch'],1))
  s,count=re.subn(r'(<div class="setup-topics">).*?</div>',lambda m:m[1]+topics+'</div>',s,count=1,flags=re.S);assert count==1
 if n==7:
  body=rich(content['slides'][6]['copy'][1]);intro,rest=body.split(' comes in.',1)
  body='<span class="reveal-intro">'+intro+' comes in.</span>'+rest
  s,count=re.subn(r'(<div class="reveal-body">).*?</div>',lambda m:m[1]+body+'</div>',s,count=1,flags=re.S);assert count==1
 css=task if n in (3,4,5,6) else styles[n]
 if n==5:css+=' .scene-word{top:356px;font-size:92px}'
 s=s.replace('</style>','\n/* Placement refinement for revised script */\n'+css+'</style>',1);f.write_text(s)
print('Refined heading wraps, text grouping, spacing and final-slide hierarchy')
