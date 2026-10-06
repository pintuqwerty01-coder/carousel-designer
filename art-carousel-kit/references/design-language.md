# ART carousel design language

The look in one line: **a playful pixel robot acting out the busywork, on clean flat-vector sets, inside a calm white/ink/aqua brand frame, with teal-green only where things get done.**

Every rule below came from the ART team's review of the "6 things your team could stop doing by hand this week" carousel (October 2026). The reasons are given so new posts can extend the style rather than copy it.

## Contents
1. Brand tokens
2. Slide templates
3. The mascot
4. Props and sets (vector)
5. Accent colour rule
6. Dynamic UI on every slide
7. Motion rules
8. Things we tried and dropped

## 1. Brand tokens (from ART-Brand-Guidelines-2026)
| Token | Value | Notes |
|---|---|---|
| Primary aqua | `#04ADC3` | brand, structure, robot |
| Ink | `#1A1A1A` | text, outlines, dark slides |
| White | `#FFFFFF` | task-slide background |
| Accent teal-green | light `#41A486` → mid `#2B907F` → deep `#1C5E55` (dark `#173331`) | ONLY results, lit windows, checks (see §5) |
| Support | red `#F27A7A` (problems, "!", mismatch), yellow `#FFD166` (big purchase, reply, bell), light aqua `#9BE3EC` / `#DDF3F7` (fills) | |
| Headline font | Preahvihear | brand font |
| Body font | Poppins 400/500/600/700 | approved 2026-10-05 |
| Size | 1080 × 1350 (4:5) | IG |
| Margins | 84 px sides; content must end above 1220 px (handle zone) | `stills.py` checks it |
| Handle | `@arealtimetech`, bottom-left; counter `0i/0n` bottom-right | placeholder until confirmed |

**Logo:** full logo only on the reveal slide, only on white, ink or aqua, never on a photo, no effects or recolouring, min 121 × 44 px, clear space = icon height. Motion on it: fade plus 96→100 % scale only, never animate parts of the icon. The old website wordmark is retired.

## 2. Slide templates (`scripts/build.py`)
| Template | Background | Contents |
|---|---|---|
| `cover` | full-bleed cover image (see free-cover.md) with a top shade | headline (accent words aqua), subline, aqua "Swipe →" pill, the robot acting inside the scene |
| `task` | white | aqua counter pill `1/6` + uppercase label; Preahvihear question headline with ONE highlighted phrase (aqua band behind the lower 50 % of the line); one pain line; the **stage card** (robot scene); "What if…" box; outcome chips |
| `reveal` | ink | logo top-left, pride-led headline (accent words aqua), body (ART name in aqua), aqua line, grey sign-off, the robot walks in and celebrates |
| `cta` | aqua | big question, numbered chips (one per task) that light up in turn as the robot points, comment/DM line, save line with a bookmark that drops in, the robot in a white card |

Copy length is deliberately short: headline + one pain line + one what-if line + 2–3 chips. The pictures carry the explanation (review feedback: "all the slides are text heavy").

## 3. The mascot: the pixel robot (`assets/kit/js/pixelbot.js`)
- The **only** pixel-art element in the carousel. Its chunky pixels against smooth vector props are what make it read as a character (the Claude Code critter idea).
- **One size everywhere: 10 px per art pixel, 240 px tall.** Task stages draw at u = 8 on a stage scaled ×1.25; full-frame slides (cover, reveal) and the CTA card draw at u = 10. Never mix sizes.
- Poses step at 8 per second (S = floor(t × 8)); positions snap to 4 px. This stepped motion is intentional, so don't tween the robot smoothly.
- Mood is told with the antenna bulb and face: **red blinking bulb + wide eyes + wobble mouth + sweat = overwhelmed; yellow bulb + focus eyes = working it out; aqua bulb + happy eyes + grin = sorted.** End most scenes with a small button: tea, a wave, a blink or a hop.
- On dark slides it gets a white halo and white legs; on the aqua CTA it sits in a white card.
- Humour targets the busywork, never the business or its people.

## 4. Props and sets: smooth flat vector (`assets/kit/js/props-vector.js`)
- Rounded shapes, 2.5–3 px ink outlines, brand fills, soft shadows, anti-aliased. Real-world objects drawn simply: smartphones, storefronts with striped awnings, documents with folded corners, cartons, shelves, conveyor belts, rubber stamps, chat bubbles with typing dots, inbox trays, bells, mugs with steam.
- Props move on continuous time with easing (eOut, eInOut, eBack overshoot), unlike the stepped robot. Pops use overshoot; drops use gravity (k²) then a small bounce.
- **Staging rule: the robot is never behind or under a prop.** It stands in a clear gap; its hand meets the prop's edge. A desk, counter or booth may hide its legs only (like a person behind a counter). Lines and links go behind the robot. Details and spacing math are in scene-authoring.md.

## 5. Accent colour rule (teal-green)
Teal-green means **"done / result"** and appears in exactly three places:
1. **Result chips** on task slides: gradient fill (light→mid→deep, 135°), white text, white ✓ that draws itself, soft shadow.
2. **Lit windows** (e.g. a shop window glowing when its update lands).
3. **Every check mark**: ✓ on finished props, ✓ badges (gradient circle, white ring, white tick, overshoot pop), stamp marks.

Everything else stays aqua or ink: the highlight band, the what-if box, trails, planes, the robot, pills, labels. (A lighter "mixed green" on more elements was tried first and narrowed to these three.)

## 6. Dynamic UI on every slide
- **Bottom trail:** dotted aqua line across the full width, solid up to this slide's position (i/n), filling during the first 0.8 s; a tiny pixel robot head rides the end; half-gears on the left and right edges so the swipe looks continuous. On the aqua CTA the trail turns ink.
- **What-if box:** aqua tint sweeps in from left to right at 1.4 s, with an aqua edge bar.
- **Outcome chips:** ✓ draws on from 2.6 s, staggered 0.2 s.
- **CTA:** chip rings light in sequence while the robot points; the bookmark drops at 2.8 s.

## 7. Motion rules
- 4 s per slide, 30 fps, MP4 per slide (Instagram plays them as a carousel of videos).
- **Text never moves and is readable from frame 1.** No fades, slides or typewriter on copy. `render.py` checks that headline pixels don't change.
- Scene story arc in ~4 s: problem (0–1.5 s) → turn (≈1.2–2.5 s) → resolution with teal checks (≈2.5–3.5 s) → button (last 0.5 s).
- Cover: photo pushes in 1.00 → 1.05 over 4 s; swipe arrow nudges from 2.6 s.
- Reveal: logo fade + 96→100 % scale only.
- Calm easing for UI (power2/sine); playful overshoot only on pops and the bookmark.

## 8. Tried and dropped (don't bring back)
- Text-heavy "clean" slides (v2) and before/after split panels (v3 "playful").
- Pixelated props, desks, trails (only the robot stays pixel).
- A hand-drawn aqua scribble under words ("not required").
- Count-up numbers (copy rules ban numbers until approved) and a meme slide.
- Robot at different sizes on different slides.
- Using paid image generation by default (covers now come from free routes).
