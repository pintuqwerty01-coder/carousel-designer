# ART stock replenishment — Style 1, revision 14

The edge treatment is now a subtle, light vignette. The former black perimeter gradients are removed; one continuous radial gradient reaches only 12% opacity at the outer corners. The photo's separate text-readability shade is also lighter, including the footer. There is no opaque border or stacked black edge layer.

Slide 9 retains the closing headline, body, mascot, stock props and CTA. Only the black rectangle behind the logo is removed, as clarified by the user. The original logo asset stays unchanged; its existing dark backing blends into the scene without a visible rectangular panel. The closing is not a logo-only slide.

Slides 1–8 retain the revision-13 type grid, copy, animation, ₹1,00,000 example limit and stock-check endings. The original opening choreography and canonical mascot engine remain unchanged. Only their overall shade and edge treatment change in this revision.

## Delivery

Nine native 1080 × 1350 MP4s at 30fps, nine high-quality 1080 × 1350 JPEGs, a nine-page high-quality PDF, storyboard and validation reports. Durations remain 8, 6, 7, 7, 8, 8, 8, 7 and 7 seconds: 66 seconds total. A focused review covers slides 4, 5, 7, 8 and the closing in 37 seconds.

The audit checks the original opening choreography and mascot, actual font rendering, fixed copy, margins, type grid, scene motion, JavaScript errors and native video metadata. The closing is checked for the retained content and a transparent logo container with no rectangular backing. Exported frames are compared to the browser reference stills. The original media hashes in `proof/approved-opening.json` are historical references; the typography, shade and edge changes were requested by the user.

```bash
source /workspace/art-carousel-venv/bin/activate
python build.py
python stills.py
python motion-sheets.py 1,2,3,4,5,6,7,8,9
python render-lossless.py
python audit.py
python package.py
```

Delivery branch: `stock-reorders-style-1-v14`. Earlier revisions remain on their separate branches.
