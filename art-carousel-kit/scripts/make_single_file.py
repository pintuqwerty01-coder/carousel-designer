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
