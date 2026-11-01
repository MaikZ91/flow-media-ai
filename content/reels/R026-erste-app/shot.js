const { chromium } = require('playwright');
(async()=>{ const b=await chromium.launch(); const p=await b.newPage({viewport:{width:1080,height:1920}});
 await p.goto('file://'+process.cwd()+'/reel.html'); await p.evaluate(()=>document.fonts.ready);
 const ts=process.argv.slice(2).map(Number);
 for(const t of ts){ await p.evaluate(t=>window.DRAW(t),t); await p.screenshot({path:`/tmp/claude-0/-home-user/a01ee5cb-df27-59af-9971-bacc4c22168f/scratchpad/r26_${t}.jpg`,type:'jpeg',quality:70}); }
 await b.close(); })();
