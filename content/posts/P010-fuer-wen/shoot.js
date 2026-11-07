const { chromium } = require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1350}});
await p.goto('file://'+__dirname+'/post.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(400);
await p.screenshot({path:__dirname+'/fuer_wen.png'});await b.close();})();
