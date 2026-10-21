# ART stock replenishment — Style 1, revision 7

Nine photographic scenes with the established script, Preahvihear Regular headlines and Poppins body copy. Revision 7 replaces the previous generic travel, waving, floating scanner columns and dotted diagrams with individual scene actions.

## Motion direction

- **Opening and low-stock detection:** ART walks toward the bottom shelf carton. A handheld scanner remains attached to the mascot's hand. A short light cone begins at the device nozzle, and its moving scan line is clipped to a barcode on that carton. It does not scan the empty shelf bay. A prepared-order terminal rests on the pictured workbench.
- **Next order handled:** ART reaches the printer control on the workbench; the printer feeds an order, which receives an order status stamp.
- **Manual checking:** papers slide across the pictured records table toward ART. A restrained vibration follows the pictured telephone.
- **Stock and incoming:** ART scans the label on the actual incoming carton on the trolley. A desk terminal shows the stock-and-incoming check.
- **Two spending paths:** both terminals sit on the pictured full-width records table. ART walks to and taps the within-limit order, then the above-limit request. No connecting arrows or dotted routing lines are used.
- **Human review:** the request moves along the review desk to ART's left hand. ART uses the adjacent terminal; its status waits for a person's decision. Approval is not assumed.
- **Routine and exception:** the trolley carton receives a completion mark. The desk terminal identifies the exception for review.
- **Rules:** ART approaches the terminal and touches its save control. The controls update and the saved state appears.

The mascot retains its original 240px pixel design and stepped motion. Props use smooth vector shapes with restrained lighting, tabletop shadows and perspective. The former dotted footer is replaced with quiet solid progress segments. Backgrounds remain stationary so scene coordinates cannot drift away from their physical objects. Text stays visible and still from the first frame.

Timing: 7 seconds for the opener, 8 seconds for the price comparison and 6 seconds for every other slide. Total 57 seconds. Native size: 1080 × 1350, 30fps. The ₹10,000 limit, ₹6,000 automatic order and ₹15,000 approval request remain illustrative.

Existing generated backgrounds are reused from `festive-dispatch-realistic` and `festive-dispatch-photo`. No new paid image generation was used. The underlying background image files are unchanged; hardware and scene effects are rendered separately as animation layers. Preahvihear lacks the curly apostrophe; that character uses the approved Poppins family. Chrome DevTools verifies the fonts actually rendered.

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

The ZIP contains nine MP4 masters, nine native-size high-quality JPEGs, a nine-page PDF and validation reports. The combined MP4 is a compressed viewing copy. The storyboard is extracted from actual exported video frames.

Delivered on the separate `stock-reorders-style-1-v7` branch; earlier revisions remain available on their branches.
