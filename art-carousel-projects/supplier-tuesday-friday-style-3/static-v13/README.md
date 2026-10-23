# Static v13 — closing-slide design correction

Slide 6 only: increase the original blue/black logo from 150 to 224px wide, preserve its vector geometry, and provide clear space on a white CTA panel. Separate logo and CTA text into aligned grid columns with a subtle divider. Centre both columns vertically; retain left-aligned wording.

Create a clearer copy hierarchy: the opening sentence is a smaller 35px lead-in; “Put ART on the follow-through” becomes the dominant two-line 72px headline. Set the 30px supporting copy in three balanced lines with a narrower measure, away from the mascot antenna. Shared left alignment remains x=84px. The white CTA panel remains within the same 84px side margins and ends above the footer.

All marketing words, logo geometry, mascot, photograph and colours remain the same. Slides 1–5 are copied byte-for-byte, including native PNGs, printed PDF pages and JPEGs. Historical v12 remains archived.

`slides/slide-06.html` is editable source. `content.json` records the unchanged words with the new hierarchy and line breaks. `render.py 6` checks copy/font/bounds and exports the revised closing slide, then rebuilds the six-page PDF and complete slide ZIP from the retained first five pages.
