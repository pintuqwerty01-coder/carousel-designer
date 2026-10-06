"""Frame sheets: 9 moments of each slide's animation on one image, so staging and timing can be checked by eye.

Usage: python sheets.py <project_dir> [01,02,...]   (default: all slides)
Writes <project_dir>/proof/sheet-NN.png. Task slides are cropped to the stage card; other slides are shown whole.
Look for: the robot never behind/under a prop, props never clipped by the stage edge, every beat readable,
checks popping in, nothing overlapping the headline.
"""
import pathlib, sys
from playwright.sync_api import sync_playwright
from PIL import Image, ImageDraw

TIMES = [0.3, 0.8, 1.3, 1.7, 2.1, 2.5, 2.9, 3.3, 3.95]

def main(project, nums=None):
    project = pathlib.Path(project).resolve()
    files = sorted((project / "slides").glob("slide-*.html"))
    if nums: files = [f for f in files if f.stem.split("-")[1] in nums]
    out = project / "proof"; out.mkdir(exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1080, "height": 1350})
        for f in files:
            n = f.stem.split("-")[1]; errs = []
            pg.on("pageerror", lambda e, errs=errs: errs.append(str(e)))
            pg.goto(f.as_uri(), wait_until="load"); pg.wait_for_timeout(700)
            box = pg.evaluate("(()=>{const e=document.querySelector('.stage'); if(!e) return null; const r=e.getBoundingClientRect();"
                              " return [Math.round(r.left),Math.round(r.top),Math.round(r.right),Math.round(r.bottom)]})()")
            crops = []
            for t in TIMES:
                pg.evaluate(f"Object.values(window.__timelines).forEach(tl => tl.seek({t}, false)); 0")
                tmp = out / "_tmp.png"; pg.screenshot(path=str(tmp)); im = Image.open(tmp).convert("RGB")
                crops.append((t, im.crop(tuple(box)) if box else im.resize((540, 675))))
            W, H = crops[0][1].size
            sheet = Image.new("RGB", (W * 3 + 40, (H + 34) * 3), "white"); d = ImageDraw.Draw(sheet)
            for j, (t, c) in enumerate(crops):
                x = (j % 3) * (W + 20); y = (j // 3) * (H + 34); sheet.paste(c, (x, y + 26)); d.text((x + 6, y + 6), f"t={t}s", fill="black")
            sheet.save(out / f"sheet-{n}.png")
            print(f"sheet-{n}.png", "errors:", errs or "none")
        b.close()
    (out / "_tmp.png").unlink(missing_ok=True)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2].split(",") if len(sys.argv) > 2 else None)
