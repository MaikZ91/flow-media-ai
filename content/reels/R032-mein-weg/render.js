// render the transparent overlay to overlay.mov (PNG codec with alpha)
const { chromium } = require('playwright'); const { spawn } = require('child_process');
(async()=>{const fps=30,b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
await p.goto('file://'+process.cwd()+'/overlay.html');await p.evaluate(()=>document.fonts.ready);
const n=Math.round(await p.evaluate(()=>window.TOTAL)*fps);
const ff=spawn('ffmpeg',['-y','-v','error','-f','image2pipe','-framerate',String(fps),'-i','-','-c:v','qtrle','overlay.mov']);
for(let i=0;i<n;i++){await p.evaluate(t=>window.DRAW(t),i/fps);const buf=await p.screenshot({type:'png',omitBackground:true});if(!ff.stdin.write(buf))await new Promise(r=>ff.stdin.once('drain',r));}
ff.stdin.end();await new Promise(r=>ff.on('close',r));await b.close();console.log('frames',n);})();
