# Delivery delays — revised Style 2 proofs

Two review slides have been rebuilt following the user's rejection of the initial direction. The current PDF and videos contain the cover (1) and in-transit task (4); the other seven layouts remain preliminary and are not completed deliverables.

The cover now uses a generated 3D parcel and notification bell, with an animated alert branching to the team before the customer. The in-transit slide shows the shipment signal stopping at an alert marker, alongside the stationary 3D truck/road object. Motion explains early warning. Text stays stationary; the exact supplied script is retained. Small diagram labels are explanatory visual annotations.

The palette remains Style 2 dark blue-green and aqua, with Poppins cover/supporting text and Preahvihear headlines. Following feedback, decorative flares, bokeh and ghost numbers have been removed from these two proofs. No mascot is present. All checkmarks are vectors.

Files: `first-two-proof.pdf`, `proof/first-two.png`, `stills/slide-01.png`, `stills/slide-04.png`, and the two corresponding MP4s in `render/out/`. Initial rejected files are preserved in `proof/archive-v1/`.

Validation: exact script copy, actual custom fonts, glyph bounds, loaded assets, text-block separation, two-page PDF inspection, four-second 1080×1350 30fps export, unchanged first/last text positions and visible animation. Rendering uses browser frames and ffmpeg; no HyperFrames lint result is claimed.

Review these two revisions before completing all nine, following the Style 2 “Show two before all” approval step. The canonical script is `source-content.json`; `content.json` contains the earlier full-strip implementation and does not rebuild the revised standalone proofs. Edit the current two HTML compositions directly, then use `proof.py` and `render-proofs.py`.
