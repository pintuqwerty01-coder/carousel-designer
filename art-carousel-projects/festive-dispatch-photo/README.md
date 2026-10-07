# Festive dispatch — articulated 2D mascot revision 6

The first six slides now contain genuine 2D character action. The original ART 24×24 pixel-grid mascot is drawn as independently changing arms, legs, eyes, mouth and antenna states. Photographs and copy remain stationary. Robot poses update at eight poses/second; props follow smoothly eased trajectories. A single 240px mascot scale is used throughout.

The embedded 3D mascots and fake floating effects were removed with image edits, reconstructing clean photographic warehouse plates in `artwork/clean-02.png` through `clean-06.png`. Cover uses its existing clean plate with original approved lettering preserved as a stationary masked image layer. Source typography and exact draft text remain unchanged from revision 5.

| Slide | Action |
|---|---|
| 01 | Bot walks with one parcel, transfers it to a dispatch tray and relaxes. |
| 02 | Bot stays at its workstation, reacts to a growing queue, raises its arms to route three documents and clears the queue. |
| 03 | Phone/chat/email orders travel into one inbox; bot receives, walks to the inbox and files them. |
| 04 | Bot carries a carton to the empty shelf, lifts and places it, then confirms replenishment. |
| 05 | Bot moves a hand-held magnifier down a document and presses a stamp, leaving a verification mark. |
| 06 | Bot notices a delayed consignment, extends its arm and sends an envelope to a customer phone; incoming calls resolve to a check. |

Cover and setup differ in stance, leg action, arms, expression and movement pattern. First-six MP4s are in `motion/render/out/`; `motion/first-six-preview.mp4` plays them in order. Each file: 1080×1350, 30fps, four seconds, H.264 High/yuv420p, faststart.

Closing 07–09 retain their approved layouts, typography and palette (ink / white / ink), with the mascot converted to the same flat 2D identity: wave / cup / point. Closing pages remain static review proofs. Original ART logo remains intact on 07.

Authoring: `actors-2d.js`, `build-2d.py`. Rebuild: `build-statics.py` → `revise-endings.py` → `refine-photo-style.py` → `build-2d.py` → `build-motion.py`. Capture and review: `capture-statics.py`, `make-review.py`, `preview-endings.py`. Render `motion/render-frames.py 1,2,3,4,5,6`. Browser scripts use `/workspace/art-carousel-kit/run-system-browser.py` with `/workspace/art-carousel-venv/bin/python`.

Checks: `motion/check-actors.py` verifies actual changing poses, expressions, visible animation, unique first-two actions, static background/copy and no JavaScript errors; `motion/actor-sheets.py` exports nine-frame sheets for visual inspection; `audit-fonts.py` verifies actual rendered font families; `validate-motion.py` checks video metadata, scene changes and static upper region; `motion/browser-check.py` verifies playback.

Draft review assets, not production publication approval. GitHub contains review deliveries and editable sources.
