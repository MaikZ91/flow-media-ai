// Rendert den Einzelpost als PNG (1080×1350).
const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1080, height: 1350 } });
  await p.goto('file://' + __dirname + '/single.html');
  await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(1200);
  await (await p.$('section')).screenshot({ path: __dirname + '/flow_single.png' });
  await b.close();
})();
