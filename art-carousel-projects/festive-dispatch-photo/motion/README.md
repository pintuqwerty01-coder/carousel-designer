# Photographic camera motion — revision 5

Posting order: `render/out/slide-01.mp4` through `slide-06.mp4`. Each: 1080×1350, 30fps, four seconds, 120 frames, H.264 High/yuv420p with faststart.

The original photo scene itself moves gently behind stationary text and shading. Live copy and shading remain stationary over the moving photo on slides 02–06. The cover alone uses a fixed feathered scene mask to preserve its baked lettering. Camera focus: 01 mascot/dispatch area; 02 rush scene; 03 orders destination; 04 stock shelves; 05 document area; 06 customer update area. Smooth cosine easing, 1–1.4% push and 2–7px pan, no repeat bounce, no new illustrative props or scanning effects. Embedded mascots are not independently articulated. This is camera animation of still photography, not generated character video.

Build with `../build-motion.py`; render `render-frames.py 1,2,3,4,5,6` through `/workspace/art-carousel-kit/run-system-browser.py`. Validation: `../validate-motion.py`, `browser-check.py`. All live copy stays outside the moving layer; baked cover copy stays outside the scene mask. Slides 07–09 remain static.
