# Supplier follow-up — first motion test

One representative **slide 4** motion proof, based on the corrected Style 3 carousel. Duration 7 seconds, 30 fps, native 1080×1350, silent H.264 MP4 with fast-start. This is a motion treatment for review, not an eight-slide motion delivery.

## Sequence

- 0.0–0.5 s: supplier follow-up screen ready; stable headline and ART explanation.
- 0.5–1.35 s: request appears inside the phone.
- 1.95–2.45 s: isolated foreground arm rotates at its shoulder to press Send.
- 2.55–3.0 s: sent confirmation, “Already sent.” and outcomes appear together after the tap.
- 2.7–3.25 s: arm releases the press.
- 3.25–7.0 s: readable final hold; supplier reply remains pending.

## Production

The source scene is split into a clean photographic plate and a transparent foreground arm, prepared from the current original scene. Only that independent layer rotates; the body, face, camera, clock details and background remain stable. No body stretching, bouncing or repeated tap loop. The arm is aligned to the original shoulder and phone contact point with a fixed affine transform. The original steadying hand remains on the phone.

Preahvihear typography and copy positions follow the static source. Three editable HTML states are printed to native raster layers through Chromium/PDF to preserve reliable type rendering. `index.html` controls a deterministic, seekable timeline via `setTime(t)`. `render.py --video` captures 210 frames and encodes the MP4. Serve the parent carousel project over local HTTP to preview `/motion-preview/index.html`.

Assets are generated illustrative layers, not customer photographs or an actual product interface. The action is a generic supplier follow-up request, without invented revised dates, a supplier response, or an arrival guarantee. The full static carousel remains in `delivery-v6/`.
