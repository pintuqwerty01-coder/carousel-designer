#!/usr/bin/env bash
set -euo pipefail
cd /workspace
command -v node >/dev/null
command -v ffmpeg >/dev/null
command -v ffprobe >/dev/null
test -x /usr/bin/chromium
python -m venv /workspace/art-carousel-venv
export PATH=/workspace/art-carousel-venv/bin:$PATH
export npm_config_cache=/workspace/art-carousel-npm-cache
python -m pip install --no-cache-dir playwright==1.63.0 pillow==12.3.0
python /workspace/art-carousel-kit/scripts/setup_assets.py
# The upstream probe uses bundled Chromium; the cloud adapter uses system Chromium.
python /workspace/art-carousel-kit/run-system-browser.py /workspace/art-carousel-kit/scripts/stills.py /workspace/art-carousel-projects/example
HYPERFRAMES_BROWSER_PATH=/usr/bin/chromium npx --yes hyperframes@0.8.55 --version
