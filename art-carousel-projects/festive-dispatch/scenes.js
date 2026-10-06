// Festive dispatch v3: one action per slide, fixed robot staging, restrained props.
// Timing: establish 0–1.0s; action 1.0–2.5s; resolve 2.5–3.0s; hold to 4.0s.
const FST = {
 k(t,a,b){const q=Math.max(0,Math.min(1,(t-a)/(b-a)));return q*q*(3-2*q);},
 box(c,x,y,w=76,h=64){c.fillStyle='#DDF3F7';c.strokeStyle='#1A1A1A';c.lineWidth=2.5;c.beginPath();c.roundRect(x,y,w,h,6);c.fill();c.stroke();c.strokeStyle='#04ADC3';c.beginPath();c.moveTo(x+w/2,y);c.lineTo(x+w/2,y+h);c.stroke();},
 paper(c,x,y,bad=false,w=64,h=76){c.fillStyle='#FFFFFF';c.strokeStyle='#1A1A1A';c.lineWidth=2.5;c.beginPath();c.roundRect(x,y,w,h,5);c.fill();c.stroke();c.strokeStyle=bad?'#F27A7A':'#04ADC3';c.beginPath();for(let j=0;j<3;j++){c.moveTo(x+12,y+20+j*13);c.lineTo(x+w-12,y+20+j*13);}c.stroke();},
 bot(c,x,y,u,pose){vShadow(c,x+12*u,y+23*u+5,14*u,0,!!pose.dark);drawBot(c,snap(x),snap(y),u,pose);},
 tick(c,x,y,t,start=2.6){const k=FST.k(t,start,start+.4);if(!k)return;c.save();c.globalAlpha=k;c.strokeStyle='#2B907F';c.lineWidth=5;c.lineCap='round';c.lineJoin='round';c.beginPath();c.moveTo(x-12,y);c.lineTo(x-3,y+9);c.lineTo(x+16,y-12);c.stroke();c.restore();},
 shelf(c){c.strokeStyle='#1A1A1A';c.lineWidth=3;c.beginPath();c.moveTo(446,148);c.lineTo(634,148);c.lineTo(634,292);c.lineTo(446,292);c.stroke();c.beginPath();c.moveTo(446,220);c.lineTo(634,220);c.stroke();}
};
Object.assign(SCENES_DYN,{
 // 02: More orders, same team — three parcels arrive; bot turns between the incoming queues.
 festiveSetup(c,t,S){
  const x=276;
  FST.box(c,lerp(-84,142,FST.k(t,.2,1.25)),250,72,62);
  FST.box(c,lerp(748,525,FST.k(t,.85,1.9)),250,72,62);
  FST.box(c,lerp(748,611,FST.k(t,1.55,2.65)),250,72,62);
  const left=S<12,panicked=S>=20;
  FST.bot(c,x,VY,8,{flip:left,legs:'stand',armL:S>=20?'up':'down',armR:S<12?'reach':S<20?'tap':'up',eyes:panicked?'wide':left?'lookL':'lookR',mouth:panicked?'wobble':'o',bulb:panicked?'red':'yellow'});
  if(panicked)vSweat(c,x+160,VY+48,t,.8);
 },
 // 03: A phone, chat bubble and email each produce an order; bot collects all into a single register.
 festiveOrders(c,t,S){
  const channels=[80,174,268];
  c.strokeStyle='#1A1A1A';c.lineWidth=2.5;c.fillStyle='#FFFFFF';
  channels.forEach((x,i)=>{c.beginPath();if(i===0)c.roundRect(x-13,30,26,42,5);else c.roundRect(x-23,38,46,28,5);c.fill();c.stroke();c.strokeStyle='#04ADC3';c.beginPath();if(i===0){c.moveTo(x-5,63);c.lineTo(x+5,63);}else if(i===1){c.moveTo(x-10,66);c.lineTo(x-17,74);c.lineTo(x-17,64);}else{c.moveTo(x-23,38);c.lineTo(x,54);c.lineTo(x+23,38);}c.stroke();c.strokeStyle='#1A1A1A';});
  c.fillStyle='#DDF3F7';c.beginPath();c.roundRect(512,229,154,79,9);c.fill();c.stroke();
  const flip=S<13,collect=S>=6&&S<20;
  FST.bot(c,300,VY,8,{flip,legs:'stand',armL:S<6?'up':'down',armR:S<6?'down':S<13?'reach':S<22?'hold':'tap',eyes:S<6?'wide':S<22?'focus':'happy',mouth:S<6?'o':S<22?'flat':'smile',bulb:S<6?'red':S<22?'yellow':'aqua'});
  for(let i=0;i<3;i++){
   const gather=FST.k(t,.55+i*.17,1.6+i*.17),file=FST.k(t,2+i*.17,2.9+i*.17);
   const x=lerp(lerp(channels[i]-19,251+i*7,gather),530+i*40,file);
   const y=lerp(lerp(86,215+i*5,gather),245,file)-Math.sin(file*Math.PI)*170;
   FST.paper(c,x,y,false,34,46);
  }
  FST.tick(c,656,216,t,3.1);
 },
 // 04: Count a shelf that empties, raise a reorder draft, then wait for the owner's approval.
 festiveStock(c,t,S){
  c.strokeStyle='#1A1A1A';c.lineWidth=3;c.strokeRect(443,45,235,177);c.beginPath();c.moveTo(443,137);c.lineTo(678,137);c.stroke();
  for(let i=0;i<3;i++){
   const gone=FST.k(t,.2+i*.25,.7+i*.25);c.save();c.globalAlpha=1-gone;FST.box(c,458+i*66,80,48,54);c.restore();
  }
  FST.box(c,458,164,48,54);
  const wait=S>=10&&S<25;
  FST.bot(c,240,VY,8,{legs:'stand',armL:S<10?'down':wait?'out':'down',armR:S<10?'tap':wait?'hold':'up',eyes:S<10?'lookR':wait?'focus':'happy',mouth:S<10?'o':wait?'flat':'smile',bulb:S<10?'red':wait?'yellow':'aqua'});
  const draft=FST.k(t,1,1.65);if(draft){c.save();c.globalAlpha=draft;FST.paper(c,416,lerp(268,234,draft),false,46,59);c.restore();}
  if(wait)vMark(c,445,199,'?',FST.k(t,1.7,2),'q',.65);
  FST.tick(c,471,240,t,3.05);
  // A replenishment draft is prepared; only approval is shown, not guaranteed immediate stock delivery.
  const stamped=FST.k(t,3.1,3.55);if(stamped){c.save();c.globalAlpha=stamped;FST.box(c,552,164,48,54);c.restore();}
 },
 // 05: Match the order against the invoice/e-way document, inspect the mismatch, stamp before dispatch.
 festivePaperwork(c,t,S){
  FST.paper(c,470,153,false,64,86);FST.paper(c,574,153,t<2.65,64,86);FST.box(c,618,260,66,54);
  const inspect=S<21,stamp=S>=21&&S<27;
  FST.bot(c,288,VY,8,{legs:'stand',armL:'down',armR:S<8?'hold':inspect?'reach':stamp?'tap':'flex',eyes:S<8?'lookR':inspect?'focus':'happy',mouth:S<21?'flat':'grin',bulb:S<21?'yellow':'aqua'});
  const scan=FST.k(t,.7,2.45),lensX=lerp(489,601,scan),lensY=196;
  if(inspect){c.strokeStyle='#1A1A1A';c.lineWidth=4;c.beginPath();c.moveTo(456,255);c.lineTo(lensX-13,lensY+20);c.stroke();c.fillStyle='rgba(155,227,236,.3)';c.beginPath();c.arc(lensX,lensY,24,0,Math.PI*2);c.fill();c.stroke();}
  if(stamp){const down=FST.k(t,2.65,3.05);c.fillStyle='#1A1A1A';c.beginPath();c.roundRect(587,lerp(120,140,down),38,11,4);c.fill();c.fillRect(602,lerp(105,125,down),8,17);}
  FST.tick(c,630,138,t,3.05);
 },
 // 06: Delivery stops at a delay; bot raises the alert and actively sends the customer an update.
 festiveDispatch(c,t,S){
  c.strokeStyle='#04ADC3';c.lineWidth=3;c.beginPath();c.moveTo(404,295);c.lineTo(700,295);c.stroke();FST.box(c,455,241,62,54);
  c.strokeStyle='#F27A7A';c.lineWidth=4;c.beginPath();c.moveTo(552,245);c.lineTo(552,295);c.stroke();
  const flag=FST.k(t,.75,1.6);c.strokeStyle='#1A1A1A';c.lineWidth=3;c.beginPath();c.moveTo(350,lerp(300,201,flag));c.lineTo(350,316);c.stroke();c.fillStyle='#F27A7A';c.beginPath();c.moveTo(350,lerp(300,201,flag));c.lineTo(394,lerp(312,213,flag));c.lineTo(350,lerp(326,227,flag));c.fill();
  FST.bot(c,176,VY,8,{legs:'stand',armL:S>=18?'up':'down',armR:S<6?'down':S<14?'up':S<24?'reach':'down',eyes:S<6?'wide':S<24?'lookR':'happy',mouth:S<6?'o':S<24?'flat':'smile',bulb:S<6?'red':S<24?'yellow':'aqua'});
  // Generic customer mailbox; no real product UI or storefront repeats.
  c.fillStyle='#FFFFFF';c.strokeStyle='#1A1A1A';c.lineWidth=2.5;c.beginPath();c.roundRect(614,68,76,48,8);c.fill();c.stroke();c.beginPath();c.moveTo(625,91);c.lineTo(680,91);c.stroke();
  const send=FST.k(t,1.85,3.05);if(t>=1.65){const ex=lerp(358,630,send),ey=lerp(234,78,send);c.fillStyle='#FFFFFF';c.beginPath();c.roundRect(ex,ey,42,28,4);c.fill();c.stroke();c.beginPath();c.moveTo(ex,ey);c.lineTo(ex+21,ey+15);c.lineTo(ex+42,ey);c.stroke();}
  FST.tick(c,698,68,t,3.15);
 },
 // 07: A conductor, not a packer — brings four operational stages into one steady rhythm.
 festiveReveal(c,t,S){
  const settle=FST.k(t,1.2,2.7),y=1118;
  [132,282,432,582].forEach((x,i)=>{const yy=lerp(y+(i%2?26:-20),y,settle);if(i===0)FST.paper(c,x,yy,false,52,65);else if(i===1)FST.box(c,x,yy,65,65);else if(i===2)FST.paper(c,x,yy,false,52,65);else FST.box(c,x,yy,65,65);});
  c.strokeStyle='#04ADC3';c.lineWidth=3;c.beginPath();c.moveTo(128,1200);c.lineTo(654,1200);c.stroke();
  const lead=S<10?'up':S<22?'reach':'flex';
  FST.bot(c,766,966,10,{dark:true,halo:true,flip:true,legs:'stand',armL:'down',armR:lead,eyes:S<22?'focus':'happy',mouth:S<22?'flat':'smile',bulb:S<22?'yellow':'aqua'});
  c.strokeStyle='#FFFFFF';c.lineWidth=4;const angle=lerp(-.9,.2,FST.k(t,.8,2.2));c.save();c.translate(786,1094);c.rotate(angle);c.beginPath();c.moveTo(0,0);c.lineTo(-100,0);c.stroke();c.restore();
 },
 // 08: Work is cleared; the bot hands a finished gift parcel to the customer counter.
 festiveOutcome(c,t,S){
  // A small generic shop conveys serving customers, not another processing tray.
  vShop(c,616,45,true,1);
  c.fillStyle='#DDF3F7';c.strokeStyle='#1A1A1A';c.lineWidth=3;c.beginPath();c.roundRect(510,270,186,36,8);c.fill();c.stroke();
  const walk=Math.min(1,S/12),x=lerp(108,300,walk),handoff=FST.k(t,1.5,2.85);
  FST.bot(c,x,VY,8,{legs:S<12?walkLegs(S):'stand',armL:'down',armR:S<12?'hold':S<24?'reach':'down',eyes:S<24?'lookR':'happy',mouth:'smile',bulb:'aqua'});
  FST.box(c,lerp(snap(x)+174,558,handoff),lerp(246,212,handoff),66,56);FST.tick(c,634,236,t,3.05);
 },
 // 09: Point to the saved note, then send the DM envelope — distinct from fulfillment actions.
 festiveCTA(c,t,S){
  FST.bot(c,24,42,10,{legs:'stand',armL:S<11?'up':'down',armR:S<11?'up':S<23?'tap':'reach',eyes:S<11?'lookR':S<23?'focus':'happy',mouth:'smile',bulb:'aqua'});
  const mark=FST.k(t,.5,1.25);c.fillStyle='#04ADC3';c.beginPath();c.moveTo(285,lerp(35,66,mark));c.lineTo(315,lerp(35,66,mark));c.lineTo(315,lerp(83,114,mark));c.lineTo(300,lerp(72,103,mark));c.lineTo(285,lerp(83,114,mark));c.closePath();c.fill();
  const send=FST.k(t,1.65,2.8),xx=lerp(242,275,send);c.fillStyle='#FFFFFF';c.strokeStyle='#1A1A1A';c.lineWidth=2.5;c.beginPath();c.roundRect(xx,187,60,39,5);c.fill();c.stroke();c.beginPath();c.moveTo(xx,187);c.lineTo(xx+30,208);c.lineTo(xx+60,187);c.stroke();
 }
});
