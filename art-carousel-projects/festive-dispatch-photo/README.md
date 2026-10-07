# Festive dispatch — photographic motion revision 5

Exact source draft copy retained. Slides 01–06 use photographic camera motion: a gently eased pan/push across the existing image behind separate live copy; the baked cover uses a softly feathered scene mask below its lettering. Headlines, body copy, CTAs, footer and shading remain stationary. All added moving vector slips, boxes, scan bars, route lines and extra check marks have been removed. There is no articulated character animation; the mascot is part of the original photo plate.

Typography on slides 02–07 is explicitly locked: Preahvihear 400 for the headline and its accent words; Poppins 500 for body, what-if, outcome and reveal copy. The result arrow is an SVG alongside the preserved source character, avoiding a visible fallback font. The approved cover lettering remains exactly as supplied in its raster artwork.

Slide 07 now uses ink with white/grey copy and aqua emphasis. A white process strip and dark central inset make the aqua mascot distinct. Slide 08 and 09 HTML and still pixels are unchanged from their accepted versions. These three remain static for review.

Deliveries: `motion/render/out/slide-01.mp4` through `slide-06.mp4`; combined `motion/first-six-preview.mp4`. Format: 1080×1350, four seconds, 30fps, H.264 High/yuv420p and faststart. Static review: `proof/last-three.png`, `static-review.pdf` and `stills/`.

Rebuild: `build-statics.py` → `revise-endings.py` → `refine-photo-style.py` → `capture-statics.py` → `make-review.py` → `preview-endings.py` → `build-motion.py` → `motion/render-frames.py 1,2,3,4,5,6` → `validate-motion.py`. Browser scripts run through `/workspace/art-carousel-kit/run-system-browser.py` with `/workspace/art-carousel-venv/bin/python`. `audit-fonts.py` checks actual rendered font families through Chromium, not just CSS declarations. `motion/browser-check.py` tests actual video playback.

Draft is a design review, not production publication approval. GitHub assets are pushed for review.
