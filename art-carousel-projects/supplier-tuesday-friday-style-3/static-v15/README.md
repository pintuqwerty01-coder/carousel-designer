# Static v15 — delivery-pad and mobile element/text design

User request: change the element and text design of the pad on slide 1 and mobile on slide 2.

Slide 1: replace the loose text on the clipboard with an editable delivery-status composition. A calendar header, aligned expected/current date rows, a restrained red “Not received” state and an aqua follow-up state establish a clear hierarchy. Text follows the physical paper's angle and stays inside the frame.

Slide 2: replace the sparse messages with a generic supplier conversation UI, including supplier header, separate update/reminder message cards, sent states and an awaiting-reply status. “Dispatch confirmed?” and “When will it arrive?” are outgoing questions, not invented supplier replies. The interface does not represent or claim a named messaging integration. Its scale/skew follows the photographed screen. The awaiting-reply status is checked against the screen-panel bounds.

All six photographs and the white-limb mascot design are unchanged. Main headings and body text are unchanged. Slides 3–6, including the upper-left closing logo and governance slide, are byte-identical to v14 in the PDF and individual exports.

`build.py` creates editable HTML from v14, `content.json` records main copy and the new prop copy, and `render.py 1 2` verifies fonts/copy/bounds before rebuilding the full six-page PDF, native 1080×1350 JPEG/PNG exports, overview and ZIP. Existing versions remain archived.
