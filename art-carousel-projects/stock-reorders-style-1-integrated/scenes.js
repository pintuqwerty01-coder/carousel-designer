// Scene-specific actions. Objects meet hands and the pictured work surfaces.
// No floating connectors, scan columns, generic arrival or celebration loops.
function ink(c,pts,color='#04ADC3',w=2){c.save();c.strokeStyle=color;c.lineWidth=w;c.lineCap='round';c.lineJoin='round';c.beginPath();pts.forEach(([x,y],i)=>i?c.lineTo(x,y):c.moveTo(x,y));c.stroke();c.restore();}
function text(c,s,x,y,size=23,color='#EDF3F3',weight=500){c.save();c.font=`${weight} ${size}px Poppins`;c.fillStyle=color;c.fillText(s,x,y);c.restore();}
function surfaceShadow(c,x,y,w){c.save();c.translate(x,y);c.scale(1,.16);let g=c.createRadialGradient(0,0,0,0,0,w/2);g.addColorStop(0,'rgba(0,0,0,.58)');g.addColorStop(1,'rgba(0,0,0,0)');c.fillStyle=g;c.beginPath();c.arc(0,0,w/2,0,Math.PI*2);c.fill();c.restore();}
function robot(c,x,feet,S,p={}){
 x=snap(x);feet=snap(feet);surfaceShadow(c,x+119,feet+3,155);
 const arm=p.arm||'down',flip=!!p.flip;
 drawBot(c,x,feet-230,10,{dark:true,halo:true,haloColor:'#F0EEE7',armR:arm,armL:p.left||(p.walk?'out':'down'),legs:p.walk?(S%2?'stepL':'stepR'):'stand',eyes:S%29===0?'blink':p.done?'happy':p.alert?'wide':p.eyes||(flip?'lookL':'lookR'),mouth:p.done?'smile':p.alert?'wobble':'flat',bulb:p.done?'aqua':p.alert?'red':'yellow',flip});
 const hand=arm==='hold'?[185,165]:arm==='tap'?[205,185]:arm==='up'?[195,115]:[215,155];
 return {x:x+(flip?240-hand[0]:hand[0]),y:feet-230+hand[1]};
}
function paper(c,x,y,w=120,h=150,angle=0){c.save();c.translate(x,y);c.rotate(angle);c.shadowColor='rgba(0,0,0,.23)';c.shadowBlur=12;c.shadowOffsetY=6;rr(c,0,0,w,h,3);fs(c,'#F4F0E7');c.shadowColor='transparent';ink(c,[[14,24],[w-14,24]],'#04ADC3',5);for(let i=0;i<4;i++)ink(c,[[14,48+i*19],[w-19-(i%2)*18,48+i*19]],'#9BA8A7',2);c.restore();}

function pill(c,s,x,y,color='#04ADC3') {c.save();c.font='500 24px Poppins';const w=c.measureText(s).width+34;rr(c,x,y,w,43,7);fs(c,'rgba(14,26,28,.86)');ink(c,[[x+1,y+8],[x+1,y+35]],color,3);text(c,s,x+17,y+29,24);c.restore();}
function reveal(c,k,fn){c.save();c.globalAlpha=eOut(k);fn();c.restore();}
function person(c,x,y){c.save();c.fillStyle='#18272A';c.beginPath();c.arc(x,y,16,0,Math.PI*2);c.fill();c.beginPath();c.ellipse(x,y+35,30,23,0,Math.PI,Math.PI*2);c.fill();c.restore();}
// Opening-specific pixel props: user requested boxes in the mascot's art style.
function pixelCells(c,cells,colour,u=10){c.fillStyle=colour;for(const [x,y,w=1,h=1] of cells)c.fillRect(x,y,w*u,h*u);}
function pixelTick(c,x,y,size=10){pixelCells(c,[[x,y+size],[x+size,y+2*size],[x+2*size,y+size],[x+3*size,y],[x+4*size,y-size]],'#41A486',size);}
function heroBox(c,x,y,w,h,opening,checked,occupied=false){
 const lift=occupied?0:Math.round(Math.sin(Math.PI*clamp01(opening))*3)*10;
 surfaceShadow(c,x+w/2,1134,w+55);
 // Cut corners, block shading and 10px tape use the same geometry as ART.
 pixelCells(c,[[x+10,y,w/10-2,h/10],[x,y+10,w/10,h/10-2]],'#F0EEE7');
 pixelCells(c,[[x+10,y+10,w/10-2,h/10-2]],'#96643E');
 pixelCells(c,[[x+10,y+10,w/10-4,h/10-3]],'#CB965F');
 pixelCells(c,[[x+20,y+20,w/10-6,1]],'#E0B885');
 pixelCells(c,[[x+w/2-10,y+10,2,h/10-2]],'#E4C79E');
 // The lid opens and closes once as ART inspects this carton.
 pixelCells(c,[[x+10,y-lift,w/10-2,1]],'#F0EEE7');
 pixelCells(c,[[x+20,y-lift+10,w/10-4,1]],'#E0B885');
 if(lift){pixelCells(c,[[x+20,y+10,w/10-4,1]],'#473C32');pixelCells(c,[[x,y-lift+10,2,1],[x+w-20,y-lift+10,2,1]],'#CB965F');}
 const labelX=x+30,labelY=y+h-70;
 pixelCells(c,[[labelX,labelY,8,5]],'#F0EEE7');
 if(checked)pixelTick(c,labelX+10,labelY+10,10);
 else pixelCells(c,[[labelX+10,labelY+10,1,3],[labelX+30,labelY+10,1,3],[labelX+50,labelY+10,1,3]],opening>0&&opening<1?'#04ADC3':'#8A9290');
}
function heroTablet(c,x,y,update){
 x=snap(x);y=snap(y);
 // Landscape tablet. It starts visibly resting on the first carton.
 pixelCells(c,[[x+10,y,12,8],[x,y+10,14,6]],'#F0EEE7');
 pixelCells(c,[[x+10,y+10,12,6]],'#203136');
 pixelCells(c,[[x+20,y+20,10,4]],'#DDECE9');
 for(let j=0;j<3;j++)pixelCells(c,[[x+30,y+20+j*10,4+j,1]],update>(j+1)/4?'#04ADC3':'#A1B3B1');
 if(update>=1)pixelTick(c,x+90,y+30,5);
}
function heroArm(c,points){
 // Square stepping for the pickup forearm, rather than a smooth vector limb.
 const cells=[];
 for(let j=1;j<points.length;j++){
  const a=points[j-1],b=points[j],n=Math.max(1,Math.ceil(Math.hypot(b[0]-a[0],b[1]-a[1])/8));
  for(let k=0;k<=n;k++)cells.push([Math.round((a[0]+(b[0]-a[0])*k/n)/10)*10,Math.round((a[1]+(b[1]-a[1])*k/n)/10)*10]);
 }
 c.fillStyle='#F0EEE7';for(const [x,y] of cells)c.fillRect(x-4,y-4,18,18);
 c.fillStyle='#04ADC3';for(const [x,y] of cells)c.fillRect(x,y,10,10);
}

const SCENES={
 1(c,t,S){
  const sec=t*2; // The opening runs eight seconds, with five deliberate beats.
  const walking=sec<1.5;
  const x=snap(-250+670*eInOut(sec/1.5)),top=900;
  const first=clamp01((sec-1.65)/1.05),second=clamp01((sec-3)/1.05);
  const taking=clamp01((sec-4.2)/1.1),k=eInOut(taking);
  const updating=sec>5.5,done=sec>=7.1;
  // Lower the tablet beside the face before bringing it across to both hands.
  const lower=eInOut(k/.55),across=eInOut((k-.55)/.45);
  const tabX=650+(x+50-650)*across,tabY=910+(top+140-910)*lower;
  const update=clamp01((sec-5.65)/1.4);
  heroBox(c,650,990,140,140,first,sec>=2.7,true);
  heroBox(c,820,960,140,170,second,sec>=4.05);
  // Tablet continuity: on the carton from frame one, then carried to ART's hands.
  if(sec<4.2)heroTablet(c,650,910,0);
  surfaceShadow(c,x+119,1133,155);
  drawBot(c,x,top,10,{dark:true,halo:true,haloColor:'#F0EEE7',legs:walking?(S%2?'stepL':'stepR'):'stand',armL:walking?'out':'down',armR:walking?'down':sec<3?'reach':sec<4.2?'up':'hold',eyes:S%29===0?'blink':done?'happy':walking?'lookR':updating?'focus':'lookR',mouth:done?'grin':'flat',bulb:done?'aqua':'yellow'});
  if(sec>=4.2){
   heroTablet(c,tabX,tabY,update);
   if(taking<1){
    // Reach to the same tablet that was resting on the carton; follow its grip.
    const grip=[tabX+5+125*k,tabY+70-30*k];
    heroArm(c,[[x+170,top+150],[x+210,top+150],grip]);
   }else{
    // Left hand supports the tablet. Right forearm taps its visible screen.
    pixelCells(c,[[x+40,top+170,2,2]],'#04ADC3');
    const tapping=(sec>5.55&&sec<5.85)||(sec>6.15&&sec<6.45);
    heroArm(c,[[x+170,top+150],[x+180,top+140],[x+160,top+140],[x+160,top+(tapping?160:130)]]);
   }
  }
  if(done)text(c,'Stock updated',x+23,1180,25,'#DDECE9');
 },
 2(c,t,S){
  // At x=380 the photographed tabletop is y=875..982. Feet sit at y=920,
  // well inside its surface, rather than at y=1012 on the vertical apron.
  // The document edge shares the hand x; its base rests on that same surface.
  const hand=robot(c,380,920,S,{arm:'reach',done:t>2.55,eyes:'lookR'});
  paper(c,hand.x,752,158,168);
  if(t>1.65)vBadge(c,hand.x+120,887,eOut((t-1.65)/.65),21);
 },
 3(c,t,S){
  // Manual checking is the only scene with a pile of paperwork.
  robot(c,360-eInOut((t-2.4)/.5)*24,980,S,{arm:t>2.8?'up':t>.8?'reach':'down',alert:true});
  for(let j=2;j>=0;j--){const k=eInOut((t-.5-j*.3)/.75);paper(c,737+j*12-k*(142+j*5),867+j*10,104,103,-.07+j*.04);}
 },
 4(c,t,S){
  // A stock-data threshold, not a physical barcode scan.
  const x=96,y=810,w=252,k=eInOut((t-.6)/1.4),fill=236-k*151;
  ink(c,[[x,y],[x+w,y]],'rgba(255,255,255,.38)',5);
  ink(c,[[x,y],[x+fill,y]],'#04ADC3',5);
  ink(c,[[x+85,y-14],[x+85,y+14]],'#FFD166',3);
  text(c,'Reorder point',96,858,25);
  if(t>2.1)reveal(c,(t-2.1)/.35,()=>pill(c,'Rule triggered',96,910,'#FFD166'));
  robot(c,440,1120,S,{flip:true,arm:t>2?'up':'down',done:t>2.8});
 },
 5(c,t,S){
  // Labels identify the pictured stock and incoming trolley; no invented quantities.
  pill(c,'On hand',500,654);pill(c,'Incoming',111,715);
  if(t>.55)reveal(c,(t-.55)/.4,()=>{ink(c,[[494,695],[494,857]],'#04ADC3',2);ink(c,[[111,864],[111,886],[314,886]],'#04ADC3',2);});
  const flip=t<1.8;
  robot(c,406,1092,S,{flip,arm:t>.7&&t<2.7?'up':'down',done:t>2.8});
  if(t>2.65)reveal(c,(t-2.65)/.4,()=>pill(c,'Reorder only the gap',681,884));
 },
 6(c,t,S){
  // The approved amount panels are the visual. No second set of mini screens.
  const left=eInOut((t-.15)/.8),right=eInOut((t-1.9)/1.1),x=430-left*140+right*280;
  robot(c,x,1170,S,{flip:t<1.9,walk:t>.15&&t<.95||t>1.9&&t<3,arm:t>1&&t<1.8||t>3?'up':'down',done:t>3.55});
  if(t>1.1)vBadge(c,270,939,eOut((t-1.1)/.3),34);
  if(t>3.05)reveal(c,(t-3.05)/.3,()=>{rr(c,787,898,85,89,15);fs(c,'#F4F0E7');person(c,830,923);c.beginPath();c.arc(866,902,8,0,Math.PI*2);fs(c,'#FFD166');});
 },
 7(c,t,S){
  // Only the human-review slide uses a device. ART waits; it never approves itself.
  surfaceShadow(c,797,1046,188);
  c.save();c.translate(720,802);c.transform(1,.025,-.04,1,0,0);
  rr(c,0,0,156,237,17);fs(c,'#253337','#A0ABA6',2);rr(c,8,12,140,207,10);fs(c,'#F2EFE8');
  person(c,78,54);text(c,'₹15,000',29,127,23,'#18272A',600);
  text(c,'For your review',16,156,16,'#344E50');
  text(c,'Approve  /  Hold',15,193,15,'#344E50');
  if(t>1.5){c.beginPath();c.arc(143,17,8,0,Math.PI*2);fs(c,'#FFD166');}
  c.restore();
  robot(c,352,1016,S,{arm:t>.7&&t<1.8?'reach':'down',eyes:t>2?'open':'lookR'});
 },
 8(c,t,S){
  // Completion is attached to the actual dispatch carton, not another screen.
  const k=eInOut((t-.2)/1.5);
  robot(c,350+k*170,1120,S,{walk:t>.2&&t<1.7,arm:t>2.1?'flex':'down',done:t>2.1});
  if(t>1.8)vBadge(c,285,800,eOut((t-1.8)/.35),24);
 },
 9(c,t,S){
  // Quiet close: the mascot, the working environment and the existing call to action.
  const k=eInOut((t-.15)/1.05);
  robot(c,650-k*230,1128,S,{flip:true,walk:t>.15&&t<1.2,arm:t>1.8?'flex':'down',left:t>2.7?'up':'down',done:t>2.7,eyes:'open'});
 }
};
