# Stock reorders — Style 1, revision 3

Approved script: `content.json`. The user approved the illustrated direction and requested clearer, cleaner execution and a price-threshold example on slide 5. ART appears from the beginning. No photos or paid image generation are used.

## Style 1 background revision

Requested change: use the original Style 1 background approach. Tasks now have the original white page, flat #EEF9FB scene stage and #DDF3F7 aqua copy strip with an aqua leading edge. Headline highlights and top counter pills use the primary #04ADC3. The cover and summary use open ink backgrounds instead of tinted scene cards, with the supplied logo on the summary. The closing slide stays aqua with a white scene card. Both threshold panels use the same pale-aqua treatment. The earlier no-photo direction remains in effect.

The approved script, illustrative price examples, scene timing and 240px mascot scale are unchanged. Revision 2 remains available on its own branch.

## Motion and clarity

The original 240px pixel mascot operates inside smooth vector stockroom scenes. Preahvihear headlines, Poppins body text, white/ink/aqua layouts, and green only for completion checks. All text is visible from frame one and remains stationary.

Actions proceed in sequence, then hold their outcomes. Repeated waving, flashing antennae, phone vibration, expanding rings and simultaneous actions have been removed. The cover depicts a reorder prepared against low stock, rather than implying that delivery instantly fills the shelf.

| Slide | Action |
| --- | --- |
| 01 | A low-stock shelf leads to a prepared reorder card. |
| 02 | Stock dwindles while manual checking sends the mascot between shelf and records. |
| 03 | A stock-level indicator crosses the marked reorder point; ART flags it. |
| 04 | ART compares stock on hand with an incoming order before the reorder check completes. |
| 05 | Example approval limit ₹10,000. The ₹6,000 order passes automatically first; the ₹15,000 request then stops at a closed gate and reaches a human notification. Both outcomes hold. |
| 06 | The exception request is routed to a person, with review/adjust/approve/hold choices. No approval is assumed. |
| 07 | Routine orders complete while exceptions remain with a person. |
| 08 | Rule controls are set; the order flow proceeds within them. |

The currency values are illustrative examples requested for clarity, not real configured spending rules. An amount within the limit is eligible for automatic ordering; an amount above it requires approval.

## Build, render and validate

Use the existing checkout and prepared virtual environment, with Node, Chromium and ffmpeg installed.

```bash
source /workspace/art-carousel-venv/bin/activate
cd /workspace/carousel-designer/art-carousel-projects/stock-reorders-style-1
python build.py
python /workspace/art-carousel-kit/run-system-browser.py /workspace/art-carousel-kit/scripts/stills.py "$PWD"
python /workspace/art-carousel-kit/run-system-browser.py /workspace/art-carousel-kit/scripts/sheets.py "$PWD"
export npm_config_cache=/workspace/art-carousel-npm-cache HYPERFRAMES_BROWSER_PATH=/usr/bin/chromium
python render-lossless.py
python audit.py
python package.py
```

Each per-slide master is 1080 × 1350, 30fps, 120 frames and four seconds. Lossless H.264 preserves stationary text. The combined 32-second MP4 and GIF are compressed review copies; the ZIP contains individual masters in posting order and static JPEGs.

Validation compares approved copy, checks the requested price examples and their relation to the limit, verifies fonts and margins, compares text screenshots across three moments, confirms scene motion, checks JavaScript errors and probes the final videos. Frame sheets support visual review of transitions and mascot/prop separation.

Earlier three-slide studies remain in Git history and on the `stock-reorders-style-1-preview` branch. The current revision is delivered separately on `stock-reorders-style-1-v3`.
