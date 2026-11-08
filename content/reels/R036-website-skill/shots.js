// Echte Aufnahmen: Demo-Seiten (Handy, ganze Seite) + Workshop-Karte im Flow-DNA-Store
const { chromium } = require('playwright');
(async()=>{const R='/home/user/flow-media-ai/flow-dna/';const b=await chromium.launch();
const ctx=await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2,isMobile:true,hasTouch:true});
for(const k of ['baeckerei','physio','friseur']){const p=await ctx.newPage();await p.goto('file://'+R+'demos/'+k+'/index.html');
 await p.evaluate(()=>{document.querySelectorAll('.reveal').forEach(e=>e.classList.add('in'));document.querySelector('.ask').style.display='none';document.querySelector('.mcta').style.display='none';document.getElementById('hd').style.position='absolute'});
 await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(1500);
 await p.screenshot({path:`img/${k}.jpg`,type:'jpeg',quality:86,fullPage:true,clip:{x:0,y:0,width:390,height:4200}});await p.close();}
const p=await ctx.newPage();await p.goto('file://'+R+'index.html?workshop=website');await p.waitForTimeout(1500);
await p.evaluate(()=>{const i=document.querySelector('.inst');i&&i.remove();});await p.waitForTimeout(300);
await p.screenshot({path:'img/store_ws.jpg',type:'jpeg',quality:88,fullPage:true,clip:{x:0,y:0,width:390,height:2600}});
await b.close();})();
