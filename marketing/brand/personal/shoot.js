const { chromium } = require('playwright');
(async()=>{const b=await chromium.launch();
for(const [h,out] of [['holo','maik_hololens_ar_2017_branded.jpg'],['robo','maik_roboter_teststand_branded.jpg'],['hki','maik_hololens_ki_branded.jpg'],['rki','maik_roboter_ki_branded.jpg']]){
const p=await b.newPage({viewport:{width:1080,height:1350}});await p.goto('file://'+__dirname+'/branded.html#'+h);await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(500);
await p.screenshot({path:__dirname+'/'+out,type:'jpeg',quality:92});await p.close();}
await b.close();})();
