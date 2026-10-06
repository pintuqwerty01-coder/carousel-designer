# Festive dispatch — simplified motion review

Draft review; exact source copy retained. Slides 02–09 are provided. The cover photo binary and Aiotrix logo are missing. The ART logo stays intact. LinkedIn is a separate asset and has not been produced.

## Current motion

Each scene has fixed robot staging, one main action, restrained supporting props, and a final hold. Props use smooth easing. The robot changes pose at the action and result beats, without running, hopping, blinking or waving loops.

- 02: One parcel waits at a gate; one delay marker fades in.
- 03: One order slip settles into one tray.
- 04: One reorder moves for approval; one carton appears afterward.
- 05: One document is scanned and checked beside one parcel.
- 06: One gate opens, one parcel passes, one customer notice settles.
- 07: One ribbon settles on a gift.
- 08: One carton is sealed and checked.
- 09: One envelope flap closes.

Timing: establish for the first second, action through roughly 2.5 seconds, resolve by 3 seconds, then hold. Stock and dispatch retain a short secondary confirmation beat. Text does not move. The source paragraphs are unchanged and remain dense; this revision simplifies illustration action, not approved copy.

## Files

Videos: `render/out/slide-02.mp4` through `slide-09.mp4`. Still images: `stills/`. Animation sheets: `proof/sheet-NN.png`. Overview: `proof/contact-sheet.png`. Original script: `source-script.md`. Caption: `caption.txt`. These filenames replace the previous versions.

## Rebuild in the cloud

Use this post-specific builder; the generic kit builder does not handle the setup/outcome layouts.

```bash
/workspace/art-carousel-venv/bin/python /workspace/art-carousel-projects/festive-dispatch/build-review.py
/workspace/art-carousel-venv/bin/python /workspace/art-carousel-kit/run-system-browser.py /workspace/art-carousel-kit/scripts/stills.py /workspace/art-carousel-projects/festive-dispatch
/workspace/art-carousel-venv/bin/python /workspace/art-carousel-kit/run-system-browser.py /workspace/art-carousel-kit/scripts/sheets.py /workspace/art-carousel-projects/festive-dispatch
npm_config_cache=/workspace/art-carousel-npm-cache HYPERFRAMES_BROWSER_PATH=/usr/bin/chromium /workspace/art-carousel-venv/bin/python /workspace/art-carousel-projects/festive-dispatch/render-lossless.py
/workspace/art-carousel-venv/bin/python /workspace/art-carousel-projects/festive-dispatch/encode-delivery.py
```

Lossless masters permit static-pixel checks, but their H.264 profile is unsuitable for many players. The final encoding step produces standard H.264 High, yuv420p and faststart for delivery. Minor compression differences between static pixels are possible in these final MP4s.
