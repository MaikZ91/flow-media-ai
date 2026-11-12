const { chromium } = require('playwright');
(async () => { const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1080, height: 3400 } });
  await p.goto('file://' + process.argv[2] + '/post.html'); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(400);
  await (await p.$('#post')).screenshot({ path: process.argv[2] + '/P015-post.png' });
  await (await p.$('#story')).screenshot({ path: process.argv[2] + '/P015-story.png' }); await b.close(); })();
