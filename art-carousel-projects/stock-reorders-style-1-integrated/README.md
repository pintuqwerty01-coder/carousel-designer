# ART stock replenishment — Style 1, revision 12

Slide 1 is the user-approved reference. Its video, still image, scene function and pixel-prop helpers are preserved. The original mascot engine stays unchanged: 240px scale, identical body/head geometry, approved facial poses, palette and outline. Emotion comes from poses, facial expressions, antenna states, stepped movement and a single victory jump—not a redesigned mascot.

The remaining scenes now use foreground elements in the opening's pixel-art style over the existing photographic backgrounds. This follows the user's explicit request to match the liked opening, including incoming stock in the mascot's animation style.

## Scene direction

| Slide | Action and cause/result | Emotion |
| --- | --- | --- |
| 01 | Approved side entrance, two carton checks, tablet pickup and stock update. Unchanged. | Focus → satisfaction. |
| 02 | A pixel purchase order forms, confirms, then is collected from the tabletop. | Concentration → relief. |
| 03 | Checking paperwork builds up at the records table. ART recoils and sweats. | Urgency and overwhelm; no false completion. |
| 04 | A cutaway carton visibly dwindles to a remaining stock symbol. ART recoils, the low-stock alert appears, then ART starts checking incoming stock. | Shock → urgency → focused action. |
| 05 | A loaded pixel truck enters with its cab leading leftward. ART checks on-hand stock first, counts the incoming cartons, then compares them on the tablet. The loaded truck remains in transit; it does not unload into on-hand stock. | Attention → verification → relief. |
| 06 | The existing ₹10,000 example limit remains clear: the ₹6,000 path completes; the ₹15,000 request remains pending. Pixel documents and reactions replace mixed-style icons. | Routine confidence → exception urgency. |
| 07 | ART hurries the above-limit request to a person. A hand reaches from the frame edge, grips the request and takes it to the review tray. It remains awaiting a decision. | Urgency → attentive waiting; no automatic approval. |
| 08 | ART releases completed routine orders along a pixel roller belt. They leave before ART jumps and celebrates. The separate human-review tray stays pending. | Focus → relief → celebration. |
| 09 | “Stock handled. Time handed back.” A pixel clock settles, the routine-order box confirms and ART raises both arms. “Put ART to work.” provides the closing action. | Pride and celebration. |

ART (A Realtime Tech) remains on the first and final slides. The new closing emphasises the team's time, rather than repeating rule settings.

All stock symbols are illustrative. No quantities, delivery guarantees or numeric time-saving claims are added. The ₹10,000/₹6,000/₹15,000 values remain illustrative spending examples. A completion mark on incoming cartons means they have been included in the check, not received into stock. Exception handoff means sent for review, not approved.

## Visual system and timing

- Canonical Preahvihear Regular headlines and Poppins body text; no synthetic weights.
- Main copy stays stationary and readable from frame one.
- Same mascot model and 240px scale across scenes; pixel cartons, papers, truck, hand, roller belt and clock support the story.
- 84px text margins, photographed backgrounds at native resolution and consistent white/ink/aqua branding.
- Red antenna and wide eyes communicate urgency. Green appears only on completion marks. One restrained pixel-confetti burst follows the dispatch celebration.
- Durations: 8, 6, 7, 7, 8, 8, 8, 7 and 7 seconds. Total: 66 seconds. Every frame and JPEG is 1080 × 1350; videos run at 30fps.

Background files remain unchanged. No new paid generation was used. The existing generated images are illustrative and do not depict an identified real business. Preahvihear lacks the curly apostrophe, which alone uses the approved Poppins family.

## Reproduce

```bash
source /workspace/art-carousel-venv/bin/activate
python build.py
python stills.py 2,3,4,5,6,7,8,9
python motion-sheets.py 2,3,4,5,6,7,8,9
python render-lossless.py 2,3,4,5,6,7,8,9
python audit.py
python package.py
```

Keep the approved opening master and still in place. The audit checks their hashes and the approved scene/model source. It also checks copy, actual rendered fonts, margins, fixed text, scene motion, image loading, JavaScript errors and per-video metadata. Exported video frames are compared against the browser reference stills. The ZIP includes nine native MP4s, nine high-quality JPEGs, a nine-page PDF and validation reports.

Delivered on `stock-reorders-style-1-v12`. Earlier versions stay on their separate branches.
