"""Render the final frame of every slide as a PNG still and check the layout.

Usage: python stills.py <project_dir>
Writes <project_dir>/stills/slide-NN.png at exactly 1080x1350. Prints OK per slide, or the problem:
fonts not loaded, content running into the handle zone (below 1220px), or a wrong size.
Exit code 1 if any slide fails.
"""
import pathlib, sys
from playwright.sync_api import sync_playwright
from PIL import Image

def main(project):
    project = pathlib.Path(project).resolve()
    slides = sorted((project / "slides").glob("slide-*.html"))
    out = project / "stills"; out.mkdir(exist_ok=True)
    problems = []
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1080, "height": 1350})
        for f in slides:
            errs = []
            pg.on("pageerror", lambda e, errs=errs: errs.append(str(e)))
            pg.goto(f.as_uri(), wait_until="load"); pg.wait_for_timeout(800)
            # jump to the final frame with events ON so canvas scenes redraw (the still = the video's end state).
            # The trailing "; 0" matters: returning the GSAP timeline object to Playwright crashes the page.
            pg.evaluate("Object.values(window.__timelines || {}).forEach(t => t.progress(1, false)); 0")
            fonts_ok = pg.evaluate("document.fonts.check('40px Preahvihear') && document.fonts.check('600 40px Poppins')")
            bottom = pg.evaluate("Math.max(0, ...[...document.querySelectorAll('.col')].map(e => e.getBoundingClientRect().bottom))")
            png = out / (f.stem + ".png")
            pg.screenshot(path=str(png))
            w, h = Image.open(png).size
            status = []
            if errs: status.append("JS ERROR: " + errs[0][:120])
            if not fonts_ok: status.append("FONTS NOT LOADED")
            if bottom > 1220: status.append(f"content bottom {bottom:.0f}px runs into the handle zone")
            if (w, h) != (1080, 1350): status.append(f"size {w}x{h}")
            print(f.stem, f"{w}x{h}", f"content-bottom={bottom:.0f}", "OK" if not status else " | ".join(status))
            problems += status
        b.close()
    return 1 if problems else 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
