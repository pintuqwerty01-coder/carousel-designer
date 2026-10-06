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
