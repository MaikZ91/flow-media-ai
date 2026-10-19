// Screens for R002 from the current board build with the demo sample cards (sample data only, kept in this browser) plus the landing page and the analytics view.
// usage: node shoot.js <out-dir> [board-key-file]
const { chromium } = require('playwright');
const fs = require('fs');
const [out, keyFile] = process.argv.slice(2);
const FB = 'file:///home/user/flow-media-ai/tools/flow-board/';
(async () => {
  const b = await chromium.launch();
  const ctx = await b.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2 });
  const p = await ctx.newPage();
  await p.goto(FB + 'index.html');
  await p.evaluate(() => {
    applyTheme('light'); seedDemo(); fin = []; meta.name = "Beispiel-Board";
    meta.mottos = { 0: "Ordnung & Klarheit", 1: "Health", 2: "Social" };
    const wk = mondayOf(new Date()), d = n => { const x = new Date(wk); x.setDate(x.getDate() + n); return ymd(x) };
    const T = (title, day, time, endTime, status = "todo") => ({ id: "r" + Math.random().toString(36).slice(2), title, status, due: d(day), time, endTime, order: 0, createdAt: Date.now(), updatedAt: Date.now() });
    tasks.push(T("Kundencall (Beispiel)", 0, "10:00", "11:00"), T("Reel drehen", 1, "09:00", "10:30"), T("Workshop vorbereiten", 2, "14:00", "16:00"),
      T("Deep Work: Board", 3, "08:00", "11:00", "doing"), T("Gym", 1, "18:00", "19:30"), T("Netzwerk-Abend", 2, "19:00", "21:00"));
    const y = new Date().getFullYear(), mk = (m, day) => `${y}-${String(m).padStart(2, "0")}-${String(day).padStart(2, "0")}`;
    const tx = (o) => ({ id: "f" + Math.random().toString(36).slice(2), type: "tx", vat: 0, category: "Kundenprojekt", status: "paid", receipt: true, createdAt: Date.now(), ...o });
    fin.push(tx({ kind: "in", date: mk(8, 12), amount: 900, title: "Landingpage (Beispiel)", party: "Beispiel GmbH" }),
      tx({ kind: "out", date: mk(8, 20), amount: 23.8, vat: 19, title: "KI-Abo", party: "Beispiel-Anbieter", category: "Tools & Software" }),
      tx({ kind: "in", date: mk(9, 5), amount: 600, title: "KI-Workshop (Beispiel)", party: "Beispiel Studio", category: "Workshop" }),
      tx({ kind: "out", date: mk(9, 18), amount: 49, title: "Domain & Hosting", party: "Beispiel-Hoster", category: "Tools & Software", receipt: false }),
      tx({ kind: "in", date: mk(10, 14), amount: 1450, title: "Rechnung 2026-001", party: "Beispiel GmbH", status: "open",
        inv: { no: "2026-001", customerNo: "K-01", date: mk(10, 14), service: "Oktober " + y, vat: 0, terms: 14, intro: "Vielen Dank für dein Vertrauen. Hiermit stelle ich folgende Positionen in Rechnung:",
          customer: { name: "Beispiel GmbH", street: "Musterweg 1", city: "12345 Musterstadt", country: "Deutschland" },
          items: [{ desc: "Landingpage inkl. Texte", qty: 1, price: 1200 }, { desc: "Tracking & Dashboard einrichten", qty: 1, price: 250 }] } }),
      tx({ kind: "out", date: mk(10, 16), amount: 120, title: "Kamera-Zubehör", party: "Beispiel-Shop", category: "Hardware" }));
    meta.invoice = { company: "Flow Media AI", name: "Maik", street: "Beispielstraße 1", city: "12345 Beispielstadt", iban: "DE00 0000 0000 0000 0000 00", taxId: "Steuernummer 000/000/00000", email: "hallo@beispiel.de", small: true };
    view = "board"; render();
  });
  await p.waitForTimeout(800);
  const shot = async n => { await p.waitForTimeout(250); await p.screenshot({ path: `${out}/${n}.png` }); console.log(n) };
  await shot('board');
  await p.evaluate(() => { view = "matrix"; render() }); await shot('matrix');
  await p.evaluate(() => { meta.mottos = { 0: "Ordnung & Klarheit", 1: "Health", 2: "Social" }; view = "cal"; calMode = "week"; weekStart = mondayOf(new Date()); render() }); await shot('cal');
  // drag "Reel drehen" one day right and later, frame by frame
  const ev = p.locator('.wev', { hasText: 'Reel drehen' }); const bb = await ev.boundingBox(); const col = await p.locator('.wcol').first().boundingBox();
  const hour = col.height / 15, x0 = bb.x + 30, y0 = bb.y + 10, dx = col.width * 2, dy = hour * 2;
  await p.mouse.move(x0, y0); await p.mouse.down(); await p.mouse.move(x0 + 6, y0 + 6, { steps: 2 });
  for (let i = 1; i <= 14; i++) { const t = i / 14, e = t * t * (3 - 2 * t); await p.mouse.move(x0 + dx * e, y0 + dy * e); await p.waitForTimeout(40); await p.screenshot({ path: `${out}/drag_${String(i).padStart(2, '0')}.png` }) }
  await p.mouse.up(); await shot('cal_after');
  await p.mouse.move(5, 5); await p.evaluate(() => { view = "fin"; finUi.tab = "business"; render() }); await shot('fin');
  await p.evaluate(() => { finUi.tab = "invoices"; render(); showInvoice(fin.find(x => x.inv)) }); await p.waitForTimeout(600); await shot('invoice');
  await p.evaluate(() => { closeModal(); finUi.tab = "private"; render() });
  // dark-mode screens for the cinematic B-roll (tilted board on a dark stage)
  await p.mouse.move(5, 5);
  await p.evaluate(() => { applyTheme('dark'); view = "board"; render() }); await shot('board_dark');
  await p.evaluate(() => { view = "cal"; render() }); await shot('cal_dark');
  await p.evaluate(() => { view = "fin"; finUi.tab = "business"; render() }); await shot('fin_dark');
  await p.evaluate(() => { applyTheme('light'); view = "board"; render() });
  // landing page, phone format
  const m = await b.newContext({ viewport: { width: 390, height: 693 }, deviceScaleFactor: 2.77, isMobile: true, hasTouch: true });
  const lp = await m.newPage(); await lp.goto('file:///home/user/flow-media-ai/marketing/landing-page/index.html'); await lp.waitForTimeout(1500);
  await lp.screenshot({ path: `${out}/landing.png`, fullPage: true }); console.log('landing');
  // analytics: the real web board, only the Auswertung view is captured (no finance data)
  if (keyFile && fs.existsSync(keyFile)) {
    const key = fs.readFileSync(keyFile, 'utf8').trim();
    const w = await ctx.newPage(); await w.goto(FB + 'web/index.html#b=maik&k=' + encodeURIComponent(key));
    await w.waitForTimeout(3500); await w.evaluate(() => { try { localStorage.removeItem("flow-board-creds") } catch {} });
    await w.click('[data-view="stats"]');
    await w.waitForFunction(() => stats.data || stats.error, null, { timeout: 30000 }).catch(() => console.log('stats timeout'));
    await w.mouse.move(5, 5); await w.waitForTimeout(800);
    await w.screenshot({ path: `${out}/stats.png` }); console.log('stats');
  }
  await b.close();
})();
