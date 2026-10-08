---
name: art-carousel-design-style2
description: Design and render animated Instagram carousels for ART (A Realtime Tech) by Aiotrix in ART Style 2, the dark/aqua/light "standout" look with photoreal 3D cut-out objects (no mascot). Slides alternate a deep blue-green gradient, full aqua, light and teal-green; huge Poppins capitals on the cover, Preahvihear headlines with one aqua accent, a giant vertical word across a slide edge, ghost numbers, light streaks and lens flares, and 3D objects that cross slide edges. Every slide is a 4-second 1080x1350 MP4 where text stays still and each object has one small story moment (sparks, bubbles, a tin toppling, a van rolling, flames flickering). Images come from free routes by default (a Google AI Studio or Gemini prompt), with paid generation only on request. Use whenever someone asks for an ART or Aiotrix carousel in Style 2, the 3D-object or "standout" style, or redoes a post in that style, even if they only give the post title. For the robot-mascot stage look and LinkedIn carousels use the ART-carousel-design skill instead. Not for other brands or ART Reels.
---

# ART-carousel-design-style2

Turns an approved ART carousel script into nine finished, animated Instagram slides in ART Style 2. The style was set and approved by the ART team on the "Festive season" carousel (October 2026). Every new post keeps the same look and gets its own 3D objects, story moments and topic words.

**Fixed across posts**: background rhythm, text format and positions, frame (counter, footer, arrow box), light effects, motion rules, checks, the logo rule.
**New for every post**: the six or so 3D objects, their story moments, the vertical word, the giant word, the reveal's ghost word, warm festive lights or not.

> **Reading this as a single file?** Everything mentioned below as `references/…`, `scripts/…` or `assets/…` is included further down, in the Appendix. You can read those sections directly, or unpack them into a folder with the snippet under "Unpack". The example's images are not in the single file; generate your own (references/images.md).

**Style 1 or Style 2?** ART has two Instagram styles and the team chooses per post. Style 1 (white stage, pixel-robot mascot) and the LinkedIn static carousel live in the **ART-carousel-design** skill. If it isn't clear which style is wanted, ask (multiple choice) before starting.

## Read first
- `references/design-language.md`: the whole look and the reason for each rule. Read it every time.
- `references/motion.md`: what always moves, the story-moment library, and how to choose moments.
- `references/images.md`: the 3D-object prompt pattern, the free routes, checks, and cut-outs.
- `references/copy-rules.md`: the script rules the visuals must respect. Flag problems; never rewrite copy.
- `assets/example/content.json`: the complete content file of the approved pilot (with its prompts in `assets/example/PROMPTS.md`).

## Setup
The design work (planning, laying out copy, choosing objects and moments, writing image prompts) needs only an assistant that can read this skill. Producing the files needs a computer with:
- **Python 3.10+** with `pip install playwright pillow`, then `python -m playwright install chromium`
- **Node.js 18+** (`npx` runs HyperFrames 0.8.55, which renders the MP4s; it downloads itself on first use)
- **ffmpeg** on the PATH
- Optional, for free cut-outs: `pip install "rembg[cpu]"`

Then run `python scripts/setup_assets.py` once (downloads the free fonts and GSAP if missing, and reports what's installed). The ART logo is included. If the tools aren't available, still do steps 1–4 and hand the project folder to someone who can run the scripts.

## Workflow
Keep updates short. Show a plan before building, use multiple-choice questions where there's a real choice, and show two finished slides before making all of them.

### 1. Get the approved script
Ask for the approved carousel script (file or pasted text). Use the Instagram copy exactly as written. If it isn't approved, or breaks `references/copy-rules.md`, say so before designing. The cover needs a big hook line and a pride-led question; if the script only has one headline, propose the split and get it approved.

### 2. Plan objects and moments, get an OK
A short table, one row per slide: background, the 3D object (and which slide edge it crosses), its story moment, plus the vertical word, the giant word and the reveal's ghost word. Moments come from `references/motion.md`; keep them calm and tied to each slide's problem. Wait for approval.

### 3. Images (free first)
Write `images/PROMPTS.md` with the pattern in `references/images.md`, give the click-by-click free steps (Google AI Studio / Gemini, fallbacks Bing Image Creator or ChatGPT free), and wait for the images in `images/raw/`. Paid generation (`scripts/gen_images.py`, about $0.04 per image) only if the user asks and has seen the cost. **Look at every image**: no real brand badges, no readable text, no people. Then cut them out (`scripts/cutout.py`, free) and, for a topple moment, split the prop (`scripts/split_prop.py`).

### 4. Set up the project and fill content.json
```bash
python scripts/new_project.py <projects_folder>/<post-slug> "<full post title>"
```
Fill `content.json` from the script word for word (`**double asterisks**` mark the one accent phrase) and add the `objects` list (image, slide, x, y, w, rot, glow, ph, moment). The template docstring at the top of `scripts/build.py` lists every field; `assets/example/content.json` shows a finished post. Keep the project in a normal local folder (renders are heavy), not inside a synced cloud folder.

### 5. Build, then look
```bash
python scripts/build.py <project>
python scripts/stills.py <project>          # stills + layout checks; every slide must print OK
python scripts/frames.py <project>          # 6 frames per slide -> proof/frames-NN.jpg
```
**Open and look at the stills and every frame sheet.** Fix overlaps by nudging `x`, `y`, `w` of text or objects, rebuild, look again. `stills.py` warns when a 3D object covers text; resolve every warning or say why it's fine.

### 6. Show two before all
Render the cover plus one slide with a story moment first (`python scripts/render.py <project> 01,04`) and share them. After approval, render the rest. When feedback is about the style, apply it to the whole carousel.

### 7. Render and verify
```bash
python scripts/render.py <project>
```
Every slide must report `lint=0 errors`, `1080,1350,30/1 4.000000` and `text-moved` between 0 and 30, then `OK`. Pull one or two frames from the MP4s with ffmpeg and look at them.

### 8. Hand over
The MP4s are in `<project>/render/out/`, the stills in `<project>/stills/`. Send them in posting order with a few lines: what moves on each slide, the check results, and where the files are. To gather everything into one folder: `python scripts/publish.py <project> <their folder> --archive-as <tag>` (keeps the previous version instead of overwriting it).

## The rules that matter most (reasons in design-language.md)
- The ART logo appears only on the reveal, always the aqua icon with white clock hands. Animating the hands is a brand exception: note it for the brand owner's sign-off.
- Text never moves; every headline is readable from the first frame.
- 3D objects tell the slide's problem, cross slide edges, never cover text, and never show real brands, readable text, people or product screens.
- Images cost nothing by default; paid routes only on request with the cost shown.
- Calm motion: one small story moment per object.
- No real companies, numbers or product screens; ART is named only on the reveal.
- Report honestly: if a check fails or something looks off, say so. Never say a file is done without having checked it exists.

## Extending the system
- New story moment: see the last section of `references/motion.md`.
- New slide layout: add a template function in `scripts/build.py`, check it with `stills.py`, document it in `references/design-language.md`.
- When the team changes a style rule, record the rule and the reason in `references/design-language.md`, then run `python scripts/make_single_file.py` to refresh the single-file edition.

<!-- END SKILL -->

# Appendix: every file in this skill
This single file contains the whole skill. If your assistant can read it, it can follow the instructions above directly; the sections below are the reference documents and the code the instructions point to (`references/...`, `scripts/...`, `assets/...`).

## Unpack

Run this once with Python 3, in the folder where you saved this file. It rebuilds the full skill folder
(`ART-carousel-design-style2/`) next to it, then run `python ART-carousel-design-style2/scripts/setup_assets.py`.

~~~~python
import pathlib, re
src = pathlib.Path("ART-carousel-design-style2.md").read_text(encoding="utf-8")
out = pathlib.Path("ART-carousel-design-style2")
out.mkdir(exist_ok=True)
(out / "SKILL.md").write_text(src.split("<!-- END SKILL -->")[0].rstrip() + "\n", encoding="utf-8")
for path, kind, body in re.findall(r"<!-- FILE: (\S+) (text|code) -->\n(.*?)\n<!-- END FILE -->", src, re.S):
    f = out / path; f.parent.mkdir(parents=True, exist_ok=True)
    if kind == "code": body = body.split("\n", 1)[1].rsplit("\n", 1)[0]          # strip the ~~~~ fences
    f.write_text(body + "\n", encoding="utf-8")
    print("wrote", f)
~~~~

---

<!-- FILE: references/design-language.md text -->
# ART Style 2: design language (the look, and why)

Style 2 was set by the ART team on the "Festive season" carousel (October 2026), from two reference carousels the team liked:
a dark "standout" tech carousel (big type, giant words across slide edges, ghost numbers, light flares) and a
"split object" sales carousel (one 3D object split across each slide pair, clean text column, one accent word).
**Style 2 = the first one's look + the second one's text format.** Everything here is approved; keep it unless the
team changes a rule (then record the new rule and its reason here).

## Fixed vs per post
- **Fixed**: palette rhythm, text format and positions, frame elements (counter, footer, arrow box), light effects,
  motion rules, checks, the logo rule.
- **Per post**: the 3D objects and their story moments, the vertical word, the giant word, the reveal's ghost word,
  festive/warm lights or not, and small layout nudges so text and objects never collide.

## Canvas and colour
- 1080 × 1350 (4:5), 9 slides: cover, setup, 4 task slides, reveal, outcome, CTA.
- **Background rhythm** (one per slide, `palette` in content.json): dark, aqua, light, aqua, light, dark, dark, teal, dark.
  - **dark**: deep blue-green gradient (#0F4E57 → #08303A → #03161B) with an aqua glow top-right. White text, body #C9D6D8.
  - **aqua**: aqua gradient (#36C2D4 → #04ADC3 → #038DA0) with thin white concentric wave lines. Ink text; accents white.
  - **light**: white → #EEF4F4. Ink text, body #3D3D3D.
  - **teal**: teal-green gradient (#5BBE9E → #41A486 → #2B907F) with wave lines; used for the outcome slide.
  - Why: the ART website will use the same dark/light blue-green look; the rhythm keeps a swipe lively, like the reference.
- Accent colour: aqua #04ADC3 (light aqua #36C2D4 on the dark shape). Result pills are aqua (ink on aqua slides).

## Type (brand fonts only)
- **Preahvihear** for headlines (one accent phrase, marked `**…**`), **Poppins** for everything else.
- Cover: huge **Poppins 700 capitals** (108 px, accent phrase in aqua), then a Preahvihear question (56 px), then a
  short subline with the swipe line in bold aqua, then a dashed curved arrow whose head follows the curve's angle.
- Task slides (B's format, exactly): label `1/4 · ORDERS` (Poppins 700, aqua, 28 px, wide tracking) → headline 64 px →
  pain line (31 px) → what-if line (31 px, semibold) → result pills stacked (27 px, tick + text).
- Setup: headline, body, "Here's where ↓" label, then numbered black circles with white numbers (2 × 2).
- Reveal: logo, headline 55 px, body 27.5 px (ART name bold aqua), one Preahvihear line in aqua, small sign-off.
- Outcome: headline 62 px, four rows with aqua tick circles and a thin line under each, one closing line.
- CTA: centred headline 72 px, double chevron, one line, aqua "DM us…" pill, the save line right under it (28 px),
  and a Like · Comment · Save row near the bottom.
- Slides 2–8 use the slightly larger text set (`sz`); the cover and CTA keep their own sizes.

## Frame (every slide)
- Counter pill top-left (`01/09`), `@arealtimetech` footer bottom-left (26 px). No topic tags.
- **Arrow box** bottom-right on every slide except the last, with a pulsing halo (aqua; white on aqua/teal slides).
- The ART logo appears only on the reveal, and it is always **the aqua icon with white clock hands**.

## Decor (what makes it "standout")
- **Giant vertical word** across the setup slide's right edge into the next slide, on a 150 px strip of the setup
  colour (`vword`). Pick a 1–2 word topic phrase ("Festive rush").
- **Ghost numbers** (1–4) huge and faded behind each task slide's text, on the side away from the text.
- **Dark blob** behind the text on one aqua task slide (`blob`), with airier line spacing there.
- **Giant bottom word** on one light slide (`giant`, e.g. "PAPERWORK"), cut off by the slide edges, an object in front.
- **Ghost word** behind the reveal (`ghost_word`, e.g. "CLOCKWORK", tied to the reveal line).
- **Light effects**: soft whitish-green / whitish-blue streaks on dark, aqua and teal slides; lens flares (bright core,
  thin anamorphic streak, ghost rings) on 3–4 dark slides; bokeh dots on dark slides (warm gold + aqua when the topic is
  festive, `warm_bokeh`; aqua only otherwise). Light slides stay clean.

## 3D objects (instead of a mascot)
- Photoreal 3D product-render cut-outs, one per slide or slide pair, that **tell the slide's problem** (a gift tower,
  a phone spilling order bubbles, a near-empty shelf, an invoice stack, a delivery van, lit diyas).
- Brand-tinted: aqua / teal / ivory with gold touches; the topic's local detail where it fits (cashew tins, marigolds).
- They **cross slide edges** (x < 0 or x + w > 1080), so a swipe feels like one continuous scene.
- They sit beside the text, never under it: the stills check warns when an object covers text.
- Never: real brand badges or logos (check car grilles, packaging), readable text, people, hands or faces, product screens.

## Text never moves
Only images, glows, light effects, tick marks and the clock hands move. Every headline is readable from the first frame.
render.py proves it (text-moved 0–30 per slide).

## Tried and dropped (don't bring these back without asking)
- **Panorama world with the walking robot** (the first Style 2): replaced by this look.
- **Paper slips from the phone, page flips on the invoices, the van driving fully across its slide, a board-shake
  wobble**: tried on the pilot and the team preferred the calmer version. A van rolling forward a little, a prop that
  topples once, one blinking marker: yes.
- Stepped (frame-by-frame) clock hands: replaced by one smooth sweep.
- A bright light sweep: kept, but at 0.15 opacity with a heavy blur.
<!-- END FILE -->

---

<!-- FILE: references/motion.md text -->
# Motion: 4-second "living stills" with one story moment per slide

Every slide is a 4-second MP4 (1080 × 1350, 30 fps). The whole carousel is one strip and one timeline, so an object
that crosses a slide edge moves the same on both slides. Instagram loops each slide; moments that hold an end state
(a fallen tin, a parked van) snap back on the loop. That is accepted.

## Always on (built in, nothing to configure)
| What | Where | How it moves |
|---|---|---|
| Float | every 3D object (unless `"float": false`) | bobs 7 px and rocks ±0.6° on a 4 s cycle; `ph` offsets the phase so objects don't move in sync |
| Lens flares | slides with `flare` | core pulses, streak drifts, ghost rings breathe |
| Light streaks + one sweep | dark, aqua, teal slides | static streaks; one soft band sweeps diagonally at 0.5–2.7 s (0.15 opacity) |
| Bokeh | dark slides | twinkles |
| Arrow-box halo | slides 1 to n-1 | pulses twice (aqua; white on aqua/teal) |
| Tick marks | result pills, outcome rows | draw in from 0.7 s, one after another |
| Cover arrow | cover | dashes flow toward the head; the head nudges forward |
| Setup circles | setup | light up 1 → 4 left to right with a ring pulse |
| Clock hands | reveal logo | one smooth sweep, 0.5–3.1 s (animating part of the logo needs the brand owner's OK) |
| DM button | CTA | soft glow pulse |

## Story moments (pick one per object in content.json `moment`)
| type | Use it for | Fields |
|---|---|---|
| `sparks` | festive/celebration energy (sparklers, fireworks fuse) | `points`: emitter spots as fractions of the image `[[x, y], …]` |
| `bubbles` | messages or orders arriving (phone, laptop, inbox) | `origin`: where they're born, as image fractions `[x, y]` |
| `topple` | something running out / tipping over (tin, jar, cup) | `body`, `lid`, `geom` from split_prop.py; `angle` (-85 left, +85 right), `at` (0.75 s), `foreshorten` (0.72) |
| `blink` | a flag, tab or warning light being caught | `box`: `[left, top, width, height]` as image fractions |
| `drive` | movement toward the next slide (van, cart, parcel) | `dx` px forward, `at`, `dur`; it rocks slightly while rolling |
| `flicker` | flames, lamps, candles | `points`: flame spots as image fractions |
| `none` | float only | |

To find the fractions, open the cut-out PNG in any image viewer, read the pixel position and divide by its width and height.

## Choosing moments for a new post
- One small action per slide, tied to that slide's problem ("stock runs out" → a tin topples).
- Calm beats busy: the team turned down page flips, paper storms and objects racing across a slide.
- Keep moments on the object's own slide; only `drive` and `bubbles` should reach into a neighbour.
- Check with `frames.py` (6 frames per slide) and zoom in on small moments (`--zoom x0,y0,x1,y1 --times …`).

## New moment types
Add a branch in `object_html()` (the HTML it needs) and in the `R(t)` function in `scripts/build.py` (how it moves as a
pure function of t, so seeking works), document it in this table, and test it on one slide before using it.
<!-- END FILE -->

---

<!-- FILE: references/images.md text -->
# 3D object images: prompts, free routes, cut-outs

Each post needs about six 3D objects (cover hero + one per task slide or slide pair + one for the outcome).
**Default: free.** Paid generation only when the user asks for it and has seen the cost.

## 1. Write the prompts (images/PROMPTS.md)
`new_project.py` creates the sheet. One section per image, in this exact format (gen_images.py reads it):

```
## 1. `01-cover-gift-tower.png` (aspect 3:4, slide 1)
<what the object is, its colours, its angle>. + shared style line
```
The **shared style line** (keep it word for word; it makes every object match):
> Photoreal 3D product render, premium commercial studio style, one isolated object group centred with generous empty
> margin all round, on a plain seamless flat light-grey background (#E9ECEC), soft diffused key light from the top left,
> subtle cool aqua-teal (#04ADC3) rim light on the edges, realistic materials, crisp detail, sharp focus. No text, no
> letters, no numbers, no logos, no brand names, no people, no hands, no faces. No floor and no cast shadow on the background.

Prompt tips that worked:
- Name brand-tinted colours in the object: "glossy boxes in deep teal, aqua and ivory with aqua satin ribbons".
- Vehicles and packaging: say "an unbranded fictional design with a smooth plain front grille, no emblem, no badge, no
  manufacturer logo and no lettering anywhere" (a model added a real car badge without it).
- Paper: "blank table grids and abstract soft grey bars, absolutely no letters, words or headings" (else fake text appears).
- Aspect: 3:4 or 4:5 for tall objects, 16:9 for wide ones.
- See assets/example/PROMPTS.md for the six approved Festive prompts.

## 2. Generate (free routes, offer them first)
Click by click for the person generating:
1. Open **aistudio.google.com** (or the **Gemini** app) and sign in with a Google account.
2. Choose the Gemini model with **"Image"** in its name; set the aspect ratio shown in the prompt.
3. Paste prompt 1, press **Run**, make 2–3 versions, keep the best. Do the rest **in the same chat** so they match.
4. Download each image with the exact file name into `images/raw/` (or paste them to the assistant).
Fallbacks if the free allowance runs out or the tool fails: **Microsoft Designer / Bing Image Creator**, **ChatGPT free
tier**. Check the tool's terms allow commercial use, and crop any visible watermark.

**Paid, opt-in only** (when asked, after showing the cost): `python scripts/gen_images.py <project>` prints the estimate
(fal.ai Nano Banana, about $0.04 per image, about $0.25–0.35 per post with redos); add `--yes` to spend. Needs the
FAL_KEY environment variable; never write the key into a file or share it.

## 3. Check every image (always, by looking)
- Real brand badges, emblems or logos (car grilles, packaging, appliances) → regenerate.
- Readable or fake text (headings like "INVOICE", hex codes printed in a corner) → regenerate, or paint it out if tiny.
- Extra people, hands, faces, product screens → regenerate.
- Wrong facing direction → mirror it (fine when there is no text on it).

## 4. Cut out the background
- **Free, local**: `python scripts/cutout.py <project>` (rembg; `pip install "rembg[cpu]"`, the first run downloads a
  model once). Writes trimmed PNGs to `images/cut/`.
- **Free, web** (if rembg can't run): remove.bg, Adobe Express "Remove background" or Photoroom; save the PNG with the
  same name into `images/cut/`.
- **Opt-in**: `cutout.py <project> --fal` (fal.ai BiRefNet, a fraction of a cent per image; needs FAL_KEY).
Look at the cut-outs on a dark background: no grey halo, no missing parts (thin sparks may drop; that's fine).

## 5. A prop that topples (optional "topple" moment)
1. AI-edit the RAW image to remove just that prop, keeping everything else identical (free: an AI eraser in Gemini,
   Canva or Photoshop Express; paid opt-in: `gen_images.py <project> --edit <raw> "<instruction>" <out> --yes`).
2. Cut the edited image out (step 4). It becomes the object's `image`.
3. `python scripts/split_prop.py <project> <original cut> <edited cut> <name> --cx … --rx … --top … --lid … --bottom …`
   cuts the prop into a body and a lid layer, writes the geometry, checks the edit lines up (offset 0,0) and saves a
   check image: the right side must look exactly like the left.
Works for upright cylinders (tins, jars, cups, bottles).
<!-- END FILE -->

---

<!-- FILE: references/copy-rules.md text -->
# Copy rules the designer must respect

The designer **never writes or rewrites copy**. It lays out the approved script word for word. If copy breaks a rule below or won't fit, flag it to the user with a suggested fix; don't change it silently.

## Carousel structure (curiosity format, 9 slides in Style 2)
- **Cover**: a big hook line (one accent phrase) + a pride-led question + a subline with the swipe line. ART is not named.
- **Setup**: why the topic matters now, then "Here's where" and the four stops.
- **Four task slides**: label (`1/4 · Orders`), question headline (one phrase accented), one pain line, a "What if / How about / Imagine" line, and two result pills. ART and tools are not named.
- **Reveal**: the first and only slide that names ART: "ART (A Realtime Tech)", Aiotrix's Governed Automation Platform. The ART logo appears here only.
- **Outcome**: headline + four tick rows + one closing line.
- **CTA**: headline, one line, the "DM us…" line, the save line.

## Tone (the ART team's standing rules)
- **Pride-led.** The business is already good; ART is a layer on top of the tools it already runs ("no switching systems, no starting over"); you still set the rules. ART is never a rescue. Even the cover question assumes the business copes ("Your dispatch already keeps up. What if it got even simpler?").
- **Never imply the business isn't at its best.** Use "even smoother / even more / even simpler". Avoid "finally", "fix", "get back on track", "less strain".
- Reveal wording is written fresh per topic.
- Short: the pictures explain, the words land the point.
- No numbers until approved, no real company names, logos or premises, no product screens or UI. One local detail per post is welcome (Mangaluru, coastal Karnataka, the port, cashew, festive season).
- Festival names: the team may prefer the general "festive season" over a specific festival name; follow the approved script.

## What the visuals must also respect
- Humour and drama target the busywork, never the business or its staff.
- Never present a real company as an ART user (no real shop signs, vehicle badges or brand names in the 3D objects).
- The LinkedIn version of a post is a separate, formal asset; never cross-post the Instagram carousel there.
<!-- END FILE -->

---

### `scripts/setup_assets.py`

<!-- FILE: scripts/setup_assets.py code -->
~~~~python
"""ART Style 2 skill: download the free third-party files the kit needs (only if they're missing), then check the toolchain.

Usage: python setup_assets.py
- Fonts: Preahvihear + Poppins 400/500/600/700 from the Google Fonts repository (SIL Open Font License).
- GSAP 3.14.2 from jsDelivr (free under GreenSock's standard licence).
Then reports whether Playwright/Chromium, Pillow, Node (npx), ffmpeg and rembg (optional, free cut-outs) are available.
"""
import pathlib, subprocess, urllib.request

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
        "Pillow": 'python -c "import PIL"',
        "Playwright + Chromium": 'python -c "from playwright.sync_api import sync_playwright as s; p=s().start(); b=p.chromium.launch(); b.close(); p.stop()"',
        "Node / npx": "npx --version",
        "ffmpeg": "ffmpeg -version",
        "rembg (optional: free cut-outs)": 'python -c "import rembg"',
    }
    for name, cmd in checks.items():
        r = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        print(("ok     " if r.returncode == 0 else "MISSING"), name)
    print("\nIf anything is MISSING, see 'Setup' in SKILL.md. Planning, copy layout and image prompts work without it;"
          "\nstills need Pillow + Playwright; MP4s also need Node and ffmpeg."
          '\nFree cut-outs: pip install "rembg[cpu]" (or a free web tool, see references/images.md).')

if __name__ == "__main__":
    main()
~~~~
<!-- END FILE -->

---

### `scripts/new_project.py`

<!-- FILE: scripts/new_project.py code -->
~~~~python
"""Start a new ART Style 2 carousel project.

Usage: python new_project.py <project_dir> "<full post title>"
Creates content.json (9 slides in the approved order: cover, setup, 4 tasks, reveal, outcome, cta, with the
default background rhythm), images/raw/, images/cut/ and images/PROMPTS.md (the 3D-object prompt sheet).
Fill content.json with the APPROVED script copy, word for word, then plan one 3D object + story moment per slide.
See assets/example/content.json for a complete approved post.
"""
import json, pathlib, sys

STYLE_LINE = ("Photoreal 3D product render, premium commercial studio style, one isolated object group centred with generous "
              "empty margin all round, on a plain seamless flat light-grey background (#E9ECEC), soft diffused key light from the "
              "top left, subtle cool aqua-teal (#04ADC3) rim light on the edges, realistic materials, crisp detail, sharp focus. "
              "No text, no letters, no numbers, no logos, no brand names, no people, no hands, no faces. No floor and no cast shadow on the background.")

PROMPTS = f"""# {{title}}: 3D object prompts

Generate each image on the plain grey background, then cut it out (scripts/cutout.py or a free web tool).
Save the downloads into `images/raw/` with the file names below.

## Shared style line (already included at the end of every prompt)
{STYLE_LINE}

## 1. `01-cover-object.png` (aspect 3:4, slide 1)
<the hero object for the topic, themed, slightly heroic angle>. + shared style line

## 2. `02-object.png` (aspect 16:9, slides 3-4)
<object for task 1>. + shared style line
"""

def main(project, title):
    p = pathlib.Path(project)
    for d in ["images/raw", "images/cut"]: (p / d).mkdir(parents=True, exist_ok=True)
    task = lambda n: {"template": "task", "n": n, "of": 4, "label": "Label", "headline": "Question headline with **one accent?**",
                      "pain": "One pain line.", "whatif": "What if ...?", "outcome": ["Outcome one", "Outcome two"]}
    content = {
        "title": title, "handle": "@arealtimetech",
        "palette": ["dark", "aqua", "light", "aqua", "light", "dark", "dark", "teal", "dark"], "warm_bokeh": False,
        "slides": [
            {"template": "cover", "big": "**Accent phrase** rest of the hook.", "question": "Pride-led question line.",
             "sub": "Subline.", "swipe": "Swipe to see ...", "flare": [900, 170, 1.1]},
            {"template": "setup", "headline": "Setup line. **Accent?**", "body": "Short body.", "cue": "Here's where",
             "stops": ["One", "Two", "Three", "Four"], "vword": {"text": "Topic word", "top": 130}},
            dict(task(1), x=200, y=260, w=600, ghost={"side": "right", "offset": -60, "top": 330}),
            dict(task(2), x=440, y=230, w=590, blob=[250, 90, 1000, 1040], ghost={"side": "left", "offset": 20, "top": 420}),
            dict(task(3), x=56, y=240, w=690, ghost={"side": "right", "offset": -40, "top": 260}, giant="TOPICWORD"),
            dict(task(4), x=450, y=240, w=580, ghost={"side": "left", "offset": -30, "top": 330}, flare=[980, 120, 0.8]),
            {"template": "reveal", "headline": "Pride-led line with **accent.** What if ...?",
             "body": "That's where **ART (A Realtime Tech)** comes in. ...", "line": "One short line.", "sign": "Sign-off from Mangaluru.",
             "ghost_word": "WORD", "flare": [940, 260, 1.0]},
            {"template": "outcome", "headline": "Outcome headline, **accent.**", "rows": ["Row one", "Row two", "Row three", "Row four"],
             "closing": "Closing line."},
            {"template": "cta", "headline": "CTA question **accent.**", "line": "One line.", "main": "DM us to ...",
             "save": "Save this and share it with ...", "flare": [540, 150, 0.9]},
        ],
        "objects": [],
    }
    if not (p / "content.json").exists(): (p / "content.json").write_text(json.dumps(content, indent=2, ensure_ascii=False), encoding="utf-8")
    if not (p / "images" / "PROMPTS.md").exists(): (p / "images" / "PROMPTS.md").write_text(PROMPTS.format(title=title), encoding="utf-8")
    print("project ready:", p.resolve())

if __name__ == "__main__":
    if len(sys.argv) < 3: sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2])
~~~~
<!-- END FILE -->

---

### `scripts/gen_images.py`

<!-- FILE: scripts/gen_images.py code -->
~~~~python
"""PAID, opt-in: generate the 3D objects with fal.ai Nano Banana (about $0.04 per image), or AI-edit one image.

Only when the user asks for it and has seen the cost estimate. The free route is the default (references/images.md).
Usage:
  python gen_images.py <project> [names ...]                      -> prints the cost estimate only
  python gen_images.py <project> [names ...] --yes                -> generates images/raw/<name>.png from images/PROMPTS.md
  python gen_images.py <project> --edit <raw.png> "<instruction>" <out.png> [--yes]
      AI edit, e.g. remove one prop so it can topple on its own layer ("Remove the front-left tin completely ...
      keep everything else exactly the same: camera, framing, size and position ..."). Writes images/raw/<out.png>.
Key: the FAL_KEY environment variable (never write it into a file). Prompts: images/PROMPTS.md (see new_project.py).
"""
import base64, concurrent.futures as cf, json, os, pathlib, re, sys, time, urllib.request

PRICE = 0.039

def fal():
    key = os.environ.get("FAL_KEY") or sys.exit("Set the FAL_KEY environment variable first (never store it in a file).")
    hdr = {"Authorization": f"Key {key}", "Content-Type": "application/json"}
    def call(url, body=None):
        req = urllib.request.Request(url, data=json.dumps(body).encode() if body else None, headers=hdr, method="POST" if body else "GET")
        return json.loads(urllib.request.urlopen(req, timeout=120).read())
    def run(endpoint, body, out):
        sub = call(f"https://queue.fal.run/{endpoint}", body)
        for _ in range(80):
            time.sleep(4)
            if call(sub["status_url"]).get("status") == "COMPLETED": break
        urllib.request.urlretrieve(call(sub["response_url"])["images"][0]["url"], out); return out.name
    return run

def jobs(project):
    md = (project / "images" / "PROMPTS.md").read_text(encoding="utf-8")
    style = md.split("## Shared style line (already included at the end of every prompt)\n")[1].split("\n\n")[0].strip()
    return {m[0]: (m[1], m[2].replace("+ shared style line", style).strip())
            for m in re.findall(r"## \d+\. `(\S+?)\.png` \(aspect (\d+:\d+)[^)]*\)\n(.+?)(?=\n\n## |\Z)", md, re.S)}

def main(argv):
    project = pathlib.Path(argv[0]); yes = "--yes" in argv; argv = [a for a in argv[1:] if a != "--yes"]
    (project / "images" / "raw").mkdir(parents=True, exist_ok=True)
    if argv and argv[0] == "--edit":
        src, instr, out = pathlib.Path(argv[1]), argv[2], project / "images" / "raw" / argv[3]
        print(f"1 AI edit, about ${PRICE:.2f}.")
        if not yes: return print("Add --yes to spend it.")
        uri = "data:image/png;base64," + base64.b64encode(src.read_bytes()).decode()
        print("saved", fal()("fal-ai/nano-banana/edit", {"prompt": instr, "image_urls": [uri], "num_images": 1, "output_format": "png"}, out)); return
    J = jobs(project); names = argv or list(J)
    print(f"{len(names)} image(s), about ${PRICE * len(names):.2f} (fal.ai Nano Banana).")
    if not yes: return print("Add --yes to spend it.")
    run = fal()
    with cf.ThreadPoolExecutor(6) as ex:
        for r in ex.map(lambda n: run("fal-ai/nano-banana", {"prompt": J[n][1], "aspect_ratio": J[n][0], "num_images": 1, "output_format": "png"},
                                      project / "images" / "raw" / f"{n}.png"), names): print("saved", r)
    print("Now LOOK at every image: real brand badges or emblems, readable text, extra objects. Redo any that fail.")

if __name__ == "__main__":
    if len(sys.argv) < 2: sys.exit(__doc__)
    main(sys.argv[1:])
~~~~
<!-- END FILE -->

---

### `scripts/cutout.py`

<!-- FILE: scripts/cutout.py code -->
~~~~python
"""Cut the 3D objects out of their plain grey background: images/raw/*.png -> images/cut/*.png (trimmed).

Usage: python cutout.py <project> [file names ...] [--fal]
Default route, free and local: rembg (pip install "rembg[cpu]"; the first run downloads a ~180 MB model once).
If rembg can't run (no pip, blocked download, old computer), use a free web tool instead and save the PNG with the
same name into images/cut/: remove.bg, Adobe Express "Remove background" or Photoroom (free tiers; check the result).
--fal: fal.ai BiRefNet v2 (costs a fraction of a cent per image). Opt-in only, when the user asks. Needs the FAL_KEY
environment variable; never write the key into a file.
"""
import base64, json, os, pathlib, sys, time, urllib.request
from PIL import Image

def trim(path):
    im = Image.open(path).convert("RGBA"); box = im.getchannel("A").point(lambda a: 255 if a > 8 else 0).getbbox()
    im.crop(box).save(path); return im.crop(box).size

def via_rembg(src, dst):
    from rembg import remove, new_session
    remove(Image.open(src).convert("RGB"), session=new_session("isnet-general-use")).save(dst)

def via_fal(src, dst):
    key = os.environ.get("FAL_KEY") or sys.exit("Set the FAL_KEY environment variable first (never store it in a file).")
    hdr = {"Authorization": f"Key {key}", "Content-Type": "application/json"}
    call = lambda url, body=None: json.loads(urllib.request.urlopen(urllib.request.Request(
        url, data=json.dumps(body).encode() if body else None, headers=hdr, method="POST" if body else "GET"), timeout=120).read())
    uri = "data:image/png;base64," + base64.b64encode(pathlib.Path(src).read_bytes()).decode()
    sub = call("https://queue.fal.run/fal-ai/birefnet/v2", {"image_url": uri, "operating_resolution": "2048x2048", "output_format": "png"})
    for _ in range(80):
        time.sleep(3)
        if call(sub["status_url"]).get("status") == "COMPLETED": break
    urllib.request.urlretrieve(call(sub["response_url"])["image"]["url"], dst)

def main(project, names, use_fal):
    p = pathlib.Path(project); (p / "images" / "cut").mkdir(parents=True, exist_ok=True)
    files = [p / "images" / "raw" / n for n in names] or sorted((p / "images" / "raw").glob("*.png"))
    for f in files:
        dst = p / "images" / "cut" / f.name
        try:
            (via_fal if use_fal else via_rembg)(f, dst); print(f.name, "->", trim(dst))
        except Exception as e:
            print(f.name, "FAILED:", str(e)[:160])
            print("  Free fallback: remove the background on remove.bg / Adobe Express / Photoroom and save it as", dst)

if __name__ == "__main__":
    a = [x for x in sys.argv[1:] if x != "--fal"]
    if not a: sys.exit(__doc__)
    main(a[0], a[1:], "--fal" in sys.argv)
~~~~
<!-- END FILE -->

---

### `scripts/split_prop.py`

<!-- FILE: scripts/split_prop.py code -->
~~~~python
"""Split one cylindrical prop (a tin, jar, cup, bottle) out of a cut-out so it can topple on its own ("topple" moment).

Usage: python split_prop.py <project> <object.png> <base.png> <name> --cx 198 --rx 66 --top 62 --lid 112 --bottom 302
  object.png  the cut-out WITH the prop (images/cut/)
  base.png    the same image WITHOUT the prop, cut out too (images/cut/). Make it by AI-editing the RAW image to remove
              the prop: free in an editor's AI eraser (Gemini image edit, Canva Magic Eraser, Photoshop Express), or
              paid opt-in with gen_images.py --edit. Then run cutout.py on it.
  name        prefix for the outputs, e.g. 03-tin -> images/cut/03-tin-body.png, 03-tin-lid.png, 03-tin.json
  --cx/--rx   the prop's centre x and half-width; --top/--bottom its top of lid and bottom edge; --lid the y where the
              lid ends (all in object.png pixels; open the image in any viewer to read them)
Then use in content.json: {"type": "topple", "body": "<name>-body.png", "lid": "<name>-lid.png", "geom": "<name>.json",
"angle": -85 (falls left; +85 falls right), "at": 0.75, "foreshorten": 0.72}, with the object's "image" set to the base.
Checks that the base lines up with the original (best offset should be 0,0) and writes a check image to proof/.
"""
import argparse, json, pathlib
from PIL import Image, ImageChops, ImageDraw

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("project"); ap.add_argument("obj"); ap.add_argument("base"); ap.add_argument("name")
    for k in ["cx", "rx", "top", "lid", "bottom"]: ap.add_argument(f"--{k}", type=int, required=True)
    a = ap.parse_args(); cut = pathlib.Path(a.project) / "images" / "cut"
    src = Image.open(cut / a.obj).convert("RGBA"); W, H = src.size; sp = src.load()
    mask = Image.new("L", (W, H), 0); d = ImageDraw.Draw(mask); ry = max(8, a.rx // 3)
    d.rectangle((a.cx - a.rx, a.top + ry // 2, a.cx + a.rx, a.bottom - ry // 2), fill=255)
    d.ellipse((a.cx - a.rx, a.top, a.cx + a.rx, a.top + ry * 2), fill=255)
    d.ellipse((a.cx - a.rx + 1, a.bottom - ry, a.cx + a.rx - 1, a.bottom), fill=255); mp = mask.load()
    lid_y = lambda x: a.lid + (ry // 2) * (1 - ((x - a.cx) / a.rx) ** 2) ** 0.5 if abs(x - a.cx) <= a.rx else a.lid
    def layer(cond):
        im = Image.new("RGBA", (W, H), (0, 0, 0, 0)); p = im.load()
        for y in range(H):
            for x in range(W):
                if mp[x, y] and sp[x, y][3] > 0 and cond(x, y): p[x, y] = sp[x, y]
        return im
    geom = {"pivot": [a.cx - a.rx, a.bottom - 2], "src": {"w": W, "h": H}}
    for part, im in [("lid", layer(lambda x, y: y <= lid_y(x))), ("body", layer(lambda x, y: y > lid_y(x)))]:
        box = im.getbbox(); im.crop(box).save(cut / f"{a.name}-{part}.png")
        geom[part] = {"x": box[0], "y": box[1], "w": box[2] - box[0], "h": box[3] - box[1]}
    (cut / f"{a.name}.json").write_text(json.dumps(geom, indent=1), encoding="utf-8")
    base = Image.open(cut / a.base).convert("RGBA"); best = None
    for dx in range(-6, 7):
        for dy in range(-6, 7):
            bb = Image.new("RGBA", (W, H)); bb.alpha_composite(base, (dx, dy))
            region = (min(W - 1, a.cx + a.rx + 10), 0, W, H)
            diff = ImageChops.difference(src.crop(region).convert("L"), bb.crop(region).convert("L"))
            score = sum(i * n for i, n in enumerate(diff.histogram()))
            if best is None or score < best[0]: best = (score, dx, dy)
    proof = pathlib.Path(a.project) / "proof"; proof.mkdir(exist_ok=True)
    chk = Image.new("RGBA", (W * 2 + 20, H), (40, 40, 40, 255)); chk.alpha_composite(src); chk.alpha_composite(base, (W + 20, 0))
    for part in ["body", "lid"]: chk.alpha_composite(Image.open(cut / f"{a.name}-{part}.png"), (W + 20 + geom[part]["x"], geom[part]["y"]))
    chk.convert("RGB").save(proof / f"split-{a.name}.png")
    print("wrote", f"{a.name}-body.png, {a.name}-lid.png, {a.name}.json", "| base offset", best[1:], "(should be (0, 0))",
          "| look at", proof / f"split-{a.name}.png", "(right side must look exactly like the left)")

if __name__ == "__main__":
    main()
~~~~
<!-- END FILE -->

---

### `scripts/build.py`

<!-- FILE: scripts/build.py code -->
~~~~python
"""Build ART Style 2 slides from <project>/content.json -> <project>/slides/slide-NN.html (+ slides/assets/).

Usage: python build.py <project>

How it works: every slide file holds the WHOLE carousel as one horizontal strip (slide i starts at x = (i-1)*1080)
plus one shared animation timeline, and is shifted so only its own slide shows. Anything that crosses a slide edge
(3D objects, the vertical word) is therefore drawn and animated identically on both slides, so the join is seamless
when someone swipes. Text never animates: only images, glows, light effects and icons move.

content.json (see assets/example/content.json for a complete, approved post):
  title, handle, palette (one background per slide: dark | aqua | light | teal), warm_bokeh (festive warm lights on
  dark slides, else aqua only), slides[] (templates below), objects[] (3D cut-outs + their story moment).
  Text fields use **double asterisks** for the one accent phrase.
Templates (layout keys in brackets are optional overrides; defaults are the approved positions):
  cover   big, question, sub, swipe            [big_top, q_top, q_size, sub_top, arrow:[x,y]]
  setup   headline, body, cue, stops[]          [x, y, w, vword:{text, top}]
  task    n, of, label, headline, pain, whatif, outcome[]   [x, y, w, ghost:{side, offset, top}, blob:[l,t,w,h], giant]
  reveal  headline, body, line, sign            [ghost_word]
  outcome headline, rows[], closing             [x, y, w, hd_size]
  cta     headline, line, main, save
  Any slide: flare:[x, y, scale], streaks:[seed, strength] (non-light slides; defaults by slide number)
Objects: {id, image, slide, x, y, w, rot, glow, ph, float, moment:{type, ...}} with x/y relative to the slide's
  top-left (x < 0 or x + w > 1080 crosses into the neighbour). Moment types: sparks, bubbles, topple, blink,
  drive, flicker, none (see references/motion.md).
"""
import html, json, pathlib, shutil, sys
from PIL import Image

SKILL = pathlib.Path(__file__).resolve().parent.parent
KIT = SKILL / "assets" / "kit"
W, H, DUR = 1080, 1350, 4
LOGO_SVG = (KIT / "brand" / "logo-art.svg").read_text(encoding="utf-8")

FONTS = """@font-face { font-family: "Preahvihear"; src: url("assets/fonts/Preahvihear-Regular.ttf"); font-weight: 400; }
@font-face { font-family: "Poppins"; src: url("assets/fonts/Poppins-Regular.ttf"); font-weight: 400; }
@font-face { font-family: "Poppins"; src: url("assets/fonts/Poppins-Medium.ttf"); font-weight: 500; }
@font-face { font-family: "Poppins"; src: url("assets/fonts/Poppins-SemiBold.ttf"); font-weight: 600; }
@font-face { font-family: "Poppins"; src: url("assets/fonts/Poppins-Bold.ttf"); font-weight: 700; }
"""

def esc(s): return html.escape(s)
def acc(s, cls="acc"):
    p = s.split("**"); return "".join(f'<span class="{cls}">{esc(x)}</span>' if i % 2 else esc(x) for i, x in enumerate(p))
TICK = '<svg viewBox="0 0 28 28" width="{s}" height="{s}"><path class="ck" d="M5 15 L11 21 L23 7" fill="none" stroke="{c}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></svg>'
def tick(s=24, c="#fff"): return TICK.format(s=s, c=c)
ICON_HEART = '<svg viewBox="0 0 24 24"><path d="M12 21s-7.5-4.6-9.6-9.2C.9 8.4 3 5 6.4 5c2 0 3.3 1.1 4 2.3h3.2C14.3 6.1 15.6 5 17.6 5 21 5 23.1 8.4 21.6 11.8 19.5 16.4 12 21 12 21z" fill="#04ADC3"/></svg>'
ICON_CHAT = '<svg viewBox="0 0 24 24"><path d="M4 4h16a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2H9l-5 4v-4a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2z" fill="#04ADC3"/></svg>'
ICON_SAVE = '<svg viewBox="0 0 24 24"><path d="M6 2h12a1 1 0 0 1 1 1v19l-7-5-7 5V3a1 1 0 0 1 1-1z" fill="#04ADC3"/></svg>'

def waves(op=.16, cx=1300, cy=1500, col="255,255,255"):
    """Concentric wave lines on the aqua and teal slides."""
    rings = "".join(f'<ellipse cx="{cx}" cy="{cy}" rx="{300 + k * 70}" ry="{220 + k * 52}" fill="none" stroke="rgba({col},{op})" stroke-width="2"/>' for k in range(22))
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="1350">{rings}</svg>'
    return "url(\"data:image/svg+xml;utf8," + svg.replace('"', "'").replace("#", "%23").replace("<", "%3C").replace(">", "%3E") + "\")"

def css(n):
    return FONTS + f"""
:root {{ --aqua:#04ADC3; --aqua-l:#36C2D4; --aqua-d:#038DA0; --ink:#1A1A1A; --tg:#41A486; --tg-d:#2B907F;
  --deep1:#0F4E57; --deep2:#08303A; --deep3:#03161B; --light:#F3F6F6; }}
* {{ margin:0; padding:0; box-sizing:border-box; }}
.sl {{ position:absolute; top:0; width:{W}px; height:{H}px; overflow:hidden; }}
.bg-aqua {{ background: {waves(.18)}, linear-gradient(140deg, var(--aqua-l) 0%, var(--aqua) 50%, var(--aqua-d) 100%); color:var(--ink); }}
.bg-teal {{ background: {waves(.16)}, linear-gradient(140deg, #5BBE9E 0%, var(--tg) 50%, var(--tg-d) 100%); color:var(--ink); }}
.bg-light {{ background: linear-gradient(180deg, #FFFFFF 0%, #EEF4F4 100%); color:var(--ink); }}
.acc {{ color: var(--aqua); }}
.bg-aqua .acc, .bg-teal .acc {{ color:#fff; }}
.sl > * {{ z-index:3; }} .sl > .ghost, .sl > .blob, .sl > .bok, .sl > .fnum, .sl > .back {{ z-index:1; }}
.layer {{ z-index:2; position:absolute; left:0; top:0; width:{W * n}px; height:{H}px; pointer-events:none; }}
.bok {{ position:absolute; border-radius:50%; filter: blur(6px); }}
.bg-dark {{ background: radial-gradient(38% 30% at 86% 14%, rgba(4,173,195,.38) 0%, rgba(4,173,195,0) 100%),
  radial-gradient(120% 90% at 78% 22%, var(--deep1) 0%, var(--deep2) 45%, var(--deep3) 100%); color:#fff; }}
.cnt {{ position:absolute; top:56px; left:64px; font: 600 20px/1 "Poppins"; padding: 9px 16px; border-radius: 999px; background: rgba(4,173,195,.18); color: var(--aqua); letter-spacing:.06em; }}
.bg-aqua .cnt, .bg-teal .cnt {{ background: rgba(26,26,26,.85); color:#fff; }} .bg-light .cnt {{ background: var(--ink); color:#fff; }}
.foot {{ position:absolute; bottom:50px; left:64px; font: 600 26px/1 "Poppins"; letter-spacing:.02em; opacity:.85; }}
.arw {{ position:absolute; right:56px; bottom:48px; width:46px; height:46px; border:2.5px solid currentColor; border-radius:10px; display:flex; align-items:center; justify-content:center; font: 700 24px/1 "Poppins"; opacity:.8; }}
.ghost {{ position:absolute; font: 700 760px/.8 "Poppins"; letter-spacing:-.06em; }}
.bg-dark .ghost, .bg-light .ghost {{ color: rgba(4,173,195,.10); }} .bg-aqua .ghost {{ color: rgba(255,255,255,.16); }}
.blob {{ position:absolute; background: radial-gradient(circle at 40% 35%, #0F4E57, #03161B 75%); border-radius: 46% 54% 48% 52% / 55% 45% 55% 45%; }}
.vword {{ position:absolute; font: 700 300px/1 "Poppins"; text-transform:uppercase; letter-spacing:-.03em; color:#fff; transform-origin: left top; transform: rotate(90deg); white-space:nowrap; }}
.chev {{ font: 700 40px/.6 "Poppins"; color: var(--aqua); text-align:center; }}
.icons {{ position:absolute; left:64px; right:64px; bottom:120px; display:flex; justify-content:space-between; font: 600 22px/1 "Poppins"; color:#fff; }}
.icons span {{ display:flex; align-items:center; gap:10px; }} .icons svg {{ width:30px; height:30px; }}
.big {{ font: 700 108px/.95 "Poppins"; text-transform: uppercase; letter-spacing:-.03em; }}
.hd {{ font-family:"Preahvihear"; font-size: 60px; line-height:1.13; }}
.bd {{ font: 500 29px/1.45 "Poppins"; }}
.bg-dark .bd {{ color:#C9D6D8; }} .bg-light .bd {{ color:#3D3D3D; }} .bg-aqua .bd, .bg-teal .bd {{ color: rgba(26,26,26,.85); }}
.wi {{ font: 600 29px/1.42 "Poppins"; margin-top: 24px; }}
.lab {{ font: 700 22px/1 "Poppins"; letter-spacing:.18em; text-transform:uppercase; color: var(--aqua); margin-bottom: 22px; }}
.bg-aqua .lab {{ color:#fff; }}
.res {{ display:flex; flex-direction:column; gap:12px; margin-top: 28px; }}
.res span {{ display:inline-flex; align-self:flex-start; align-items:center; gap:10px; font: 600 25px/1 "Poppins"; color:#fff; background: var(--aqua); padding: 12px 20px 12px 14px; border-radius: 999px; }}
.bg-aqua .res span {{ background: var(--ink); }}
.pill {{ display:inline-block; background: var(--aqua); color:#fff; font: 700 30px/1.3 "Poppins"; padding: 18px 34px; border-radius: 999px; }}
.row {{ display:flex; align-items:center; gap:16px; font: 600 31px/1.2 "Poppins"; color: var(--ink); padding: 18px 0; border-bottom: 2px solid rgba(26,26,26,.18); }}
.row i {{ width:42px; height:42px; flex:none; border-radius:50%; background: var(--aqua); display:flex; align-items:center; justify-content:center; }}
.stops {{ display:grid; grid-template-columns: 270px 270px; row-gap: 22px; font: 600 28px/1 "Poppins"; color: var(--ink); }}
.stops span {{ display:flex; align-items:center; gap:12px; }}
.stops b {{ display:inline-flex; width:52px; height:52px; border-radius:50%; background: var(--ink); color:#fff; align-items:center; justify-content:center; font-size: 24px; }}
.sz .hd {{ font-size:64px; }} .sz .bd {{ font-size:31px; }} .sz .wi {{ font-size:31px; }} .sz .res span {{ font-size:27px; }} .sz .row {{ font-size:33px; }}
.task .lab {{ font-size:28px; margin-bottom:24px; }}
.onblob {{ color:#fff; }} .onblob .bd {{ color:#C9D6D8; }} .onblob .acc {{ color: var(--aqua-l); }} .onblob .lab {{ color: var(--aqua-l); }} .onblob .res span {{ background: var(--aqua); }}
.airy .hd {{ line-height:1.28; }} .airy .bd {{ line-height:1.7; }} .airy .wi {{ line-height:1.66; margin-top:30px; }} .airy .res {{ margin-top:34px; }}
.fx {{ position:absolute; pointer-events:none; mix-blend-mode: screen; }}
html, body {{ width:{W}px; height:{H}px; overflow:hidden; background:#03161B; }}"""

# ---------- light effects ----------
def bokeh(n=16, seed=1, warm=True):
    out, s = [], seed
    for k in range(n):
        s = (s * 9301 + 49297) % 233280; r = s / 233280
        s = (s * 9301 + 49297) % 233280; r2 = s / 233280
        size = 10 + int(r * 34); col = "rgba(255,196,92,.35)" if (warm and k % 3 == 0) else "rgba(54,194,212,.28)"
        out.append(f'<div class="bok" style="left:{int(r2 * 1040)}px;top:{40 + int(((r * 7) % 1) * 1250)}px;width:{size}px;height:{size}px;background:{col}"></div>')
    return "".join(out)

def flare(x, y, s=1.0, ang=-18):
    """Lens flare: bright core, anamorphic streak, ghost rings along a diagonal."""
    c = int(300 * s)
    g = (f'<div class="fx back flc" style="left:{x - c // 2}px;top:{y - c // 2}px;width:{c}px;height:{c}px;border-radius:50%;'
         f'background: radial-gradient(circle, rgba(255,255,255,.95) 0%, rgba(205,250,255,.7) 7%, rgba(120,225,235,.28) 22%, rgba(4,173,195,0) 62%)"></div>'
         f'<div class="fx back fls" style="left:{x - int(650 * s)}px;top:{y - 3}px;width:{int(1300 * s)}px;height:6px;transform:rotate({ang / 6:.1f}deg);'
         f'background: linear-gradient(90deg, rgba(200,255,240,0), rgba(215,250,255,.75) 50%, rgba(200,255,240,0));filter:blur(1.5px)"></div>')
    for k, (d, r, a) in enumerate([(170, 36, .16), (300, 70, .10), (430, 22, .2), (560, 110, .07)]):
        gx, gy = x - int(d * s), y + int(d * s * .62)
        col = "190,245,255" if k % 2 else "200,255,230"
        g += (f'<div class="fx back flg" style="left:{gx - r}px;top:{gy - r}px;width:{2 * r}px;height:{2 * r}px;border-radius:50%;'
              f'background: radial-gradient(circle, rgba({col},{a}) 0%, rgba({col},{a * .6:.3f}) 60%, rgba({col},0) 72%);border:1px solid rgba({col},{a * .8:.3f})"></div>')
    return g

def streaks(seed=1, strength=1.0, ang=-24):
    """Soft diagonal light streaks in whitish-green / whitish-blue."""
    out, s = [], seed
    for k in range(6):
        s = (s * 9301 + 49297) % 233280; r = s / 233280
        y = 80 + int(r * 1150); thick = 40 + int(r * 120) if k % 2 == 0 else 2 + int(r * 3)
        col = "205,255,235" if k % 2 else "200,240,255"
        a = (.13 if thick > 10 else .32) * strength
        blur = 22 if thick > 10 else 1
        out.append(f'<div class="fx back" style="left:-300px;top:{y}px;width:1700px;height:{thick}px;transform:rotate({ang + (r - .5) * 8:.1f}deg);'
                   f'background: linear-gradient(90deg, rgba({col},0) 0%, rgba({col},{a:.2f}) 45%, rgba({col},0) 100%);filter:blur({blur}px)"></div>')
    return "".join(out)

SWEEP = ('<div class="fx back sweep" style="left:-200px;top:520px;width:520px;height:120px;transform:translateX(-2000px) rotate(-24deg);'
         'background:linear-gradient(90deg,rgba(210,255,240,0),rgba(225,255,250,.15) 50%,rgba(210,255,240,0));filter:blur(22px)"></div>')
STREAK_DEFAULT = {"dark": 1.0, "aqua": .9, "teal": .8}

# ---------- slide templates ----------
def t_cover(s, ctx):
    ax, ay = s.get("arrow", [600, 1030])
    return f"""
      <div class="big tx" style="position:absolute;left:56px;top:{s.get('big_top', 190)}px;width:640px">{acc(s['big'])}</div>
      <div class="hd tx" style="position:absolute;left:56px;top:{s.get('q_top', 665)}px;width:640px;font-size:{s.get('q_size', 56)}px">{esc(s['question'])}</div>
      <div class="bd tx" style="position:absolute;left:56px;top:{s.get('sub_top', 905)}px;width:520px">{esc(s['sub'])} <b style="color:var(--aqua)">{esc(s['swipe'])}</b></div>
      <svg style="position:absolute;left:{ax}px;top:{ay}px" width="300" height="160" viewBox="0 0 300 160"><path id="dash" d="M10 20 C 90 150, 200 150, 270 60" fill="none" stroke="#fff" stroke-width="4" stroke-dasharray="12 12" stroke-linecap="round"/><path id="dhead" d="M246 70 L270 60 L266 86" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/></svg>"""

def t_setup(s, ctx):
    stops = "".join(f'<span><b>{k + 1}</b> {esc(v)}</span>' for k, v in enumerate(s["stops"]))
    return f"""
      <div class="tx" style="position:absolute;left:{s.get('x', 150)}px;top:{s.get('y', 300)}px;width:{s.get('w', 660)}px">
        <div class="hd">{acc(s['headline'])}</div>
        <div class="bd" style="margin-top:26px">{esc(s['body'])}</div>
        <div class="lab" style="margin-top:44px">{esc(s['cue'])} &darr;</div>
        <div class="stops">{stops}</div></div>"""

def t_task(s, ctx):
    out = ""
    if s.get("blob"):
        l, t, w, h = s["blob"] if isinstance(s["blob"], list) else [250, 90, 1000, 1040]
        out += f'<div class="blob" style="left:{l}px;top:{t}px;width:{w}px;height:{h}px"></div>'
    g = s.get("ghost", {})
    if g is not None:
        side, off, top = g.get("side", "right"), g.get("offset", -60), g.get("top", 330)
        out += f'<div class="ghost" style="{side}:{off}px;top:{top}px">{esc(str(g.get("text", s["n"])))}</div>'
    cls = "onblob airy" if s.get("blob") else ""
    res = "".join(f'<span>{tick(22)}{esc(o)}</span>' for o in s["outcome"])
    out += (f'<div class="task tx {cls}" style="position:absolute;left:{s.get("x", 200)}px;top:{s.get("y", 240)}px;width:{s.get("w", 600)}px">'
            f'<div class="lab">{s["n"]}/{s["of"]} &middot; {esc(s["label"])}</div>'
            f'<div class="hd">{acc(s["headline"])}</div><div class="bd" style="margin-top:22px">{esc(s["pain"])}</div>'
            f'<div class="wi">{esc(s["whatif"])}</div><div class="res">{res}</div></div>')
    if s.get("giant"):
        out += f'<div class="back" style="position:absolute;left:-20px;bottom:120px;font:700 210px/.8 Poppins;letter-spacing:-.05em;color:var(--ink);white-space:nowrap">{esc(s["giant"])}</div>'
    return out

def t_reveal(s, ctx):
    gw = s.get("ghost_word")
    body = acc(s["body"]).replace('class="acc"', 'style="color:var(--aqua);font-weight:700"')
    return ((f'\n      <div class="back" style="position:absolute;left:-30px;top:120px;font:700 250px/.8 Poppins;letter-spacing:-.05em;color:rgba(4,173,195,.08);white-space:nowrap">{esc(gw)}</div>' if gw else "") + f"""
      <div class="logo" style="position:absolute;left:56px;top:150px;width:380px">{LOGO_SVG}</div>
      <div class="hd tx" style="position:absolute;left:56px;top:370px;width:660px;font-size:{s.get('hd_size', 55)}px">{acc(s['headline'])}</div>
      <div class="bd tx" style="position:absolute;left:56px;top:{s.get('body_top', 710)}px;width:640px;font-size:27.5px">{body}</div>
      <div class="tx" style="position:absolute;left:56px;top:{s.get('line_top', 1050)}px;width:760px;font-family:Preahvihear;font-size:36px;color:var(--aqua)">{esc(s['line'])}</div>
      <div class="bd tx" style="position:absolute;left:56px;top:{s.get('sign_top', 1112)}px;width:660px;font-size:23px;color:#9FB3B6">{esc(s['sign'])}</div>""")

def t_outcome(s, ctx):
    rows = "".join(f'<div class="row"><i>{tick(24)}</i>{esc(r)}</div>' for r in s["rows"])
    return f"""
      <div class="tx" style="position:absolute;left:{s.get('x', 400)}px;top:{s.get('y', 230)}px;width:{s.get('w', 630)}px">
        <div class="hd" style="font-size:{s.get('hd_size', 62)}px">{acc(s['headline'])}</div>
        <div style="margin-top:30px">{rows}</div>
        <div class="bd" style="margin-top:28px;font-weight:600;color:var(--ink)">{esc(s['closing'])}</div></div>"""

def t_cta(s, ctx):
    return f"""
      <div style="position:absolute;left:90px;right:90px;top:280px;text-align:center">
        <div class="hd tx" style="font-size:72px">{acc(s['headline'])}</div>
        <div class="chev" style="margin-top:34px">&#8964;<br>&#8964;</div>
        <div class="bd tx" style="margin:30px auto 0;width:760px">{esc(s['line'])}</div>
        <div style="margin-top:56px"><span class="pill" id="dm">{esc(s['main'])}</span></div>
        <div class="bd tx" style="margin:26px auto 0;width:760px;font-size:28px;color:#B9CBCE">{esc(s['save'])}</div></div>
      <div class="icons tx"><span>{ICON_HEART}Like the post</span><span>{ICON_CHAT}Leave a comment</span><span>{ICON_SAVE}Save &amp; share it</span></div>"""

TEMPLATES = {"cover": t_cover, "setup": t_setup, "task": t_task, "reveal": t_reveal, "outcome": t_outcome, "cta": t_cta}

# ---------- 3D objects ----------
FLAME = ('<div class="flame" style="position:absolute;left:{x:.1f}%;top:{y:.1f}%;width:46px;height:46px;margin:-23px 0 0 -23px;border-radius:50%;'
         'background:radial-gradient(circle,rgba(255,236,170,.95) 0%,rgba(255,180,70,.55) 35%,rgba(255,150,40,0) 70%);mix-blend-mode:screen"></div>')

def object_html(o, sx, img_dir, project):
    """Returns (html for the layer, extra html appended after everything: canvases / bubble layers)."""
    src = project / "images" / "cut" / o["image"]
    iw, ih = Image.open(src).size; w = o["w"]; h = w * ih / iw
    x, y = sx + o["x"], o["y"]
    m = o.get("moment", {"type": "none"}); mt = m.get("type", "none")
    glow = ("drop-shadow(0 0 34px rgba(4,173,195,.55)) drop-shadow(0 40px 36px rgba(0,0,0,.55))" if o.get("glow")
            else "drop-shadow(0 34px 30px rgba(0,0,0,.28))")
    data = f' data-rot="{o.get("rot", 0)}" data-ph="{o.get("ph", 0.0)}"' + ('' if o.get("float", True) else ' data-float="0"')
    inner, after = "", ""
    if mt == "drive":
        data += f" data-drive='{json.dumps({'dx': m.get('dx', 80), 'at': m.get('at', 0.3), 'dur': m.get('dur', 2.3)})}'"
    elif mt == "blink":
        l, t, bw, bh = m["box"]
        inner = (f'<div class="blink" style="position:absolute;left:{l * 100:g}%;top:{t * 100:g}%;width:{bw * 100:g}%;height:{bh * 100:g}%;border-radius:6px;'
                 f'background:rgba(54,194,212,.9);box-shadow:0 0 18px 6px rgba(54,194,212,.8);opacity:0"></div>')
    elif mt == "flicker":
        inner = "".join(FLAME.format(x=px * 100, y=py * 100) for px, py in m["points"])
    elif mt == "topple":
        g = json.loads((project / "images" / "cut" / m["geom"]).read_text(encoding="utf-8")); k = w / g["src"]["w"]
        b, l = g["body"], g["lid"]; pvx, pvy = g["pivot"]
        inner = (f'<div class="topple" data-angle="{m.get("angle", -85)}" data-at="{m.get("at", 0.75)}" data-foreshorten="{m.get("foreshorten", 0.72)}" '
                 f'style="position:absolute;left:0;top:0;width:100%;height:100%;transform-origin:{pvx * k:.1f}px {pvy * k:.1f}px">'
                 f'<img class="tp-body" src="{img_dir}{m["body"]}" style="position:absolute;left:{b["x"] * k:.1f}px;top:{b["y"] * k:.1f}px;width:{b["w"] * k:.1f}px">'
                 f'<img class="tp-lid" src="{img_dir}{m["lid"]}" style="position:absolute;left:{l["x"] * k:.1f}px;top:{l["y"] * k:.1f}px;width:{l["w"] * k:.1f}px;transform-origin:50% 50%"></div>')
    elif mt == "sparks":
        cx, cy = x - 400, y - 400
        em = [[400 + px * w, 400 + py * h] for px, py in m["points"]]
        after = f"<canvas class=\"sparks\" data-em='{json.dumps(em)}' data-ph=\"{o.get('ph', 0.0)}\" width=\"{int(w) + 800}\" height=\"{int(h) + 800}\" style=\"position:absolute;left:{cx}px;top:{cy}px\"></canvas>"
    elif mt == "bubbles":
        ox, oy = m["origin"]
        after = f'<div class="bubbles" data-x="{x + ox * w:.2f}" data-y="{y + oy * h:.2f}" data-ph="{o.get("ph", 0.0)}" style="position:absolute;left:0;top:0"></div>'
    div = (f'<div class="flt" id="o-{o["id"]}"{data} style="position:absolute;left:{x}px;top:{y}px;width:{w}px;transform:rotate({o.get("rot", 0)}deg)">'
           f'<img src="{img_dir}{o["image"]}" style="display:block;width:100%;filter:{glow}">{inner}</div>')
    return div, after

# ---------- motion (one timeline, the same on every slide) ----------
JS = r"""
const TAU = Math.PI * 2, cl = v => Math.max(0, Math.min(1, v)), eio = v => v < .5 ? 2 * v * v : 1 - Math.pow(-2 * v + 2, 2) / 2;
const Q = s => [...document.querySelectorAll(s)];
const FLT = Q('.flt').map(e => ({ e, rot: +e.dataset.rot, ph: +e.dataset.ph, fl: e.dataset.float !== '0', drive: e.dataset.drive ? JSON.parse(e.dataset.drive) : null }));
const FLC = Q('.flc'), FLS = Q('.fls').map(e => ({ e, bt: e.style.transform })), FLG = Q('.flg'), SW = Q('.sweep'), BOK = Q('.bok');
const ARW = Q('.arw').map(e => ({ e, col: e.closest('.bg-aqua, .bg-teal') ? '255,255,255' : '4,173,195' }));
const CK = []; Q('.sl').forEach(sl => sl.querySelectorAll('.ck').forEach((p, j) => { p.style.strokeDasharray = 30; CK.push({ p, t0: 0.7 + j * 0.22 }); }));
const STP = Q('.stops b').map((b, k) => { b.style.position = 'relative'; const r = document.createElement('i');
  r.style.cssText = 'position:absolute;left:-5px;top:-5px;right:-5px;bottom:-5px;border-radius:50%;border:3px solid #fff;opacity:0'; b.appendChild(r); return { b, r, t0: 0.5 + k * 0.45 }; });
const DASH = document.getElementById('dash'), DHEAD = document.getElementById('dhead'), DM = document.getElementById('dm');
const FLM = Q('.flame'), BLINK = Q('.blink');
let seed = 7; const rnd = () => (seed = (seed * 16807) % 2147483647) / 2147483647;
// sparks: emitters in canvas pixels, particles are a pure function of t (seek-safe)
const SPK = Q('canvas.sparks').map(c => { const em = JSON.parse(c.dataset.em), parts = [];
  em.forEach((p, ei) => { for (let k = 0; k < 70; k++) parts.push({ ei, b: (k / 70) * 4 + rnd() * 0.05, life: 0.55 + rnd() * 0.5,
    a: -Math.PI / 2 + (rnd() - 0.5) * 2.6, sp: 150 + rnd() * 230, w: 1.5 + rnd() * 2 }); });
  return { c, x: c.getContext('2d'), em, parts, ph: +c.dataset.ph }; });
// bubbles: speech bubbles born at a point on the object, drifting right and up
const BCOL = ['#36C2D4', '#FFFFFF', '#5BBE9E', '#04ADC3', '#E6FAFC', '#41A486', '#36C2D4', '#FFFFFF', '#5BBE9E'];
const BUBS = Q('.bubbles').map(L => ({ x: +L.dataset.x, y: +L.dataset.y, ph: +L.dataset.ph, bs: BCOL.map((c, k) => { const d = document.createElement('div'); const s = 34 + (k * 13) % 30;
  d.style.cssText = `position:absolute;left:0;top:0;width:${s}px;height:${s * 0.8}px;border-radius:50% 50% 50% 14%;background:${c};box-shadow:0 8px 16px rgba(0,0,0,.18);opacity:0`;
  L.appendChild(d); return { d, b: k * 4 / 9, dx: 200 + (k * 71) % 240, dy: -40 - (k * 53) % 200 }; }) }));
const TOP = Q('.topple').map(e => ({ e, lid: e.querySelector('.tp-lid'), ang: +e.dataset.angle, at: +e.dataset.at, fs: +e.dataset.foreshorten }));
const hands = document.getElementById('hands');

function fy(ph, t) { return 7 * Math.sin(TAU * t / 4 + ph); }
function R(t) {
  FLT.forEach(o => {
    let x = 0, y = fy(o.ph, t), r = o.rot + 0.6 * Math.sin(TAU * t / 4 + o.ph + 1.2);
    if (!o.fl) { y = 0; r = o.rot; }
    if (o.drive) { x = o.drive.dx * eio(cl((t - o.drive.at) / o.drive.dur)); r = o.rot + 0.25 * Math.sin(TAU * t * 2); }
    o.e.style.transform = `translate(${x}px, ${y}px) rotate(${r}deg)`;
  });
  FLC.forEach((e, k) => { e.style.transform = `scale(${1 + 0.08 * Math.sin(TAU * t / 2 + k)})`; e.style.opacity = 0.8 + 0.2 * Math.sin(TAU * t / 2 + k + 1); });
  FLS.forEach((o, k) => { o.e.style.transform = `${o.bt} translateX(${28 * Math.sin(TAU * t / 4 + k)}px)`; o.e.style.opacity = 0.7 + 0.3 * Math.sin(TAU * t / 2 + k); });
  FLG.forEach((e, k) => { e.style.opacity = 0.55 + 0.45 * Math.sin(TAU * t / 4 + k * 0.9); });
  SW.forEach((e, k) => { const a = (t - 0.5 - (k % 3) * 0.15) / 1.9;
    const x = a <= 0 ? -2400 : a >= 1 ? 2400 : -1500 + 3000 * eio(a); e.style.transform = `translate(${x}px, ${-x * 0.45}px) rotate(-24deg)`; });
  BOK.forEach((e, k) => { e.style.opacity = 0.35 + 0.65 * (0.5 + 0.5 * Math.sin(TAU * t / (1.2 + (k % 4) * 0.35) + k * 1.7)); });
  const g = 0.5 - 0.5 * Math.cos(TAU * t / 2);
  ARW.forEach(o => { o.e.style.boxShadow = `0 0 ${6 + 24 * g}px ${1 + 7 * g}px rgba(${o.col},${0.25 + 0.6 * g})`; });
  if (DM) DM.style.boxShadow = `0 0 ${12 + 34 * g}px ${2 + 9 * g}px rgba(54,194,212,${0.3 + 0.5 * g})`;
  CK.forEach(o => { o.p.style.strokeDashoffset = 30 * (1 - eio(cl((t - o.t0) / 0.3))); });
  STP.forEach(o => { const on = t >= o.t0, a = cl((t - o.t0) / 0.7);
    o.b.style.background = on ? '#FFFFFF' : '#1A1A1A'; o.b.style.color = on ? '#1A1A1A' : '#FFFFFF';
    o.r.style.opacity = on ? (1 - a) * 0.9 : 0; o.r.style.transform = `scale(${1 + a * 0.9})`; });
  if (DASH) { DASH.style.strokeDashoffset = -t * 36;
    const n = 5 * Math.pow(Math.max(0, Math.sin(TAU * t)), 2); DHEAD.setAttribute('transform', `translate(${0.614 * n} ${-0.789 * n})`); }
  BLINK.forEach(e => { let o = t > 2.65 ? 0.85 : 0; [0.9, 1.4, 1.9, 2.4].forEach(v => { if (t >= v && t < v + 0.25) o = 1; }); e.style.opacity = o; });
  FLM.forEach((e, k) => { e.style.transform = `scale(${1 + 0.14 * Math.sin(TAU * t * 3.1 + k) + 0.08 * Math.sin(TAU * t * 5.3 + k * 2)})`;
    e.style.opacity = 0.7 + 0.3 * Math.sin(TAU * t * 4.2 + k * 1.3); });
  SPK.forEach(S => { const SX = S.x; SX.setTransform(1, 0, 0, 1, 0, 0); SX.clearRect(0, 0, S.c.width, S.c.height); SX.globalCompositeOperation = 'lighter';
    const ty = fy(S.ph, t);
    S.parts.forEach(p => { const age = (((t - p.b) % 4) + 4) % 4; if (age >= p.life) return;
      const [ex, ey] = S.em[p.ei], vx = Math.cos(p.a) * p.sp, vy = Math.sin(p.a) * p.sp, a0 = Math.max(0, age - 0.05);
      const x1 = ex + vx * age, y1 = ey + ty + vy * age + 190 * age * age, x0 = ex + vx * a0, y0 = ey + ty + vy * a0 + 190 * a0 * a0;
      const f = 1 - age / p.life; SX.strokeStyle = `rgba(255,${200 + 55 * f | 0},${120 + 120 * f | 0},${f})`; SX.lineWidth = p.w;
      SX.beginPath(); SX.moveTo(x0, y0); SX.lineTo(x1, y1); SX.stroke(); });
    S.em.forEach(([ex, ey], k) => { const r = 16 + 6 * Math.sin(TAU * t * 6 + k); const gr = SX.createRadialGradient(ex, ey + ty, 0, ex, ey + ty, r);
      gr.addColorStop(0, 'rgba(255,250,220,.95)'); gr.addColorStop(1, 'rgba(255,190,80,0)'); SX.fillStyle = gr; SX.beginPath(); SX.arc(ex, ey + ty, r, 0, TAU); SX.fill(); });
    SX.globalCompositeOperation = 'source-over'; });
  BUBS.forEach(B => { const py = fy(B.ph, t);
    B.bs.forEach(o => { const age = (((t - o.b) % 4) + 4) % 4, L = 1.9; if (age >= L) { o.d.style.opacity = 0; return; }
      const a = age / L, s = 0.3 + 0.7 * eio(cl(age / 0.35)), x = B.x + o.dx * eio(a), y = B.y + py + o.dy * a;
      o.d.style.opacity = Math.min(cl(age / 0.15), cl((L - age) / 0.4)); o.d.style.transform = `translate(${x}px, ${y}px) scale(${s})`; }); });
  TOP.forEach(T => { const t0 = T.at; let a = 0;   /* teeter, fall, land on its side (foreshortened), lid pops off and rolls away */
    if (t >= t0 - 0.3 && t < t0) a = (T.ang < 0 ? -5 : 5) * Math.sin(Math.PI * (t - t0 + 0.3) / 0.3);
    else if (t >= t0 && t < t0 + 0.45) { const u = (t - t0) / 0.45; a = T.ang * u * u; }
    else if (t >= t0 + 0.45) { const u = t - t0 - 0.45; a = T.ang - Math.sign(T.ang) * 8 * Math.exp(-6 * u) * Math.abs(Math.sin(13 * u)); }
    const sy = 1 - (1 - T.fs) * cl((t - t0) / 0.45);
    T.e.style.transform = `rotate(${a}deg) scaleY(${sy})`;
    const tau = t - t0 - 0.47;
    if (tau <= 0) T.lid.style.transform = '';
    else { const pop = 24 * eio(cl(tau / 0.18)), tf = Math.max(0, tau - 0.12), dx = Math.sign(T.ang) * 80 * tau, dy = 0.5 * 1500 * tf * tf, q = -a * Math.PI / 180;
      const lx = dx * Math.cos(q) - dy * Math.sin(q), ly = dx * Math.sin(q) + dy * Math.cos(q);
      T.lid.style.transform = `translate(${lx}px, ${ly / sy - pop}px) rotate(${Math.sign(T.ang) * 520 * tau}deg)`; } });
}
"""

HANDS = """(() => { if (!hands) return; const o = hands.dataset.origin;
  tl.fromTo(hands, { rotation: -42, svgOrigin: o }, { rotation: 0, svgOrigin: o, duration: 2.6, ease: "sine.inOut" }, 0.5); })();"""

def page(i, sid, strip, style):
    x0 = (i - 1) * W; n = strip[1]
    return f"""<!doctype html>
<html lang="en"><head><meta charset="UTF-8" /><meta name="viewport" content="width=1080, height=1350" />
<script src="assets/gsap.min.js"></script>
<style>{style}</style></head>
<body>
<div id="root" data-composition-id="{sid}" data-start="0" data-duration="{DUR}" data-width="1080" data-height="1350" data-fps="30">
  <div id="s" class="clip" data-start="0" data-duration="{DUR}" style="position:absolute;left:0;top:0;width:1080px;height:1350px;overflow:hidden">
    <div id="strip" style="position:absolute;left:-{x0}px;top:0;width:{W * n}px;height:1350px">{strip[0]}</div>
  </div>
</div>
<script>
const SLIDE = {i};
{JS}
window.__timelines = window.__timelines || {{}};
const tl = gsap.timeline({{ paused: true }});
const st = {{ t: 0 }};
tl.to(st, {{ t: {DUR}, duration: {DUR}, ease: "none", onUpdate: () => R(st.t) }}, 0);
{HANDS}
R(0);
window.__timelines["{sid}"] = tl;
</script>
</body></html>"""

def build_strip(project, c, img_dir="assets/img/"):
    slides, n = c["slides"], len(c["slides"])
    pal = c.get("palette") or (["dark", "aqua", "light", "aqua", "light", "dark", "dark", "teal", "dark"] * 2)[:n]
    pages, over, after = [], [], []
    for i, s in enumerate(slides, 1):
        bg, tpl = pal[i - 1], s["template"]; sx = (i - 1) * W
        fx = ""
        if bg != "light":
            seed, strength = s.get("streaks", [4 * i - 1, STREAK_DEFAULT[bg]])
            fx += streaks(seed, strength)
        if s.get("flare"): fx += flare(*s["flare"])
        sz = "" if tpl in ("cover", "cta") else " sz"
        inner = TEMPLATES[tpl](s, c)
        pages.append(f'<div class="sl bg-{bg}{sz}" style="left:{sx}px">{bokeh(16, i, c.get("warm_bokeh", True)) if bg == "dark" else ""}{fx}{"" if bg == "light" else SWEEP}{inner}'
                     f'<div class="cnt">{i:02d}/{n:02d}</div><div class="foot">{esc(c["handle"])}</div>{"<div class=arw>&rarr;</div>" if i < n else ""}</div>')
        if tpl == "setup" and s.get("vword"):   # giant vertical word across the edge into the next slide
            v = s["vword"]
            over.append(f'<div class="bg-{bg}" style="position:absolute;left:{sx + W}px;top:0;width:150px;height:{H}px"></div>'
                        f'<div class="vword" style="left:{sx + W + 150}px;top:{v.get("top", 130)}px">{esc(v["text"])}</div>')
        for o in c.get("objects", []):
            if o["slide"] == i:
                d, a = object_html(o, sx, img_dir, project); over.append(d); after.append(a)
    return "".join(pages) + f'<div class="layer">{"".join(over)}{"".join(after)}</div>', n

def main(project):
    project = pathlib.Path(project).resolve()
    c = json.loads((project / "content.json").read_text(encoding="utf-8"))
    out = project / "slides"; out.mkdir(exist_ok=True)
    if not (KIT / "gsap.min.js").exists() or not (KIT / "fonts" / "Poppins-Bold.ttf").exists():
        sys.exit("Missing fonts or GSAP: run python scripts/setup_assets.py first.")
    shutil.copytree(KIT / "fonts", out / "assets" / "fonts", dirs_exist_ok=True)
    shutil.copyfile(KIT / "gsap.min.js", out / "assets" / "gsap.min.js")
    shutil.copytree(project / "images" / "cut", out / "assets" / "img", dirs_exist_ok=True)
    strip = build_strip(project, c); style = css(strip[1]); slug = project.name.lower().replace(" ", "-")[:40]
    for i in range(1, strip[1] + 1):
        (out / f"slide-{i:02d}.html").write_text(page(i, f"{slug}-s2-{i:02d}", strip, style), encoding="utf-8")
    print(f"built {strip[1]} slides in {out}")

if __name__ == "__main__":
    if len(sys.argv) < 2: sys.exit(__doc__)
    main(sys.argv[1])
~~~~
<!-- END FILE -->

---

### `scripts/stills.py`

<!-- FILE: scripts/stills.py code -->
~~~~python
"""Stills + layout checks for every slide (needs the slides from build.py).

Usage: python stills.py <project> [--t 3.0]
- stills/slide-NN.png at t (default 3.0 s; a slide can set "still_t" in content.json), and preview-all-slides.jpg.
- proof/textboxes.json: where the text sits on each slide (render.py uses it to prove text never moves).
- Prints one line per slide: OK, or what to fix:
    fonts not loaded | text outside the safe area | two text blocks overlap | text under a 3D object (warning only)
"""
import json, pathlib, sys
from playwright.sync_api import sync_playwright
from PIL import Image

PROBE = """() => {
  const vis = r => r.right > 0 && r.left < 1080 && r.width > 0;
  const tx = [...document.querySelectorAll('.tx')].map(e => e.getBoundingClientRect()).filter(vis)
    .map(r => [Math.round(r.left), Math.round(r.top), Math.round(r.right), Math.round(r.bottom)]);
  const ob = [...document.querySelectorAll('.flt img:first-child')].map(e => e.getBoundingClientRect()).filter(vis)
    .map(r => [Math.round(r.left), Math.round(r.top), Math.round(r.right), Math.round(r.bottom)]);
  return { tx, ob, fonts: document.fonts.check('40px Preahvihear') && document.fonts.check('700 40px Poppins') };
}"""

def inter(a, b, slack=8):
    """Overlap area of two boxes, ignoring overlaps thinner than `slack` px (line-height padding, not real collisions)."""
    w, h = min(a[2], b[2]) - max(a[0], b[0]), min(a[3], b[3]) - max(a[1], b[1])
    return w * h if w > slack and h > slack else 0

def main(project, t_default=3.0):
    project = pathlib.Path(project).resolve(); c = json.loads((project / "content.json").read_text(encoding="utf-8"))
    out = project / "stills"; out.mkdir(exist_ok=True); (project / "proof").mkdir(exist_ok=True)
    boxes, bad = {}, 0
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1080, "height": 1350}); errs = []
        pg.on("pageerror", lambda e: errs.append(str(e)))
        for i, s in enumerate(c["slides"], 1):
            n = f"{i:02d}"; pg.goto((project / "slides" / f"slide-{n}.html").as_uri(), wait_until="load")
            pg.evaluate("document.fonts.ready.then(() => 1)")
            t = s.get("still_t", t_default)
            pg.evaluate(f"(() => {{ const k = document.querySelector('[data-composition-id]').dataset.compositionId; window.__timelines[k].seek({t}, false); }})(); 0")
            pg.wait_for_timeout(80); pg.screenshot(path=str(out / f"slide-{n}.png"))
            r = pg.evaluate(PROBE); boxes[n] = r["tx"]; issues = []
            if not r["fonts"]: issues.append("fonts not loaded")
            for bx in r["tx"]:
                if bx[0] < 40 or bx[2] > 1050 or bx[1] < 40 or bx[3] > 1250: issues.append(f"text outside the safe area {bx}")
            for k, a in enumerate(r["tx"]):
                for b2 in r["tx"][k + 1:]:
                    if inter(a, b2) > 200: issues.append(f"text blocks overlap {a} {b2}")
            warn = [f"text under a 3D object {a}" for a in r["tx"] for o in r["ob"] if inter(a, o) > 0.08 * (a[2] - a[0]) * (a[3] - a[1])]
            bad += bool(issues)
            print(n, "OK" if not issues else "FIX: " + "; ".join(issues), ("| check: " + "; ".join(warn)) if warn else "")
        b.close()
    if errs: print("page errors:", errs[:3]); bad += 1
    (project / "proof" / "textboxes.json").write_text(json.dumps(boxes), encoding="utf-8")
    ims = [Image.open(out / f"slide-{i:02d}.png").convert("RGB").resize((360, 450)) for i in range(1, len(c["slides"]) + 1)]
    sheet = Image.new("RGB", (360 * len(ims), 450)); [sheet.paste(im, (k * 360, 0)) for k, im in enumerate(ims)]
    sheet.save(project / "preview-all-slides.jpg", quality=90)
    print("stills in", out, "| preview-all-slides.jpg written"); return 1 if bad else 0

if __name__ == "__main__":
    if len(sys.argv) < 2: sys.exit(__doc__)
    sys.exit(main(sys.argv[1], float(sys.argv[sys.argv.index("--t") + 1]) if "--t" in sys.argv else 3.0))
~~~~
<!-- END FILE -->

---

### `scripts/frames.py`

<!-- FILE: scripts/frames.py code -->
~~~~python
"""Frame sheets: each slide at t = 0, 0.8, 1.6, 2.4, 3.2, 3.9 s, to check the motion before rendering.

Usage: python frames.py <project> [01,04]        -> <project>/proof/frames-NN.jpg
Optional zoom: python frames.py <project> 04 --zoom 380,1000,1080,1350 --times 0.6,0.95,1.2,1.4,1.6,2.0
"""
import pathlib, sys
from playwright.sync_api import sync_playwright
from PIL import Image, ImageDraw

def main(project, nums=None, times=(0, 0.8, 1.6, 2.4, 3.2, 3.9), zoom=None):
    project = pathlib.Path(project).resolve(); proof = project / "proof"; proof.mkdir(exist_ok=True)
    nums = nums or sorted(f.stem.split("-")[1] for f in (project / "slides").glob("slide-*.html"))
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1080, "height": 1350}); errs = []
        pg.on("pageerror", lambda e: errs.append(str(e)))
        for n in nums:
            pg.goto((project / "slides" / f"slide-{n}.html").as_uri(), wait_until="load"); pg.evaluate("document.fonts.ready.then(() => 1)")
            tiles = []
            for t in times:
                pg.evaluate(f"(() => {{ const k = document.querySelector('[data-composition-id]').dataset.compositionId; window.__timelines[k].seek({t}, false); }})(); 0")
                pg.wait_for_timeout(60); f = proof / "_f.png"; pg.screenshot(path=str(f))
                im = Image.open(f).convert("RGB"); im = im.crop(zoom) if zoom else im.resize((360, 450)); tiles.append(im)
            w, h = tiles[0].size; s = Image.new("RGB", (len(tiles) * (w + 10) + 10, h + 30), "#202426"); d = ImageDraw.Draw(s)
            for k, (t, im) in enumerate(zip(times, tiles)): s.paste(im, (10 + k * (w + 10), 30)); d.text((14 + k * (w + 10), 8), f"slide {n}  t={t}s", fill="white")
            s.save(proof / f"{'zoom' if zoom else 'frames'}-{n}.jpg", quality=90)
        (proof / "_f.png").unlink(missing_ok=True); b.close()
    print("sheets in", proof, "| page errors:", errs[:3] or "none")

if __name__ == "__main__":
    if len(sys.argv) < 2: sys.exit(__doc__)
    a = sys.argv; nums = a[2].split(",") if len(a) > 2 and not a[2].startswith("--") else None
    zoom = tuple(int(v) for v in a[a.index("--zoom") + 1].split(",")) if "--zoom" in a else None
    times = tuple(float(v) for v in a[a.index("--times") + 1].split(",")) if "--times" in a else (0, 0.8, 1.6, 2.4, 3.2, 3.9)
    main(a[1], nums, times, zoom)
~~~~
<!-- END FILE -->

---

### `scripts/render.py`

<!-- FILE: scripts/render.py code -->
~~~~python
"""Lint, render and verify the MP4 for every slide (HyperFrames + GSAP, 4 s, 1080x1350, 30 fps).

Usage: python render.py <project> [01,02,...]
Needs: Node (npx), ffmpeg/ffprobe on the PATH, and proof/textboxes.json from stills.py (run stills.py first).
HyperFrames wants ONE root composition per folder, so each slide is copied in turn to <project>/render/index.html.
Prints per slide: lint errors, size, fps, duration, and text-moved: changed pixels inside the text blocks between
2.8 s and 3.9 s (after the tick marks and the light sweep have finished). It must be 0-30 (light flicker under text);
more means something is moving over or with the text.
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
    tb = project / "proof" / "textboxes.json"
    boxes = json.loads(tb.read_text(encoding="utf-8")) if tb.exists() else {}
    if not boxes: print("note: run stills.py first so the text check knows where the text is")
    r = project / "render"; (r / "out").mkdir(parents=True, exist_ok=True)
    for f in ["package.json", "hyperframes.json"]: shutil.copyfile(SKILL / "assets" / "render" / f, r / f)
    (r / "meta.json").write_text(json.dumps({"id": project.name, "name": project.name}), encoding="utf-8")
    shutil.rmtree(r / "assets", ignore_errors=True); shutil.copytree(project / "slides" / "assets", r / "assets")
    slides = sorted((project / "slides").glob("slide-*.html"))
    if nums: slides = [s for s in slides if s.stem.split("-")[1] in nums]
    bad = 0
    for s in slides:
        n = s.stem.split("-")[1]; shutil.copyfile(s, r / "index.html")
        lo = sh(f"{HF} lint", r); m = re.search(r"(\d+) error\(s\)", lo.stdout + lo.stderr); errs = int(m.group(1)) if m else -1
        mp4 = r / "out" / f"slide-{n}.mp4"; mp4.unlink(missing_ok=True)
        rr = sh(f'{HF} render --quality delivery --fps 30 --output "out/slide-{n}.mp4"', r)
        if not mp4.exists(): print(n, "RENDER FAILED:", (rr.stdout + rr.stderr)[-400:]); bad += 1; continue
        probe = sh(f'ffprobe -v error -show_entries stream=width,height,r_frame_rate:format=duration -of csv=p=0 "{mp4}"', r).stdout.split()
        d = ImageChops.difference(frame(mp4, 2.8, r / "_a.png"), frame(mp4, 3.9, r / "_b.png")).point(lambda v: 255 if v > 40 else 0)
        moved = max([d.crop(tuple(b)).histogram()[255] for b in boxes.get(n, [])] or [0])
        ok = errs == 0 and probe[:2] == ["1080,1350,30/1", "4.000000"] and moved <= 30
        bad += 0 if ok else 1
        print(n, f"lint={errs} errors", " ".join(probe), f"text-moved={moved}", "OK" if ok else "CHECK")
    for t in ["_a.png", "_b.png"]: (r / t).unlink(missing_ok=True)
    return 1 if bad else 0

if __name__ == "__main__":
    if len(sys.argv) < 2: sys.exit(__doc__)
    sys.exit(main(sys.argv[1], sys.argv[2].split(",") if len(sys.argv) > 2 else None))
~~~~
<!-- END FILE -->

---

### `scripts/publish.py`

<!-- FILE: scripts/publish.py code -->
~~~~python
"""Copy the finished Style 2 deliverables into one folder (any folder the user chooses).

Usage: python publish.py <project_dir> <dest_dir> [--archive-as v2-something]
Copies render/out/*.mp4 -> dest/motion/, stills/*.png -> dest/stills/, preview-all-slides.jpg, content.json,
images/cut/* + images/PROMPTS.md -> dest/images/. If dest already exists and --archive-as is given, the old folder is
renamed to <dest>-<tag> first (nothing is deleted); without it, files are overwritten.
Never copies API keys or anything outside the project. Prints every file it wrote.
"""
import argparse, pathlib, shutil

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("project"); ap.add_argument("dest"); ap.add_argument("--archive-as", default="")
    a = ap.parse_args(); p, d = pathlib.Path(a.project), pathlib.Path(a.dest)
    mp4s = sorted((p / "render" / "out").glob("slide-*.mp4"))
    if not mp4s: raise SystemExit("No MP4s in render/out: run render.py first.")
    if d.exists() and a.archive_as:
        old = d.with_name(f"{d.name}-{a.archive_as}")
        if old.exists(): raise SystemExit(f"{old} already exists: choose another --archive-as tag.")
        d.rename(old); print("archived the previous version as", old)
    for sub in ["motion", "stills", "images"]: (d / sub).mkdir(parents=True, exist_ok=True)
    for f in mp4s: shutil.copyfile(f, d / "motion" / f.name)
    for f in sorted((p / "stills").glob("slide-*.png")): shutil.copyfile(f, d / "stills" / f.name)
    for f in sorted((p / "images" / "cut").glob("*")): shutil.copyfile(f, d / "images" / f.name)
    for f in [p / "images" / "PROMPTS.md"]:
        if f.exists(): shutil.copyfile(f, d / "images" / f.name)
    for f in [p / "preview-all-slides.jpg", p / "content.json"]:
        if f.exists(): shutil.copyfile(f, d / f.name)
    for f in sorted(d.rglob("*")):
        if f.is_file(): print(f.relative_to(d), f"{f.stat().st_size / 1024:.0f} KB")

if __name__ == "__main__":
    main()
~~~~
<!-- END FILE -->

---

### `scripts/make_single_file.py`

<!-- FILE: scripts/make_single_file.py code -->
~~~~python
"""Bundle this skill folder into ONE self-contained markdown file: ART-carousel-design-style2.md.

Usage: python make_single_file.py [output_path]
The file = SKILL.md (instructions) + every reference, script and kit text file as marked blocks.
Fonts, GSAP (downloaded by setup_assets.py) and the example's 3D images are not embedded.
Anyone can unpack the file back into this folder layout with the snippet printed in its "Unpack" section.
"""
import pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
TEXT = ["references/design-language.md", "references/motion.md", "references/images.md", "references/copy-rules.md",
        "scripts/setup_assets.py", "scripts/new_project.py", "scripts/gen_images.py", "scripts/cutout.py", "scripts/split_prop.py",
        "scripts/build.py", "scripts/stills.py", "scripts/frames.py", "scripts/render.py", "scripts/publish.py", "scripts/make_single_file.py",
        "assets/render/package.json", "assets/render/hyperframes.json", "assets/example/content.json", "assets/example/PROMPTS.md",
        "assets/example/img/03-tin.json", "assets/kit/brand/logo-art.svg"]
FENCE = "~~~~"   # tilde fences never collide with backticks inside the code

UNPACK = r'''
## Unpack

Run this once with Python 3, in the folder where you saved this file. It rebuilds the full skill folder
(`ART-carousel-design-style2/`) next to it, then run `python ART-carousel-design-style2/scripts/setup_assets.py`.

~~~~python
import pathlib, re
src = pathlib.Path("ART-carousel-design-style2.md").read_text(encoding="utf-8")
out = pathlib.Path("ART-carousel-design-style2")
out.mkdir(exist_ok=True)
(out / "SKILL.md").write_text(src.split("<!-- END SKILL -->")[0].rstrip() + "\n", encoding="utf-8")
for path, kind, body in re.findall(r"<!-- FILE: (\S+) (text|code) -->\n(.*?)\n<!-- END FILE -->", src, re.S):
    f = out / path; f.parent.mkdir(parents=True, exist_ok=True)
    if kind == "code": body = body.split("\n", 1)[1].rsplit("\n", 1)[0]          # strip the ~~~~ fences
    f.write_text(body + "\n", encoding="utf-8")
    print("wrote", f)
~~~~
'''

def lang(p):
    return {".py": "python", ".js": "javascript", ".css": "css", ".json": "json", ".svg": "xml"}.get(pathlib.Path(p).suffix, "")

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
    pathlib.Path(out).write_text("".join(parts), encoding="utf-8")
    print("wrote", out, f"{pathlib.Path(out).stat().st_size / 1024:.0f} KB")

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else str(ROOT.parent / "ART-carousel-design-style2.md"))
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

### `assets/example/content.json`

<!-- FILE: assets/example/content.json code -->
~~~~json
{
  "title": "Festive season orders are coming. Your dispatch already keeps up. What if it got even simpler?",
  "handle": "@arealtimetech",
  "palette": ["dark", "aqua", "light", "aqua", "light", "dark", "dark", "teal", "dark"],
  "warm_bokeh": true,
  "slides": [
    {
      "template": "cover",
      "big": "**Festive season orders** are coming.",
      "question": "Your dispatch already keeps up. What if it got even simpler?",
      "sub": "Festive orders don't wait for anyone.",
      "swipe": "Swipe to see where the rush usually breaks.",
      "streaks": [3, 1.0],
      "flare": [900, 170, 1.1]
    },
    {
      "template": "setup",
      "headline": "More orders. Same team. **Same system?**",
      "body": "Cashew, sweets and gifting orders pile up before the festive season, and the rush tends to crack in four places.",
      "cue": "Here's where",
      "stops": ["Orders", "Stock", "Paperwork", "Dispatch"],
      "vword": {"text": "Festive rush", "top": 130},
      "streaks": [7, 0.9]
    },
    {
      "template": "task", "n": 1, "of": 4, "label": "Orders",
      "headline": "Orders buried in **multiple places?**",
      "pain": "One gets lost in the scroll, and you hear about it when the customer calls.",
      "whatif": "What if every order, from every channel, landed in one place?",
      "outcome": ["No order missed", "No festive sale lost"],
      "x": 200, "y": 260, "w": 600,
      "ghost": {"side": "right", "offset": -60, "top": 330}
    },
    {
      "template": "task", "n": 2, "of": 4, "label": "Stock",
      "headline": "Ran out of your **best-seller** mid-rush?",
      "pain": "In peak season, stock moves faster than anyone can count.",
      "whatif": "How about a reorder drafted before it runs low, waiting for your OK?",
      "outcome": ["Stock that keeps up", "No sales turned away"],
      "x": 440, "y": 230, "w": 590,
      "blob": [250, 90, 1000, 1040],
      "ghost": {"side": "left", "offset": 20, "top": 420},
      "streaks": [11, 0.8]
    },
    {
      "template": "task", "n": 3, "of": 4, "label": "Paperwork",
      "headline": "Invoices and e-way bills **stacking up?**",
      "pain": "One wrong detail can hold a consignment back.",
      "whatif": "What if every document was checked against the order before the goods left?",
      "outcome": ["Fewer errors", "Goods leave on time"],
      "x": 56, "y": 240, "w": 690,
      "ghost": {"side": "right", "offset": -40, "top": 260},
      "giant": "PAPERWORK"
    },
    {
      "template": "task", "n": 4, "of": 4, "label": "Dispatch",
      "headline": "“Where's my order?” calls **piling up?**",
      "pain": "In festive season, a late delivery can cost you a customer for the year.",
      "whatif": "Imagine delays flagged the moment they happen, and customers updated before they ask.",
      "outcome": ["Fewer calls", "Customers who come back"],
      "x": 450, "y": 240, "w": 580,
      "ghost": {"side": "left", "offset": -30, "top": 330},
      "streaks": [13, 1.0],
      "flare": [980, 120, 0.8]
    },
    {
      "template": "reveal",
      "headline": "Your business already runs the rush **like clockwork.** What if it took even less effort?",
      "body": "That's where **ART (A Realtime Tech)** comes in. Aiotrix's Governed Automation Platform sits on top of the systems you already use and keeps every order, shelf, invoice and delivery in step, in real time. You decide what it runs on its own.",
      "line": "Even more ease, this festive season.",
      "sign": "From our team in Mangaluru to yours: here's to your best festive season yet 🪔",
      "ghost_word": "CLOCKWORK",
      "streaks": [17, 1.0],
      "flare": [940, 260, 1.0]
    },
    {
      "template": "outcome",
      "headline": "This festive season, **everything moves seamlessly.**",
      "rows": ["Every order captured", "Stock that keeps up", "Paperwork right the first time", "Customers kept in the loop"],
      "closing": "And a team that spends the rush with its customers.",
      "streaks": [19, 0.8]
    },
    {
      "template": "cta",
      "headline": "The festive season is only **weeks away.**",
      "line": "The best time to get ready for the rush is before it starts.",
      "main": "DM us to see how ART could fit your business this season.",
      "save": "Save this and share it with whoever runs your dispatch.",
      "streaks": [23, 1.0],
      "flare": [540, 150, 0.9]
    }
  ],
  "objects": [
    {"id": "gift-tower", "image": "01-cover-gift-tower.png", "slide": 1, "x": 690, "y": 150, "w": 480, "glow": true, "ph": 0.0,
     "moment": {"type": "sparks", "points": [[0.52, 0.055], [0.905, 0.105]]}},
    {"id": "phone", "image": "02-phone-orders.png", "slide": 4, "x": -380, "y": 880, "w": 660, "rot": -4, "ph": 1.3,
     "moment": {"type": "bubbles", "origin": [0.269697, 0.449679]}},
    {"id": "shelf", "image": "03-shelf-base.png", "slide": 4, "x": 560, "y": 1030, "w": 520, "ph": 2.1, "float": false,
     "moment": {"type": "topple", "body": "03-tin-body.png", "lid": "03-tin-lid.png", "geom": "03-tin.json", "angle": -85, "at": 0.75, "foreshorten": 0.72}},
    {"id": "invoices", "image": "04-invoice-stack.png", "slide": 5, "x": 650, "y": 760, "w": 390, "rot": 6, "ph": 0.7,
     "moment": {"type": "blink", "box": [0.73, 0.065, 0.16, 0.05]}},
    {"id": "van", "image": "05-delivery-van.png", "slide": 7, "x": -680, "y": 990, "w": 640, "glow": true, "ph": 3.0,
     "moment": {"type": "drive", "dx": 80, "at": 0.3, "dur": 2.3}},
    {"id": "diyas", "image": "06-diyas-marigolds.png", "slide": 8, "x": -150, "y": 830, "w": 540, "ph": 1.8,
     "moment": {"type": "flicker", "points": [[0.494, 0.07], [0.215, 0.30], [0.309, 0.315], [0.682, 0.255], [0.502, 0.61], [0.932, 0.53], [0.063, 0.53]]}}
  ]
}
~~~~
<!-- END FILE -->

---

<!-- FILE: assets/example/PROMPTS.md text -->
# Festive season, Style 2 (A + B mix): 3D image prompts

Free route: Google AI Studio (Gemini image model). Generate on a plain grey background; Claude removes the backgrounds locally (free) and places the cut-outs.
Save the downloads into `images/raw/` with the file names below.

## Shared style line (already included at the end of every prompt)
Photoreal 3D product render, premium commercial studio style, one isolated object group centred with generous empty margin all round, on a plain seamless flat light-grey background (#E9ECEC), soft diffused key light from the top left, subtle cool aqua-teal (#04ADC3) rim light on the edges, realistic materials, crisp detail, sharp focus. No text, no letters, no numbers, no logos, no brand names, no people, no hands, no faces. No floor and no cast shadow on the background.

## 1. `01-cover-gift-tower.png` (aspect 3:4, slide 1)
A tall, slightly leaning tower of festive Indian gift boxes and parcels stacked together: glossy boxes in deep teal, aqua and ivory with aqua satin ribbons and thin gold trim, a few kraft-paper parcels tied with twine, a small marigold garland draped over the top box, a couple of tiny sparkler sparks near the top. Three-quarter view from slightly below so it feels heroic. + shared style line

## 2. `02-phone-orders.png` (aspect 16:9, slides 3–4)
A modern smartphone floating at a dynamic angle, three-quarter view, its screen glowing soft aqua and completely blank with no interface. Bursting out of the screen in an arc to the right: small paper order slips, receipt strips and rounded speech-bubble shapes in aqua, white and teal-green, all blank with no writing, as if orders are pouring in. + shared style line

## 3. `03-shelf-stock.png` (aspect 16:9, slide 4)
A short section of a wooden shop shelf, almost empty: only two plain, unlabelled brushed-metal cashew tins with aqua lids and one ornate sweet box in teal and gold, with one more sweet box tipped over on its side. Lots of empty shelf space shows the stock has run low. Three-quarter view. + shared style line

## 4. `04-invoice-stack.png` (aspect 4:5, slide 5)
A tall, slightly messy stack of paper invoices and delivery documents, fanned and leaning, the sheets showing only blank table grids and abstract soft grey bars, absolutely no letters, words or headings anywhere on the paper, a few aqua and teal-green paper clips and folder tabs, and one sheet near the top marked with a bright aqua flag tab, as if an error was caught. Three-quarter view. + shared style line

## 5. `05-delivery-van.png` (aspect 16:9, slides 6–7)
A compact modern delivery van in clean white with aqua accents, an unbranded fictional design with a smooth plain front grille, no emblem, no badge, no manufacturer logo and no lettering anywhere, side three-quarter view facing right, moving forward with a hint of motion. Its back doors are slightly open, showing festive gift parcels with aqua ribbons inside. Warm amber headlights on and a soft aqua glow underneath. + shared style line

## 6. `06-diyas-marigolds.png` (aspect 3:4, slide 8)
A small cluster of five traditional clay diyas (oil lamps) at different heights, each with a warm glowing flame, arranged with loose orange and yellow marigold flowers and a short marigold garland, with a few small aqua and teal decorative beads. Warm flame light mixed with the cool aqua rim light. + shared style line
<!-- END FILE -->

---

### `assets/example/img/03-tin.json`

<!-- FILE: assets/example/img/03-tin.json code -->
~~~~json
{
 "body": {
  "x": 132,
  "y": 113,
  "w": 133,
  "h": 190
 },
 "lid": {
  "x": 132,
  "y": 63,
  "w": 133,
  "h": 62
 },
 "pivot": [
  132,
  300
 ],
 "src": {
  "w": 686,
  "h": 397
 }
}
~~~~
<!-- END FILE -->

---

### `assets/kit/brand/logo-art.svg`

<!-- FILE: assets/kit/brand/logo-art.svg code -->
~~~~xml
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape" version="1.1" width="400" height="159" viewBox="105 86 337 134" role="img" aria-label="A Realtime Tech logo">
<defs>
<clipPath id="clip_1">
<path transform="matrix(1,0,0,-1,-1224,811)" d="M1224 504H1770V811H1224Z"/>
</clipPath>
<clipPath id="clip_2">
<path transform="matrix(1,0,0,-1,-1224,811)" d="M0 0H1920V1080H0Z"/>
</clipPath>
<clipPath id="clip_3">
<path transform="matrix(1,0,0,-1,-1224,811)" d="M643 469H1188.7562V161.68091H643V469Z"/>
</clipPath>
<g id="mask_4_contents">
<rect x="0" y="0" width="100%" height="100%" fill-opacity="0"/>
<g>
<clipPath id="clip_5">
<path transform="matrix(1,0,0,-1,-1224,811)" d="M0 0H1920V1080H0Z"/>
</clipPath>
<g clip-path="url(#clip_5)">
<path transform="matrix(1,0,0,-1,-413.55763,512.7886)" d="M4.04396 38.518266C.492703 35.32051-.351089 29.271937 .119212 24.337388 .961427 15.500595 14.678793 1.927639 18.730143 9.144522 22.781493 16.361403 21.05495 29.414395 19.48977 31.93446 16.763016 36.324754 7.044421 41.220056 4.04396 38.518266Z"/>
</g>
</g>
</g>
<mask id="mask_4" mask-type="alpha">
<use xlink:href="#mask_4_contents"/>
</mask>
<clipPath id="clip_6">
<path transform="matrix(1,0,0,-1,-1224,811)" d="M0 0H1920V1080H0Z"/>
</clipPath>
<g id="mask_7_contents">
<rect x="0" y="0" width="100%" height="100%" fill-opacity="0"/>
<g>
<clipPath id="clip_8">
<path transform="matrix(1,0,0,-1,-1224,811)" d="M0 0H1920V1080H0Z"/>
</clipPath>
<g clip-path="url(#clip_8)">
<path transform="matrix(1,0,0,-1,161.88672,512.7886)" d="M4.04396 38.518266C.492703 35.32051-.351089 29.271937 .119212 24.337388 .961427 15.500595 14.678793 1.927639 18.730143 9.144522 22.781493 16.361403 21.05495 29.414395 19.48977 31.93446 16.763016 36.324754 7.044421 41.220056 4.04396 38.518266Z"/>
</g>
</g>
</g>
<mask id="mask_7" mask-type="alpha">
<use xlink:href="#mask_7_contents"/>
</mask>
<clipPath id="clip_9">
<path transform="matrix(1,0,0,-1,-1224,811)" d="M0 0H1920V1080H0Z"/>
</clipPath>
<g id="mask_10_contents">
<rect x="0" y="0" width="100%" height="100%" fill-opacity="0"/>
<g>
<clipPath id="clip_11">
<path transform="matrix(1,0,0,-1,-1224,811)" d="M0 0H1920V1080H0Z"/>
</clipPath>
<g clip-path="url(#clip_11)">
<path transform="matrix(1,0,0,-1,161.88672,170.78858)" d="M4.04396 38.518266C.492703 35.32051-.351089 29.271937 .119212 24.337388 .961427 15.500595 14.678793 1.927639 18.730143 9.144522 22.781493 16.361403 21.05495 29.414395 19.48977 31.93446 16.763016 36.324754 7.044421 41.220056 4.04396 38.518266Z"/>
</g>
</g>
</g>
<mask id="mask_10" mask-type="alpha">
<use xlink:href="#mask_10_contents"/>
</mask>
<clipPath id="clip_12">
<path transform="matrix(1,0,0,-1,-1224,811)" d="M0 0H1920V1080H0Z"/>
</clipPath>
<g id="font_13_1">
</g>
<g id="font_13_0">
</g>
<g id="font_13_87">
</g>
<g id="font_13_13">
</g>
<g id="font_13_15">
</g>
<g id="font_13_14">
</g>
<g id="font_13_19">
</g>
<g id="font_13_17">
</g>
<g id="font_13_29">
</g>
<g id="font_13_31">
</g>
<g id="font_13_10">
</g>
<g id="font_13_18">
</g>
<g id="font_13_24">
</g>
<g id="font_13_28">
</g>
<g id="font_13_30">
</g>
<g id="font_13_22">
</g>
<g id="font_13_23">
</g>
<g id="font_13_21">
</g>
<g id="font_13_9">
</g>
<g id="font_13_26">
</g>
<g id="font_13_8">
</g>
<g id="font_13_11">
</g>
<g id="font_13_20">
</g>
<g id="font_13_6">
</g>
<g id="font_13_12">
</g>
<g id="font_13_7">
</g>
<g id="font_13_25">
</g>
<g id="font_13_4">
</g>
<g id="font_13_3">
</g>
<g id="font_13_27">
</g>
<g id="font_13_2">
</g>
<g id="font_13_16">
</g>
<g id="font_13_5">
</g>
<g id="font_13_54">
</g>
<g id="font_13_53">
</g>
<g id="font_13_51">
</g>
<g id="font_13_50">
</g>
<g id="font_13_49">
</g>
<g id="font_13_46">
</g>
<g id="font_13_48">
</g>
<g id="font_13_47">
</g>
<g id="font_13_52">
</g>
<g id="font_13_45">
</g>
<g id="font_13_41">
</g>
<g id="font_13_42">
</g>
<g id="font_13_37">
</g>
<g id="font_13_40">
</g>
<g id="font_13_44">
</g>
<g id="font_13_38">
</g>
<g id="font_13_35">
</g>
<g id="font_13_39">
</g>
<g id="font_13_34">
</g>
<g id="font_13_33">
</g>
<g id="font_13_43">
</g>
<g id="font_13_32">
</g>
<g id="font_13_36">
</g>
<g id="font_13_73">
</g>
<g id="font_13_66">
</g>
<g id="font_13_67">
</g>
<g id="font_13_72">
</g>
<g id="font_13_70">
</g>
<g id="font_13_69">
</g>
<g id="font_13_68">
</g>
<g id="font_13_71">
</g>
<g id="font_13_64">
</g>
<g id="font_13_63">
</g>
<g id="font_13_62">
</g>
<g id="font_13_61">
</g>
<g id="font_13_60">
</g>
<g id="font_13_65">
</g>
<g id="font_13_59">
</g>
<g id="font_13_58">
</g>
<g id="font_13_57">
</g>
<g id="font_13_56">
</g>
<g id="font_13_55">
</g>
</defs>
<g clip-path="url(#clip_1)">
<g clip-path="url(#clip_2)">





















































<path transform="matrix(1,0,0,-1,250.92774,131.5708)" d="M25.68598 .778566 21.77614 .215284C21.1245 2.46841 20.434205 4.704973 19.705252 6.924967L6.368723 6.345118C5.573501 4.257662 4.816936 2.142591 4.099028-.000088L.338293 .513493C1.895602 4.688406 3.618582 8.79705 5.507233 12.839426 7.406929 16.881802 9.428117 20.885523 11.570797 24.850586L16.209589 24.76775C18.109286 20.935225 19.843312 17.025385 21.411665 13.038233 22.980019 9.062124 24.404789 4.975571 25.68598 .778566ZM13.542284 22.100445C12.426765 19.979855 11.371992 17.848219 10.377965 15.705538 9.383938 13.573902 8.434091 11.414655 7.528421 9.227796L18.72779 9.708241C17.976748 11.828833 17.170483 13.910767 16.308993 15.954044 15.447503 17.997323 14.525267 20.046122 13.542284 22.100445Z" fill="#ffffff"/>
<path transform="matrix(1,0,0,-1,250.92774,131.86914)" d="M22.150155-17.906052C22.11702-18.7565 21.945828-19.535153 21.636576-20.242016 21.327322-20.94888 20.918665-21.583954 20.410607-22.147236 19.902548-22.721562 19.311655-23.235142 18.637927-23.687977 17.964198-24.129769 17.246289-24.510807 16.484202-24.831109L21.305232-32.418848 17.87584-33.545415 13.237045-25.808568C12.706898-25.90797 12.154661-25.990807 11.580335-26.057072 11.017053-26.12334 10.393024-26.156479 9.708251-26.156479 9.156013-26.156479 8.548553-26.134385 7.885868-26.090207 7.234228-26.034985 6.549454-25.941105 5.831545-25.808568L5.897814-32.833028 2.402152-32.96556V-9.523094C3.352-9.235931 4.301848-9.020557 5.251696-8.876972 6.201544-8.733391 7.068556-8.622948 7.852733-8.545635 8.769447-8.457275 9.647504-8.407574 10.486905-8.39653 11.204813-8.39653 12.000034-8.446232 12.872569-8.545635 13.745104-8.645035 14.61764-8.821751 15.490174-9.075783 16.373755-9.329811 17.229722-9.683243 18.058077-10.136078 18.875388-10.588913 19.598818-11.163235 20.228369-11.859055 20.846875-12.565918 21.332844-13.416363 21.686276-14.410393 22.039708-15.404419 22.194333-16.569642 22.150155-17.906052ZM10.486905-11.726521C10.232876-11.726521 9.973325-11.73204 9.708251-11.743088 9.454222-11.754131 9.189148-11.770699 8.913029-11.792786 8.44915-11.82592 7.935569-11.875622 7.372287-11.941891 6.809005-11.997116 6.26229-12.085472 5.732142-12.206966L5.798411-22.760216C6.317514-22.85962 6.836617-22.931412 7.35572-22.975594 7.885868-23.008728 8.399448-23.025292 8.896461-23.025292 10.221831-23.025292 11.475409-22.876187 12.657197-22.577977 13.850029-22.268727 14.893757-21.849026 15.788382-21.318879 16.683007-20.78873 17.395392-20.164704 17.92554-19.446797 18.455689-18.717843 18.720763-17.933663 18.720763-17.094262 18.720763-16.243817 18.516434-15.487255 18.107779-14.82457 17.710167-14.161884 17.146887-13.598602 16.417933-13.134724 14.915848-12.195923 12.938838-11.726521 10.486905-11.726521Z" fill="#ffffff"/>
<path transform="matrix(1,0,0,-1,250.92774,130.61035)" d="M29.82073-22.34573 39.661596-21.94812 39.727865-25.129006 29.886998-25.609448 29.953267-30.794957 44.267255-29.983166 44.333528-33.24689 26.83865-34.191217 26.457604-10.583076 44.44949-10.301434 44.333528-13.465755 29.721325-13.697693 29.82073-22.34573Z" fill="#ffffff"/>
<path transform="matrix(1,0,0,-1,250.92774,131.5708)" d="M71.18882-33.479276 67.27898-34.042558C66.627338-31.789429 65.93704-29.552868 65.20809-27.332875L51.87156-27.912724C51.076337-30.00018 50.31977-32.11525 49.601865-34.257928L45.84113-33.744348C47.398439-29.569436 49.121419-25.460789 51.010068-21.418412 52.909765-17.376038 54.93095-13.372318 57.07363-9.407253L61.712427-9.490089C63.61212-13.322617 65.346149-17.232457 66.9145-21.219609 68.48285-25.195717 69.90763-29.282273 71.18882-33.479276ZM59.04512-12.157394C57.929605-14.277985 56.87483-16.409623 55.880804-18.552304 54.886777-20.683938 53.936929-22.843186 53.031259-25.030045L64.23063-24.549599C63.479585-22.429009 62.673318-20.347073 61.811826-18.303795 60.950338-16.260518 60.028104-14.211716 59.04512-12.157394Z" fill="#ffffff"/>
<path transform="matrix(1,0,0,-1,250.92774,132.10108)" d="M78.39551-30.563336 93.05741-29.420208 93.223079-32.949 75.164928-34.191537 75.06552-8.99295 78.49491-8.810711 78.39551-30.563336Z" fill="#ffffff"/>
<path transform="matrix(1,0,0,-1,250.92774,131.15674)" d="M95.86437-13.499535 95.7981-10.003872 114.93312-9.589695 114.86686-12.754013 107.13001-13.052223 107.36195-33.959924 103.700618-34.026189V-13.184761L95.86437-13.499535Z" fill="#ffffff"/>
<path transform="matrix(1,0,0,-1,250.92774,129.74854)" d="M118.41222-11.312675 122.10669-11.44521 122.32206-34.340967H118.99207L118.41222-11.312675Z" fill="#ffffff"/>
<path transform="matrix(1,0,0,-1,250.92774,132.13428)" d="M147.02362-8.711559 150.9169-8.612156 155.40659-33.247457 151.97719-33.92671 148.6472-13.134979 143.18006-31.143437 139.07141-31.623879 132.8753-14.145573 129.87667-33.148057 126.381008-32.667608 130.9701-8.512753H134.39949L141.07604-27.614636 147.02362-8.711559Z" fill="#ffffff"/>
<path transform="matrix(1,0,0,-1,250.92774,130.60987)" d="M162.76239-22.346535 172.60326-21.948925 172.66953-25.12981 162.82866-25.610257 162.89493-30.795765 177.20891-29.983975 177.27519-33.2477 159.7803-34.19202 159.39926-10.583881 177.39116-10.302242 177.27519-13.46656 162.663-13.698502 162.76239-22.346535Z" fill="#ffffff"/>
<path transform="matrix(1,0,0,-1,250.92774,131.15674)" d="M.066268-48.663949 0-45.16828 19.13502-44.754114 19.06875-47.918428 11.331907-48.216638 11.563847-69.12433 7.902514-69.190608V-48.349176L.066268-48.663949Z" fill="#ffffff"/>
<path transform="matrix(1,0,0,-1,250.92774,130.60987)" d="M26.043507-57.51095 35.884374-57.113336 35.95064-60.29422 26.109774-60.774667 26.176043-65.960178 40.49003-65.14839 40.556299-68.41211 23.061427-69.35644 22.68038-45.74829 40.67227-45.466653 40.556299-48.630975 25.944104-48.862916 26.043507-57.51095Z" fill="#ffffff"/>
<path transform="matrix(1,0,0,-1,250.92774,132.36621)" d="M63.501756-61.254884 66.18563-63.12697C65.05907-64.76159 63.60668-66.05935 61.828477-67.02024 60.955945-67.484119 60.028184-67.84307 59.0452-68.0971 58.073266-68.35113 57.06267-68.47814 56.01342-68.47814 54.85372-68.47814 53.743726-68.32904 52.68343-68.03083 50.56284-67.42337 48.71837-66.31889 47.150014-64.71741 46.39897-63.955316 45.747335-63.093835 45.195096-62.132936 44.653905-61.18309 44.2342-60.161447 43.93599-59.068017 43.637784-57.974588 43.48868-56.836984 43.48868-55.655199 43.48868-54.473405 43.637784-53.3358 43.93599-52.24237 44.532407-50.044466 45.60375-48.155817 47.150014-46.576417 47.90106-45.81433 48.74598-45.146127 49.68478-44.5718 50.61254-44.01956 51.612089-43.594339 52.68343-43.296129 53.75477-42.986879 54.864767-42.832254 56.01342-42.832254 56.996404-42.832254 57.946249-42.942697 58.862966-43.163599 59.77968-43.38449 60.65221-43.699266 61.480569-44.107919 63.148324-44.925233 64.56757-46.073877 65.73832-47.55387L63.20355-49.624765C62.34206-48.55343 61.29281-47.70298 60.055799-47.073434 58.82983-46.44388 57.482374-46.129106 56.01342-46.129106 54.73223-46.129106 53.53388-46.383134 52.418359-46.891199 51.302839-47.388208 50.32538-48.06746 49.485979-48.928949 48.646577-49.790437 47.98389-50.801034 47.497926-51.960725 47.023-53.109384 46.785539-54.340867 46.785539-55.655199 46.785539-56.96952 47.023-58.206529 47.497926-59.366228 47.98389-60.525926 48.646577-61.536523 49.485979-62.398019 50.32538-63.259508 51.302839-63.944284 52.418359-64.45234 53.53388-64.94935 54.73223-65.19786 56.01342-65.19786 56.786554-65.19786 57.532075-65.10397 58.24998-64.916217 58.96789-64.728458 59.64714-64.46338 60.287736-64.120998 61.568925-63.43622 62.640264-62.48085 63.501756-61.254884Z" fill="#ffffff"/>
<path transform="matrix(1,0,0,-1,250.92774,130.57715)" d="M70.0292-45.565637 73.52486-45.399965 73.657398-58.670228 88.25302-57.95784 88.08736-45.648469 91.781818-45.913545 91.98063-68.676769 88.4187-68.958408 88.31929-61.03932 73.69053-61.68544 73.806499-69.12408 70.34397-69.25661 70.0292-45.565637Z" fill="#ffffff"/>
<path transform="matrix(1,0,0,-1,117.4375,128.92139)" d="M66.7662 31.168948 112.039958 31.168934V5.235312C104.42252 1.099867 90.84291 .020662 85.06174-.00201 79.51186 2.827503 74.22497 8.114702 72.27525 10.404613 67.976818 18.947569 66.81153 27.768069 66.7662 31.168948Z" fill="#04adc3"/>
<path transform="matrix(1,0,0,-1,117.4375,174.69043)" d="M101.72025-35.109407H112.0375V41.83053C98.83836 37.53735 87.59598 27.08937 83.67991 22.40203 81.45771 15.735043 81.86401 7.707336 82.34494 4.526848 86.80698-12.461189 96.99075-28.781304 101.72025-35.109407Z" fill="#04adc3"/>
<path transform="matrix(1,0,0,-1,117.4375,131.13916)" d="M44.547204-58.773027C41.60209-64.93134 39.805936-74.40501 39.266744-78.662639H95.13154C86.197757-61.099534 72.12583-49.279176 66.18928-45.27381 55.792146-47.72821 47.42909-55.29596 44.547204-58.773027Z" fill="#04adc3"/>
<path transform="matrix(1,0,0,-1,117.4375,151.38428)" d="M0-58.41752H32.293077C37.314867-42.98535 36.90278-25.023659 36.17996-17.68126 32.98426-9.189339 24.500449-5.544529 20.658003-4.783607 11.527462-6.518513 3.081665-12.811348 .000084-15.740906L0-58.41752Z" fill="#04adc3"/>
<path transform="matrix(1,0,0,-1,117.4375,159.93848)" d="M13.608426 62.18799H.000084V.000229C13.414592 7.302071 23.953736 17.64524 27.546496 21.904095 29.040627 34.944536 18.900319 54.15519 13.608426 62.18799Z" fill="#04adc3"/>
<path transform="matrix(1,0,0,-1,117.4375,117.200199)" d="M59.430776 19.447655H21.463849C33.211076 4.890387 42.726099 .465803 46.036668-.001949 54.13543 4.64992 58.340559 14.863698 59.430776 19.447655Z" fill="#04adc3"/>
<path transform="matrix(1,0,0,-1,142.06348,168.86035)" d="M24.560547 36.976076C28.067406 38.73761 36.861185 34.147989 39.433595 30.006348 39.532846 29.846545 39.632413 29.644145 39.731447 29.403809L87.40137 40.644044 41.097658 21.76123C41.38498 16.971749 40.91207 11.203411 38.67383 7.216309 34.622369-.000225 20.905686 13.572937 20.063477 22.409668 19.825253 24.909604 19.924483 27.695275 20.541993 30.251465L0 60.589357 24.560547 36.976076Z" fill="#ffffff" id="hands" data-origin="172.3 146.1"/>
<g mask="url(#mask_10)">
<g>
<g clip-path="url(#clip_12)">
<path transform="matrix(.997579,-.069542,-.069528,-.99758,161.62989,166.67255)" d="M10.449219 3.393066C11.330009 2.862442 12.318276 2.531727 13.313477 2.268066 13.480862 2.229691 13.724991 2.172775 13.891602 2.134277 13.967375 2.121708 14.390717 2.038521 14.475586 2.021973 15.574072 1.827782 16.695414 1.75565 17.810547 1.692871 17.349764 1.63974 16.829005 1.601368 16.361329 1.604004 15.515753 1.593971 14.654824 1.692486 13.828125 1.86084 13.65856 1.902382 13.408623 1.964275 13.238281 2.006348 12.237729 2.29974 11.2319 2.703011 10.449219 3.393066ZM10.269531 3.817871C11.269859 3.344906 12.380539 3.162823 13.489258 3.175293 14.237379 3.169968 14.997907 3.263309 15.745117 3.117676 16.114825 3.050072 16.477454 2.915829 16.826172 2.781738 17.171627 2.659904 17.524739 2.555233 17.88379 2.471191 18.242968 2.386475 18.608798 2.319588 18.980469 2.281738 18.60603 2.256809 18.228735 2.287685 17.856446 2.335449 17.484616 2.388985 17.115342 2.465649 16.753907 2.572754L16.22461 2.737793C15.875801 2.836094 15.519183 2.89299 15.15625 2.912598 14.65326 2.933735 14.152818 2.903568 13.645508 2.908691 14.251099 2.779144 15.059476 2.589314 15.637695 2.519043 16.357312 2.452126 17.089434 2.352001 17.742188 2.032715 17.203539 2.103298 16.679078 2.161972 16.141602 2.197754 15.243499 2.228432 14.360736 2.479061 13.583984 2.909668 13.550824 2.910213 13.517599 2.908745 13.484375 2.909668 12.360756 2.930683 11.198738 3.18261 10.270508 3.816895L10.269531 3.817871ZM8.59375 4.952637C9.484483 4.680691 10.380591 4.412418 11.303711 4.27002 12.226357 4.156128 13.173666 4.118534 14.103516 4.016113 14.746803 3.935883 15.417576 3.873993 16.033204 3.647949 16.949336 3.290306 17.8924 2.9743 18.87207 2.827637 19.10299 2.797131 19.335804 2.77636 19.57129 2.773926 19.10074 2.717415 18.623805 2.75304 18.157227 2.821777 17.456395 2.933277 16.770565 3.119801 16.103516 3.354004 15.891834 3.433533 15.670019 3.502392 15.447266 3.54248 14.07908 3.806541 12.641495 3.819805 11.264648 4.054199 10.335291 4.241138 9.450159 4.567532 8.59375 4.95166V4.952637ZM7.501953 6.154785C8.198909 6.119749 8.901689 5.988529 9.536133 5.697754 10.36821 5.260056 11.304363 4.938347 12.254883 4.943848 13.098367 4.985638 13.943054 4.885796 14.766602 4.718262 15.089911 4.652058 15.411532 4.57085 15.725586 4.468262 16.101109 4.545319 16.486838 4.578518 16.874024 4.569824 17.348475 4.563446 17.811699 4.445576 18.273438 4.36084 19.188546 4.186069 20.089295 3.988342 21.02539 3.937988 19.743752 3.708187 18.438887 4.045033 17.19336 4.303223 16.766777 4.375504 16.338404 4.401566 15.90332 4.407715 16.1301 4.326714 16.352307 4.233681 16.567383 4.125488 16.668559 4.077984 16.825642 3.999695 16.932618 3.963379 17.760376 3.655731 18.674862 3.588074 19.561524 3.543457 19.838732 3.530857 20.117045 3.526188 20.394532 3.512207 19.837252 3.47533 19.281348 3.442284 18.722657 3.459473 18.16332 3.479427 17.593445 3.534767 17.05371 3.686035 16.790156 3.754356 16.517218 3.879692 16.269532 3.992676 16.021058 4.095428 15.765533 4.186008 15.50293 4.257324 14.453488 4.542271 13.348731 4.708591 12.253906 4.678223 11.249116 4.695347 10.299383 5.047523 9.460938 5.553223 8.856889 5.870964 8.179946 6.047497 7.50293 6.153809L7.501953 6.154785ZM10.633789 5.714355C11.156927 5.622253 11.689042 5.606644 12.21582 5.66748 12.583135 5.726696 12.964957 5.725628 13.332031 5.691895 14.074698 5.620304 14.790499 5.469147 15.507812 5.272949 16.19354 5.061886 16.906533 4.928867 17.624024 4.879395 18.103085 4.835384 18.607958 4.904747 19.086915 4.868652 19.826813 4.832283 20.515065 4.528831 21.249024 4.481934 21.48901 4.468941 21.732792 4.488628 21.973633 4.536621 21.741583 4.459644 21.496106 4.412479 21.248047 4.403809 20.515442 4.382977 19.793959 4.643715 19.074219 4.649902 18.592535 4.659771 18.088927 4.583191 17.607422 4.61377 16.863959 4.65369 16.126204 4.783367 15.420898 5.01123 14.731719 5.205963 14.015769 5.373962 13.304688 5.474121 12.946421 5.521812 12.587831 5.541367 12.228516 5.507324 11.612567 5.474354 10.984437 5.555397 10.410156 5.758301L10.633789 5.714355ZM17.574219 5.42334C18.177832 5.303406 18.771813 5.214108 19.382813 5.224121 20.20121 5.240925 21.02595 5.317295 21.84668 5.257324 22.052876 5.237518 22.264576 5.216946 22.460938 5.147949 22.253584 5.155361 22.050028 5.138065 21.845704 5.119629 21.033095 5.04538 20.193678 4.937347 19.376954 4.959473 18.751334 4.982201 18.124108 5.139977 17.574219 5.42334ZM7.694336 6.744629C8.500098 6.584593 9.312288 6.452946 10.133789 6.435059 11.070478 6.479971 12.01191 6.395237 12.935547 6.283691 14.358731 6.107195 15.772405 5.822739 17.204102 5.730957 17.45624 5.711212 17.703005 5.722416 17.955079 5.731934 18.299366 5.739319 18.63948 5.728321 18.979493 5.713379 19.658528 5.684044 20.33573 5.63554 21.010743 5.571777 21.341578 5.544247 21.680405 5.555222 22.010743 5.609863 22.344418 5.662331 22.66859 5.766006 22.96582 5.92627 22.540089 5.644142 22.02658 5.497299 21.516602 5.450684 21.00756 5.403557 20.49497 5.46838 19.985352 5.471191 19.647156 5.480778 19.308354 5.491371 18.970704 5.494629 18.633173 5.497887 18.295413 5.497696 17.960938 5.48584 17.704731 5.470509 17.443209 5.455399 17.1875 5.470215 15.739856 5.539463 14.325102 5.824856 12.896484 6.020996 11.977961 6.147825 11.054259 6.252548 10.126953 6.241699 9.020797 6.311298 7.939339 6.587887 6.889648 6.910645L7.694336 6.744629ZM6.382812 7.794434C7.737651 7.426064 9.106718 6.993822 10.527344 7.006348 11.214328 7.003551 11.910789 7.044788 12.604492 7.04541 11.461413 7.276636 10.31916 7.465048 9.163086 7.655762 10.414171 7.809076 11.90104 7.592161 13.053711 7.038574 13.466326 7.025562 13.877344 6.99288 14.28418 6.91748 17.066859 6.169558 20.371018 5.826141 23.203125 6.562012 22.533249 6.317078 21.828326 6.166481 21.11914 6.068848 18.809147 5.794872 16.447167 6.028656 14.219727 6.646973 13.709498 6.754097 13.183441 6.767714 12.658203 6.778809 11.685251 6.804544 10.687856 6.727396 9.713867 6.845215 8.566726 7.023144 7.460752 7.389114 6.382812 7.793457V7.794434ZM23.291016 7.10498C21.054417 6.290071 17.947836 6.398369 15.651367 6.92334 18.198523 6.781723 20.761515 6.655722 23.291016 7.10498ZM23.544922 7.82373C22.079415 7.018314 20.067564 6.799721 18.45996 7.236816 20.181073 7.194466 21.878964 7.379595 23.544922 7.82373ZM23.850586 8.962402C23.67025 8.731392 23.452567 8.517899 23.211915 8.346191 21.939469 7.429228 20.132992 7.37097 18.61621 7.260254 16.44068 7.136503 14.215759 7.121887 12.106445 7.710449 10.975362 7.978891 9.810878 8.268709 8.636719 8.185059 8.038398 8.148518 7.436766 8.242882 6.857422 8.369629 6.472659 8.454248 6.094067 8.561892 5.724609 8.692871 6.665804 8.450239 7.648218 8.261604 8.625977 8.344238 9.222273 8.420473 9.832311 8.37377 10.420898 8.29248 11.011951 8.212465 11.594453 8.093454 12.172852 7.956543 14.64122 7.317472 17.251948 7.431232 19.78711 7.566895 20.942917 7.658274 22.171738 7.765297 23.167969 8.406738 23.493088 8.620527 23.781023 8.891832 24.023438 9.199707L23.850586 8.962402ZM23.90039 9.471191C23.457976 9.155642 22.963883 8.91206 22.458985 8.702637 21.665469 8.38122 20.83815 8.144236 19.996094 7.986816 19.929026 7.971109 19.753848 7.954985 19.682618 7.947754 18.188672 7.811596 16.678997 7.722609 15.182617 7.852051 14.908894 7.876108 14.635364 7.915909 14.364258 7.974121 13.839564 8.094767 13.31017 8.177626 12.771484 8.215332 12.232669 8.254381 11.689581 8.256603 11.149414 8.20459 12.219277 8.416632 13.338511 8.392952 14.412109 8.187988 14.934492 8.100504 15.474083 8.073332 16.012696 8.064941 17.2938 8.047188 18.582613 8.121792 19.861329 8.217285 20.725499 8.349123 21.581358 8.552778 22.410157 8.830566 22.922638 9.002174 23.423974 9.208166 23.90039 9.471191ZM24.067383 10.122559C23.533366 9.760687 22.946906 9.477213 22.34375 9.243652 21.438769 8.893963 20.468817 8.644567 19.49414 8.606934 19.211178 8.593349 18.906403 8.612309 18.626954 8.653809 18.12202 8.73481 17.608508 8.800673 17.098633 8.76123 16.949275 8.746756 16.799227 8.731949 16.66211 8.671387 16.187064 8.524521 15.712019 8.459579 15.219727 8.44873 14.855176 8.440111 14.489851 8.472315 14.132812 8.54248 13.567871 8.674284 13.016635 8.844166 12.427734 8.786621 11.483269 8.697201 10.520282 8.716085 9.579102 8.816895 8.167205 8.95919 6.767436 9.209671 5.391602 9.539551H5.393555C6.323332 9.382776 7.257814 9.252117 8.194336 9.148926 9.359055 9.025381 10.534943 8.922518 11.707031 8.990723 12.18164 9.019476 12.666633 9.106121 13.146484 9.036621 13.389658 9.00424 13.626137 8.950678 13.857422 8.890137 14.301018 8.771759 14.758404 8.719715 15.217773 8.726074 15.669955 8.732391 16.143692 8.795958 16.572266 8.92627L16.549805 8.91748C16.719498 8.994688 16.898589 9.012587 17.080079 9.027832 17.61765 9.060688 18.150494 8.984398 18.673829 8.89209 18.785006 8.878105 18.909035 8.854401 19.020508 8.846191 19.201169 8.829094 19.428202 8.825336 19.609375 8.827637 20.20073 8.848501 20.805249 8.946867 21.38086 9.085449 22.31547 9.317379 23.230742 9.645113 24.067383 10.122559ZM5.724609 8.692871H5.72168L5.719727 8.693848C5.721252 8.693306 5.723083 8.693413 5.724609 8.692871ZM24.191407 11.941895C24.005852 11.744184 23.8111 11.533741 23.601563 11.356934 22.218279 10.137211 20.146433 9.244173 18.30371 9.039551 20.137331 9.625719 21.926087 10.379833 23.514649 11.464355 23.745898 11.609797 23.96451 11.789436 24.191407 11.941895ZM23.72461 12.632324 23.246094 12.223145 22.74707 11.838379C17.626202 8.114182 10.782436 9.040003 5.030273 10.48877L5.029297 10.489746C7.491595 10.011137 9.991225 9.652454 12.501953 9.524902 16.650013 9.27714 21.031397 10.240782 24.177735 13.066895L23.72461 12.632324ZM24.11914 10.827637C23.54975 10.15823 22.241127 9.828106 21.379883 9.841309 22.273432 10.244436 23.220704 10.437824 24.11914 10.827637ZM24.17871 14.071777C23.246394 13.194353 22.25643 12.342655 21.183594 11.631348 20.878249 11.424385 20.530884 11.224197 20.206055 11.04834 19.718792 10.802418 19.206463 10.56288 18.644532 10.501465 18.583775 10.497759 18.516777 10.493464 18.456055 10.500488 18.149138 10.52635 17.833455 10.526794 17.52832 10.475098 17.22047 10.425705 16.922677 10.334049 16.638672 10.206543 16.489998 10.145008 16.329964 10.051397 16.164063 10.01709 15.781445 9.942572 15.393641 9.94006 15.007812 9.932129 14.383143 9.931 13.693138 9.93051 13.06543 9.95166 10.270861 10.048986 7.453649 10.379646 4.780273 11.178223V11.180176C7.387152 10.576996 10.076534 10.323112 12.753906 10.22998 13.488262 10.210365 14.275218 10.206163 15.007812 10.213379 15.372699 10.219934 15.744945 10.218878 16.103516 10.285645 16.352709 10.353926 16.574887 10.496744 16.836915 10.577637 17.048428 10.650429 17.267035 10.705906 17.488282 10.737793 17.82298 10.788317 18.157139 10.783997 18.492188 10.749512 18.53199 10.744684 18.586993 10.747869 18.626954 10.749512 19.39965 10.840725 20.134919 11.236523 20.80664 11.620605 22.011713 12.323622 23.102627 13.190952 24.17871 14.071777ZM23.978516 15.062012C23.386488 14.38496 22.653594 13.836372 21.905274 13.334473 20.106345 12.15587 18.063502 11.324341 15.951172 10.884277 15.395347 10.767586 14.825563 10.687218 14.263672 10.618652 13.936011 10.587437 13.57098 10.570871 13.241211 10.546387 12.710346 10.530603 12.065057 10.524256 11.536133 10.553223 11.096079 10.567232 10.615033 10.613117 10.178711 10.655762 7.938931 10.922468 5.706294 11.493397 3.702148 12.507324L3.700195 12.508301C6.953622 11.13871 10.697428 10.56951 14.235352 10.897949 16.911303 11.183773 19.52779 12.064425 21.829102 13.449707 22.597579 13.909895 23.34341 14.431335 23.978516 15.062012ZM23.97754 16.064942C21.960064 13.992119 19.340863 12.44879 16.510743 11.721191 13.688009 11.00518 10.644301 10.966072 7.861328 11.803223L8.257812 11.722168C12.363232 10.93297 16.768237 11.565947 20.447266 13.577637 21.707602 14.275373 22.886387 15.117401 23.97754 16.064942ZM23.74121 18.355957C23.406188 17.889706 23.038727 17.428849 22.658204 16.995606 20.583287 14.620068 17.724743 12.914389 14.611328 12.236816 10.937803 11.438101 7.022013 11.833632 3.560547 13.199707 7.064349 12.05538 10.913699 11.710258 14.549805 12.509277 17.503317 13.148104 20.23107 14.687763 22.344727 16.810059 22.83666 17.293732 23.30192 17.825695 23.74121 18.355957ZM23.365235 20.211426C22.312226 18.658459 20.971034 17.266394 19.457032 16.127442 17.3641 14.570742 14.893349 13.385708 12.308594 12.85498 12.468603 12.872969 12.628585 12.891233 12.788086 12.913574 16.082884 13.378862 19.164965 14.943211 21.59082 17.177247 21.932053 17.48235 22.294657 17.834822 22.611329 18.163575 22.941094 18.503546 23.253899 18.858099 23.567383 19.213379 21.574522 16.573204 18.836562 14.373495 15.635742 13.309082 11.539305 11.922228 6.905549 12.333534 3.054688 14.161621 5.712495 13.078247 8.642526 12.585035 11.52832 12.782715 14.939355 13.564734 18.13979 15.227835 20.761719 17.507325 21.698958 18.33575 22.566226 19.242827 23.365235 20.211426ZM23.96875 17.231934C23.82218 17.033568 23.67229 16.834908 23.515625 16.643067 22.709502 15.698784 21.737723 14.885315 20.69336 14.202637 19.720738 13.564608 18.681609 13.009619 17.580079 12.621582 19.593214 13.74692 21.552117 14.995663 23.249024 16.55127 23.496047 16.764346 23.728323 17.011607 23.96875 17.231934ZM2.396484 15.190918C5.846733 13.684549 9.721534 13.179798 13.480469 13.664551 12.554714 13.43512 11.601608 13.307276 10.645508 13.26416 7.862775 13.154253 4.784524 13.785961 2.396484 15.190918ZM23.265625 21.520997C22.898116 20.87512 22.495396 20.235735 22.049805 19.63916 20.135142 16.989066 17.299263 14.972651 14.055664 14.23584 10.087949 13.331221 5.862885 14.069323 2.271484 15.813965 5.015078 14.653429 8.026996 14.022018 11.029297 14.117676 15.416862 14.229462 19.294068 16.296883 21.96289 19.702637 22.433054 20.279149 22.858511 20.900723 23.265625 21.520997ZM1.145508 18.252442C3.161992 16.558318 5.632727 15.399261 8.233398 14.852051 9.102847 14.675173 9.987324 14.564659 10.882812 14.505371 9.084642 14.391407 7.257298 14.69689 5.584961 15.337402 3.922734 15.989946 2.342553 16.939709 1.145508 18.251465V18.252442ZM23.148438 23.415528C22.398018 21.108923 20.927523 19.020339 19.00586 17.484864 17.081616 15.968939 14.75983 14.887161 12.316406 14.534668 14.685158 15.10243 16.928738 16.19337 18.825196 17.700684 20.733487 19.215565 22.184826 21.206715 23.148438 23.415528ZM22.532227 25.14502C22.317868 24.314145 22.030571 23.495823 21.668946 22.712403 20.266936 19.697422 17.767426 17.162747 14.733398 15.687012 14.702691 15.672216 14.65556 15.65204 14.625 15.640137 14.559967 15.619787 14.376637 15.557262 14.308594 15.535645L13.885742 15.397949 13.458008 15.284668C11.171827 14.682098 8.706225 14.825764 6.513672 15.658691 4.351719 16.471329 2.364755 17.863192 .874023 19.591309 2.895577 17.491377 5.548032 15.914278 8.464844 15.36377 10.234632 15.042017 12.075869 15.160255 13.806641 15.665527 13.939434 15.708855 14.291525 15.821854 14.420898 15.86377L14.523438 15.896973C14.533135 15.899649 14.53637 15.902534 14.543945 15.904785L14.568359 15.915527 14.616211 15.937012C18.399445 17.765212 21.334418 21.192017 22.532227 25.14502ZM1.572266 17.135254C2.81578 16.484654 4.04044 15.843748 5.3125 15.247559 3.971794 15.444372 2.523862 16.200318 1.572266 17.135254ZM21.916993 27.376465C21.874548 27.09758 21.833348 26.722594 21.78418 26.45166 21.754078 26.285315 21.68032 25.918759 21.651368 25.76123 21.61682 25.627457 21.52316 25.219639 21.487305 25.077637 21.422657 24.821343 21.332982 24.542828 21.261719 24.286622 21.2426 24.236252 21.094532 23.794976 21.070313 23.72998 20.010704 20.764313 17.89474 18.129857 15.077148 16.580567 14.649789 16.346787 14.219472 16.132868 13.753906 15.972168L13.286133 15.845215C13.018514 15.763203 12.61669 15.696899 12.34082 15.641113 12.109232 15.602144 11.854088 15.581406 11.621094 15.549316 11.246819 15.520124 10.787686 15.500307 10.413086 15.516113L10.171875 15.520996C9.942591 15.546848 9.678928 15.556774 9.451172 15.589355 5.618981 16.115006 2.374846 18.686303 .208008 21.703614 2.455298 18.846369 5.736013 16.324662 9.488281 15.850098 9.710195 15.821302 9.96612 15.811167 10.19043 15.788574L10.424805 15.784668C10.580997 15.783363 10.737488 15.778053 10.894531 15.779785L11.364258 15.805176C11.495522 15.801031 11.698601 15.836695 11.832031 15.850098 12.194846 15.884876 12.632119 15.975016 12.989258 16.052247 13.127796 16.091711 13.524911 16.197735 13.669922 16.237793 16.165102 17.185976 18.250784 19.080252 19.671875 21.279786 20.592797 22.728772 21.24778 24.34488 21.637696 26.003418 21.740427 26.422562 21.840954 26.951931 21.916993 27.376465ZM21.50879 28.271973C21.402699 27.64812 21.258755 27.030156 21.094727 26.41748 20.05966 22.652497 18.017094 17.917752 13.952148 16.529786 10.341949 15.39983 6.833283 16.262209 4.098633 18.7583 3.621224 19.184723 3.178683 19.64607 2.757812 20.122559 1.940048 21.08747 1.038046 21.987025 -0 22.72998 1.077077 22.040644 2.008126 21.148112 2.862305 20.213379 3.720255 19.285185 4.671692 18.438736 5.74707 17.771973 8.08528 16.30176 10.838954 15.948999 13.522461 16.694825 17.111737 17.663945 19.178524 21.461909 20.405274 24.641114 20.857733 25.823658 21.22728 27.037434 21.50879 28.271973ZM11.803711 37.75049C12.636822 37.47401 13.438745 37.10796 14.204102 36.681154 15.730882 35.82527 17.149378 34.697469 18.05957 33.199708 19.157082 31.311285 19.665326 29.115063 19.63086 26.941895 19.620274 25.632039 19.263613 24.339743 18.832032 23.10498 18.238305 21.461773 17.366787 19.856968 16.033204 18.666504 14.992142 17.728367 13.774821 17.259934 12.400391 17.024903 10.192996 16.627167 7.866842 17.10424 5.995117 18.281739 5.153346 18.803978 4.389316 19.447606 3.754883 20.197754 3.485985 20.520409 3.211756 20.887726 2.923828 21.1958 2.116068 22.060446 1.163034 22.835854 .046875 23.287598L.048828 23.288575C1.495997 22.754197 2.689622 21.691472 3.646484 20.527832 4.329826 19.698803 5.163413 18.987694 6.091797 18.432129 8.342694 17.063782 11.09625 16.767592 13.624023 17.591309 16.182379 18.39487 17.712286 20.835976 18.567383 23.193848 18.993018 24.40738 19.345774 25.658135 19.36914 26.944825 19.415677 29.073204 18.948336 31.243176 17.90332 33.10791 16.585753 35.305418 14.188934 36.83061 11.803711 37.75049ZM15.05957 35.614748C15.389022 35.430974 15.679303 35.18783 15.951172 34.930177 16.489726 34.40748 16.956688 33.81888 17.385743 33.20752 18.75729 30.956637 19.114289 28.206404 18.786133 25.619629 18.593319 24.124077 18.067473 22.676985 17.288086 21.372559 16.435027 19.94302 15.171847 18.69296 13.576172 18.088379 9.873575 16.7274 6.110379 18.370694 3.678711 21.165528 3.430398 21.448548 3.216805 21.75937 2.984375 22.043457 2.265864 22.886883 1.307165 23.569104 .212891 23.85791L.211914 23.858887C1.327253 23.610829 2.316493 22.944859 3.066406 22.112793 3.313942 21.826128 3.531685 21.527722 3.78418 21.256348 5.025603 19.89195 6.603496 18.78242 8.396484 18.22998 10.159798 17.678837 12.163801 17.734539 13.859375 18.507325 16.258595 19.644253 17.6796 22.124909 18.326172 24.564942 19.058016 27.669663 18.70272 31.51073 16.649415 34.055177 16.189267 34.63533 15.697287 35.214296 15.05957 35.614748ZM22.993165 24.184082C22.901919 23.870869 22.803709 23.520806 22.677735 23.216309L22.484375 22.742676C22.3358 22.441544 22.189076 22.121705 22.014649 21.83252 21.685677 21.249482 21.280634 20.657687 20.856446 20.13623 20.105458 19.206053 19.242852 18.345118 18.251954 17.659668L18.902344 18.312989C20.396943 19.861014 21.707985 21.581439 22.667969 23.494629 22.769539 23.716923 22.88372 23.964489 22.993165 24.184082ZM9.949219 37.65381C10.40669 37.452356 10.870977 37.233118 11.314453 36.99951 11.515268 36.88637 11.771237 36.7414 11.972656 36.62549 14.101697 35.35984 15.904243 33.515096 16.888672 31.255372 17.334107 30.244397 17.627278 29.153424 17.682618 28.046387 17.695696 27.54335 17.66108 27.038453 17.613282 26.53955 17.338103 24.005713 16.534953 21.187294 14.449219 19.492676 12.739116 18.120923 10.590723 17.901526 8.566406 18.648926 6.467743 19.445038 4.699349 20.926066 3.289062 22.614747 3.099296 22.839627 2.933423 23.100157 2.723633 23.308106 2.101985 23.951375 1.199099 24.312949 .294922 24.354004 1.259789 24.349553 2.235209 23.961022 2.891602 23.2583 2.939421 23.199303 3.041029 23.085873 3.088867 23.026856 3.425564 22.597046 3.800726 22.195076 4.19043 21.811036 5.463055 20.563893 6.938407 19.46518 8.645508 18.858887 9.765812 18.470192 11.001626 18.334832 12.166016 18.641114 12.932154 18.841126 13.661608 19.205643 14.272461 19.702637 16.275919 21.336966 17.067128 24.121785 17.341797 26.563965 17.383992 26.956637 17.413573 27.3512 17.422852 27.743653 17.439858 28.525486 17.291367 29.307812 17.078125 30.058106 16.30699 32.784517 14.33186 35.048505 11.933594 36.565919 11.296999 36.96443 10.627496 37.32811 9.949219 37.65381ZM10.479492 36.918458C11.594174 36.18389 12.662525 35.380529 13.639648 34.475099 15.031337 33.175447 16.219729 31.59089 16.728516 29.748536 17.625477 26.239884 16.736834 21.825158 13.537109 19.651856 13.250031 19.47436 12.939507 19.291111 12.62793 19.158692 10.223118 18.19731 7.569979 19.475348 5.786133 21.040528 5.42907 21.353859 5.090866 21.699294 4.775391 22.053223 4.648986 22.196503 4.348387 22.552983 4.21875 22.697754 3.312 23.714858 1.886037 24.987824 .421875 24.961426 1.904113 25.043694 3.377618 23.790032 4.324219 22.78955 4.452386 22.640976 4.771967 22.297936 4.892578 22.154786 5.210384 21.811259 5.549926 21.476687 5.907227 21.17334 7.625917 19.713082 10.24921 18.469639 12.519531 19.403809 12.813902 19.530562 13.109553 19.704577 13.381836 19.875489 15.518331 21.327059 16.598034 23.89215 16.754883 26.362793 16.942959 28.675148 16.437676 30.80833 15.030273 32.68213 13.6783 34.50268 11.863636 35.92827 10 37.229005L10.479492 36.918458ZM20.926758 29.108887C20.776383 25.51208 19.266194 21.616002 16.670899 19.006348L16.989258 19.42041C18.549929 21.512343 19.651106 23.917368 20.34375 26.405762 20.58541 27.293808 20.774367 28.195969 20.926758 29.108887ZM10.259766 37.91748C10.375601 37.898656 10.690553 37.78675 10.80957 37.75049 10.924 37.71353 11.064927 37.668638 11.171875 37.621583 11.763406 37.394968 12.353939 37.108976 12.890625 36.776857 13.762704 36.245725 14.565651 35.5929 15.265625 34.858888 17.24697 32.699914 18.305706 29.757218 18.283204 26.851075 18.272229 25.329384 17.902955 23.800744 17.168946 22.449707 16.438405 21.113667 15.41205 19.90955 14.140625 19.038575 16.546029 20.902237 18.052273 23.853413 18.012696 26.850098 18.015933 29.667426 16.975253 32.580095 15.092773 34.705568 14.508177 35.34705 13.830091 35.93403 13.121094 36.440919 13.025089 36.503004 12.744856 36.693639 12.649414 36.75537 12.538159 36.82373 12.274211 36.97846 12.162109 37.047365 11.719031 37.289678 11.264797 37.51919 10.789062 37.694826 10.689471 37.727586 10.357828 37.86231 10.25 37.887208 10.113214 37.929658 9.834319 38.008935 9.699219 38.050294 9.834337 38.01609 10.131816 37.94884 10.259766 37.91748ZM16.39746 28.3208C16.785988 25.873885 16.030762 23.257296 14.352539 21.372559 13.673567 20.625763 12.850553 19.900456 11.831055 19.671387 10.283218 19.269892 8.725553 19.896758 7.501953 20.78955 6.683189 21.375178 5.947448 22.054726 5.264648 22.775879 5.087186 22.954 4.663379 23.393589 4.476562 23.553223 3.626917 24.339173 2.660138 25.064595 1.553711 25.465332 1.152917 25.603466 .718168 25.720343 .288086 25.70166 .524467 25.731068 .79141 25.699952 1.025391 25.662598 1.266977 25.61988 1.522963 25.550129 1.754883 25.468262 3.186774 24.962273 4.379864 23.977257 5.426758 22.92627 6.122258 22.22918 6.853725 21.56296 7.661133 21.004395 7.946594 20.802489 8.287483 20.590212 8.599609 20.430176L8.761719 20.344239 8.928711 20.27002C10.243716 19.643103 11.87497 19.64023 13.071289 20.553223 15.069387 22.026164 16.256464 24.43407 16.417969 26.849122 16.454348 27.332243 16.43579 27.837763 16.39746 28.3208ZM15.860352 28.21045C16.228108 25.579863 15.382751 22.546067 13.094727 20.913575 12.23875 20.314105 11.122757 19.973994 10.079102 20.219239 8.411564 20.598454 6.993431 21.80676 5.924805 23.060059 7.091166 21.918549 8.48483 20.803824 10.130859 20.459473 10.782132 20.328692 11.448949 20.411526 12.0625 20.666504 14.909504 21.915484 16.01162 25.360722 15.860352 28.21045ZM15.370117 27.983887C15.391223 26.238198 15.124849 24.400525 14.202148 22.858887 13.65309 21.962485 12.841894 21.146582 11.803711 20.814942 9.81776 20.336127 7.893569 21.708996 6.730469 23.149903 7.990096 21.891438 9.780209 20.639998 11.675781 21.059082 12.102785 21.182648 12.492653 21.422938 12.838867 21.699707 14.684971 23.238564 15.157971 25.73254 15.370117 27.983887ZM8.306641 35.865724C10.471289 34.76106 12.430248 33.10309 13.53125 30.937012 14.567563 28.871472 14.74094 26.3596 13.882812 24.191895 13.782196 23.832684 13.652328 23.479386 13.479492 23.146973 13.299181 22.825108 13.070463 22.525986 12.80957 22.262207 11.210249 20.646828 8.923851 21.689167 7.598633 23.065918 8.967708 21.961327 11.132704 20.93706 12.607422 22.458497 13.286615 23.110253 13.614986 24.010346 13.813477 24.901856 14.014309 25.817215 14.019082 26.758553 13.889648 27.685059 14.131098 26.80888 14.185925 25.879252 14.049805 24.975098 14.631433 27.844529 13.770292 30.809092 11.767578 33.001466 10.77344 34.121114 9.580667 35.05022 8.306641 35.865724ZM13.405273 27.79541C13.829825 26.325987 13.809924 24.558993 12.817383 23.283692 11.581442 21.773142 9.793567 22.329007 8.530273 23.442872 9.824766 22.609356 11.464135 22.043459 12.59375 23.456543 13.546579 24.682291 13.587988 26.322836 13.405273 27.79541ZM12.959961 27.70459C13.086516 27.013386 13.139501 26.29147 13.06543 25.58545 12.990607 24.864985 12.780307 24.11924 12.259766 23.574707 11.627238 22.905919 10.557072 22.833424 9.761719 23.216309L9.912109 23.183106C10.672298 23.036458 11.533916 23.157418 12.061523 23.754395 12.51969 24.262642 12.709961 24.959017 12.81543 25.614747 12.926318 26.305315 12.939072 27.000033 12.959961 27.70459ZM.682617 29.063965C.993669 29.108277 1.318405 29.068907 1.625 29.012207 2.309386 28.870163 2.949783 28.569588 3.526367 28.188965 4.156864 27.787789 4.714696 27.259093 5.240234 26.73584 6.115549 25.881257 7.075024 25.094136 8.157227 24.502442 9.006775 24.042988 9.934455 23.730534 10.898438 23.577637 12.240429 24.495373 12.708831 26.060774 12.381836 27.588379 12.79951 26.239865 12.508891 24.763026 11.464844 23.745606 11.311026 23.593647 11.147059 23.452347 10.956055 23.328614L10.908203 23.334473C8.579743 23.61197 6.634002 24.938084 5.05957 26.562012 4.552876 27.086224 4.023654 27.62283 3.420898 28.04248 2.625635 28.602744 1.690455 29.074044 .681641 29.063965H.682617ZM.981445 29.838379C1.475167 29.88839 1.970331 29.749238 2.424805 29.575684 3.822303 29.029847 4.872122 27.926825 5.954102 26.94873 7.00978 25.977498 8.115394 24.981184 9.463867 24.42041 9.894184 24.244248 10.345045 24.118969 10.804688 24.029786 11.652289 24.68806 11.936523 25.831938 11.884766 26.846192L11.873047 27.095215 11.8125 27.590332 11.916992 27.100098 11.947266 26.851075C12.080549 25.811532 11.831296 24.638058 11.007812 23.904786 10.967234 23.866557 10.913139 23.828299 10.863281 23.79248 10.349919 23.864617 9.845152 23.996554 9.362305 24.182129 7.964668 24.732235 6.833169 25.74801 5.767578 26.757325 4.749257 27.713969 3.676421 28.888148 2.379883 29.478028 1.94102 29.674653 1.472133 29.844855 .981445 29.838379ZM.558594 28.63623C1.913505 28.43519 3.187605 27.807293 4.274414 27.0083 4.928546 26.53749 5.510171 25.935122 6.039062 25.337403 6.526209 24.819264 7.018988 24.305539 7.59668 23.879395 6.870374 24.251105 6.260756 24.81215 5.683594 25.373536 4.277967 26.843518 2.529665 28.01366 .558594 28.635254V28.63623ZM.46582 27.03955C1.089045 27.112645 1.727517 26.994912 2.321289 26.818848 2.785482 26.671622 3.23463 26.467377 3.65625 26.22998 3.890461 26.082116 4.129827 25.940709 4.34668 25.77002 4.39867 25.730423 4.543252 25.621752 4.59375 25.58252 5.146374 25.128369 5.645896 24.590466 6.053711 24.0083 5.757221 24.26814 5.450906 24.571482 5.143555 24.819825 3.824772 25.940203 2.233801 26.839756 .464844 27.038575L.46582 27.03955ZM.449219 26.410645C.88712 26.46713 1.334145 26.391201 1.755859 26.278809 2.819039 25.983765 3.760122 25.35368 4.516602 24.57959 4.661816 24.419367 4.804546 24.256806 4.9375 24.088379 4.592865 24.336335 4.251493 24.612942 3.90332 24.853028 2.865845 25.568055 1.721464 26.208374 .449219 26.410645ZM1.386719 30.615723C2.097807 30.50493 2.759023 30.170287 3.374023 29.818848 4.401084 29.206665 5.317394 28.397368 6.147461 27.549317 7.39243 26.292448 8.968361 24.968493 10.706055 24.44873 10.801959 24.59613 10.889215 24.772828 10.955078 24.935059 11.303496 25.798142 11.336376 26.751355 11.228516 27.661622 11.351464 27.10059 11.407804 26.517296 11.358398 25.942872 11.299256 25.358664 11.163202 24.770863 10.838867 24.263184L10.801758 24.20752C10.284273 24.303902 9.81808 24.504078 9.355469 24.730957 8.060245 25.386918 6.935839 26.330304 5.946289 27.365723 4.767543 28.615712 3.087083 30.144263 1.386719 30.615723ZM17.566407 34.578615C18.30579 34.05209 18.884974 33.317686 19.297852 32.51123 19.619107 31.915137 19.801579 31.23753 19.918946 30.57373 19.92883 30.51764 19.956376 30.378636 19.96582 30.324707 19.97314 30.270384 20.01389 29.965294 20.02246 29.904786 20.223034 28.119145 20.078686 26.290177 19.594727 24.5542L19.59375 24.553223C19.871676 26.45364 19.954506 28.38176 19.686524 30.279786 19.63617 30.561427 19.5829 30.895106 19.510743 31.172364 19.224282 32.462316 18.537255 33.653863 17.566407 34.578615ZM1.420898 31.536622C1.631696 31.497693 1.934115 31.451676 2.136719 31.398926 3.920304 31.012009 5.234354 30.106114 6.402344 28.76416 7.037735 28.052762 7.586125 27.274649 8.290039 26.626465 8.952705 26.00209 9.70331 25.44189 10.532227 25.046387 10.894649 25.786187 10.821939 26.662337 10.667969 27.444825 10.930209 26.600213 11.05121 25.629658 10.620117 24.810059 9.671615 25.176873 8.843914 25.760209 8.100586 26.430176 7.383987 27.075795 6.820436 27.864232 6.192383 28.586426 4.981112 30.008374 3.770454 30.858853 1.946289 31.39209 1.810476 31.42973 1.552915 31.499646 1.420898 31.536622ZM8.475586 27.242676C8.86234 26.907834 9.254262 26.546465 9.623047 26.225098 9.686578 26.169856 9.75053 26.115262 9.814453 26.061036 9.682898 26.564244 9.511429 27.059887 9.255859 27.516114 9.843509 26.946707 10.104149 26.133805 10.274414 25.356934 9.406975 25.944163 8.68212 26.71517 8.091797 27.565918L8.475586 27.242676ZM10.015625 27.416504C10.429153 26.92923 10.656081 26.106003 10.40332 25.497559 10.257172 26.126107 10.05973 26.770905 10.015625 27.416504ZM2.475586 32.947755C4.575322 32.42598 6.592171 30.783768 8.103516 29.246582 7.435753 30.225625 6.631198 31.120808 5.748047 31.912598L5.498047 32.135255C5.86165 31.876824 6.220759 31.607209 6.551758 31.307129 7.2243 30.71628 7.824967 30.046336 8.349609 29.324707 8.590236 29.009867 8.823861 28.618367 9.042969 28.222168L9.048828 28.215332 9.046875 28.214356C9.230684 27.881615 9.404634 27.545844 9.55957 27.247559L8.837891 28.03955 8.15625 28.785645C7.943244 28.998667 7.659696 29.298712 7.447266 29.505372 7.323925 29.62276 7.017388 29.91542 6.898438 30.028809 6.778321 30.133955 6.454428 30.422055 6.331055 30.531739 5.560987 31.18087 4.744164 31.799492 3.862305 32.302248 3.417542 32.54984 2.964567 32.788179 2.475586 32.946779V32.947755ZM1.972656 30.844239C3.22845 30.687558 4.391063 30.01232 5.262695 29.13623 5.86619 28.4571 6.484501 27.772915 7.263672 27.279786 6.682179 27.506222 6.177844 27.892075 5.719727 28.302247 5.495484 28.498654 5.278941 28.741013 5.067383 28.950684 4.042189 29.915955 2.50634 30.83454 1.032227 30.79541 1.33652 30.869824 1.658351 30.873648 1.972656 30.844239ZM1.987305 32.32373C4.446558 31.921772 6.728277 30.112969 7.993164 28.060059 6.3569 29.906224 4.372222 31.506812 1.987305 32.32373ZM4.479492 34.2583C7.252973 33.298227 9.482223 30.691735 10.541992 28.062989 9.068475 30.564387 7.122221 32.886899 4.479492 34.2583ZM5.396484 34.766115C5.759257 34.6521 6.105832 34.48751 6.4375 34.299318 8.607795 33.004007 10.27424 30.396063 11.139648 28.094239 10.417077 29.396153 9.639181 30.663437 8.717773 31.836426 8.093311 32.638719 7.392029 33.389604 6.584961 34.019044 6.2135 34.298677 5.817048 34.55504 5.396484 34.766115ZM3.495117 33.779787C3.860702 33.732107 4.22011 33.63763 4.569336 33.515138 6.914434 32.626554 8.77782 30.313879 9.765625 28.109864 8.411461 30.17324 6.79206 32.260499 4.512695 33.38916 4.186297 33.54407 3.845801 33.67123 3.495117 33.779787ZM6.541992 35.23584C6.93551 35.03868 7.317645 34.812444 7.679688 34.561037 9.827544 33.046636 11.525344 30.60886 12.274414 28.125489L12.060547 28.5708C10.96591 30.783539 9.49856 32.84191 7.584961 34.44287 7.249528 34.721887 6.898993 34.98049 6.541992 35.23584ZM8.501953 33.347169C9.961376 32.139894 11.133912 29.95255 11.695312 28.172364 10.689031 29.935523 9.758452 31.737622 8.501953 33.347169ZM6.794922 35.288576C7.161305 35.131658 7.515236 34.943925 7.854492 34.73291 10.11714 33.292444 11.928594 30.706973 12.851562 28.243653L12.374023 29.08545C11.230782 31.037304 9.875773 32.88663 8.120117 34.348146 7.70008 34.6908 7.258808 35.000528 6.794922 35.288576ZM7.59668 35.72119C10.322301 34.200586 12.597101 31.348372 13.291992 28.33252 12.169015 31.277508 10.13198 33.81584 7.59668 35.72119ZM11.974609 32.57666C12.884408 31.46073 13.631278 29.85973 13.740234 28.422364L13.379883 29.342286C13.008909 30.255528 12.607003 31.152956 12.199219 32.053224 12.123854 32.226774 12.042377 32.39729 11.974609 32.57666ZM7.21582 36.665529C8.16912 36.36686 9.088398 35.956815 9.952148 35.452638 12.514299 33.947546 14.647083 31.479374 15.251953 28.563965L15.132812 28.908692C14.661016 30.207819 13.929397 31.407633 13.03418 32.470216 13.8575 31.297684 14.53033 29.936743 14.820312 28.641114 14.08789 30.20558 13.227047 31.70433 12.326172 33.178224 12.291367 33.236848 12.257203 33.295827 12.22168 33.354005 12.19137 33.384256 12.161427 33.41486 12.130859 33.444826 10.728285 34.8238 9.023726 35.857858 7.21582 36.665529ZM8.078125 36.996583C9.899926 36.279706 11.579381 35.195028 12.951172 33.819826 14.293263 32.43389 15.417217 30.746027 15.795898 28.845215 15.203178 30.655165 14.076804 32.261686 12.744141 33.623537 11.392791 34.991994 9.784226 36.079694 8.078125 36.996583ZM9.767578 36.686037C11.351143 35.933847 12.757529 34.82672 13.879883 33.50049 14.986272 32.169649 15.886543 30.622639 16.27246 28.935059 15.363533 31.332507 13.800281 33.45924 11.849609 35.143068 11.195459 35.70107 10.497184 36.21124 9.767578 36.686037ZM1.386719 30.615723C1.381485 30.616539 1.376332 30.61786 1.371094 30.618653V30.620606C1.376352 30.619168 1.381461 30.61718 1.386719 30.615723ZM13.362305 37.907716C15.135222 37.359857 16.904698 36.017545 18.026368 34.58252 17.832224 34.72779 17.652516 34.88621 17.464844 35.035646 16.173525 36.092908 14.819326 37.07424 13.362305 37.907716Z" fill-opacity=".26"/>
</g>
</g>
</g>






































































































































































































































































</g>
</g>
</svg>
~~~~
<!-- END FILE -->
