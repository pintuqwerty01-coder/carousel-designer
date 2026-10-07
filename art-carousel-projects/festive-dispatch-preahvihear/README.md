# Festive dispatch — Preahvihear throughout

The user's typography rule overrides the earlier kit body-font rule: use Preahvihear Regular for all editable text, including headings, body, prompts, results, CTA, handle and slide numbers. Disable synthetic bold and italic. Use vector paths for arrows, checks and original script emoji so they do not introduce fallback fonts. Preserve the original ART logo artwork.

Slides 01–06 use the user's selected original photo review (`34b0fca7d8c6f6095556c55575df73ae5a609405`). Cover lettering was removed from a photographic plate, then the exact script was typeset in genuine Preahvihear. The cover remains the same warehouse/mascot concept; the cleaned plate is an image edit rather than a pixel-identical original.

Slides 07–09 use the user's selected closing layouts at `1e624103470e03b236a48151f680b5bf5f8bc660`: aqua hub reveal, alternating offset benefit rows on white, and calendar CTA on ink. These closing concepts are now unified on the brand ink background (#1A1A1A), with white cards, matched heading positions and 28px card corners. Aqua is reserved for emphasis, links and small card edges rather than a full-slide background. The aqua mascot sits against ink or a contrasting card. The original mascot and ART logo artwork are retained. All typography remains Preahvihear.

Deliverables: `stills/slide-01.png` through `slide-09.png` (1080 × 1350), `static-review.pdf` (nine pages), `proof/all-slides.png`, `proof/last-three.png`. This is a static review, not a new animation export. Exact draft copy retained.

Regenerate with `capture-statics.py`, `make-review.py`, `preview-endings.py` and `audit-fonts.py` using Playwright/Chromium. `use-preahvihear.py` records the initial typography conversion and is idempotent. `refine-closing.py` records the shared closing design; `capture-closing.py` refreshes only slides 07–09.

Slide 02 hand artwork: Twemoji v14.0.2, Twitter and contributors, CC-BY 4.0. Source and licence are recorded in `slides/assets/point-down-attribution.txt`.
