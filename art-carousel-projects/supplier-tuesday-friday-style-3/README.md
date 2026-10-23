## Current review: static v19

Slide 2: entire Meet ART (A Realtime Tech) line enlarged to 54 px, above the 43 px supporting headline. ART remains bold. Updated PDF, JPEGs and ZIP: `static-v19/delivery/`. Other slides unchanged.

## Current review: static v18

Slide 2: ART bold emphasis (explicit user request), aligned regular supporting typography and an editable perspective-fitted tablet delivery interface. Approved marketing copy retained. Other slides unchanged. Latest downloads: `static-v18/delivery/`.

## Current review: static v17

Slide 2 uses the approved ART product introduction and supplier follow-through closing. Other slides are unchanged from v16. Downloads: `static-v17/delivery/` (7-page PDF, seven 1080 x 1350 JPEGs, overview and ZIP with PNGs). Canonical copy and editable HTML: `static-v17/content.json` and `static-v17/slides/`. Run `static-v17/render.py` to reproduce exports.

## Current review: static v16 (7 slides)

Pain-first cover, new ART introduction on slide 2, existing four workflow slides retained, and blue-and-white closing logo without a white background. Closing CTA: DM "DELIVERY" to discuss your supplier workflow.

Deliverables: `static-v16/delivery/` (PDF, seven 1080 x 1350 JPEGs, overview and ZIP with PNGs). Editable HTML and canonical copy are in `static-v16/`; reproduce with its `build.py` and `render.py`.

# Supplier said Tuesday. It's Friday. — Style 3

Current review: **static v15, redesigned pad and mobile text/elements on slides 1 and 2**, in `static-v15/`. The v14 closing-slide layout is retained. The six-slide supplier follow-through story and slide 5 governance are retained. The original white-limb mascot treatment is retained. Static v7 records the copy and scene-logic revision. The previously approved static baseline is **v6, with clean facial geometry on slides 1, 2, 3 and 5**. Each slide now has its own generated photographic setting, pose, expression and explanatory props. ART appears from the cover. The full carousel is static. A single-slide motion test is available in `motion-preview/`.

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

## Static v13 — closing-slide hierarchy and logo

Slide 6 has a larger original logo with white clear space, aligned logo/CTA columns, a stronger primary headline and balanced paragraph lines. Slides 1–5 and all marketing wording are retained unchanged.

## Static v14 — distinct upper-left brand placement

After further user feedback, the final slide is rebuilt: blue/black logo on a full-width white header, a left-aligned text column that clears the mascot, and a text-only bottom CTA. Slides 1–5, the mascot/photo and all words are retained.

## Static v15 — pad and mobile

Slide 1 has a delivery-status pad with aligned dates and status treatments. Slide 2 has a supplier follow-up conversation UI fitted to the phone. Main copy, photographs, mascot and slides 3–6 are retained.
