# ART stock replenishment — Style 1, revision 15

This revision addresses the size hierarchy, approval handoff and closing composition.

- Headings: a consistent 80px Preahvihear Regular, with deliberate two-line breaks and 1.2 line spacing.
- Body copy: 34px Poppins Medium / 1.5, enlarged from 30px. Line breaks preserve the approved words.
- Scene labels: 30px, aligned with the objects they describe. Final status captions: 30px instead of 24px.
- Documents: 10% larger, consistently applied across scenes; handoff and phone spacing adjusted to preserve clear gaps around the mascot.
- Canonical mascot: unchanged 240px model, palette and geometry on every slide. Poses remain stepped at 8Hz.
- Slide 6: the ₹1,00,000 example remains; amounts are 56px, with larger card descriptions.
- Slide 7: as the hand grips the document at 3.2 seconds, a clearly visible 44px semibold “Awaiting approval” line appears and holds. Taking the request does not automatically approve it.
- Slide 9: the logo is at the top-left, with clear space. The original aqua vector comes from Style 2's final slide 7. Its paths and white clock hands remain intact; CSS presents its wordmark in ink, as requested by the user. There is no logo patch or central logo.
- Slide 9: mascot feet and both cartons share the photographed tabletop at y=920. The former floor-level platform is removed. The tablet stays in ART's hands during the entrance and stock check.
- Slide 9 CTA: “Put ART to work.” is centered, 58px Poppins Bold, readable from the first frame. The lighter top treatment gives the aqua-and-ink logo and ink headline contrast without a rectangular backing.

The user's subtle 12% radial edge vignette is retained. All main copy, the logo and CTA stay stationary. The only conditional copy is the approval status explicitly requested after handoff. No internal logo shapes are animated. The original opening choreography and mascot engine remain pinned in the audit. Prior user directions authorize the pixel props, photographic backgrounds and 5–8-second timing used in this project.

## Delivery and checks

Nine MP4s, 1080 × 1350, 30fps. Durations: 8, 6, 7, 7, 8, 8, 8, 7 and 7 seconds; 66 seconds total. Nine high-quality native JPEGs, a nine-page high-quality PDF and storyboard accompany the videos. The focused review covers slides 4, 5, 7, 8 and 9 in 37 seconds.

Checks cover original model/choreography, actual rendered brand fonts, fixed text, safe margins, deliberate line breaks, timing of the approval status, the original vector source and requested presentation, logo position, CTA centering/weight/size, native video metadata, browser errors, exported frame comparisons and ZIP integrity. Motion sheets are inspected for hand contact, prop clearance and placement on the photographed table.

```bash
source /workspace/art-carousel-venv/bin/activate
python build.py
python stills.py
python motion-sheets.py 1,2,3,4,5,6,7,8,9
python render-lossless.py
python audit.py
python package.py
```

Delivery branch: `stock-reorders-style-1-v15`. Earlier versions remain on their separate branches.
