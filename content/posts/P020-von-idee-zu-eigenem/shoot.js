const { chromium } = require('playwright');
(async () => { const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1080, height: 1350 } });
  await p.goto('file://' + __dirname + '/post.html'); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(1200);
  await p.screenshot({ path: __dirname + '/P020.png' }); await b.close(); })();
