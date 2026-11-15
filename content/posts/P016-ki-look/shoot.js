// Rendert die 5 Karussell-Folien als PNG (1080×1350).
const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1080, height: 1350 } });
  await p.goto('file://' + __dirname + '/post.html');
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(1200);
  const ss = await p.$$('section');
  for (let i = 0; i < ss.length; i++) {
    await ss[i].screenshot({ path: __dirname + `/ki_s${i + 1}.png` });
  }
  await b.close();
})();
