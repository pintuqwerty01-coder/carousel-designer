# First six slides — approved static designs animated

Files: `render/out/slide-01.mp4` through `slide-06.mp4`, in posting order. Each is 1080×1350, 30fps, four seconds, H.264 High/yuv420p with faststart.

01 retains the corrected approved-image cover balance motion. 02 parcels build into a queue. 03 three order slips converge into one destination. 04 a carton travels along a replenishment path and confirms. 05 a scan crosses the invoice then confirms. 06 a delivery marker travels along a route and turns into an update confirmation. These are scene/prop actions over the approved photo plates; the task mascots remain embedded in the photographs, without articulated limb animation. Text and shading stay stationary. No new copy, claims or numerical metrics.

Rebuild with `../build-motion.py`, then `render-frames.py` through `/workspace/art-carousel-kit/run-system-browser.py`. Cover source is in `../cover-motion/`. Validate with `../validate-motion.py`. Browser timeline rendering uses the original GSAP timeline and deterministic 120-frame sampling, encoded directly through ffmpeg.

Slides 07–09 are revised static concepts awaiting review; not animated.
