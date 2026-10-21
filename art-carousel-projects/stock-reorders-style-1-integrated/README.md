# ART stock replenishment — Style 1, revision 6

Nine slides: a new opening scene, expanded supporting copy, photographic backgrounds throughout, and more mascot action. Preahvihear Regular headlines and Poppins body text follow the Style 1 guide. Text remains stationary and visible from the first frame.

The new opener uses the real low-stock shelf in the existing generated background: ART enters, scans the rack, prepares the next order and reacts. Later scenes include walking arrivals, stepped legs and arms, scanning, routing, review and completion gestures. Photographic shelves, desks and cartons anchor the annotations.

Timing: 7 seconds for the opener, 8 seconds for the two-path spending example, and 6 seconds for each remaining slide. Total: 57 seconds. Every slide is 1080 × 1350 at 30 fps.

The ₹10,000 limit, ₹6,000 automatic order and ₹15,000 approval request are illustrative, not live business settings. Orders within the configured amount proceed automatically; above-limit orders reach a person. The review scene does not assume approval.

Existing generated backgrounds are reused unchanged from `festive-dispatch-realistic` and `festive-dispatch-photo`. No new paid image generation was used. Preahvihear lacks the curly apostrophe; that character alone uses the approved Poppins family. Actual font usage is checked through Chrome DevTools.

## Reproduce

```bash
source /workspace/art-carousel-venv/bin/activate
python build.py
python /workspace/art-carousel-kit/run-system-browser.py /workspace/art-carousel-kit/scripts/stills.py "$PWD"
python render-lossless.py
python audit.py
python package.py
```

The ZIP includes nine native-size MP4s, nine high-quality JPEGs, a nine-page PDF and validation reports. The PDF uses the same 1080 × 1350 slide artwork. The combined MP4 is a compressed viewing copy. The storyboard is generated from the actual rendered videos.

Earlier revisions are preserved on their separate branches. Revision 6 is delivered on `stock-reorders-style-1-v6`.
