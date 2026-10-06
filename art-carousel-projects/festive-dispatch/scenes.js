// Festive dispatch v2: original choreographies for this order's journey.
// Props move smoothly; the 240px robot uses stepped poses throughout.
const FST = {
 k(t,a,b){return eInOut(Math.max(0,Math.min(1,(t-a)/(b-a))));},
 box(c,x,y,w=64,h=54){c.fillStyle='#DDF3F7';c.strokeStyle='#1A1A1A';c.lineWidth=3;c.beginPath();c.roundRect(x,y,w,h,5);c.fill();c.stroke();c.strokeStyle='#04ADC3';c.beginPath();c.moveTo(x+w/2,y);c.lineTo(x+w/2,y+h);c.moveTo(x,y+15);c.lineTo(x+w,y+15);c.stroke();},
 paper(c,x,y,bad=false){c.fillStyle='#FFFFFF';c.strokeStyle='#1A1A1A';c.lineWidth=2.5;c.beginPath();c.roundRect(x,y,44,58,4);c.fill();c.stroke();c.strokeStyle=bad?'#F27A7A':'#04ADC3';c.beginPath();for(let j=0;j<3;j++){c.moveTo(x+9,y+14+j*10);c.lineTo(x+35,y+14+j*10);}c.stroke();},
 belt(c,x,y,w){c.fillStyle='#DDF3F7';c.strokeStyle='#1A1A1A';c.lineWidth=3;c.beginPath();c.roundRect(x,y,w,30,12);c.fill();c.stroke();for(let q=x+14;q<x+w;q+=34){c.beginPath();c.arc(q,y+15,5,0,Math.PI*2);c.stroke();}},
 bot(c,x,y,S,pose,u=8){x=snap(x);y=snap(y);vShadow(c,x+12*u,y+23*u+7,15*u,0,u===10);drawBot(c,x,y,u,pose);},
 link(c,x,y,xx,yy){c.strokeStyle='#04ADC3';c.lineWidth=3;c.beginPath();c.moveTo(x,y);c.lineTo(xx,yy);c.stroke();}
};
Object.assign(SCENES_DYN,{
 // Setup: the robot tries to drag a parcel train; an obstruction makes it skid back.
 festiveSetup(c,t,S){
  FST.belt(c,328,286,368);
  const jam=FST.k(t,.2,1.7), recoil=FST.k(t,1.8,2.3);
  const bx=lerp(44,112,jam)-recoil*28;
  FST.link(c,bx+168,258,354,258);
  [0,1,2,3].forEach(i=>FST.box(c,354+i*78,225+(i%2)*5,64,54));
  c.fillStyle='#F27A7A';c.fillRect(681,205,10,80);vMark(c,660,167,'!',(t-1.7)/.3,'bang',1);
  FST.bot(c,bx,VY,S,{legs:S<14?walkLegs(S):'stand',armR:'reach',armL:S<16?'out':'up',eyes:S<16?'focus':'wide',mouth:S<16?'flat':'o',bulb:S<16?'yellow':'red'});
  if(S>=16)vSweat(c,bx+160,VY+48,t,1);
 },
 // Orders: catch scattered order slips with a basket, then lower them into one rack.
 festiveOrders(c,t,S){
  c.fillStyle='#DDF3F7';c.strokeStyle='#1A1A1A';c.lineWidth=3;c.beginPath();c.roundRect(480,230,210,78,10);c.fill();c.stroke();
  const bx=S<12?lerp(48,164,S/11):S<23?lerp(164,292,(S-12)/10):292;
  const by=S<12?VY-Math.sin(S/11*Math.PI)*20:VY;
  FST.bot(c,bx,by,S,{legs:S<23?walkLegs(S):'stand',armR:'reach',armL:S<12?'up':'down',eyes:S<12?'wide':S<24?'focus':'happy',mouth:S<12?'o':S<24?'flat':'grin',bulb:S<12?'red':S<24?'yellow':'aqua'});
  const basketX=snap(bx)+174,basketY=by+126;
  c.fillStyle='#9BE3EC';c.beginPath();c.roundRect(basketX,basketY,64,45,8);c.fill();c.stroke();
  for(let i=0;i<3;i++){
   const fall=FST.k(t,.15+i*.23,1.25+i*.18),file=FST.k(t,2.1+i*.18,3.2+i*.13);
   const x=lerp(lerp(350+i*105,basketX+8,fall),500+i*58,file),y=lerp(lerp(20+i*12,basketY-44,fall),245,file);
   FST.paper(c,x,y);if(t>3.2+i*.13)vBadge(c,x+38,y-7,(t-3.2-i*.13)/.25);
  }
 },
 // Stock: measure a low shelf, offer a draft slip, pause at an approval gate, then receive stock.
 festiveStock(c,t,S){
  c.strokeStyle='#1A1A1A';c.lineWidth=5;c.strokeRect(448,55,244,240);FST.link(c,448,163,692,163);
  FST.box(c,462,106,54,54);
  const bx=S<10?lerp(76,240,S/9):240;
  FST.bot(c,bx,VY,S,{legs:S<10?walkLegs(S):'stand',armR:S<11?'reach':S<23?'hold':'up',eyes:S<10?'lookR':S<23?'focus':'happy',mouth:S<23?'flat':'grin',bulb:S<10?'red':S<23?'yellow':'aqua'});
  if(S<11){c.strokeStyle='#FFD166';c.lineWidth=7;c.beginPath();c.moveTo(snap(bx)+173,258);c.lineTo(452,258);c.stroke();}
  if(S>=11){FST.paper(c,414,245);if(S<23)vMark(c,420,208,'?',(t-1.35)/.3,'q',.7);else vBadge(c,452,240,(t-2.8)/.25);}
  // Replenishment starts only after the approval beat at 2.8 seconds.
  for(let i=0;i<3;i++){const k=FST.k(t,2.85+i*.12,3.55+i*.12);if(k>0)FST.box(c,462+i*72,lerp(-65,220,k),54,54);}
 },
 // Paperwork: pull a red mismatch off the conveyor, compare it, then release the corrected pack.
 festivePaperwork(c,t,S){
  FST.belt(c,354,283,346);
  const inK=FST.k(t,0,1.2),fix=FST.k(t,1.4,2.7),out=FST.k(t,2.8,3.8);
  FST.box(c,lerp(596,646,out),228,54,54);
  FST.paper(c,lerp(650,482,inK),lerp(220,194,fix),t<2.7);
  if(t<2.7)vMark(c,506,167,'!',(t-.8)/.3,'bang',.7);else vBadge(c,523,190,(t-2.7)/.25);
  const bx=S<10?lerp(80,276,S/9):S>23?lerp(276,320,(S-23)/8):276;
  FST.bot(c,bx,VY,S,{legs:S<10||S>23?walkLegs(S):'stand',armR:S<11?'up':S<23?'reach':'tap',armL:S>=11&&S<23?'out':'down',eyes:S<11?'wide':S<23?'focus':'happy',mouth:S<23?'flat':'smile',bulb:S<11?'red':S<23?'yellow':'aqua'});
  if(S>=11&&S<23)FST.paper(c,snap(bx)+10,240);
 },
 // Dispatch: stop a parcel at a delay flag, divert it to a clear route, send an envelope ahead.
 festiveDispatch(c,t,S){
  FST.link(c,354,268,680,268);FST.link(c,410,268,500,130);FST.link(c,500,130,680,130);
  c.fillStyle=t<2.1?'#F27A7A':'#04ADC3';c.fillRect(580,230,8,64);
  const turn=FST.k(t,1.6,2.6),leave=FST.k(t,2.6,3.8);
  FST.box(c,lerp(lerp(510,478,turn),650,leave),lerp(220,82,turn),48,48);
  const bx=S<10?lerp(100,240,S/9):240;
  FST.bot(c,bx,VY,S,{legs:S<10?walkLegs(S):'stand',armR:S<13?'up':S<23?'reach':'up',armL:S>=23?'up':'down',eyes:S<13?'wide':S<23?'lookR':'happy',mouth:S<13?'o':'smile',bulb:S<13?'red':S<23?'yellow':'aqua'});
  const send=FST.k(t,2.1,3.1);c.fillStyle='#FFFFFF';c.strokeStyle='#1A1A1A';c.lineWidth=2.5;const ex=lerp(426,652,send),ey=lerp(192,30,send);
  c.beginPath();c.roundRect(ex,ey,44,28,4);c.fill();c.stroke();c.beginPath();c.moveTo(ex,ey);c.lineTo(ex+22,ey+16);c.lineTo(ex+44,ey);c.stroke();if(t>3.1)vBadge(c,690,32,(t-3.1)/.25);
 },
 // Reveal: a festive bow tied to the parcel, then a proud presenting pose; no library celebration.
 festiveReveal(c,t,S){
  const x=S<10?lerp(1100,730,S/9):730,y=966;
  FST.bot(c,x,y,S,{dark:true,halo:true,legs:S<10?walkLegs(S):'stand',armR:S<20?'reach':'up',armL:S<20?'out':'up',eyes:S<20?'focus':'happy',mouth:S<20?'flat':'grin',bulb:S<20?'yellow':'aqua'},10);
  const boxX=560;FST.box(c,boxX,1106,138,84);
  const k=FST.k(t,1.25,2.65);c.strokeStyle='#04ADC3';c.lineWidth=6;c.beginPath();c.moveTo(629,1106);c.lineTo(629,1190);c.stroke();
  c.beginPath();c.ellipse(629-25*k,1099,26*k,12*k,-.4,0,Math.PI*2);c.ellipse(629+25*k,1099,26*k,12*k,.4,0,Math.PI*2);c.stroke();
 },
 // Outcome: robot pushes a checked parcel smoothly down a clear conveyor and lets it go.
 festiveOutcome(c,t,S){
  FST.belt(c,318,282,382);[360,455,550,645].forEach((x,i)=>vBadge(c,x,75,(t-.3-i*.38)/.25));
  const k=FST.k(t,.6,3.6),bx=S<24?lerp(64,300,Math.min(1,S/23)):300;
  FST.bot(c,bx,VY,S,{legs:S<24?walkLegs(S):'stand',armR:S<24?'reach':'wave2',eyes:'happy',mouth:'smile',bulb:'aqua'});
  FST.box(c,lerp(258,646,k),224,54,54);if(t>2.7)vBadge(c,lerp(258,646,k)+47,218,(t-2.7)/.25);
 },
 // CTA: the robot folds a note into an envelope and presents it; no repeated waving loop.
 festiveCTA(c,t,S){
  FST.bot(c,24,42,S,{armR:S<12?'hold':S<24?'tap':'reach',armL:S<24?'out':'down',eyes:S<24?'focus':'lookR',mouth:S<24?'flat':'smile',bulb:S<24?'yellow':'aqua'},10);
  const k=FST.k(t,1.1,2.8),x=246,y=180;
  c.fillStyle='#FFFFFF';c.strokeStyle='#1A1A1A';c.lineWidth=3;c.beginPath();c.roundRect(x,y,82,lerp(65,46,k),5);c.fill();c.stroke();
  c.strokeStyle='#04ADC3';c.beginPath();c.moveTo(x,y);c.lineTo(x+41,y+lerp(5,26,k));c.lineTo(x+82,y);c.stroke();
 }
});
