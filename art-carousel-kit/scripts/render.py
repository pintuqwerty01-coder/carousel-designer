"""Lint, render and verify the MP4 for every slide (HyperFrames + GSAP, 4s, 1080x1350, 30fps).

Usage: python render.py <project_dir> [01,02,...]
Needs: Node (npx), ffmpeg/ffprobe on PATH. HyperFrames is pinned to 0.8.55.
HyperFrames wants ONE root composition per folder, so each slide is copied in turn to <project>/render/index.html.
Prints per slide: lint errors, size, fps, duration, and how many headline pixels changed between 0.1s and 3.9s
(must be 0 on task slides: text never moves; the cover photo and the reveal logo animate, so those two will differ).
Output: <project>/render/out/slide-NN.mp4
"""
import json, pathlib, re, shutil, subprocess, sys
from PIL import Image, ImageChops

SKILL = pathlib.Path(__file__).resolve().parent.parent
HF = "npx --yes hyperframes@0.8.55"

def sh(cmd, cwd):
    return subprocess.run(cmd, cwd=cwd, shell=True, capture_output=True, text=True, encoding="utf-8", errors="replace")

def frame(mp4, t, png):
    sh(f'ffmpeg -v error -y -ss {t} -i "{mp4}" -frames:v 1 "{png}"', mp4.parent)
    return Image.open(png).convert("L")

def main(project, nums=None):
    project = pathlib.Path(project).resolve()
    r = project / "render"; (r / "out").mkdir(parents=True, exist_ok=True)
    for f in ["package.json", "hyperframes.json"]: shutil.copyfile(SKILL / "assets" / "render" / f, r / f)
    (r / "meta.json").write_text(json.dumps({"id": project.name, "name": project.name}), encoding="utf-8")
    shutil.rmtree(r / "assets", ignore_errors=True); shutil.copytree(project / "slides" / "assets", r / "assets")
    slides = sorted((project / "slides").glob("slide-*.html"))
    if nums: slides = [s for s in slides if s.stem.split("-")[1] in nums]
    bad = 0
    for s in slides:
        n = s.stem.split("-")[1]; shutil.copyfile(s, r / "index.html")
        lo = sh(f"{HF} lint", r); lint = lo.stdout + lo.stderr
        m = re.search(r"(\d+) error\(s\)", lint); errs = int(m.group(1)) if m else -1
        mp4 = r / "out" / f"slide-{n}.mp4"
        rr = sh(f'{HF} render --quality delivery --fps 30 --output "out/slide-{n}.mp4"', r)
        if not mp4.exists(): print(n, "RENDER FAILED:", (rr.stdout + rr.stderr)[-400:]); bad += 1; continue
        probe = sh(f'ffprobe -v error -show_entries stream=width,height,r_frame_rate:format=duration -of csv=p=0 "{mp4}"', r).stdout.split()
        is_task = 'class="stage"' in s.read_text(encoding="utf-8")
        a = frame(mp4, 0.1, r / "_a.png").crop((0, 0, 1080, 400)); b = frame(mp4, 3.9, r / "_b.png").crop((0, 0, 1080, 400))
        moved = ImageChops.difference(a, b).point(lambda v: 255 if v > 40 else 0).histogram()[255]
        ok = errs == 0 and probe[:2] == ["1080,1350,30/1", "4.000000"] and (moved == 0 or not is_task)
        bad += 0 if ok else 1
        print(n, f"lint={errs} errors", " ".join(probe), f"headline-px-moved={moved}", "OK" if ok else "CHECK")
    for t in ["_a.png", "_b.png"]: (r / t).unlink(missing_ok=True)
    return 1 if bad else 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2].split(",") if len(sys.argv) > 2 else None))
