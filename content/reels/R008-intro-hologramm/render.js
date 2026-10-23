const { chromium } = require('playwright'); const { spawn } = require('child_process');
(async()=>{const fps=30;const b=await chromium.launch({args:['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader']});
const p=await b.newPage({viewport:{width:1080,height:1920}});
await p.goto('http://localhost:8766/intro.html');await p.waitForFunction(()=>window.READY,null,{timeout:60000});await p.evaluate(()=>document.fonts.ready);
const total=await p.evaluate(()=>window.TOTAL),n=Math.round(total*fps);
const ff=spawn('ffmpeg',['-y','-v','error','-f','image2pipe','-framerate',String(fps),'-i','-','-c:v','libx264','-crf','20','-preset','medium','-pix_fmt','yuv420p',__dirname+'/video_only.mp4']);
for(let i=0;i<n;i++){await p.evaluate(t=>window.DRAW(t),i/fps);const buf=await p.screenshot({type:'jpeg',quality:92});if(!ff.stdin.write(buf))await new Promise(r=>ff.stdin.once('drain',r))}
ff.stdin.end();await new Promise(r=>ff.on('close',r));await b.close();console.log('frames',n)})();
