# Rendering setup verified

Python 3.12 virtual environment: `/workspace/art-carousel-venv` with Pillow and Playwright.
Node 24.19, ffmpeg/ffprobe 7.1, GSAP 3.14.2 and original brand fonts are present.
HyperFrames 0.8.55 installed in the workspace npm cache; its doctor detects `/usr/bin/chromium` and ffmpeg.

The Playwright-managed browser download returned a network 403. Use the installed system Chromium through `/workspace/art-carousel-kit/run-system-browser.py` for the supplied stills/frame scripts. This runs workspace files over a local HTTP server internally.

For HyperFrames:

```sh
export npm_config_cache=/workspace/.npm-cache
export HYPERFRAMES_BROWSER_PATH=/usr/bin/chromium
```

No optional speech, transcription or music packages are needed for silent carousel clips. Transparent generated cut-outs avoid a rembg dependency.

Commands from this folder:

```sh
/workspace/art-carousel-venv/bin/python build.py
/workspace/art-carousel-venv/bin/python /workspace/art-carousel-kit/run-system-browser.py /workspace/art-carousel-style2-kit/scripts/stills.py .
/workspace/art-carousel-venv/bin/python /workspace/art-carousel-kit/run-system-browser.py /workspace/art-carousel-style2-kit/scripts/frames.py . 01,04
/workspace/art-carousel-venv/bin/python /workspace/art-carousel-style2-kit/scripts/render.py . 01,04
```

The scripts use the unpacked user guide at `/workspace/art-carousel-style2-kit`. Retain that folder. Do not create a worktree for this workflow.
