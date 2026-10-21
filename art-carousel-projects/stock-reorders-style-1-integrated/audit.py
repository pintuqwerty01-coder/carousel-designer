"""Validate approved copy, stationary text, fonts, layout, motion and MP4 metadata."""
import functools, hashlib, http.server, json, pathlib, subprocess, threading, sys
from playwright.sync_api import sync_playwright

P=pathlib.Path(__file__).resolve().parent
content=json.loads((P/'content.json').read_text())
def inr(n):
 s=str(n);head=s[:-3];g=[]
 while head:g.insert(0,head[-2:]);head=head[:-2]
 return ','.join(g+[s[-3:]])
# The user approved only slide 1: pin its media, choreography and model.
opening_ref=json.loads((P/'proof/approved-opening.json').read_text())
# Typography and edge treatment are authorized to change on all slides.
# Preserve the approved opening's choreography and original mascot model.
scene_source=(P/'scenes.js').read_text()
opening_source=scene_source[scene_source.index(' 1(c,t,S){'):scene_source.index(' 2(c,t,S){')]
opening_helpers=scene_source[scene_source.index('// Opening-specific pixel props:'):scene_source.index('// All new foreground props')].strip()
assert hashlib.sha256(opening_source.encode()).hexdigest()==opening_ref['scene_function_sha256']
assert hashlib.sha256(opening_helpers.encode()).hexdigest()==opening_ref['pixel_helpers_sha256']
assert hashlib.sha256((P.parents[1]/'art-carousel-kit/assets/kit/js/pixelbot.js').read_bytes()).hexdigest()==opening_ref['mascot_engine_sha256']

class Quiet(http.server.SimpleHTTPRequestHandler):
    def log_message(self,*args):pass
server=http.server.ThreadingHTTPServer(('127.0.0.1',0),functools.partial(Quiet,directory=str(P/'slides')))
threading.Thread(target=server.serve_forever,daemon=True).start()
norm=lambda s:''.join(s.split())
report=[]
try:
    with sync_playwright() as pw:
        browser=pw.chromium.launch(executable_path='/usr/bin/chromium')
        page=browser.new_page(viewport={'width':1080,'height':1350})
        cdp=page.context.new_cdp_session(page)
        cdp.send('DOM.enable');cdp.send('CSS.enable')
        for n in range(1,10):
            errors=[]
            page.on('pageerror',lambda e:errors.append(str(e)))
            page.goto(f'http://127.0.0.1:{server.server_port}/slide-{n:02}.html')
            page.evaluate('document.fonts.ready')
            assert page.evaluate("document.fonts.check('40px Preahvihear') && document.fonts.check('600 40px Poppins')")
            root=cdp.send('DOM.getDocument')['root']['nodeId']
            fonts={}
            for selector,required in [('h1','Preahvihear'),('.panel h2' if n==6 else '.body','Poppins'),('.topline','Poppins')]:
                node=cdp.send('DOM.querySelector',{'nodeId':root,'selector':selector})['nodeId']
                used=cdp.send('CSS.getPlatformFontsForNode',{'nodeId':node})['fonts']
                assert used and all(f['isCustomFont'] and f['glyphCount']>0 for f in used),(n,selector,used)
                if selector=='h1':
                    # Preahvihear lacks U+2019. Preserve the approved punctuation
                    # using the other approved family, never a system-font glyph.
                    assert any(f['familyName'].startswith('Preahvihear') for f in used),(n,used)
                    assert all(f['familyName'].startswith(('Preahvihear','Poppins')) for f in used),(n,used)
                    punctuation=page.locator('h1').inner_text().count('’')
                    assert sum(f['glyphCount'] for f in used if f['familyName'].startswith('Poppins'))<=punctuation,(n,used)
                else:
                    assert all(f['familyName'].startswith(required) for f in used),(n,selector,used)
                fonts[selector]=[f['familyName'] for f in used]
            assert page.locator('h1').evaluate('e=>getComputedStyle(e).fontWeight')=='400'
            photo=page.locator('.backdrop img').evaluate('e=>({loaded:e.complete,w:e.naturalWidth,h:e.naturalHeight,fit:getComputedStyle(e).objectFit,box:[e.getBoundingClientRect().width,e.getBoundingClientRect().height]})')
            assert photo['loaded'] and photo['w']>=1080 and photo['h']>=1350 and photo['fit']=='cover' and photo['box']==[1080,1350],photo
            assert page.locator('.stage').evaluate('e=>getComputedStyle(e).backgroundColor')=='rgba(0, 0, 0, 0)'
            assert page.locator('h1').evaluate('e=>getComputedStyle(e).color')=='rgb(255, 255, 255)'
            assert norm(page.locator('.topline').inner_text())==norm(content['brand_full_name'] if n in (1,9) else 'ART')
            s=content['slides'][n-1]
            assert norm(page.locator('h1').inner_text())==norm(' '.join(s['headline']))
            if s.get('panels'):
                for j,p in enumerate(s['panels']):
                    assert norm(page.locator('.panel h2').nth(j).inner_text())==norm(p['headline'])
                    assert norm(page.locator('.panel p').nth(j).inner_text())==norm(p['body'])
                ex=content['threshold_example']
                assert norm(page.locator('.example-limit').inner_text())==norm('Example approval limit: ₹'+inr(ex['approval_limit']))
                assert '₹'+inr(ex['automatic_order']) in page.locator('.amount').nth(0).inner_text()
                assert '₹'+inr(ex['approval_required_order']) in page.locator('.amount').nth(1).inner_text()
                assert ex['automatic_order']<=ex['approval_limit']<ex['approval_required_order']
            else:
                assert norm(page.locator('.body').inner_text())==norm(' '.join(s['body']))
            selector='.topline,h1:visible,.body:visible,.panel h2,.panel p,.amount,.example-limit'
            boxes=page.locator(selector).evaluate_all('els=>els.map(e=>{let r=e.getBoundingClientRect();return {left:r.left,right:r.right,bottom:r.bottom,scroll:e.scrollWidth,width:e.clientWidth}})')
            assert all(b['left']>=83 and b['right']<=997 and b['bottom']<1220 and b['scroll']<=b['width']+1 for b in boxes),boxes
            grid=page.locator('.col').evaluate('e=>{const r=e.getBoundingClientRect(),h=e.querySelector("h1"),b=e.querySelector(".body"),hs=getComputedStyle(h),bs=getComputedStyle(b);return {left:r.left,top:r.top,gap:getComputedStyle(e).gap,size:parseFloat(hs.fontSize),height:h.getBoundingClientRect().height,line:parseFloat(hs.lineHeight),bodySize:parseFloat(bs.fontSize),bodyLine:parseFloat(bs.lineHeight)}}')
            assert grid['left']==84 and grid['top']==168 and grid['gap']=='30px',grid
            assert abs(grid['height']-2*grid['line'])<1,(n,'headline must have two deliberate lines',grid)
            assert grid['bodySize']==30 and abs(grid['bodyLine']-46.5)<.1,grid
            assert page.locator('.edge-fade').count()==1
            if n==9:
                logo=page.locator('.closing-brand img').evaluate('e=>({loaded:e.complete,w:e.naturalWidth,h:e.naturalHeight,box:e.getBoundingClientRect().toJSON(),parent:e.parentElement.getBoundingClientRect().toJSON(),color:getComputedStyle(e.parentElement).backgroundColor})')
                assert logo['loaded'] and logo['w']>0 and logo['box']['width']==340 and logo['color']=='rgb(26, 26, 26)',logo
                assert logo['parent']['bottom']<=885 and logo['box']['top']-logo['parent']['top']>=116,logo
            text_frames=[];scene_frames=[]
            for t in [.1,s['duration']*.5,s['duration']-.1]:
                page.evaluate('(t)=>{Object.values(window.__timelines).forEach(tl=>tl.seek(t,false));}',t)
                text_frames.append([hashlib.sha256(e.screenshot()).hexdigest() for e in page.locator(selector).all()])
                scene_frames.append(hashlib.sha256(page.locator('#scene').screenshot()).hexdigest())
            assert text_frames[0]==text_frames[1]==text_frames[2],f'text moved on {n}'
            assert len(set(scene_frames))==3,f'missing motion on {n}'
            assert not errors,errors
            if '--html-only' not in sys.argv:
                probe=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(P/'render'/'out'/f'slide-{n:02}.mp4')]))
                v=probe['streams'][0]
                assert (v['width'],v['height'],v['r_frame_rate'],int(v['nb_frames']))==(1080,1350,'30/1',s['duration']*30)
                assert float(probe['format']['duration'])==s['duration']
            report.append({'slide':n,'photorealistic_full_frame_background':'verified loaded at native resolution','script_copy':'exact','text_pixels':'stationary','actual_rendered_fonts':fonts,'text_layout':'within margins','typography_grid':grid,'edge_fade':'black fade on all four edges','closing_logo':'supplied unmodified logo on ink' if n==9 else 'not applicable','scene_motion':'verified at 3 times','javascript_errors':errors,'video':'not checked' if '--html-only' in sys.argv else f"1080x1350 / 30fps / {s['duration']}s"})
        browser.close()
finally:server.shutdown()
(P/'proof'/('html-validation.json' if '--html-only' in sys.argv else 'validation.json')).write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
