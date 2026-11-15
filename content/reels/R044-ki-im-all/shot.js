// Standbilder zur Kontrolle: node shot.js 0.5 3.5 ...  -> test/t_<zeit>.jpg (halbe Größe)
const { chromium } = require('playwright');
(async()=>{ const b=await chromium.launch({args:['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader']});
 const p=await b.newPage({viewport:{width:1080,height:1920}}); const errs=[]; p.on('pageerror',e=>errs.push(e.message)); p.on('console',m=>{if(m.type()==='error')errs.push(m.text())});
 await p.goto('http://localhost:8774/space.html'+(process.env.NOTEXT?'?notext':'')); try{await p.waitForFunction(()=>window.READY,null,{timeout:120000})}catch(e){console.log('NOT READY',errs.slice(0,6));await b.close();return}
 require('fs').mkdirSync(__dirname+'/test',{recursive:true});
 for(const a of process.argv.slice(2)){ const t=parseFloat(a); const t0=Date.now(); await p.evaluate(t=>window.DRAW(t),t); await p.screenshot({path:__dirname+`/test/t_${a}.jpg`,type:'jpeg',quality:88}); console.log(a,Date.now()-t0,'ms'); }
 console.log('T',await p.evaluate(()=>window.T.map(x=>+x.toFixed(2)).join(' ')), errs.slice(0,6)); await b.close();})();
