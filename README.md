# ART carousel designer kit

ART house-style carousel rendering kit and festive-dispatch draft review assets. This is a Python/Canvas/HyperFrames rendering workflow, not a deployed web application.

## Included

- `art-carousel-kit/`: unpacked kit, design references, fonts, GSAP, ART logo, cloud adapter and setup script.
- `art-carousel-projects/festive-dispatch/`: exact draft script, post-specific builders/scenes, slide HTML, stills, animation proofs, caption and MP4s for slides 02–09.
- `art-carousel-projects/example/`: original example and verified sample task video.
- `art-carousel-projects/festive-dispatch-review.zip`: review handoff pack.
- `source-documents/`: both uploaded source documents.

## Status

Draft review only. Eight festive slides were rendered at 1080×1350, 30 fps, four seconds with zero lint errors; layout/font checks and source-copy checks passed. Slide 03 uses lossless encoding to preserve static headline pixels. The reveal logo animation is exempt from static-pixel checks.

Slide 01 remains unfinished. The generated cover photo is visible in the originating chat but was not persisted locally; its prompt is in `art-carousel-projects/festive-dispatch/cover/generation-prompt.md`. The Aiotrix logo is also not supplied. LinkedIn assets have not been produced.

## Run in the prepared cloud environment

Use the existing checkout; cloud tasks are isolated, so no worktree is needed. The tested cloud scripts use `/workspace/art-carousel-kit`, `/workspace/art-carousel-projects`, and `/workspace/art-carousel-venv`; those original directories remain in the prepared snapshot.

```bash
bash /workspace/art-carousel-kit/setup-cloud.sh
/workspace/art-carousel-venv/bin/python /workspace/art-carousel-projects/festive-dispatch/build-review.py
/workspace/art-carousel-venv/bin/python /workspace/art-carousel-kit/run-system-browser.py /workspace/art-carousel-kit/scripts/stills.py /workspace/art-carousel-projects/festive-dispatch
```

For other machines, follow `art-carousel-kit/SKILL.md` to install Python 3.10+, Playwright/Pillow, Node 18+ and ffmpeg. The generic kit scripts resolve their assets relative to the kit directory. Cloud-specific helpers and festive builders currently contain absolute cloud paths; adapt those paths to your local checkout before using them elsewhere.

See the festive project README, validation report, cover brief and design plan for production limitations and render commands. Environment publication is handled separately in Codex environment settings; GitHub hosts the files.
