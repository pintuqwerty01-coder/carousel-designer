# ART stock replenishment — Style 1, revision 16

This revision follows the user's reference for the copy-area treatment, removes the decorative ART header from every slide and clarifies the animation outcomes.

## Visual corrections

Slides 1–8 now have the black equivalent of the closing slide's soft white upper fade: dark behind the copy, smoothly fading into the photograph. This is a copy-area treatment, not a black perimeter or rectangular logo panel. The light closing treatment, original aqua vector with the requested ink wordmark, tabletop mascot and cartons, and bold centered CTA are retained.

The ART dot, wordmark and horizontal rule at the top are removed from every slide's markup. The actual blue-and-black ART logo remains on the closing only. Main headlines on slides 1–8 start at y=112, with the same 84px left margin. The closing retains its corner-logo layout and clear space.

Slide 3's subheading has two left-aligned 820px blocks, both starting at x=84. A 22px gap separates the pain points from their consequence. The approved wording is preserved.

## Meaning and animation timing

| Slide | What the animation establishes | Copy following the action |
| --- | --- | --- |
| 1 | ART checks stock and records the update on its tablet. The boxes do not refill. | The original “Stock updated” label refers to the stock record. Original opening choreography retained. |
| 2 | A routine purchase order forms and completes. | Main copy remains readable throughout; no additional completion claim is introduced. |
| 3 | Manual paperwork builds up and causes urgency. | No false resolution or success caption. |
| 4 | Stock dwindles and ART detects the low-stock state. | “Stock is below your reorder point.” appears after 3.5 seconds. It states the finding, without suggesting an order has already been placed. |
| 5 | ART checks stock on hand and accounts for the loaded incoming shipment on its tablet. | “ART calculates how much stock to reorder.” appears after 5.1 seconds. Incoming stock remains in transit, not received. This present-tense caption accompanies the calculation. Ordering follows the amount rules on slide 6. |
| 6 | ₹60,000 completes automatically under the ₹1,00,000 example limit; ₹1,50,000 remains pending. | The panels explain the two paths. There is no automatic approval on the exception. |
| 7 | A person receives the above-limit request. | “Awaiting approval” appears at the handoff, at 3.2 seconds, and remains visible. Receipt is not approval. |
| 8 | The routine order completes, then an exception reaches the review phone. | “Routine orders placed. Exceptions await approval.” appears after 5.0 seconds, after both destinations are established. |
| 9 | ART completes the stock-recording task while standing on the table. | The centered “Put ART to work.” CTA is static and readable from the first frame. |

The three revised outcomes and their times live in `content.json` and are injected into the animation from that single source. The vague “check started,” “gap ready” and “exception with you” phrases are removed.

## Delivery and verification

Nine native 1080 × 1350 MP4s, 30fps; durations 8, 6, 7, 7, 8, 8, 8, 7 and 7 seconds, totaling 66 seconds. Nine high-quality JPEGs, a nine-page PDF, storyboard and validation reports. The focused review covers slides 4, 5, 7, 8 and 9 in 37 seconds.

Preahvihear Regular headings remain 80px; Poppins Medium body is 34px. The original 240px mascot, its palette and stepped poses, and the original opening choreography remain unchanged. Text stays stationary. Poppins Semibold is explicitly loaded before late canvas labels appear, preventing a temporary fallback font on the low-stock label. Pixel props, photographic backgrounds, requested logo presentation and 5–8-second durations follow the user's explicit direction. No shared brand kit or guide is modified.

Checks cover header removal on all nine slides, fonts, copy, safe margins, line breaks, slide 3's paragraph alignment, outcome copy and width, approval timing, source-logo geometry and colors, logo clear space, CTA position/weight/size, motion, browser errors, native video metadata, exported frame comparisons and package integrity.

```bash
source /workspace/art-carousel-venv/bin/activate
python build.py
python stills.py
python motion-sheets.py 1,2,3,4,5,6,7,8,9
python render-lossless.py
python audit.py
python package.py
```

Delivery branch: `stock-reorders-style-1-v16`. Prior revisions remain on separate branches.
