Latest review candidate: `reference-rebuild/title-preview/`. A single cover now illustrates a delay at a checkpoint and an alert reaching the team before a customer call. Previous scan motion was rejected for not matching the title. Review this preview before extending to all nine.

# Current status: previous full set rejected

The user rejected the preceding designs and animation. The current revision is `reference-rebuild/`, using the supplied Style 2 kit, physical logistics objects and HyperFrames. Only the cover and in-transit review proofs are completed in that folder. Review them before extending to all nine. Earlier `final/` files and ZIP remain historical, rejected exports.

# Delivery delays — Style 2 / Race to know

Completed nine-slide carousel using the user-selected A — Reference composition animation treatment. The cover and in-transit composition are retained from the approved previews; pickup, arrival and customer-update slides have distinct alert actions.

## Deliverables

- `final/carousel-review.pdf`: all nine static slides.
- `final/all-slides.png`: complete overview.
- `final/slide-01.mp4` through `slide-09.mp4`: nine individual animations, 1080×1350, 30fps, four seconds each.
- `final/slide-01.png` through `slide-09.png`: static exports.
- `delivery-delays-style-2.zip`: videos, images, PDF, overview and validation reports.

The exact supplied script is preserved in `source-content.json`. Style 2 uses Poppins for the cover hook and supporting copy, Preahvihear for headlines, generated 3D objects, no mascot, and the original ART logo on the reveal. Text stays stationary while objects drift gently and slide-specific alert/check actions play.

## Editing and export

The nine standalone HTML files under `final/` and their local assets are the current editable source. Earlier kit content and proof folders are historical experiments and do not rebuild the completed design.

From the project directory, with the prepared cloud environment:

```sh
/workspace/art-carousel-venv/bin/python /workspace/art-carousel-kit/run-system-browser.py final/export.py
/workspace/art-carousel-venv/bin/python /workspace/art-carousel-kit/run-system-browser.py final/audit.py
```

Use `final/export.py --stills-only` to export static images and PDF without rendering videos. Rendering requires Chromium, Playwright and ffmpeg. `frames-*` intermediate folders are ignored.

Verified: exact script copy, loaded image assets, glyph bounds, text block separation, actual custom font use, stationary text positions across animation, nine decoded PDF pages, and nine four-second 1080×1350 30fps MP4s with visible frame changes. Reports are in `final/validation.json`, `font-validation.json` and `video-validation.json`. The decoded PDF was visually reviewed. No HyperFrames lint result is claimed.
