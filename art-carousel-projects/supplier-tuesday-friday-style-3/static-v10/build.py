from pathlib import Path
import re,json,html
V=Path(__file__).resolve().parent;P=V.parent
H=[['Supplier said Tuesday.',"It's Friday.","ART's on it."],['One late delivery.','A whole team waiting.'],['ART checks first.','Then follows up.'],['"Any update?"','Already sent.'],['A supplier reply.','A clearer picture.'],["Silence shouldn't",'hide the hold-up.'],['ART brings the facts.','You make the call.'],['Your team has work to do.','Let ART do the chasing.']]
B=[['ART (A Realtime Tech) follows up','on overdue deliveries.'],['Hours meant for packing turn into','calls, reminders and "any updates?"'],['It compares the promised delivery date','with your receiving record.'],["Your team shouldn't need",'to write the same reminder again.'],['When the supplier responds,','ART keeps the update with the order.'],['If the supplier stays silent,','ART alerts your team.'],['Get the delivery details,','including any supplier response.'],['ART (A Realtime Tech) keeps supplier follow-ups',"off your team's to-do list."]]
R=[[],['Materials are still missing.','The packing line is on hold.'],['The due date has passed.','The shipment is still missing.'],[],['Revised date, if provided.','Latest delivery status.'],['See the overdue delivery.','See the work it is holding up.'],['Give the supplier more time.','Escalate or explore alternatives.'],[]]
slides=[]
for i in range(8):
 n=i+1;s=(P/f'static-v9/slides/slide-{n:02}.html').read_text()
 s=re.sub(r'(<h1 class="headline">).*?(</h1>)',lambda m:m[1]+''.join('<span>'+html.escape(x)+'</span>' for x in H[i])+m[2],s,count=1)
 s=re.sub(r'(<p class="body">).*?(</p>)',lambda m:m[1]+'<br>'.join(map(html.escape,B[i]))+m[2],s,count=1)
 s=re.sub(r'<p class="scene-label">.*?</p>','',s,count=1)
 if n==1:s=re.sub(r'(<p class="prompt">).*?(</p>)',lambda m:m[1]+'See what happens next.'+m[2],s,count=1)
 else:s=re.sub(r'<p class="prompt">.*?</p>','',s,count=1)
 if not R[i]:s=re.sub(r'<div class="results">.*?</div>','',s,count=1)
 else:
  it=iter(R[i]);s=re.sub(r'(<p class="result"><svg.*?</svg>).*?(</p>)',lambda m:m[1]+html.escape(next(it))+m[2],s)
 # These are inputs/options, not completed outcomes: replace completion ticks with neutral aqua bullets.
 s=re.sub(r'(<p class="result">)<svg.*?</svg>',r'\1<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4" fill="#04ADC3"/></svg>',s)
 (V/f'slides/slide-{n:02}.html').write_text(s)
 slides.append(dict(slide=n,headline=H[i],body=B[i],prompt='See what happens next.' if n==1 else None,scene_label=None,results=R[i],visual_logic=json.loads((P/'static-v9/content.json').read_text())['slides'][i]['visual_logic']))
(V/'content.json').write_text(json.dumps(dict(topic="Supplier said Tuesday. It's Friday.",status='Static v10 review: concise hooks and distinct copy roles; exact white-limb v9 scene images retained',slides=slides),indent=2)+'\n')
