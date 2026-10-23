const { chromium } = require('playwright');
(async()=>{const b=await chromium.launch();
for(const [h,H,name] of [['',1350,'flyer_feed.png'],['#story',1920,'flyer_story.png']]){
 const p=await b.newPage({viewport:{width:1080,height:H}});
 await p.goto('file://'+__dirname+'/flyer.html'+h);await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(400);
 await p.screenshot({path:__dirname+'/'+name});await p.close()}
await b.close()})();
