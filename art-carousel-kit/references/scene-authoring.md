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
