const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1080, height: 1350 } });
  await p.goto('file://' + process.argv[2] + '/karussell.html'); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(400);
  for (let i = 1; i <= 6; i++) await (await p.$('#s' + i)).screenshot({ path: `${process.argv[2]}/P013-${i}.png` });
  await b.close();
})();
