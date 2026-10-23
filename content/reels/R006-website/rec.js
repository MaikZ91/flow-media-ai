// Records the live website frame by frame (JS time via Playwright clock, CSS animations slowed to match)
const { chromium } = require('playwright'); const { spawn } = require('child_process');
(async()=>{
 const out=process.argv[2], fps=30;
 const b=await chromium.launch(); const ctx=await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2});
 const p=await ctx.newPage();
 await p.addInitScript(()=>{try{sessionStorage.setItem('flow-intro','1')}catch{}});
 await p.route(/posthog/,r=>r.abort());
 await p.clock.install();
 await p.goto('https://maikz91.github.io/flow-media-ai/marketing/landing-page/',{waitUntil:'load'});
 await p.evaluate(()=>document.fonts.ready); await p.addStyleTag({content:'.cur,.cur-ring{display:none!important}'});
 const cdp=await ctx.newCDPSession(p); await cdp.send('Animation.enable');
 const pos=await p.evaluate(()=>{const y=s=>document.querySelector(s).getBoundingClientRect().top+scrollY;const v=document.querySelector('.vals');return{man:y('.manifest'),vals:y('.vals'),valsH:v.offsetHeight,ang:y('#angebote'),work:y('#workshop'),tool:y('#tool'),end:document.body.scrollHeight}});
 const vh=844; console.log(pos);
 // keyframes: [time s, scrollY]
 const K=[[0,0],[2.6,0],[4.2,pos.man-120],[7.2,pos.man+260],[8.2,pos.vals],[10.6,pos.vals+(pos.valsH-vh)*.3],[13,pos.vals+(pos.valsH-vh)*.62],[15.6,pos.vals+(pos.valsH-vh)*.97],[16.6,pos.ang+380],[18.2,pos.ang+380],[19.4,pos.tool-90],[21.2,pos.tool-90]];
 const T=22.4, n=Math.round(T*fps);
 const ease=x=>x<.5?4*x*x*x:1-Math.pow(-2*x+2,3)/2;
 const at=t=>{for(let i=0;i<K.length-1;i++){const[a,ya]=K[i],[bb,yb]=K[i+1];if(t<=bb)return ya+(yb-ya)*ease((t-a)/(bb-a))}return K[K.length-1][1]};
 const ff=spawn('ffmpeg',['-y','-v','error','-f','image2pipe','-framerate',String(fps),'-i','-','-c:v','libvpx-vp9','-b:v','6M','-deadline','realtime','-cpu-used','8','-pix_fmt','yuv420p',out]);
 let opened=false, t0=Date.now();
 for(let i=0;i<n;i++){
  const t=i/fps;
  if(t>=21.2&&!opened){await p.click('#fab-btn');opened=true}
  await p.evaluate(y=>window.scrollTo(0,y),Math.round(at(t)));
  await p.clock.runFor(1000/fps);
  const buf=await p.screenshot({type:'jpeg',quality:90});
  if(i===5){const per=(Date.now()-t0)/6; await cdp.send('Animation.setPlaybackRate',{playbackRate:Math.max(.05,(1000/fps)/per)}); console.log('ms/frame',per)}
  if(!ff.stdin.write(buf)) await new Promise(r=>ff.stdin.once('drain',r));
 }
 ff.stdin.end(); await new Promise(r=>ff.on('close',r)); await b.close(); console.log('frames',n);
})();
