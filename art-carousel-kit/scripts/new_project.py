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
