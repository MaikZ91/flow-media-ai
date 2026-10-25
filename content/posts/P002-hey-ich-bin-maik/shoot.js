const { chromium } = require('playwright');
(async()=>{ const b=await chromium.launch();
 for(const [m,w,h] of [['feed',1080,1350],['story',1080,1920]]){
  const p=await b.newPage({viewport:{width:w,height:h}}); await p.goto('file://'+__dirname+'/post.html#'+m);
  await p.evaluate(()=>document.fonts.ready); await p.waitForTimeout(400);
  await p.screenshot({path:__dirname+`/hey_maik_${m}.png`}); await p.close(); }
 await b.close();})();
