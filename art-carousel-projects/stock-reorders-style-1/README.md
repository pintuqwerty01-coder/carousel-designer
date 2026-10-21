# Stock reorders — Style 1 motion preview

Approved script: `content.json`. User explicitly requested ART from the beginning, the within-limit/over-limit split, and a new illustrated cover instead of photography. These take precedence over the older curiosity/reveal and photo-cover defaults in the Style 1 guide.

## Concept: Inside ART's stockroom

One connected visual world follows a stock need into a reorder and through the spending rules. Smooth vector shelving, order cards and conveyors; original pixel mascot at the same 240px scale. White/ink/aqua, Preahvihear headlines and Poppins body text. Text is stationary and readable from the first frame. Green checks indicate completed work only.

First motion studies: cover (01), stock chasing (02), and the two rule paths (05). They are for visual review, not a finished eight-slide delivery. No paid image service or photo is used.

| Slide | Planned action |
| --- | --- |
| 01 | An empty shelf triggers a reorder card; the mascot handles it and the stock flow resumes. |
| 02 | Stock disappears while the mascot chases a shelf, spreadsheet and ringing phone. |
| 03 | A scanner spots the stock threshold and signals the mascot. |
| 04 | The mascot compares on-hand stock with an incoming shipment before drafting a request. |
| 05 | A smaller order passes automatically; a larger request stops and notifies a person. |
| 06 | The exception request reaches a human review desk with review/adjust/approve/hold choices. |
| 07 | Routine and exception routes operate together without blocking one another. |
| 08 | The mascot sets the rule controls and watches the replenishment loop run. |

## Reproduce

From this directory, with the prepared Python virtual environment:

```bash
python build.py
python /workspace/art-carousel-kit/run-system-browser.py /workspace/art-carousel-kit/scripts/stills.py "$PWD"
python /workspace/art-carousel-kit/run-system-browser.py /workspace/art-carousel-kit/scripts/sheets.py "$PWD" 01,02,05
export npm_config_cache=/workspace/art-carousel-npm-cache HYPERFRAMES_BROWSER_PATH=/usr/bin/chromium
python /workspace/art-carousel-kit/scripts/render.py "$PWD" 02,05
python render-lossless.py 01
python audit.py
```

The cover uses supported lossless H.264 encoding because the default delivery encode produced one changed headline pixel in the static-copy comparison. Per-slide masters remain at 1080 × 1350, 30fps and four seconds. Review MP4/GIF files are compressed viewing copies.

Following the Style 1 guide's instruction to show a finished sample before completing all slides, the remaining five slide animations await visual approval of these first studies.
