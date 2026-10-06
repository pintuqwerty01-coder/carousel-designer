Object.assign(SCENES_DYN, {
 festiveOrders(ctx,t,S) {
  const k=eInOut(Math.max(0,Math.min(1,(t-1.2)/1.8)));
  const icons=['phone','chat','email'];
  const origins=[[330,60],[540,92],[650,190]];
  function card(x,y,label,done) {
   ctx.save();ctx.translate(x,y);ctx.fillStyle='#FFFFFF';ctx.strokeStyle='#1A1A1A';ctx.lineWidth=2.5;
   ctx.beginPath();ctx.roundRect(-40,-25,80,50,10);ctx.fill();ctx.stroke();
   ctx.strokeStyle='#04ADC3';ctx.beginPath();
   if(label==='email'){ctx.rect(-22,-12,44,24);ctx.moveTo(-22,-12);ctx.lineTo(0,3);ctx.lineTo(22,-12);}
   else if(label==='chat'){ctx.roundRect(-22,-12,44,24,6);ctx.moveTo(-10,12);ctx.lineTo(-18,20);ctx.lineTo(-18,10);}
   else {ctx.roundRect(-10,-18,20,36,4);ctx.moveTo(-4,12);ctx.lineTo(4,12);}
   ctx.stroke();ctx.restore();if(done>0)vBadge(ctx,x+40,y-22,done);
  }
  // Three generic channels move into one tray; no product UI or written labels.
  ctx.strokeStyle='#04ADC3';ctx.lineWidth=2.5;ctx.setLineDash([5,6]);
  origins.forEach(([x,y])=>{ctx.beginPath();ctx.moveTo(x,y+26);ctx.lineTo(490,270);ctx.stroke();});ctx.setLineDash([]);
  ctx.fillStyle='#DDF3F7';ctx.strokeStyle='#1A1A1A';ctx.lineWidth=3;
  ctx.beginPath();ctx.roundRect(350,245,320,67,14);ctx.fill();ctx.stroke();
  origins.forEach(([x,y],i)=>card(lerp(x,398+i*102,k),lerp(y,269,k),icons[i],(t-2.8-i*.15)/.3));
  vShadow(ctx,180,VF+4,120,0);
  drawBot(ctx,84,VY,8,{legs:'stand',armR:S<10?'up':S<22?'reach':'wave1',eyes:S<10?'wide':S<22?'focus':'happy',mouth:S<10?'wobble':S<22?'flat':'grin',bulb:S<10?'red':S<22?'yellow':'aqua',bulbOff:S<10&&S%2===0});
  if(S<10)vSweat(ctx,244,VY+48,t,1);
 }
});
Object.assign(SCENES_DYN, {
 festiveJourney(ctx,t,S) {
  const done = typeof SCENE_OPTS !== 'undefined' && SCENE_OPTS.done;
  const names=['order','stock','paper','dispatch'];
  [340,440,540,640].forEach((x,i)=>{
   ctx.fillStyle='#FFFFFF';ctx.strokeStyle='#1A1A1A';ctx.lineWidth=3;
   ctx.beginPath();ctx.roundRect(x-36,70,72,85,10);ctx.fill();ctx.stroke();
   ctx.strokeStyle='#04ADC3';ctx.beginPath();ctx.rect(x-18,90,36,30);ctx.moveTo(x-18,105);ctx.lineTo(x+18,105);ctx.stroke();
   if(done) vBadge(ctx,x+32,70,(t-.8-i*.45)/.3);
   else vMark(ctx,x,180,'!',(t-.5-i*.35)/.25,'bang',.7);
  });
  const k=eInOut(Math.min(1,t/3));
  ctx.fillStyle='#DDF3F7';ctx.strokeStyle='#1A1A1A';ctx.lineWidth=3;
  ctx.beginPath();ctx.roundRect(320,280,384,28,8);ctx.fill();ctx.stroke();
  const x=lerp(346,672,k);ctx.fillStyle='#FFFFFF';ctx.beginPath();ctx.roundRect(x-22,230,44,48,4);ctx.fill();ctx.stroke();
  ctx.beginPath();ctx.moveTo(x,230);ctx.lineTo(x,250);ctx.stroke();
  vShadow(ctx,180,VF+4,120,0);
  drawBot(ctx,84,VY,8,{eyes:done?'happy':'wide',mouth:done?'grin':'wobble',armR:S%4<2?'reach':'up',bulb:done?'aqua':'red',bulbOff:!done&&S%2===0});
 }
});
