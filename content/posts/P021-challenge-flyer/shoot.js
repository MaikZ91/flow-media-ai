const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  for (const [q, h, out] of [['', 1350, 'challenge-flyer.jpg'], ['?f=story', 1920, 'challenge-flyer-story.jpg']]) {
    const p = await b.newPage({ viewport: { width: 1080, height: h } });
    await p.goto('file://' + __dirname + '/flyer.html' + q); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(1500);
    await p.screenshot({ path: __dirname + '/' + out, type: 'jpeg', quality: 92 }); await p.close();
  }
  await b.close();
})();
