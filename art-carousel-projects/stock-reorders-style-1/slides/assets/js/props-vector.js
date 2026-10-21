// ART smooth vector props (Aiotrix kit). RULE: only the robot mascot is pixel art; every other element is
// smooth, anti-aliased flat vector, and moves on continuous time t with easing (the robot steps at 8 poses/s).
// GL/GM/GD = accent teal-green (light -> mid -> deep). ONLY for result chips, lit shop windows and check marks
const VC = { GL: "#41A486", GM: "#2B907F", GD: "#1C5E55", A: "#04ADC3", K: "#1A1A1A", W: "#FFFFFF", T: "#DDF3F7", S: "#9BE3EC", R: "#F27A7A", Y: "#FFD166", G: "#D9D9D9", D: "#5A5A5A" };
const clamp01 = k => Math.max(0, Math.min(1, k));
const eOut = k => 1 - Math.pow(1 - clamp01(k), 3);
const eInOut = k => { k = clamp01(k); return k < .5 ? 4 * k * k * k : 1 - Math.pow(-2 * k + 2, 3) / 2; };
const eBack = k => { k = clamp01(k); const c1 = 1.70158, c3 = c1 + 1; return 1 + c3 * Math.pow(k - 1, 3) + c1 * Math.pow(k - 1, 2); };
const rr = (ctx, x, y, w, h, r) => { ctx.beginPath(); ctx.roundRect(x, y, w, h, r); };
const fs = (ctx, fill, stroke, lw) => { if (fill) { ctx.fillStyle = fill; ctx.fill(); } if (stroke) { ctx.strokeStyle = stroke; ctx.lineWidth = lw || 3; ctx.lineJoin = "round"; ctx.stroke(); } };

// soft ellipse shadow under the robot's feet (shrinks while it hops)
function vShadow(ctx, cx, y, w, lift = 0, dark = false) {
  const s = 1 - Math.min(0.5, lift / 80);
  ctx.save(); ctx.globalAlpha = dark ? 0.35 : 0.13; ctx.fillStyle = VC.K;
  ctx.beginPath(); ctx.ellipse(cx, y, (w / 2) * s, 7 * s, 0, 0, Math.PI * 2); ctx.fill(); ctx.restore();
}

// desk: rounded ink top + soft aqua front panel with drawer handles
function vDesk(ctx, x0, x1, top, h = 44) {
  rr(ctx, x0 + 10, top + 8, x1 - x0 - 20, h, [0, 0, 12, 12]); fs(ctx, VC.T);
  ctx.fillStyle = "rgba(4,173,195,.35)";
  for (const dx of [0.22, 0.5, 0.78]) { rr(ctx, x0 + (x1 - x0) * dx - 22, top + 24, 44, 6, 3); ctx.fill(); }
  rr(ctx, x0, top, x1 - x0, 14, 7); fs(ctx, VC.K);
}

// Material "call" handset glyph (Apache 2.0), 24x24 box
const HANDSET = new Path2D("M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z");
function tick(ctx, cx, cy, s, color, lw, k = 1) {   // self-drawing check mark, k = 0..1
  const P = [[-0.5, 0.05], [-0.15, 0.4], [0.55, -0.4]].map(([a, b]) => [cx + a * s, cy + b * s]);
  const L1 = Math.hypot(P[1][0] - P[0][0], P[1][1] - P[0][1]), L2 = Math.hypot(P[2][0] - P[1][0], P[2][1] - P[1][1]);
  let d = clamp01(k) * (L1 + L2);
  ctx.save(); ctx.strokeStyle = color; ctx.lineWidth = lw; ctx.lineCap = "round"; ctx.lineJoin = "round"; ctx.beginPath(); ctx.moveTo(...P[0]);
  if (d <= L1) ctx.lineTo(P[0][0] + (P[1][0] - P[0][0]) * d / L1, P[0][1] + (P[1][1] - P[0][1]) * d / L1);
  else { ctx.lineTo(...P[1]); d -= L1; ctx.lineTo(P[1][0] + (P[2][0] - P[1][0]) * d / L2, P[1][1] + (P[2][1] - P[1][1]) * d / L2); }
  ctx.stroke(); ctx.restore();
}

// smartphone standing on the desk. ring = buzzing with an incoming call; else quiet with a check on the screen.
function vPhone(ctx, cx, bottom, t, ring, quietK = 1, icon = "call") {
  const w = 38, h = 62, ang = ring ? Math.sin(t * 52) * 0.1 : 0;
  ctx.save(); ctx.translate(cx, bottom); ctx.rotate(ang);
  rr(ctx, -w / 2, -h, w, h, 9); fs(ctx, VC.K);
  rr(ctx, -w / 2 + 4, -h + 7, w - 8, h - 16, 5); fs(ctx, ring ? VC.A : VC.T);
  rr(ctx, -6, -6, 12, 3, 1.5); fs(ctx, "#5A5A5A");
  if (ring) {
    const p = 1 + Math.sin(t * 18) * 0.08;
    if (icon === "bell") { ctx.save(); ctx.translate(0, -h / 2 - 2); ctx.scale(p, p); bellPath(ctx); fs(ctx, VC.W); ctx.beginPath(); ctx.arc(0, 11, 3, 0, 7); fs(ctx, VC.W); ctx.restore(); }
    else { ctx.save(); ctx.translate(0, -h / 2 - 2); ctx.scale(p, p); ctx.translate(-12, -12); ctx.fillStyle = VC.W; ctx.fill(HANDSET); ctx.restore(); }
  } else tick(ctx, 0, -h / 2 - 2, 18, VC.GM, 4, quietK);
  ctx.restore();
}

// expanding ring waves either side of a ringing phone
function vRings(ctx, cx, cy, t) {
  ctx.save(); ctx.lineCap = "round"; ctx.strokeStyle = VC.A; ctx.lineWidth = 3.5;
  for (let j = 0; j < 2; j++) {
    const ph = (t * 2.4 + j * 0.5) % 1, r = 26 + ph * 22;
    ctx.globalAlpha = (1 - ph) * 0.9;
    ctx.beginPath(); ctx.arc(cx, cy, r, -0.55, 0.55); ctx.stroke();
    ctx.beginPath(); ctx.arc(cx, cy, r, Math.PI - 0.55, Math.PI + 0.55); ctx.stroke();
  }
  ctx.restore();
}

// little impact burst where the robot's hand taps (k = 0..1)
function vTapBurst(ctx, x, y, k) {
  if (k <= 0 || k >= 1) return;
  ctx.save(); ctx.strokeStyle = VC.K; ctx.lineWidth = 3; ctx.lineCap = "round"; ctx.globalAlpha = 1 - k;
  for (const a of [-2.3, -1.57, -0.85]) {
    const r0 = 8 + k * 8, r1 = 16 + k * 10;
    ctx.beginPath(); ctx.moveTo(x + Math.cos(a) * r0, y + Math.sin(a) * r0); ctx.lineTo(x + Math.cos(a) * r1, y + Math.sin(a) * r1); ctx.stroke();
  }
  ctx.restore();
}

// client storefront: striped scalloped awning, window, door. lit = update received (warm window), bump = 0..1 squash on arrival
function vShop(ctx, cx, top, lit, bump = 1) {
  const w = 96, x = -w / 2, sq = bump < 1 ? 1 - Math.sin(clamp01(bump) * Math.PI) * 0.07 : 1;
  ctx.save(); ctx.translate(cx, top + 76); ctx.scale(1 / sq, sq); ctx.translate(0, -76);
  rr(ctx, x + 6, 18, w - 12, 58, [0, 0, 6, 6]); fs(ctx, VC.W, VC.K, 3);
  let win = VC.T;
  if (lit) { win = ctx.createLinearGradient(0, 36, 0, 62); win.addColorStop(0, VC.GL); win.addColorStop(1, VC.GD);
    ctx.save(); ctx.shadowColor = "rgba(65,164,134,.85)"; ctx.shadowBlur = 16; rr(ctx, x + 16, 36, 36, 26, 4); fs(ctx, win); ctx.restore(); }
  rr(ctx, x + 16, 36, 36, 26, 4); fs(ctx, win, VC.K, 2.5);
  ctx.strokeStyle = VC.K; ctx.lineWidth = 2; ctx.beginPath(); ctx.moveTo(x + 34, 36); ctx.lineTo(x + 34, 62); ctx.stroke();
  rr(ctx, x + 60, 38, 22, 38, [5, 5, 0, 0]); fs(ctx, VC.K);
  ctx.fillStyle = VC.Y; ctx.beginPath(); ctx.arc(x + 76, 58, 2, 0, 7); ctx.fill();
  // awning
  const n = 6, sw = w / n;
  for (let i = 0; i < n; i++) {
    const c = i % 2 ? VC.W : VC.A, sx = x + i * sw;
    ctx.beginPath(); ctx.moveTo(sx, 4); ctx.lineTo(sx + sw, 4); ctx.lineTo(sx + sw, 18); ctx.arc(sx + sw / 2, 18, sw / 2, 0, Math.PI); ctx.closePath(); fs(ctx, c);
  }
  ctx.beginPath(); ctx.moveTo(x, 18); ctx.lineTo(x, 4); ctx.quadraticCurveTo(x, 0, x + 4, 0); ctx.lineTo(x + w - 4, 0); ctx.quadraticCurveTo(x + w, 0, x + w, 4); ctx.lineTo(x + w, 18);
  for (let i = n - 1; i >= 0; i--) ctx.arc(x + i * sw + sw / 2, 18, sw / 2, 0, Math.PI);
  ctx.closePath(); fs(ctx, null, VC.K, 3);
  ctx.restore();
}

// paper plane pointing along angle ang, scale s
function vPlane(ctx, x, y, ang, s = 1, alpha = 1) {
  ctx.save(); ctx.globalAlpha = alpha; ctx.translate(x, y); ctx.rotate(ang); ctx.scale(s, s);
  ctx.beginPath(); ctx.moveTo(16, 0); ctx.lineTo(-14, -12); ctx.lineTo(-6, 0); ctx.closePath(); fs(ctx, VC.W, VC.K, 2.5);
  ctx.beginPath(); ctx.moveTo(16, 0); ctx.lineTo(-6, 0); ctx.lineTo(-14, 11); ctx.closePath(); fs(ctx, VC.A, VC.K, 2.5);
  ctx.restore();
}
// quadratic bezier point + tangent
const qb = (p0, p1, p2, k) => [(1 - k) * (1 - k) * p0[0] + 2 * (1 - k) * k * p1[0] + k * k * p2[0], (1 - k) * (1 - k) * p0[1] + 2 * (1 - k) * k * p1[1] + k * k * p2[1]];
const qbAng = (p0, p1, p2, k) => Math.atan2(2 * (1 - k) * (p1[1] - p0[1]) + 2 * k * (p2[1] - p1[1]), 2 * (1 - k) * (p1[0] - p0[0]) + 2 * k * (p2[0] - p1[0]));
// a plane flying p0 -> p2 along a curve with a dashed trail behind it; k = 0..1 (already eased by caller)
function vFlight(ctx, p0, p1, p2, k) {
  if (k <= 0 || k >= 1) return;
  ctx.save(); ctx.setLineDash([6, 8]); ctx.lineCap = "round"; ctx.strokeStyle = VC.A; ctx.lineWidth = 3; ctx.globalAlpha = 0.55;
  ctx.beginPath(); ctx.moveTo(...p0);
  for (let j = 1; j <= 24; j++) ctx.lineTo(...qb(p0, p1, p2, (k * j) / 24));
  ctx.stroke(); ctx.restore();
  const [x, y] = qb(p0, p1, p2, k), s = k > 0.8 ? 1 - (k - 0.8) / 0.2 * 0.6 : 1;
  vPlane(ctx, x, y, qbAng(p0, p1, p2, k), s);
}

// aqua check badge that pops in with overshoot (k = 0..1 over the pop)
function vBadge(ctx, cx, cy, k, r = 15) {
  if (k <= 0) return;
  const s = eBack(k);
  ctx.save(); ctx.translate(cx, cy); ctx.scale(s, s);
  const g = ctx.createLinearGradient(-r, -r, r, r); g.addColorStop(0, VC.GL); g.addColorStop(1, VC.GD);
  ctx.beginPath(); ctx.arc(0, 0, r, 0, Math.PI * 2); fs(ctx, g, VC.W, 3);
  tick(ctx, 0, 0, r * 1.05, VC.W, 3.5, clamp01(k * 1.6 - 0.4));
  ctx.restore();
}

// sweat drops flicking off the robot's head (stress)
function vSweat(ctx, x, y, t, dir = 1) {
  for (let j = 0; j < 2; j++) {
    const ph = (t * 1.8 + j * 0.5) % 1;
    const dx = dir * (6 + ph * 26), dy = -18 * Math.sin(ph * Math.PI) + ph * 22;
    ctx.save(); ctx.globalAlpha = 1 - ph * ph; ctx.translate(x + dx, y + dy); ctx.rotate(dir * 0.5);
    ctx.beginPath(); ctx.moveTo(0, -9); ctx.bezierCurveTo(6, -2, 7, 4, 0, 7); ctx.bezierCurveTo(-7, 4, -6, -2, 0, -9); fs(ctx, VC.S, VC.A, 2);
    ctx.restore();
  }
}

// mug with the handle on the left (towards the robot's hand) + soft wavy steam; t = time since it appeared
function vMug(ctx, x, bottom, t) {
  const w = 32, h = 34, top = bottom - h, k = eBack(t / 0.3);
  ctx.save(); ctx.translate(x + w / 2, bottom); ctx.scale(k, k); ctx.translate(-x - w / 2, -bottom);
  ctx.save(); ctx.strokeStyle = VC.K; ctx.lineWidth = 4; ctx.beginPath(); ctx.arc(x, top + 15, 9, Math.PI * 0.5, Math.PI * 1.5); ctx.stroke(); ctx.restore();
  rr(ctx, x, top, w, h, [3, 3, 9, 9]); fs(ctx, VC.W, VC.K, 3);
  rr(ctx, x + 1.5, top + 12, w - 3, 8, 0); fs(ctx, VC.A);
  ctx.restore();
  ctx.save(); ctx.strokeStyle = "rgba(90,90,90,.55)"; ctx.lineWidth = 3; ctx.lineCap = "round";
  for (let j = 0; j < 3; j++) {
    const ph = (t * 0.8 + j / 3) % 1; ctx.globalAlpha = Math.sin(ph * Math.PI) * clamp01(t / 0.3);
    const sx = x + 6 + j * 10, sy = top - 4 - ph * 14;
    ctx.beginPath();
    for (let q = 0; q <= 14; q++) { const yy = sy - q * 2, xx = sx + Math.sin(q * 0.55 + t * 5 + j * 2) * 3; q ? ctx.lineTo(xx, yy) : ctx.moveTo(xx, yy); }
    ctx.stroke();
  }
  ctx.restore();
}

// gear (for the trail seams). evenodd hole.
function vGear(ctx, cx, cy, r, color, rot = 0, teeth = 8) {
  const ri = r * 0.74, N = teeth * 4;
  ctx.save(); ctx.translate(cx, cy); ctx.rotate(rot); ctx.beginPath();
  for (let j = 0; j <= N; j++) { const a = (j / N) * Math.PI * 2, rad = (j % 4 < 2) ? r : ri; j ? ctx.lineTo(Math.cos(a) * rad, Math.sin(a) * rad) : ctx.moveTo(Math.cos(a) * rad, Math.sin(a) * rad); }
  ctx.closePath(); ctx.moveTo(r * 0.32, 0); ctx.arc(0, 0, r * 0.32, 0, Math.PI * 2, true);
  ctx.fillStyle = color; ctx.fill("evenodd"); ctx.restore();
}

// ---- props for the other scenes ----
const _ink = (ctx, font, color) => { ctx.font = font; ctx.fillStyle = color; ctx.textAlign = "center"; ctx.textBaseline = "middle"; };

// speech mark over the robot: "?" (white) or "!" (red); pops in with overshoot. s = size factor
function vMark(ctx, cx, cy, ch, k, kind = "q", s = 1) {
  if (k <= 0) return;
  const bg = kind === "bang" ? VC.R : VC.W, fg = kind === "bang" ? VC.W : VC.K, z = eBack(k) * s;
  ctx.save(); ctx.translate(cx, cy); ctx.scale(z, z);
  ctx.beginPath(); ctx.moveTo(-7, 16); ctx.lineTo(-4, 32); ctx.lineTo(8, 17); ctx.closePath(); fs(ctx, bg, VC.K, 3);
  ctx.beginPath(); ctx.arc(0, 0, 22, 0, Math.PI * 2); fs(ctx, bg, VC.K, 3);
  ctx.beginPath(); ctx.moveTo(-6, 16); ctx.lineTo(-3, 28); ctx.lineTo(7, 17); ctx.closePath(); fs(ctx, bg);
  _ink(ctx, "700 28px Poppins, sans-serif", fg); ctx.fillText(ch, 0, 2);
  ctx.restore();
}

// document with a folded corner, coloured header (optional label) and grey text lines
function vPaper(ctx, x, y, w, h, o = {}) {
  const f = 12;
  ctx.save(); ctx.globalAlpha = o.alpha == null ? 1 : o.alpha; ctx.translate(x + w / 2, y + h / 2); ctx.rotate(o.rot || 0); ctx.translate(-w / 2, -h / 2);
  ctx.beginPath(); ctx.moveTo(5, 0); ctx.lineTo(w - f, 0); ctx.lineTo(w, f); ctx.lineTo(w, h - 5); ctx.quadraticCurveTo(w, h, w - 5, h);
  ctx.lineTo(5, h); ctx.quadraticCurveTo(0, h, 0, h - 5); ctx.lineTo(0, 5); ctx.quadraticCurveTo(0, 0, 5, 0); ctx.closePath(); fs(ctx, VC.W, VC.K, 3);
  ctx.beginPath(); ctx.moveTo(w - f, 0); ctx.lineTo(w - f, f); ctx.lineTo(w, f); ctx.closePath(); fs(ctx, VC.T, VC.K, 2.5);
  let ly = 12;
  if (o.head) { rr(ctx, 7, 8, w - f - 11, 13, 3); fs(ctx, o.head); if (o.label) { _ink(ctx, "700 9px Poppins, sans-serif", VC.W); ctx.fillText(o.label, 7 + (w - f - 11) / 2, 15); } ly = 28; }
  ctx.fillStyle = VC.G;
  for (let j = 0; ly + j * 9 < h - 8; j++) { rr(ctx, 7, ly + j * 9, (w - 14) * (j % 2 ? 0.6 : 0.85), 4, 2); ctx.fill(); }
  ctx.restore();
}

// keyboard seen from the side: slab with a row of key caps; one cap lights up per keystroke while typing
function vKeyboard(ctx, x, y, w, t, typing) {
  const n = Math.floor((w - 8) / 12), lit = typing ? Math.floor(t * 14) % n : -1;
  for (let j = 0; j < n; j++) { rr(ctx, x + 5 + j * 12, y - (j === lit ? 2 : 5), 9, 7, 2); fs(ctx, j === lit ? VC.A : VC.W, VC.K, 2); }
  rr(ctx, x, y, w, 12, 5); fs(ctx, VC.K);
}

// red flag on a pole that springs up (k 0..1) and waves
function vFlag(ctx, x, bottom, t, k) {
  if (k <= 0) return;
  const s = eBack(k);
  ctx.save(); ctx.translate(x, bottom); ctx.scale(1, s);
  ctx.strokeStyle = VC.K; ctx.lineWidth = 3.5; ctx.lineCap = "round"; ctx.beginPath(); ctx.moveTo(0, 0); ctx.lineTo(0, -48); ctx.stroke();
  ctx.beginPath(); ctx.moveTo(0, -48);
  for (let q = 0; q <= 8; q++) ctx.lineTo(q * 3.5, -48 + Math.sin(q * 0.8 - t * 9) * 2.5);
  for (let q = 8; q >= 0; q--) ctx.lineTo(q * 3.5, -30 + Math.sin(q * 0.8 - t * 9) * 2.5);
  ctx.closePath(); fs(ctx, VC.R, VC.K, 2.5);
  ctx.restore();
}

// vertical scan beam with a soft glow
function vBeam(ctx, x, y0, y1) {
  const g = ctx.createLinearGradient(x - 18, 0, x + 18, 0);
  g.addColorStop(0, "rgba(4,173,195,0)"); g.addColorStop(0.5, "rgba(4,173,195,.45)"); g.addColorStop(1, "rgba(4,173,195,0)");
  ctx.fillStyle = g; ctx.fillRect(x - 18, y0, 36, y1 - y0);
  rr(ctx, x - 1.5, y0, 3, y1 - y0, 1.5); fs(ctx, VC.A);
}

// shelf unit: light back panel, ink posts and boards
function vShelf(ctx, x0, x1, top, boards) {
  const bottom = boards[boards.length - 1];
  rr(ctx, x0, top, x1 - x0, bottom - top, 6); fs(ctx, "#E4F6F9");
  rr(ctx, x0, top - 4, x1 - x0, 8, 4); fs(ctx, VC.K);
  for (const b of boards) { rr(ctx, x0, b, x1 - x0, 8, 4); fs(ctx, VC.K); }
  rr(ctx, x0, top - 4, 8, bottom - top + 12, 4); fs(ctx, VC.K); rr(ctx, x1 - 8, top - 4, 8, bottom - top + 12, 4); fs(ctx, VC.K);
}

// carton box with tape stripe; scales from its bottom centre
function vBox(ctx, x, y, w, h, alpha = 1, scale = 1) {
  if (scale <= 0 || alpha <= 0) return;
  ctx.save(); ctx.globalAlpha = alpha; ctx.translate(x + w / 2, y + h); ctx.scale(scale, scale); ctx.translate(-w / 2, -h);
  rr(ctx, 0, 0, w, h, 5); fs(ctx, VC.A, VC.K, 2.5);
  rr(ctx, 1.5, 1.5, w - 3, 10, [4, 4, 0, 0]); fs(ctx, "#36C2D4");
  ctx.strokeStyle = VC.K; ctx.lineWidth = 2; ctx.beginPath(); ctx.moveTo(1.5, 12); ctx.lineTo(w - 1.5, 12); ctx.stroke();
  rr(ctx, w / 2 - 5, 1.5, 10, h - 3, 0); fs(ctx, VC.S);
  ctx.restore();
}

// puff of smoke (k 0..1)
function vPoof(ctx, cx, cy, k) {
  if (k <= 0 || k >= 1) return;
  ctx.save(); ctx.globalAlpha = (1 - k) * 0.9; ctx.fillStyle = VC.S;
  for (let j = 0; j < 6; j++) { const a = j / 6 * Math.PI * 2, d = 6 + k * 18; ctx.beginPath(); ctx.arc(cx + Math.cos(a) * d, cy + Math.sin(a) * d * 0.7, 8 + k * 5, 0, 7); ctx.fill(); }
  ctx.restore();
}

// slip of paper (reorder / purchase). big = yellow purchase slip
function vSlip(ctx, x, y, w, h, o = {}) {
  ctx.save(); ctx.globalAlpha = o.alpha == null ? 1 : o.alpha;
  rr(ctx, x, y, w, h, 5); fs(ctx, o.big ? VC.Y : VC.W, VC.K, 2.5);
  if (o.big) { _ink(ctx, "700 17px Poppins, sans-serif", VC.K); ctx.fillText("₹₹₹", x + w / 2, y + h / 2 + 1); }
  else { ctx.fillStyle = o.line || VC.A; for (let j = 0; j < 3 && 7 + j * 8 < h - 6; j++) { rr(ctx, x + 6, y + 7 + j * 8, (w - 12) * (j === 1 ? 0.6 : 1), 4, 2); ctx.fill(); } }
  ctx.restore();
}

// teal approval mark (ring + check) left by the stamp
function vStampMark(ctx, cx, cy, k) {
  if (k <= 0) return;
  ctx.save(); ctx.globalAlpha = clamp01(k * 3); ctx.strokeStyle = VC.GM; ctx.lineWidth = 3; ctx.beginPath(); ctx.arc(cx, cy, 13, 0, 7); ctx.stroke(); ctx.restore();
  tick(ctx, cx, cy, 15, VC.GM, 3.5, clamp01(k * 1.5));
}

// rubber stamp: knob, neck, aqua base; bottom edge at y
function vStamp(ctx, cx, y) {
  ctx.beginPath(); ctx.arc(cx, y - 40, 9, 0, 7); fs(ctx, VC.K);
  rr(ctx, cx - 5, y - 34, 10, 16, 3); fs(ctx, VC.K);
  rr(ctx, cx - 22, y - 20, 44, 12, 4); fs(ctx, VC.A, VC.K, 2.5);
  rr(ctx, cx - 18, y - 8, 36, 8, [0, 0, 3, 3]); fs(ctx, VC.D);
}

// magnifying glass held from (hx,hy)
function vLens(ctx, cx, cy, r, hx, hy) {
  ctx.save(); ctx.strokeStyle = VC.K; ctx.lineWidth = 7; ctx.lineCap = "round";
  const a = Math.atan2(hy - cy, hx - cx); ctx.beginPath(); ctx.moveTo(hx, hy); ctx.lineTo(cx + Math.cos(a) * r, cy + Math.sin(a) * r); ctx.stroke(); ctx.restore();
  ctx.beginPath(); ctx.arc(cx, cy, r, 0, 7); fs(ctx, "rgba(155,227,236,.38)", VC.K, 4);
  ctx.save(); ctx.strokeStyle = "rgba(255,255,255,.95)"; ctx.lineWidth = 3; ctx.lineCap = "round"; ctx.beginPath(); ctx.arc(cx, cy, r - 6, -2.6, -1.7); ctx.stroke(); ctx.restore();
}

// dotted curve p0 -> p2 drawn up to k (links, follow-up arrows); arrow head optional
function vCurve(ctx, p0, p1, p2, k, color, o = {}) {
  if (k <= 0) return;
  ctx.save(); ctx.strokeStyle = color; ctx.lineWidth = o.lw || 3.5; ctx.lineCap = "round"; ctx.setLineDash(o.dash || [2, 9]);
  ctx.beginPath(); ctx.moveTo(...p0); const kk = clamp01(k);
  for (let j = 1; j <= 30; j++) ctx.lineTo(...qb(p0, p1, p2, (kk * j) / 30));
  ctx.stroke(); ctx.setLineDash([]);
  if (o.arrow && kk > 0.95) { const [x, y] = p2, a = qbAng(p0, p1, p2, 1); ctx.translate(x, y); ctx.rotate(a);
    ctx.beginPath(); ctx.moveTo(-10, -7); ctx.lineTo(0, 0); ctx.lineTo(-10, 7); ctx.stroke(); }
  ctx.restore();
}

// chat bubble with a tail and three typing dots; (x,y) top-left, s = scale
function vBubble(ctx, x, y, s, color, t, seed = 0, alpha = 1) {
  ctx.save(); ctx.globalAlpha = alpha; ctx.translate(x, y); ctx.scale(s, s);
  ctx.beginPath(); ctx.moveTo(10, 30); ctx.lineTo(6, 44); ctx.lineTo(22, 32); ctx.closePath(); fs(ctx, color, VC.K, 2.5);
  rr(ctx, 0, 0, 64, 36, 14); fs(ctx, color, VC.K, 2.5);
  ctx.beginPath(); ctx.moveTo(11, 29); ctx.lineTo(8, 40); ctx.lineTo(21, 30); ctx.closePath(); fs(ctx, color);
  ctx.fillStyle = color === VC.Y ? VC.K : VC.W;
  for (let j = 0; j < 3; j++) { ctx.beginPath(); ctx.arc(19 + j * 13, 18 + Math.sin(t * 10 + j * 0.9 + seed) * 2.5, 4, 0, 7); ctx.fill(); }
  ctx.restore();
}

// inbox tray: back drawn first, then contents, then front lip
function vTrayBack(ctx, x, y, w, h) { rr(ctx, x + 6, y - 16, w - 12, h + 16, 6); fs(ctx, "#E4F6F9", VC.K, 2.5); }
function vTrayFront(ctx, x, y, w, h) {
  ctx.beginPath(); ctx.moveTo(x, y); ctx.lineTo(x + w, y); ctx.lineTo(x + w - 8, y + h); ctx.lineTo(x + 8, y + h); ctx.closePath(); fs(ctx, VC.W, VC.K, 3);
  rr(ctx, x + w / 2 - 14, y + 8, 28, 5, 2.5); fs(ctx, VC.A);
}

// conveyor belt: top rail with moving marks, body, rollers that turn
function vBelt(ctx, x0, x1, y, h, off) {
  rr(ctx, x0, y + 8, x1 - x0, h - 8, 0); fs(ctx, VC.T);
  ctx.save(); ctx.beginPath(); ctx.rect(x0, y, x1 - x0, 10); ctx.clip();
  rr(ctx, x0 - 10, y, x1 - x0 + 20, 10, 5); fs(ctx, VC.K);
  ctx.fillStyle = VC.D; for (let bx = x0 - 32 + (off % 32); bx < x1; bx += 32) { rr(ctx, bx, y + 3, 14, 4, 2); ctx.fill(); }
  ctx.restore();
  for (let rx = x0 + 24; rx < x1; rx += 64) {
    ctx.beginPath(); ctx.arc(rx, y + h / 2 + 5, 9, 0, 7); fs(ctx, VC.W, VC.K, 2.5);
    const a = off / 9; ctx.save(); ctx.strokeStyle = VC.K; ctx.lineWidth = 2; ctx.beginPath(); ctx.moveTo(rx, y + h / 2 + 5); ctx.lineTo(rx + Math.cos(a) * 7, y + h / 2 + 5 + Math.sin(a) * 7); ctx.stroke(); ctx.restore();
  }
}

// gate: two posts, top bar and a signal light (colour) with glow
function vGate(ctx, x, w, top, bottom, light) {
  rr(ctx, x, top, 8, bottom - top, 4); fs(ctx, VC.K); rr(ctx, x + w - 8, top, 8, bottom - top, 4); fs(ctx, VC.K);
  rr(ctx, x - 4, top - 4, w + 8, 10, 5); fs(ctx, VC.K);
  ctx.save(); if (light !== VC.G) { ctx.shadowColor = light; ctx.shadowBlur = 18; }
  ctx.beginPath(); ctx.arc(x + w / 2, top - 18, 12, 0, 7); fs(ctx, light, VC.K, 3); ctx.restore();
}

// bell shape (centred, ~24 wide); swings by ang around its top
function bellPath(ctx) {
  ctx.beginPath(); ctx.moveTo(-12, 8); ctx.quadraticCurveTo(-10, 4, -10, -2); ctx.bezierCurveTo(-10, -13, 10, -13, 10, -2); ctx.quadraticCurveTo(10, 4, 12, 8); ctx.closePath();
}
function vBell(ctx, cx, cy, ang, ringing, t, s = 1.4) {
  ctx.save(); ctx.translate(cx, cy - 14 * s); ctx.rotate(ang); ctx.translate(0, 14 * s); ctx.scale(s, s);
  ctx.beginPath(); ctx.arc(0, 12, 3.5, 0, 7); fs(ctx, VC.K);
  bellPath(ctx); fs(ctx, VC.Y, VC.K, 2.5 / s);
  ctx.beginPath(); ctx.arc(0, -13, 2.5, 0, 7); fs(ctx, VC.K);
  ctx.restore();
  if (ringing) { ctx.save(); ctx.strokeStyle = VC.K; ctx.lineWidth = 2.5; ctx.lineCap = "round"; ctx.globalAlpha = 0.5 + 0.5 * Math.sin(t * 20);
    for (const d of [-1, 1]) { ctx.beginPath(); ctx.arc(cx, cy, 26 * s / 1.4, d < 0 ? Math.PI - 0.5 : -0.5, d < 0 ? Math.PI + 0.5 : 0.5); ctx.stroke(); }
    ctx.restore(); }
}

// heart
function vHeart(ctx, cx, cy, s) {
  if (s <= 0) return;
  ctx.save(); ctx.translate(cx, cy); ctx.scale(s, s);
  ctx.beginPath(); ctx.moveTo(0, 14); ctx.bezierCurveTo(-26, -2, -14, -24, 0, -10); ctx.bezierCurveTo(14, -24, 26, -2, 0, 14); ctx.closePath(); fs(ctx, VC.R, VC.K, 3 / s);
  ctx.restore();
}
