# Festive dispatch — Preahvihear throughout

The user's typography rule overrides the earlier kit body-font rule: use Preahvihear Regular for all editable text, including headings, body, prompts, results, CTA, handle and slide numbers. Disable synthetic bold and italic. Use vector paths for arrows, checks and original script emoji so they do not introduce fallback fonts. Preserve the original ART logo artwork.

Slides 01–06 use the user's selected original photo review (`34b0fca7d8c6f6095556c55575df73ae5a609405`). Cover lettering was removed from a photographic plate, then the exact script was typeset in genuine Preahvihear. The cover remains the same warehouse/mascot concept; the cleaned plate is an image edit rather than a pixel-identical original.

Slides 07–09 use the user's selected closing layouts at `1e624103470e03b236a48151f680b5bf5f8bc660`: aqua hub reveal, alternating offset benefit rows on white, and calendar CTA on ink. Their typography uses Preahvihear too. Layouts, colours, mascot and original logo are retained.

Deliverables: `stills/slide-01.png` through `slide-09.png` (1080 × 1350), `static-review.pdf` (nine pages), `proof/all-slides.png`, `proof/last-three.png`. This is a static review, not a new animation export. Exact draft copy retained.

Regenerate with `capture-statics.py`, `make-review.py`, `preview-endings.py` and `audit-fonts.py` using Playwright/Chromium. `use-preahvihear.py` records the initial typography conversion and is idempotent.
