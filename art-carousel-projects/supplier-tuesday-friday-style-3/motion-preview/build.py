from pathlib import Path
import shutil,re
P=Path(__file__).resolve().parent.parent;M=P/'motion-preview';A=M/'assets';S=M/'states'
for d in [A,S,M/'delivery',M/'proof']:d.mkdir(parents=True,exist_ok=True)
src=(P/'slides/slide-04.html').read_text().replace('<head>','<head><base href="../../slides/">',1).replace('src="assets/scene-04.png"','src="../motion-preview/assets/plate.png"')
for state in ['prep','ready','sent']:
 doc=src
 if state!='sent':
  doc=doc.replace('<span class="sent">Follow-up sent</span>','<div class="send-control">Send</div>')
  css='.headline span:last-child,.results,.scene-label{visibility:hidden}.send-control{display:block;width:166px;margin-top:6px;background:#04ADC3;color:#1A1A1A;border-radius:12px;padding:8px 14px;font-size:22px;line-height:1.3;text-align:center}'
  if state=='prep':css+='.phone-note p{color:transparent}.send-control{visibility:hidden}'
  doc=doc.replace('</style>',css+'</style>')
 (S/f'{state}.html').write_text(doc)
html='''<!doctype html><html><head><meta charset="utf-8"><style>*{margin:0;padding:0;box-sizing:border-box}html,body{width:1080px;height:1350px;overflow:hidden;background:#1A1A1A}.state{position:absolute;left:0;top:0;width:1080px;height:1350px}#ready,#sent{opacity:0}#arm{position:absolute;left:0;top:0;width:1080px;height:1350px;transform-origin:829px 778px;will-change:transform}#arm img{position:absolute;left:0;top:0;width:1122px;height:1402px;transform-origin:0 0;transform:matrix(.5891,.0216,-.0216,.5891,258,312);clip-path:inset(49% 6% 18% 28%)} </style></head><body><img class="state" src="assets/prep.png"><img class="state" id="ready" src="assets/ready.png"><img class="state" id="sent" src="assets/sent.png"><div id="arm"><img src="assets/arm.png"></div><script>
const ease=(x)=>{x=Math.max(0,Math.min(1,x));return x*x*(3-2*x)};
window.setTime=function(t){document.getElementById('ready').style.opacity=ease((t-.5)/.85);document.getElementById('sent').style.opacity=ease((t-2.55)/.45);let angle=-6;if(t>=1.95&&t<2.45)angle=-6*(1-ease((t-1.95)/.5));else if(t>=2.45&&t<2.7)angle=0;else if(t>=2.7&&t<3.25)angle=-6*ease((t-2.7)/.55);document.getElementById('arm').style.transform=`rotate(${angle}deg)`;};window.setTime(0);
let start=null;function play(ms){if(start===null)start=ms;setTime(Math.min(7,(ms-start)/1000));if(ms-start<7000)requestAnimationFrame(play)};if(!new URLSearchParams(location.search).has('capture'))requestAnimationFrame(play);
</script></body></html>'''
(M/'index.html').write_text(html)
print(M)
