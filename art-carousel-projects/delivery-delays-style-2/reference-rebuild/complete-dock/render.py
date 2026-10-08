"""Lint, render and verify the MP4 for every slide (HyperFrames + GSAP, 4 s, 1080x1350, 30 fps).

Usage: python render.py <project> [01,02,...]
Needs: Node (npx), ffmpeg/ffprobe on the PATH, and proof/textboxes.json from stills.py (run stills.py first).
HyperFrames wants ONE root composition per folder, so each slide is copied in turn to <project>/render/index.html.
Prints per slide: lint errors, size, fps, duration, and text-moved: changed pixels inside the text blocks between
2.8 s and 3.9 s (after the tick marks and the light sweep have finished). It must be 0-30 (light flicker under text);
more means something is moving over or with the text.
Output: <project>/render/out/slide-NN.mp4
"""
import json, pathlib, re, shutil, subprocess, sys
from PIL import Image, ImageChops

SKILL = pathlib.Path('/workspace/art-carousel-style2-kit')
HF = "npx --yes hyperframes@0.8.55"

def sh(cmd, cwd):
    return subprocess.run(cmd, cwd=cwd, shell=True, capture_output=True, text=True, encoding="utf-8", errors="replace")

def frame(mp4, t, png):
    sh(f'ffmpeg -v error -y -ss {t} -i "{mp4}" -frames:v 1 "{png}"', mp4.parent)
    return Image.open(png).convert("L")

def main(project, nums=None):
    project = pathlib.Path(project).resolve()
    tb = project / "proof" / "textboxes.json"
    boxes = json.loads(tb.read_text(encoding="utf-8")) if tb.exists() else {}
    if not boxes: print("note: run stills.py first so the text check knows where the text is")
    r = project / "render"; (r / "out").mkdir(parents=True, exist_ok=True)
    for f in ["package.json", "hyperframes.json"]: shutil.copyfile(SKILL / "assets" / "render" / f, r / f)
    (r / "meta.json").write_text(json.dumps({"id": project.name, "name": project.name}), encoding="utf-8")
    shutil.rmtree(r / "assets", ignore_errors=True); shutil.copytree(project / "slides" / "assets", r / "assets")
    slides = sorted((project / "slides").glob("slide-*.html"))
    if nums: slides = [s for s in slides if s.stem.split("-")[1] in nums]
    bad = 0
    for s in slides:
        n = s.stem.split("-")[1]; shutil.copyfile(s, r / "index.html")
        lo = sh(f"{HF} lint", r); m = re.search(r"(\d+) errors?", lo.stdout + lo.stderr); errs = int(m.group(1)) if m else -1
        mp4 = r / "out" / f"slide-{n}.mp4"; mp4.unlink(missing_ok=True)
        rr = sh(f'{HF} render --quality delivery --fps 30 --output "out/slide-{n}.mp4"', r)
        if not mp4.exists(): print(n, "RENDER FAILED:", (rr.stdout + rr.stderr)[-400:]); bad += 1; continue
        probe = sh(f'ffprobe -v error -show_entries stream=width,height,r_frame_rate:format=duration -of csv=p=0 "{mp4}"', r).stdout.split()
        d = ImageChops.difference(frame(mp4, 2.8, r / "_a.png"), frame(mp4, 3.9, r / "_b.png")).point(lambda v: 255 if v > 40 else 0)
        moved = max([d.crop(tuple(b)).histogram()[255] for b in boxes.get(n, [])] or [0])
        ok = errs == 0 and probe[:2] == ["1080,1350,30/1", "4.000000"] and moved <= 30
        bad += 0 if ok else 1
        print(n, f"lint={errs} errors", " ".join(probe), f"text-moved={moved}", "OK" if ok else "CHECK")
    for t in ["_a.png", "_b.png"]: (r / t).unlink(missing_ok=True)
    return 1 if bad else 0

if __name__ == "__main__":
    if len(sys.argv) < 2: sys.exit(__doc__)
    sys.exit(main(sys.argv[1], sys.argv[2].split(",") if len(sys.argv) > 2 else None))
