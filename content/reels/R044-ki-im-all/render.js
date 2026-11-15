// Rendert space.html Bild für Bild (WebGL über SwiftShader) nach frames/f_00000.jpg.
// Vorher diesen Ordner ausliefern:  python3 -m http.server 8774
// Aufruf: node render.js [von] [bis]   (Bildnummern, 30 fps) · danach: bash build.sh
const { chromium } = require('playwright'); const fs = require('fs');
(async()=>{ const fps=30; const b=await chromium.launch({args:['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader']});
 const p=await b.newPage({viewport:{width:1080,height:1920}});
 await p.goto('http://localhost:8774/space.html'); await p.waitForFunction(()=>window.READY,null,{timeout:180000});
 const total=await p.evaluate(()=>window.TOTAL), n=Math.round(total*fps);
 const from=parseInt(process.argv[2]||'0'), to=Math.min(n,parseInt(process.argv[3]||String(n)));
 fs.mkdirSync(__dirname+'/frames',{recursive:true});
 for(let i=from;i<to;i++){ await p.evaluate(t=>window.DRAW(t),i/fps); await p.screenshot({path:`${__dirname}/frames/f_${String(i).padStart(5,'0')}.jpg`,type:'jpeg',quality:94}); if(i%50===0) console.log(i,'/',to); }
 await b.close(); console.log('fertig',from,to,'von',n);})();
