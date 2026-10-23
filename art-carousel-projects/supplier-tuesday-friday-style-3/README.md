# Supplier said Tuesday. It's Friday. — Style 3

Current review: **static v12, six-slide supplier follow-through story with governance on slide 5**, in `static-v12/`. The original white-limb mascot treatment is retained. Static v7 records the copy and scene-logic revision. The previously approved static baseline is **v6, with clean facial geometry on slides 1, 2, 3 and 5**. Each slide now has its own generated photographic setting, pose, expression and explanatory props. ART appears from the cover. The full carousel is static. A single-slide motion test is available in `motion-preview/`.

## Current downloads

`delivery-v6/` contains the ordered eight-page PDF, eight native 1080×1350 JPEGs, a contact sheet and a ZIP including the native PNGs. `delivery/` and `delivery-v2/` are superseded two-slide proofs; `delivery-v3/`, `delivery-v4/` and `delivery-v5/` are superseded full sets.

## Scene logic

The sequence moves from an overdue delivery to paused work, delivery-record comparison, outgoing follow-up, response tracking, unresolved-delay escalation, a human decision handoff and a calm close. The response-tracking slide illustrates what ART does when a reply is received; the next slide covers the unanswered branch. No revised date, real supplier reply or guaranteed delivery is invented.

## Source and brand

All marketing copy is editable HTML, in local Preahvihear Regular. New illustrative photographs integrate variations of the supplied original dimensional mascot, using `mascot-point.png` as a strict reference. They are generated scenes, not customer photographs. The original ART vector geometry and clock hands are unchanged; the previously approved blue-and-black wordmark presentation is applied via CSS. No top watermark is added.

`static-v7/content.json` is the canonical copy for the current static review; root `content.json` records the earlier draft. `slides/` holds editable layouts and assets; `stills/` holds current native PNGs. `build-full.py` creates the layouts. `capture-full.py` audits browser fonts/copy/bounds; `print-full.py` renders reliable native PNGs through the PDF print pipeline; `export-v6.py` packages the current version. The final PDF retains vector text and embedded Preahvihear rather than rasterizing typography. Historical `build.py` and `capture.py` reproduce earlier proofs and must not be used to rebuild v3.

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

## Static v7 — copy and scene consistency

The user returned to the non-animated format and requested clear, natural sentences with headings, supporting copy and scene elements aligned on every slide. `static-v7/` retains the original approved images, faces, font, logo and layout, with revised copy and separate supplier-reply/no-reply branches. See `static-v7/README.md` for the per-slide rationale. This is a review revision; v6 and all motion exports remain unchanged.

## Static v8 — mascot model consistency

The user requested consistency in body size, shape, colour and details. All scenes are referenced to the same original ART mascot; short legs on slide 3 and the extended hanging arm on slide 2 receive specific anatomical corrections. The latest v7 copy and layout are retained. `static-v8/character-spec.md` records the shared model rules. This remains a static review revision.

## Static v9 — white limb colour correction

The user clarified that the mascot has no blue in its hands or legs and asked not to alter the design. The blue limb segments in v8 were incorrect. `static-v9/` removes those colours through localized scene edits, retaining the v8 copy/layout and existing character poses. White limbs, aqua head/torso and black shoes are the current explicit colour rule.

## Static v10 — concise copy without repeated boxes

Removed repeated captions, task prompts and redundant cards. Each heading hooks, the body adds context or mechanism, and the remaining boxes give evidence, detail or choices. The v9 mascot/scene images are referenced byte-for-byte without alteration. See `static-v10/README.md` for the slide-by-slide content roles.

## Six-slide static v12 — follow-through and alternate sourcing

The user approved the six-slide script and the governance addition on slide 5, then requested design. This sequence covers ongoing supplier updates/reminders, stock impact, approved alternatives, original-delivery accounting with policy-based execution and human exceptions, and a supplier-workflow CTA. `static-v12/` contains the full static design. Previous eight-slide deliveries are superseded review versions.
