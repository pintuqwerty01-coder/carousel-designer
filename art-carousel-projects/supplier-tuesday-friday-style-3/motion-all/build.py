from pathlib import Path
import json,shutil
P=Path(__file__).resolve().parent.parent; M=P/'motion-all'; data=json.loads((M/'alignment-analysis.json').read_text())
pivots={1:(700,830),2:(652,862),3:(548,987),5:(565,935),6:(838,924),7:(693,857),8:(674,816)}
keys={1:[[0,0],[.7,0],[1.5,-8],[2.1,-8],[2.8,0],[7,0]],2:[[0,0],[.8,0],[1.7,-10],[2,-10],[2.6,0],[7,0]],3:[[0,-7],[.8,-7],[2.4,7],[3.2,0],[7,0]],5:[[0,0],[.9,0],[1.2,-3],[1.5,2],[1.8,-2],[2.1,1],[2.5,0],[7,0]],6:[[0,-5],[.7,-5],[2.2,0],[7,0]],7:[[0,5],[1.2,5],[2.5,0],[7,0]],8:[[0,0],[.8,0],[1.8,7],[2.2,7],[2.8,0],[7,0]]}
for ns,d in data.items():
 n=int(ns); nn=f'{n:02}'; source=(P/f'slides/slide-{nn}.html').read_text();source=source.replace('<head>','<head><base href="../../slides/">').replace(f'assets/scene-{nn}.png',f'../motion-all/assets/{nn}-plate.png')
 for state in ['prep','ready','final']:
  hide='' if state=='final' else '.scene-label,.results,.brand-cta{visibility:hidden!important}'
  if n==1 and state=='prep':hide+='.record em{visibility:hidden!important}'
  if n==5 and state=='prep':hide+='.tablet-note p{visibility:hidden!important}'
  if n==6 and state!='final':hide+='.headline span:last-child{visibility:hidden!important}'
  (M/f'states/{nn}-{state}.html').write_text(source.replace('</head>',f'<style>{hide}</style></head>'))
 w,h=d['source_size'];pw,ph=d['part_size'];s=max(1080/w,1350/h);cx=(w*s-1080)/2;cy=(h*s-1350)/2;A=d['affine_native'];a,c,x=A[0];b,e,y=A[1];matrix=[s*a,s*b,s*c,s*e,s*x-cx,s*y-cy];px,py=pivots[n];px=px*s-cx;py=py*s-cy;bx,by,bw,bh=d['part_bbox'];clip=f'inset({max(0,by-8)}px {max(0,pw-bx-bw-8)}px {max(0,ph-by-bh-8)}px {max(0,bx-8)}px)'
 ready={1:1.6,5:2.6}.get(n,.7);final={3:3.2,5:3,6:2.6,7:2.7}.get(n,2.8)
 html='''<!doctype html><html><head><meta charset="utf-8"><style>*{margin:0;padding:0}html,body{width:1080px;height:1350px;overflow:hidden;background:#1a1a1a}.state{position:absolute;inset:0;width:1080px;height:1350px}#ready,#final{opacity:0}#part{position:absolute;inset:0;transform-origin:PIVOT}#part img{position:absolute;left:0;top:0;width:PWpx;height:PHpx;transform-origin:0 0;transform:matrix(MATRIX);clip-path:CLIP}</style></head><body><img class="state" src="assets/NN-prep.png"><img class="state" id="ready" src="assets/NN-ready.png"><img class="state" id="final" src="assets/NN-final.png"><div id="part"><img src="assets/NN-part.png"></div><script>const keys=KEYS;const ease=x=>{x=Math.max(0,Math.min(1,x));return x*x*(3-2*x)};window.setTime=t=>{ready.style.opacity=ease((t-READY)/.4);document.getElementById('final').style.opacity=ease((t-FINAL)/.5);let a=keys.at(-1)[1];for(let i=1;i<keys.length;i++){if(t<=keys[i][0]){let [t0,a0]=keys[i-1],[t1,a1]=keys[i];a=a0+(a1-a0)*ease((t-t0)/(t1-t0));break}}part.style.transform=`rotate(${a}deg)`};setTime(0);let start;function play(ms){start??=ms;setTime(Math.min(7,(ms-start)/1000));if(ms-start<7000)requestAnimationFrame(play)}if(!location.search.includes('capture'))requestAnimationFrame(play);</script></body></html>'''
 for k,v in {'PIVOT':f'{px}px {py}px','PW':str(pw),'PH':str(ph),'MATRIX':','.join(map(str,matrix)),'CLIP':clip,'NN':nn,'KEYS':json.dumps(keys[n]),'READY':str(ready),'FINAL':str(final)}.items():html=html.replace(k,v)
 (M/f'slide-{nn}.html').write_text(html)
shutil.copyfile(P/'delivery-v6/ART-supplier-delay-style3-full-v6.pdf',M/'delivery/ART-supplier-delay-approved-static.pdf')
