from pathlib import Path
import html,json,re
p=Path(__file__).resolve().parent
slides=[
["**FESTIVE SEASON ORDERS** ARE COMING.","Your dispatch already keeps up. What if it got even simpler?","Festive orders don't wait for anyone.","**Swipe to see where the rush usually breaks.**"],
["More orders. Same team. **Same system?**","Cashew, sweets and gifting orders pile up before the festive season, and the rush tends to crack in four places.","HERE'S WHERE ↓","1 Orders · 2 Stock · 3 Paperwork · 4 Dispatch"],
["Orders buried in **multiple places?**","One gets lost in the scroll, and you hear about it when the customer calls.","What if every order, from every channel, landed in one place?","✓ No order missed · ✓ No festive sale lost"],
["Ran out of your **best-seller** mid-rush?","In peak season, stock moves faster than anyone can count.","How about a reorder drafted before it runs low, waiting for your OK?","✓ Stock that keeps up · ✓ No sales turned away"],
["Invoices and e-way bills **stacking up?**","One wrong detail can hold a consignment back.","What if every document was checked against the order before the goods left?","✓ Fewer errors · ✓ Goods leave on time"],
['"Where\'s my order?" calls **piling up?**',"In festive season, a late delivery can cost you a customer for the year.","Imagine delays flagged the moment they happen, and customers updated before they ask.","✓ Fewer calls · ✓ Customers who come back"],
["Your business already runs the rush **like clockwork.** What if it took even less effort?","That's where **ART (A Realtime Tech)** comes in. Aiotrix's Governed Automation Platform sits on top of the systems you already use and keeps every order, shelf, invoice and delivery in step, in real time. You decide what it runs on its own.","Even more ease, this festive season.","From our team in Mangaluru to yours: here's to your best festive season yet 🪔"],
["This festive season, **everything moves seamlessly.**","✓ Every order captured","✓ Stock that keeps up","✓ Paperwork right the first time","✓ Customers kept in the loop","And a team that spends the rush with its customers."],
["The festive season is only **weeks away.**","The best time to get ready for the rush is before it starts.","DM us to see how ART could fit your business this season.","Save this and share it with whoever runs your dispatch.","♥ Like the post · 💬 Leave a comment · 🔖 Save & share it"]]
notes={2:{'background_word':'FESTIVE RUSH','orientation':'vertical'},5:{'background_word':'PAPERWORK'},7:{'background_word':'CLOCKWORK','clock_hands':'Sweep beside unchanged original ART logo; PDF shows still, MP4 shows motion.'}}
content={'status':'COPY UPDATED — user supplied script; design proof for review','handle':'@arealtimetech','typography':'Preahvihear throughout','slides':[{'number':n,'copy':copy,**({'design_notes':notes[n]} if n in notes else {})} for n,copy in enumerate(slides,1)]}
(p/'content.json').write_text(json.dumps(content,indent=2,ensure_ascii=False)+'\n')
def symbol(char,paths):
 return '<span class="copy-symbol"><span class="source-symbol">'+char+'</span><svg aria-hidden="true" viewBox="0 0 24 24">'+paths+'</svg></span>'
check=symbol('✓','<path d="m4 12 5 5 11-12" fill="none" stroke="#2B907F" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>')
down=symbol('↓','<path d="M12 3v18m-7-7 7 7 7-7" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>')
lamp=symbol('🪔','<path d="M3 14q9 13 18 0z" fill="#FFD166"/><path d="M12 14q-6-4 0-12 6 8 0 12z" fill="#F27A7A"/>')
heart=symbol('♥','<path d="M12 21 3 12C-4 3 7-2 12 6 17-2 28 3 21 12z" fill="#F27A7A"/>')
chat=symbol('💬','<path d="M3 3h18v14H10l-6 5v-5H3z" fill="none" stroke="#FFFFFF" stroke-width="2" stroke-linejoin="round"/><path d="M7 7h10M7 12h7" fill="none" stroke="#FFFFFF" stroke-width="2"/>')
dot=symbol('·','<circle cx="12" cy="12" r="9.6" fill="currentColor"/>').replace('class="copy-symbol"','class="copy-symbol separator-dot"')
save=symbol('🔖','<path d="M5 3h14v19l-7-5-7 5z" fill="none" stroke="#04ADC3" stroke-width="2" stroke-linejoin="round"/>')
def rich(text):
 text=html.escape(text)
 text=re.sub(r'\*\*(.*?)\*\*',r'<em>\1</em>',text)
 for a,b in [('✓',check),('↓',down),('🪔',lamp),('♥',heart),('💬',chat),('🔖',save),('·',dot)]:text=text.replace(a,b)
 return text
common='''
/* Revised user content, keeping approved visual identity and Preahvihear. */
.scene-word{position:absolute;left:84px;right:84px;top:810px;font-size:104px;line-height:1;color:white;opacity:.12;letter-spacing:3px;pointer-events:none;white-space:nowrap;z-index:1;}
.scene-word.vertical{top:444px;left:84px;right:auto;width:88px;height:520px;writing-mode:vertical-rl;transform:rotate(180deg);width:130px;line-height:1.8;font-size:72px;opacity:.42;text-shadow:0 2px 10px rgba(0,0,0,.4);}
.copy-symbol.separator-dot,.engagement .copy-symbol.separator-dot{width:4px;height:4px;margin:0 4px;vertical-align:middle}
.photo-result{gap:0;}
.photo-result .copy-symbol{margin-right:7px;}
.photo-result .copy-symbol svg{width:100%;height:100%;}
.cover-h{font-size:68px;line-height:1.12;}
.cover-sub{top:365px;font-size:40px;line-height:1.35;}
.cover-note{position:absolute;left:84px;right:84px;top:518px;color:white;font-size:30px;line-height:1.4;}
.cover-cta{font-size:29px;}
.setup-next{top:997px;font-size:27px;}
.setup-topics{position:absolute;left:84px;right:84px;top:1104px;padding:20px 24px;color:#FFFFFF;background:rgba(26,26,26,.85);border:1px solid rgba(255,255,255,.3);border-radius:24px;font-size:25px;line-height:1.45;}
.reveal-body em{color:#04ADC3;}
.reveal-ease{position:absolute;left:84px;right:84px;top:680px;font-size:28px;line-height:1.4;color:#04ADC3;}
.reveal-sign{top:747px;}
.brand-clock{position:absolute;right:84px;top:54px;width:82px;height:82px;}
.brand-clock .hand{transform-origin:40px 40px;}
.engagement{position:absolute;left:84px;right:84px;top:1174px;display:flex;justify-content:space-between;align-items:center;font-size:20px;line-height:1.4;color:white;gap:10px;}
.engagement .copy-symbol{width:23px;height:23px;margin-right:7px;vertical-align:-5px;}
'''
for n,copy in enumerate(slides,1):
 f=p/f'slides/slide-{n:02d}.html';s=f.read_text()
 def block(cls,text):
  global s
  s,count=re.subn(r'(<div class="'+re.escape(cls)+r'">).*?</div>',lambda m:m[1]+text+'</div>',s,count=1,flags=re.S)
  assert count==1,(n,cls)
 if n==1:
  block('cover-h','<em>FESTIVE SEASON<br>ORDERS</em><br>ARE COMING.')
  block('cover-sub',rich(copy[1]));block('cover-cta',rich(copy[3]))
  if 'class="cover-note"' not in s:s=s.replace('<div class="cover-cta">','<div class="cover-note">'+rich(copy[2])+'</div><div class="cover-cta">',1)
 elif n<=6:
  block('h-display photo-h',rich(copy[0]));block('photo-pain',rich(copy[1]))
  if n==2:
   block('setup-next',rich(copy[2]))
   if 'class="setup-topics"' not in s:s=s.replace('\n    <div class="handle">','<div class="setup-topics">'+rich(copy[3])+'</div>\n    <div class="handle">',1)
  else:
   block('photo-whatif',rich(copy[2]));block('photo-result',rich(copy[3]))
 elif n==7:
  block('h-display photo-h',rich(copy[0]));block('reveal-body',rich(copy[1]));block('reveal-sign',rich(copy[3]))
  if 'class="reveal-ease"' not in s:s=s.replace('<div class="reveal-sign">','<div class="reveal-ease">'+rich(copy[2])+'</div><div class="reveal-sign">',1)
  clock='<svg class="brand-clock" viewBox="0 0 80 80"><circle cx="40" cy="40" r="34" fill="none" stroke="#04ADC3" stroke-width="2"/><path d="M40 10v4M70 40h-4M40 70v-4M10 40h4" stroke="white" stroke-width="2"/><path class="hand hour-hand" d="M40 40V21" fill="none" stroke="white" stroke-width="4" stroke-linecap="round"/><path class="hand minute-hand" d="M40 40V12" fill="none" stroke="#04ADC3" stroke-width="2" stroke-linecap="round"/><circle cx="40" cy="40" r="3" fill="white"/></svg>'
  if 'class="brand-clock"' not in s:s=s.replace('<img class="logo"',clock+'<img class="logo"',1)
  if 'tl.to(".minute-hand"' not in s:s=s.replace('document.fonts.load(', 'tl.to(".minute-hand",{svgOrigin:"40 40",rotation:360,duration:4,ease:"none"},0);tl.to(".hour-hand",{svgOrigin:"40 40",rotation:30,duration:4,ease:"none"},0);\ndocument.fonts.load(',1)
 elif n==8:
  block('h-display photo-h',rich(copy[0]));block('col summary-end',rich(copy[5]))
  texts=iter(copy[1:5]);s,count=re.subn(r'<p>.*?</p>',lambda m:'<p>'+rich(next(texts))+'</p>',s,flags=re.S);assert count==4
 else:
  block('h-display photo-h',rich(copy[0]));block('cta-body',rich(copy[1]));block('cta-dm',rich(copy[2]));block('col cta-save',rich(copy[3]))
  if 'class="engagement"' not in s:
   # Keep the literal middot separators in the supplied line.
   items=[rich(t) for t in copy[4].split(' · ')]
   s=s.replace('\n    <div class="handle">','<div class="engagement">'+(' '+dot+' ').join('<span>'+t+'</span>' for t in items)+'</div>\n    <div class="handle">',1)
 extra={5:'.photo-pain{top:274px}.header{--fade-start:330px}.scene-word{top:350px;font-size:96px;opacity:.3;text-shadow:0 2px 10px rgba(0,0,0,.4)}',7:'.scene-word{top:839px;font-size:106px;opacity:.065;z-index:0}',8:'.photo-h{font-size:62px;line-height:1.12}.benefits{top:412px}.benefit{height:118px;margin-bottom:18px}.benefit p{top:35px}.mascot{top:946px!important}.summary-end{top:1034px}',9:'.cta-dm{top:982px;padding:20px 24px;font-size:29px;line-height:1.4}.cta-save{top:1117px;font-size:22px;line-height:1.4}.save-icon{top:1119px;height:30px;width:22px}'}
 if 'Revised user content, keeping' not in s:s=s.replace('</style>',common+extra.get(n,'')+'</style>',1)
 if n in notes and 'class="scene-word' not in s:
  cls='scene-word vertical' if n==2 else 'scene-word'
  s=s.replace('\n    <div class="handle">','<div class="'+cls+'">'+notes[n]['background_word']+'</div>\n    <div class="handle">',1)
 f.write_text(s)
print('Updated all nine slides from exact user-supplied content')
