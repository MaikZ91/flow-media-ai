const { chromium } = require('playwright');
(async()=>{ const b=await chromium.launch();
 for(const s of ['s1','s2','s3','s4']){
  const p=await b.newPage({viewport:{width:1080,height:1350}}); await p.goto('file://'+__dirname+'/post.html#'+s);
  await p.evaluate(()=>document.fonts.ready); await p.waitForTimeout(400);
  await p.screenshot({path:__dirname+`/workshop_${s}.png`}); await p.close(); }
 await b.close();})();
