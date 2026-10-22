# Supplier said Tuesday. It's Friday. — Style 3

Current version: **v3, full eight-slide static review**. Each slide now has its own generated photographic setting, pose, expression and explanatory props. ART appears from the cover. No animation is included.

## Current downloads

`delivery-v3/` contains the ordered eight-page PDF, eight native 1080×1350 JPEGs, a contact sheet and a ZIP including the native PNGs. `delivery/` and `delivery-v2/` are superseded two-slide proofs.

## Scene logic

The sequence moves from an overdue delivery to paused work, delivery-record comparison, outgoing follow-up, response tracking, unresolved-delay escalation, a human decision handoff and a calm close. The response-tracking slide illustrates what ART does when a reply is received; the next slide covers the unanswered branch. No revised date, real supplier reply or guaranteed delivery is invented.

## Source and brand

All marketing copy is editable HTML, in local Preahvihear Regular. New illustrative photographs integrate variations of the supplied original dimensional mascot, using `mascot-point.png` as a strict reference. They are generated scenes, not customer photographs. The original ART vector geometry and clock hands are unchanged; the previously approved blue-and-black wordmark presentation is applied via CSS. No top watermark is added.

`content.json` remains the canonical eight-slide draft copy. `slides/` holds editable layouts and assets; `stills/` holds current native PNGs. `build-full.py` creates the layouts. `capture-full.py` audits browser fonts/copy/bounds; `print-full.py` renders reliable native PNGs through the PDF print pipeline; `export-full.py` packages them. The final PDF retains vector text and embedded Preahvihear rather than rasterizing typography. Historical `build.py` and `capture.py` reproduce earlier proofs and must not be used to rebuild v3.

## Validation

Chromium checked actual Preahvihear font use, body copy, image loads and content bounds for all eight slides. Full renders and decoded PDF pages were visually inspected. See `audit-full-v3.json`. The document remains a static design review, not a publication approval.
