"""Copy finished deliverables to the post's deliverables folder (any folder the user chooses).

Usage: python publish.py <project_dir> <dest_dir> [--archive-as v5-something]
Copies render/out/*.mp4 -> dest/motion/, stills/*.png -> dest/stills/, content.json, cover/ (art, source.txt),
and writes dest/preview-all-slides.png (all stills in a row). If dest/motion already exists and --archive-as is
given, the old motion/ and stills/ are renamed to motion-<tag>/ and stills-<tag>/ first; without it they are replaced.
Never copies API keys or anything outside the project.
"""
import argparse, pathlib, shutil
from PIL import Image

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("project"); ap.add_argument("dest"); ap.add_argument("--archive-as", default="")
    a = ap.parse_args()
    p, d = pathlib.Path(a.project), pathlib.Path(a.dest); d.mkdir(parents=True, exist_ok=True)
    for sub in ["motion", "stills"]:
        if (d / sub).exists():
            if a.archive_as: (d / sub).rename(d / f"{sub}-{a.archive_as}")
            else: shutil.rmtree(d / sub)
        (d / sub).mkdir()
    mp4s = sorted((p / "render" / "out").glob("slide-*.mp4")); pngs = sorted((p / "stills").glob("slide-*.png"))
    for f in mp4s: shutil.copyfile(f, d / "motion" / f.name)
    for f in pngs: shutil.copyfile(f, d / "stills" / f.name)
    shutil.copyfile(p / "content.json", d / "content.json")
    if (p / "cover").exists():
        (d / "cover").mkdir(exist_ok=True)
        for f in (p / "cover").iterdir():
            if f.is_file(): shutil.copyfile(f, d / "cover" / f.name)
    if pngs:
        ims = [Image.open(f).resize((360, 450)) for f in pngs]
        sheet = Image.new("RGB", (370 * len(ims), 450), "white")
        for i, im in enumerate(ims): sheet.paste(im, (i * 370, 0))
        sheet.save(d / "preview-all-slides.png")
    print(f"published {len(mp4s)} MP4s, {len(pngs)} stills ->", d)
    for f in sorted(d.rglob("*")):
        if f.is_file() and f.parent.name in ("motion", "stills"): print("  ", f.relative_to(d))

if __name__ == "__main__":
    main()
