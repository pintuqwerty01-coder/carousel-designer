# ART stock replenishment — Style 1, revision 13

Designer revision following the user's review: consistent typography and alignment, black fades at every edge, finished stock-check endings, a ₹1 lakh approval-limit example, order-routing recap and a branded closing.

## Layout and type

All copy uses the same 84px left margin and 168px headline start. Headings use Preahvihear Regular at 82px with 1.24 line spacing; the two longest titles use 72px and the closing uses 78px to keep intentional two-line breaks. Body copy uses Poppins Medium, 30px / 1.55, with a 30px gap below the title. Text stays stationary. The pain paragraph has balanced line breaks; slides 8 and 9 now follow the same left alignment as the rest.

A black fade covers all four edges of every photo and scene. It replaces the visible full-frame photo boundaries while keeping the working area clear. The closing uses the supplied, unmodified ART logo on a solid ink field, with clear space on every side. ART (A Realtime Tech) remains in the first and final headers.

## Scene changes

| Slide | Final behavior |
| --- | --- |
| 1 | Original side entrance, carton checks, tablet pickup and update choreography retained. Typography and edge fade updated as requested across every slide. |
| 2–3 | Existing purchase-order and paperwork animations retained, with the new type grid and edge treatment. |
| 4 | Stock visibly dwindles; ART reacts, checks the shortage, the carton closes and the scene holds on “Low stock confirmed. Check started.” No false replenishment or approval is shown. |
| 5 | ART checks on-hand stock, counts the loaded incoming shipment and updates its tablet. Wheels and tablet tapping stop. The final hold reads “Stock + incoming checked. Gap ready.” Incoming stock remains loaded, not received. |
| 6 | Example limit ₹1,00,000; ₹60,000 is placed automatically; ₹1,50,000 goes for review. |
| 7 | The ₹1,50,000 request is handed to a person; copy and stage identify the ₹1,00,000 limit. It remains awaiting a decision. |
| 8 | A ₹60,000 purchase order completes, then ART moves to the exception phone and a ₹1.5L review request appears. The recap concerns purchase orders, not outgoing physical stock. No conveyor or unrelated celebration. |
| 9 | Stock checks and the completed tablet record support “Stock handled. Time handed back.” The actual ART logo and “Put ART to work.” close the carousel. No clock or unrelated celebration. |

The canonical mascot model, geometry, palette and scale remain unchanged. Pixel props follow the opening the user liked. Existing photographic backgrounds remain unchanged; no new paid image generation was used. The curly apostrophe alone uses Poppins because Preahvihear lacks that glyph.

## Delivery and verification

Nine MP4s at native 1080 × 1350, 30fps; durations 8, 6, 7, 7, 8, 8, 8, 7 and 7 seconds, totaling 66 seconds. Nine high-quality 1080 × 1350 JPEGs, a nine-page high-quality PDF, storyboard and validation reports accompany the videos. The focused review covers slides 4, 5, 7, 8 and 9 in 37 seconds.

The audit pins the approved opening's choreography, original helper functions and canonical mascot model. Historical media hashes in `proof/approved-opening.json` refer to the original reference; this revision intentionally changes typography and edge treatment on all slides. Checks cover actual rendered fonts, copy, grid positions, line spacing, image loading, safe margins, stationary text, motion, JavaScript errors, logo treatment and native video metadata. Exported video frames are compared with the browser reference stills before packaging.

```bash
source /workspace/art-carousel-venv/bin/activate
python build.py
python stills.py
python motion-sheets.py 1,2,3,4,5,6,7,8,9
python render-lossless.py
python audit.py
python package.py
```

Delivery branch: `stock-reorders-style-1-v13`. Earlier revisions remain on their separate branches.
