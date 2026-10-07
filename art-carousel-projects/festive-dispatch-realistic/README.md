# Realistic festive dispatch — first motion proof

The user approved the static cover and instructed proceeding to animation. This review contains only cover 01 and Orders 03, following the ART workflow's cover-plus-one-task approval step. The remaining slides await motion proof approval.

Cover: realistic generated warehouse plate, separate static brand typography, 240px pixel mascot balancing two vector cartons, then steadying; restrained background push-in. The generated static reference is in `cover/static-cover-proof.png`; the rebuilt animation uses separate layers and the supplied Preahvihear/Poppins brand fonts. It is not a licensed stock photograph.

Orders: previous motion-poster direction, three scattered sheets straightening into one inbox, a single green completion check. Exact existing draft copy retained on both slides. Draft review status continues; this is not publication approval.

Videos: `render/out/slide-01.mp4`, `render/out/slide-03.mp4`. Joined review: `first-motion-proof.mp4` (8 seconds). Each slide is 1080×1350, 30fps, four seconds, H.264 High/yuv420p with faststart. All text stays stationary; photo, mascot, props and trail animate.

Rebuild: `build-cover.py` builds cover. Orders HTML retains the motion-poster project scene. Run kit stills/sheets through `run-system-browser.py`, then `render-lossless.py 01,03` and `encode-delivery.py`.
