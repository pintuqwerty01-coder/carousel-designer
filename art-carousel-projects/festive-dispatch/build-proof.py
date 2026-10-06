import importlib.util,json,pathlib,shutil
p=pathlib.Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('kitbuild','/workspace/art-carousel-kit/scripts/build.py');b=importlib.util.module_from_spec(spec);spec.loader.exec_module(b)
c={'template':'task','n':1,'of':4,'label':'Orders','scene':'festiveOrders','headline':'Orders buried in multiple places?','pain':'Orders come in by phone, chat and email, all at once. One gets lost in the scroll, and you only find out when the customer calls asking where it is.','whatif':'What if every order, from every channel, landed in one place, logged and tracked from the moment it came in?','outcome':['→ No order missed. No festive sale lost.']}
(p/'proof-content.json').write_text(json.dumps({'status':'review proof, unapproved draft','slide':3,'content':c},indent=2))
theme,css,inner,scene,canvas,js,dark=b.task(c)
css+='\n.tk-h{font-size:66px}.tk-pain{font-size:29px;line-height:1.35}.tk-col{gap:18px}.tk-whatif{font-size:29px;line-height:1.35}.chip{font-size:27px}.chip svg{display:none}\n'
lib=b.LIB+'\n'+(p/'scenes.js').read_text()
out=p/'slides';out.mkdir(exist_ok=True);shutil.copytree(b.KIT,out/'assets',dirs_exist_ok=True)
(out/'slide-03.html').write_text(b.page('festive-orders',theme,inner,css,scene,canvas,js,3,9,'@arealtimetech',dark,lib,{}))
print('Built draft proof slide-03 with exact source wording')
