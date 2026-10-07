// Six distinct articulated ART mascot scenes. 2D robot uses the original 24x24 brand grid.
// Background and all typography are fixed; robot poses advance at 8fps, props ease continuously.
function parcel2d(c,x,y,w=72,h=60){c.save();rr(c,x,y,w,h,5);fs(c,'#D5A36A',VC.K,2.5);c.fillStyle='#F1D4AA';c.fillRect(x+w*.43,y+1,w*.14,h-2);c.strokeStyle='#8B643E';c.lineWidth=2;c.beginPath();c.moveTo(x+2,y+12);c.lineTo(x+w-2,y+12);c.stroke();c.restore();}
function pixelArm(c,a,b){const steps=Math.max(1,Math.ceil(Math.max(Math.abs(b[0]-a[0]),Math.abs(b[1]-a[1]))/7));for(let i=0;i<=steps;i++){const q=i/steps,x=snap(a[0]+(b[0]-a[0])*q),y=snap(a[1]+(b[1]-a[1])*q);c.fillStyle='white';c.fillRect(x-3,y-3,16,16);}for(let i=0;i<=steps;i++){const q=i/steps;c.fillStyle=VC.A;c.fillRect(snap(a[0]+(b[0]-a[0])*q),snap(a[1]+(b[1]-a[1])*q),10,10);}}
function actorPose(c,x,y,p){vShadow(c,x+120,y+236,142,0,true);drawBot(c,x,y,10,{dark:true,halo:true,haloColor:'#FFFFFF',...p});}
function actorEnvelope(c,x,y,w=76,h=51){rr(c,x,y,w,h,7);fs(c,VC.W,VC.K,2.5);c.beginPath();c.moveTo(x+5,y+7);c.lineTo(x+w/2,y+h*.58);c.lineTo(x+w-5,y+7);fs(c,null,VC.A,4);}
function actorPhone(c,x,y,t,done){c.save();c.translate(x,y);c.scale(1.6,1.6);vPhone(c,0,0,t,!done,eOut((t-2.5)/.45),'call');c.restore();}
function actorTray(c,x,y,w=130){vTrayBack(c,x,y,w,25);vTrayFront(c,x,y,w,25);}
function sceneCover(c,t,S){
 const walking=t<2.1,x=430+220*eInOut(t/2.1),y=760+(walking&&S%2?4:0),transfer=eInOut((t-2.1)/.65);
 // A single parcel is carried toward dispatch, then handed into the waiting tray.
 actorTray(c,912,1005,104);
 const p={legs:walking?walkLegs(S):'stand',armL:walking?'out':'down',armR:walking?'hold':t<2.75?'reach':'down',eyes:t<2.75?'lookR':S===29?'blink':'happy',mouth:t<2.75?'smile':'grin',bulb:'aqua'};
 actorPose(c,x,y,p);parcel2d(c,x+180+(912-(650+180))*transfer,y+151+58*transfer,72,60);
 if(t>=2.75)vBadge(c,994,998,eOut((t-2.75)/.4),17);
 window.__actorState={slide:1,x,y,...p,parcel:[x+180+82*transfer,y+151+58*transfer]};
}
function sceneQueue(c,t,S){
 const x=492,y=620,working=t>=1.15,done=t>=2.95;
 // Fixed stance: queue grows on the left; the bot raises its arms and routes each sheet overhead.
 for(let i=0;i<3;i++){
  const arrive=eOut((t-i*.28)/.45),start=1.2+i*.48,k=eInOut((t-start)/.72);
  if(t<start)vPaper(c,310-110*(1-arrive),752-i*9,61,79,{alpha:arrive,rot:(i-1)*.07});
  else if(k<1){const pt=qb([310,752-i*9],[640,280],[813,756-i*8],k);vPaper(c,pt[0],pt[1],61,79,{rot:Math.sin(k*Math.PI)*.2});}
  else vPaper(c,813,756-i*8,61,79,{});
 }
 const p={legs:'stand',armL:done?'down':'up',armR:done?'tap':working?(S%2?'wave1':'wave2'):'flex',eyes:done?'happy':working?'focus':'wide',mouth:done?'smile':working?'flat':'wobble',bulb:done?'aqua':working?'yellow':'red',bulbOff:!working&&S%2===0};
 actorPose(c,x,y,p);actorTray(c,795,835,120);if(done)vBadge(c,900,828,eOut((t-2.95)/.4),19);
 window.__actorState={slide:2,x,y,...p,queue:Math.min(3,Math.floor(t/.28)+1),completed:Math.max(0,Math.min(3,Math.floor((t-1.2)/.48)))};
}
function channelGlyph(c,x,y,kind){c.save();rr(c,x,y,68,68,13);fs(c,VC.W,VC.K,2.5);c.translate(x+34,y+34);if(kind===0){c.save();c.translate(-18,-18);c.scale(1.5,1.5);c.fillStyle=VC.A;c.fill(HANDSET);c.restore();}else if(kind===1){rr(c,-21,-17,42,29,7);fs(c,VC.A);c.beginPath();c.moveTo(-12,10);c.lineTo(-17,21);c.lineTo(0,10);fs(c,VC.A);c.fillStyle='white';for(const z of [-11,0,11]){c.beginPath();c.arc(z,-3,3,0,7);c.fill();}}else actorEnvelope(c,-23,-16,46,32);c.restore();}
function sceneChannels(c,t,S){
 const destinations=[560,665,775],x=480+100*eInOut((t-1.6)/.6),y=640,done=t>=3.0;
 for(let i=0;i<3;i++)channelGlyph(c,170,destinations[i]-32,i);
 for(let i=0;i<3;i++){
  const k=eInOut((t-.4-i*.55)/1.15);if(k>0&&k<1){const pt=qb([245,destinations[i]-25],[540,455],[826,738-i*8],k);vPaper(c,pt[0],pt[1],51,67,{rot:(1-k)*.1});}
  if(k===1)vPaper(c,826,738-i*8,51,67,{});
 }
 const p={legs:t>1.6&&t<2.2?walkLegs(S):'stand',armL:t<1.6?'out':'down',armR:t<2.2?'reach':t<3?'tap':'down',eyes:t<1.6?'lookL':done?'happy':'lookR',mouth:done?'smile':'flat',bulb:done?'aqua':'yellow'};
 actorPose(c,x,y,p);actorTray(c,791,821,143);if(done)vBadge(c,911,815,eOut((t-3)/.35),18);
 window.__actorState={slide:3,x,y,...p,phase:t<1.6?'receive':t<3?'file':'captured'};
}
function sceneStock(c,t,S){
 const walk=eInOut((t-.3)/1.1),x=530-290*walk,y=641,drop=eInOut((t-1.55)/.85),done=t>=2.7;
 const bx=x-17+(190-(240-17))*drop,by=y+131+(672-(641+131))*drop;
 // Inspect an empty physical shelf, carry one replenishment carton, place it, then confirm.
 if(t<2.7)parcel2d(c,bx,by,74,64);else parcel2d(c,190,672,74,64);
 const p={flip:true,legs:t>.3&&t<1.4?walkLegs(S):'stand',armL:t<1.15?'down':done?'down':'out',armR:t<1.55?'hold':t<2.45?'down':done?'up':'down',eyes:done?'happy':'lookR',mouth:done?'smile':'flat',bulb:done?'aqua':t<.7?'red':'yellow'};
 actorPose(c,x,y,p);if(t>=1.55&&t<2.45){pixelArm(c,[x+60,y+150],[x+28,y+120]);pixelArm(c,[x+28,y+120],[bx+74,by+32]);}if(done)vBadge(c,253,665,eOut((t-2.7)/.35),17);
 window.__actorState={slide:4,x,y,...p,parcel:[bx,by],phase:t<1.55?'carry':t<2.7?'restock':'confirmed'};
}
function sceneDocuments(c,t,S){
 const x=395,y=635,scan=eInOut((t-.55)/1.4),stamping=t>2.05&&t<2.8,done=t>=2.8;
 vPaper(c,620,662,115,174,{head:VC.A});
 const p={legs:'stand',armL:'down',armR:stamping?'down':done?'down':'reach',eyes:done?'happy':'focus',mouth:done?'smile':'flat',bulb:done?'aqua':'yellow'};
 actorPose(c,x,y,p);
 if(t<2.05)vLens(c,650,696+73*scan,36,x+210,y+150);
 if(stamping){const press=Math.sin(Math.PI*clamp01((t-2.05)/.75));const wrist=[645,735+34*press];pixelArm(c,[x+170,y+150],[605,755]);pixelArm(c,[605,755],wrist);vStamp(c,645,wrist[1]+40);}
 if(t>=2.43)vStampMark(c,645,809,eOut((t-2.43)/.35));
 window.__actorState={slide:5,x,y,...p,lensY:696+73*scan,phase:t<2.05?'inspect':t<2.8?'stamp':'verified'};
}
function sceneDispatch(c,t,S){
 const x=440,y=642,sending=t>=1.1,done=t>=2.65,k=eInOut((t-1.1)/1.35);
 actorPhone(c,818,865,t,done);
 if(!sending)vMark(c,240,760,'!',eOut(t/.15)*(1-eOut((t-.85)/.25)),'bang',1.2);
 const p={legs:'stand',armL:sending?'down':'up',armR:done?'down':sending?'reach':'hold',eyes:done?'happy':sending?'lookR':'lookL',mouth:done?'smile':sending?'flat':'o',bulb:done?'aqua':sending?'yellow':'red',bulbOff:!sending&&S%2===0};
 actorPose(c,x,y,p);
 if(k<1){const pt=qb([x+210,y+140],[730,614],[800,745],k);actorEnvelope(c,pt[0],pt[1],65,45);}
 window.__actorState={slide:6,x,y,...p,envelopeProgress:k,phase:!sending?'delay':done?'updated':'send'};
}
function renderArtActors(n,t){const canvas=document.getElementById('hero-2d'),c=canvas.getContext('2d'),S=Math.floor(t*8+1e-6);c.clearRect(0,0,1080,1350);[null,sceneCover,sceneQueue,sceneChannels,sceneStock,sceneDocuments,sceneDispatch][n](c,t,S);}
