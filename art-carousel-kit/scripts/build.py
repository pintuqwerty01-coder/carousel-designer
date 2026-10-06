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
