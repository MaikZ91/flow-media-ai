// Phone screens of the Flow Board with demo data only (local build, sample cards; no real board data).
const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  const ctx = await b.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 3, isMobile: false, hasTouch: true });
  const p = await ctx.newPage();
  await p.goto('file:///home/user/flow-media-ai/tools/flow-board/index.html');
  await p.evaluate(() => {
    applyTheme('dark'); seedDemo(); fin = []; meta.name = "Beispiel-Board";
    const wk = mondayOf(new Date()), d = n => { const x = new Date(wk); x.setDate(x.getDate() + n); return ymd(x) };
    const T = (title, day, time, endTime, status = "todo") => ({ id: "r" + Math.random().toString(36).slice(2), title, status, due: d(day), time, endTime, order: 0, createdAt: Date.now(), updatedAt: Date.now() });
    tasks.push(T("Reel drehen", 1, "09:00", "10:30"), T("Workshop vorbereiten", 1, "14:00", "16:00"), T("Gym", 1, "18:00", "19:30"), T("Netzwerk-Abend", 2, "19:00", "21:00"));
    const y = new Date().getFullYear(), mk = (m, day) => `${y}-${String(m).padStart(2, "0")}-${String(day).padStart(2, "0")}`;
    const tx = o => ({ id: "f" + Math.random().toString(36).slice(2), type: "tx", vat: 0, category: "Kundenprojekt", status: "paid", receipt: true, createdAt: Date.now(), ...o });
    fin.push(tx({ kind: "in", date: mk(9, 5), amount: 600, title: "Workshop (Beispiel)", party: "Beispiel Studio", category: "Workshop" }),
      tx({ kind: "out", date: mk(9, 18), amount: 49, title: "Domain & Hosting", party: "Beispiel-Hoster", category: "Tools & Software" }),
      tx({ kind: "in", date: mk(10, 14), amount: 900, title: "Landingpage (Beispiel)", party: "Beispiel GmbH" }));
    view = "board"; render();
  });
  const shot = async n => { await p.mouse.move(2, 2); await p.waitForTimeout(400); await p.screenshot({ path: `img/${n}.png` }); console.log(n) };
  await shot('board');
  await p.evaluate(() => { view = "cal"; calMode = "list"; render() }); await shot('cal');
  await p.evaluate(() => { view = "fin"; finUi.tab = "business"; render() }); await shot('fin');
  await b.close();
})();
