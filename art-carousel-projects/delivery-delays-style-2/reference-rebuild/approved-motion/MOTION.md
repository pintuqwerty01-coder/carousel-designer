# Visible story motion — Style 2

The MD calls for one calm story moment per object. Earlier small glow-only props have been replaced with actual prop actions. Ambient floating remains disabled according to the user's feedback.

1. Loaded cover pallet rolls 22px once. The attached clock follows the mounting post exactly; hands continue a smooth mechanical sweep.
2. Native setup sequence: four numbered circles activate.
3. Pickup pallet rolls 45px toward its handoff position, stops, then the collection docket is flagged. The docket marker is attached to the moving pallet.
4. Exact approved truck roll → stop → amber flag; untouched HTML and MP4.
5. Goods remain held behind the checkpoint; the actual clock hands advance 75° while the hour hand moves at 1/12 speed. The old scan/glow proxy is removed. Clock-face asset edited to remove baked hands first.
6. Phone and empty tray stay still; a separate 3D envelope moves outward once to represent a proactive customer update. No looping floating or page storm. Uses the native `drive` motion on the message object.
7. Native ART logo hand sweep.
8. Native outcome checks and small completed-delivery truck roll.
9. Native CTA glow.

`clock_sweep` is the added project moment type. Its two vector hands are rendered over the handless clock face and updated by R(t) as a pure function, so seeking and export are deterministic. All typography stays fixed.
