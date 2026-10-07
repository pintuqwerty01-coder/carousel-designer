# Festive dispatch — updated nine-slide script

All nine slides use the latest user-supplied copy. `content.json` stores the exact displayed wording, emphasis markers and separate visual directions. Editorial labels and the CTA button brackets are layout directions, not extra visible copy.

Preahvihear Regular is used throughout: headings, body, prompts, outcomes, CTA, footer and large background words. Synthetic bold/italic is disabled. Emphasis uses aqua. Checks, arrows, separators and emoji are vector artwork so no fallback font enters the export.

Approved realistic festive photo scenes and mascot are retained. The final three use the cohesive brand ink background (#1A1A1A), white cards and restrained aqua accents. The unchanged original ART logo is on the reveal only.

New details:
- Cover: new festive-season headline, dispatch reassurance, festive-orders subline and swipe prompt.
- Setup: right-side HERE'S WHERE ↓, four-part topic list, large vertical FESTIVE RUSH.
- Task pages: shortened copy and two explicit check-mark outcomes each; PAPERWORK is the large background word on slide 05.
- Reveal: new ART platform explanation, ease line, team greeting, faded CLOCKWORK and a sweeping clock beside the original logo.
- Outcome: everything moves seamlessly and the new customer-focused summary.
- CTA: new festive deadline headline and preparation message, DM panel, save/share copy and all three engagement prompts.

Deliverables: `stills/slide-01.png` through `slide-09.png` (1080 × 1350), nine-page `static-review.pdf`, overview proofs, and `render/out/slide-07.mp4` (four seconds, 30fps). The PDF is static; the MP4 shows the clock-hand sweep. Existing videos for older scripts are not part of this image/PDF delivery.

`update-content.py` records this content revision. Regenerate with `capture-statics.py`, `make-review.py`, `preview-endings.py` and `audit-fonts.py`. Reveal motion uses `render-reveal.py 7` and `check-reveal-motion.py`. `check-pdf.py` assembles the Poppler-decoded exported pages for visual review.

Unused prior hand asset: Twemoji v14.0.2, Twitter and contributors, CC-BY 4.0. Original attribution retained in `slides/assets/point-down-attribution.txt`.

## Placement refinement

The latest script is unchanged. The cover uses a stronger headline and balanced reassurance lines. Setup topics have even spacing and aqua numerals. Task headlines put the highlighted concept on its own line; body and question copy use deliberate clause breaks. Questions share a lower edge and sit 28px above the outcome cards. The reveal separates the ART introduction from its explanation, enlarges body text and groups the ease line and greeting. Outcome cards sit closer to their heading and summary. The CTA calendar is scaled to create space for a distinct DM card, save line and engagement row.

`improve-layout.py` records these placement changes after `update-content.py`. All nine stills and the full PDF were refreshed; the reveal video was re-rendered to match.
