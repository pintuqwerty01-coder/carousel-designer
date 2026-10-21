# Stock reorders — integrated photographic design, revision 5

The user requested that design and background work together, and that typography follow the Style 1 guide. The approved script and the illustrative ₹10,000 limit / ₹6,000 automatic order / ₹15,000 approval request are unchanged.

## Design rationale

- **Photo-first composition:** each scene uses its pictured desk, shelves or cartons. Duplicate cartoon shelving and conveyors have been removed.
- **A clear reading order:** headline, supporting copy, then the scene. Supporting copy is no longer detached into a generic bottom strip.
- **Canonical Style 1 fonts:** actual Preahvihear Regular for headlines; actual Poppins Medium for body copy and labels, Poppins Semibold for amounts and brand text. No synthetic bold or italic. Preahvihear lacks the curly apostrophe, so only that character uses the approved Poppins Regular instead of a system-serif fallback; approved wording and punctuation stay intact. The browser's rendered font names and glyph counts are checked through the Chrome DevTools font API.
- **Consistent brand system:** white/ink/aqua; green only for completion marks. Original 240px pixel mascot, stepped poses and smoothly eased vector annotations.
- **Legibility:** dark headroom behind text; static copy from frame one; 84px safe margins; scene elements stay below copy.
- **Contextual motion:** scans follow the pictured rack, a paper highlight sits over the pictured records, and the incoming check links real cartons. There is one mascot per slide, including the two-path example.
- **Compact threshold layout:** 270px-tall cards replace 638px panels. The image and the two paths remain visible. The amount examples resolve sequentially and then hold for comparison.

## Scene anchors

| Slide | Photographic setting | Action |
| --- | --- | --- |
| 01 | Warehouse aisle, real stocked shelves | Mascot presents the prepared reorder beside the aisle. |
| 02 | Record-checking table with real papers and phone | Mascot faces the paperwork; the highlight follows the paper stack and the alert points to the phone. |
| 03 | Low-stock shelf and open floor | Scanner tracks the photographed rack; the alert stays attached to its shelf area. |
| 04 | Stock and a dispatch cart | The check connects the pictured stock and incoming cartons, with a magnifier beside the mascot. |
| 05 | Warehouse aisle | One mascot routes a ₹6,000 order directly and a ₹15,000 request to a person, against a ₹10,000 example limit. |
| 06 | Review desk | The request and human review choices sit at the desk. No approval is assumed. |
| 07 | Dispatch area | Completed routine work is marked on actual cartons; a human receives the exception. |
| 08 | Stockroom workbench | Rule controls occupy the desk while the mascot gestures toward stock flow. |

Backgrounds are existing generated photorealistic assets from this repository, not photographs of an identified real business. Sources: `festive-dispatch-realistic/slides/assets/cover-art.png` and `festive-dispatch-photo/slides/assets/clean-02.png` through `clean-06.png`. The source bitmaps are preserved unchanged. No new paid generation was used.

## Reproduce

```bash
source /workspace/art-carousel-venv/bin/activate
cd /workspace/carousel-designer/art-carousel-projects/stock-reorders-style-1-integrated
python build.py
python /workspace/art-carousel-kit/run-system-browser.py /workspace/art-carousel-kit/scripts/stills.py "$PWD"
python /workspace/art-carousel-kit/run-system-browser.py /workspace/art-carousel-kit/scripts/sheets.py "$PWD"
export npm_config_cache=/workspace/art-carousel-npm-cache HYPERFRAMES_BROWSER_PATH=/usr/bin/chromium
python render-lossless.py
python audit.py
python package.py
```

Per-slide masters: 1080 × 1350, 30fps, 120 frames, four seconds. Copy, font usage, margins, real image loading, stationary text, actual scene motion, JavaScript errors and final video metadata are checked. Frame sheets support visual staging review. The combined MP4/GIF are compressed review copies; the ZIP contains individual videos, native-size JPEGs, an eight-page raster PDF and a validation report.

Delivered on the separate `stock-reorders-style-1-v5` branch. Earlier versions are preserved.
