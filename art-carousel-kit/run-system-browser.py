"""Run an unchanged kit script using installed Chromium and local HTTP."""
import functools, http.server, pathlib, runpy, sys, threading
from playwright.sync_api import BrowserType, Page
class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args): pass
server = http.server.ThreadingHTTPServer(('127.0.0.1', 0), functools.partial(QuietHandler, directory='/workspace'))
threading.Thread(target=server.serve_forever, daemon=True).start()
original_launch, original_goto = BrowserType.launch, Page.goto
def launch(self, *args, **kwargs):
    kwargs.setdefault('executable_path', '/usr/bin/chromium')
    return original_launch(self, *args, **kwargs)
def goto(self, url, *args, **kwargs):
    if url.startswith('file:///workspace/'):
        url = f'http://127.0.0.1:{server.server_port}/' + url[len('file:///workspace/'):]
    return original_goto(self, url, *args, **kwargs)
BrowserType.launch, Page.goto = launch, goto
script = sys.argv.pop(1)
try: runpy.run_path(script, run_name='__main__')
finally: server.shutdown()
