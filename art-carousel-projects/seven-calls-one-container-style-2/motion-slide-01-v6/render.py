from pathlib import Path
import http.server
import json
import subprocess
import sys
import threading
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent
DELIVERY = ROOT / 'delivery'
DELIVERY.mkdir(exist_ok=True)
FPS = 30
DURATION = 10

class Quiet(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)
    def log_message(self, *args):
        pass

server = http.server.ThreadingHTTPServer(('127.0.0.1', 0), Quiet)
threading.Thread(target=server.serve_forever, daemon=True).start()

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(executable_path='/usr/bin/chromium', args=['--no-sandbox', '--disable-gpu'])
    page = browser.new_page(viewport={'width': 1080, 'height': 1350}, device_scale_factor=1)
    page.goto(f'http://127.0.0.1:{server.server_port}/index.html')
    page.evaluate('document.fonts.ready')
    page.evaluate('Promise.all(Array.from(document.images).map(i=>i.decode()))')
    assert page.evaluate("document.fonts.check('700 83px Poppins')")
    assert page.evaluate("document.fonts.check('400 35px Poppins')")
    for timestamp in [0, 0.7, 1.5, 2.4, 4.2, 5.4, 5.8, 6.6, 7.4, 9.5]:
        page.evaluate('(t)=>window.setTime(t)', timestamp)
        page.screenshot(path=str(DELIVERY / f'proof-{timestamp:04.1f}s.jpg'), type='jpeg', quality=94)
    if '--stills' not in sys.argv:
        output = DELIVERY / 'ART-seven-calls-slide-01-motion-v6-storyboard-10s.mp4'
        command = ['ffmpeg','-hide_banner','-loglevel','error','-y','-f','image2pipe','-vcodec','mjpeg','-r',str(FPS),'-i','-','-an','-c:v','libx264','-preset','medium','-crf','18','-pix_fmt','yuv420p','-r',str(FPS),'-movflags','+faststart',str(output)]
        ffmpeg = subprocess.Popen(command, stdin=subprocess.PIPE)
        for frame in range(FPS * DURATION):
            t = frame / FPS
            page.evaluate('(t)=>window.setTime(t)', t)
            ffmpeg.stdin.write(page.screenshot(type='jpeg', quality=94))
            if frame % FPS == 0:
                print(f'{t:.0f}/{DURATION}s', flush=True)
        ffmpeg.stdin.close()
        assert ffmpeg.wait() == 0
        probe = json.loads(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration:stream=width,height,r_frame_rate','-of','json',str(output)], text=True))
        assert abs(float(probe['format']['duration'])-DURATION)<.1
        assert probe['streams'][0]['width']==1080 and probe['streams'][0]['height']==1350
        print(f'Exported {output}, {probe["format"]["duration"]} seconds', flush=True)
    browser.close()
server.shutdown()
