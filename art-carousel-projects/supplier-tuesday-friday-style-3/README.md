# Supplier said Tuesday. It's Friday. — Style 3

Representative static design proof: cover (01) and supplier follow-up (04), from an eight-slide narrative. The approach is approved; these layouts and draft copy are for design review before completing the set. No motion is included.

## Design

Preahvihear Regular throughout; clean modern receiving counter; original dimensional aqua ART mascot; fitted aqua callouts; separate white outcome cards. ART is present from the opening. The follow-up ends with a reply pending, without inventing a supplier response or delivery guarantee. No top ART watermark.

## Files

- `slides/`: editable HTML, local font and original assets.
- `stills/`: native 1080×1350 PNGs.
- `delivery/`: high-quality individual JPEGs, two-page raster PDF, overview and download ZIP.
- `content.json`: eight-slide draft narrative; only slides 01 and 04 are designed in this proof.
- `audit.json`: browser font and image-load checks.

Revision v2 replaces the festive warehouse with a newly generated non-festive receiving-counter background. It is illustrative imagery, not a customer photograph. Original mascot/font assets come from `festive-dispatch-preahvihear`. `build.py` regenerates the editable layouts using those repository assets. Capture with Chromium over local HTTP after document.fonts.ready, at viewport 1080×1350 and device scale 1.

Validation: visually inspected both native renders; browser reports embedded Preahvihear in all main text elements; images loaded. PDF pages exported at native dimensions.

## Background revision v2

Latest exports are in `delivery-v2/`; `delivery/` is the superseded first proof. Background revised on both slides; script, mascot identity and typography preserved. Reproduce: `python build.py`, `python capture.py`, `python export-v2.py`. The generated source background is retained as `slides/assets/warehouse.png`.
