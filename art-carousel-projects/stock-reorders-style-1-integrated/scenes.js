// Scene-specific actions. Objects meet hands and the pictured work surfaces.
// No floating connectors, scan columns, generic arrival or celebration loops.
function ink(c,pts,color='#04ADC3',w=2){c.save();c.strokeStyle=color;c.lineWidth=w;c.lineCap='round';c.lineJoin='round';c.beginPath();pts.forEach(([x,y],i)=>i?c.lineTo(x,y):c.moveTo(x,y));c.stroke();c.restore();}
function text(c,s,x,y,size=23,color='#EDF3F3',weight=500){c.save();c.font=`${weight} ${size}px Poppins`;c.fillStyle=color;c.fillText(s,x,y);c.restore();}
function surfaceShadow(c,x,y,w){c.save();c.translate(x,y);c.scale(1,.16);let g=c.createRadialGradient(0,0,0,0,0,w/2);g.addColorStop(0,'rgba(0,0,0,.58)');g.addColorStop(1,'rgba(0,0,0,0)');c.fillStyle=g;c.beginPath();c.arc(0,0,w/2,0,Math.PI*2);c.fill();c.restore();}
function robot(c,x,feet,S,p={}){
 x=snap(x);feet=snap(feet);surfaceShadow(c,x+119,feet+3,155);
 const arm=p.arm||'down',flip=!!p.flip;
 drawBot(c,x,feet-230,10,{dark:true,halo:true,haloColor:'#F0EEE7',armR:arm,armL:p.left||(p.walk?'out':'down'),legs:p.walk?(S%2?'stepL':'stepR'):'stand',eyes:S%29===0?'blink':p.done?'happy':p.alert?'wide':flip?'lookL':'lookR',mouth:p.done?'smile':p.alert?'wobble':'flat',bulb:p.done?'aqua':p.alert?'red':'yellow',flip});
 const hand=arm==='hold'?[185,165]:arm==='tap'?[205,185]:arm==='up'?[195,115]:[215,155];
 return {x:x+(flip?240-hand[0]:hand[0]),y:feet-230+hand[1]};
}
function paper(c,x,y,w=120,h=150,angle=0){c.save();c.translate(x,y);c.rotate(angle);c.shadowColor='rgba(0,0,0,.23)';c.shadowBlur=12;c.shadowOffsetY=6;rr(c,0,0,w,h,3);fs(c,'#F4F0E7');c.shadowColor='transparent';ink(c,[[14,24],[w-14,24]],'#04ADC3',5);for(let i=0;i<4;i++)ink(c,[[14,48+i*19],[w-19-(i%2)*18,48+i*19]],'#9BA8A7',2);c.restore();}
function barcode(c,x,y,w=65,h=37){c.save();c.translate(x,y);c.transform(1,.015,-.045,1,0,0);rr(c,0,0,w,h,2);fs(c,'#EDE7DB');for(let j=0;j<20;j++){c.fillStyle='#353B3A';c.fillRect(6+j*(w-12)/20,7,1+(j%3===0),h-17);}c.restore();}
function device(c,x,y,w,h,title,rows,progress=0,done=false){
 surfaceShadow(c,x+w/2,y+h+7,w*1.15);
 c.save();c.translate(x,y);c.transform(1,.018,-.045,1,0,0);
 rr(c,0,0,w,h,13);fs(c,'#222A2B','#7D8786',2);rr(c,8,8,w-16,h-19,8);fs(c,'#112124');
 text(c,title,23,42,Math.min(23,(w-46)/(title.length*.57)));ink(c,[[23,58],[w-25,58]],'#415455',1);
 rows.forEach((r,j)=>text(c,r,23,88+j*31,Math.min(20,(w-46)/(r.length*.56)),'#D4DEDC',400));
 rr(c,22,h-43,w-45,11,5);fs(c,'#3A4848');rr(c,22,h-43,Math.max(1,(w-45)*clamp01(progress)),11,5);fs(c,done?'#2B907F':'#04ADC3');
 if(done)vBadge(c,w-32,h-37,1,12);
 c.restore();
}
function touch(c,x,y,k){if(k<=0||k>=1)return;c.save();c.globalAlpha=1-k;c.strokeStyle='#9BE3EC';c.lineWidth=2;c.beginPath();c.arc(x,y,6+22*k,0,Math.PI*2);c.stroke();c.restore();}
function scanner(c,hand,target,t,active){
 const angle=Math.atan2(target.y-hand.y,target.x-hand.x);
 const nozzle={x:hand.x+28*Math.cos(angle),y:hand.y+28*Math.sin(angle)};
 if(active){
  // The light starts at the actual nozzle and lands ONLY on the carton label.
  c.save();const g=c.createLinearGradient(nozzle.x,nozzle.y,target.x,target.y);g.addColorStop(0,'rgba(4,173,195,.02)');g.addColorStop(1,'rgba(4,173,195,.20)');c.fillStyle=g;c.beginPath();c.moveTo(nozzle.x,nozzle.y);c.lineTo(target.x-29,target.y-15);c.lineTo(target.x+29,target.y+15);c.closePath();c.fill();
  c.beginPath();c.rect(target.x-31,target.y-18,62,36);c.clip();const y=target.y-13+26*((t*1.5)%1);c.shadowColor='#04ADC3';c.shadowBlur=10;ink(c,[[target.x-31,y],[target.x+31,y]],'#9BE3EC',2.5);c.restore();
 }
 c.save();c.translate(hand.x,hand.y);c.rotate(angle);
 rr(c,-13,-7,23,14,4);fs(c,'#202C30','#B7C4C1',1.5);rr(c,0,-12,29,24,5);fs(c,'#2C3C40','#B7C4C1',1.5);rr(c,23,-8,7,16,2);fs(c,active?'#04ADC3':'#526769');c.restore();
}
function stamp(c,x,y,k){if(k<=0)return;const q=eOut(k);c.save();c.globalAlpha=q;c.translate(x,y);c.rotate(-.08);rr(c,-57,-21,114,42,4);fs(c,'rgba(43,144,127,.17)','#41A486',2);text(c,'ORDERED',-45,7,19,'#A7E3CC',600);c.restore();}
function scanShelf(c,t,S,hero=false){
 const arrival=eInOut(t/.85),x=456-arrival*196,feet=1116;
 // This label is on the front of the bottom carton, not in the empty shelf bay.
 barcode(c,108,900,64,37);
 const scan=t>.85&&t<2.3;
 const hand=robot(c,x,feet,S,{flip:true,arm:t>.8?'hold':'down',walk:t<.85,done:t>2.4});
 if(t>.8)scanner(c,hand,{x:140,y:919},t,scan);
 if(t>2.4){c.save();c.globalAlpha=eOut((t-2.4)/.35);device(c,718,755,256,153,hero?'Reorder prepared':'Stock rule triggered',['Low stock detected'],1,true);c.restore();}
 if(t>2.4)vBadge(c,181,914,eOut((t-2.4)/.25),15);
}
const SCENES={
 1(c,t,S){scanShelf(c,t,S,true);},
 2(c,t,S){
  // The order printer rests on the pictured workbench; the hand meets its button.
  const x=154+eInOut(t/.65)*84;
  surfaceShadow(c,527,859,188);
  rr(c,446,758,163,100,12);fs(c,'#C4C8C2','#526161',2);rr(c,457,777,141,20,4);fs(c,'#1A292B');
  const feed=eInOut((t-1.35)/1.15);if(t>1.35){c.save();c.beginPath();c.rect(453,798,148,160);c.clip();paper(c,468,803,122,feed*140+1);c.restore();}
  rr(c,452,818,23,20,4);fs(c,t>1.2?'#04ADC3':'#586F70');
  const hand=robot(c,x,900,S,{walk:t<.65,arm:t>.9&&t<1.4?'reach':t>2.6?'hold':'down',done:t>2.6});
  touch(c,hand.x,hand.y,(t-1.1)/.35);if(t>2.7)stamp(c,530,912,(t-2.7)/.25);
 },
 3(c,t,S){
  // Papers slide across the actual table into the mascot's reach.
  const x=356+eInOut(t/.65)*28,hand=robot(c,x,980,S,{walk:t<.65,arm:t>.7?'reach':'down',alert:true});
  for(let j=2;j>=0;j--){let q=eInOut((t-.65-j*.34)/.7);paper(c,700+j*14-q*(110+j*5),865+j*8,108,106,-.045+j*.025);}
  if(t>2.3){text(c,'Still checking…',584,1043,24,'#FFD166');}
  // A restrained vibration stays on the pictured handset, not in a floating bubble.
  if(t>.7&&t<2.7){c.save();c.globalAlpha=.45+.3*Math.sin(t*12);c.strokeStyle='#FFD166';c.lineWidth=2;c.beginPath();c.ellipse(909,871,61,17,-.3,3.8,5.4);c.stroke();c.restore();}
 },
 4(c,t,S){scanShelf(c,t,S,false);},
 5(c,t,S){
  // Check the label on the real incoming carton on the left trolley.
  barcode(c,260,780,42,44);
  const x=490-eInOut(t/.8)*100;
  const hand=robot(c,x,1080,S,{flip:true,walk:t<.8,arm:t>.8?'hold':'down',done:t>2.7});
  if(t>.8)scanner(c,hand,{x:281,y:802},t,t>.8&&t<2.1);
  if(t>2.15){c.save();c.globalAlpha=eOut((t-2.15)/.3);device(c,698,761,276,187,'Replenishment check',['On hand + incoming','Reorder only the gap'],eOut((t-2.15)/.65),t>2.85);c.restore();}
 },
 6(c,t,S){
  // Both examples are acted out beneath their own panels; no diagram connectors.
  const goLeft=eInOut((t-.2)/.85),goRight=eInOut((t-1.8)/1.1);
  const x=430-goLeft*128+goRight*294;
  // Both terminals rest directly on the pictured full-width records table.
  const sent=t>1.15;device(c,190,860,176,154,'₹6,000',[sent?'Order placed':'Within limit'],eOut((t-1.05)/.45),sent);
  device(c,779,860,170,154,'₹15,000',[t>3?'Review sent':'Above limit'],eOut((t-2.8)/.5),false);
  const walking=t>.2&&t<1.05||t>1.8&&t<2.9;
  const hand=robot(c,x,1016,S,{flip:t<1.8,walk:walking,arm:t>1.05&&t<1.65||t>2.9?'tap':'down',done:t>3.35});
  touch(c,hand.x,hand.y,(t-1.1)/.35);touch(c,hand.x,hand.y,(t-2.95)/.35);
  if(t>3.05){c.beginPath();c.arc(923,881,6,0,Math.PI*2);fs(c,'#FFD166');}
 },
 7(c,t,S){
  // Slide the review request along the photographed desk to a review terminal.
  const q=eInOut((t-.75)/1.2);
  paper(c,110+q*162,879-q*5,113,129,-.04+q*.04);
  const hand=robot(c,360,1015,S,{left:'out',arm:t>.7&&t<2.15?'reach':'tap'});
  device(c,565,800,393,220,'Your decision',['Review  ·  Adjust','Approve  ·  Hold'],0,false);
  rr(c,586,968,348,30,6);fs(c,t>2.1?'#6B5A30':'#39494B');text(c,t>2.1?'Waiting for your decision':'Request ready',600,990,20,t>2.1?'#FFD166':'#C4D5D4');
  rr(c,560,958,27,30,5);fs(c,'#04ADC3');touch(c,hand.x,hand.y,(t-2.2)/.35);
 },
 8(c,t,S){
  // One scan on the actual trolley carton; the exception is shown on a desk device.
  barcode(c,260,780,42,44);
  const x=405-eInOut(t/.7)*32,hand=robot(c,x,1080,S,{flip:true,walk:t<.7,arm:t>.7?'hold':'down',done:t>2.4});
  if(t>.7)scanner(c,hand,{x:281,y:802},t,t>.7&&t<1.65);
  if(t>1.8)vBadge(c,285,800,eOut((t-1.8)/.3),18);
  device(c,716,774,258,176,'Exceptions only',[t>2.2?'Review requested':'Routine order handled'],eOut((t-1.5)/.6),false);
  if(t>2.2){c.beginPath();c.arc(943,807,6,0,Math.PI*2);fs(c,'#FFD166');}
 },
 9(c,t,S){
  // ART reaches the actual control instead of waving beside it.
  device(c,94,795,421,243,'Your replenishment rules',[],0,false);
  const k=eInOut((t-1.15)/.7);
  const rows=[['Reorder point',876,232+k*100],['Amount limit',944,421]];
  rows.forEach(([label,y,x])=>{text(c,label,119,y-13,20,'#D4DEDC');ink(c,[[119,y+9],[493,y+9]],'#566D70',5);c.beginPath();c.arc(x,y+9,9,0,Math.PI*2);fs(c,'#04ADC3','#DAEFEC',2);});
  const x=674-eInOut(t/.8)*206;
  const hand=robot(c,x,1034,S,{flip:true,walk:t<.8,arm:t>.8&&t<2?'tap':t>2.6?'up':'down',done:t>2.6});
  rr(c,479,974,29,30,5);fs(c,'#04ADC3');text(c,'Save',427,995,17);touch(c,hand.x,hand.y,(t-1.05)/.4);
  if(t>2.5){rr(c,118,1005,350,24,5);fs(c,'#173331');text(c,'Rules saved. Routine handled.',132,1023,17,'#B8E2D5');}
 }
};
