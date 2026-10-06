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

The stock, paperwork and dispatch scenes reuse the kit library; the order-capture, setup and outcome scenes are specific to this draft. No LinkedIn slides have been produced; those remain a separate formal static asset.

If static headline pixels differ because of video compression, use the supported lossless encoder override for the affected slide:

    npm_config_cache=/workspace/art-carousel-npm-cache HYPERFRAMES_BROWSER_PATH=/usr/bin/chromium /workspace/art-carousel-venv/bin/python render-lossless.py 03

Slide 03’s uncompressed headline region was verified identical at 0.1s and 3.9s. The lossless override preserves the same checks and assertions.
