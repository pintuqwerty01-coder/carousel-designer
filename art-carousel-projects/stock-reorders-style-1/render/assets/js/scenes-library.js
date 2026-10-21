// ART carousel scene LIBRARY (art-carousel skill). cover / reveal / cta are generic; the task scenes
// (calls, docs, stock, bills, chats, approvals) come from the "6 things" post and double as worked examples.
// A post adds its own scenes in <project>/scenes.js (Object.assign(SCENES_DYN, {...})).
// Per-slide options from content.json "opts" arrive as the global SCENE_OPTS.
// Each scene(ctx, t, S, W, H) redraws one frame.
// ONLY the robot is pixel art (pixelbot.js, posed by S = 8 steps/s). Every prop is smooth vector (props-vector.js) moving on t.
// S = pose step (0..31 over 4s). Deterministic: same t -> same frame.
// STAGE scenes (task slides) are drawn on a virtual 728x336 stage that the page scales by exactly 1.25
// (912x420 on screen). Keep every size/position a multiple of 4 so pixels stay crisp after scaling.
const lerp = (a, b, k) => a + (b - a) * Math.max(0, Math.min(1, k));
const walkLegs = S => (S % 2 ? "stepL" : "stepR");
const VF = 316, VY = VF - 23 * 8;            // stage floor (feet) and robot top for u=8

const SCENES_DYN = {

  // COVER (full frame): robot walks in along the desk, spots the paper pile, "?" -> "!", then rolls up its sleeves.
  cover(ctx, t, S, W, H) {
    // u = 10 matches task slides (8 x 1.25 stage scale). opts: x = where the robot stops (must sit on a clear patch of the
    // cover image), feet = y of its feet, from = x it walks in from (off the right edge).
    const o = (typeof SCENE_OPTS !== "undefined" && SCENE_OPTS) || {}, X = o.x ?? 812, FROM = o.from ?? 1100;
    const u = 10, FEET = o.feet ?? 1172, Y = FEET - 23 * u;
    let x = X, legs = "stand", armL = "down", armR = "down", eyes = "lookL", mouth = "o", bulb = "aqua";
    if (S < 10) { x = lerp(FROM, X, S / 9); legs = walkLegs(S); eyes = "open"; mouth = "smile"; }
    else if (S < 14) { eyes = "lookL"; mouth = "o"; }
    else if (S < 18) { eyes = "wide"; mouth = "open"; bulb = "red"; }
    else if (S < 24) { armL = S % 2 ? "flex" : "up"; armR = S % 2 ? "flex" : "up"; eyes = "focus"; mouth = "grin"; bulb = "yellow"; }
    else { armL = "flex"; armR = "flex"; eyes = S === 29 ? "blink" : "happy"; mouth = "grin"; bulb = "aqua"; }
    const hop = (S >= 24 && S <= 25) ? -20 : 0;
    vShadow(ctx, x + 120, FEET + 8, 190, -hop, true);
    drawBot(ctx, x, Y + hop, u, { legs, armL, armR, eyes, mouth, bulb, dark: true, halo: true, flip: FROM > X });   // faces the way it walks
    if (S >= 10 && S < 14) vMark(ctx, x + 120, Y - 44, "?", (t - 10 / 8) / 0.2, "q", 1.2);
    if (S >= 14 && S < 18) vMark(ctx, x + 120, Y - 44, "!", (t - 14 / 8) / 0.2, "bang", 1.2);
  },

  // 1 CLIENT UPDATES (vector props, pixel robot only): phones buzz on the desk; the robot hops from phone to phone and
  // taps each quiet; a paper plane carries the update up to that client's shop, whose window lights up with a check.
  calls(ctx, t, S) {
    // robot stands in the gap left of each phone (arms x+24..x+168; tapping hand tip = phone's left edge), never overlapping one
    const cxs = [300, 484, 668], Q = [8, 15, 22], stops = [112, 296, 480], FLY = 0.6, TOP = 292;
    const land = Q.map(q => q / 8 + FLY);
    cxs.forEach((cx, i) => vShop(ctx, cx, 6, t >= land[i], (t - land[i]) / 0.3));
    let x, legs = "stand", armR = "down", eyes = "wide", mouth = "wobble", hopY = 0;
    if (S < 6) { x = lerp(-140, stops[0], S / 6); legs = walkLegs(S); }
    else if (S >= 25) { x = stops[2]; armR = "hold"; eyes = S === 30 ? "blink" : "happy"; mouth = "smile"; }
    else {
      const i = Math.min(2, Math.floor((S - 6) / 7)), r = S - 6 - 7 * i;
      if (r < 3) { x = stops[i]; armR = r === 0 ? "reach" : "tap"; eyes = "focus"; mouth = "flat"; }
      else if (i === 2) { x = stops[2]; eyes = "happy"; mouth = "grin"; legs = r === 3 ? "tuck" : "stand"; hopY = r === 3 ? -24 : 0; }   // little victory hop
      else { const h = r - 3; x = lerp(stops[i], stops[i + 1], h / 3); legs = "tuck"; hopY = [-24, -40, -24, 0][h]; }
    }
    x = snap(x);
    vShadow(ctx, x + 96, VF + 4, 120, -hopY);
    drawBot(ctx, x, VY + hopY, 8, { legs, armR, eyes, mouth, bulb: S < 22 ? "red" : "aqua", bulbOff: S < 22 && S % 2 === 0 });
    if (S < 22) vSweat(ctx, x + 160, VY + 48 + hopY, t, 1);
    vDesk(ctx, 264, 724, TOP);
    if (S >= 25) vMug(ctx, x + 116, TOP, t - 25 / 8);
    cxs.forEach((cx, i) => {
      const q = Q[i] / 8, ring = t < q;
      vPhone(ctx, cx, TOP, t, ring, (t - q) / 0.25);
      if (ring) vRings(ctx, cx, TOP - 34, t);
      vTapBurst(ctx, cx - 22, TOP - 14, (t - (q - 0.2)) / 0.35);
      vFlight(ctx, [cx, TOP - 66], [Math.min(cx + 64, 708), 170], [cx + 4, 78], eInOut((t - q) / FLY));
      vBadge(ctx, cx + 40, 10, (t - land[i]) / 0.35);
    });
  },

  // 2 RETYPING DOCUMENTS: papers tumble onto the desk while the robot types frantically; a beam scans them once,
  // they merge into one clean document with a check, and a red flag springs up on the one mismatch.
  docs(ctx, t, S) {
    const x = 220, TOP = 284, P = [492, 572, 652], PW = 52, PH = 64, PY = TOP - PH;
    let armR = "down", eyes = "wide", mouth = "wobble", bulb = "red", bulbOff = S % 2 === 0;
    if (S < 9) { armR = S % 2 ? "tap" : "reach"; }
    else if (S < 17) { armR = "reach"; eyes = "focus"; mouth = "flat"; bulbOff = false; bulb = "yellow"; }
    else if (S < 22) { eyes = "open"; mouth = "o"; bulb = "aqua"; bulbOff = false; }
    else { armR = S % 2 ? "wave1" : "wave2"; eyes = S === 30 ? "blink" : "happy"; mouth = "grin"; bulb = "aqua"; bulbOff = false; }
    drawBot(ctx, x, VY, 8, { armR, eyes, mouth, bulb, bulbOff });
    if (S < 9) vSweat(ctx, x + 160, VY + 48, t, 1);
    vDesk(ctx, 260, 724, TOP);
    vKeyboard(ctx, 388, TOP - 12, 92, t, S < 9);
    const scanX = 484 + (712 - 484) * clamp01((t - 9 / 8) / 1.0), m = eInOut((t - 17 / 8) / 0.5);
    [0, 2, 1].forEach(i => {
      const px0 = P[i], land = (2 + 2 * i) / 8, k = (t - (land - 0.25)) / 0.25;
      if (k <= 0) return;
      let px = px0, py = PY, rot = 0, alpha = 1;
      if (k < 1) { py = lerp(-90, PY, k * k); rot = (1 - k) * (i === 1 ? 0.5 : -0.6); }
      else if (t - land < 0.16) py = PY - Math.sin((t - land) / 0.16 * Math.PI) * 6;
      if (m > 0) { px = lerp(px0, 572, m); if (i !== 1) alpha = 1 - m; }
      if (alpha <= 0) return;
      vPaper(ctx, px, py, PW, PH, { rot, alpha, head: i === 1 ? VC.A : VC.D });
      const scanned = t > 9 / 8 && scanX > px0 + PW / 2;
      if (!scanned && t >= land) vMark(ctx, px0 + PW - 4, PY - 6, "?", (t - land) / 0.2, "bang", 0.5);
    });
    if (t >= 9 / 8 && t < 17 / 8) vBeam(ctx, scanX, PY - 18, TOP);
    vFlag(ctx, 584, PY + 22, t, (t - 22 / 8) / 0.3);
    vBadge(ctx, 572 + PW - 2, PY + 2, (t - 21 / 8) / 0.35);
  },

  // 3 STOCK: boxes vanish from the shelf one by one; the robot's bulb flashes, it holds up a reorder slip,
  // an approval stamp thumps down on it (teal check), and new boxes drop into the gaps.
  stock(ctx, t, S) {
    vShelf(ctx, 400, 712, 112, [204, 296]);
    const BW = 52, BH = 44, slots = [];
    for (const by of [160, 252]) for (let c = 0; c < 4; c++) slots.push([418 + c * 72, by]);
    const goneAt = { 4: 0.25, 6: 0.5, 1: 0.75, 7: 1.0 }, backAt = { 4: 2.5, 6: 2.75, 1: 3.0, 7: 3.25 };
    slots.forEach(([bx, by], k) => {
      const g = goneAt[k];
      if (g === undefined || t < g) { vBox(ctx, bx, by, BW, BH); return; }
      const b = backAt[k];
      if (t < b) { vBox(ctx, bx, by, BW, BH, 1, 1 - eOut((t - g) / 0.15)); vPoof(ctx, bx + BW / 2, by + BH / 2, (t - g) / 0.4); }
      if (t >= b - 0.2) { const q = clamp01((t - (b - 0.2)) / 0.2); vBox(ctx, bx, lerp(by - 36, by, q * q), BW, BH, clamp01(q * 2)); }
    });
    let x, legs = "stand", armR = "down", eyes = "open", mouth = "smile", bulb = "aqua", bulbOff = false;
    if (S < 6) { x = lerp(-60, 160, S / 6); legs = walkLegs(S); eyes = "lookR"; }
    else if (S < 10) { x = 160; eyes = "wide"; mouth = "o"; bulb = "red"; bulbOff = S % 2 === 0; }
    else if (S < 20) { x = 160; armR = "up"; eyes = "focus"; mouth = "flat"; bulb = "yellow"; }
    else if (S < 28) { x = 160; armR = "up"; eyes = "happy"; mouth = "grin"; }
    else { x = 160; armR = S % 2 ? "wave1" : "wave2"; eyes = S === 30 ? "blink" : "happy"; mouth = "grin"; }
    x = snap(x);
    vShadow(ctx, x + 96, VF + 4, 120);
    drawBot(ctx, x, VY, 8, { legs, armR, eyes, mouth, bulb, bulbOff });
    if (S >= 6 && S < 10) vMark(ctx, x + 96, VY - 40, "!", (t - 6 / 8) / 0.2, "bang");
    if (t >= 1.25 && t < 3.6) {                          // reorder slip held up by the raised hand
      const a = Math.min(clamp01((t - 1.25) / 0.12), clamp01((3.6 - t) / 0.12));
      vSlip(ctx, 324, 160, 44, 56, { alpha: a });
      vStampMark(ctx, 346, 196, (t - 2.125) / 0.3);
      let sy = null;                                     // stamp: drops, thumps, lifts away
      if (t >= 1.875 && t < 2.125) { const q = (t - 1.875) / 0.25; sy = lerp(-10, 200, q * q); }
      else if (t >= 2.125 && t < 2.275) sy = 200;
      else if (t >= 2.275 && t < 2.55) sy = lerp(200, -10, eOut((t - 2.275) / 0.275));
      if (sy !== null) vStamp(ctx, 346, sy);
    }
  },

  // 4 MATCHING BILLS: detective robot hops from document to document with a magnifier (standing in the gap left of each);
  // PO and delivery note link up in aqua with checks, the invoice links in red and gets flagged.
  bills(ctx, t, S) {
    const cxs = [296, 480, 664], stops = [112, 296, 480], TOP = 292, DW = 44, DH = 60, DY = TOP - DH;   // doc right edge < next stop's left arm
    let x, legs = "stand", eyes = "squint", mouth = "smile", armR = "reach", hopY = 0, bulb = "aqua";
    if (S < 6) { x = lerp(-140, stops[0], S / 6); legs = walkLegs(S); eyes = "open"; }
    else if (S < 12) { x = stops[0]; eyes = S % 3 === 0 ? "lookR" : "squint"; }
    else if (S < 15) { x = lerp(stops[0], stops[1], (S - 11) / 3); legs = "tuck"; hopY = [-20, -28, 0][S - 12]; }
    else if (S < 18) { x = stops[1]; }
    else if (S < 21) { x = lerp(stops[1], stops[2], (S - 17) / 3); legs = "tuck"; hopY = [-20, -28, 0][S - 18]; }
    else if (S < 25) { x = stops[2]; if (S >= 22) { eyes = "wide"; mouth = "o"; bulb = "red"; } }
    else { x = stops[2]; eyes = S === 30 ? "blink" : "happy"; mouth = "grin"; armR = S % 2 ? "wave1" : "wave2"; }
    x = snap(x);
    // links arc high above the robot's head, drawn behind everything
    vCurve(ctx, [cxs[0], DY - 4], [(cxs[0] + cxs[1]) / 2, -20], [cxs[1], DY - 4], (t - 15 / 8) / 0.25, VC.A);
    vCurve(ctx, [cxs[1], DY - 4], [(cxs[1] + cxs[2]) / 2, -20], [cxs[2], DY - 4], (t - 22 / 8) / 0.3, VC.R);
    vShadow(ctx, x + 96, VF + 4, 120, -hopY);
    drawBot(ctx, x, VY + hopY, 8, { legs, eyes, mouth, armR, bulb });
    vDesk(ctx, 256, 724, TOP);
    [[VC.A, "PO"], [VC.D, "DN"], [VC.K, "INV"]].forEach(([head, label], i) => vPaper(ctx, cxs[i] - DW / 2, DY, DW, DH, { head, label }));
    vBadge(ctx, cxs[0] + 22, DY + 4, (t - 17 / 8) / 0.35);
    vBadge(ctx, cxs[1] + 22, DY + 4, (t - 17 / 8 - 0.08) / 0.35);
    vMark(ctx, cxs[2] + 22, DY - 18, "!", (t - 24 / 8) / 0.2, "bang", 0.7);
    if (armR === "reach") vLens(ctx, x + 194 + Math.sin(t * 9) * 5, VY + hopY + 106 + Math.cos(t * 7) * 3, 17, x + 172, VY + hopY + 124);
  },

  // 5 CHASING VENDORS: chat bubbles chase the robot across the stage; it sets down a tray, the bubbles file in neatly,
  // a follow-up flies out, the reply lands on the stack, check. Ends with tea.
  chats(ctx, t, S) {
    let x, flip = false, legs = "stand", armR = "down", eyes = "wide", mouth = "wobble", bulb = "red";
    if (S < 13) { x = lerp(420, 40, S / 12); flip = true; legs = walkLegs(S); }
    else if (S < 19) { x = 40; eyes = "focus"; mouth = "flat"; bulb = "yellow"; armR = "reach"; }
    else if (S < 25) { x = 40; eyes = "open"; mouth = "smile"; bulb = "aqua"; armR = S < 21 ? "tap" : "down"; }
    else { x = 40; armR = "hold"; eyes = S === 29 ? "blink" : "happy"; mouth = "smile"; bulb = "aqua"; }
    x = snap(x);
    const T = { x: 276, y: 292, w: 96, h: 24 }, tFile = 13 / 8;
    const xcAt = tt => lerp(420, 40, clamp01(tt * 8 / 12));
    vShadow(ctx, x + 96, VF + 4, 120);
    drawBot(ctx, x, VY, 8, { legs, armR, eyes, mouth, bulb, flip });
    if (S < 13) vSweat(ctx, x + 160, VY + 48, t, 1);
    if (S >= 25) vMug(ctx, x + 150, VY + 146, t - 25 / 8);
    const trayIn = clamp01((t - tFile + 0.15) / 0.15);
    if (trayIn > 0) { ctx.save(); ctx.globalAlpha = trayIn; vTrayBack(ctx, T.x, T.y, T.w, T.h); ctx.restore(); }
    for (let j = 0; j < 6; j++) {
      const tb = (1 + 2 * j) / 8; if (t < tb) continue;
      const col = j % 2 ? VC.S : VC.A;
      const chase = tt => [lerp(760, xcAt(tt) + 190 + (j % 3) * 64 + Math.floor(j / 3) * 96, eOut((tt - tb) / 0.5)), 20 + (j % 3) * 62 + Math.floor(j / 3) * 30 + Math.sin(tt * 8 + j) * 6];
      if (t < tFile) { const [bx, by] = chase(t); vBubble(ctx, bx, by, 1, col, t, j); continue; }
      const k = eInOut((t - tFile - j * 0.06) / 0.4), [x0, y0] = chase(tFile);
      vBubble(ctx, lerp(x0, T.x + 10 + (j % 2) * 40, k), lerp(y0, T.y - 22 - Math.floor(j / 2) * 12, k), lerp(1, 0.6, k), col, t, j);
    }
    const kr = eInOut((t - 22 / 8) / 0.45);
    if (kr > 0) vBubble(ctx, lerp(700, T.x + 26, kr), lerp(24, T.y - 58, kr), lerp(1, 0.6, kr), VC.Y, t, 9);
    if (trayIn > 0) { ctx.save(); ctx.globalAlpha = trayIn; vTrayFront(ctx, T.x, T.y, T.w, T.h); ctx.restore(); }
    vFlight(ctx, [340, 250], [560, 260], [716, 44], eInOut((t - 19 / 8) / 0.5));
    vBadge(ctx, T.x + T.w + 18, T.y - 34, (t - 26 / 8) / 0.35);
  },

  // 6 SMALL APPROVALS: the robot runs a booth beside a conveyor gate; small slips roll through and get a check,
  // the big one stops, a bell rings and a ping goes to your phone; you approve and it rolls on.
  approvals(ctx, t, S) {
    const RX = 200, RY = VY - 24, gate = 440, GW = 64, BT = 300, stopA = 2.5, stopB = 3.25;
    const travel = tt => 256 * Math.min(tt, stopA) + 320 * Math.max(0, tt - stopB);
    const stopped = t >= stopA && t < stopB, off = travel(t);
    let armR = "down", eyes = "open", mouth = "smile", bulb = "aqua";
    if (S >= 20 && S < 26) { armR = "reach"; eyes = "wide"; mouth = "o"; bulb = "yellow"; }
    else if (S >= 27) { armR = "hold"; eyes = S === 30 ? "blink" : "happy"; mouth = "smile"; }
    else if (S % 4 < 2) { armR = "wave1"; }
    drawBot(ctx, RX, RY, 8, { armR, eyes, mouth, bulb });
    rr(ctx, RX + 24, RY + 160, 160, BT - RY - 160, [8, 8, 0, 0]); fs(ctx, VC.T, VC.K, 3);      // booth front (hides legs)
    rr(ctx, RX + 18, RY + 156, 172, 9, 4.5); fs(ctx, VC.K);
    if (S >= 27) vMug(ctx, RX + 152, RY + 156, t - 27 / 8);
    const small = [200, 60, -80].map(x0 => x0 + off), big = -276 + off;
    const passing = small.some(px => px > gate - 32 && px < gate + GW);
    vGate(ctx, gate, GW, 156, BT, stopped ? VC.R : passing ? VC.A : VC.G);
    vBelt(ctx, 0, 728, BT, 36, off);
    small.forEach(px => { vSlip(ctx, px, BT - 28, 32, 28); if (px > gate + GW) vBadge(ctx, px + 16, BT - 46, (px - gate - GW) / 60, 12); });
    vSlip(ctx, big, BT - 32, 76, 32, { big: true });
    if (t >= stopB && big > gate + GW) vBadge(ctx, big + 38, BT - 50, (big - gate - GW) / 60);
    if (t >= stopA) {
      if (stopped) {
        vBell(ctx, 556, 100, Math.sin(t * 22) * 0.35, true, t);
        vCurve(ctx, [586, 80], [612, 40], [640, 64], (t - stopA - 0.12) / 0.25, VC.A, { arrow: true, dash: [6, 7], lw: 3 });
        vMark(ctx, 702, 26, "!", (t - stopA - 0.3) / 0.2, "bang", 0.55);
      }
      vPhone(ctx, 676, 104, t, stopped, (t - stopB) / 0.25, "bell");
    }
  },

  // REVEAL (full frame, dark): robot walks in, looks up at the logo, hops, waves with a heart.
  reveal(ctx, t, S) {
    const u = 10, FEET = 1196, Y = FEET - 23 * u;   // u = 10 matches task slides
    let x = 788, legs = "stand", armR = "down", eyes = "open", mouth = "smile";
    if (S < 9) { x = lerp(1100, 788, S / 8); legs = walkLegs(S); }
    else if (S < 13) { eyes = "lookL"; mouth = "o"; }
    else if (S < 15) { legs = "tuck"; eyes = "happy"; mouth = "grin"; }
    else if (S < 25) { armR = S % 2 ? "wave1" : "wave2"; eyes = "happy"; mouth = "grin"; }
    else { armR = "wave2"; eyes = S === 29 ? "blink" : "happy"; mouth = "grin"; }
    const hop = (S === 13 || S === 14) ? -28 : 0;
    vShadow(ctx, x + 120, FEET + 8, 190, -hop, true);
    drawBot(ctx, x, Y + hop, u, { legs, armR, eyes, mouth, dark: true, halo: true, flip: true });
    vHeart(ctx, x + 120, Y - 44 + Math.sin(t * 6) * 6, eBack((t - 2) / 0.3) * 1.5);
  },

  // CTA (white card on aqua): robot pops up, points left at the chips as they light up one by one, then grins.
  cta(ctx, t, S) {
    const u = 10, FEET = 272, Y = FEET - 23 * u, x = 56;   // u = 10 matches task slides; centred in the card
    let armR = "reach", eyes = "lookL", mouth = "grin", legs = "stand";
    const y = S < 4 ? lerp(320, Y, S / 3) : (S === 4 ? Y - 20 : Y);
    if (S < 5) { armR = "up"; legs = "tuck"; eyes = "happy"; }
    else if (S >= 20) { armR = S % 2 ? "wave1" : "wave2"; eyes = S === 28 ? "blink" : "happy"; }
    else if (S % 2) armR = "tap";
    vShadow(ctx, x + 120, FEET + 6, 150, FEET - 230 - y);
    drawBot(ctx, x, y, u, { legs, armR, eyes, mouth, flip: true });
  },
};

// bottom trail (smooth vector): dotted aqua line across the full width, solid up to this slide's progress,
// half-gears on the seams so the swipe joins up, and a tiny pixel robot head (the mascot) as the marker.
function drawTrail(ctx, W, i, n, k, dark, aqua) {
  const y = 22, dot = aqua ? "rgba(26,26,26,.35)" : dark ? "rgba(4,173,195,.55)" : "rgba(4,173,195,.45)", main = aqua ? VC.K : VC.A;
  ctx.fillStyle = dot;
  for (let x = 12; x < W; x += 24) { ctx.beginPath(); ctx.arc(x, y, 4, 0, Math.PI * 2); ctx.fill(); }
  const end = lerp((i - 1) / n, i / n, k) * W;
  ctx.save(); ctx.strokeStyle = main; ctx.lineWidth = 8; ctx.lineCap = "round";
  ctx.beginPath(); ctx.moveTo(-8, y); ctx.lineTo(Math.max(0, end), y); ctx.stroke(); ctx.restore();
  if (i > 1) vGear(ctx, 0, y, 24, main);
  if (i < n) vGear(ctx, W, y, 24, main);
  const mx = snap(end) - 20;
  pxr(ctx, mx, 0, 40, 40, main); pxr(ctx, mx + 6, 8, 28, 22, C8.W);
  pxr(ctx, mx + 11, 13, 6, 6, C8.K); pxr(ctx, mx + 23, 13, 6, 6, C8.K);
  pxr(ctx, mx + 17, -12, 6, 12, dark ? C8.W : C8.K); pxr(ctx, mx + 14, -18, 12, 8, aqua ? C8.W : C8.A);
}
