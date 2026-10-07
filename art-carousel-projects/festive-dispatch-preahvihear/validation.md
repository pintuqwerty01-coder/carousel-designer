# Latest script validation

- All nine PNGs exported at 1080 × 1350 with all images loaded.
- Every displayed line in the latest user-supplied script is retained, including setup topics, two checks per task, reveal ease/greeting and CTA engagement prompts.
- Large FESTIVE RUSH (vertical), PAPERWORK and faded CLOCKWORK are present. The setup direction is the downward arrow in the latest script.
- Actual Chromium rendered glyph fonts are exclusively embedded Preahvihear for headings, body, footer, CTA, added prompts, engagement line and decorative words. Details: `proof/font-validation.json`.
- Checks, arrows, separators, lamp and engagement icons use vector artwork with original characters retained in HTML. Synthetic bold and italic are disabled.
- Text blocks and actual rendered rectangles pass safe bounds. Headline/body, body/ease/signoff, prompt/outcome, CTA/save/engagement separation checks passed.
- Nine-page PDF regenerated. Every exported page decoded with Poppler and visually reviewed in `proof/exported-pdf-overview.png`.
- Clock hands rotate around the exact clock centre at 0, 1 and 2 seconds; clock frames differ while the entire copy area stays pixel-identical.
- Reveal MP4: 1080 × 1350, 30fps, four seconds, 120 frames, H264/yuv420p; actually decoded and played in Chromium.
- Original ART mark preserved. Clock motion is beside the logo, with a still frame in the PDF and motion in the separate MP4.
- This revision updates all nine static designs and one reveal motion clip. It does not re-export videos for older first-six scripts.
