# Delivery delays — Style 2 review proofs

The user approved the nine-slide visual plan and selected in-chat image generation. The current delivery contains **two review proofs only**: the cover (slide 1) and in-transit task (slide 4). The remaining seven HTML layouts are preliminary and have not been delivered as completed slides.

Generated transparent van and truck/road assets are preserved in `images/raw/` and `images/cut/`. Text remains editable and matches `source-content.json`. Style 2 fonts are Poppins for the cover hook and supporting text, and Preahvihear for headlines. No mascot is used.

Review files:

- `first-two-proof.pdf` — two pages, cover then slide 4.
- `proof/first-two.png` — side-by-side overview.
- `stills/slide-01.png` and `stills/slide-04.png`.
- `render/out/slide-01.mp4` and `render/out/slide-04.mp4` — four-second motion proofs.

The stalled-truck proof pulses its warning marker while keeping the vehicle and road stationary, instead of sliding the flattened truck/road group. This preserves contact with the road and gives a clear early-warning cue. The ART logo remains intact; internal clock-hand animation has not been approved or delivered.

Checks: exact visible copy, actual custom-font rendering, assets loaded, text bounds/overlap, two-page PDF decoded, 1080×1350 30fps four-second video export and unchanged first/last text positions. Videos use browser frame rendering, not HyperFrames; no HyperFrames lint result is claimed.

Approve these two design/motion proofs before the remaining seven slides are completed, as required by the supplied Style 2 guide's “Show two before all” workflow.
