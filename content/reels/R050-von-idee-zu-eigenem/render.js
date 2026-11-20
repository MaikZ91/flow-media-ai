// Renders reel.html frame by frame (30 fps) into frames/, then ffmpeg builds the video.
const { chromium } = require('playwright'); const fs = require('fs');
(async () => {
  const D = +process.argv[2] || 13, FPS = 30, only = process.argv[3];
  fs.mkdirSync(__dirname + '/frames', { recursive: true });
  const b = await chromium.launch({ args: ['--allow-file-access-from-files'] }); const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  await p.goto('file://' + __dirname + '/reel.html'); await p.evaluate(d => window.LOAD(d), JSON.parse(fs.readFileSync(__dirname + '/netz.json')));
  const list = only ? only.split(',').map(Number) : [...Array(D * FPS).keys()].map(i => i / FPS);
  for (const [n, t] of list.entries()) { await p.evaluate(t => window.DRAW(t), t);
    await p.screenshot({ path: __dirname + (only ? `/check_${t}.jpg` : `/frames/${String(n).padStart(4, '0')}.jpg`), type: 'jpeg', quality: 92 }); }
  await b.close();
})();
