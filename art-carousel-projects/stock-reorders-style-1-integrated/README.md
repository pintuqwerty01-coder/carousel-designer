# ART stock replenishment — Style 1, revision 11

Revision 11 applies the approved marketing headline “Your shelves called. ART’s already on it.” and its supporting copy. The opening does not mention spending limits. “ART (A Realtime Tech)” appears in the brand line on slides 1 and 9, in the approved Poppins family. The existing animated opening is preserved. Masters 1, 2 and 9 are rerendered for this revision. Slide 2 is the next scene: its order form fills automatically, confirms completion and is lifted slightly as ART reaches to collect it. The mascot stays anchored to the tabletop at y=920.

The user explicitly requested a new opening: ART walks in from the side, checks animated boxes in the mascot's pixel-art style, takes a tablet and updates the stock. This overrides the default guide's vector-prop rule for these opening props.

## Opening choreography

| Time | Action and visible response |
| --- | --- |
| 0–1.5s | ART walks in from the left, using the original 240px mascot and stepped legs. |
| 1.65–2.7s | ART inspects the first carton. Its label changes from grey to aqua, then to a pixel completion mark. Its lid remains closed because the tablet is resting on it. |
| 3–4.05s | ART inspects the second carton. Its lid opens and closes in pixel steps, and the label resolves to a completion mark. |
| 4.2–5.3s | ART takes the tablet that has been visibly resting on the first carton since frame one. The device lowers beside the face, then crosses to both hands below the face. |
| 5.55–7.1s | The left hand supports the tablet; the right forearm taps its screen. Stock rows update in sequence and a completion mark appears. |
| 7.1–8s | ART holds the updated tablet; “Stock updated” confirms the result. |

The opening uses pixel cartons, a pixel tablet and pixel arm extensions, with the same stepped geometry and light outline treatment as the mascot. The realistic background, stationary headline and established fonts stay in place. Boxes stand on the same floor line as ART. No stock quantities or business settings are invented.

The opening choreography was introduced in revision 10. The corrected slide 2 tabletop placement and slides 3–9 are preserved. The opening is now eight seconds, bringing the complete carousel to 58 seconds. The separate opening preview shows only this eight-second sequence.

## What changed

The repeated scanner, printer and terminal scenes have been removed. ART's role is represented as responding to stock rules, checking on-hand and incoming stock, placing within-limit orders and sending above-limit requests to a person. No barcode scanner or printer is used. The opening stock check and tablet update are the user-requested mascot metaphor.

Each slide now has a specific visual purpose:

| Slide | Visual purpose |
| --- | --- |
| 01 | Side entrance → inspect two pixel cartons → pick up tablet → update stock. |
| 02 | An order form builds automatically, confirms completion, then ART collects it while standing on the tabletop. |
| 03 | A pile of papers represents manual checking, with an unresolved mascot reaction. |
| 04 | A stock-data bar reaches its reorder point and triggers the rule. This is a data annotation, not a shelf scanner. |
| 05 | The pictured incoming trolley and on-hand stock are identified before the reorder gap is considered. No quantities are invented. |
| 06 | The existing two amount panels carry the explanation. A completion mark and human-review symbol identify the two paths; duplicate miniature terminals are gone. |
| 07 | A human-review phone appears only on this slide, distinct from the opening inventory tablet. ART waits for the person's decision; approval is not assumed. |
| 08 | A completion mark attaches to a dispatch carton while ART moves through the aisle. No extra screen or repeated flow diagram. |
| 09 | A centred closing composition and mascot complete the existing call to action without added controls or props. |

Consistency comes from Preahvihear Regular headlines, Poppins body copy, the 84px grid, a single 240px mascot scale, white/aqua/ink colours and the same photographic environment. Opening boxes and tablet use the pixel style specifically requested by the user. Green is reserved for completion. The outcome and closing slides use centred text to distinguish them from the explanation slides. Main copy stays still and visible from the first frame. Dotted connectors and the dotted footer remain removed.

Existing generated photographs are reused unchanged from `festive-dispatch-realistic` and `festive-dispatch-photo`; no paid image generation was used. These are illustrative backgrounds, not images of an identified real business. Preahvihear lacks the curly apostrophe, which uses the approved Poppins family. Actual rendered font names are checked through Chrome DevTools.

Timing: 8 seconds for the opening, 8 seconds for the amount comparison, 6 seconds for every other slide. All videos and JPEGs are 1080 × 1350. Videos run at 30fps. The ₹10,000 limit, ₹6,000 order and ₹15,000 request are examples, not configured business rules.

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

Delivered on `stock-reorders-style-1-v11`. Previous revisions remain on their own branches.
