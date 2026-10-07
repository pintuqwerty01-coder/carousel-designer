# Articulated 2D mascot motion — revision 6

Posting order: `render/out/slide-01.mp4` through `slide-06.mp4`. Each: 1080×1350, four seconds, 30fps, 120 frames, H.264 High/yuv420p and faststart. Full sequence: `first-six-preview.mp4`.

These clips animate the original flat ART mascot's legs, arms, eyes, mouth and antenna, plus its props. Photos and typography are static. 01 walks and hands off a parcel; 02 stays at a workstation and sorts a growing queue; 03 gathers phone/chat/email orders into one inbox; 04 walks to a shelf and lifts a replenishment carton; 05 scans with a held magnifier then stamps a document; 06 reacts to a delay and sends a customer update. No repeat camera push or generic repeated character bounce.

Every scene has its own initial pose and action sequence. Pose updates are intentionally stepped at eight per second as the ART mascot guidelines require; prop movement is smooth. The bot stays in clear space, holds props at its hands and leaves text unobscured.

Sources: `../actors-2d.js`, `../build-2d.py`, `../build-motion.py`; source HTML in `slides/`. Rebuild and render with `render-frames.py 1,2,3,4,5,6` through the kit system-browser adapter. Checks: `check-actors.py`, `actor-sheets.py`, `../validate-motion.py` and `browser-check.py`. `proof/sheet-01.png` through `sheet-06.png` show the nine-frame sequences. `proof/actor-validation.json` records pose/expression changes and first-two movement distinctions.

Closing pages 07–09 are static and use the same 2D mascot in their retained layouts.
