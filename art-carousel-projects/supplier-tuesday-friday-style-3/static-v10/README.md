# Static v10 — distinct copy roles, fewer repeated elements

User request: do not repeat boxed content in sentences on the same slide; make the carousel catchy, attractive, sensible and understandable.

The original white-limb v9 scene PNGs are referenced directly, unchanged. Mascot geometry, expressions, pose, colour, photographic backgrounds and original logo are retained. Preahvihear, font sizes, margins and graphic styling remain the same.

Copy structure:

- Cover: retain the established Tuesday/Friday/ART hook, one capability sentence and one short swipe cue; remove repeated outcome cards.
- Slide 2: hook = waiting team; body = time lost to chasing; cards = missing materials and packing impact.
- Slide 3: hook = check before follow-up; body = comparison method; cards = evidence that the delivery is overdue.
- Slide 4: hook = reminder already sent; body = the burden removed from the team; the existing phone shows the actual request. No extra boxes restate that message.
- Slide 5: hook = clearer picture; body = what ART does when a reply arrives; cards = record fields, with the revised date qualified by “if provided.”
- Slide 6: hook = unanswered delays stay visible; body = notification; cards = the delivery and affected work included in that context.
- Slide 7: hook = human decision; body = handover contents; cards = next-step options. No completion ticks imply those options have been executed.
- Closing: team-focused hook, ART named in supporting copy, original logo and one CTA.

All lower scene-caption sentences are removed. Task-slide prompts are removed where they duplicated the body/cards. Outcome icons become neutral aqua bullets because the cards now contain evidence, record fields or choices rather than completed actions.

`content.json` is canonical; `build.py` creates layouts from the v9 source without modifying it. `render.py` checks copy, presence/absence of elements, actual font use, bounds and image loading before native 1080×1350 exports. `delivery/` contains PDF, JPEGs, overview and ZIP including PNGs. This is a static review revision, not a new motion set.
