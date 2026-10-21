# ART stock replenishment — Style 1, revision 9

This revision corrects only the opening scene and slide 2 placement. The nine-slide script, threshold example, other seven scenes and 57-second timing are retained.

Slide 1 now shows ART holding a prepared order, with one confirmation mark. Its walking entrance and raised-arm gesture are removed. Slide 2 places the feet at y=920 within the photographed tabletop (approximately y=875–982 at this horizontal position), instead of y=1012 over the vertical apron. Its paper base shares the tabletop plane; the hand meets the paper edge. The mascot stays at the established 240px scale. Individual masters 1 and 2 are rerendered; masters 3–9 are reused unchanged.

## What changed

The repeated scanner, printer and terminal scenes have been removed. ART's role is represented as responding to stock rules, checking on-hand and incoming stock, placing within-limit orders and sending above-limit requests to a person. The animation no longer implies that ART must physically scan warehouse cartons or operate a printer.

Each slide now has a specific visual purpose:

| Slide | Visual purpose |
| --- | --- |
| 01 | ART holds the prepared order in a fixed opening pose; one confirmation mark draws. |
| 02 | One completed purchase order represents the routine outcome. |
| 03 | A pile of papers represents manual checking, with an unresolved mascot reaction. |
| 04 | A stock-data bar reaches its reorder point and triggers the rule. This is a data annotation, not a shelf scanner. |
| 05 | The pictured incoming trolley and on-hand stock are identified before the reorder gap is considered. No quantities are invented. |
| 06 | The existing two amount panels carry the explanation. A completion mark and human-review symbol identify the two paths; duplicate miniature terminals are gone. |
| 07 | The only device in the sequence is a human-review phone. ART waits for the person's decision; approval is not assumed. |
| 08 | A completion mark attaches to a dispatch carton while ART moves through the aisle. No extra screen or repeated flow diagram. |
| 09 | A centred closing composition and mascot complete the existing call to action without added controls or props. |

Consistency comes from Preahvihear Regular headlines, Poppins body copy, the 84px grid, a single 240px mascot scale, white/aqua/ink colours and the same photographic environment. Green is reserved for completion. The outcome and closing slides use centred text to distinguish them from the explanation slides. Main copy stays still and visible from the first frame. Dotted connectors and the dotted footer remain removed.

Existing generated photographs are reused unchanged from `festive-dispatch-realistic` and `festive-dispatch-photo`; no paid image generation was used. These are illustrative backgrounds, not images of an identified real business. Preahvihear lacks the curly apostrophe, which uses the approved Poppins family. Actual rendered font names are checked through Chrome DevTools.

Timing: 7 seconds for the opening, 8 seconds for the amount comparison, 6 seconds for every other slide. All videos and JPEGs are 1080 × 1350. Videos run at 30fps. The ₹10,000 limit, ₹6,000 order and ₹15,000 request are examples, not configured business rules.

## Reproduce

```bash
source /workspace/art-carousel-venv/bin/activate
python build.py
python /workspace/art-carousel-kit/run-system-browser.py /workspace/art-carousel-kit/scripts/stills.py "$PWD"
python motion-sheets.py
python render-lossless.py
python audit.py
python package.py
```

The ZIP contains nine MP4 masters, nine high-quality native-size JPEGs, a nine-page PDF and validation reports. The combined video is a compressed viewing copy; the storyboard comes from actual exported frames.

Delivered on `stock-reorders-style-1-v9`. Previous revisions remain on their own branches.
