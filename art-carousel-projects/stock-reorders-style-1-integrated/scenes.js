// Every anchor corresponds to a photographed shelf, table or dispatch area.
// The pixel mascot remains 240px tall; no replacement cartoon stockroom is drawn.
function stroke(c,pts,color=VC.A,width=3,dash=[]) {c.save();c.strokeStyle=color;c.lineWidth=width;c.lineCap='round';c.lineJoin='round';c.setLineDash(dash);c.beginPath();pts.forEach(([x,y],i)=>i?c.lineTo(x,y):c.moveTo(x,y));c.stroke();c.restore();}
function note(c,text,x,y,align='left') {c.save();c.font='500 25px Poppins';c.textAlign=align;c.fillStyle='#FFFFFF';c.shadowColor='rgba(0,0,0,.9)';c.shadowBlur=7;c.fillText(text,x,y);c.restore();}
function bot(c,x,feet,t,mode='focus',arm='reach',flip=false) {
 const done=mode==='done',alert=mode==='alert';
 const arrival=eInOut(t/.7),second=eInOut((t-2.1)/.65);
 const dx=snap((1-arrival)*(flip?104:-104)+second*(flip?-16:16));
 const walking=t<.7||(t>2.1&&t<2.75);
 const step=Math.floor(t*12)%2;
 const lift=walking?(step?4:0):(done&&t>3?Math.max(0,Math.sin((t-3)*Math.PI*2))*12:0);
 const blink=Math.floor(t*8)%23===0;
 const wave=done&&t>3.2?(Math.floor(t*8)%4<2?'wave1':'wave2'):arm;
 vShadow(c,x+dx+120,feet+4,150,lift,true);
 drawBot(c,x+dx,snap(feet-230-lift),10,{dark:true,halo:true,armR:wave,armL:walking?'out':'down',legs:walking?(step?'stepL':'stepR'):'stand',eyes:blink?'blink':done?'happy':alert?'wide':'focus',mouth:done?'grin':alert?'o':'smile',bulb:done?'aqua':alert?'red':'yellow',flip});
}
function card(c,x,y,w,h,fill=VC.W) {rr(c,x,y,w,h,10);fs(c,fill,VC.K,2.5);rr(c,x+16,y+19,w-32,12,3);fs(c,VC.A);for(let j=0;j<3;j++)stroke(c,[[x+16,y+53+24*j],[x+w-16,y+53+24*j]],'#B8D4D9',3);}
function corners(c,x,y,w,h,k,color=VC.A) {c.save();c.globalAlpha=clamp01(k);for(const [a,b,dx,dy] of [[x,y,1,1],[x+w,y,-1,1],[x,y+h,1,-1],[x+w,y+h,-1,-1]])stroke(c,[[a,b+dy*25],[a,b],[a+dx*25,b]],color,4);c.restore();}
function person(c,x,y,r=24) {c.beginPath();c.arc(x,y-r*.25,r*.42,0,Math.PI*2);fs(c,VC.K);c.beginPath();c.arc(x,y+r*.8,r*.82,Math.PI,Math.PI*2);c.closePath();fs(c,VC.K);}
function phone(c,x,y,k) {rr(c,x,y,92,130,13);fs(c,VC.K);rr(c,x+7,y+12,78,100,7);fs(c,VC.W);person(c,x+46,y+54,24);stroke(c,[[x+37,y+120],[x+56,y+120]],VC.A,3);if(k>0){c.beginPath();c.arc(x+82,y+10,11*eOut(k),0,Math.PI*2);fs(c,VC.Y,VC.W,3);}}
function tag(c,x,y,text,w=192) {rr(c,x,y,w,45,10);fs(c,'rgba(9,24,29,.88)');stroke(c,[[x+1,y+10],[x+1,y+35]],VC.A,3);note(c,text,x+16,y+31);}
const SCENES={
 1(c,t,S) {
   // Hero: ART walks into the real low-stock aisle and turns the signal into a reorder.
   corners(c,91,584,277,365,eOut((t-.4)/.5));
   if(t>.7&&t<2.1)vBeam(c,108+eInOut((t-.7)/1.4)*242,600,934);
   bot(c,492,1138,t,t>2.7?'done':'focus',t>2.2?'hold':'reach',true);
   if(t>1.7)vCurve(c,[365,757],[575,668],[804,859],eOut((t-1.7)/.8),VC.A,{arrow:true,dash:[6,8],lw:3});
   if(t>2.1){card(c,792,887+snap(24*(1-eOut((t-2.1)/.5))),146,176);note(c,'Next order',783,1110);}
   if(t>2.7)vBadge(c,865,955,(t-2.7)/.35,30);
 },
 2(c,t,S) {
   // A reorder card is prepared beside the mascot; real shelves remain visible.
   bot(c,636,1130,t,t>2.5?'done':'focus',t>.7?'reach':'down');
   const q=eOut((t-.6)/.7);card(c,846,910+22*(1-q),112,148);
   if(t>1.45)vCurve(c,[885,872],[759,675],[575,728],(t-1.45)/.7,VC.A,{arrow:true,dash:[5,8],lw:3});
   if(t>2.5)vBadge(c,902,951,(t-2.5)/.3,27);
 },
 3(c,t,S) {
   // The mascot works at the actual records table. The callout targets its papers.
   const x=snap(340+eInOut((t-.5)/1.1)*28);
   bot(c,x,978,t,'alert',t>1.5?'reach':'down');
   if(t>.6)corners(c,594,865,253,95,(t-.6)/.4);
   if(t>1.3)vCurve(c,[600,858],[591,764],[743,798],(t-1.3)/.6,VC.A,{arrow:true,dash:[6,8],lw:3});
   if(t>2.45)vMark(c,843,796,'!',(t-2.45)/.3,'bang',1.1);
 },
 4(c,t,S) {
   // Scan the photographed left shelf instead of adding a second drawn shelf.
   corners(c,91,584,277,365,Math.max(.2,eOut((t-.3)/.4)));
   if(t>.45&&t<1.85){let x=108+eInOut((t-.45)/1.4)*242;vBeam(c,x,600,934);}
   bot(c,452,1120,t,t>2.2?'done':'focus',t>2?'up':'reach',true);
   if(t>1.85){vCurve(c,[605,858],[515,700],[364,757],(t-1.85)/.5,VC.A,{arrow:true,dash:[6,8],lw:3});}
   if(t>2.25)vMark(c,378,667,'!',(t-2.25)/.3,'bang',1.05);
   tag(c,99,978,'Reorder point',210);
 },
 5(c,t,S) {
   // Connect the actual stock rack to the actual incoming-cart area.
   tag(c,100,670,'On hand',150);tag(c,780,670,'Incoming',180);
   corners(c,109,730,228,255,eOut((t-.4)/.5));
   if(t>1.1)corners(c,741,792,242,236,(t-1.1)/.5);
   const k=eOut((t-1.6)/.85);vCurve(c,[340,754],[540,592],[753,784],k,VC.A,{arrow:true,dash:[6,8],lw:3});
   bot(c,419,1130,t,t>2.8?'done':'focus',t>2?'hold':'reach');
   if(t>1.6)vLens(c,687,1001,34,604,1065);
   if(t>2.8)vBadge(c,551,724,(t-2.8)/.3,27);
 },
 6(c,t,S) {
   // One mascot and a visible fork. Cards occupy 270px, leaving the photo visible.
   stroke(c,[[534,918],[534,862],[301,862],[301,818]],VC.A,3,[6,8]);
   stroke(c,[[546,918],[546,862],[778,862],[778,818]],VC.A,3,[6,8]);
   const left=eInOut((t-.35)/1.1);
   if(t>.35){vSlip(c,390-left*190,962-left*33,72,86);}
   if(t>1.45)vBadge(c,227,927,(t-1.45)/.3,27);
   if(t>2.15){phone(c,797,908,(t-2.15)/.3);vCurve(c,[685,1000],[754,948],[791,950],(t-2.15)/.4,VC.A,{arrow:true,dash:[6,8],lw:3});}
   bot(c,420,1180,t,t>2.7?'done':'focus',t>1.7?'up':'reach');
 },
 7(c,t,S) {
   // A request on the photographed review table reaches a person, not a fake warehouse.
   card(c,92,866,152,190,VC.Y);
   bot(c,328,1015,t,'focus',t>1.7?'up':'reach');
   rr(c,684,828,282,234,18);fs(c,VC.W,VC.K,2.5);person(c,824,886,37);
   const choices=[['Review',701,944],['Adjust',831,944],['Approve',701,998],['Hold',831,998]];
   for(const [word,x,y] of choices){rr(c,x,y,116,40,8);fs(c,word==='Review'&&t>2.1?VC.T:'#F1F5F6',word==='Review'&&t>2.1?VC.A:'#D6E3E6',2);c.save();c.fillStyle=VC.K;c.font='500 21px Poppins';c.textAlign='center';c.fillText(word,x+58,y+28);c.restore();}
   vCurve(c,[253,881],[514,654],[674,852],eOut((t-.55)/1.2),VC.A,{arrow:true,dash:[6,8],lw:3});
   if(t>2.6){c.beginPath();c.arc(947,824,11,0,Math.PI*2);fs(c,VC.Y,VC.W,3);}
 },
 8(c,t,S) {
   // Routine completion attaches to real cartons; exceptions reach a human.
   tag(c,96,696,'Routine orders',230);tag(c,730,696,'Exceptions',200);
   corners(c,98,781,254,280,eOut((t-.3)/.5));
   if(t>1.25)vBadge(c,241,822,(t-1.25)/.3,27);
   if(t>2){phone(c,814,862,(t-2)/.3);vCurve(c,[657,984],[733,900],[806,915],(t-2)/.5,VC.A,{arrow:true,dash:[6,8],lw:3});}
   bot(c,424,1151,t,t>2.6?'done':'focus',t>2?'up':'reach');
 },
 9(c,t,S) {
   // Rule controls sit on the actual desk; the mascot gestures into the stockroom.
   rr(c,86,797,438,252,18);fs(c,'rgba(8,21,25,.93)','rgba(255,255,255,.24)',2);
   note(c,'Your rules',112,840);
   const k=eInOut((t-.4)/.8);
   for(let j=0;j<2;j++){let y=908+j*77;stroke(c,[[121,y],[488,y]],'#728D93',5);c.beginPath();c.arc(j?382:209+k*100,y,11,0,Math.PI*2);fs(c,VC.A,VC.W,2);}
   vCurve(c,[531,856],[660,694],[854,790],eOut((t-1.4)/.7),VC.A,{arrow:true,dash:[6,8],lw:3});
   bot(c,666,1143,t,t>2.6?'done':'focus',t>1.5?'up':'reach',true);
   if(t>2.65)vBadge(c,852,794,(t-2.65)/.3,28);
 }
};
