// Rendert eine Szenenliste (JSON von build.py) mit anim.html zu MP4 + Posterbild.
const { chromium } = require('playwright'); const { spawn } = require('child_process'); const fs = require('fs'); const path = require('path');
(async () => {
  const [data, audio, out, poster, fpsS, posterT] = process.argv.slice(2); const fps = +fpsS;
  const d = JSON.parse(fs.readFileSync(data, 'utf8'));
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1280, height: 800 } });
  await p.goto('file://' + path.join(__dirname, 'anim.html')); await p.evaluate(x => window.LOAD(x), d); await p.evaluate(() => document.fonts.ready);
  await p.evaluate(t => window.DRAW(t), +posterT); await p.screenshot({ path: poster, type: 'jpeg', quality: 80 });
  const n = Math.round(d.total * fps);
  const ff = spawn('ffmpeg', ['-y', '-v', 'error', '-f', 'image2pipe', '-framerate', String(fps), '-i', '-', '-i', audio, '-c:v', 'libx264', '-crf', '27', '-preset', 'medium', '-pix_fmt', 'yuv420p', '-c:a', 'copy', '-shortest', '-movflags', '+faststart', out]);
  for (let i = 0; i < n; i++) { await p.evaluate(t => window.DRAW(t), i / fps); const buf = await p.screenshot({ type: 'jpeg', quality: 88 }); if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r)); }
  ff.stdin.end(); await new Promise(r => ff.on('close', r)); await b.close();
})();
