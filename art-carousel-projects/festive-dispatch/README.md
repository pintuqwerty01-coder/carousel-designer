# Festive dispatch — simplified motion review

Draft review; exact source copy retained. Slides 02–09 are provided. The cover photo binary and Aiotrix logo are missing. The ART logo stays intact. LinkedIn is a separate asset and has not been produced.

## Current motion

Each slide has its own robot pose sequence and a scene derived from the copy. The previous shared reach-and-hold choreography is removed.

- 02: Parcels arrive from both sides; the same bot turns between queues, then becomes overwhelmed.
- 03: Phone, chat and email each produce an order. The bot collects the slips, turns and files all three in one register.
- 04: Stock disappears from a shelf. The bot counts, raises a draft reorder and waits for approval before another carton appears.
- 05: Order and dispatch document are compared. The bot tracks them with a magnifier, finds the red mismatch and stamps the checked document beside the parcel.
- 06: A parcel remains stopped at a delay. The bot raises an alert flag and sends a customer update ahead; notifying the customer does not magically resolve the delay.
- 07: The bot acts as a conductor, bringing order, stock, document and delivery symbols into alignment. The logo stays intact.
- 08: The bot carries a completed parcel to a customer counter and hands it over, depicting service rather than more processing.
- 09: The bot points toward a bookmark, then sends a DM envelope, matching the save/share and message invitation.

Robot poses retain the stepped house style. Props use smooth easing and finish in a stable hold. Copy remains verbatim.

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
