// echte Store-Aufnahmen für das Reel (Handy 390 breit, 3x)
const { chromium } = require('playwright');
(async()=>{const b=await chromium.launch();const U='file://'+require('path').resolve(__dirname,'../../../flow-dna/index.html');const O=__dirname+'/img/';
const pg=async(h)=>{const p=await b.newPage({viewport:{width:390,height:h},deviceScaleFactor:3});await p.goto(U);await p.evaluate(()=>document.fonts.ready);await p.addStyleTag({content:'.r .pr,.dna-preis,.dna-opts,.dna-opts+*{visibility:hidden}'});await p.waitForTimeout(600);return p};
let p=await pg(2600);await p.screenshot({path:O+'store_list.png'});await p.close();
p=await pg(1500);await p.locator('#seg button[data-st="basis"]').click();await p.waitForTimeout(300);await p.screenshot({path:O+'store_free.png'});await p.close();
p=await pg(844);await p.locator('[data-skill="creative-director"]').click();await p.waitForTimeout(500);await p.screenshot({path:O+'store_cd.png'});
await p.close();
p=await pg(844);await p.locator('nav [data-tab="more"]').click();await p.waitForTimeout(300);await p.evaluate(()=>{const h=[...document.querySelectorAll('.dna-x-h')].find(x=>/Creator/.test(x.textContent));document.getElementById('view').scrollTop=h.offsetTop-20});await p.waitForTimeout(200);await p.screenshot({path:O+'store_creator.png'});await p.close();
await b.close();})();
