# Concept C — motion posters

Four-slide review concept for Orders, Stock, Paperwork and Dispatch, using the exact existing draft copy. The previous carousel remains in `festive-dispatch/`.

Oversized physical metaphors take centre stage on a high-contrast ink panel. The 240px pixel mascot interacts with the illustration. Orders settle into an inbox; empty shelf spaces trigger an approval draft; paperwork aligns into a checked pack; dispatch sends a customer update while a parcel remains delayed. Each scene has its own choreography.

Brand preserved: white, ink and aqua, green reserved for results/checks, Preahvihear/Poppins, smooth vector props and pixel mascot. Copy is static and readable from frame one. No invented logo or product UI.

Each video is 1080×1350, 30fps, four seconds. `poster-preview.mp4` joins the four slides into a 16-second review movie. Individual videos are in `render/out/`. This is a four-slide design proof; the cover, setup, reveal, outcome and CTA are outside this experiment.

## Rebuild

Run `build-concept.py`, then the kit browser adapter for stills and motion sheets. Run `render-lossless.py` followed by `encode-delivery.py`. The scripts use `/workspace/art-carousel-kit` and `/workspace/art-carousel-venv`. Delivery files use H.264 High, yuv420p and faststart.
