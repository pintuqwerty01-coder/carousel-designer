---
name: art-carousel-design
description: Design and render animated Instagram carousels for ART (A Realtime Tech) by Aiotrix in the ART house style. A pixel-robot mascot acts out each post's busywork on smooth flat-vector sets inside a white, ink and aqua brand frame, with teal-green reserved for results; every slide is a 4-second 1080x1350 MP4. Covers come from free routes only (a Google AI Studio or Gemini prompt, or a free Pexels or Unsplash photo). Use whenever someone asks to design, build, animate or render an ART or Aiotrix carousel, turn an approved ART carousel script into slides, make an ART carousel cover, or redo slides in the ART style, even if they only give the post title. Not for other brands, ART Reels, or LinkedIn static carousels.
---

# ART-carousel-design

Turns an approved ART carousel script into finished, animated Instagram slides in the ART house style. The style was set and approved by the ART team on the first carousel ("6 things your team could stop doing by hand this week", October 2026). Every new post keeps the same look and gets its own scenes, gags and cover.

**Fixed across posts**: brand frame, slide templates, the robot, prop style, accent-colour rule, motion rules, checks.
**New for every post**: the cover image, the robot's gag on each task slide, and the props that tell that post's story.

> **Reading this as a single file?** Everything mentioned below as `references/…`, `scripts/…` or `assets/…` is included further down, in the Appendix. You can read those sections directly, or unpack them into a folder with the snippet under "Unpack".

## Read first
- `references/design-language.md`: the whole look and the reason for each rule. Read it every time.
- `references/scene-authoring.md`: how to write a new robot scene (stage, robot anatomy, prop library, staging maths, beat template). Read before writing scenes.
- `references/free-cover.md`: the two free cover routes and the prompt pattern. Read at the cover step.
- `references/copy-rules.md`: the script rules the visuals must respect. Flag problems; never rewrite copy.
- `assets/kit/js/scenes-library.js`: six tested task scenes plus cover, reveal and CTA. Reuse or adapt them.
- `assets/example-content.json`: the complete content file of the first approved carousel.

## Setup
The design work (planning, laying out copy, writing scenes, cover prompts) needs only an assistant that can read this skill. Producing the actual files needs a computer with:
- **Python 3.10+** with `pip install playwright pillow`, then `python -m playwright install chromium` (for stills and checks)
- **Node.js 18+** (`npx` runs HyperFrames 0.8.55, which renders the MP4s; it downloads itself on first use)
- **ffmpeg** on the PATH (checks the videos)

Then run `python scripts/setup_assets.py` once. It downloads the free fonts (Preahvihear and Poppins, Open Font License) and the GSAP animation library if they're missing, and reports which tools are present. The ART logo is already included.

If the tools aren't available, still do steps 1–4 (plan, cover, content file, scenes) and hand the project folder to someone who can run the scripts.

## Workflow

Keep updates short. Show a plan before building, use multiple-choice questions where there's a real choice, and show one finished slide before making all of them.

### 1. Get the approved script
Ask for the approved carousel script for the post (file or pasted text). Use the Instagram carousel copy exactly as written. If it isn't approved yet, or the copy breaks `references/copy-rules.md`, say so before designing.

### 2. Plan the gags and get an OK
For each slide, write one line in a short table: what the robot does, which props, the messy→sorted turn, and where teal checks appear. Reuse a library scene when the task matches; otherwise plan a new one. Keep a story arc across the carousel: the robot arrives overwhelmed on the cover, sorts each task, celebrates on the reveal, and points at the chips on the CTA. Wait for approval.

### 3. Cover image (always offer both free routes)
Ask which route to use this time, as a multiple-choice question:
- **A.** An AI prompt the user runs for free in Google AI Studio or Gemini
- **B.** A free stock photo from Pexels or Unsplash

Follow `references/free-cover.md`: write the prompt, or the brief and search terms, give click-by-click steps, wait for the image, then run `fit_cover.py`. Never use a paid image service unless the user asks for it and has seen the cost.

### 4. Set up the project
```bash
python scripts/new_project.py <projects_folder>/<post-slug> "<full post title>"
```
Fill `content.json` from the script. Templates are cover, task, reveal and cta; `**double asterisks**` mark the highlighted or accent words. Set the cover `opts` (where the robot stands on the image). Write any new scenes in `<post-slug>/scenes.js`, following `references/scene-authoring.md`. Keep the project in a normal local folder (renders are heavy), not inside a synced cloud folder.

### 5. Build, then look
```bash
python scripts/build.py <project>            # all slides, or: build.py <project> 1,2
python scripts/sheets.py <project> 02        # 9-frame sheet per slide -> proof/sheet-NN.png
python scripts/stills.py <project>           # final-frame stills + layout and font checks; every slide must print OK
```
**Open and look at every sheet you changed.** It catches what a reviewer would catch: the robot behind a prop, clipped props, unreadable beats, wrong colours. Fix, rebuild, look again.

### 6. Show one before all
Render the **cover plus one task slide** first (`python scripts/render.py <project> 01,02`) and share them. After approval, build and render the rest. When feedback is about the style, apply it to the whole carousel, not just the slide it was given on.

### 7. Render and verify
```bash
python scripts/render.py <project>
```
Every slide must report `lint=0 errors`, `1080,1350,30/1 4.000000` and `headline-px-moved=0`. The cover and reveal are exempt from the last one: the cover photo pushes in behind static text, and the reveal logo fades in. Then pull one or two real frames from the MP4s with ffmpeg and look at them.

### 8. Hand over
The MP4s are in `<project>/render/out/`, the stills in `<project>/stills/`. Send them in posting order with a few lines: what each slide does, the check results, and where the files are. If the user wants everything gathered in one folder (MP4s, stills, cover, content file, a preview strip), run `python scripts/publish.py <project> <their folder> --archive-as <tag>`. `--archive-as` keeps an earlier version instead of overwriting it.

## The rules that matter most (reasons in design-language.md)
- Only the robot is pixel art, at one size everywhere (240 px). Everything else is smooth vector.
- The robot is never behind or under a prop.
- Teal-green appears only on result chips, lit windows and check marks.
- Text never moves; copy stays short; the picture explains.
- The ART logo appears only on the reveal. No real companies, product screens or numbers. Humour targets the busywork, never the business.
- Covers cost nothing by default; offer both free routes every time.
- Report honestly: if a check fails or something looks off, say so. Never say a file is done without having checked it exists.

## Extending the system
- New prop: add a `v…` function to `assets/kit/js/props-vector.js` in the same style.
- A scene worth reusing: move it from the post's `scenes.js` into `scenes-library.js`.
- New slide type: add a template function to `scripts/build.py`, check it at true 1080 × 1350 with `stills.py`, and document it in `references/design-language.md`.
- When the team changes a style rule, record the rule and the reason in `references/design-language.md`, then run `python scripts/make_single_file.py` to refresh the single-file edition.

<!-- END SKILL -->

# Appendix: every file in this skill
This single file contains the whole skill. If your assistant can read it, it can follow the instructions above directly; the sections below are the reference documents and the code the instructions point to (`references/...`, `scripts/...`, `assets/...`).

## Unpack

Run this once with Python 3, in the folder where you saved this file. It rebuilds the full skill folder
(`ART-carousel-design/`) next to it, then run `python ART-carousel-design/scripts/setup_assets.py`.

~~~~python
import base64, pathlib, re
src = pathlib.Path("ART-carousel-design.md").read_text(encoding="utf-8")
out = pathlib.Path("ART-carousel-design")
out.mkdir(exist_ok=True)
(out / "SKILL.md").write_text(src.split("<!-- END SKILL -->")[0].rstrip() + "\n", encoding="utf-8")
for path, kind, body in re.findall(r"<!-- FILE: (\S+) (text|code|base64) -->\n(.*?)\n<!-- END FILE -->", src, re.S):
    f = out / path; f.parent.mkdir(parents=True, exist_ok=True)
    if kind == "code": body = body.split("\n", 1)[1].rsplit("\n", 1)[0]          # strip the ~~~~ fences
    if kind == "base64": f.write_bytes(base64.b64decode(re.sub(r"\s", "", body.split("\n", 1)[1].rsplit("\n", 1)[0])))
    else: f.write_text(body + "\n", encoding="utf-8")
    print("wrote", f)
~~~~

---

<!-- FILE: references/design-language.md text -->
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
<!-- END FILE -->

---

<!-- FILE: references/scene-authoring.md text -->
# Writing a scene for a new post

Each task slide gets its own gag: the robot acts out the busywork, then the "what if" happens and teal checks appear. Scenes are plain canvas functions that redraw one frame from the time `t`. They go in `<project>/scenes.js` as `Object.assign(SCENES_DYN, { myScene(ctx, t, S) { ... } })`, and `content.json` points to them with `"scene": "myScene"`.

Read the library first (`assets/kit/js/scenes-library.js`). Its six task scenes (`calls`, `docs`, `stock`, `bills`, `chats`, `approvals`) are tested worked examples of everything below. Reuse one directly when a post covers the same task; otherwise copy the closest one and change it.

## Contents
1. The stage
2. Robot anatomy and poses
3. Prop API
4. Staging rules and spacing math
5. Timing and the beat template
6. Draw order
7. Checklist

## 1. The stage
- Virtual stage **728 × 336**, drawn into a 912 × 420 canvas scaled exactly ×1.25. Keep robot positions multiples of 4.
- Floor (robot feet): `VF = 316`. Robot top when standing on the floor: `VY = VF - 184 = 132`.
- A pale floor band covers the bottom ~22 px. Desks sit with their top at y ≈ 284–292 and their front panel down to 336.
- Full-frame scenes (cover, reveal) use the real 1080 × 1350 canvas with no scale, and draw the robot at `u = 10`. The CTA card is 352 × 300 with `u = 10`.

## 2. Robot anatomy (24 × 24 grid; at u = 8 one cell = 8 virtual px, 192 px total)
| Part | Grid | At robot (x, y), u = 8 |
|---|---|---|
| Antenna bulb | x 10–12, y 0–1 | top of the robot = y |
| Head (with ears) | x 3–19, y 4–13 | x+24 … x+160, y+32 … y+112 |
| Body | x 6–16, y 14–19 | x+48 … x+136, y+112 … y+160 |
| Legs | y 20–22 | y+160 … y+184 (feet) |
| Left arm | x 2–5 | from x+16 |
| Right arm `reach` | to x 21, y 15 | hand tip x+168 … x+176 at y+120 |
| Right arm `tap` | to (20, 18) | tip x+160 … x+168, y+144 … y+152 |
| Right arm `up` | to (19, 11) | hand x+152 … x+160 at y+88 |
| Right arm `hold` | (18, 16) | hand x+144 … x+152, y+128 … y+136 (hold a mug here) |

`drawBot(ctx, x, y, u, pose)` pose fields:
- `legs`: stand / stepL / stepR / tuck (`walkLegs(S)` alternates steps)
- `armL`: down / up / flex / out
- `armR`: down / up / wave1 / wave2 / flex / reach / hold / tap
- `eyes`: open / lookL / lookR / blink / happy / wide / squint / focus
- `mouth`: smile / grin / wobble / o / flat / open
- `bulb`: red / yellow / aqua, plus `bulbOff` to blink it
- `flip` mirrors it (it faces the way it walks); `dark` + `halo` for dark slides

Shadow: `vShadow(ctx, x + 96, VF + 4, 120, lift)`; pass the hop height as `lift` so it shrinks mid-air. A hop is `legs: "tuck"` with y offsets like `[-24, -40, -24, 0]` over 4 steps.

## 3. Prop API (`props-vector.js`; all smooth vector, take virtual-stage coordinates)
| Function | What it draws |
|---|---|
| `vDesk(ctx, x0, x1, top, h=44)` | ink-topped desk with an aqua-tint front |
| `vPhone(ctx, cx, bottom, t, ring, quietK, icon="call"\|"bell")` | smartphone; ringing = buzz + icon, else a teal ✓ that draws with quietK 0→1 |
| `vRings(ctx, cx, cy, t)` | expanding ring waves |
| `vTapBurst(ctx, x, y, k)` | impact lines where the hand taps |
| `vShop(ctx, cx, top, lit, bump)` | storefront, striped awning; lit = teal-green window |
| `vFlight(ctx, p0, p1, p2, k)` / `vPlane` | paper plane along a curve with a dashed aqua trail |
| `vBadge(ctx, cx, cy, k, r=15)` | teal-green ✓ badge popping with overshoot |
| `vMark(ctx, cx, cy, "?"\|"!", k, "q"\|"bang", s)` | speech bubble mark (white "?" or red "!") |
| `vSweat(ctx, x, y, t, dir)` | sweat drops flicking off |
| `vMug(ctx, x, bottom, t)` | mug with steam (handle on the left, toward the robot's hand) |
| `vPaper(ctx, x, y, w, h, {head, label, rot, alpha})` | document with folded corner |
| `vKeyboard(ctx, x, y, w, t, typing)` | keys that light while typing |
| `vFlag(ctx, x, bottom, t, k)` | red flag that springs up and waves |
| `vBeam(ctx, x, y0, y1)` | glowing scan beam |
| `vShelf`, `vBox`, `vPoof` | shelving, cartons, smoke puff |
| `vSlip(ctx, x, y, w, h, {big})`, `vStamp`, `vStampMark` | slips, rubber stamp, teal approval mark |
| `vLens(ctx, cx, cy, r, hx, hy)` | magnifier held from the hand |
| `vCurve(ctx, p0, p1, p2, k, color, {arrow, dash})` | dotted link or arrow |
| `vBubble`, `vTrayBack`/`vTrayFront` | chat bubble with typing dots; inbox tray |
| `vBelt`, `vGate`, `vBell`, `vHeart`, `vGear` | conveyor, gate with signal light, bell, heart, gear |
| helpers | `rr` (rounded rect path), `fs` (fill/stroke), `tick`, `lerp`, `clamp01`, `eOut`, `eInOut`, `eBack`, `qb`/`qbAng` |

Need a new prop? Add a `v…` function to `props-vector.js` in the same style (rounded, 2.5–3 px ink outline, brand fills, takes `t` or `k` for motion), and use teal-green only if it's a result, a lit window or a check.

## 4. Staging rules and spacing math
The rule: **the robot is never behind or under a prop, and props never cover its face or body.** Reviewers flagged this twice on the first carousel.
- When the robot works through a row of props (phones, documents), stand it in the gap to the **left** of each one: prop left edge = robot x + 168 (the hand tip). The previous prop's right edge must stay left of the robot's left arm (x + 24). For ~40 px wide props that means about **184 px between stops**. The proven layout: prop centres 300 / 484 / 668, robot stops 112 / 296 / 480.
- A desk, counter or booth may hide the robot's legs only. Keep it as the robot's "workstation"; things on top of it sit beside the body, not over it.
- Lines, links and arcs are drawn **before** the robot, so they pass behind it. Arc links peak at y ≈ 100 so they clear the antenna.
- Things the robot holds (slip, lens, mug) attach at the hand coordinates above, beside the head, never over the face.
- Nothing important within ~8 px of the stage edges, so props don't get clipped.

## 5. Timing and the beat template (4 s = 32 robot steps)
- Robot pose: from `S` (stepped). Props, checks and motion: from `t` with easing, so they move smoothly.
- Typical arc:
  - **0–1.5 s problem**: robot walks in or is already swamped; red blinking bulb, wide eyes, wobble mouth, sweat; props pile up, ring or chase.
  - **≈1.2–2.5 s turn**: focus eyes, yellow bulb; the "what if" action (scan, stamp, file, approve, send).
  - **≈2.5–3.5 s resolution**: aqua bulb, happy eyes; teal ✓ badges pop and lit windows glow.
  - **3.5–4 s button**: tea, a wave, a blink or a victory hop.
- Make the change visible: something must clearly go from messy to sorted, so the slide reads without its text.

## 6. Draw order inside a scene
1. Background set pieces and anything that passes **behind** the robot (shelves on the far side, link arcs, wall items)
2. `vShadow` + `drawBot` (+ sweat)
3. Desk / counter / booth front
4. Props on the desk and in front
5. Marks, badges and checks on top

## 7. Checklist before rendering
- Build, then `sheets.py <project> NN` and **look** at the sheet: robot never behind a prop, nothing clipped, each beat readable, checks teal.
- Robot same size as the other slides (u = 8 on stages, u = 10 full-frame).
- Only the robot is pixel art. No `blitRows` or `SPR` sprites for props (legacy).
- Teal-green only on results, lit windows and checks.
- The gag pokes fun at the busywork, never at the business or its people.
<!-- END FILE -->

---

<!-- FILE: references/free-cover.md text -->
# Free cover image: two zero-cost routes

The cover is the only slide with a photo-style image. It must cost nothing by default. **Each time, offer the user both routes and let them pick** (ask with a multiple-choice question):

- **A. AI image, free tier**: the skill writes a prompt; the user generates it themselves in Google AI Studio or the Gemini app (free daily allowance). Best when the scene must be specific (a Mangaluru back office at dusk, festive dispatch, a port at night).
- **B. Free stock photo**: the skill writes a shot brief and search terms; the user picks a photo on Pexels or Unsplash. Real photos, free for commercial use, no AI look. Best when a generic real scene works.

Never use a paid image service (paid image-generation APIs, or design-tool AI features that spend credits) unless the user explicitly asks for it and has seen a cost estimate. Running an image model locally is free but needs a strong graphics card; don't assume one.

## What every cover needs (both routes)
- **4:5 portrait**, at least 1080 px wide (ideally 1280+).
- **Calm, dark top ~40 %** (sky, wall, window) with no clutter: the white headline goes there.
- **A clear patch in the lower RIGHT** (desk surface or floor) where the robot can stand. The bottom-left is taken by the aqua "Swipe" pill (about x 84–260, y 1140–1200), and a robot there collides with it (seen in testing). Use the left only if the patch is high enough to keep the robot's feet at y ≤ 1120.
- Tells the post's topic at a glance, with one local touch where it fits (coastal Karnataka, port cranes, cashew, festive lights).
- Mood: cinematic, warm amber practical light against cool teal dusk tones, which sit well with aqua.
- **No people, hands or faces. No readable text, logos, brand names or signage.** No real, identifiable business premises.

## Route A: prompt for Google AI Studio / Gemini
Write the prompt to this pattern (the approved "6 things" cover is the model):

```
Cinematic photoreal scene, vertical 4:5 composition. <topic scene: place, time of day, what the busywork looks like
as objects: piles, phones, boxes, slips…>. Behind it <local context: harbour, cranes, street, festive lights…>.
Lighting: warm amber practical light on the clutter, cool aqua-teal dusk light from <source>, soft haze, gentle film
grain, shallow depth of field, moody but inviting. The top 40 percent of the frame is calm and dark with no clutter,
leaving clean headroom for a headline. Keep a small clear patch of <surface> in the lower <right|left> corner.
No people, no hands, no faces. No readable text anywhere, no logos, no brand names, no signage; papers have only
blurred unreadable marks.
```

Click-by-click steps to give the user:
1. Open **aistudio.google.com** and sign in with a Google account (or use the **Gemini** app).
2. In the model picker, choose the Gemini model whose name includes **"Image"**.
3. If there's an aspect-ratio setting, choose **4:5** (portrait). If not, keep "vertical 4:5" in the prompt.
4. Paste the prompt and press **Run**. Generate 2–3 and keep the best.
5. Download it and save it into the post's `cover/` folder (or paste it into the chat).

Fallbacks if the free allowance is used up: **Microsoft Designer / Bing Image Creator** (free, Microsoft account) or **ChatGPT free tier** (a few images a day). Same prompt.

Before use: check for a **visible watermark** (free tiers sometimes add one; `fit_cover.py` flags bright corners; crop it out) and, because ART is a business, that the tool's terms allow **commercial use**.

## Route B: free stock photo
Give the user:
- **3–5 search terms** (for example "office desk paperwork night", "port cranes dusk", "warehouse cartons warm light", "diwali lights shop").
- **A one-line shot brief**: what to look for (dark calm top, clear lower patch, no people or faces, no readable signage).
- Where to search: **pexels.com** and **unsplash.com** (both free for commercial use, no attribution required, but record the photographer anyway).

The user downloads the largest size and saves it to `cover/`. Store the photo URL and photographer in `cover/source.txt` (via `--source`).

## Then, for either route
1. `python scripts/fit_cover.py <image> <project> --anchor center --source "<route, URL, credit>"`. Crops to 4:5, saves `cover/cover-art.png`, and checks headroom brightness, resolution and corners.
2. Set the robot's cover position in `content.json` → cover slide `opts`: `x` (left edge where it stops; the robot is 240 px wide, so keep x ≤ 800), `feet` (y of its feet, on the clear patch; default 1172), `from` (x it walks in from, e.g. 1100 from the right or -260 from the left; it faces the way it walks). Defaults (812 / 1172 / 1100) suit a lower-right patch.
3. Build the cover and look at it: is the headline readable on the shade, and does the robot stand on a surface, not floating over clutter?
<!-- END FILE -->

---

<!-- FILE: references/copy-rules.md text -->
# Copy rules the designer must respect

The designer **never writes or rewrites copy**. It lays out the approved script word for word. If copy breaks a rule below or won't fit, flag it to the user with a suggested fix; don't change it silently.

## Carousel structure (format D, curiosity format)
- **Cover**: hook headline + subline. ART is not named.
- **One task slide per pain point**: counter pill (`1/6`) + short label, question headline (one phrase highlighted), one pain line, a "What if / How about / Imagine" line, and 2–3 outcome chips. ART and tools (Zoho etc.) are not named.
- **Reveal**: the first and only slide that names ART: "ART (A Realtime Tech)", Aiotrix's Governed Automation Platform. The ART logo appears here only.
- **CTA**: one question, numbered chips (one per task), comment/DM line, save line.

## Tone (the ART team's standing rules)
- **Pride-led reveal.** The business is already good; ART is a layer on top of the tools it already runs ("no switching systems, no starting over"); you still set the rules. ART is never a rescue.
- **Never imply the business isn't at its best.** Use "even smoother / even more / even further". Avoid "finally", "fix", "get back on track", "less strain", "run like clockwork" (as if it doesn't already).
- Reveal wording is written fresh per topic; "and more" is used sparingly.
- Short: the pictures explain, the words land the point.
- No numbers until approved (so no count-up animations), no real company names, logos or premises, no product screens or UI. One local detail per post is welcome (Mangaluru, coastal Karnataka, the port, cashew, festive season).

## What the visuals must also respect
- Humour targets the busywork, never the business or its staff.
- Never present a real company as an ART user (no real shop signs or brand names in scenes or covers).
- The LinkedIn version of a post is a separate, formal asset; never cross-post the Instagram carousel there.
<!-- END FILE -->

---

### `scripts/setup_assets.py`

<!-- FILE: scripts/setup_assets.py code -->
~~~~python
"""Download the free third-party files the kit needs (only if they're missing), then check the toolchain.

Usage: python setup_assets.py
- Fonts: Preahvihear + Poppins 400/500/600/700 from the Google Fonts repository (SIL Open Font License).
- GSAP 3.14.2 from jsDelivr (free under GreenSock's standard licence).
Then reports whether Playwright/Chromium, Pillow, Node (npx) and ffmpeg are available.
"""
import pathlib, shutil, subprocess, urllib.request

KIT = pathlib.Path(__file__).resolve().parent.parent / "assets" / "kit"
GF = "https://raw.githubusercontent.com/google/fonts/main/ofl"
FILES = {
    "fonts/Preahvihear-Regular.ttf": f"{GF}/preahvihear/Preahvihear-Regular.ttf",
    "fonts/Poppins-Regular.ttf": f"{GF}/poppins/Poppins-Regular.ttf",
    "fonts/Poppins-Medium.ttf": f"{GF}/poppins/Poppins-Medium.ttf",
    "fonts/Poppins-SemiBold.ttf": f"{GF}/poppins/Poppins-SemiBold.ttf",
    "fonts/Poppins-Bold.ttf": f"{GF}/poppins/Poppins-Bold.ttf",
    "gsap.min.js": "https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js",
}

def main():
    for rel, url in FILES.items():
        dest = KIT / rel
        if dest.exists() and dest.stat().st_size > 1000: print("ok     ", rel); continue
        dest.parent.mkdir(parents=True, exist_ok=True)
        print("fetch  ", rel, "<-", url)
        urllib.request.urlretrieve(url, dest)
    print()
    checks = {
        "Pillow": "python -c \"import PIL\"",
        "Playwright + Chromium": "python -c \"from playwright.sync_api import sync_playwright as s; p=s().start(); b=p.chromium.launch(); b.close(); p.stop()\"",
        "Node / npx": "npx --version",
        "ffmpeg": "ffmpeg -version",
    }
    for name, cmd in checks.items():
        r = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        print(("ok     " if r.returncode == 0 else "MISSING"), name)
    print("\nIf anything is MISSING, see 'Setup' in SKILL.md. Planning, copy layout, scenes and cover prompts work without it;"
          "\nstills need Pillow + Playwright; MP4s also need Node and ffmpeg.")

if __name__ == "__main__":
    main()
~~~~
<!-- END FILE -->

---

### `scripts/new_project.py`

<!-- FILE: scripts/new_project.py code -->
~~~~python
"""Start a new ART carousel project.

Usage: python new_project.py <project_dir> "<full post title>"
Creates content.json (cover, one task slide, reveal, cta as a starting shape), scenes.js (a commented template
for this post's own scenes) and cover/. Fill content.json with the APPROVED script copy, word for word.
"""
import json, pathlib, sys

SCENES_TEMPLATE = """// Post-specific scenes for "{title}". Loaded after the skill's scene library, so you can use drawBot, every v* prop
// from props-vector.js, lerp/walkLegs/snap, VF and VY. One scene per task slide; reuse library scenes where they fit.
// See the skill's references/scene-authoring.md for the stage, robot anatomy, staging rules and a beat template.
Object.assign(SCENES_DYN, {{
  // example(ctx, t, S) {{
  //   // 1. props that sit BEHIND the robot (links, wall items)
  //   // 2. vShadow + drawBot (pixel robot, stepped by S)
  //   // 3. desk / counter, then props in front (on the desk), then marks, checks and badges on top
  // }},
}});
"""

def main(project, title):
    p = pathlib.Path(project); (p / "cover").mkdir(parents=True, exist_ok=True)
    content = {
        "title": title, "handle": "@arealtimetech",
        "slides": [
            {"template": "cover", "headline": "Headline with **accent words**", "sub": "Subline. **Accent part.**", "swipe": "Swipe",
             "opts": {"x": 812, "feet": 1172, "from": 1100}},
            {"template": "task", "n": 1, "of": 1, "label": "Task label", "scene": "calls",
             "headline": "Question headline with **one highlight?**", "pain": "One pain line.",
             "whatif": "What if ...?", "outcome": ["Outcome one", "Outcome two"]},
            {"template": "reveal", "headline": "Pride-led line with **accent**", "body": "That's where **ART (A Realtime Tech)** comes in. ...",
             "line": "No switching systems. No starting over.", "sign": "Made with pride in Mangaluru."},
            {"template": "cta", "headline": "Which one costs **you** the most?", "chips": ["One", "Two"],
             "main": "Comment the number or DM us ...", "save": "Save this for your next team meeting."},
        ],
    }
    if not (p / "content.json").exists(): (p / "content.json").write_text(json.dumps(content, indent=2, ensure_ascii=False), encoding="utf-8")
    if not (p / "scenes.js").exists(): (p / "scenes.js").write_text(SCENES_TEMPLATE.format(title=title), encoding="utf-8")
    print("project ready:", p.resolve())

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
~~~~
<!-- END FILE -->

---

### `scripts/fit_cover.py`

<!-- FILE: scripts/fit_cover.py code -->
~~~~python
"""Turn a free cover image (Google AI Studio / Gemini / Microsoft Designer output, or a Pexels/Unsplash photo)
into the cover art the build uses.

Usage: python fit_cover.py <image> <project_dir> [--anchor top|center|bottom] [--source "text"]
Writes <project_dir>/cover/cover-art.png (centre-cropped to 4:5, 1080x1350 or larger) and appends the source
(route, URL, photographer credit) to cover/source.txt.

Checks it prints (fix before building if any say WARN):
- resolution: the crop should be at least 1080 px wide, otherwise it will look soft
- headroom: the top 40% should be fairly dark and calm so the white headline reads (the slide adds a shade too)
- corners: a bright small blob in a bottom corner often means a visible watermark; crop or cover it
"""
import argparse, pathlib
from PIL import Image, ImageStat

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("image"); ap.add_argument("project")
    ap.add_argument("--anchor", default="center", choices=["top", "center", "bottom"])
    ap.add_argument("--source", default="")
    a = ap.parse_args()
    im = Image.open(a.image).convert("RGB"); w, h = im.size
    tw, th = (w, round(w * 5 / 4)) if w * 5 / 4 <= h else (round(h * 4 / 5), h)
    x0 = (w - tw) // 2
    y0 = {"top": 0, "center": (h - th) // 2, "bottom": h - th}[a.anchor]
    crop = im.crop((x0, y0, x0 + tw, y0 + th))
    if tw > 1280: crop = crop.resize((1280, 1600), Image.LANCZOS)      # plenty for a 1.05 push-in; keeps files small
    elif tw < 1080: print(f"WARN resolution: crop is only {tw}px wide; upscaling, may look soft. Prefer a bigger image.")
    if crop.width < 1080: crop = crop.resize((1080, 1350), Image.LANCZOS)
    out = pathlib.Path(a.project) / "cover"; out.mkdir(parents=True, exist_ok=True)
    crop.save(out / "cover-art.png")
    g = crop.convert("L"); W, H = g.size
    top = ImageStat.Stat(g.crop((0, 0, W, int(H * 0.4)))).mean[0]
    print(f"headroom brightness (top 40%): {top:.0f}/255", "OK" if top < 110 else "WARN: bright top; headline may be hard to read")
    for name, box in {"bottom-left": (0, int(H * .9), int(W * .2), H), "bottom-right": (int(W * .8), int(H * .9), W, H)}.items():
        s = ImageStat.Stat(g.crop(box));
        if s.extrema[0][1] > 235 and s.stddev[0] > 45: print(f"check {name} corner for a watermark")
    with open(out / "source.txt", "a", encoding="utf-8") as f:
        f.write(f"{pathlib.Path(a.image).name} -> cover-art.png ({crop.width}x{crop.height}, anchor {a.anchor}). Source: {a.source or 'not given'}\n")
    print("saved", out / "cover-art.png", f"{crop.width}x{crop.height}")

if __name__ == "__main__":
    main()
~~~~
<!-- END FILE -->

---

### `scripts/build.py`

<!-- FILE: scripts/build.py code -->
~~~~python
"""ART carousel builder (art-carousel skill): one HTML page per slide, ready for stills and HyperFrames render.

Usage:  python build.py <project_dir> [slide numbers, e.g. 1,2,9]
Reads   <project_dir>/content.json, optional <project_dir>/scenes.js (post-specific scenes),
        <project_dir>/cover/cover-art.png (made with fit_cover.py).
Writes  <project_dir>/slides/slide-NN.html (+ slides/assets/).
Rules baked in: text never animates; only canvas art, checks, sweeps and the cover image move.
"""
import json, pathlib, shutil, sys, html

SKILL = pathlib.Path(__file__).resolve().parent.parent
KIT = SKILL / "assets" / "kit"
CSS = (SKILL / "assets" / "shared.css").read_text(encoding="utf-8")
LIB = "\n".join((KIT / "js" / f).read_text(encoding="utf-8") for f in ["pixelbot.js", "props-vector.js", "scenes-library.js"])
DURATION = 4

BASE_CSS = """
:root { --g-lite: #41A486; --g-mid: #2B907F; --g-deep: #1C5E55; --g-dark: #173331; }   /* accent: teal-green (approved swatch). ONLY on result chips, shop windows and check marks */
.hl { background: linear-gradient(var(--aqua), var(--aqua)) no-repeat 0 80% / 100% 50%; padding: 0 .1em; margin: 0 -.04em; box-decoration-break: clone; -webkit-box-decoration-break: clone; }
.dark .hl { background: none; color: var(--aqua); padding: 0; margin: 0; }
.aqua .hl { background: linear-gradient(var(--white), var(--white)) no-repeat 0 80% / 100% 50%; }
.em { color: var(--aqua); font-weight: 600; }
.handle { bottom: 92px; }
.count { position:absolute; right: var(--pad); bottom: 92px; font: 600 24px/1 "Poppins", sans-serif; color:#8A8A8A; z-index:30; letter-spacing:.06em; }
.dark .handle, .dark .count { color: rgba(255,255,255,.75); }
.aqua .handle, .aqua .count { color: rgba(26,26,26,.75); }
#trail { position:absolute; left:0; bottom:0; width:1080px; height:80px; z-index: 40; image-rendering: pixelated; }
canvas { image-rendering: pixelated; }
"""

def hl(s):
    p = s.split("**"); return "".join(f'<span class="hl">{html.escape(x)}</span>' if i % 2 else html.escape(x) for i, x in enumerate(p))
def rich(s):
    p = s.split("**"); return "".join(f'<strong class="em">{html.escape(x)}</strong>' if i % 2 else html.escape(x) for i, x in enumerate(p))

def page(sid, theme, inner, css, scene_key, scene_canvas, js_extra, i, n, handle, dark, js_lib, opts):
    return f"""<!doctype html>
<html lang="en"><head><meta charset="UTF-8" />
<meta name="viewport" content="width=1080, height=1350" />
<script src="assets/gsap.min.js"></script>
<style>
{CSS}
{BASE_CSS}
{css}
</style></head>
<body>
<div id="root" data-composition-id="{sid}" data-start="0" data-duration="{DURATION}" data-width="1080" data-height="1350" data-fps="30">
  <div id="s" class="clip slide {theme}" data-start="0" data-duration="{DURATION}">
{inner}
    <div class="handle">{handle}</div>
    <div class="count">{i:02d}/{n:02d}</div>
    <canvas id="trail" width="1080" height="80"></canvas>
  </div>
</div>
<script>
{js_lib}
const SCENE_OPTS = {json.dumps(opts)};
const SCENE = {json.dumps(scene_key)}, SC = document.getElementById({json.dumps(scene_canvas)});
const TR = document.getElementById("trail"), TRX = TR.getContext("2d");
const st = {{ t: 0 }};
function render() {{
  const t = st.t, S = Math.min(31, Math.floor(t * 8 + 1e-6));
  if (SC && SCENE && SCENES_DYN[SCENE]) {{ const c = SC.getContext("2d"); c.setTransform(1, 0, 0, 1, 0, 0); c.clearRect(0, 0, SC.width, SC.height);
    const k = Number(SC.dataset.scale || 1); c.setTransform(k, 0, 0, k, 0, 0); SCENES_DYN[SCENE](c, t, S, SC.width / k, SC.height / k); c.setTransform(1, 0, 0, 1, 0, 0); }}
  TRX.clearRect(0, 0, 1080, 80); TRX.save(); TRX.translate(0, 26);
  const k = Math.min(1, t / 0.8); drawTrail(TRX, 1080, {i}, {n}, 1 - Math.pow(1 - k, 3), {str(dark).lower()}, {str(theme == "aqua").lower()}); TRX.restore();
}}
window.__timelines = window.__timelines || {{}};
const tl = gsap.timeline({{ paused: true }});
tl.to(st, {{ t: 4, duration: 4, ease: "none", onUpdate: render }}, 0);
{js_extra}
render();
window.__timelines["{sid}"] = tl;
</script>
</body></html>"""

def cover(c):
    css = """
.art { position:absolute; inset:0; z-index:0; overflow:hidden; }
.art img { width:1080px; height:1350px; object-fit: cover; display:block; transform-origin: 60% 60%; }
.shade { position:absolute; inset:0; z-index:1; background: linear-gradient(to bottom, rgba(8,14,20,.86) 0%, rgba(8,14,20,.62) 34%, rgba(8,14,20,0) 56%, rgba(8,14,20,0) 78%, rgba(8,14,20,.55) 100%); }
#scene { position:absolute; inset:0; z-index: 20; }
.cv-col { top: 96px; gap: 28px; }
.cv-h { font-size: 104px; line-height: 1.12; color: var(--white); text-shadow: 0 2px 24px rgba(0,0,0,.35); }
.cv-sub { font: 500 40px/1.4 "Poppins", sans-serif; color: #E3E3E3; text-shadow: 0 2px 14px rgba(0,0,0,.6); }
.cv-swipe { position:absolute; left: var(--pad); bottom: 150px; z-index: 30; display:flex; align-items:center; gap:14px; background: var(--aqua); color: var(--ink); font: 700 30px/1 "Poppins", sans-serif; padding: 18px 26px; border-radius: 999px; }
"""
    inner = f"""    <div class="art"><img id="artimg" src="assets/cover-art.png" alt="" /></div>
    <div class="shade"></div>
    <canvas id="scene" width="1080" height="1350"></canvas>
    <div class="col cv-col">
      <div class="h-display cv-h">{hl(c['headline'])}</div>
      <div class="cv-sub">{rich(c['sub'])}</div>
    </div>
    <div class="cv-swipe">{html.escape(c.get('swipe','Swipe'))} <span id="arr">&rarr;</span></div>"""
    js = """tl.fromTo("#artimg", { scale: 1.0 }, { scale: 1.05, duration: 4, ease: "none" }, 0);
tl.to("#arr", { x: 10, duration: 0.25, yoyo: true, repeat: 5, ease: "sine.inOut" }, 2.6);"""
    return "dark", css, inner, "cover", "scene", js, True

def task(c):
    css = """
.tk-top { position:absolute; left:var(--pad); top:76px; display:flex; align-items:center; gap:18px; z-index:10; }
.pill { font: 600 26px/1 "Poppins", sans-serif; color: var(--white); background: var(--aqua); padding: 14px 22px; border-radius: 999px; letter-spacing: .04em; }
.label { font: 600 24px/1 "Poppins", sans-serif; color: var(--aqua); letter-spacing: .14em; text-transform: uppercase; }
.tk-col { top: 156px; gap: 24px; }
.tk-h { font-size: 72px; line-height: 1.18; color: var(--ink); }
.tk-pain { font: 500 33px/1.4 "Poppins", sans-serif; color: var(--body-dark); }
.stage { position: relative; width: 912px; height: 420px; border-radius: 26px; background: #EEF9FB; overflow: hidden; }
.stage::after { content:""; position:absolute; left:0; right:0; bottom:0; height: 28px; background: rgba(4,173,195,.10); }
.stage canvas { position:absolute; inset:0; width:912px; height:420px; }
.tk-whatif { position: relative; font: 600 33px/1.42 "Poppins", sans-serif; color: var(--ink); padding: 14px 20px 14px 30px; }
.tk-whatif .sweep { position:absolute; inset:0; background: rgba(4,173,195,.14); border-radius: 14px; transform-origin: left center; }
.tk-whatif .bar { position:absolute; left:0; top:0; bottom:0; width:8px; background: var(--aqua); border-radius: 14px 0 0 14px; }
.tk-whatif .txt { position: relative; }
.chips { display:flex; flex-wrap: wrap; gap: 14px; }
.chip { display:flex; align-items:center; gap: 10px; font: 600 28px/1 "Poppins", sans-serif; color: var(--white); background: linear-gradient(135deg, var(--g-lite) 0%, var(--g-mid) 45%, var(--g-deep) 100%); border: 0; border-radius: 999px; padding: 15px 25px 15px 19px; box-shadow: 0 6px 16px rgba(23,51,49,.18); }
.chip svg { width: 28px; height: 28px; flex:none; }
.chip svg path { fill:none; stroke: var(--white); stroke-width: 5; stroke-linecap: round; stroke-linejoin: round; }
"""
    chips = "".join(f'<span class="chip"><svg viewBox="0 0 28 28"><path class="ck" d="M5 15 L11 21 L23 7"/></svg>{html.escape(x)}</span>' for x in c["outcome"])
    inner = f"""    <div class="tk-top"><span class="pill">{c['n']}/{c['of']}</span><span class="label">{html.escape(c['label'])}</span></div>
    <div class="col tk-col">
      <div class="h-display tk-h">{hl(c['headline'])}</div>
      <div class="tk-pain">{html.escape(c['pain'])}</div>
      <div class="stage"><canvas id="scene" width="912" height="420" data-scale="1.25"></canvas></div>
      <div class="tk-whatif"><div class="sweep" id="sweep"></div><div class="bar"></div><div class="txt">{html.escape(c['whatif'])}</div></div>
      <div class="chips" id="chips">{chips}</div>
    </div>"""
    js = """tl.fromTo("#sweep", { scaleX: 0 }, { scaleX: 1, duration: 0.6, ease: "power2.out" }, 1.4);
document.querySelectorAll(".ck").forEach((p, j) => { p.style.strokeDasharray = 30; tl.fromTo(p, { strokeDashoffset: 30 }, { strokeDashoffset: 0, duration: 0.3, ease: "power2.out" }, 2.6 + j * 0.2); });
"""
    return "light", css, inner, c.get("scene"), "scene", js, False

def reveal(c):
    css = """
.logo { position:absolute; left: var(--pad); top: 96px; width: 400px; z-index: 10; }
.logo img { width: 100%; display: block; }
.rv-col { top: 360px; gap: 30px; right: 84px; }
.rv-h { font-size: 62px; line-height: 1.2; color: var(--white); }
.rv-body { font: 400 33px/1.5 "Poppins", sans-serif; color: var(--body-light); }
.rv-line { font: 700 36px/1.4 "Poppins", sans-serif; color: var(--aqua); }
.rv-sign { font: 500 28px/1.4 "Poppins", sans-serif; color: #9A9A9A; max-width: 640px; }
#scene { position:absolute; inset:0; z-index: 20; }
"""
    inner = f"""    <div class="logo" id="logo"><img src="assets/brand/logo-on-dark.png" alt="A Realtime Tech logo" /></div>
    <div class="col rv-col">
      <div class="h-display rv-h">{hl(c['headline'])}</div>
      <div class="rv-body">{rich(c['body'])}</div>
      <div class="rv-line">{html.escape(c['line'])}</div>
      <div class="rv-sign">{html.escape(c['sign'])}</div>
    </div>
    <canvas id="scene" width="1080" height="1350"></canvas>"""
    js = """tl.fromTo("#logo", { opacity: 0, scale: 0.96 }, { opacity: 1, scale: 1, duration: 0.8, ease: "power2.out" }, 0);"""
    return "dark", css, inner, "reveal", "scene", js, True

def cta(c):
    css = """
.ct-col { top: 150px; gap: 44px; }
.ct-h { font-size: 96px; line-height: 1.15; color: var(--ink); }
.nums { display:grid; grid-template-columns: repeat(3, 1fr); gap: 22px; }
.num { position: relative; background: var(--white); border-radius: 22px; padding: 20px 22px; display:flex; align-items:center; gap: 16px; }
.num .ring { position:absolute; inset:-7px; border: 6px solid var(--ink); border-radius: 28px; opacity: 0; }
.num b { font-family: "Preahvihear", sans-serif; font-weight: 400; font-size: 54px; line-height: 1; color: var(--aqua); }
.num span { font: 600 24px/1.2 "Poppins", sans-serif; color: var(--ink); }
.ct-main { font: 700 40px/1.35 "Poppins", sans-serif; color: var(--ink); max-width: 560px; }
.ct-save { font: 500 30px/1.4 "Poppins", sans-serif; color: rgba(26,26,26,.8); display:flex; gap:14px; align-items:center; max-width: 560px; }
.card { position:absolute; right: 84px; bottom: 150px; width: 352px; height: 300px; background: var(--white); border-radius: 28px; z-index: 12; overflow: hidden; }
.card canvas { position:absolute; inset:0; width: 352px; height: 300px; }
"""
    nums = "".join(f'<div class="num"><div class="ring"></div><b>{i+1}</b><span>{html.escape(l)}</span></div>' for i, l in enumerate(c['chips']))
    inner = f"""    <div class="col ct-col">
      <div class="h-display ct-h">{hl(c['headline'])}</div>
      <div class="nums" id="nums">{nums}</div>
      <div class="ct-main">{html.escape(c['main'])}</div>
      <div class="ct-save"><svg id="mark" width="30" height="36" viewBox="0 0 30 36"><path d="M3 3h24v30l-12-8-12 8z" fill="#1A1A1A" stroke="#1A1A1A" stroke-width="3.5" stroke-linejoin="round"/></svg>{html.escape(c['save'])}</div>
    </div>
    <div class="card"><canvas id="scene" width="352" height="300"></canvas></div>"""
    js = """document.querySelectorAll("#nums .ring").forEach((r, j) => { tl.fromTo(r, { opacity: 0 }, { opacity: 1, duration: 0.08 }, (6 + 2 * j) / 8); tl.to(r, { opacity: 0, duration: 0.12 }, (7.6 + 2 * j) / 8); });
tl.fromTo("#mark", { y: -26 }, { y: 0, duration: 0.45, ease: "bounce.out" }, 2.8);"""
    return "aqua", css, inner, "cta", "scene", js, False

TEMPLATES = {"cover": cover, "task": task, "reveal": reveal, "cta": cta}

def main(project, only=None):
    project = pathlib.Path(project)
    content = json.loads((project / "content.json").read_text(encoding="utf-8"))
    js_lib = LIB + ("\n" + (project / "scenes.js").read_text(encoding="utf-8") if (project / "scenes.js").exists() else "")
    out = project / "slides"; out.mkdir(exist_ok=True)
    shutil.copytree(KIT, out / "assets", dirs_exist_ok=True)
    cover_png = project / "cover" / "cover-art.png"
    if cover_png.exists(): shutil.copyfile(cover_png, out / "assets" / "cover-art.png")
    elif any(s["template"] == "cover" for s in content["slides"]): print("WARNING: no cover/cover-art.png yet (run fit_cover.py)")
    n = len(content["slides"])
    for i, s in enumerate(content["slides"], 1):
        if only and i not in only: continue
        if s["template"] not in TEMPLATES: print("skip", i, s["template"], "(no such template)"); continue
        theme, css, inner, key, canvas_id, js, dark = TEMPLATES[s["template"]](s)
        sid = f"slide-{i:02d}"
        (out / f"{sid}.html").write_text(page(sid, theme, inner, css, key, canvas_id, js, i, n, content["handle"], dark, js_lib, s.get("opts", {})), encoding="utf-8")
        print("built", sid, s["template"], key)

if __name__ == "__main__":
    only = [int(x) for x in sys.argv[2].split(",")] if len(sys.argv) > 2 else None
    main(sys.argv[1], only)
~~~~
<!-- END FILE -->

---

### `scripts/sheets.py`

<!-- FILE: scripts/sheets.py code -->
~~~~python
"""Frame sheets: 9 moments of each slide's animation on one image, so staging and timing can be checked by eye.

Usage: python sheets.py <project_dir> [01,02,...]   (default: all slides)
Writes <project_dir>/proof/sheet-NN.png. Task slides are cropped to the stage card; other slides are shown whole.
Look for: the robot never behind/under a prop, props never clipped by the stage edge, every beat readable,
checks popping in, nothing overlapping the headline.
"""
import pathlib, sys
from playwright.sync_api import sync_playwright
from PIL import Image, ImageDraw

TIMES = [0.3, 0.8, 1.3, 1.7, 2.1, 2.5, 2.9, 3.3, 3.95]

def main(project, nums=None):
    project = pathlib.Path(project).resolve()
    files = sorted((project / "slides").glob("slide-*.html"))
    if nums: files = [f for f in files if f.stem.split("-")[1] in nums]
    out = project / "proof"; out.mkdir(exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1080, "height": 1350})
        for f in files:
            n = f.stem.split("-")[1]; errs = []
            pg.on("pageerror", lambda e, errs=errs: errs.append(str(e)))
            pg.goto(f.as_uri(), wait_until="load"); pg.wait_for_timeout(700)
            box = pg.evaluate("(()=>{const e=document.querySelector('.stage'); if(!e) return null; const r=e.getBoundingClientRect();"
                              " return [Math.round(r.left),Math.round(r.top),Math.round(r.right),Math.round(r.bottom)]})()")
            crops = []
            for t in TIMES:
                pg.evaluate(f"Object.values(window.__timelines).forEach(tl => tl.seek({t}, false)); 0")
                tmp = out / "_tmp.png"; pg.screenshot(path=str(tmp)); im = Image.open(tmp).convert("RGB")
                crops.append((t, im.crop(tuple(box)) if box else im.resize((540, 675))))
            W, H = crops[0][1].size
            sheet = Image.new("RGB", (W * 3 + 40, (H + 34) * 3), "white"); d = ImageDraw.Draw(sheet)
            for j, (t, c) in enumerate(crops):
                x = (j % 3) * (W + 20); y = (j // 3) * (H + 34); sheet.paste(c, (x, y + 26)); d.text((x + 6, y + 6), f"t={t}s", fill="black")
            sheet.save(out / f"sheet-{n}.png")
            print(f"sheet-{n}.png", "errors:", errs or "none")
        b.close()
    (out / "_tmp.png").unlink(missing_ok=True)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2].split(",") if len(sys.argv) > 2 else None)
~~~~
<!-- END FILE -->

---

### `scripts/stills.py`

<!-- FILE: scripts/stills.py code -->
~~~~python
"""Render the final frame of every slide as a PNG still and check the layout.

Usage: python stills.py <project_dir>
Writes <project_dir>/stills/slide-NN.png at exactly 1080x1350. Prints OK per slide, or the problem:
fonts not loaded, content running into the handle zone (below 1220px), or a wrong size.
Exit code 1 if any slide fails.
"""
import pathlib, sys
from playwright.sync_api import sync_playwright
from PIL import Image

def main(project):
    project = pathlib.Path(project).resolve()
    slides = sorted((project / "slides").glob("slide-*.html"))
    out = project / "stills"; out.mkdir(exist_ok=True)
    problems = []
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1080, "height": 1350})
        for f in slides:
            errs = []
            pg.on("pageerror", lambda e, errs=errs: errs.append(str(e)))
            pg.goto(f.as_uri(), wait_until="load"); pg.wait_for_timeout(800)
            # jump to the final frame with events ON so canvas scenes redraw (the still = the video's end state).
            # The trailing "; 0" matters: returning the GSAP timeline object to Playwright crashes the page.
            pg.evaluate("Object.values(window.__timelines || {}).forEach(t => t.progress(1, false)); 0")
            fonts_ok = pg.evaluate("document.fonts.check('40px Preahvihear') && document.fonts.check('600 40px Poppins')")
            bottom = pg.evaluate("Math.max(0, ...[...document.querySelectorAll('.col')].map(e => e.getBoundingClientRect().bottom))")
            png = out / (f.stem + ".png")
            pg.screenshot(path=str(png))
            w, h = Image.open(png).size
            status = []
            if errs: status.append("JS ERROR: " + errs[0][:120])
            if not fonts_ok: status.append("FONTS NOT LOADED")
            if bottom > 1220: status.append(f"content bottom {bottom:.0f}px runs into the handle zone")
            if (w, h) != (1080, 1350): status.append(f"size {w}x{h}")
            print(f.stem, f"{w}x{h}", f"content-bottom={bottom:.0f}", "OK" if not status else " | ".join(status))
            problems += status
        b.close()
    return 1 if problems else 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
~~~~
<!-- END FILE -->

---

### `scripts/render.py`

<!-- FILE: scripts/render.py code -->
~~~~python
"""Lint, render and verify the MP4 for every slide (HyperFrames + GSAP, 4s, 1080x1350, 30fps).

Usage: python render.py <project_dir> [01,02,...]
Needs: Node (npx), ffmpeg/ffprobe on PATH. HyperFrames is pinned to 0.8.55.
HyperFrames wants ONE root composition per folder, so each slide is copied in turn to <project>/render/index.html.
Prints per slide: lint errors, size, fps, duration, and how many headline pixels changed between 0.1s and 3.9s
(must be 0 on task slides: text never moves; the cover photo and the reveal logo animate, so those two will differ).
Output: <project>/render/out/slide-NN.mp4
"""
import json, pathlib, re, shutil, subprocess, sys
from PIL import Image, ImageChops

SKILL = pathlib.Path(__file__).resolve().parent.parent
HF = "npx --yes hyperframes@0.8.55"

def sh(cmd, cwd):
    return subprocess.run(cmd, cwd=cwd, shell=True, capture_output=True, text=True, encoding="utf-8", errors="replace")

def frame(mp4, t, png):
    sh(f'ffmpeg -v error -y -ss {t} -i "{mp4}" -frames:v 1 "{png}"', mp4.parent)
    return Image.open(png).convert("L")

def main(project, nums=None):
    project = pathlib.Path(project).resolve()
    r = project / "render"; (r / "out").mkdir(parents=True, exist_ok=True)
    for f in ["package.json", "hyperframes.json"]: shutil.copyfile(SKILL / "assets" / "render" / f, r / f)
    (r / "meta.json").write_text(json.dumps({"id": project.name, "name": project.name}), encoding="utf-8")
    shutil.rmtree(r / "assets", ignore_errors=True); shutil.copytree(project / "slides" / "assets", r / "assets")
    slides = sorted((project / "slides").glob("slide-*.html"))
    if nums: slides = [s for s in slides if s.stem.split("-")[1] in nums]
    bad = 0
    for s in slides:
        n = s.stem.split("-")[1]; shutil.copyfile(s, r / "index.html")
        lo = sh(f"{HF} lint", r); lint = lo.stdout + lo.stderr
        m = re.search(r"(\d+) error\(s\)", lint); errs = int(m.group(1)) if m else -1
        mp4 = r / "out" / f"slide-{n}.mp4"
        rr = sh(f'{HF} render --quality delivery --fps 30 --output "out/slide-{n}.mp4"', r)
        if not mp4.exists(): print(n, "RENDER FAILED:", (rr.stdout + rr.stderr)[-400:]); bad += 1; continue
        probe = sh(f'ffprobe -v error -show_entries stream=width,height,r_frame_rate:format=duration -of csv=p=0 "{mp4}"', r).stdout.split()
        is_task = 'class="stage"' in s.read_text(encoding="utf-8")
        a = frame(mp4, 0.1, r / "_a.png").crop((0, 0, 1080, 400)); b = frame(mp4, 3.9, r / "_b.png").crop((0, 0, 1080, 400))
        moved = ImageChops.difference(a, b).point(lambda v: 255 if v > 40 else 0).histogram()[255]
        ok = errs == 0 and probe[:2] == ["1080,1350,30/1", "4.000000"] and (moved == 0 or not is_task)
        bad += 0 if ok else 1
        print(n, f"lint={errs} errors", " ".join(probe), f"headline-px-moved={moved}", "OK" if ok else "CHECK")
    for t in ["_a.png", "_b.png"]: (r / t).unlink(missing_ok=True)
    return 1 if bad else 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2].split(",") if len(sys.argv) > 2 else None))
~~~~
<!-- END FILE -->

---

### `scripts/publish.py`

<!-- FILE: scripts/publish.py code -->
~~~~python
"""Copy finished deliverables to the post's deliverables folder (any folder the user chooses).

Usage: python publish.py <project_dir> <dest_dir> [--archive-as v5-something]
Copies render/out/*.mp4 -> dest/motion/, stills/*.png -> dest/stills/, content.json, cover/ (art, source.txt),
and writes dest/preview-all-slides.png (all stills in a row). If dest/motion already exists and --archive-as is
given, the old motion/ and stills/ are renamed to motion-<tag>/ and stills-<tag>/ first; without it they are replaced.
Never copies API keys or anything outside the project.
"""
import argparse, pathlib, shutil
from PIL import Image

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("project"); ap.add_argument("dest"); ap.add_argument("--archive-as", default="")
    a = ap.parse_args()
    p, d = pathlib.Path(a.project), pathlib.Path(a.dest); d.mkdir(parents=True, exist_ok=True)
    for sub in ["motion", "stills"]:
        if (d / sub).exists():
            if a.archive_as: (d / sub).rename(d / f"{sub}-{a.archive_as}")
            else: shutil.rmtree(d / sub)
        (d / sub).mkdir()
    mp4s = sorted((p / "render" / "out").glob("slide-*.mp4")); pngs = sorted((p / "stills").glob("slide-*.png"))
    for f in mp4s: shutil.copyfile(f, d / "motion" / f.name)
    for f in pngs: shutil.copyfile(f, d / "stills" / f.name)
    shutil.copyfile(p / "content.json", d / "content.json")
    if (p / "cover").exists():
        (d / "cover").mkdir(exist_ok=True)
        for f in (p / "cover").iterdir():
            if f.is_file(): shutil.copyfile(f, d / "cover" / f.name)
    if pngs:
        ims = [Image.open(f).resize((360, 450)) for f in pngs]
        sheet = Image.new("RGB", (370 * len(ims), 450), "white")
        for i, im in enumerate(ims): sheet.paste(im, (i * 370, 0))
        sheet.save(d / "preview-all-slides.png")
    print(f"published {len(mp4s)} MP4s, {len(pngs)} stills ->", d)
    for f in sorted(d.rglob("*")):
        if f.is_file() and f.parent.name in ("motion", "stills"): print("  ", f.relative_to(d))

if __name__ == "__main__":
    main()
~~~~
<!-- END FILE -->

---

### `scripts/make_single_file.py`

<!-- FILE: scripts/make_single_file.py code -->
~~~~python
"""Bundle this skill folder into ONE self-contained markdown file: ART-carousel-design.md.

Usage: python make_single_file.py [output_path]
The file = SKILL.md (instructions) + every reference, script and kit file as marked blocks + the logo in base64.
Fonts and GSAP are not embedded (they download with setup_assets.py). Re-run after editing anything in the folder.
Anyone can unpack the file back into this folder layout with the snippet printed in its "Unpack" section.
"""
import base64, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
TEXT = ["references/design-language.md", "references/scene-authoring.md", "references/free-cover.md", "references/copy-rules.md",
        "scripts/setup_assets.py", "scripts/new_project.py", "scripts/fit_cover.py", "scripts/build.py", "scripts/sheets.py",
        "scripts/stills.py", "scripts/render.py", "scripts/publish.py", "scripts/make_single_file.py",
        "assets/shared.css", "assets/kit/js/pixelbot.js", "assets/kit/js/props-vector.js", "assets/kit/js/scenes-library.js",
        "assets/render/package.json", "assets/render/hyperframes.json", "assets/example-content.json"]
BINARY = ["assets/kit/brand/logo-on-dark.png"]
FENCE = "~~~~"   # tilde fences never collide with backticks inside the code

UNPACK = r'''
## Unpack

Run this once with Python 3, in the folder where you saved this file. It rebuilds the full skill folder
(`ART-carousel-design/`) next to it, then run `python ART-carousel-design/scripts/setup_assets.py`.

~~~~python
import base64, pathlib, re
src = pathlib.Path("ART-carousel-design.md").read_text(encoding="utf-8")
out = pathlib.Path("ART-carousel-design")
out.mkdir(exist_ok=True)
(out / "SKILL.md").write_text(src.split("<!-- END SKILL -->")[0].rstrip() + "\n", encoding="utf-8")
for path, kind, body in re.findall(r"<!-- FILE: (\S+) (text|code|base64) -->\n(.*?)\n<!-- END FILE -->", src, re.S):
    f = out / path; f.parent.mkdir(parents=True, exist_ok=True)
    if kind == "code": body = body.split("\n", 1)[1].rsplit("\n", 1)[0]          # strip the ~~~~ fences
    if kind == "base64": f.write_bytes(base64.b64decode(re.sub(r"\s", "", body.split("\n", 1)[1].rsplit("\n", 1)[0])))
    else: f.write_text(body + "\n", encoding="utf-8")
    print("wrote", f)
~~~~
'''

def lang(p):
    return {".py": "python", ".js": "javascript", ".css": "css", ".json": "json"}.get(pathlib.Path(p).suffix, "")

def main(out):
    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8").rstrip()
    parts = [skill, "\n\n<!-- END SKILL -->\n\n# Appendix: every file in this skill\n",
             "This single file contains the whole skill. If your assistant can read it, it can follow the instructions above "
             "directly; the sections below are the reference documents and the code the instructions point to "
             "(`references/...`, `scripts/...`, `assets/...`).\n", UNPACK]
    for rel in TEXT:
        body = (ROOT / rel).read_text(encoding="utf-8").rstrip("\n")
        if rel.endswith(".md"):
            parts.append(f"\n---\n\n<!-- FILE: {rel} text -->\n{body}\n<!-- END FILE -->\n")
        else:
            parts.append(f"\n---\n\n### `{rel}`\n\n<!-- FILE: {rel} code -->\n{FENCE}{lang(rel)}\n{body}\n{FENCE}\n<!-- END FILE -->\n")
    for rel in BINARY:
        b64 = base64.b64encode((ROOT / rel).read_bytes()).decode()
        lines = "\n".join(b64[i:i + 100] for i in range(0, len(b64), 100))
        parts.append(f"\n---\n\n### `{rel}` (image, base64)\n\n<!-- FILE: {rel} base64 -->\n{FENCE}\n{lines}\n{FENCE}\n<!-- END FILE -->\n")
    pathlib.Path(out).write_text("".join(parts), encoding="utf-8")
    print("wrote", out, f"{pathlib.Path(out).stat().st_size / 1024:.0f} KB")

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else str(ROOT.parent / "ART-carousel-design.md"))
~~~~
<!-- END FILE -->

---

### `assets/shared.css`

<!-- FILE: assets/shared.css code -->
~~~~css
/* ART carousel house style (ART-carousel-design skill). Tokens come from the ART brand guidelines (2026). */
@font-face { font-family: "Preahvihear"; src: url("assets/fonts/Preahvihear-Regular.ttf"); font-weight: 400; }
@font-face { font-family: "Poppins"; src: url("assets/fonts/Poppins-Regular.ttf"); font-weight: 400; }
@font-face { font-family: "Poppins"; src: url("assets/fonts/Poppins-Medium.ttf"); font-weight: 500; }
@font-face { font-family: "Poppins"; src: url("assets/fonts/Poppins-SemiBold.ttf"); font-weight: 600; }
@font-face { font-family: "Poppins"; src: url("assets/fonts/Poppins-Bold.ttf"); font-weight: 700; }

:root {
  --aqua: #04ADC3;      /* primary */
  --ink: #1A1A1A;       /* secondary */
  --white: #FFFFFF;
  --body-dark: #3D3D3D; /* body text on white */
  --body-light: #CFCFCF;/* body text on ink */
  --aqua-tint: rgba(4, 173, 195, 0.12);
  --pad: 84px;
}
* { margin: 0; padding: 0; box-sizing: border-box; }
html, body { width: 1080px; height: 1350px; overflow: hidden; background: var(--ink); }
.slide { position: absolute; inset: 0; width: 1080px; height: 1350px; overflow: hidden; }
.slide.light { background: var(--white); color: var(--ink); }
.slide.dark  { background: var(--ink); color: var(--white); }
.slide.aqua  { background: var(--aqua); color: var(--ink); }

.h-display { font-family: "Preahvihear", sans-serif; font-weight: 400; letter-spacing: -0.01em; }
.p { font-family: "Poppins", sans-serif; }

/* handle, bottom-left on every slide */
.handle { position: absolute; left: var(--pad); bottom: 64px; font: 500 26px/1 "Poppins", sans-serif; letter-spacing: 0.02em; z-index: 30; }
.light .handle { color: #8A8A8A; } .dark .handle { color: #8A8A8A; } .aqua .handle { color: rgba(26,26,26,0.7); }

/* swipe hint, bottom-right */
.swipe { position: absolute; right: var(--pad); bottom: 56px; font: 600 26px/1 "Poppins", sans-serif; color: var(--aqua); z-index: 30; display: flex; align-items: center; gap: 12px; }
.swipe .arr { display: inline-block; }


/* content column */
.col { position: absolute; left: var(--pad); right: var(--pad); z-index: 10; display: flex; flex-direction: column; }
~~~~
<!-- END FILE -->

---

### `assets/kit/js/pixelbot.js`

<!-- FILE: assets/kit/js/pixelbot.js code -->
~~~~javascript
// ART pixel robot, canvas engine (frame-by-frame poses). Aiotrix kit only.
// Grid 24x24 art pixels. drawBot(ctx, x, y, u, pose): (x,y) = top-left of grid, u = px per art pixel.
// Poses step at 8/s (S = floor(t*8)); travel snaps to 4px. Deterministic: no random, no clocks.
const C8 = { A: "#04ADC3", W: "#FFFFFF", K: "#1A1A1A", S: "#9BE3EC", R: "#F27A7A", Y: "#FFD166", G: "#D9D9D9", D: "#5A5A5A" };
const snap = v => Math.round(v / 4) * 4;

function _pts(list, color) { return list.map(([x, y, w = 1, h = 1]) => [x, y, w, h, color]); }

function botParts(p) {
  const L = p.dark ? C8.W : C8.K;
  const out = [];
  const add = (list, c) => out.push(..._pts(list, c));
  // antenna
  add([[11, 2, 1, 2]], L);
  if (!p.bulbOff) add([[10, 0, 3, 2]], p.bulb === "red" ? C8.R : p.bulb === "yellow" ? C8.Y : C8.A);
  // head
  add([[5, 4, 13, 1], [4, 5, 15, 1], [4, 6, 2, 6], [17, 6, 2, 6], [4, 12, 15, 1], [5, 13, 13, 1]], C8.A);
  add([[3, 7, 1, 4], [19, 7, 1, 4]], C8.A); // ears
  add([[6, 6, 11, 6]], C8.W);                 // face screen
  // body
  add([[6, 14, 11, 6]], C8.A);
  add([[9, 16, 5, 3]], C8.W);
  add([[10, 17]], p.light2 ? C8.Y : C8.A); add([[12, 17]], C8.S);
  // legs
  const legs = {
    stand: [[8, 20, 2, 2], [13, 20, 2, 2], [7, 22, 3, 1], [13, 22, 3, 1]],
    stepL: [[8, 20, 2, 1], [7, 21, 3, 1], [13, 20, 2, 2], [13, 22, 3, 1]],
    stepR: [[8, 20, 2, 2], [7, 22, 3, 1], [13, 20, 2, 1], [13, 21, 3, 1]],
    tuck:  [[8, 20, 2, 1], [13, 20, 2, 1], [7, 21, 3, 1], [13, 21, 3, 1]],
  }[p.legs || "stand"];
  add(legs, L);
  // arms (A)
  const AL = {
    down: [[5, 15], [5, 16], [4, 17], [4, 18]],
    up:   [[5, 15], [4, 15], [4, 14], [3, 13], [3, 12], [3, 11]],
    flex: [[5, 15], [4, 15], [3, 14], [3, 13], [4, 12], [5, 12]],
    out:  [[5, 15], [4, 15], [3, 15], [2, 15]],
  }[p.armL || "down"];
  const AR = {
    down:  [[17, 15], [17, 16], [18, 17], [18, 18]],
    up:    [[17, 15], [18, 15], [18, 14], [19, 13], [19, 12], [19, 11]],
    wave1: [[17, 15], [18, 15], [19, 14], [20, 13], [21, 12]],
    wave2: [[17, 15], [18, 15], [18, 14], [18, 13], [18, 12]],
    flex:  [[17, 15], [18, 15], [19, 14], [19, 13], [18, 12], [17, 12]],
    reach: [[17, 15], [18, 15], [19, 15], [20, 15], [21, 15]],
    hold:  [[17, 15], [17, 16], [18, 16]],
    tap:   [[17, 15], [18, 16], [19, 17], [20, 18]],
  }[p.armR || "down"];
  add(AL, C8.A); add(AR, C8.A);
  // eyes
  const EY = {
    open:  [[[8, 7, 2, 2], [13, 7, 2, 2]], C8.K, [[8, 7], [13, 7]]],
    lookL: [[[7, 7, 2, 2], [12, 7, 2, 2]], C8.K, [[7, 7], [12, 7]]],
    lookR: [[[9, 7, 2, 2], [14, 7, 2, 2]], C8.K, [[9, 7], [14, 7]]],
    blink: [[[8, 8, 2, 1], [13, 8, 2, 1]], C8.K, []],
    happy: [[[7, 8], [8, 7, 2, 1], [10, 8], [12, 8], [13, 7, 2, 1], [15, 8]], C8.K, []],
    wide:  [[[8, 6, 2, 3], [13, 6, 2, 3]], C8.K, [[8, 6], [13, 6]]],
    squint:[[[7, 8, 4, 1], [13, 7, 2, 2]], C8.K, []],
    focus: [[[7, 8, 3, 1], [13, 8, 3, 1]], C8.K, []],
  }[p.eyes || "open"];
  add(EY[0], EY[1]); add(EY[2], C8.W);
  const MO = {
    smile: [[9, 10], [10, 11, 3, 1], [13, 10]],
    grin:  [[9, 10, 5, 1], [10, 11, 3, 1]],
    wobble:[[8, 11], [9, 10, 2, 1], [11, 11, 2, 1], [13, 10, 2, 1]],
    o:     [[10, 10, 3, 2]],
    flat:  [[9, 10, 5, 1]],
    open:  [[10, 10, 3, 2]],
  }[p.mouth || "smile"];
  add(MO, C8.K);
  return out;
}

function drawBot(ctx, x, y, u, p = {}) {
  x = snap(x); y = snap(y);
  const parts = botParts(p);
  const flip = !!p.flip;
  const put = (gx, gy, w, h, c, dx = 0, dy = 0) => {
    const X = flip ? (24 - gx - w) : gx;
    ctx.fillStyle = c; ctx.fillRect(x + X * u + dx, y + gy * u + dy, w * u, h * u);
  };
  if (p.halo) {                                   // cream/white halo on dark scenes
    const h = 4;
    for (const [dx, dy] of [[-h, 0], [h, 0], [0, -h], [0, h], [-h, -h], [h, h], [-h, h], [h, -h]])
      for (const [gx, gy, w, hh] of parts) put(gx, gy, w, hh, p.haloColor || "#FFFFFF", dx, dy);
  }
  for (const [gx, gy, w, h, c] of parts) put(gx, gy, w, h, c);
}

// soft flat shadow under feet
function botShadow(ctx, cx, feetY, w, dark) {
  ctx.fillStyle = dark ? "rgba(0,0,0,.35)" : "rgba(26,26,26,.12)";
  ctx.fillRect(snap(cx - w / 2), snap(feetY), snap(w), 8);
}

// ---- generic pixel helpers for props (u = art pixel size) ----
function pxr(ctx, x, y, w, h, c) { ctx.fillStyle = c; ctx.fillRect(snap(x), snap(y), w, h); }
function blitRows(ctx, rows, x, y, u, pal) {
  rows.forEach((r, j) => [...r].forEach((ch, i) => { if (ch !== ".") { ctx.fillStyle = pal[ch] || ch; ctx.fillRect(snap(x) + i * u, snap(y) + j * u, u, u); } }));
}
const SPR = {
  q:    [".KKK.", "K...K", "....K", "...K.", "..K..", ".....", "..K.."],
  bang: ["R", "R", "R", ".", "R"],
  check:["....A", "...A.", "A.A..", ".A..."],
  phone:["KKKKK", "KAAAK", "KAAAK", "KAAAK", "KAAAK", "KKWKK"],
  ringL:["K.", ".K", "K."],
  paper:["KKKKKK", "KWWWWK", "KWGGWK", "KWWWWK", "KWGGWK", "KWWWWK", "KKKKKK"],
  bubble:["AAAAAAA", "AWWWWWA", "AAAAAAA", ".AA...."],
  mug:  ["KKKK.", "KKKKK", "KKKK.", "KKKK."],
  steam:[".S", "S.", ".S"],
  lens: [".KKK.", "KSSSK", "KSSSK", "KSSSK", ".KKK.", "....K", ".....K"],
  box:  ["AAAAA", "ASSSA", "AAAAA", "ASSSA", "AAAAA"],
  plane:["A....", "AAA..", "AAAAA", "AAA..", "A...."],
  shop: ["AWAWAWAWA", "AWAWAWAWA", ".KKKKKKK.", ".KWWKWWK.", ".KWWKWWK.", ".KKKKAAK.", ".KWWKAAK.", ".KKKKKKK."],
  kbd:  ["KKKKKKKKK", "KWKWKWKWK", "KKKKKKKKK"],
  flag: ["RRR.", "RRRR", "RRR.", "K...", "K...", "K..."],
  slip: ["KKKKK", "KWWWK", "KWAWK", "KWWWK", "KWAWK", "KKKKK"],
  stamp:["..AAA..", ".AAAAA.", "AAAAAWA", "AAAAWAA", "AWAWAAA", ".AAWAA.", "..AAA.."],
  bell: ["..K..", ".YYY.", ".YYY.", "YYYYY", "..K.."],
  arrow:["..AAA", "...AA", "..A.A", ".A...", "A...."],
  tray: ["K.........K", "K.........K", "KKKKKKKKKKK"],
  big:  ["YYYYYY", "YWWWWY", "YWKKWY", "YWWWWY", "YWKKWY", "YWWWWY", "YWKKWY", "YYYYYY"],
  small:["KKKK", "KWWK", "KWAK", "KKKK"],
  heart:[".R.R.", "RRRRR", "RRRRR", ".RRR.", "..R.."],
  poof: ["S.S", ".S.", "S.S"],
  gear: ["..A.A..", ".AAAAA.", "AAA.AAA", ".A...A.", "AAA.AAA", ".AAAAA.", "..A.A.."],
};
const PAL = { K: C8.K, A: C8.A, W: C8.W, S: C8.S, R: C8.R, G: C8.G, Y: C8.Y };
~~~~
<!-- END FILE -->

---

### `assets/kit/js/props-vector.js`

<!-- FILE: assets/kit/js/props-vector.js code -->
~~~~javascript
// ART smooth vector props (Aiotrix kit). RULE: only the robot mascot is pixel art; every other element is
// smooth, anti-aliased flat vector, and moves on continuous time t with easing (the robot steps at 8 poses/s).
// GL/GM/GD = accent teal-green (light -> mid -> deep). ONLY for result chips, lit shop windows and check marks
const VC = { GL: "#41A486", GM: "#2B907F", GD: "#1C5E55", A: "#04ADC3", K: "#1A1A1A", W: "#FFFFFF", T: "#DDF3F7", S: "#9BE3EC", R: "#F27A7A", Y: "#FFD166", G: "#D9D9D9", D: "#5A5A5A" };
const clamp01 = k => Math.max(0, Math.min(1, k));
const eOut = k => 1 - Math.pow(1 - clamp01(k), 3);
const eInOut = k => { k = clamp01(k); return k < .5 ? 4 * k * k * k : 1 - Math.pow(-2 * k + 2, 3) / 2; };
const eBack = k => { k = clamp01(k); const c1 = 1.70158, c3 = c1 + 1; return 1 + c3 * Math.pow(k - 1, 3) + c1 * Math.pow(k - 1, 2); };
const rr = (ctx, x, y, w, h, r) => { ctx.beginPath(); ctx.roundRect(x, y, w, h, r); };
const fs = (ctx, fill, stroke, lw) => { if (fill) { ctx.fillStyle = fill; ctx.fill(); } if (stroke) { ctx.strokeStyle = stroke; ctx.lineWidth = lw || 3; ctx.lineJoin = "round"; ctx.stroke(); } };

// soft ellipse shadow under the robot's feet (shrinks while it hops)
function vShadow(ctx, cx, y, w, lift = 0, dark = false) {
  const s = 1 - Math.min(0.5, lift / 80);
  ctx.save(); ctx.globalAlpha = dark ? 0.35 : 0.13; ctx.fillStyle = VC.K;
  ctx.beginPath(); ctx.ellipse(cx, y, (w / 2) * s, 7 * s, 0, 0, Math.PI * 2); ctx.fill(); ctx.restore();
}

// desk: rounded ink top + soft aqua front panel with drawer handles
function vDesk(ctx, x0, x1, top, h = 44) {
  rr(ctx, x0 + 10, top + 8, x1 - x0 - 20, h, [0, 0, 12, 12]); fs(ctx, VC.T);
  ctx.fillStyle = "rgba(4,173,195,.35)";
  for (const dx of [0.22, 0.5, 0.78]) { rr(ctx, x0 + (x1 - x0) * dx - 22, top + 24, 44, 6, 3); ctx.fill(); }
  rr(ctx, x0, top, x1 - x0, 14, 7); fs(ctx, VC.K);
}

// Material "call" handset glyph (Apache 2.0), 24x24 box
const HANDSET = new Path2D("M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z");
function tick(ctx, cx, cy, s, color, lw, k = 1) {   // self-drawing check mark, k = 0..1
  const P = [[-0.5, 0.05], [-0.15, 0.4], [0.55, -0.4]].map(([a, b]) => [cx + a * s, cy + b * s]);
  const L1 = Math.hypot(P[1][0] - P[0][0], P[1][1] - P[0][1]), L2 = Math.hypot(P[2][0] - P[1][0], P[2][1] - P[1][1]);
  let d = clamp01(k) * (L1 + L2);
  ctx.save(); ctx.strokeStyle = color; ctx.lineWidth = lw; ctx.lineCap = "round"; ctx.lineJoin = "round"; ctx.beginPath(); ctx.moveTo(...P[0]);
  if (d <= L1) ctx.lineTo(P[0][0] + (P[1][0] - P[0][0]) * d / L1, P[0][1] + (P[1][1] - P[0][1]) * d / L1);
  else { ctx.lineTo(...P[1]); d -= L1; ctx.lineTo(P[1][0] + (P[2][0] - P[1][0]) * d / L2, P[1][1] + (P[2][1] - P[1][1]) * d / L2); }
  ctx.stroke(); ctx.restore();
}

// smartphone standing on the desk. ring = buzzing with an incoming call; else quiet with a check on the screen.
function vPhone(ctx, cx, bottom, t, ring, quietK = 1, icon = "call") {
  const w = 38, h = 62, ang = ring ? Math.sin(t * 52) * 0.1 : 0;
  ctx.save(); ctx.translate(cx, bottom); ctx.rotate(ang);
  rr(ctx, -w / 2, -h, w, h, 9); fs(ctx, VC.K);
  rr(ctx, -w / 2 + 4, -h + 7, w - 8, h - 16, 5); fs(ctx, ring ? VC.A : VC.T);
  rr(ctx, -6, -6, 12, 3, 1.5); fs(ctx, "#5A5A5A");
  if (ring) {
    const p = 1 + Math.sin(t * 18) * 0.08;
    if (icon === "bell") { ctx.save(); ctx.translate(0, -h / 2 - 2); ctx.scale(p, p); bellPath(ctx); fs(ctx, VC.W); ctx.beginPath(); ctx.arc(0, 11, 3, 0, 7); fs(ctx, VC.W); ctx.restore(); }
    else { ctx.save(); ctx.translate(0, -h / 2 - 2); ctx.scale(p, p); ctx.translate(-12, -12); ctx.fillStyle = VC.W; ctx.fill(HANDSET); ctx.restore(); }
  } else tick(ctx, 0, -h / 2 - 2, 18, VC.GM, 4, quietK);
  ctx.restore();
}

// expanding ring waves either side of a ringing phone
function vRings(ctx, cx, cy, t) {
  ctx.save(); ctx.lineCap = "round"; ctx.strokeStyle = VC.A; ctx.lineWidth = 3.5;
  for (let j = 0; j < 2; j++) {
    const ph = (t * 2.4 + j * 0.5) % 1, r = 26 + ph * 22;
    ctx.globalAlpha = (1 - ph) * 0.9;
    ctx.beginPath(); ctx.arc(cx, cy, r, -0.55, 0.55); ctx.stroke();
    ctx.beginPath(); ctx.arc(cx, cy, r, Math.PI - 0.55, Math.PI + 0.55); ctx.stroke();
  }
  ctx.restore();
}

// little impact burst where the robot's hand taps (k = 0..1)
function vTapBurst(ctx, x, y, k) {
  if (k <= 0 || k >= 1) return;
  ctx.save(); ctx.strokeStyle = VC.K; ctx.lineWidth = 3; ctx.lineCap = "round"; ctx.globalAlpha = 1 - k;
  for (const a of [-2.3, -1.57, -0.85]) {
    const r0 = 8 + k * 8, r1 = 16 + k * 10;
    ctx.beginPath(); ctx.moveTo(x + Math.cos(a) * r0, y + Math.sin(a) * r0); ctx.lineTo(x + Math.cos(a) * r1, y + Math.sin(a) * r1); ctx.stroke();
  }
  ctx.restore();
}

// client storefront: striped scalloped awning, window, door. lit = update received (warm window), bump = 0..1 squash on arrival
function vShop(ctx, cx, top, lit, bump = 1) {
  const w = 96, x = -w / 2, sq = bump < 1 ? 1 - Math.sin(clamp01(bump) * Math.PI) * 0.07 : 1;
  ctx.save(); ctx.translate(cx, top + 76); ctx.scale(1 / sq, sq); ctx.translate(0, -76);
  rr(ctx, x + 6, 18, w - 12, 58, [0, 0, 6, 6]); fs(ctx, VC.W, VC.K, 3);
  let win = VC.T;
  if (lit) { win = ctx.createLinearGradient(0, 36, 0, 62); win.addColorStop(0, VC.GL); win.addColorStop(1, VC.GD);
    ctx.save(); ctx.shadowColor = "rgba(65,164,134,.85)"; ctx.shadowBlur = 16; rr(ctx, x + 16, 36, 36, 26, 4); fs(ctx, win); ctx.restore(); }
  rr(ctx, x + 16, 36, 36, 26, 4); fs(ctx, win, VC.K, 2.5);
  ctx.strokeStyle = VC.K; ctx.lineWidth = 2; ctx.beginPath(); ctx.moveTo(x + 34, 36); ctx.lineTo(x + 34, 62); ctx.stroke();
  rr(ctx, x + 60, 38, 22, 38, [5, 5, 0, 0]); fs(ctx, VC.K);
  ctx.fillStyle = VC.Y; ctx.beginPath(); ctx.arc(x + 76, 58, 2, 0, 7); ctx.fill();
  // awning
  const n = 6, sw = w / n;
  for (let i = 0; i < n; i++) {
    const c = i % 2 ? VC.W : VC.A, sx = x + i * sw;
    ctx.beginPath(); ctx.moveTo(sx, 4); ctx.lineTo(sx + sw, 4); ctx.lineTo(sx + sw, 18); ctx.arc(sx + sw / 2, 18, sw / 2, 0, Math.PI); ctx.closePath(); fs(ctx, c);
  }
  ctx.beginPath(); ctx.moveTo(x, 18); ctx.lineTo(x, 4); ctx.quadraticCurveTo(x, 0, x + 4, 0); ctx.lineTo(x + w - 4, 0); ctx.quadraticCurveTo(x + w, 0, x + w, 4); ctx.lineTo(x + w, 18);
  for (let i = n - 1; i >= 0; i--) ctx.arc(x + i * sw + sw / 2, 18, sw / 2, 0, Math.PI);
  ctx.closePath(); fs(ctx, null, VC.K, 3);
  ctx.restore();
}

// paper plane pointing along angle ang, scale s
function vPlane(ctx, x, y, ang, s = 1, alpha = 1) {
  ctx.save(); ctx.globalAlpha = alpha; ctx.translate(x, y); ctx.rotate(ang); ctx.scale(s, s);
  ctx.beginPath(); ctx.moveTo(16, 0); ctx.lineTo(-14, -12); ctx.lineTo(-6, 0); ctx.closePath(); fs(ctx, VC.W, VC.K, 2.5);
  ctx.beginPath(); ctx.moveTo(16, 0); ctx.lineTo(-6, 0); ctx.lineTo(-14, 11); ctx.closePath(); fs(ctx, VC.A, VC.K, 2.5);
  ctx.restore();
}
// quadratic bezier point + tangent
const qb = (p0, p1, p2, k) => [(1 - k) * (1 - k) * p0[0] + 2 * (1 - k) * k * p1[0] + k * k * p2[0], (1 - k) * (1 - k) * p0[1] + 2 * (1 - k) * k * p1[1] + k * k * p2[1]];
const qbAng = (p0, p1, p2, k) => Math.atan2(2 * (1 - k) * (p1[1] - p0[1]) + 2 * k * (p2[1] - p1[1]), 2 * (1 - k) * (p1[0] - p0[0]) + 2 * k * (p2[0] - p1[0]));
// a plane flying p0 -> p2 along a curve with a dashed trail behind it; k = 0..1 (already eased by caller)
function vFlight(ctx, p0, p1, p2, k) {
  if (k <= 0 || k >= 1) return;
  ctx.save(); ctx.setLineDash([6, 8]); ctx.lineCap = "round"; ctx.strokeStyle = VC.A; ctx.lineWidth = 3; ctx.globalAlpha = 0.55;
  ctx.beginPath(); ctx.moveTo(...p0);
  for (let j = 1; j <= 24; j++) ctx.lineTo(...qb(p0, p1, p2, (k * j) / 24));
  ctx.stroke(); ctx.restore();
  const [x, y] = qb(p0, p1, p2, k), s = k > 0.8 ? 1 - (k - 0.8) / 0.2 * 0.6 : 1;
  vPlane(ctx, x, y, qbAng(p0, p1, p2, k), s);
}

// aqua check badge that pops in with overshoot (k = 0..1 over the pop)
function vBadge(ctx, cx, cy, k, r = 15) {
  if (k <= 0) return;
  const s = eBack(k);
  ctx.save(); ctx.translate(cx, cy); ctx.scale(s, s);
  const g = ctx.createLinearGradient(-r, -r, r, r); g.addColorStop(0, VC.GL); g.addColorStop(1, VC.GD);
  ctx.beginPath(); ctx.arc(0, 0, r, 0, Math.PI * 2); fs(ctx, g, VC.W, 3);
  tick(ctx, 0, 0, r * 1.05, VC.W, 3.5, clamp01(k * 1.6 - 0.4));
  ctx.restore();
}

// sweat drops flicking off the robot's head (stress)
function vSweat(ctx, x, y, t, dir = 1) {
  for (let j = 0; j < 2; j++) {
    const ph = (t * 1.8 + j * 0.5) % 1;
    const dx = dir * (6 + ph * 26), dy = -18 * Math.sin(ph * Math.PI) + ph * 22;
    ctx.save(); ctx.globalAlpha = 1 - ph * ph; ctx.translate(x + dx, y + dy); ctx.rotate(dir * 0.5);
    ctx.beginPath(); ctx.moveTo(0, -9); ctx.bezierCurveTo(6, -2, 7, 4, 0, 7); ctx.bezierCurveTo(-7, 4, -6, -2, 0, -9); fs(ctx, VC.S, VC.A, 2);
    ctx.restore();
  }
}

// mug with the handle on the left (towards the robot's hand) + soft wavy steam; t = time since it appeared
function vMug(ctx, x, bottom, t) {
  const w = 32, h = 34, top = bottom - h, k = eBack(t / 0.3);
  ctx.save(); ctx.translate(x + w / 2, bottom); ctx.scale(k, k); ctx.translate(-x - w / 2, -bottom);
  ctx.save(); ctx.strokeStyle = VC.K; ctx.lineWidth = 4; ctx.beginPath(); ctx.arc(x, top + 15, 9, Math.PI * 0.5, Math.PI * 1.5); ctx.stroke(); ctx.restore();
  rr(ctx, x, top, w, h, [3, 3, 9, 9]); fs(ctx, VC.W, VC.K, 3);
  rr(ctx, x + 1.5, top + 12, w - 3, 8, 0); fs(ctx, VC.A);
  ctx.restore();
  ctx.save(); ctx.strokeStyle = "rgba(90,90,90,.55)"; ctx.lineWidth = 3; ctx.lineCap = "round";
  for (let j = 0; j < 3; j++) {
    const ph = (t * 0.8 + j / 3) % 1; ctx.globalAlpha = Math.sin(ph * Math.PI) * clamp01(t / 0.3);
    const sx = x + 6 + j * 10, sy = top - 4 - ph * 14;
    ctx.beginPath();
    for (let q = 0; q <= 14; q++) { const yy = sy - q * 2, xx = sx + Math.sin(q * 0.55 + t * 5 + j * 2) * 3; q ? ctx.lineTo(xx, yy) : ctx.moveTo(xx, yy); }
    ctx.stroke();
  }
  ctx.restore();
}

// gear (for the trail seams). evenodd hole.
function vGear(ctx, cx, cy, r, color, rot = 0, teeth = 8) {
  const ri = r * 0.74, N = teeth * 4;
  ctx.save(); ctx.translate(cx, cy); ctx.rotate(rot); ctx.beginPath();
  for (let j = 0; j <= N; j++) { const a = (j / N) * Math.PI * 2, rad = (j % 4 < 2) ? r : ri; j ? ctx.lineTo(Math.cos(a) * rad, Math.sin(a) * rad) : ctx.moveTo(Math.cos(a) * rad, Math.sin(a) * rad); }
  ctx.closePath(); ctx.moveTo(r * 0.32, 0); ctx.arc(0, 0, r * 0.32, 0, Math.PI * 2, true);
  ctx.fillStyle = color; ctx.fill("evenodd"); ctx.restore();
}

// ---- props for the other scenes ----
const _ink = (ctx, font, color) => { ctx.font = font; ctx.fillStyle = color; ctx.textAlign = "center"; ctx.textBaseline = "middle"; };

// speech mark over the robot: "?" (white) or "!" (red); pops in with overshoot. s = size factor
function vMark(ctx, cx, cy, ch, k, kind = "q", s = 1) {
  if (k <= 0) return;
  const bg = kind === "bang" ? VC.R : VC.W, fg = kind === "bang" ? VC.W : VC.K, z = eBack(k) * s;
  ctx.save(); ctx.translate(cx, cy); ctx.scale(z, z);
  ctx.beginPath(); ctx.moveTo(-7, 16); ctx.lineTo(-4, 32); ctx.lineTo(8, 17); ctx.closePath(); fs(ctx, bg, VC.K, 3);
  ctx.beginPath(); ctx.arc(0, 0, 22, 0, Math.PI * 2); fs(ctx, bg, VC.K, 3);
  ctx.beginPath(); ctx.moveTo(-6, 16); ctx.lineTo(-3, 28); ctx.lineTo(7, 17); ctx.closePath(); fs(ctx, bg);
  _ink(ctx, "700 28px Poppins, sans-serif", fg); ctx.fillText(ch, 0, 2);
  ctx.restore();
}

// document with a folded corner, coloured header (optional label) and grey text lines
function vPaper(ctx, x, y, w, h, o = {}) {
  const f = 12;
  ctx.save(); ctx.globalAlpha = o.alpha == null ? 1 : o.alpha; ctx.translate(x + w / 2, y + h / 2); ctx.rotate(o.rot || 0); ctx.translate(-w / 2, -h / 2);
  ctx.beginPath(); ctx.moveTo(5, 0); ctx.lineTo(w - f, 0); ctx.lineTo(w, f); ctx.lineTo(w, h - 5); ctx.quadraticCurveTo(w, h, w - 5, h);
  ctx.lineTo(5, h); ctx.quadraticCurveTo(0, h, 0, h - 5); ctx.lineTo(0, 5); ctx.quadraticCurveTo(0, 0, 5, 0); ctx.closePath(); fs(ctx, VC.W, VC.K, 3);
  ctx.beginPath(); ctx.moveTo(w - f, 0); ctx.lineTo(w - f, f); ctx.lineTo(w, f); ctx.closePath(); fs(ctx, VC.T, VC.K, 2.5);
  let ly = 12;
  if (o.head) { rr(ctx, 7, 8, w - f - 11, 13, 3); fs(ctx, o.head); if (o.label) { _ink(ctx, "700 9px Poppins, sans-serif", VC.W); ctx.fillText(o.label, 7 + (w - f - 11) / 2, 15); } ly = 28; }
  ctx.fillStyle = VC.G;
  for (let j = 0; ly + j * 9 < h - 8; j++) { rr(ctx, 7, ly + j * 9, (w - 14) * (j % 2 ? 0.6 : 0.85), 4, 2); ctx.fill(); }
  ctx.restore();
}

// keyboard seen from the side: slab with a row of key caps; one cap lights up per keystroke while typing
function vKeyboard(ctx, x, y, w, t, typing) {
  const n = Math.floor((w - 8) / 12), lit = typing ? Math.floor(t * 14) % n : -1;
  for (let j = 0; j < n; j++) { rr(ctx, x + 5 + j * 12, y - (j === lit ? 2 : 5), 9, 7, 2); fs(ctx, j === lit ? VC.A : VC.W, VC.K, 2); }
  rr(ctx, x, y, w, 12, 5); fs(ctx, VC.K);
}

// red flag on a pole that springs up (k 0..1) and waves
function vFlag(ctx, x, bottom, t, k) {
  if (k <= 0) return;
  const s = eBack(k);
  ctx.save(); ctx.translate(x, bottom); ctx.scale(1, s);
  ctx.strokeStyle = VC.K; ctx.lineWidth = 3.5; ctx.lineCap = "round"; ctx.beginPath(); ctx.moveTo(0, 0); ctx.lineTo(0, -48); ctx.stroke();
  ctx.beginPath(); ctx.moveTo(0, -48);
  for (let q = 0; q <= 8; q++) ctx.lineTo(q * 3.5, -48 + Math.sin(q * 0.8 - t * 9) * 2.5);
  for (let q = 8; q >= 0; q--) ctx.lineTo(q * 3.5, -30 + Math.sin(q * 0.8 - t * 9) * 2.5);
  ctx.closePath(); fs(ctx, VC.R, VC.K, 2.5);
  ctx.restore();
}

// vertical scan beam with a soft glow
function vBeam(ctx, x, y0, y1) {
  const g = ctx.createLinearGradient(x - 18, 0, x + 18, 0);
  g.addColorStop(0, "rgba(4,173,195,0)"); g.addColorStop(0.5, "rgba(4,173,195,.45)"); g.addColorStop(1, "rgba(4,173,195,0)");
  ctx.fillStyle = g; ctx.fillRect(x - 18, y0, 36, y1 - y0);
  rr(ctx, x - 1.5, y0, 3, y1 - y0, 1.5); fs(ctx, VC.A);
}

// shelf unit: light back panel, ink posts and boards
function vShelf(ctx, x0, x1, top, boards) {
  const bottom = boards[boards.length - 1];
  rr(ctx, x0, top, x1 - x0, bottom - top, 6); fs(ctx, "#E4F6F9");
  rr(ctx, x0, top - 4, x1 - x0, 8, 4); fs(ctx, VC.K);
  for (const b of boards) { rr(ctx, x0, b, x1 - x0, 8, 4); fs(ctx, VC.K); }
  rr(ctx, x0, top - 4, 8, bottom - top + 12, 4); fs(ctx, VC.K); rr(ctx, x1 - 8, top - 4, 8, bottom - top + 12, 4); fs(ctx, VC.K);
}

// carton box with tape stripe; scales from its bottom centre
function vBox(ctx, x, y, w, h, alpha = 1, scale = 1) {
  if (scale <= 0 || alpha <= 0) return;
  ctx.save(); ctx.globalAlpha = alpha; ctx.translate(x + w / 2, y + h); ctx.scale(scale, scale); ctx.translate(-w / 2, -h);
  rr(ctx, 0, 0, w, h, 5); fs(ctx, VC.A, VC.K, 2.5);
  rr(ctx, 1.5, 1.5, w - 3, 10, [4, 4, 0, 0]); fs(ctx, "#36C2D4");
  ctx.strokeStyle = VC.K; ctx.lineWidth = 2; ctx.beginPath(); ctx.moveTo(1.5, 12); ctx.lineTo(w - 1.5, 12); ctx.stroke();
  rr(ctx, w / 2 - 5, 1.5, 10, h - 3, 0); fs(ctx, VC.S);
  ctx.restore();
}

// puff of smoke (k 0..1)
function vPoof(ctx, cx, cy, k) {
  if (k <= 0 || k >= 1) return;
  ctx.save(); ctx.globalAlpha = (1 - k) * 0.9; ctx.fillStyle = VC.S;
  for (let j = 0; j < 6; j++) { const a = j / 6 * Math.PI * 2, d = 6 + k * 18; ctx.beginPath(); ctx.arc(cx + Math.cos(a) * d, cy + Math.sin(a) * d * 0.7, 8 + k * 5, 0, 7); ctx.fill(); }
  ctx.restore();
}

// slip of paper (reorder / purchase). big = yellow purchase slip
function vSlip(ctx, x, y, w, h, o = {}) {
  ctx.save(); ctx.globalAlpha = o.alpha == null ? 1 : o.alpha;
  rr(ctx, x, y, w, h, 5); fs(ctx, o.big ? VC.Y : VC.W, VC.K, 2.5);
  if (o.big) { _ink(ctx, "700 17px Poppins, sans-serif", VC.K); ctx.fillText("₹₹₹", x + w / 2, y + h / 2 + 1); }
  else { ctx.fillStyle = o.line || VC.A; for (let j = 0; j < 3 && 7 + j * 8 < h - 6; j++) { rr(ctx, x + 6, y + 7 + j * 8, (w - 12) * (j === 1 ? 0.6 : 1), 4, 2); ctx.fill(); } }
  ctx.restore();
}

// teal approval mark (ring + check) left by the stamp
function vStampMark(ctx, cx, cy, k) {
  if (k <= 0) return;
  ctx.save(); ctx.globalAlpha = clamp01(k * 3); ctx.strokeStyle = VC.GM; ctx.lineWidth = 3; ctx.beginPath(); ctx.arc(cx, cy, 13, 0, 7); ctx.stroke(); ctx.restore();
  tick(ctx, cx, cy, 15, VC.GM, 3.5, clamp01(k * 1.5));
}

// rubber stamp: knob, neck, aqua base; bottom edge at y
function vStamp(ctx, cx, y) {
  ctx.beginPath(); ctx.arc(cx, y - 40, 9, 0, 7); fs(ctx, VC.K);
  rr(ctx, cx - 5, y - 34, 10, 16, 3); fs(ctx, VC.K);
  rr(ctx, cx - 22, y - 20, 44, 12, 4); fs(ctx, VC.A, VC.K, 2.5);
  rr(ctx, cx - 18, y - 8, 36, 8, [0, 0, 3, 3]); fs(ctx, VC.D);
}

// magnifying glass held from (hx,hy)
function vLens(ctx, cx, cy, r, hx, hy) {
  ctx.save(); ctx.strokeStyle = VC.K; ctx.lineWidth = 7; ctx.lineCap = "round";
  const a = Math.atan2(hy - cy, hx - cx); ctx.beginPath(); ctx.moveTo(hx, hy); ctx.lineTo(cx + Math.cos(a) * r, cy + Math.sin(a) * r); ctx.stroke(); ctx.restore();
  ctx.beginPath(); ctx.arc(cx, cy, r, 0, 7); fs(ctx, "rgba(155,227,236,.38)", VC.K, 4);
  ctx.save(); ctx.strokeStyle = "rgba(255,255,255,.95)"; ctx.lineWidth = 3; ctx.lineCap = "round"; ctx.beginPath(); ctx.arc(cx, cy, r - 6, -2.6, -1.7); ctx.stroke(); ctx.restore();
}

// dotted curve p0 -> p2 drawn up to k (links, follow-up arrows); arrow head optional
function vCurve(ctx, p0, p1, p2, k, color, o = {}) {
  if (k <= 0) return;
  ctx.save(); ctx.strokeStyle = color; ctx.lineWidth = o.lw || 3.5; ctx.lineCap = "round"; ctx.setLineDash(o.dash || [2, 9]);
  ctx.beginPath(); ctx.moveTo(...p0); const kk = clamp01(k);
  for (let j = 1; j <= 30; j++) ctx.lineTo(...qb(p0, p1, p2, (kk * j) / 30));
  ctx.stroke(); ctx.setLineDash([]);
  if (o.arrow && kk > 0.95) { const [x, y] = p2, a = qbAng(p0, p1, p2, 1); ctx.translate(x, y); ctx.rotate(a);
    ctx.beginPath(); ctx.moveTo(-10, -7); ctx.lineTo(0, 0); ctx.lineTo(-10, 7); ctx.stroke(); }
  ctx.restore();
}

// chat bubble with a tail and three typing dots; (x,y) top-left, s = scale
function vBubble(ctx, x, y, s, color, t, seed = 0, alpha = 1) {
  ctx.save(); ctx.globalAlpha = alpha; ctx.translate(x, y); ctx.scale(s, s);
  ctx.beginPath(); ctx.moveTo(10, 30); ctx.lineTo(6, 44); ctx.lineTo(22, 32); ctx.closePath(); fs(ctx, color, VC.K, 2.5);
  rr(ctx, 0, 0, 64, 36, 14); fs(ctx, color, VC.K, 2.5);
  ctx.beginPath(); ctx.moveTo(11, 29); ctx.lineTo(8, 40); ctx.lineTo(21, 30); ctx.closePath(); fs(ctx, color);
  ctx.fillStyle = color === VC.Y ? VC.K : VC.W;
  for (let j = 0; j < 3; j++) { ctx.beginPath(); ctx.arc(19 + j * 13, 18 + Math.sin(t * 10 + j * 0.9 + seed) * 2.5, 4, 0, 7); ctx.fill(); }
  ctx.restore();
}

// inbox tray: back drawn first, then contents, then front lip
function vTrayBack(ctx, x, y, w, h) { rr(ctx, x + 6, y - 16, w - 12, h + 16, 6); fs(ctx, "#E4F6F9", VC.K, 2.5); }
function vTrayFront(ctx, x, y, w, h) {
  ctx.beginPath(); ctx.moveTo(x, y); ctx.lineTo(x + w, y); ctx.lineTo(x + w - 8, y + h); ctx.lineTo(x + 8, y + h); ctx.closePath(); fs(ctx, VC.W, VC.K, 3);
  rr(ctx, x + w / 2 - 14, y + 8, 28, 5, 2.5); fs(ctx, VC.A);
}

// conveyor belt: top rail with moving marks, body, rollers that turn
function vBelt(ctx, x0, x1, y, h, off) {
  rr(ctx, x0, y + 8, x1 - x0, h - 8, 0); fs(ctx, VC.T);
  ctx.save(); ctx.beginPath(); ctx.rect(x0, y, x1 - x0, 10); ctx.clip();
  rr(ctx, x0 - 10, y, x1 - x0 + 20, 10, 5); fs(ctx, VC.K);
  ctx.fillStyle = VC.D; for (let bx = x0 - 32 + (off % 32); bx < x1; bx += 32) { rr(ctx, bx, y + 3, 14, 4, 2); ctx.fill(); }
  ctx.restore();
  for (let rx = x0 + 24; rx < x1; rx += 64) {
    ctx.beginPath(); ctx.arc(rx, y + h / 2 + 5, 9, 0, 7); fs(ctx, VC.W, VC.K, 2.5);
    const a = off / 9; ctx.save(); ctx.strokeStyle = VC.K; ctx.lineWidth = 2; ctx.beginPath(); ctx.moveTo(rx, y + h / 2 + 5); ctx.lineTo(rx + Math.cos(a) * 7, y + h / 2 + 5 + Math.sin(a) * 7); ctx.stroke(); ctx.restore();
  }
}

// gate: two posts, top bar and a signal light (colour) with glow
function vGate(ctx, x, w, top, bottom, light) {
  rr(ctx, x, top, 8, bottom - top, 4); fs(ctx, VC.K); rr(ctx, x + w - 8, top, 8, bottom - top, 4); fs(ctx, VC.K);
  rr(ctx, x - 4, top - 4, w + 8, 10, 5); fs(ctx, VC.K);
  ctx.save(); if (light !== VC.G) { ctx.shadowColor = light; ctx.shadowBlur = 18; }
  ctx.beginPath(); ctx.arc(x + w / 2, top - 18, 12, 0, 7); fs(ctx, light, VC.K, 3); ctx.restore();
}

// bell shape (centred, ~24 wide); swings by ang around its top
function bellPath(ctx) {
  ctx.beginPath(); ctx.moveTo(-12, 8); ctx.quadraticCurveTo(-10, 4, -10, -2); ctx.bezierCurveTo(-10, -13, 10, -13, 10, -2); ctx.quadraticCurveTo(10, 4, 12, 8); ctx.closePath();
}
function vBell(ctx, cx, cy, ang, ringing, t, s = 1.4) {
  ctx.save(); ctx.translate(cx, cy - 14 * s); ctx.rotate(ang); ctx.translate(0, 14 * s); ctx.scale(s, s);
  ctx.beginPath(); ctx.arc(0, 12, 3.5, 0, 7); fs(ctx, VC.K);
  bellPath(ctx); fs(ctx, VC.Y, VC.K, 2.5 / s);
  ctx.beginPath(); ctx.arc(0, -13, 2.5, 0, 7); fs(ctx, VC.K);
  ctx.restore();
  if (ringing) { ctx.save(); ctx.strokeStyle = VC.K; ctx.lineWidth = 2.5; ctx.lineCap = "round"; ctx.globalAlpha = 0.5 + 0.5 * Math.sin(t * 20);
    for (const d of [-1, 1]) { ctx.beginPath(); ctx.arc(cx, cy, 26 * s / 1.4, d < 0 ? Math.PI - 0.5 : -0.5, d < 0 ? Math.PI + 0.5 : 0.5); ctx.stroke(); }
    ctx.restore(); }
}

// heart
function vHeart(ctx, cx, cy, s) {
  if (s <= 0) return;
  ctx.save(); ctx.translate(cx, cy); ctx.scale(s, s);
  ctx.beginPath(); ctx.moveTo(0, 14); ctx.bezierCurveTo(-26, -2, -14, -24, 0, -10); ctx.bezierCurveTo(14, -24, 26, -2, 0, 14); ctx.closePath(); fs(ctx, VC.R, VC.K, 3 / s);
  ctx.restore();
}
~~~~
<!-- END FILE -->

---

### `assets/kit/js/scenes-library.js`

<!-- FILE: assets/kit/js/scenes-library.js code -->
~~~~javascript
// ART carousel scene LIBRARY (art-carousel skill). cover / reveal / cta are generic; the task scenes
// (calls, docs, stock, bills, chats, approvals) come from the "6 things" post and double as worked examples.
// A post adds its own scenes in <project>/scenes.js (Object.assign(SCENES_DYN, {...})).
// Per-slide options from content.json "opts" arrive as the global SCENE_OPTS.
// Each scene(ctx, t, S, W, H) redraws one frame.
// ONLY the robot is pixel art (pixelbot.js, posed by S = 8 steps/s). Every prop is smooth vector (props-vector.js) moving on t.
// S = pose step (0..31 over 4s). Deterministic: same t -> same frame.
// STAGE scenes (task slides) are drawn on a virtual 728x336 stage that the page scales by exactly 1.25
// (912x420 on screen). Keep every size/position a multiple of 4 so pixels stay crisp after scaling.
const lerp = (a, b, k) => a + (b - a) * Math.max(0, Math.min(1, k));
const walkLegs = S => (S % 2 ? "stepL" : "stepR");
const VF = 316, VY = VF - 23 * 8;            // stage floor (feet) and robot top for u=8

const SCENES_DYN = {

  // COVER (full frame): robot walks in along the desk, spots the paper pile, "?" -> "!", then rolls up its sleeves.
  cover(ctx, t, S, W, H) {
    // u = 10 matches task slides (8 x 1.25 stage scale). opts: x = where the robot stops (must sit on a clear patch of the
    // cover image), feet = y of its feet, from = x it walks in from (off the right edge).
    const o = (typeof SCENE_OPTS !== "undefined" && SCENE_OPTS) || {}, X = o.x ?? 812, FROM = o.from ?? 1100;
    const u = 10, FEET = o.feet ?? 1172, Y = FEET - 23 * u;
    let x = X, legs = "stand", armL = "down", armR = "down", eyes = "lookL", mouth = "o", bulb = "aqua";
    if (S < 10) { x = lerp(FROM, X, S / 9); legs = walkLegs(S); eyes = "open"; mouth = "smile"; }
    else if (S < 14) { eyes = "lookL"; mouth = "o"; }
    else if (S < 18) { eyes = "wide"; mouth = "open"; bulb = "red"; }
    else if (S < 24) { armL = S % 2 ? "flex" : "up"; armR = S % 2 ? "flex" : "up"; eyes = "focus"; mouth = "grin"; bulb = "yellow"; }
    else { armL = "flex"; armR = "flex"; eyes = S === 29 ? "blink" : "happy"; mouth = "grin"; bulb = "aqua"; }
    const hop = (S >= 24 && S <= 25) ? -20 : 0;
    vShadow(ctx, x + 120, FEET + 8, 190, -hop, true);
    drawBot(ctx, x, Y + hop, u, { legs, armL, armR, eyes, mouth, bulb, dark: true, halo: true, flip: FROM > X });   // faces the way it walks
    if (S >= 10 && S < 14) vMark(ctx, x + 120, Y - 44, "?", (t - 10 / 8) / 0.2, "q", 1.2);
    if (S >= 14 && S < 18) vMark(ctx, x + 120, Y - 44, "!", (t - 14 / 8) / 0.2, "bang", 1.2);
  },

  // 1 CLIENT UPDATES (vector props, pixel robot only): phones buzz on the desk; the robot hops from phone to phone and
  // taps each quiet; a paper plane carries the update up to that client's shop, whose window lights up with a check.
  calls(ctx, t, S) {
    // robot stands in the gap left of each phone (arms x+24..x+168; tapping hand tip = phone's left edge), never overlapping one
    const cxs = [300, 484, 668], Q = [8, 15, 22], stops = [112, 296, 480], FLY = 0.6, TOP = 292;
    const land = Q.map(q => q / 8 + FLY);
    cxs.forEach((cx, i) => vShop(ctx, cx, 6, t >= land[i], (t - land[i]) / 0.3));
    let x, legs = "stand", armR = "down", eyes = "wide", mouth = "wobble", hopY = 0;
    if (S < 6) { x = lerp(-140, stops[0], S / 6); legs = walkLegs(S); }
    else if (S >= 25) { x = stops[2]; armR = "hold"; eyes = S === 30 ? "blink" : "happy"; mouth = "smile"; }
    else {
      const i = Math.min(2, Math.floor((S - 6) / 7)), r = S - 6 - 7 * i;
      if (r < 3) { x = stops[i]; armR = r === 0 ? "reach" : "tap"; eyes = "focus"; mouth = "flat"; }
      else if (i === 2) { x = stops[2]; eyes = "happy"; mouth = "grin"; legs = r === 3 ? "tuck" : "stand"; hopY = r === 3 ? -24 : 0; }   // little victory hop
      else { const h = r - 3; x = lerp(stops[i], stops[i + 1], h / 3); legs = "tuck"; hopY = [-24, -40, -24, 0][h]; }
    }
    x = snap(x);
    vShadow(ctx, x + 96, VF + 4, 120, -hopY);
    drawBot(ctx, x, VY + hopY, 8, { legs, armR, eyes, mouth, bulb: S < 22 ? "red" : "aqua", bulbOff: S < 22 && S % 2 === 0 });
    if (S < 22) vSweat(ctx, x + 160, VY + 48 + hopY, t, 1);
    vDesk(ctx, 264, 724, TOP);
    if (S >= 25) vMug(ctx, x + 116, TOP, t - 25 / 8);
    cxs.forEach((cx, i) => {
      const q = Q[i] / 8, ring = t < q;
      vPhone(ctx, cx, TOP, t, ring, (t - q) / 0.25);
      if (ring) vRings(ctx, cx, TOP - 34, t);
      vTapBurst(ctx, cx - 22, TOP - 14, (t - (q - 0.2)) / 0.35);
      vFlight(ctx, [cx, TOP - 66], [Math.min(cx + 64, 708), 170], [cx + 4, 78], eInOut((t - q) / FLY));
      vBadge(ctx, cx + 40, 10, (t - land[i]) / 0.35);
    });
  },

  // 2 RETYPING DOCUMENTS: papers tumble onto the desk while the robot types frantically; a beam scans them once,
  // they merge into one clean document with a check, and a red flag springs up on the one mismatch.
  docs(ctx, t, S) {
    const x = 220, TOP = 284, P = [492, 572, 652], PW = 52, PH = 64, PY = TOP - PH;
    let armR = "down", eyes = "wide", mouth = "wobble", bulb = "red", bulbOff = S % 2 === 0;
    if (S < 9) { armR = S % 2 ? "tap" : "reach"; }
    else if (S < 17) { armR = "reach"; eyes = "focus"; mouth = "flat"; bulbOff = false; bulb = "yellow"; }
    else if (S < 22) { eyes = "open"; mouth = "o"; bulb = "aqua"; bulbOff = false; }
    else { armR = S % 2 ? "wave1" : "wave2"; eyes = S === 30 ? "blink" : "happy"; mouth = "grin"; bulb = "aqua"; bulbOff = false; }
    drawBot(ctx, x, VY, 8, { armR, eyes, mouth, bulb, bulbOff });
    if (S < 9) vSweat(ctx, x + 160, VY + 48, t, 1);
    vDesk(ctx, 260, 724, TOP);
    vKeyboard(ctx, 388, TOP - 12, 92, t, S < 9);
    const scanX = 484 + (712 - 484) * clamp01((t - 9 / 8) / 1.0), m = eInOut((t - 17 / 8) / 0.5);
    [0, 2, 1].forEach(i => {
      const px0 = P[i], land = (2 + 2 * i) / 8, k = (t - (land - 0.25)) / 0.25;
      if (k <= 0) return;
      let px = px0, py = PY, rot = 0, alpha = 1;
      if (k < 1) { py = lerp(-90, PY, k * k); rot = (1 - k) * (i === 1 ? 0.5 : -0.6); }
      else if (t - land < 0.16) py = PY - Math.sin((t - land) / 0.16 * Math.PI) * 6;
      if (m > 0) { px = lerp(px0, 572, m); if (i !== 1) alpha = 1 - m; }
      if (alpha <= 0) return;
      vPaper(ctx, px, py, PW, PH, { rot, alpha, head: i === 1 ? VC.A : VC.D });
      const scanned = t > 9 / 8 && scanX > px0 + PW / 2;
      if (!scanned && t >= land) vMark(ctx, px0 + PW - 4, PY - 6, "?", (t - land) / 0.2, "bang", 0.5);
    });
    if (t >= 9 / 8 && t < 17 / 8) vBeam(ctx, scanX, PY - 18, TOP);
    vFlag(ctx, 584, PY + 22, t, (t - 22 / 8) / 0.3);
    vBadge(ctx, 572 + PW - 2, PY + 2, (t - 21 / 8) / 0.35);
  },

  // 3 STOCK: boxes vanish from the shelf one by one; the robot's bulb flashes, it holds up a reorder slip,
  // an approval stamp thumps down on it (teal check), and new boxes drop into the gaps.
  stock(ctx, t, S) {
    vShelf(ctx, 400, 712, 112, [204, 296]);
    const BW = 52, BH = 44, slots = [];
    for (const by of [160, 252]) for (let c = 0; c < 4; c++) slots.push([418 + c * 72, by]);
    const goneAt = { 4: 0.25, 6: 0.5, 1: 0.75, 7: 1.0 }, backAt = { 4: 2.5, 6: 2.75, 1: 3.0, 7: 3.25 };
    slots.forEach(([bx, by], k) => {
      const g = goneAt[k];
      if (g === undefined || t < g) { vBox(ctx, bx, by, BW, BH); return; }
      const b = backAt[k];
      if (t < b) { vBox(ctx, bx, by, BW, BH, 1, 1 - eOut((t - g) / 0.15)); vPoof(ctx, bx + BW / 2, by + BH / 2, (t - g) / 0.4); }
      if (t >= b - 0.2) { const q = clamp01((t - (b - 0.2)) / 0.2); vBox(ctx, bx, lerp(by - 36, by, q * q), BW, BH, clamp01(q * 2)); }
    });
    let x, legs = "stand", armR = "down", eyes = "open", mouth = "smile", bulb = "aqua", bulbOff = false;
    if (S < 6) { x = lerp(-60, 160, S / 6); legs = walkLegs(S); eyes = "lookR"; }
    else if (S < 10) { x = 160; eyes = "wide"; mouth = "o"; bulb = "red"; bulbOff = S % 2 === 0; }
    else if (S < 20) { x = 160; armR = "up"; eyes = "focus"; mouth = "flat"; bulb = "yellow"; }
    else if (S < 28) { x = 160; armR = "up"; eyes = "happy"; mouth = "grin"; }
    else { x = 160; armR = S % 2 ? "wave1" : "wave2"; eyes = S === 30 ? "blink" : "happy"; mouth = "grin"; }
    x = snap(x);
    vShadow(ctx, x + 96, VF + 4, 120);
    drawBot(ctx, x, VY, 8, { legs, armR, eyes, mouth, bulb, bulbOff });
    if (S >= 6 && S < 10) vMark(ctx, x + 96, VY - 40, "!", (t - 6 / 8) / 0.2, "bang");
    if (t >= 1.25 && t < 3.6) {                          // reorder slip held up by the raised hand
      const a = Math.min(clamp01((t - 1.25) / 0.12), clamp01((3.6 - t) / 0.12));
      vSlip(ctx, 324, 160, 44, 56, { alpha: a });
      vStampMark(ctx, 346, 196, (t - 2.125) / 0.3);
      let sy = null;                                     // stamp: drops, thumps, lifts away
      if (t >= 1.875 && t < 2.125) { const q = (t - 1.875) / 0.25; sy = lerp(-10, 200, q * q); }
      else if (t >= 2.125 && t < 2.275) sy = 200;
      else if (t >= 2.275 && t < 2.55) sy = lerp(200, -10, eOut((t - 2.275) / 0.275));
      if (sy !== null) vStamp(ctx, 346, sy);
    }
  },

  // 4 MATCHING BILLS: detective robot hops from document to document with a magnifier (standing in the gap left of each);
  // PO and delivery note link up in aqua with checks, the invoice links in red and gets flagged.
  bills(ctx, t, S) {
    const cxs = [296, 480, 664], stops = [112, 296, 480], TOP = 292, DW = 44, DH = 60, DY = TOP - DH;   // doc right edge < next stop's left arm
    let x, legs = "stand", eyes = "squint", mouth = "smile", armR = "reach", hopY = 0, bulb = "aqua";
    if (S < 6) { x = lerp(-140, stops[0], S / 6); legs = walkLegs(S); eyes = "open"; }
    else if (S < 12) { x = stops[0]; eyes = S % 3 === 0 ? "lookR" : "squint"; }
    else if (S < 15) { x = lerp(stops[0], stops[1], (S - 11) / 3); legs = "tuck"; hopY = [-20, -28, 0][S - 12]; }
    else if (S < 18) { x = stops[1]; }
    else if (S < 21) { x = lerp(stops[1], stops[2], (S - 17) / 3); legs = "tuck"; hopY = [-20, -28, 0][S - 18]; }
    else if (S < 25) { x = stops[2]; if (S >= 22) { eyes = "wide"; mouth = "o"; bulb = "red"; } }
    else { x = stops[2]; eyes = S === 30 ? "blink" : "happy"; mouth = "grin"; armR = S % 2 ? "wave1" : "wave2"; }
    x = snap(x);
    // links arc high above the robot's head, drawn behind everything
    vCurve(ctx, [cxs[0], DY - 4], [(cxs[0] + cxs[1]) / 2, -20], [cxs[1], DY - 4], (t - 15 / 8) / 0.25, VC.A);
    vCurve(ctx, [cxs[1], DY - 4], [(cxs[1] + cxs[2]) / 2, -20], [cxs[2], DY - 4], (t - 22 / 8) / 0.3, VC.R);
    vShadow(ctx, x + 96, VF + 4, 120, -hopY);
    drawBot(ctx, x, VY + hopY, 8, { legs, eyes, mouth, armR, bulb });
    vDesk(ctx, 256, 724, TOP);
    [[VC.A, "PO"], [VC.D, "DN"], [VC.K, "INV"]].forEach(([head, label], i) => vPaper(ctx, cxs[i] - DW / 2, DY, DW, DH, { head, label }));
    vBadge(ctx, cxs[0] + 22, DY + 4, (t - 17 / 8) / 0.35);
    vBadge(ctx, cxs[1] + 22, DY + 4, (t - 17 / 8 - 0.08) / 0.35);
    vMark(ctx, cxs[2] + 22, DY - 18, "!", (t - 24 / 8) / 0.2, "bang", 0.7);
    if (armR === "reach") vLens(ctx, x + 194 + Math.sin(t * 9) * 5, VY + hopY + 106 + Math.cos(t * 7) * 3, 17, x + 172, VY + hopY + 124);
  },

  // 5 CHASING VENDORS: chat bubbles chase the robot across the stage; it sets down a tray, the bubbles file in neatly,
  // a follow-up flies out, the reply lands on the stack, check. Ends with tea.
  chats(ctx, t, S) {
    let x, flip = false, legs = "stand", armR = "down", eyes = "wide", mouth = "wobble", bulb = "red";
    if (S < 13) { x = lerp(420, 40, S / 12); flip = true; legs = walkLegs(S); }
    else if (S < 19) { x = 40; eyes = "focus"; mouth = "flat"; bulb = "yellow"; armR = "reach"; }
    else if (S < 25) { x = 40; eyes = "open"; mouth = "smile"; bulb = "aqua"; armR = S < 21 ? "tap" : "down"; }
    else { x = 40; armR = "hold"; eyes = S === 29 ? "blink" : "happy"; mouth = "smile"; bulb = "aqua"; }
    x = snap(x);
    const T = { x: 276, y: 292, w: 96, h: 24 }, tFile = 13 / 8;
    const xcAt = tt => lerp(420, 40, clamp01(tt * 8 / 12));
    vShadow(ctx, x + 96, VF + 4, 120);
    drawBot(ctx, x, VY, 8, { legs, armR, eyes, mouth, bulb, flip });
    if (S < 13) vSweat(ctx, x + 160, VY + 48, t, 1);
    if (S >= 25) vMug(ctx, x + 150, VY + 146, t - 25 / 8);
    const trayIn = clamp01((t - tFile + 0.15) / 0.15);
    if (trayIn > 0) { ctx.save(); ctx.globalAlpha = trayIn; vTrayBack(ctx, T.x, T.y, T.w, T.h); ctx.restore(); }
    for (let j = 0; j < 6; j++) {
      const tb = (1 + 2 * j) / 8; if (t < tb) continue;
      const col = j % 2 ? VC.S : VC.A;
      const chase = tt => [lerp(760, xcAt(tt) + 190 + (j % 3) * 64 + Math.floor(j / 3) * 96, eOut((tt - tb) / 0.5)), 20 + (j % 3) * 62 + Math.floor(j / 3) * 30 + Math.sin(tt * 8 + j) * 6];
      if (t < tFile) { const [bx, by] = chase(t); vBubble(ctx, bx, by, 1, col, t, j); continue; }
      const k = eInOut((t - tFile - j * 0.06) / 0.4), [x0, y0] = chase(tFile);
      vBubble(ctx, lerp(x0, T.x + 10 + (j % 2) * 40, k), lerp(y0, T.y - 22 - Math.floor(j / 2) * 12, k), lerp(1, 0.6, k), col, t, j);
    }
    const kr = eInOut((t - 22 / 8) / 0.45);
    if (kr > 0) vBubble(ctx, lerp(700, T.x + 26, kr), lerp(24, T.y - 58, kr), lerp(1, 0.6, kr), VC.Y, t, 9);
    if (trayIn > 0) { ctx.save(); ctx.globalAlpha = trayIn; vTrayFront(ctx, T.x, T.y, T.w, T.h); ctx.restore(); }
    vFlight(ctx, [340, 250], [560, 260], [716, 44], eInOut((t - 19 / 8) / 0.5));
    vBadge(ctx, T.x + T.w + 18, T.y - 34, (t - 26 / 8) / 0.35);
  },

  // 6 SMALL APPROVALS: the robot runs a booth beside a conveyor gate; small slips roll through and get a check,
  // the big one stops, a bell rings and a ping goes to your phone; you approve and it rolls on.
  approvals(ctx, t, S) {
    const RX = 200, RY = VY - 24, gate = 440, GW = 64, BT = 300, stopA = 2.5, stopB = 3.25;
    const travel = tt => 256 * Math.min(tt, stopA) + 320 * Math.max(0, tt - stopB);
    const stopped = t >= stopA && t < stopB, off = travel(t);
    let armR = "down", eyes = "open", mouth = "smile", bulb = "aqua";
    if (S >= 20 && S < 26) { armR = "reach"; eyes = "wide"; mouth = "o"; bulb = "yellow"; }
    else if (S >= 27) { armR = "hold"; eyes = S === 30 ? "blink" : "happy"; mouth = "smile"; }
    else if (S % 4 < 2) { armR = "wave1"; }
    drawBot(ctx, RX, RY, 8, { armR, eyes, mouth, bulb });
    rr(ctx, RX + 24, RY + 160, 160, BT - RY - 160, [8, 8, 0, 0]); fs(ctx, VC.T, VC.K, 3);      // booth front (hides legs)
    rr(ctx, RX + 18, RY + 156, 172, 9, 4.5); fs(ctx, VC.K);
    if (S >= 27) vMug(ctx, RX + 152, RY + 156, t - 27 / 8);
    const small = [200, 60, -80].map(x0 => x0 + off), big = -276 + off;
    const passing = small.some(px => px > gate - 32 && px < gate + GW);
    vGate(ctx, gate, GW, 156, BT, stopped ? VC.R : passing ? VC.A : VC.G);
    vBelt(ctx, 0, 728, BT, 36, off);
    small.forEach(px => { vSlip(ctx, px, BT - 28, 32, 28); if (px > gate + GW) vBadge(ctx, px + 16, BT - 46, (px - gate - GW) / 60, 12); });
    vSlip(ctx, big, BT - 32, 76, 32, { big: true });
    if (t >= stopB && big > gate + GW) vBadge(ctx, big + 38, BT - 50, (big - gate - GW) / 60);
    if (t >= stopA) {
      if (stopped) {
        vBell(ctx, 556, 100, Math.sin(t * 22) * 0.35, true, t);
        vCurve(ctx, [586, 80], [612, 40], [640, 64], (t - stopA - 0.12) / 0.25, VC.A, { arrow: true, dash: [6, 7], lw: 3 });
        vMark(ctx, 702, 26, "!", (t - stopA - 0.3) / 0.2, "bang", 0.55);
      }
      vPhone(ctx, 676, 104, t, stopped, (t - stopB) / 0.25, "bell");
    }
  },

  // REVEAL (full frame, dark): robot walks in, looks up at the logo, hops, waves with a heart.
  reveal(ctx, t, S) {
    const u = 10, FEET = 1196, Y = FEET - 23 * u;   // u = 10 matches task slides
    let x = 788, legs = "stand", armR = "down", eyes = "open", mouth = "smile";
    if (S < 9) { x = lerp(1100, 788, S / 8); legs = walkLegs(S); }
    else if (S < 13) { eyes = "lookL"; mouth = "o"; }
    else if (S < 15) { legs = "tuck"; eyes = "happy"; mouth = "grin"; }
    else if (S < 25) { armR = S % 2 ? "wave1" : "wave2"; eyes = "happy"; mouth = "grin"; }
    else { armR = "wave2"; eyes = S === 29 ? "blink" : "happy"; mouth = "grin"; }
    const hop = (S === 13 || S === 14) ? -28 : 0;
    vShadow(ctx, x + 120, FEET + 8, 190, -hop, true);
    drawBot(ctx, x, Y + hop, u, { legs, armR, eyes, mouth, dark: true, halo: true, flip: true });
    vHeart(ctx, x + 120, Y - 44 + Math.sin(t * 6) * 6, eBack((t - 2) / 0.3) * 1.5);
  },

  // CTA (white card on aqua): robot pops up, points left at the chips as they light up one by one, then grins.
  cta(ctx, t, S) {
    const u = 10, FEET = 272, Y = FEET - 23 * u, x = 56;   // u = 10 matches task slides; centred in the card
    let armR = "reach", eyes = "lookL", mouth = "grin", legs = "stand";
    const y = S < 4 ? lerp(320, Y, S / 3) : (S === 4 ? Y - 20 : Y);
    if (S < 5) { armR = "up"; legs = "tuck"; eyes = "happy"; }
    else if (S >= 20) { armR = S % 2 ? "wave1" : "wave2"; eyes = S === 28 ? "blink" : "happy"; }
    else if (S % 2) armR = "tap";
    vShadow(ctx, x + 120, FEET + 6, 150, FEET - 230 - y);
    drawBot(ctx, x, y, u, { legs, armR, eyes, mouth, flip: true });
  },
};

// bottom trail (smooth vector): dotted aqua line across the full width, solid up to this slide's progress,
// half-gears on the seams so the swipe joins up, and a tiny pixel robot head (the mascot) as the marker.
function drawTrail(ctx, W, i, n, k, dark, aqua) {
  const y = 22, dot = aqua ? "rgba(26,26,26,.35)" : dark ? "rgba(4,173,195,.55)" : "rgba(4,173,195,.45)", main = aqua ? VC.K : VC.A;
  ctx.fillStyle = dot;
  for (let x = 12; x < W; x += 24) { ctx.beginPath(); ctx.arc(x, y, 4, 0, Math.PI * 2); ctx.fill(); }
  const end = lerp((i - 1) / n, i / n, k) * W;
  ctx.save(); ctx.strokeStyle = main; ctx.lineWidth = 8; ctx.lineCap = "round";
  ctx.beginPath(); ctx.moveTo(-8, y); ctx.lineTo(Math.max(0, end), y); ctx.stroke(); ctx.restore();
  if (i > 1) vGear(ctx, 0, y, 24, main);
  if (i < n) vGear(ctx, W, y, 24, main);
  const mx = snap(end) - 20;
  pxr(ctx, mx, 0, 40, 40, main); pxr(ctx, mx + 6, 8, 28, 22, C8.W);
  pxr(ctx, mx + 11, 13, 6, 6, C8.K); pxr(ctx, mx + 23, 13, 6, 6, C8.K);
  pxr(ctx, mx + 17, -12, 6, 12, dark ? C8.W : C8.K); pxr(ctx, mx + 14, -18, 12, 8, aqua ? C8.W : C8.A);
}
~~~~
<!-- END FILE -->

---

### `assets/render/package.json`

<!-- FILE: assets/render/package.json code -->
~~~~json
{
  "name": "aiotrix-6-things",
  "private": true,
  "type": "module",
  "scripts": {
    "dev": "npx --yes hyperframes@0.8.55 preview",
    "check": "npx --yes hyperframes@0.8.55 check",
    "render": "npx --yes hyperframes@0.8.55 render",
    "publish": "npx --yes hyperframes@0.8.55 publish"
  }
}
~~~~
<!-- END FILE -->

---

### `assets/render/hyperframes.json`

<!-- FILE: assets/render/hyperframes.json code -->
~~~~json
{
  "$schema": "https://hyperframes.heygen.com/schema/hyperframes.json",
  "registry": "https://raw.githubusercontent.com/heygen-com/hyperframes/main/registry",
  "paths": {
    "blocks": "compositions",
    "components": "compositions/components",
    "assets": "assets"
  },
  "media": {
    "autoProxy": true
  }
}
~~~~
<!-- END FILE -->

---

### `assets/example-content.json`

<!-- FILE: assets/example-content.json code -->
~~~~json
{
  "title": "6 things your team could stop doing by hand this week",
  "style": "playful",
  "handle": "@arealtimetech",
  "slides": [
    {"template": "cover", "headline": "**6 things** your team could stop doing by hand this week",
     "sub": "Your team is great. **The busywork isn't.**", "swipe": "Swipe"},
    {"template": "task", "n": 1, "of": 6, "label": "Client updates", "scene": "calls",
     "headline": "Still answering \u201cWhere's my shipment?\u201d **all day?**",
     "pain": "Every call pulls someone off real work.",
     "whatif": "What if clients got live updates before they even asked?",
     "outcome": ["Fewer calls", "Faster answers", "More trust"]},
    {"template": "task", "n": 2, "of": 6, "label": "Retyping documents", "scene": "docs",
     "headline": "Typing the same invoice **three times?**",
     "pain": "One wrong digit = a penalty or a held shipment.",
     "whatif": "What if every document was read once, with mismatches flagged for you?",
     "outcome": ["Fewer errors", "Faster paperwork"]},
    {"template": "task", "n": 3, "of": 6, "label": "Stock reorders", "scene": "stock",
     "headline": "Out of stock **after** the order is in?",
     "pain": "Most stock-outs are spotted too late.",
     "whatif": "What if a reorder was drafted the moment stock ran low, ready for your OK?",
     "outcome": ["No surprises", "Less cash stuck", "You stay in control"]},
    {"template": "task", "n": 4, "of": 6, "label": "Matching vendor bills", "scene": "bills",
     "headline": "Matching POs, delivery notes and invoices **by hand?**",
     "pain": "Pay late, or pay for what never came.",
     "whatif": "Imagine all three matched for you, with only real mismatches flagged.",
     "outcome": ["Vendors paid on time", "Never overpay"]},
    {"template": "task", "n": 5, "of": 6, "label": "Chasing vendors", "scene": "chats",
     "headline": "Chasing vendors on **endless** WhatsApp threads?",
     "pain": "When the chaser gets busy, things slip.",
     "whatif": "What if follow-ups went out on their own, with every reply in one place?",
     "outcome": ["Hours back", "Nothing forgotten"]},
    {"template": "task", "n": 6, "of": 6, "label": "Small approvals", "scene": "approvals",
     "headline": "Still approving every **small** purchase yourself?",
     "pain": "Everything waits on one signature.",
     "whatif": "What if small spends were approved within your rules, and only big ones came to you?",
     "outcome": ["Control over every rupee", "No bottleneck"]},
    {"template": "reveal",
     "headline": "You've built something that works. What if it worked **even smoother** without you having to lift a finger?",
     "body": "That's where **ART (A Realtime Tech)** comes in. Aiotrix's Governed Automation Platform sits on top of the tools you already run and takes all six off your plate. You set the rules.",
     "line": "No switching systems. No starting over.",
     "sign": "Made with pride in Mangaluru."},
    {"template": "cta", "headline": "Which one costs **you** the most?",
     "chips": ["Client updates", "Retyping docs", "Stock reorders", "Vendor bills", "Vendor follow-ups", "Small approvals"],
     "main": "Comment the number \ud83d\udc47 or DM us to see where ART fits first.",
     "save": "Save this for your next team meeting."}
  ]
}
~~~~
<!-- END FILE -->

---

### `assets/kit/brand/logo-on-dark.png` (image, base64)

<!-- FILE: assets/kit/brand/logo-on-dark.png base64 -->
~~~~
iVBORw0KGgoAAAANSUhEUgAAAZAAAACfCAMAAADgQH+fAAAAwFBMVEX////+/v79/f38/Pz7+/v6+vr5+fn4+Pj29vbz8/Pw8PDu
7u7r6+vo6Ojm5ubj4+Pf39/a2trT09PKysq/v7+ysrKnp6ebm5uSkpKMjIyBgYF5eXl1dXVvb29lZWVgYGBcXFxWVlZNTU1DQ0M6
OjoyMjIsLCwnJyciIiIfHx8eHh4dHR0cHBwbGxsaGhoZGRkYGBgXFxcWFhYVFRUUFBQTExMSEhIREREQEBAPDw8ODg4NDQ0MDAwL
CwsKCgoHBwdZRRKdAAAkd0lEQVR42u1dh3biShZUIIqcDTbYZFBA5Cjw///V1u0WIIGEBZ45bz2mz9l9ZwwI0aXum+pWC6Pn+L8a
wnMKnoA8xxOQJyDP8QTkCchzPAF5AvIc/yEghnYxjNNL2j1D973gnZ//5YAYU2vnGtb0iMh4vws+rLX9MWNm7R4Y1sJ4AsLw6L1f
jN6MTY0x7jc+3oOP1sS+YPf9kdFoz4wnINiVrHfhYhRXuj21JeGOUd5r/IIN4aFROahPQDB/uw8pJDlHWKjv2dQYk3lRiEjBRkhs
7jgg26Ycku4eEfnlCYgNiCC5nlRJTPanbI3o835WkAM93pKQ6k/YlqOv24J4//oICU9AfAABBGV7brR1J3H5qveQjzsWUOzGHkDk
CYg/IIIktzZ8dlWrFZGCzK4oNDe25RkP0k9A/iwgslBY2h7P8NAQAiAiifnJyW+bF4KtqicgQQEBIo29PTvq4U2Qxa93rLfjB+Bm
lTG9T0D+JCCSmNVMe41oh9qXiEhiejA+RhHsA09A/iggmNDaaXoCIEJv105X3Db/6palX+R3fgUg5PpOjqmQLxFxLRCkTrrx+616
YED05Z7GxPhVgOCZr57mhyEiSbctiObMjj1g1YMCoi9bb/V6o9GbGr8KEFFM8JTWGLYEiNQF/zmWhbxrdtRD5X6rHhAQONUpnmjZ
q78KEMwym6BxX6WoXT28R30ttSwdw5ajm9X4aytExWKNhDBinbn+qwARRYWWiKk2BnONJqKV9HnsZaQFNddT/IgRCQYIctNJUbK/
VP1VgNhWBJmp8mhGiOy6eU/TLgl5wzQu9vni3Y5vMEDUw4sQEcpFMYTn5V+yIgEAEbmjpX7WCmOGyGpYEsTrkEWKdVaa++qPRCKB
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
~~~~
<!-- END FILE -->
