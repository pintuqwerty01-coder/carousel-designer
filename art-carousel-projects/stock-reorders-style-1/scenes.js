// Style 1 v2. One deliberate action at a time; all copy remains stationary.
// The original mascot is always u=10 / 240px. Props use continuous easing.
function line(c,pts,color=VC.K,width=3,dash=[]) {
  c.save();c.strokeStyle=color;c.lineWidth=width;c.lineCap='round';c.lineJoin='round';c.setLineDash(dash);c.beginPath();pts.forEach(([x,y],i)=>i?c.lineTo(x,y):c.moveTo(x,y));c.stroke();c.restore();
}
function label(c,text,x,y,color='#F0F4F5',size=22,align='center') {
  c.save();c.fillStyle=color;c.font='500 '+size+'px Poppins';c.textAlign=align;c.fillText(text,x,y);c.restore();
}
function parcel(c,x,y,w=80,h=64,fill=VC.A) {
  rr(c,x,y,w,h,8);fs(c,fill,VC.K,3);line(c,[[x+2,y+16],[x+w-2,y+16]],VC.K,2);rr(c,x+w*.43,y+2,w*.14,h-4,0);fs(c,fill===VC.Y?'#FFE6A0':VC.S);
}
function sheet(c,x,y,w,h,fill=VC.W) {
  rr(c,x,y,w,h,14);fs(c,fill,VC.K,3);rr(c,x+18,y+22,w-36,16,4);fs(c,VC.S);
  for(let j=0;j<3;j++)line(c,[[x+18,y+63+j*24],[x+w-18,y+63+j*24]],'#C5D9DD',3);
}
function avatar(c,x,y,r=23) {
  c.save();c.beginPath();c.arc(x,y-r*.25,r*.43,0,Math.PI*2);fs(c,VC.K);
  c.beginPath();c.arc(x,y+r*.8,r*.85,Math.PI,Math.PI*2);c.closePath();fs(c,VC.K);c.restore();
}
function robot(c,x,y,t,mode='work',dark=false,arm='reach') {
  dark=!c.canvas.closest('.branch'); // Photo scenes need white legs/halo; slide 5 keeps black legs on its light cards.
  const done=mode==='done',alert=mode==='alert';
  vShadow(c,x+120,y+236,148,0,dark);
  drawBot(c,x,y,10,{dark,halo:dark,armR:arm,armL:'down',legs:'stand',eyes:done?'happy':alert?'wide':'focus',mouth:done?'grin':alert?'o':'smile',bulb:done?'aqua':alert?'red':'yellow'});
}
function shelf(c,x,y,full=false,t=0) {
  vShelf(c,x,x+222,y,[y+112,y+228]);
  for(let j=0;j<6;j++){
    if(!full&&j!==5)continue;
    parcel(c,x+16+(j%3)*66,y+56+(j<3?0:116),52,56);
  }
}
function clock(c,x,y,t) {
  c.beginPath();c.arc(x,y,37,0,Math.PI*2);fs(c,VC.W,VC.K,3);
  line(c,[[x,y-21],[x,y],[x+Math.sin(Math.min(t,2.4)*1.8)*22,y-Math.cos(Math.min(t,2.4)*1.8)*22]],VC.K,3);
}
function notification(c,x,y,k) {
  rr(c,x,y,91,122,13);fs(c,VC.K);rr(c,x+7,y+12,77,92,7);fs(c,VC.W);avatar(c,x+45,y+50,22);
  if(k>0){c.beginPath();c.arc(x+80,y+13,11*eOut(k),0,Math.PI*2);fs(c,VC.Y,VC.W,3);}
  line(c,[[x+37,y+113],[x+54,y+113]],VC.S,3);
}
function hero(c,t,S) {
  label(c,'Reorder',491,200,'#D9E6E8');label(c,'Stock',732,60,'#D9E6E8');
  shelf(c,620,100,false);
  // The existing stock stays low: the check means an order is ready, not instant delivery.
  line(c,[[550,322],[586,322],[586,214],[615,214]],VC.A,3,[6,8]);
  const ready=t>=2.25;
  robot(c,220,225,t,ready?'done':'work',true,t<.7?'down':'reach');
  const q=eOut((t-.65)/.75);sheet(c,440,294-22*q,100,134);
  if(ready)vBadge(c,491,300,(t-2.25)/.35,26);
}
function chasing(c,t,S) {
  label(c,'Shelf checks',153,65);label(c,'Manual records',751,65);
  vShelf(c,42,264,138,[250,366]);
  for(let j=0;j<6;j++){
    const a=j===5?1:1-eOut((t-.3-j*.22)/.3);
    if(a>0){c.save();c.globalAlpha=a;parcel(c,58+(j%3)*66,j<3?194:310,52,56);c.restore();}
  }
  sheet(c,657,176,188,222);clock(c,751,123,t);
  const moving=t>.6&&t<2.3,x=snap(302+eInOut((t-.6)/1.7)*65);
  vShadow(c,x+120,460,148,0,true);drawBot(c,x,224,10,{dark:true,halo:true,legs:moving?walkLegs(S):'stand',armR:t<1.4?'down':'reach',eyes:'wide',mouth:'wobble',bulb:'red'});
  if(t>2.35)vMark(c,288,110,'!',(t-2.35)/.3,'bang',1);
}
function monitor(c,t,S) {
  label(c,'Stock level',174,70);label(c,'Reorder point',736,128);
  shelf(c,62,140,false);
  const scan=eInOut((t-.4)/1.3);if(t>.4&&t<1.9)vBeam(c,70+scan*200,147,365);
  rr(c,690,170,92,230,12);fs(c,VC.W,'#B6D8DF',3);
  const h=168-110*eInOut((t-.55)/1.2);rr(c,702,388-h,68,h,6);fs(c,VC.A);
  line(c,[[667,292],[803,292]],VC.R,3,[6,6]);
  const active=t>1.9;robot(c,360,224,t,active?'done':'work',false,active?'up':'reach');
  if(active)vMark(c,815,205,'!',(t-1.9)/.25,'bang',.9);
}
function compare(c,t,S) {
  label(c,'On hand',170,72);label(c,'Incoming',747,72);label(c,'Reorder check',456,80);
  shelf(c,60,150,false);
  // Incoming parcel advances only in its own far-right lane.
  vBelt(c,650,855,360,30,Math.min(Math.max(t-.7,0),1.1)*70);
  parcel(c,657+eInOut((t-.7)/1.1)*70,281,100,79);
  const a=eOut((t-1.1)/.9),b=eOut((t-1.9)/.65);
  vCurve(c,[282,210],[346,97],[450,186],a,VC.A,{arrow:true,dash:[6,7],lw:3});
  vCurve(c,[698,255],[636,93],[501,186],b,VC.A,{arrow:true,dash:[6,7],lw:3});
  robot(c,350,224,t,t>2.8?'done':'work',false,'up');
  if(t>2.8)vBadge(c,469,188,(t-2.8)/.3,26);
}
function paths(c,t,S) {
  for(let i=0;i<2;i++){
    c.save();c.translate(i?477:7,0);
    const start=i?1.8:.35,duration=i?.65:1.05,k=eInOut((t-start)/duration);
    const x=232+k*(i?20:92),floor=333;
    // Each example resolves in sequence, then holds still for comparison.
    const beltOff=80*Math.min(Math.max(t-start,0),duration);
    vBelt(c,231,415,285,30,beltOff);
    parcel(c,x,231,i?88:62,54,i?VC.Y:VC.A);
    if(i){
      // Request stops before the closed review gate. No approval is implied.
      line(c,[[371,284],[371,211],[411,211]],VC.K,4);
      line(c,[[377,215],[399,237]],VC.R,4);
      if(t>2.45){
        vCurve(c,[298,227],[264,150],[309,133],(t-2.45)/.35,VC.A,{arrow:true,dash:[6,7],lw:3});
        notification(c,300,22,(t-2.45)/.35);
      }
      robot(c,4,floor-230,t,'work',false,t>2.45?'up':'reach');
    }else{
      if(t>1.45)vBadge(c,350,189,(t-1.45)/.3,25);
      robot(c,4,floor-230,t,t>1.45?'done':'work',false,t>1.45?'up':'reach');
    }
    c.restore();
  }
}
function review(c,t,S) {
  label(c,'Exception request',191,68);label(c,'Your decision',718,68);
  // Human review is an abstract illustration, not a real product interface.
  rr(c,622,152,213,236,20);fs(c,VC.W,VC.K,3);avatar(c,730,210,44);
  const q=eInOut((t-.55)/1.25);
  sheet(c,80,145,145,185,VC.Y);
  vCurve(c,[232,208],[431,87],[611,222],q,VC.A,{arrow:true,dash:[7,8],lw:3});
  robot(c,330,225,t,'work',false,t>1.7?'up':'reach');
  // All choices stay visible; only a restrained focus outline changes.
  const choices=[['Review',638,280],['Adjust',733,280],['Approve',638,329],['Hold',733,329]];
  choices.forEach(([text,x,y],j)=>{
    rr(c,x,y,87,37,8);fs(c,j===0&&t>2?VC.T:'#F4F7F8',j===0&&t>2?VC.A:'#DBE5E8',2);
    label(c,text,x+43,y+25,VC.K,16);
  });
  if(t>2.7){c.beginPath();c.arc(806,146,10,0,Math.PI*2);fs(c,VC.Y,VC.W,3);}
}
function together(c,t,S) {
  label(c,'Routine orders',171,70,'#D9E6E8');label(c,'Exceptions',750,70,'#D9E6E8');
  vBelt(c,52,285,346,31,70*Math.min(Math.max(t-.3,0),1.3));
  const k=eInOut((t-.3)/1.3);parcel(c,70+110*k,285,72,61);
  if(t>1.7)vBadge(c,233,249,(t-1.7)/.3,24);
  line(c,[[570,235],[614,235],[614,150],[659,150]],VC.A,3,[6,8]);
  sheet(c,680,274,128,137,VC.Y);
  notification(c,700,100,Math.max(0,(t-2.1)/.3));
  robot(c,334,224,t,t>2.7?'done':'work',true,t>2?'up':'reach');
}
function controls(c,t,S) {
  label(c,'Your rules',157,68);label(c,'Stock flow',742,68);
  rr(c,51,126,211,257,20);fs(c,VC.W,VC.K,3);
  const q=eInOut((t-.45)/.8);
  for(let j=0;j<3;j++){
    const y=191+j*67;
    line(c,[[80,y],[232,y]],'#B7D5DA',5);
    const x=j===0?110+q*76:j===1?190:147;
    c.beginPath();c.arc(x,y,11,0,Math.PI*2);fs(c,VC.A,VC.K,2);
  }
  const k=eInOut((t-1.6)/1.2);
  vBelt(c,643,855,353,31,k*100);parcel(c,655+110*k,287,75,66);
  vCurve(c,[270,144],[455,39],[657,169],eOut((t-1.1)/.8),VC.A,{arrow:true,dash:[7,8],lw:3});
  robot(c,340,224,t,t>2.8?'done':'work',false,t<1.3?'reach':'up');
  if(t>2.8)vBadge(c,790,241,(t-2.8)/.3,27);
}
