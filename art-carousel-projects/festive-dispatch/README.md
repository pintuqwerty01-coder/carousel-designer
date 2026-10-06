# Festive dispatch Instagram review proof

Status: DRAFT REVIEW. Source copy is preserved; not approved for publication. Slides 02–09 are provided. Slide 01 has not been created because the selected stock cover photo has not been supplied. The Aiotrix logo is also not supplied, so the reveal currently uses only the intact ART logo. Optional CTA logo omitted. ART clock parts are not animated.

Open proof/contact-sheet.png for all eight layouts. Still PNGs are in stills/. Four-second videos are in render/out/. Nine-frame animation proofs are in proof/sheet-NN.png. The caption is in caption.txt. Original script and editorial issues are in source-script.md and design-plan.md. Cover selection guidance is in cover-brief.md.

To rebuild these post-specific layouts:

    /workspace/art-carousel-venv/bin/python build-review.py

To check stills:

    /workspace/art-carousel-venv/bin/python /workspace/art-carousel-kit/run-system-browser.py /workspace/art-carousel-kit/scripts/stills.py /workspace/art-carousel-projects/festive-dispatch

To render the standard quality proof:

    npm_config_cache=/workspace/art-carousel-npm-cache HYPERFRAMES_BROWSER_PATH=/usr/bin/chromium /workspace/art-carousel-venv/bin/python /workspace/art-carousel-kit/scripts/render.py /workspace/art-carousel-projects/festive-dispatch

Do not run the generic kit builder on this project: it needs this post-specific builder for setup/outcome layouts and exact draft copy.

All eight slides now use post-specific festive choreography; none uses the original topic’s stock, paperwork, calls, reveal or CTA choreography. No LinkedIn slides have been produced; those remain a separate formal static asset.

If static headline pixels differ because of video compression, use the supported lossless encoder override for the affected slide:

    npm_config_cache=/workspace/art-carousel-npm-cache HYPERFRAMES_BROWSER_PATH=/usr/bin/chromium /workspace/art-carousel-venv/bin/python render-lossless.py 03

The updated videos use the lossless override to preserve static headline pixels; the same validation checks remain active.

## Motion revision v2

02: Pull a parcel train and recoil at a jam.
03: Catch falling order slips in a basket and file them.
04: Measure a low shelf, offer a reorder, pause for approval, then receive cartons.
05: Isolate a mismatched document, compare it, and release the corrected pack.
06: Divert a delayed parcel and send a customer envelope ahead.
07: Tie a bow on a festive parcel and present it.
08: Push a checked parcel along a clear conveyor and let it go.
09: Fold a note into an envelope and present it.

The existing video and still filenames are overwritten by this revision.

Playback delivery files use standard H.264 High, yuv420p and faststart. Do not distribute CRF 0 exports directly: their High 4:4:4 Predictive profile can fail on common players.
