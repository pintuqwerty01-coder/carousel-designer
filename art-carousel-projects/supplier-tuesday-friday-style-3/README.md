# Supplier said Tuesday. It's Friday. — Style 3

Current version: **v6, full eight-slide static review with clean facial geometry on slides 1, 2, 3 and 5**. Each slide now has its own generated photographic setting, pose, expression and explanatory props. ART appears from the cover. The full carousel is static. A single-slide motion test is available in `motion-preview/`.

## Current downloads

`delivery-v6/` contains the ordered eight-page PDF, eight native 1080×1350 JPEGs, a contact sheet and a ZIP including the native PNGs. `delivery/` and `delivery-v2/` are superseded two-slide proofs; `delivery-v3/`, `delivery-v4/` and `delivery-v5/` are superseded full sets.

## Scene logic

The sequence moves from an overdue delivery to paused work, delivery-record comparison, outgoing follow-up, response tracking, unresolved-delay escalation, a human decision handoff and a calm close. The response-tracking slide illustrates what ART does when a reply is received; the next slide covers the unanswered branch. No revised date, real supplier reply or guaranteed delivery is invented.

## Source and brand

All marketing copy is editable HTML, in local Preahvihear Regular. New illustrative photographs integrate variations of the supplied original dimensional mascot, using `mascot-point.png` as a strict reference. They are generated scenes, not customer photographs. The original ART vector geometry and clock hands are unchanged; the previously approved blue-and-black wordmark presentation is applied via CSS. No top watermark is added.

`content.json` remains the canonical eight-slide draft copy. `slides/` holds editable layouts and assets; `stills/` holds current native PNGs. `build-full.py` creates the layouts. `capture-full.py` audits browser fonts/copy/bounds; `print-full.py` renders reliable native PNGs through the PDF print pipeline; `export-v6.py` packages the current version. The final PDF retains vector text and embedded Preahvihear rather than rasterizing typography. Historical `build.py` and `capture.py` reproduce earlier proofs and must not be used to rebuild v3.

## Validation

Chromium checked actual Preahvihear font use, body copy, image loads and content bounds for all eight slides. Full renders and decoded PDF pages were visually inspected. See `audit-full-v3.json`. The document remains a static design review, not a publication approval.

## Expression correction — v4

Slides 1, 2, 3, 5, 6 and 7 have localized face edits referenced to the original mascot. Cute friendly pixel eyes and a small stepped smile replace stern, worried or irregular facial marks. Slides 4 and 8 already use the friendly face and are retained. Posture, gesture and props carry the scene context. Marketing copy and layout are unchanged.

## Content-matched expression/action revision — v5

The user approved a different emotional/action cue per slide. Gentle concern and puzzlement replace happy faces on the delay and missing-stock scenes; checking, sending and updating use attentive focus; escalation is concerned and alert. The human handoff stays reassuring and the closing stays relaxed and confident. See `expression-action-v5.json`. This supersedes the uniform-friendly-face direction of v4.

## Facial geometry correction — v6

Only slides 1, 2, 3 and 5 are revised: clean coherent eye shapes, well-spaced features and simple mouths replace fragmented marks. Concern, puzzlement and focus remain appropriate to the content. Other slide imagery, all copy and editable layout are retained.

## First motion test

`motion-preview/delivery/` contains a seven-second slide 4 supplier-follow-up test at 1080×1350 and 30 fps. It synchronizes a send press with confirmation and a pending supplier reply. The full static set remains the current complete delivery.
