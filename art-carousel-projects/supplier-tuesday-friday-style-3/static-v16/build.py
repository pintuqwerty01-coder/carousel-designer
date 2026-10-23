from pathlib import Path
import json,re,html
P=Path(__file__).resolve().parent.parent;V=Path(__file__).resolve().parent;old=P/'static-v15'
for d in ['slides','proof','delivery']:(V/d).mkdir(exist_ok=True)
d=json.loads((old/'content.json').read_text());slides=d['slides'];slides[0]['headline']=['Supplier said Tuesday.',"It's Friday."];slides[0]['body']=['The promised date has passed.','Your stock and your team are still waiting.'];slides[0]['prop_copy']=slides[0]['prop_copy'][:-1]
intro=dict(slide=2,headline=['Meet ART.','Your supplier','follow-through agent.'],body=['ART (A Realtime Tech) follows up with suppliers,','spots delivery risks and helps','coordinate the next move.'],prompt=None,scene_label=None,results=[],rules=[],cta=None,photo='../static-v9/assets/scene-05.png')
slides.insert(1,intro);slides[-1]['cta']='DM "DELIVERY" to discuss your supplier workflow.'
for n,s in enumerate(slides,1):
 s['slide']=n;source=1 if n<=2 else n-1;t=(old/f'slides/slide-{source:02}.html').read_text()
 headline=''.join('<span class="'+('em' if i==len(s['headline'])-1 else '')+'">'+html.escape(x)+'</span>' for i,x in enumerate(s['headline']))
 t=re.sub(r'<h1 class="headline">.*?</h1>','<h1 class="headline">'+headline+'</h1>',t,flags=re.S)
 t=re.sub(r'<p class="body">.*?</p>','<p class="body">'+'<br>'.join(html.escape(x) for x in s['body'])+'</p>',t,flags=re.S)
 t=re.sub(r'<span>\d\d / 06</span>',f'<span>{n:02} / 07</span>',t)
 t=re.sub(r'<div class="trail">.*?</div>','<div class="trail">'+''.join('<i class="'+('on' if i<n else '')+'"></i>' for i in range(7))+'</div>',t)
 if n==1:
  t=t.replace('<p class="pad-action">ART following up</p>','');t=t.replace('</style>','.cover .headline{font-size:76px}.cover .body{font-size:34px}</style>')
 if n==2:
  t=t.replace('../static-v9/assets/scene-01.png',s['photo']);t=re.sub(r'<div class="prop-text record pad-redesign">.*?</div><footer', '<footer',t,flags=re.S)
  t=t.replace('</style>','.cover .headline{font-size:65px;line-height:1.15}.cover .body{font-size:31px;line-height:1.4}.cover .copy{top:84px}</style>')
 if n==7:
  t=t.replace('Talk to us about your supplier workflow.',html.escape(s['cta']))
  t=t.replace('</style>','.brand-header{background:transparent!important;box-shadow:none!important}.brand-header .brand-logo path[transform^="matrix(1,0,0,-1,250.92774"]{fill:#fff!important}.brand-cta{background:#fff}.brand-cta span{max-width:none!important;font-size:29px!important}</style>')
 (V/f'slides/slide-{n:02}.html').write_text(t)
d['topic']="Supplier said Tuesday. It's Friday.";d['status']='Static v16 review: pain-first cover, ART introduction, transparent blue-white closing logo and DM CTA';(V/'content.json').write_text(json.dumps(d,indent=2)+'\n')
r=(old/'render.py').read_text().replace('static-v15','static-v16').replace('-v15','-v16').replace('if n in [1,2]:',"if s.get('prop_copy'):").replace('if n==2:','if n==3:').replace('if n==6:','if n==7:').replace('if n==4:','if n==5:').replace('range(1,7)','range(1,8)').replace('(1620,1350)','(2160,1350)').replace('range(6)','range(7)').replace('(i%3)','(i%4)').replace('(i//3)','(i//4)')
(V/'render.py').write_text(r)
