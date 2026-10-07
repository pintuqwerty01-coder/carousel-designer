# Font-corrected original photo review

Typography-only revision of the exact photo carousel linked by the user at Git commit `34b0fca7d8c6f6095556c55575df73ae5a609405`. This preserves that version's photographs, dimensional mascot, colours, scene graphics and layout rather than substituting the later 2D animation design.

Slides 02–09 use embedded Preahvihear Regular for headings and Poppins Medium for body copy, prompts, outcomes and footer text. Highlighted words inherit their surrounding font and weight. Font synthesis is disabled. Outcome arrows and benefit checks use vector paths instead of fallback font glyphs; the original characters are retained in the HTML copy. Native emoji in the original copy are retained.

Slide 01 is the original approved raster cover, byte-identical to the linked review. Its lettering is baked into the image and has not been retyped or claimed to be audited as a font.

Deliverables: nine 1080 × 1350 PNGs in `stills/`, nine-page `static-review.pdf`, and `proof/all-slides.png`. Source copy remains draft review, unchanged.

Regenerate with Playwright/Chromium using `capture-statics.py`, `make-review.py`, and `audit-fonts.py`. `fix-fonts.py` is idempotent and records the typography correction.
