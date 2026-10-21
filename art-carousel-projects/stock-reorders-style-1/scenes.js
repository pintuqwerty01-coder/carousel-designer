// Style 1: smooth vector props; the original pixel mascot at u=10 (240px).
// No random numbers or wall clocks: every frame is a deterministic function of t.
function line(c, pts, color=VC.K, width=3, dash=[]) {
  c.save(); c.strokeStyle=color; c.lineWidth=width; c.lineCap='round'; c.lineJoin='round'; c.setLineDash(dash);
  c.beginPath(); pts.forEach(([x,y],i)=>i?c.lineTo(x,y):c.moveTo(x,y)); c.stroke(); c.restore();
}
function clock(c,x,y,t) {
  c.save(); c.translate(x,y); c.beginPath(); c.arc(0,0,39,0,Math.PI*2); fs(c,VC.W,VC.K,3);
  line(c,[[0,-24],[0,0],[Math.cos(t*2)*22,Math.sin(t*2)*22]],VC.K,4);
  c.restore();
}
function sheet(c,x,y,w,h,fill=VC.W) {
  rr(c,x,y,w,h,14);fs(c,fill,VC.K,3);
  rr(c,x+17,y+21,w-34,22,5);fs(c,VC.T);
  for(let row=0;row<4;row++){
    line(c,[[x+17,y+67+row*27],[x+w-17,y+67+row*27]],'#D5E2E4',2);
    line(c,[[x+w*.55,y+54],[x+w*.55,y+h-14]],'#D5E2E4',2);
  }
}
function parcel(c,x,y,w=80,h=64,fill=VC.A) {
  rr(c,x,y,w,h,8);fs(c,fill,VC.K,3);
  line(c,[[x+2,y+16],[x+w-2,y+16]],VC.K,2);
  rr(c,x+w*.43,y+2,w*.14,h-4,0);fs(c,fill===VC.Y?'#FFE6A0':VC.S);
}
function shelf(c,t,restore=false) {
  vShelf(c,42,264,138,[250,366]);
  for(let j=0;j<6;j++){
    let x=58+(j%3)*66,y=j<3?194:310;
    let disappear=[.35,.7,1,1.3,1.6,9][j];
    let a=1-eOut((t-disappear)/.3);
    if(restore)a=Math.max(a,eOut((t-2.6-j*.06)/.25));
    if(a>.001){c.save();c.globalAlpha=a;parcel(c,x,y,52,56);c.restore();}
    else {c.save();c.strokeStyle='#BBD5D9';c.lineWidth=2;c.setLineDash([5,7]);c.strokeRect(x,y,52,56);c.restore();}
  }
}
function chasing(c,t,S) {
  shelf(c,t);
  clock(c,152,66,t);
  const x=snap(t<1.4?300+eInOut(t/1.4)*100:400-eInOut((t-1.4)/1.4)*100);
  sheet(c,654,182,194,218);
  c.save();c.translate(752,140);c.scale(1.5,1.5);vPhone(c,0,0,t,true,0);c.restore();
  vRings(c,752,87,t);
  vShadow(c,x+120,457,152);
  drawBot(c,x,224,10,{legs:walkLegs(S),armL:S%4<2?'up':'down',armR:S%4<2?'reach':'up',eyes:'wide',mouth:'wobble',bulb:'red',bulbOff:S%3===0});
  vSweat(c,x+188,286,t,1);
  if(t>.9)vMark(c,276,104,'!',(t-.9)/.25,'bang',1.15);
  c.save();c.globalAlpha=.45;line(c,[[300,470],[620,470]],VC.K,2,[6,8]);c.restore();
}
function hero(c,t,S) {
  c.save(); c.translate(580,2);
  vShelf(c,0,276,100,[225,350]);
  for(let j=0;j<6;j++) {
    const k=j===5?1:eOut((t-2.1-j*.1)/.3);
    if(k>0) {c.save();c.globalAlpha=k;parcel(c,18+(j%3)*83,(j<3?155:280)-20*(1-k),67,70);c.restore();}
  }
  c.restore();
  const x=snap(150+eOut(Math.min(1,t/1.1))*70), y=225;
  vShadow(c,x+120,461,154,0,true);
  drawBot(c,x,y,10,{dark:true,halo:true,legs:t<1?'stepL':'stand',armR:t>1?'reach':'down',eyes:t>2.6?'happy':t>1?'focus':'lookR',mouth:t>2.6?'grin':'smile',bulb:t>2.6?'aqua':'yellow'});
  if(t>.9) {
    const k=eOut((t-.9)/.4);
    c.save();c.globalAlpha=k;vSlip(c,440,280+30*(1-k),100,128);
    if(t>2.35)vBadge(c,492,304,(t-2.35)/.35,25);c.restore();
    vCurve(c,[544,330],[570,315],[580,263],(t-1.45)/.65,VC.A,{arrow:true,dash:[6,8],lw:3});
  }
}
// Two fixed branches. Small orders leave immediately; the larger request remains
// visibly held for a person. It never acquires a completion check in this slide.
function paths(c,t,S) {
  const leftX=7,rightX=477;
  for(let i=0;i<2;i++) {
    const offset=i?rightX:leftX;
    c.save();c.translate(offset,0);
    const floor=445, bx=4, by=floor-230;
    // The belt stays beside the mascot, rather than passing through its body.
    vBelt(c,232,420,383,36,i?Math.min(t,1.8)*65:t*80);
    if(!i){
      // A low-amount request becomes an order, then leaves on the conveyor.
      const k=eInOut((t-.7)/1.5), x=230+k*125;
      parcel(c,x,329,58,52);
      if(t>2.15)vBadge(c,328,273,(t-2.15)/.3,28);
      line(c,[[253,229],[291,229],[291,283]],VC.A,3,[6,7]);
      if(t>1.4) {const q=eOut((t-1.4)/.25);line(c,[[285,274],[291,283],[297,274]],VC.A,3*q);}
    } else {
      const k=eInOut((t-.7)/1.1), x=230+k*26;
      parcel(c,x,329,92,52,VC.Y);
      // Closed gate + an unanswered notification = request awaits human action.
      line(c,[[371,383],[371,290],[414,290]],VC.K,5);
      line(c,[[376,294],[400,318]],VC.R,5);
      if(t>1.8){
        c.save();c.translate(337,217);c.scale(1.2,1.2);vPhone(c,0,0,t,true,0,'bell');c.restore();
        vRings(c,337,178,t);
        vCurve(c,[300,328],[242,253],[315,220],(t-1.8)/.55,VC.A,{arrow:true,dash:[5,7],lw:3});
      }
    }
    vShadow(c,bx+120,floor+6,142);
    drawBot(c,bx,by,10,{armR:t<1.2?'reach':i?'up':S%4<2?'wave1':'wave2',armL:'down',eyes:t>2?i?'lookR':'happy':'focus',mouth:t>2&&!i?'grin':'smile',bulb:t>1.8&&i?'yellow':'aqua'});
    c.restore();
  }
}
