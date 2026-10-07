# Festive dispatch — static redesign v3

Nine static slides for review. Exact approved cover remains. Slides 02–06 use full photographic backgrounds with smoothly blended ink shading behind the text and footer. Hard panel edges and the white fading overlay are removed.

The closing sequence has three distinct visual roles and page colours:

- 07 — aqua brand reveal: a connected rail of order, stock, document and customer-update icons shows the automation layer linking existing processes. Mascot celebrates. Original ART logo is intact on its ink patch.
- 08 — white benefit summary: four ink cards turn the four claims into a scannable recap; relaxed mascot holds a cup and gives a thumbs-up.
- 09 — ink CTA: a large message symbol and pointing mascot focus attention on the exact DM invitation; bookmark reinforces the save line. No new claims or metrics.

Fonts, brand palette, mascot identity and exact source draft copy retained. The imagery is generated, not licensed stock. New mascot assets are transparent layers suitable for later scene animation.

Review files: `static-review.pdf`, `proof/all-slides.png`, `stills/slide-01.png` through `slide-09.png`, and local gallery `review.html`. Earlier layouts remain in Git history. These revised layouts have not been animated; review approval comes first, as requested. `corrected-cover.mp4` is the previously checked cover motion, unchanged by this revision.

Rebuild: `build-statics.py`; capture via `capture-statics.py` through the kit browser adapter; `make-review.py` checks exact copy, image loading and text bounds, then creates PDF and overview. Source assets are in `artwork/`, layouts in `slides/`. Cloud scripts resolve `/workspace/art-carousel-kit` and `/workspace/art-carousel-venv`.

## Revision 4

Slides 01–06 now have motion deliveries in `motion/render/out/`. Closing slides 07–09 have new static concepts: connected hub, flowing benefits and calendar deadline CTA. See `proof/last-three.png`. These closing designs await approval before motion. Exact copy remains unchanged. Build instructions are in `design-plan.md`; scene actions and rendering details are in `motion/README.md`.
