# Actual 3D container motion preview

This revision replaces the clipped-image translation with a Blender scene: individual container shells, corrugated steel panels, hinged doors, locking rods, brackets, castings, pallet and cartons. The middle right door opens 24 degrees, pauses and closes. Its hardware follows the same hinge and the render computes perspective, lighting and occlusion. The stack and text stay fixed.

The supplied cover is the visual direction; these are rebuilt objects, not a pixel-identical conversion of that image. Preview for review only. The previous image-layer proof is preserved separately.

Source: model.py and scene.blend. Render: Blender 4.3.2 Eevee, alpha PNG sequence at 15 samples per second, composited over the fixed HTML background and interpolated to 30 fps for the 4-second 1080×1350 MP4. Frozen identical poses reuse their render. Source HTML retains the supplied copy.
