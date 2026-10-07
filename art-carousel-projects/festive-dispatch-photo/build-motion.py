from pathlib import Path
import shutil
p=Path(__file__).resolve().parent;m=p/'motion';shutil.copytree(p/'slides/assets',m/'slides/assets',dirs_exist_ok=True)
# Cover is the previously approved matching-image motion, not a new interpretation.
shutil.copy2(p/'corrected-cover.mp4',m/'render/out/slide-01.mp4')
js=r'''
const action=document.createElement('canvas');action.width=1080;action.height=1350;action.style='position:absolute;inset:0;pointer-events:none';document.querySelector('.photo').after(action);
const ac=action.getContext('2d');const N=NUMBER;
function ease(v){v=Math.max(0,Math.min(1,v));return v*v*(3-2*v)}
function line(x1,y1,x2,y2,k){ac.beginPath();ac.moveTo(x1,y1);ac.lineTo(x1+(x2-x1)*k,y1+(y2-y1)*k);ac.stroke()}
function check(x,y,k){ac.save();ac.globalAlpha=k;ac.fillStyle='#2B907F';ac.beginPath();ac.arc(x,y,23,0,Math.PI*2);ac.fill();ac.strokeStyle='white';ac.lineWidth=5;ac.beginPath();ac.moveTo(x-11,y);ac.lineTo(x-2,y+9);ac.lineTo(x+12,y-10);ac.stroke();ac.restore()}
function paper(x,y,a=1){ac.save();ac.globalAlpha=a;ac.fillStyle='white';ac.shadowColor='#0008';ac.shadowBlur=15;ac.fillRect(x,y,48,63);ac.shadowBlur=0;ac.fillStyle='#04ADC3';ac.fillRect(x+8,y+9,32,6);ac.fillStyle='#aaa';for(let i=0;i<3;i++)ac.fillRect(x+8,y+25+i*9,26,3);ac.restore()}
function box(x,y,a=1){ac.save();ac.globalAlpha=a;ac.fillStyle='#d5a36a';ac.strokeStyle='#6a462b';ac.lineWidth=2;ac.fillRect(x,y,57,49);ac.strokeRect(x,y,57,49);ac.fillStyle='#f3d3aa';ac.fillRect(x+24,y,10,49);ac.restore()}
function drawAction(t){ac.clearRect(0,0,1080,1350);ac.strokeStyle='#04ADC3';ac.lineWidth=5;ac.lineCap='round';ac.shadowColor='#04ADC3';ac.shadowBlur=10;
let k=ease((t-.55)/1.8),done=ease((t-2.6)/.35);
if(N===2){for(let i=0;i<4;i++){let q=ease((t-.3-i*.35)/.7);box(190+i*90,865-75*q,q)}line(175,863,580,863,ease((t-1.6)/1));}
if(N===3){let starts=[[365,485],[480,545],[610,605]];starts.forEach(([x,y],i)=>{let q=ease((t-.35-i*.18)/1.5);paper(x+(780-x)*q-24,y+(730-y)*q-32,1-ease((t-2.3)/.5));});check(814,704,done);}
if(N===4){line(133,565,133,748,k);box(105,560+140*k,Math.min(1,t*3));check(173,751,done);}
if(N===5){ac.save();ac.shadowBlur=0;ac.beginPath();ac.rect(685,540,250,235);ac.clip();let sy=545+220*k;ac.fillStyle='#04ADC344';ac.fillRect(685,sy-24,250,24);ac.strokeStyle='#04ADC3';line(685,sy,935,sy,1);ac.restore();check(884,795,done);}
if(N===6){ac.beginPath();ac.moveTo(215,785);ac.bezierCurveTo(420,805,440,665,735,672);ac.stroke();let x=215+520*k,y=785-113*ease(k);ac.fillStyle='#04ADC3';ac.beginPath();ac.arc(x,y,10,0,Math.PI*2);ac.fill();if(t>2.25){let q=ease((t-2.25)/.5);paper(765,652,1-q);check(793,682,q);}}
ac.shadowBlur=0;
}
tl.to({}, {duration:4,onUpdate:()=>drawAction(tl.time())},0);drawAction(0);
'''
for n in range(2,7):
 s=(p/f'slides/slide-{n:02d}.html').read_text();s=s.replace('render();\nwindow.__timelines',js.replace('NUMBER',str(n))+'\nrender();\nwindow.__timelines')
 (m/f'slides/slide-{n:02d}.html').write_text(s)
print('Five distinct scene actions built; matching cover retained')
