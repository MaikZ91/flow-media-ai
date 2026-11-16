
/* ---------- Bühne: Kamera über der Erde, Objekt vor der Kamera ---------- */
function camBasis(){return{cu:V3(0,1,0).applyQuaternion(camera.quaternion),cr:V3(1,0,0).applyQuaternion(camera.quaternion),cb:V3(0,0,1).applyQuaternion(camera.quaternion)}}
function stage(P,{sunElev=30*DEG,sunAz=2.4,lon=0,fov=44,pitch=-.5,head=0,roll=0,sunVis=true}={}){const up=P.clone().normalize();const sb=frameAt(P,V3(.3,.2,1));const f=sb.f.clone().applyAxisAngle(up,head);
 const sdir=f.clone().applyAxisAngle(up,sunAz).multiplyScalar(Math.cos(sunElev)).addScaledVector(up,Math.sin(sunElev));
 setCam(P,P.clone().addScaledVector(f,Math.cos(pitch)).addScaledVector(up,Math.sin(pitch)),up.clone().applyAxisAngle(f,roll),fov);setSun(sdir,sunVis);aimEarth(P,lon);earthLight.position.set(0,0,0);}
function place(o,{d=.05,x=0,y=-.08,size=.2,rx=0,ry=0,rz=0}={}){const{cu,cr,cb}=camBasis();const hgt=2*d*Math.tan(camera.fov*DEG/2);
 o.position.copy(camera.position).addScaledVector(cb,-d).addScaledVector(cr,x*hgt).addScaledVector(cu,y*hgt);
 o.quaternion.copy(camera.quaternion).multiply(new THREE.Quaternion().setFromEuler(new THREE.Euler(rx,ry,rz)));o.scale.setScalar(size*hgt)}
const pop=u=>{const x=cl(u/.22);return 1-Math.pow(1-x,3)*(1-2.2*x*(1-x))};

/* ---------- Szenen ---------- */
function Z0(u,t){show(earth,earthAtmo);earth.rotation.y=0;earthMat.uniforms.lights.value=4.2;bloom.strength=.6;
 const Pc=geo(46,8);const d=lerp(6.4,1.72,out3(u*.96));const cp=Pc.clone().applyAxisAngle(V3(0,1,0),.5-.5*out3(u)).multiplyScalar(d);
 setCam(cp,V3(0,.17*d,0),V3(0,1,0),44);setSun(Pc.clone().multiplyScalar(-1).applyAxisAngle(V3(0,1,0),.62),true);
 warpMat.uniforms.k.value=.55*(1-u);warpMat.uniforms.t.value=t*26;warpMat.uniforms.len.value=5;}
function Z22(u,t){show(earth,earthAtmo,G.bubble);earthMat.uniforms.lights.value=3.2;bloom.strength=.5;fill.intensity=1.2;
 stage(geo(39+u*1.5,-98+u*5).multiplyScalar(1.42-.03*u),{sunElev:-41*DEG,sunAz:1.2,lon:-98+u*5,pitch:-.74,fov:44});
 place(G.bubble,{d:.05,y:-.02+.008*Math.sin(t*2),size:.15*pop(u),ry:-.28+.2*u,rx:.06});
 G.bubble.userData.dots.forEach((d,i)=>{const p=.5+.5*Math.sin(t*7-i*1.1);d.material.color.copy(BLUE).multiplyScalar(.6+p*3.4);d.scale.setScalar(.8+p*.45)});
 peopleMat.uniforms.prog.value=sm((u-.08)/.8)*1.08;peopleMat.uniforms.size.value=2.7;}
function Z23(u,t){show(earth,earthAtmo,G.net);bloom.strength=.66;
 stage(geo(12,62+u*4).multiplyScalar(1.24),{sunElev:15*DEG,sunAz:2.75,lon:62+u*4,pitch:-.5});
 place(G.net,{d:.05,y:-.11,size:.2*pop(u),ry:t*.5,rx:.3});G.net.userData.lines.material.uniforms.t.value=t;}
function Z24(u,t){show(earth,earthAtmo,G.medals);bloom.strength=.5;fill.intensity=.9;
 stage(geo(56,14+u*4).multiplyScalar(1.2),{sunElev:27*DEG,sunAz:2.5,lon:14+u*4,pitch:-.52});
 place(G.medals,{d:.05,y:-.12,size:.23});const[a,b]=G.medals.children;const s=pop(u),s2=pop(u-.12);
 a.position.set(-.5,.2,0);a.rotation.set(0,.45+Math.sin(t*1.5)*.55,-.08);a.scale.setScalar(s);
 b.position.set(.5,-.42,0);b.rotation.set(0,-.4+Math.sin(t*1.5+1.4)*.55,.08);b.scale.setScalar(Math.max(s2,.001));}
function Z25(u,t){show(earth,earthAtmo,G.chip);bloom.strength=.6;fill.intensity=.8;
 stage(geo(24,121+u*4).multiplyScalar(1.2),{sunElev:34*DEG,sunAz:2.35,lon:121+u*4,pitch:-.5});
 place(G.chip,{d:.05,y:-.13,size:.21*pop(u),rx:-.82,rz:.5+t*.32});G.chip.userData.grid.color.setScalar(1.6+1.4*Math.sin(t*6));}
function ZT(u,t){show(earth,earthAtmo);bloom.strength=.7;
 stage(geo(10,-30).multiplyScalar(lerp(1.3,2.7,u*u)),{sunElev:22*DEG,sunAz:2.2,lon:-30,pitch:lerp(-.5,.5,sm(u)),fov:lerp(44,74,sm(u))});
 warpMat.uniforms.k.value=Math.pow(u,1.4)*1.5;warpMat.uniforms.t.value=t*lerp(10,60,u)-240;warpMat.uniforms.len.value=lerp(1,16,u);}
function Z26(u,t){show();bloom.strength=.9;
 stage(geo(10,-30).multiplyScalar(3),{sunElev:22*DEG,sunAz:2.2,lon:-30,pitch:.6,fov:lerp(78,60,out3(u)),sunVis:false});
 warpMat.uniforms.k.value=lerp(1.6,.7,u);warpMat.uniforms.t.value=t*52;warpMat.uniforms.len.value=lerp(18,7,u);}
function M5(u,t){show(earth,earthAtmo,G.lattice);bloom.strength=.66;
 stage(geo(-22,24+u*4).multiplyScalar(1.28),{sunElev:30*DEG,sunAz:2.6,lon:24+u*4,pitch:-.52});
 place(G.lattice,{d:.05,y:-.12,size:.19*pop(u),rx:-.62,rz:.3+t*.28});G.lattice.userData.lines.material.uniforms.t.value=t*1.6;}
function M6(u,t){show(earth,earthAtmo,G.chart);bloom.strength=.6;fill.intensity=1.1;
 stage(geo(28,-81+u*4).multiplyScalar(1.22),{sunElev:17*DEG,sunAz:2.2,lon:-81+u*4,pitch:-.46});
 place(G.chart,{d:.05,y:-.1,size:.34,ry:-.22+.14*u});const c=G.chart.userData.curve,p=cl(.06+sm(u*1.08)*.94);
 G.chart.userData.tube.geometry.setDrawRange(0,Math.floor(p*260)*48);const rk=G.chart.userData.rocket,pt=c.getPoint(p),tg=c.getTangent(p).add(V3(0,1.4,0)).normalize();
 rk.scale.setScalar(.022);rk.position.copy(pt).addScaledVector(tg,.02);rk.quaternion.setFromUnitVectors(V3(0,1,0),tg);rk.userData.pl.forEach(m=>m.uniforms.t.value=t);}
function M8(u,t){show(earth,earthAtmo);earth.rotation.y=.1*u;earthMat.uniforms.lights.value=2.6;bloom.strength=.7;
 const Pc=geo(24,84);const d=4.7-.5*sm(u);const cp=Pc.clone().applyAxisAngle(V3(0,1,0),-.12+.24*u).multiplyScalar(d);
 setCam(cp,V3(0,.19*d,0),V3(0,1,0).applyAxisAngle(V3(0,0,1),.08),40);setSun(Pc.clone().multiplyScalar(-1).applyAxisAngle(V3(0,1,0),.7).add(V3(0,.25,0)),true);
 peopleMat.uniforms.prog.value=.5+.6*sm(u/.6);peopleMat.uniforms.size.value=2.1;}
function M9(u,t){show(G.hall);bloom.strength=.75;fill.intensity=.5;
 setCam(V3(0,401.42,1.4-5.5*u),V3(0,401.05,-30),V3(0,1,0),60);setSun(V3(.2,1,.4),false);
 G.hall.userData.led.forEach((m,k)=>{m.emissiveIntensity=2.2+1.3*Math.sin(t*5+k*1.7);m.emissiveMap.offset.y=k*.23+Math.floor(t*4+k*.5)*.071});
 G.hall.userData.lights.forEach((l,i)=>l.position.z=-2-i*9-5.5*u);}
function M10(u,t){show(earth,earthAtmo,G.hero);bloom.strength=.6;
 G.hero.userData.chips.forEach((c,k)=>c.material.emissiveIntensity=(t*4+k)%4<1.6?9:3.5);
 satShot(G.hero,geo(30,-40).multiplyScalar(1.12),26*DEG,u,{dist:.04,fov:44,spin:.35,yaw0:-.3,camH:.36,tilt:-.26,lon:-40,tgtDown:-.1,size:.00168,sunAz:2.3,orbit:.3,a0:.05,side:-.03});}
function FIN(u,t){show(earth,earthAtmo,G.core);earthMat.uniforms.lights.value=3.2;bloom.strength=.62;
 stage(geo(8,-150+u*6).multiplyScalar(1.5-.04*u),{sunElev:(-50+u*2.2)*DEG,sunAz:1.1,lon:-150+u*6,pitch:-.73});
 place(G.core,{d:.06,y:-.07,size:.155*pop(u*.6),rx:.42,ry:t*.22});const U=G.core.userData.u;U.t.value=t;U.prog.value=sm((u-.06)/.5)*1.07;U.size.value=5.5;G.core.userData.core.material.uniforms.t.value=t;}
function OUT(u,t){show(earth,earthAtmo);earth.rotation.y=2.4+.05*u;earthMat.uniforms.lights.value=3;bloom.strength=.8;
 const Pc=geo(20,10);const d=3.5+.5*sm(u);const cp=Pc.clone().multiplyScalar(d);
 setCam(cp,V3(0,.2*d,0).applyAxisAngle(V3(1,0,0),0),V3(0,1,0),42);
 setSun(Pc.clone().multiplyScalar(-1).applyAxisAngle(V3(0,1,0),lerp(.2,.52,sm(u))).add(V3(0,.32,0)),true);
 peopleMat.uniforms.prog.value=1.1;peopleMat.uniforms.size.value=1.8;}
const SC=[Z0,Z22,Z23,Z24,Z25,ZT,Z26,M5,M6,M8,M9,M10,FIN,OUT];

/* ---------- Text ---------- */
const $=id=>document.getElementById(id);
function vis(id,a,b,t,dy=40,f=.2,fo=.1){const e=$(id);if(t<a||t>=b){e.style.opacity=0;return 0}const i=out3((t-a)/f),o=1-cl((t-(b-fo))/fo);e.style.opacity=Math.min(i,o);e.style.transform=`translateY(${(1-i)*dy}px)`;return i}
const de=n=>Math.round(n).toLocaleString('de-DE');
const YEAR=[-1,0,1,2,3,3,4,4,4,4,4,4,4,4];
function TEXT(t,i){
 $('topfade').style.opacity=i===6?0:1;
 vis('hook',0,T[1],t,60,.2);
 vis('y22',T[1],T[2],t);$('n22').textContent=de(100*sm((t-T[1]-.35)/1.5));
 vis('y23',T[2],T[3],t);vis('y24',T[3],T[4],t);vis('y25',T[4],T[5],t);
 vis('tr',T[5],T[6],t,40,.25,.06);
 {const e=$('t26'),u=(t-T[6])/(T[7]-T[6]);if(i===6){e.style.opacity=Math.min(1,1-cl((u-.86)/.14));e.style.transform=`scale(${1.35-.35*out3(u*2.4)})`}else e.style.opacity=0}
 $('flash').style.opacity=t>=T[6]?Math.max(0,.9-(t-T[6])/.28*.9):0;
 vis('m5',T[7],T[8],t);vis('m6',T[8],T[9],t);
 vis('m8',T[9],T[10],t);$('n8').textContent=de(1e9*Math.pow(sm((t-T[9])/.9),1.5));
 vis('m9',T[10],T[11],t);vis('m10',T[11],T[12],t);
 vis('fin',T[12],T[13],t,50,.25);$('nag').textContent=de(1000*sm((t-T[12]-.3)/1.9));
 vis('outro',T[13],99,t,50,.3);vis('made',T[13]+3*B,99,t,30,.3);
 const y=YEAR[i],ys=$('years').children;for(let k=0;k<ys.length;k++){const idx=k>>1;if(k%2===0)ys[k].className=idx===y?'now':idx<y?'on':'';else ys[k].className=idx<y?'on':''}
 $('years').style.opacity=i===6?0:1;
 const a=$('av');const s=t<1.4?1.5-.5*sm((t-.9)/.5):1;a.style.transform=`scale(${s})`;a.style.opacity=i===6?0:1;$('logo').style.opacity=i===6?.0:1;
 $('bar').style.width=(W*t/T[14])+'px';}

const NOTEXT=location.search.includes('notext');if(NOTEXT)document.querySelectorAll('.l,#topfade,#flash').forEach(e=>e.style.display='none');
window.DRAW=t=>{t=Math.min(t,T[14]-1e-4);let i=0;while(i<13&&t>=T[i+1])i++;const u=(t-T[i])/(T[i+1]-T[i]);
 fill.intensity=.25;earthLight.intensity=1.1;earthMat.uniforms.lights.value=2.6;earthMat.uniforms.cloudShift.value=t*.00035;peopleMat.uniforms.t.value=t;
 warpMat.uniforms.k.value=0;stars.visible=milky.visible=i!==10;if(i!==1&&i!==9&&i!==13)peopleMat.uniforms.prog.value=0;
 SC[i](u,t);composer.render();if(!NOTEXT)TEXT(t,i);};
init();
