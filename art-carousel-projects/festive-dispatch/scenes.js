// Festive dispatch v3: one action per slide, fixed robot staging, restrained props.
// Timing: establish 0–1.0s; action 1.0–2.5s; resolve 2.5–3.0s; hold to 4.0s.
const FST = {
 k(t,a,b){const q=Math.max(0,Math.min(1,(t-a)/(b-a)));return q*q*(3-2*q);},
 box(c,x,y,w=76,h=64){c.fillStyle='#DDF3F7';c.strokeStyle='#1A1A1A';c.lineWidth=2.5;c.beginPath();c.roundRect(x,y,w,h,6);c.fill();c.stroke();c.strokeStyle='#04ADC3';c.beginPath();c.moveTo(x+w/2,y);c.lineTo(x+w/2,y+h);c.stroke();},
 paper(c,x,y,bad=false,w=64,h=76){c.fillStyle='#FFFFFF';c.strokeStyle='#1A1A1A';c.lineWidth=2.5;c.beginPath();c.roundRect(x,y,w,h,5);c.fill();c.stroke();c.strokeStyle=bad?'#F27A7A':'#04ADC3';c.beginPath();for(let j=0;j<3;j++){c.moveTo(x+12,y+20+j*13);c.lineTo(x+w-12,y+20+j*13);}c.stroke();},
 bot(c,t,S,x=148,y=VY,u=8,dark=false){const working=t>=1&&t<2.5,done=t>=2.5;vShadow(c,x+12*u,y+23*u+5,14*u,0,dark);drawBot(c,x,y,u,{legs:'stand',armL:'down',armR:working?'reach':done?'hold':'down',eyes:done?'happy':working?'focus':'lookR',mouth:done?'smile':'flat',bulb:done?'aqua':working?'yellow':'red',dark,halo:dark});},
 tick(c,x,y,t,start=2.6){const k=FST.k(t,start,start+.4);if(!k)return;c.save();c.globalAlpha=k;c.strokeStyle='#2B907F';c.lineWidth=5;c.lineCap='round';c.lineJoin='round';c.beginPath();c.moveTo(x-12,y);c.lineTo(x-3,y+9);c.lineTo(x+16,y-12);c.stroke();c.restore();},
 shelf(c){c.strokeStyle='#1A1A1A';c.lineWidth=3;c.beginPath();c.moveTo(446,148);c.lineTo(634,148);c.lineTo(634,292);c.lineTo(446,292);c.stroke();c.beginPath();c.moveTo(446,220);c.lineTo(634,220);c.stroke();}
};
Object.assign(SCENES_DYN,{
 // Setup: one parcel waits at a closed gate; the bot notices it once.
 festiveSetup(c,t,S){
  FST.bot(c,t<2.5?t:0,S);
  FST.box(c,438,230,86,64);
  c.strokeStyle='#F27A7A';c.lineWidth=5;c.lineCap='round';c.beginPath();c.moveTo(590,211);c.lineTo(590,294);c.stroke();
  const k=FST.k(t,1.2,2.1);c.save();c.globalAlpha=k;c.fillStyle='#F27A7A';c.beginPath();c.arc(590,184,15,0,Math.PI*2);c.fill();c.fillStyle='#FFFFFF';c.font='bold 20px sans-serif';c.textAlign='center';c.fillText('!',590,191);c.restore();
 },
 // Orders: a single loose slip glides into a single receiving tray.
 festiveOrders(c,t,S){
  FST.bot(c,t,S);const k=FST.k(t,1,2.5);
  c.fillStyle='#DDF3F7';c.strokeStyle='#1A1A1A';c.lineWidth=2.5;c.beginPath();c.roundRect(454,234,144,61,8);c.fill();c.stroke();
  FST.paper(c,lerp(355,494,k),lerp(149,211,k),false,54,68);FST.tick(c,578,211,t);
 },
 // Stock: one reorder sheet moves into an approval slot; only then one carton appears.
 festiveStock(c,t,S){
  FST.shelf(c);FST.box(c,464,169,46,48);
  FST.bot(c,t,S);const k=FST.k(t,1,2.35);
  FST.paper(c,lerp(342,548,k),250,false,44,52);
  FST.tick(c,616,262,t,2.45);
  const ready=FST.k(t,2.95,3.4);if(ready){c.save();c.globalAlpha=ready;FST.box(c,548,lerp(162,169,ready),46,48);c.restore();}
 },
 // Paperwork: compare one document against one parcel; red detail becomes a check.
 festivePaperwork(c,t,S){
  FST.bot(c,t,S);FST.box(c,539,225,76,66);FST.paper(c,415,194,t<2.5);
  const scan=FST.k(t,1,2.45);
  if(t>=1&&t<2.5){c.save();c.globalAlpha=Math.sin(scan*Math.PI)*.75;c.fillStyle='#9BE3EC';c.fillRect(419,lerp(204,254,scan),56,5);c.restore();}
  FST.tick(c,494,210,t);
 },
 // Dispatch: one gate rotates clear, one parcel slides forward, one notice settles.
 festiveDispatch(c,t,S){
  FST.bot(c,t,S);
  c.strokeStyle='#04ADC3';c.lineWidth=2.5;c.beginPath();c.moveTo(390,294);c.lineTo(650,294);c.stroke();
  const gate=FST.k(t,1,1.75);c.save();c.translate(524,292);c.rotate(-Math.PI/2*gate);c.strokeStyle=gate<1?'#F27A7A':'#04ADC3';c.lineWidth=4;c.beginPath();c.moveTo(0,0);c.lineTo(0,-82);c.stroke();c.restore();
  FST.box(c,lerp(418,578,FST.k(t,1.8,2.8)),236,54,54);
  const sent=FST.k(t,2.65,3.15);if(sent){c.save();c.globalAlpha=sent;c.strokeStyle='#1A1A1A';c.fillStyle='#FFFFFF';c.lineWidth=2.5;c.beginPath();c.roundRect(594,lerp(155,145,sent),52,34,5);c.fill();c.stroke();c.beginPath();c.moveTo(594,145);c.lineTo(620,166);c.lineTo(646,145);c.stroke();c.restore();}FST.tick(c,659,150,t,3.1);
 },
 // Reveal: one ribbon settles onto one gift; no arrival, hop, hearts or waving loop.
 festiveReveal(c,t,S){
  FST.bot(c,t,S,730,966,10,true);FST.box(c,564,1100,124,88);
  const k=FST.k(t,1,2.5);c.save();c.globalAlpha=k;c.strokeStyle='#04ADC3';c.lineWidth=5;c.beginPath();c.moveTo(626,1100);c.lineTo(626,1188);c.stroke();c.beginPath();c.ellipse(606,1094,20,9,-.3,0,Math.PI*2);c.ellipse(646,1094,20,9,.3,0,Math.PI*2);c.stroke();c.restore();
 },
 // Outcome: seal one finished carton. The summary text already supplies the four checks.
 festiveOutcome(c,t,S){
  FST.bot(c,t,S);FST.box(c,440,205,112,86);
  const k=FST.k(t,1,2.5);c.strokeStyle='#04ADC3';c.lineWidth=9;c.beginPath();c.moveTo(446,231);c.lineTo(lerp(446,546,k),231);c.stroke();FST.tick(c,579,221,t);
 },
 // CTA: close one envelope with a single smooth flap; keep the robot still.
 festiveCTA(c,t,S){
  FST.bot(c,t,S,24,42,10);const k=FST.k(t,1,2.5),x=247,y=182;
  c.fillStyle='#FFFFFF';c.strokeStyle='#1A1A1A';c.lineWidth=2.5;c.beginPath();c.roundRect(x,y,76,48,5);c.fill();c.stroke();
  c.fillStyle='#DDF3F7';c.beginPath();c.moveTo(x,y);c.lineTo(x+38,lerp(y-30,y+24,k));c.lineTo(x+76,y);c.closePath();c.fill();c.stroke();
 }
});
