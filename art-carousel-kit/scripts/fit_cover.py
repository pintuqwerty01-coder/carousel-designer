"""Turn a free cover image (Google AI Studio / Gemini / Microsoft Designer output, or a Pexels/Unsplash photo)
into the cover art the build uses.

Usage: python fit_cover.py <image> <project_dir> [--anchor top|center|bottom] [--source "text"]
Writes <project_dir>/cover/cover-art.png (centre-cropped to 4:5, 1080x1350 or larger) and appends the source
(route, URL, photographer credit) to cover/source.txt.

Checks it prints (fix before building if any say WARN):
- resolution: the crop should be at least 1080 px wide, otherwise it will look soft
- headroom: the top 40% should be fairly dark and calm so the white headline reads (the slide adds a shade too)
- corners: a bright small blob in a bottom corner often means a visible watermark; crop or cover it
"""
import argparse, pathlib
from PIL import Image, ImageStat

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("image"); ap.add_argument("project")
    ap.add_argument("--anchor", default="center", choices=["top", "center", "bottom"])
    ap.add_argument("--source", default="")
    a = ap.parse_args()
    im = Image.open(a.image).convert("RGB"); w, h = im.size
    tw, th = (w, round(w * 5 / 4)) if w * 5 / 4 <= h else (round(h * 4 / 5), h)
    x0 = (w - tw) // 2
    y0 = {"top": 0, "center": (h - th) // 2, "bottom": h - th}[a.anchor]
    crop = im.crop((x0, y0, x0 + tw, y0 + th))
    if tw > 1280: crop = crop.resize((1280, 1600), Image.LANCZOS)      # plenty for a 1.05 push-in; keeps files small
    elif tw < 1080: print(f"WARN resolution: crop is only {tw}px wide; upscaling, may look soft. Prefer a bigger image.")
    if crop.width < 1080: crop = crop.resize((1080, 1350), Image.LANCZOS)
    out = pathlib.Path(a.project) / "cover"; out.mkdir(parents=True, exist_ok=True)
    crop.save(out / "cover-art.png")
    g = crop.convert("L"); W, H = g.size
    top = ImageStat.Stat(g.crop((0, 0, W, int(H * 0.4)))).mean[0]
    print(f"headroom brightness (top 40%): {top:.0f}/255", "OK" if top < 110 else "WARN: bright top; headline may be hard to read")
    for name, box in {"bottom-left": (0, int(H * .9), int(W * .2), H), "bottom-right": (int(W * .8), int(H * .9), W, H)}.items():
        s = ImageStat.Stat(g.crop(box));
        if s.extrema[0][1] > 235 and s.stddev[0] > 45: print(f"check {name} corner for a watermark")
    with open(out / "source.txt", "a", encoding="utf-8") as f:
        f.write(f"{pathlib.Path(a.image).name} -> cover-art.png ({crop.width}x{crop.height}, anchor {a.anchor}). Source: {a.source or 'not given'}\n")
    print("saved", out / "cover-art.png", f"{crop.width}x{crop.height}")

if __name__ == "__main__":
    main()
