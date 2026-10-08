"""Use the supplied Style 2 kit's continuous strip, with a physical beacon blink and truck roll-to-stop.
All unreviewed slides remain scaffolding; only 01 and 04 are exported as proofs.
"""
from pathlib import Path
import importlib.util
KIT=Path('/workspace/art-carousel-style2-kit')
spec=importlib.util.spec_from_file_location('style2',KIT/'scripts/build.py');kit=importlib.util.module_from_spec(spec);spec.loader.exec_module(kit)
# Keep the ART logo static: an internal brand-mark animation is not approved.
kit.HANDS=''
cover=kit.t_cover
kit.TEMPLATES['cover']=lambda s,c:cover(s,c).replace('width:640px','width:720px',1)
original=kit.object_html
def obj(o,sx,imgdir,project):
 html,after=original(o,sx,imgdir,project)
 # Beacon flash remains attached to its actual glass dome rather than travelling on a diagram.
 if o.get('moment',{}).get('type')=='blink':
  html=html.replace('border-radius:6px;background:rgba(54,194,212,.9);box-shadow:0 0 18px 6px rgba(54,194,212,.8);','border-radius:50%;background:radial-gradient(ellipse,rgba(225,255,255,.95) 0%,rgba(54,194,212,.55) 28%,rgba(54,194,212,0) 72%);mix-blend-mode:screen;filter:blur(2px);')
 if o['id']=='truck':
  lamp='<div class="stallbeacon" style="position:absolute;left:71.5%;top:5%;width:6%;height:10%;border-radius:50%;background:radial-gradient(ellipse,rgba(235,255,255,1),rgba(54,194,212,.65) 35%,rgba(54,194,212,0) 72%);mix-blend-mode:screen;filter:blur(2px);opacity:0"></div>'
  html=html[:-6]+lamp+'</div>'
 return html,after
kit.object_html=obj
# CTA's extra engagement copy is absent from the user's script.
cta=kit.t_cta
kit.TEMPLATES['cta']=lambda s,c:cta(s,c).split('<div class="icons tx">')[0]
kit.JS=kit.JS.replace('r = o.rot + 0.25 * Math.sin(TAU * t * 2);','y=0; r = o.rot + ((t>o.drive.at && t<o.drive.at+o.drive.dur)?0.18*Math.sin(TAU*t*2):0);')
kit.JS=kit.JS.replace('  FLC.forEach', "  Q('.stallbeacon').forEach(e=>{let a=t-1.5;e.style.opacity=a<0?0:a>1.3?.65:Math.pow(Math.max(0,Math.sin(a*Math.PI*3)),2);});\n  FLC.forEach")
kit.main(Path(__file__).resolve().parent)
