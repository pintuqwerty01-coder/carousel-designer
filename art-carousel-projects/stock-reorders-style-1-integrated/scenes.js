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

// All new foreground props follow the approved opening's stepped pixel geometry.
function actor(c,x,top,S,p={}){
 x=snap(x);top=snap(top);const lift=snap(p.lift||0),panic=p.mood==='panic',urgent=p.mood==='urgent',joy=p.mood==='joy',relief=p.mood==='relief';
 vShadow(c,x+120,top+234,155,lift,true);
 drawBot(c,x,top-lift,10,{dark:true,halo:true,haloColor:'#F0EEE7',flip:!!p.flip,legs:lift?'tuck':p.walk?(S%2?'stepL':'stepR'):'stand',armL:p.left||(p.walk?'out':'down'),armR:p.arm||'down',eyes:panic||urgent?'wide':S%31===0?'blink':joy||relief?'happy':p.eyes||'focus',mouth:panic?'o':urgent?'wobble':joy?'grin':relief?'smile':'flat',bulb:panic||urgent?'red':joy||relief?'aqua':'yellow',bulbOff:(panic||urgent)&&S%4===0});
 if((panic||urgent)&&p.sweat){const y=top-lift+70+(S%3)*10;pixelCells(c,[[x+200,y,1,2],[x+210,y+30,1,1]],'#9BE3EC');}
}
function stockBox(c,x,y,checked=false,w=140,h=140){
 x=snap(x);y=snap(y);surfaceShadow(c,x+w/2,y+h+4,w+35);
 pixelCells(c,[[x+10,y,w/10-2,h/10],[x,y+10,w/10,h/10-2]],'#F0EEE7');
 pixelCells(c,[[x+10,y+10,w/10-2,h/10-2]],'#96643E');
 pixelCells(c,[[x+10,y+10,w/10-4,h/10-3]],'#CB965F');
 pixelCells(c,[[x+20,y+20,w/10-6,1],[x+w/2-10,y+10,2,h/10-2]],'#E4C79E');
 pixelCells(c,[[x+30,y+h-70,8,5]],'#F0EEE7');
 if(checked)pixelTick(c,x+40,y+h-60,10);
 else pixelCells(c,[[x+40,y+h-60,1,3],[x+60,y+h-60,1,3],[x+80,y+h-60,1,3]],'#8A9290');
}
function pixelPaper(c,x,y,k=1,checked=false,amount=''){
 x=snap(x);y=snap(y);surfaceShadow(c,x+70,y+184,145);
 pixelCells(c,[[x+10,y,12,18],[x,y+10,14,16]],'#F0EEE7');
 pixelCells(c,[[x+20,y+20,10,1]],'#04ADC3');
 if(amount)text(c,amount,x+16,y+62,24,'#203136',600);
 for(let j=0;j<3;j++){
  const q=clamp01(k*3-j),count=Math.floor((9-j%2)*q);
  if(count)pixelCells(c,[[x+20,y+(amount?80:55)+j*20,count,1]],'#A5B3B0');
 }
 if(checked)pixelTick(c,x+80,y+135,7);
}
function pixelTray(c,x,y,w=160){pixelCells(c,[[x,y,w/10,2],[x-10,y-10,1,3],[x+w,y-10,1,3],[x+10,y+20,w/10-2,1]],'#6D817F');pixelCells(c,[[x+10,y,w/10-2,1]],'#DDECE9');}
function warning(c,x,y,S,colour='#F27A7A'){
 pixelCells(c,[[x-10,y,2,4],[x-10,y+50,2,1]],colour);
 if(S%4<2)pixelCells(c,[[x-30,y-10,1,2],[x+20,y-10,1,2],[x-10,y-30,2,1]],'#FFD166');
}
function pixelTruck(c,x,sec,checked){
 x=snap(x);c.save();c.translate(x,0);
 // The cab leads leftward into frame; cartons remain attached to the trailer.
 pixelCells(c,[[90,1080,30,2],[10,990,8,11],[10,980,5,1],[0,1010,1,9],[0,1100,9,1]],'#F0EEE7');
 pixelCells(c,[[100,1090,28,1],[20,1020,6,7]],'#04ADC3');
 pixelCells(c,[[20,1000,5,4]],'#203136');pixelCells(c,[[30,1010,3,2]],'#9BE3EC');
 pixelCells(c,[[0,1070,2,1]],'#FFD166');
 for(const cx of [45,145,345]){
  pixelCells(c,[[cx-15,1100,3,3],[cx-25,1110,5,1]],'#203136');
  const phase=Math.floor(Math.min(sec,2.7)*8)%2;pixelCells(c,[[cx-5,1110,1,1],[cx+(phase?5:-15),1110,1,1]],'#DDECE9');
 }
 stockBox(c,100,940,checked);stockBox(c,250,940,checked);
 c.restore();
}
function tabletInHands(c,x,top,sec,update){
 heroTablet(c,x+50,top+140,update);
 pixelCells(c,[[x+40,top+170,2,2]],'#04ADC3');
 const tap=Math.floor(sec*5)%3===0;
 heroArm(c,[[x+170,top+150],[x+180,top+140],[x+160,top+140],[x+160,top+(tap?160:130)]]);
}
function reviewHand(c,edge,y){
 edge=snap(edge);y=snap(y);
 // A person reaches from outside the frame and physically grips the request edge.
 pixelCells(c,[[edge+30,y-10,20,5]],'#203136');
 pixelCells(c,[[edge+30,y-10,4,5]],'#F0EEE7');
 pixelCells(c,[[edge,y,4,3],[edge-10,y+10,1,1],[edge+10,y-10,2,1]],'#D4A47B');
 pixelCells(c,[[edge,y,1,1],[edge+10,y-10,1,1]],'#ECC7A0');
}
function confetti(c,sec,start,x){
 const k=(sec-start)/1.2;if(k<0||k>1)return;
 const colours=['#04ADC3','#F0EEE7','#FFD166'];
 for(let j=0;j<8;j++){
  const dx=(j-3.5)*30*k,dy=-110*Math.sin(Math.PI*k)+j%3*15;
  pixelCells(c,[[snap(x+dx),snap(850+dy),1,1]],colours[j%3]);
 }
}
function pixelClock(c,x,y,k){
 surfaceShadow(c,x+80,1134,200);
 pixelCells(c,[[x+20,y,12,16],[x,y+20,16,12]],'#F0EEE7');
 pixelCells(c,[[x+20,y+10,12,14],[x+10,y+20,14,12]],'#04ADC3');
 pixelCells(c,[[x+30,y+20,10,12],[x+20,y+30,12,10]],'#EAF1EB');
 const angle=-Math.PI/2+Math.PI*1.8*(1-eOut(k));
 heroArm(c,[[x+75,y+75],[x+75+Math.cos(angle)*40,y+75+Math.sin(angle)*40]]);
 pixelCells(c,[[x+70,y+50,1,3],[x+80,y+80,3,1]],'#203136');
 pixelCells(c,[[x+50,y+160,6,2],[x+30,y+180,10,2]],'#6D817F');
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
  const sec=t*1.5,ready=sec>3.1,lift=eInOut((sec-3.35)/.45)*20;
  actor(c,380,690,S,{arm:sec>3.2?'reach':'down',mood:ready?'relief':'work',eyes:'lookR'});
  pixelPaper(c,595,740-lift,clamp01((sec-.65)/1.8),sec>2.6);
 },
 3(c,t,S){
  const sec=t*1.75,shock=sec>2.8&&sec<4.1,x=320-eInOut((sec-3)/.4)*24;
  actor(c,x,750,S,{arm:shock?'up':'reach',left:shock?'up':'down',mood:shock?'panic':'urgent',sweat:true});
  for(let j=2;j>=0;j--){
   const k=eInOut((sec-.4-j*.7)/.8);
   pixelPaper(c,760+j*20-k*(225+j*12),750-j*10,1,false);
  }
 },
 4(c,t,S){
  const sec=t*1.75,open=clamp01((sec-1.3)/.9),lid=Math.round(eOut(open)*4)*10;
  // A large cutaway carton makes the shortage visible, rather than a tiny meter.
  surfaceShadow(c,780,1134,300);
  pixelCells(c,[[660,920,24,21],[650,930,26,19]],'#F0EEE7');
  pixelCells(c,[[660,930,24,19]],'#96643E');
  pixelCells(c,[[670,940,21,15]],'#CB965F');
  pixelCells(c,[[680,950,20,10]],'#473C32');
  for(let j=0;j<3;j++){
   const used=j<2?clamp01((sec-.4-j*.5)/.65):0;
   if(used<1){c.save();c.globalAlpha=1-used;c.translate(690+j*60,970);c.scale(.5,.5);stockBox(c,0,0,false,120,140);c.restore();}
  }
  pixelCells(c,[[660,920-lid,24,2],[670,940-lid,22,1]],'#E4C79E');
  const alarm=sec>2.1,recoil=sec>2.15&&sec<3.3,x=430-(recoil?eOut((sec-2.15)/.3)*36:0);
  actor(c,x,900,S,{arm:recoil?'up':sec>3.3?'reach':'down',left:recoil?'up':'down',mood:recoil?'panic':alarm&&sec<4?'urgent':'work',sweat:recoil});
  if(alarm){warning(c,930,900,S);text(c,'LOW STOCK',697,1100,25,'#FFF5E8',600);}
  if(sec>4.3)text(c,'Check incoming next',610,1180,26);
 },
 5(c,t,S){
  const sec=t*2,arrive=eInOut((sec-.6)/2.1),truckX=1110-510*arrive;
  text(c,'On hand',105,945,27);text(c,'Incoming stock',635,892,27);
  stockBox(c,110,990,sec>1);
  pixelTruck(c,truckX,sec,sec>4.3);
  const working=sec>4.4;
  actor(c,350,900,S,{flip:sec<2.4,arm:working?'hold':sec>1.3?'up':'down',mood:sec>6.7?'relief':'work',eyes:sec<2.4?'lookL':'lookR'});
  if(working)tabletInHands(c,350,900,sec,clamp01((sec-4.55)/1.6));
  if(sec>6.5)text(c,'Incoming counted. Reorder only the gap.',275,1180,25);
 },
 6(c,t,S){
  const sec=t*2,leftDone=sec>2.2,right=sec>3.8;
  pixelTray(c,180,1110,175);pixelTray(c,800,1110,175);
  pixelPaper(c,198,930,clamp01((sec-.4)/1.2),leftDone);
  if(right)pixelPaper(c,818,930,clamp01((sec-3.8)/1.1),false);
  actor(c,420,900,S,{flip:!right,arm:right?'up':'reach',left:right?'up':'down',mood:right&&sec<6.4?'urgent':leftDone&&!right?'relief':'work',sweat:right&&sec<6.4});
  if(right)warning(c,972,865,S,'#FFD166');
 },
 7(c,t,S){
  const sec=t*2,approach=eInOut((sec-.55)/1.25),handoff=eInOut((sec-3.2)/1.2);
  const x=snap(260+170*approach),paperX=x+215+handoff*165;
  pixelTray(c,795,1120,180);
  text(c,'Your decision',790,865,27);
  actor(c,x,900,S,{walk:sec>.55&&sec<1.8,arm:sec<4.5?'reach':'down',left:sec<2.5?'up':'down',mood:sec<3.2?'urgent':'work',sweat:sec<3.2,eyes:'lookR'});
  pixelPaper(c,paperX,940,1,false,'₹15,000');
  if(sec<2.8)warning(c,985,892,S);
  if(sec>2.2){
   const reach=eInOut((sec-2.2)/.8),edge=1120+(x+355-1120)*reach+handoff*165;
   reviewHand(c,edge,1010);
  }
  if(sec>4.5)text(c,'Awaiting your decision',690,1180,25,'#FFD166');
 },
 8(c,t,S){
  const sec=t*1.75,release=eInOut((sec-1.25)/3.25)*690;
  // Checked routine orders leave on a physical pixel roller belt.
  pixelCells(c,[[90,1080,53,2],[100,1100,2,3],[610,1100,2,3]],'#6D817F');
  for(let j=0;j<12;j++)pixelCells(c,[[100+j*45,1080+(Math.floor(sec*8)%2)*5,2,1]],'#DDECE9');
  for(let j=0;j<3;j++)stockBox(c,110+j*180-release,940,true);
  pixelCells(c,[[625,1070,3,3],[635,1050,1,2]],'#04ADC3');
  text(c,'Routine orders',100,893,27);
  pixelTray(c,860,1120,135);pixelPaper(c,866,940,1,false);
  text(c,'Human review',832,900,25,'#FFD166');
  const jump=sec>4.9&&sec<5.7?Math.max(0,Math.sin((sec-4.9)/.8*Math.PI))*40:0;
  actor(c,620,900,S,{flip:true,arm:sec<1.25?'tap':sec>4.6?'up':'down',left:sec>4.6?'up':'down',mood:sec>4.6?'joy':'work',lift:jump,eyes:'lookL'});
  confetti(c,sec,5,740);
 },
 9(c,t,S){
  const sec=t*1.75;
  pixelClock(c,220,930,clamp01((sec-.4)/1.8));
  stockBox(c,810,990,sec>2.6);
  actor(c,470,900,S,{arm:sec>3.3?'up':'flex',left:sec>3.3?'up':'down',mood:sec>3.3?'joy':'relief',eyes:sec<2.4?'lookL':'open'});
  if(sec>3.5)text(c,'Put ART to work.',438,1180,26);
 }
};
