// ART pixel robot, canvas engine (frame-by-frame poses). Aiotrix kit only.
// Grid 24x24 art pixels. drawBot(ctx, x, y, u, pose): (x,y) = top-left of grid, u = px per art pixel.
// Poses step at 8/s (S = floor(t*8)); travel snaps to 4px. Deterministic: no random, no clocks.
const C8 = { A: "#04ADC3", W: "#FFFFFF", K: "#1A1A1A", S: "#9BE3EC", R: "#F27A7A", Y: "#FFD166", G: "#D9D9D9", D: "#5A5A5A" };
const snap = v => Math.round(v / 4) * 4;

function _pts(list, color) { return list.map(([x, y, w = 1, h = 1]) => [x, y, w, h, color]); }

function botParts(p) {
  const L = p.dark ? C8.W : C8.K;
  const out = [];
  const add = (list, c) => out.push(..._pts(list, c));
  // antenna
  add([[11, 2, 1, 2]], L);
  if (!p.bulbOff) add([[10, 0, 3, 2]], p.bulb === "red" ? C8.R : p.bulb === "yellow" ? C8.Y : C8.A);
  // head
  add([[5, 4, 13, 1], [4, 5, 15, 1], [4, 6, 2, 6], [17, 6, 2, 6], [4, 12, 15, 1], [5, 13, 13, 1]], C8.A);
  add([[3, 7, 1, 4], [19, 7, 1, 4]], C8.A); // ears
  add([[6, 6, 11, 6]], C8.W);                 // face screen
  // body
  add([[6, 14, 11, 6]], C8.A);
  add([[9, 16, 5, 3]], C8.W);
  add([[10, 17]], p.light2 ? C8.Y : C8.A); add([[12, 17]], C8.S);
  // legs
  const legs = {
    stand: [[8, 20, 2, 2], [13, 20, 2, 2], [7, 22, 3, 1], [13, 22, 3, 1]],
    stepL: [[8, 20, 2, 1], [7, 21, 3, 1], [13, 20, 2, 2], [13, 22, 3, 1]],
    stepR: [[8, 20, 2, 2], [7, 22, 3, 1], [13, 20, 2, 1], [13, 21, 3, 1]],
    tuck:  [[8, 20, 2, 1], [13, 20, 2, 1], [7, 21, 3, 1], [13, 21, 3, 1]],
  }[p.legs || "stand"];
  add(legs, L);
  // arms (A)
  const AL = {
    down: [[5, 15], [5, 16], [4, 17], [4, 18]],
    up:   [[5, 15], [4, 15], [4, 14], [3, 13], [3, 12], [3, 11]],
    flex: [[5, 15], [4, 15], [3, 14], [3, 13], [4, 12], [5, 12]],
    out:  [[5, 15], [4, 15], [3, 15], [2, 15]],
  }[p.armL || "down"];
  const AR = {
    down:  [[17, 15], [17, 16], [18, 17], [18, 18]],
    up:    [[17, 15], [18, 15], [18, 14], [19, 13], [19, 12], [19, 11]],
    wave1: [[17, 15], [18, 15], [19, 14], [20, 13], [21, 12]],
    wave2: [[17, 15], [18, 15], [18, 14], [18, 13], [18, 12]],
    flex:  [[17, 15], [18, 15], [19, 14], [19, 13], [18, 12], [17, 12]],
    reach: [[17, 15], [18, 15], [19, 15], [20, 15], [21, 15]],
    hold:  [[17, 15], [17, 16], [18, 16]],
    tap:   [[17, 15], [18, 16], [19, 17], [20, 18]],
  }[p.armR || "down"];
  add(AL, C8.A); add(AR, C8.A);
  // eyes
  const EY = {
    open:  [[[8, 7, 2, 2], [13, 7, 2, 2]], C8.K, [[8, 7], [13, 7]]],
    lookL: [[[7, 7, 2, 2], [12, 7, 2, 2]], C8.K, [[7, 7], [12, 7]]],
    lookR: [[[9, 7, 2, 2], [14, 7, 2, 2]], C8.K, [[9, 7], [14, 7]]],
    blink: [[[8, 8, 2, 1], [13, 8, 2, 1]], C8.K, []],
    happy: [[[7, 8], [8, 7, 2, 1], [10, 8], [12, 8], [13, 7, 2, 1], [15, 8]], C8.K, []],
    wide:  [[[8, 6, 2, 3], [13, 6, 2, 3]], C8.K, [[8, 6], [13, 6]]],
    squint:[[[7, 8, 4, 1], [13, 7, 2, 2]], C8.K, []],
    focus: [[[7, 8, 3, 1], [13, 8, 3, 1]], C8.K, []],
  }[p.eyes || "open"];
  add(EY[0], EY[1]); add(EY[2], C8.W);
  const MO = {
    smile: [[9, 10], [10, 11, 3, 1], [13, 10]],
    grin:  [[9, 10, 5, 1], [10, 11, 3, 1]],
    wobble:[[8, 11], [9, 10, 2, 1], [11, 11, 2, 1], [13, 10, 2, 1]],
    o:     [[10, 10, 3, 2]],
    flat:  [[9, 10, 5, 1]],
    open:  [[10, 10, 3, 2]],
  }[p.mouth || "smile"];
  add(MO, C8.K);
  return out;
}

function drawBot(ctx, x, y, u, p = {}) {
  x = snap(x); y = snap(y);
  const parts = botParts(p);
  const flip = !!p.flip;
  const put = (gx, gy, w, h, c, dx = 0, dy = 0) => {
    const X = flip ? (24 - gx - w) : gx;
    ctx.fillStyle = c; ctx.fillRect(x + X * u + dx, y + gy * u + dy, w * u, h * u);
  };
  if (p.halo) {                                   // cream/white halo on dark scenes
    const h = 4;
    for (const [dx, dy] of [[-h, 0], [h, 0], [0, -h], [0, h], [-h, -h], [h, h], [-h, h], [h, -h]])
      for (const [gx, gy, w, hh] of parts) put(gx, gy, w, hh, p.haloColor || "#FFFFFF", dx, dy);
  }
  for (const [gx, gy, w, h, c] of parts) put(gx, gy, w, h, c);
}

// soft flat shadow under feet
function botShadow(ctx, cx, feetY, w, dark) {
  ctx.fillStyle = dark ? "rgba(0,0,0,.35)" : "rgba(26,26,26,.12)";
  ctx.fillRect(snap(cx - w / 2), snap(feetY), snap(w), 8);
}

// ---- generic pixel helpers for props (u = art pixel size) ----
function pxr(ctx, x, y, w, h, c) { ctx.fillStyle = c; ctx.fillRect(snap(x), snap(y), w, h); }
function blitRows(ctx, rows, x, y, u, pal) {
  rows.forEach((r, j) => [...r].forEach((ch, i) => { if (ch !== ".") { ctx.fillStyle = pal[ch] || ch; ctx.fillRect(snap(x) + i * u, snap(y) + j * u, u, u); } }));
}
const SPR = {
  q:    [".KKK.", "K...K", "....K", "...K.", "..K..", ".....", "..K.."],
  bang: ["R", "R", "R", ".", "R"],
  check:["....A", "...A.", "A.A..", ".A..."],
  phone:["KKKKK", "KAAAK", "KAAAK", "KAAAK", "KAAAK", "KKWKK"],
  ringL:["K.", ".K", "K."],
  paper:["KKKKKK", "KWWWWK", "KWGGWK", "KWWWWK", "KWGGWK", "KWWWWK", "KKKKKK"],
  bubble:["AAAAAAA", "AWWWWWA", "AAAAAAA", ".AA...."],
  mug:  ["KKKK.", "KKKKK", "KKKK.", "KKKK."],
  steam:[".S", "S.", ".S"],
  lens: [".KKK.", "KSSSK", "KSSSK", "KSSSK", ".KKK.", "....K", ".....K"],
  box:  ["AAAAA", "ASSSA", "AAAAA", "ASSSA", "AAAAA"],
  plane:["A....", "AAA..", "AAAAA", "AAA..", "A...."],
  shop: ["AWAWAWAWA", "AWAWAWAWA", ".KKKKKKK.", ".KWWKWWK.", ".KWWKWWK.", ".KKKKAAK.", ".KWWKAAK.", ".KKKKKKK."],
  kbd:  ["KKKKKKKKK", "KWKWKWKWK", "KKKKKKKKK"],
  flag: ["RRR.", "RRRR", "RRR.", "K...", "K...", "K..."],
  slip: ["KKKKK", "KWWWK", "KWAWK", "KWWWK", "KWAWK", "KKKKK"],
  stamp:["..AAA..", ".AAAAA.", "AAAAAWA", "AAAAWAA", "AWAWAAA", ".AAWAA.", "..AAA.."],
  bell: ["..K..", ".YYY.", ".YYY.", "YYYYY", "..K.."],
  arrow:["..AAA", "...AA", "..A.A", ".A...", "A...."],
  tray: ["K.........K", "K.........K", "KKKKKKKKKKK"],
  big:  ["YYYYYY", "YWWWWY", "YWKKWY", "YWWWWY", "YWKKWY", "YWWWWY", "YWKKWY", "YYYYYY"],
  small:["KKKK", "KWWK", "KWAK", "KKKK"],
  heart:[".R.R.", "RRRRR", "RRRRR", ".RRR.", "..R.."],
  poof: ["S.S", ".S.", "S.S"],
  gear: ["..A.A..", ".AAAAA.", "AAA.AAA", ".A...A.", "AAA.AAA", ".AAAAA.", "..A.A.."],
};
const PAL = { K: C8.K, A: C8.A, W: C8.W, S: C8.S, R: C8.R, G: C8.G, Y: C8.Y };
