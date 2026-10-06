// Concept C: physical-metaphor motion posters. One oversized transformation per scene.
const P={
 k(t,a,b){const q=Math.max(0,Math.min(1,(t-a)/(b-a)));return q*q*(3-2*q);},
 rr(c,x,y,w,h,fill,r=10){c.fillStyle=fill;c.strokeStyle='#1A1A1A';c.lineWidth=3;c.beginPath();c.roundRect(x,y,w,h,r);c.fill();c.stroke();},
 sheet(c,x,y,w=112,h=144,bad=false){P.rr(c,x,y,w,h,'#FFFFFF',8);c.strokeStyle=bad?'#F27A7A':'#04ADC3';c.lineWidth=5;c.beginPath();for(let j=0;j<3;j++){c.moveTo(x+20,y+35+j*25);c.lineTo(x+w-20,y+35+j*25);}c.stroke();},
 bot(c,x,y,S,pose){vShadow(c,x+120,y+238,160,0,true);drawBot(c,snap(x),snap(y),10,{dark:true,halo:true,...pose});},
 tick(c,x,y,t,start=2.6){const k=P.k(t,start,start+.4);if(!k)return;c.save();c.globalAlpha=k;c.strokeStyle='#41A486';c.lineWidth=7;c.lineCap='round';c.lineJoin='round';c.beginPath();c.moveTo(x-18,y);c.lineTo(x-4,y+15);c.lineTo(x+26,y-21);c.stroke();c.restore();},
 backdrop(c,x,y,r){c.fillStyle='#04ADC3';c.globalAlpha=.12;c.beginPath();c.arc(x,y,r,0,Math.PI*2);c.fill();c.globalAlpha=1;}
};
Object.assign(SCENES_DYN,{
 posterOrders(c,t,S){
  P.backdrop(c,730,205,230);
  const resolve=P.k(t,1.05,2.75),pull=P.k(t,.65,1.3);
  // One giant inbox is the metaphor; the three channel orders become a clean row.
  P.rr(c,420,lerp(257,292,pull),500,80,'#04ADC3',14);
  for(let i=0;i<3;i++){
   const start=[[439,58,-.18],[625,17,.15],[791,83,-.12]][i];
   const x=lerp(start[0],460+i*145,resolve),y=lerp(start[1],126,resolve);
   c.save();c.translate(x+55,y+72);c.rotate(start[2]*(1-resolve));P.sheet(c,-55,-72,110,144);c.restore();
  }
  P.bot(c,164,174,S,{legs:'stand',armL:S<8?'up':'down',armR:S<8?'down':S<20?'reach':'tap',eyes:S<8?'wide':S<22?'focus':'happy',mouth:S<8?'o':S<22?'flat':'grin',bulb:S<8?'red':S<22?'yellow':'aqua'});
  // A visible pull handle meets the right hand, so the bot causes the drawer reveal.
  c.strokeStyle='#9BE3EC';c.lineWidth=9;c.lineCap='round';c.beginPath();c.moveTo(377,325);c.lineTo(428,325);c.stroke();
  P.tick(c,934,104,t,2.8);
 },
 posterStock(c,t,S){
  P.backdrop(c,349,180,230);
  // Stock is a large physical shelf, not a tiny icon or screen.
  P.rr(c,132,52,424,270,'#DDF3F7',12);c.strokeStyle='#1A1A1A';c.lineWidth=4;c.beginPath();c.moveTo(132,184);c.lineTo(556,184);c.stroke();
  for(let i=0;i<3;i++){
   const gone=P.k(t,.1+i*.25,.8+i*.25);c.save();c.globalAlpha=1-gone;
   P.rr(c,157+i*128,81,100,100,'#04ADC3',8);c.strokeStyle='#9BE3EC';c.lineWidth=6;c.beginPath();c.moveTo(207+i*128,81);c.lineTo(207+i*128,181);c.stroke();c.restore();
  }
  P.rr(c,157,214,100,94,'#04ADC3',8);
  const draft=P.k(t,1.25,2);if(draft){c.save();c.globalAlpha=draft;P.sheet(c,606,lerp(303,196,draft),112,144);c.restore();}
  P.bot(c,756,174,S,{flip:true,legs:'stand',armR:S<10?'tap':S<25?'hold':'up',armL:S>=10&&S<25?'out':'down',eyes:S<10?'lookL':S<25?'focus':'happy',mouth:S<10?'o':S<25?'flat':'smile',bulb:S<10?'red':S<25?'yellow':'aqua'});
  if(S>=16&&S<25)vMark(c,666,155,'?',P.k(t,2,2.3),'q',1);
  P.tick(c,729,195,t,3.15);
 },
 posterPaperwork(c,t,S){
  P.backdrop(c,700,204,232);
  const align=P.k(t,1.25,2.7),release=P.k(t,3.25,4);
  // Two oversized physical documents line up, then the checked pack leaves for dispatch.
  c.save();c.globalAlpha=1-align*.88;c.translate(540,185);c.rotate(-.12*(1-align));P.sheet(c,-100,-127,200,254,false);c.restore();
  const x=lerp(676,554,align)+release*420,y=lerp(47,62,align);
  c.save();c.translate(x+100,y+127);c.rotate(.13*(1-align));P.sheet(c,-100,-127,200,254,t<2.7);c.restore();
  P.bot(c,212,174,S,{legs:'stand',armL:'down',armR:S<7?'hold':S<21?'reach':S<27?'tap':'flex',eyes:S<21?'focus':'happy',mouth:S<21?'flat':'grin',bulb:S<21?'yellow':'aqua'});
  if(S<21){const lx=lerp(456,733,P.k(t,.65,2.45));c.strokeStyle='#9BE3EC';c.lineWidth=5;c.beginPath();c.moveTo(423,324);c.lineTo(lx-24,216);c.stroke();c.fillStyle='rgba(155,227,236,.18)';c.beginPath();c.arc(lx,178,39,0,Math.PI*2);c.fill();c.stroke();}
  P.tick(c,x+172,y+32,t,2.8);
 },
 posterDispatch(c,t,S){
  P.backdrop(c,793,180,232);
  // A giant clock makes the delay instantly legible; the customer receives a large envelope.
  c.fillStyle='#FFFFFF';c.strokeStyle='#1A1A1A';c.lineWidth=4;c.beginPath();c.arc(533,143,90,0,Math.PI*2);c.fill();c.stroke();
  c.strokeStyle='#F27A7A';c.lineWidth=7;c.lineCap='round';const a=lerp(-1.5,-.5,P.k(t,.2,1.5));c.beginPath();c.moveTo(533,143);c.lineTo(533+Math.cos(a)*65,143+Math.sin(a)*65);c.stroke();c.strokeStyle='#1A1A1A';c.beginPath();c.moveTo(533,143);c.lineTo(500,170);c.stroke();
  P.rr(c,454,281,124,86,'#DDF3F7',9);c.strokeStyle='#F27A7A';c.lineWidth=5;c.beginPath();c.moveTo(614,270);c.lineTo(614,367);c.stroke();
  P.rr(c,734,67,230,180,'#FFFFFF',16);c.strokeStyle='#04ADC3';c.lineWidth=5;c.beginPath();c.moveTo(758,111);c.lineTo(940,111);c.stroke();
  P.bot(c,124,174,S,{legs:'stand',armL:S>=13?'up':'down',armR:S<6?'down':S<14?'up':S<23?'reach':'down',eyes:S<6?'wide':S<23?'lookR':'happy',mouth:S<6?'o':S<23?'flat':'smile',bulb:S<6?'red':S<23?'yellow':'aqua'});
  const send=P.k(t,1.45,2.95);if(t>=1.2){const xx=lerp(347,772,send),yy=lerp(294,131,send);c.save();c.translate(xx,yy);c.rotate(-.14*Math.sin(send*Math.PI));P.rr(c,0,0,153,99,'#FFFFFF',10);c.strokeStyle='#04ADC3';c.lineWidth=4;c.beginPath();c.moveTo(0,0);c.lineTo(76,54);c.lineTo(153,0);c.stroke();c.restore();}
  P.tick(c,965,74,t,3.05);
 }
});
