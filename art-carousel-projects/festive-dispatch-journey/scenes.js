// Concept B: a persistent parcel connects the slides; open hero stage and matched exit/entry.
const J={
 k(t,a,b){const q=Math.max(0,Math.min(1,(t-a)/(b-a)));return q*q*(3-2*q);},
 parcel(c,x,y){c.fillStyle='#DDF3F7';c.strokeStyle='#1A1A1A';c.lineWidth=3;c.beginPath();c.roundRect(x,y,160,106,10);c.fill();c.stroke();c.strokeStyle='#04ADC3';c.lineWidth=9;c.beginPath();c.moveTo(x+80,y);c.lineTo(x+80,y+106);c.stroke();c.fillStyle='#FFFFFF';c.beginPath();c.roundRect(x+103,y+32,38,27,4);c.fill();},
 paper(c,x,y,color='#04ADC3'){c.fillStyle='#FFFFFF';c.strokeStyle='#1A1A1A';c.lineWidth=2.5;c.beginPath();c.roundRect(x,y,42,56,4);c.fill();c.stroke();c.strokeStyle=color;c.beginPath();for(let i=0;i<3;i++){c.moveTo(x+9,y+15+i*10);c.lineTo(x+33,y+15+i*10);}c.stroke();},
 bot(c,x,y,p){vShadow(c,x+120,y+238,160,0);drawBot(c,snap(x),snap(y),10,p);},
 route(c){c.strokeStyle='#04ADC3';c.lineWidth=3;c.beginPath();c.moveTo(-20,157);c.lineTo(1100,157);c.stroke();for(let x=0;x<1080;x+=42){c.fillStyle='#9BE3EC';c.beginPath();c.arc(x,157,3,0,Math.PI*2);c.fill();}},
 tick(c,x,y,k){if(k<=0)return;c.save();c.globalAlpha=k;c.strokeStyle='#2B907F';c.lineWidth=5;c.lineCap='round';c.beginPath();c.moveTo(x-12,y);c.lineTo(x-2,y+10);c.lineTo(x+19,y-14);c.stroke();c.restore();}
};
Object.assign(SCENES_DYN,{
 journeyOrders(c,t,S){
  J.route(c);
  const enter=J.k(t,0,.65),exit=J.k(t,3.05,4);
  const parcelX=lerp(lerp(-180,570,enter),1110,exit);
  J.parcel(c,parcelX,45);
  // Three abstract channels on an airy vertical rail. The character captures their slips once.
  c.strokeStyle='#1A1A1A';c.lineWidth=2.5;c.fillStyle='#FFFFFF';
  [240,305,370].forEach((y,i)=>{c.beginPath();if(i===0)c.roundRect(400,y,25,40,5);else c.roundRect(388,y,48,30,5);c.fill();c.stroke();c.strokeStyle='#04ADC3';c.beginPath();if(i===0){c.moveTo(408,y+31);c.lineTo(418,y+31);}else if(i===1){c.moveTo(396,y+30);c.lineTo(389,y+36);}else{c.moveTo(388,y);c.lineTo(412,y+18);c.lineTo(436,y);}c.stroke();c.strokeStyle='#1A1A1A';});
  J.bot(c,120,175,{legs:'stand',armL:S<8?'up':'down',armR:S<8?'down':S<19?'tap':'up',eyes:S<8?'wide':S<21?'focus':'happy',mouth:S<21?'flat':'smile',bulb:S<8?'red':S<21?'yellow':'aqua'});
  for(let i=0;i<3;i++){
   const capture=J.k(t,.65+i*.22,1.35+i*.22),file=J.k(t,1.65+i*.2,2.5+i*.2);
   const xx=lerp(lerp(449,345,capture),625+i*7,file),yy=lerp(lerp(240+i*65,310+i*4,capture),76+i*5,file)-Math.sin(file*Math.PI)*130;
   c.save();c.globalAlpha=1-exit;J.paper(c,xx,yy);c.restore();
  }
  J.tick(c,747,48,J.k(t,2.65,3));
 },
 journeyStock(c,t,S){
  J.route(c);const enter=J.k(t,0,.65),exit=J.k(t,3.1,4);
  J.parcel(c,lerp(lerp(-180,290,enter),1110,exit),45);
  // A low shelf and a single approval draft; continuity is carried by the parcel above.
  c.strokeStyle='#1A1A1A';c.lineWidth=3;c.strokeRect(132,232,260,164);c.beginPath();c.moveTo(132,310);c.lineTo(392,310);c.stroke();
  for(let i=0;i<3;i++){c.save();c.globalAlpha=1-J.k(t,.5+i*.22,.95+i*.22);c.translate(151+i*76,251);c.scale(.32,.32);J.parcel(c,0,0);c.restore();}
  c.save();c.translate(151,334);c.scale(.32,.32);J.parcel(c,0,0);c.restore();
  J.bot(c,670,175,{flip:true,legs:'stand',armL:S<13?'down':S<25?'out':'down',armR:S<13?'tap':S<25?'hold':'flex',eyes:S<13?'lookL':S<25?'focus':'happy',mouth:S<25?'flat':'smile',bulb:S<13?'red':S<25?'yellow':'aqua'});
  const draft=J.k(t,1.2,1.7);if(draft){c.save();c.globalAlpha=draft;J.paper(c,570,lerp(345,296,draft));c.restore();}
  if(S>=14&&S<25)vMark(c,592,263,'?',J.k(t,1.7,2),'q',.7);
  J.tick(c,627,302,J.k(t,2.9,3.2));
 }
});
