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
