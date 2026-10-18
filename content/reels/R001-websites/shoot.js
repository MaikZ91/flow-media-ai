const { chromium } = require('playwright');
const [out, ...pages] = process.argv.slice(2);
(async () => {
  const b = await chromium.launch();
  const ctx = await b.newContext({ viewport: { width: 390, height: 693 }, deviceScaleFactor: 2.77, isMobile: true, hasTouch: true });
  for (const p of pages) {
    const pg = await ctx.newPage();
    const name = p.replace(/\/index\.html$/, '').replace(/\.html$/, '').replace(/\//g, '_');
    try { await pg.goto('http://localhost:8765/' + p, { waitUntil: 'networkidle', timeout: 25000 }); } catch (e) { console.log('slow', p); }
    await pg.waitForTimeout(2000);
    const h = await pg.evaluate(() => document.documentElement.scrollHeight);
    for (let y = 0; y < Math.min(h, 4000); y += 400) { await pg.evaluate(y => window.scrollTo(0, y), y); await pg.waitForTimeout(120); }
    await pg.evaluate(() => window.scrollTo(0, 0)); await pg.waitForTimeout(600);
    await pg.screenshot({ path: `${out}/${name}.png`, fullPage: true }).catch(e => console.log('fail', p, e.message));
    console.log(name, h); await pg.close();
  }
  await b.close();
})();
