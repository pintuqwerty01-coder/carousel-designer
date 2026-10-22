# Static v8 — character consistency review

All eight scenes are corrected against the same canonical `../slides/assets/mascot-point.png` reference. The latest static-v7 marketing copy, original logo, Preahvihear type, layout, photographic settings and purposeful actions are retained. This revision is for review.

See `character-spec.md` for model details: body proportions, head silhouette, limb lengths and thickness, material colour, chest panel, antenna, shoes and facial grid. Image generation makes localized character corrections using both the scene and canonical reference; it is not a shared 3D mesh, so perspective and lighting still require visual comparison.

Special corrections: slide 2 hanging arm shortened/bent to canonical proportions; slide 3 torso and legs restored to normal standing proportions; slide 4 face simplified to the same square-eye grid as the other focused task scenes. Expressions continue to match the slide messages.

`content.json` is unchanged in wording from v7. `slides/` contains editable text/layout compositions and `assets/` contains corrected scene images. `render.py` verifies copy, fonts and layout, renders native 1080×1350 PNGs and creates the full PDF with vector text plus high-quality individual JPEGs. Original scenes and all previous deliveries remain archived in their existing directories.
