from pathlib import Path
import json,re,html
V=Path(__file__).resolve().parent;P=V.parent
H=[['Supplier said Tuesday.',"It's Friday.","ART's on it."],['One late delivery.','A whole team waiting.'],['ART spots',"what's overdue."],['"Any update?"','Already sent.'],['When a reply comes in,','ART updates the record.'],['No reply yet?','ART flags the delay.'],['ART brings the details.',"You decide what's next."],['Keep work moving.','Let ART do the chasing.']]
B=[['ART (A Realtime Tech) follows up','on overdue deliveries.'],['A missing shipment can leave','the next job waiting to start.'],['ART checks the promised delivery date','against what has actually arrived.'],['ART asks the supplier','for a revised delivery date.'],["ART records the supplier's response",'and updates the delivery status.'],['ART alerts your team and shows','which work is waiting on the shipment.'],['Wait, escalate or explore another supplier.','Your team has the details to decide.'],['ART (A Realtime Tech) handles delivery follow-ups','so your team can focus on the work ahead.']]
Q=["Your team shouldn't have to chase.",'The impact goes beyond the delivery.','Check what was due against what arrived.','Ask for a date. Keep track of the reply.','Keep the reply with the delivery record.','Bring unresolved delays to your team.','You choose the next step.','Put ART to work.']
L=['ART follows up while your team gets on with work.','The receiving tray is empty. The next job waits.','The receiving record shows what is still missing.','The follow-up is sent. ART now tracks the reply.','The supplier’s reply stays with the delivery record.','No reply yet. Your team can see what is held up.','The handover includes the details your team needs.','Less chasing. More time for your team.']
R=[['ART spots the overdue delivery.','ART handles the follow-up.'],['The shipment is late.','The next job is waiting.'],['The delivery date has passed.','The shipment has not arrived.'],['A new date has been requested.','The supplier has not replied yet.'],['The supplier’s reply is recorded.','The delivery status is updated.'],['Your team is alerted.','The affected work is highlighted.'],['The delivery details are together.','Your team decides the next step.'],[]]
scenes=['Mascot points to Tuesday/Friday overdue record.','Empty receiving tray and concerned mascot show the next job waiting.','Magnifier and receiving records support the overdue check.','Mascot sends follow-up on phone; reply remains pending.','Stylus/tablet illustrate the conditional reply-recording branch.','Raised flag and waiting folder illustrate the no-reply escalation branch.','Folder handover illustrates context passed to a human decision-maker.','Relaxed mascot beside correspondence folders supports relief from follow-ups.']
slides=[]
for i in range(8):
 H[i]=[x.replace('’',chr(39)) for x in H[i]];B[i]=[x.replace('’',chr(39)) for x in B[i]];Q[i]=Q[i].replace('’',chr(39));L[i]=L[i].replace('’',chr(39));R[i]=[x.replace('’',chr(39)) for x in R[i]]
 n=i+1;s=(P/f'slides/slide-{n:02}.html').read_text().replace('<head>','<head><base href="../../slides/">',1)
 s=re.sub(r'(<h1 class="headline">).*?(</h1>)',lambda m:m[1]+''.join('<span>'+html.escape(x)+'</span>' for x in H[i])+m[2],s,count=1)
 for cls,val in [('body','<br>'.join(map(html.escape,B[i]))),('prompt',html.escape(Q[i])),('scene-label',html.escape(L[i]))]:
  s=re.sub(r'(<p class="'+cls+r'">).*?(</p>)',lambda m:m[1]+val+m[2],s,count=1)
 if n<8:
  it=iter(R[i]);s=re.sub(r'(<p class="result"><svg.*?</svg>).*?(</p>)',lambda m:m[1]+html.escape(next(it))+m[2],s)
 if n==5:s=s.replace('Response<br>tracked','Reply<br>recorded')
 # Keep existing visual assets and font sizes; adjust only the closing body line split if necessary.
 (V/f'slides/slide-{n:02}.html').write_text(s)
 slides.append(dict(slide=n,headline=H[i],body=B[i],prompt=Q[i],scene_label=L[i],results=R[i],visual_logic=scenes[i]))
(V/'content.json').write_text(json.dumps(dict(topic="Supplier said Tuesday. It's Friday.",status='Static v7 copy and scene consistency review; awaiting user review',slides=slides),indent=2,ensure_ascii=False)+'\n')
