# Concept B — one order, one journey

A separate two-slide marketing design experiment using the exact Instagram draft copy for slides 03 and 04. The approved current carousel remains in `festive-dispatch/`.

## Technique

- Persistent visual object: the same aqua-ribbon parcel connects the narrative.
- Matched motion between slides: parcel exits right and enters left at the same height, size and direction. This suggests continuity when swiping; Instagram controls the actual playback and swipe timing.
- Open hero stage: remove the rounded scene card and what-if box. A large parcel travels on a shared full-width route; the mascot stays at its prescribed 240px size.
- Alternating composition: mascot left on Orders, right on Stock, preventing identical framing.
- Progressive visual disclosure: channel slips gather into the parcel, then shelf stock drops and the reorder waits for approval.
- Static copy hierarchy: headline, pain paragraph, what-if statement and result strip are readable from frame one.

Brand retained: Preahvihear/Poppins, white/ink/aqua, result-only teal, pixel mascot only, smooth vector props. No invented company logos or product UI. The two task slides do not show the ART logo. Each is 1080×1350 at 30fps for four seconds.

This is a concept proof, not the full nine-slide carousel. Cover and reveal are not part of this prototype. No copy was shortened. The preserved paragraphs limit how far the illustration can expand without reducing type size.

## Rebuild

Use `build-concept.py`, then the cloud kit's `run-system-browser.py` adapter for stills and sheets. Render with this project's `render-lossless.py`, then run `encode-delivery.py` for browser-compatible H.264 High/yuv420p/faststart files. Cloud scripts resolve `/workspace/art-carousel-kit` and `/workspace/art-carousel-venv`.

`render/out/slide-03.mp4` and `slide-04.mp4` are the individual carousel slides. `journey-preview.mp4` joins them in order as an eight-second review movie, demonstrating the matched motion without adding an animated transition to the text.
