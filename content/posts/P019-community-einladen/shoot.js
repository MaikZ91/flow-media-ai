const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1080, height: 1350 } });
  await p.goto('file://' + __dirname + '/bild.html'); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(1500);
  await p.screenshot({ path: __dirname + '/community-einladen.png' }); await b.close();
})();
