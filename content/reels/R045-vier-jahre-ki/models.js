
/* ---------- Modelle R045 ---------- */
const ALL=[];const reg=o=>{ALL.push(o);scene.add(o);return o};
const show=(...o)=>ALL.forEach(x=>x.visible=o.includes(x));
const BLUE=new THREE.Color(0.18,0.36,1);
const addM=(g,geo_,mat,x=0,y=0,z=0)=>{const o=new THREE.Mesh(geo_,mat);o.position.set(x,y,z);g.add(o);return o};
const lineGL={vs:`attribute float u;attribute float ph;varying float vU;varying float vPh;void main(){vU=u;vPh=ph;gl_Position=projectionMatrix*modelViewMatrix*vec4(position,1.);}`,
 fs:`uniform float t,base,gain;uniform vec3 col;varying float vU;varying float vPh;void main(){float p=fract(t*.55+vPh);float pulse=smoothstep(.16,0.,abs(vU-p));gl_FragColor=vec4(mix(col,vec3(1.),pulse*.7)*(base+pulse*gain),1.);}`};
function pulseLines(pairs,R,base=.55,gain=5){const n=pairs.length,pos=new Float32Array(n*3),u=new Float32Array(n),ph=new Float32Array(n);
 for(let i=0;i<n;i+=2){const f=R();pairs[i].toArray(pos,i*3);pairs[i+1].toArray(pos,i*3+3);u[i]=0;u[i+1]=1;ph[i]=ph[i+1]=f}
 const g=new THREE.BufferGeometry();g.setAttribute('position',new THREE.BufferAttribute(pos,3));g.setAttribute('u',new THREE.BufferAttribute(u,1));g.setAttribute('ph',new THREE.BufferAttribute(ph,1));
 const m=new THREE.ShaderMaterial({uniforms:{t:{value:0},base:{value:base},gain:{value:gain},col:{value:BLUE.clone()}},vertexShader:lineGL.vs,fragmentShader:lineGL.fs,blending:THREE.AdditiveBlending,depthWrite:false,transparent:true});
 return new THREE.LineSegments(g,m)}
function dots(points,size=10,k=1.6){const g=new THREE.BufferGeometry().setFromPoints(points);
 const m=new THREE.ShaderMaterial({uniforms:{size:{value:size},k:{value:k}},vertexShader:`uniform float size;void main(){vec4 mv=modelViewMatrix*vec4(position,1.);gl_Position=projectionMatrix*mv;gl_PointSize=size;}`,
  fragmentShader:`uniform float k;void main(){float r=length(gl_PointCoord-.5);float a=smoothstep(.5,.1,r);gl_FragColor=vec4(vec3(.75,.84,1.)*a*k,1.);}`,blending:THREE.AdditiveBlending,depthWrite:false,transparent:true});
 return new THREE.Points(g,m)}

/* Sprechblase (ChatGPT, generisch) */
function makeBubble(){const g=new THREE.Group();const w=1.8,h=1.1,r=.3,x=-w/2,y=-h/2;const s=new THREE.Shape();
 s.moveTo(x+r,y);s.lineTo(x+.34,y);s.lineTo(x+.2,y-.4);s.lineTo(x+.82,y);s.lineTo(x+w-r,y);s.quadraticCurveTo(x+w,y,x+w,y+r);s.lineTo(x+w,y+h-r);s.quadraticCurveTo(x+w,y+h,x+w-r,y+h);s.lineTo(x+r,y+h);s.quadraticCurveTo(x,y+h,x,y+h-r);s.lineTo(x,y+r);s.quadraticCurveTo(x,y,x+r,y);
 const geo_=new THREE.ExtrudeGeometry(s,{depth:.16,bevelEnabled:true,bevelThickness:.05,bevelSize:.05,bevelSegments:4,curveSegments:20});geo_.translate(0,0,-.08);
 const m=new THREE.MeshStandardMaterial({color:0xf4f4f4,roughness:.32,metalness:.05,emissive:0xffffff,emissiveIntensity:.06,envMapIntensity:.7});g.add(new THREE.Mesh(geo_,m));
 g.userData.dots=[-.46,0,.46].map(px=>addM(g,new THREE.SphereGeometry(.115,24,16),new THREE.MeshBasicMaterial({color:BLUE.clone()}),px,0,.16));return g}

/* Nutzer als Lichtpunkte auf der Erde (verteilt nach der Nachtlicht-Karte) */
let people,peopleMat;
function makePeople(img,n){const c=document.createElement('canvas');c.width=1024;c.height=512;const x=c.getContext('2d');x.drawImage(img,0,0,1024,512);const d=x.getImageData(0,0,1024,512).data;const R=rng(11);
 const pos=new Float32Array(n*3),q=new Float32Array(n*2);const origin=geo(37.8,-122.4);let i=0,guard=0;
 while(i<n&&guard++<n*600){const u=R(),v=R();const k=(Math.floor(v*512)*1024+Math.floor(u*1024))*4;const b=(d[k]+d[k+1])/510;if(R()>Math.pow(b,.55)*1.5+.0015)continue;
  const p=geo((.5-v)*180,(u-.5)*360);pos.set([p.x*1.004,p.y*1.004,p.z*1.004],i*3);q[i*2]=cl(p.angleTo(origin)/Math.PI*.8+R()*.2);q[i*2+1]=.6+R()*.9;i++}
 const g=new THREE.BufferGeometry();g.setAttribute('position',new THREE.BufferAttribute(pos.subarray(0,i*3),3));g.setAttribute('q',new THREE.BufferAttribute(q.subarray(0,i*2),2));
 peopleMat=new THREE.ShaderMaterial({uniforms:{prog:{value:0},size:{value:2.2},t:{value:0}},
  vertexShader:`attribute vec2 q;uniform float prog,size,t;varying float vK;varying float vB;void main(){float on=smoothstep(q.x-.02,q.x,prog);float born=1.-smoothstep(q.x,q.x+.07,prog);vK=born;vB=on*q.y*(.75+.25*sin(t*3.+q.y*40.));vec4 mv=modelViewMatrix*vec4(position,1.);gl_Position=projectionMatrix*mv;gl_PointSize=on*size*q.y*(1.+born*1.4)*(1.1/-mv.z+.55);}`,
  fragmentShader:`varying float vK;varying float vB;void main(){float r=length(gl_PointCoord-.5);float a=smoothstep(.5,.08,r);gl_FragColor=vec4(mix(vec3(.3,.5,1.),vec3(1.),.25+vK*.6)*a*vB*(.9+vK*1.4),1.);}`,blending:THREE.AdditiveBlending,depthWrite:false,transparent:true});
 people=new THREE.Points(g,peopleMat);people.frustumCulled=false;return people}

/* Neuronales Netz als Kugel */
function makeNet(){const g=new THREE.Group();const R=rng(3);const nodes=[];
 for(let i=0;i<120;i++){const u=R()*2-1,a=R()*6.283,r=Math.sqrt(1-u*u),rad=i<78?1:.52;nodes.push(V3(r*Math.cos(a),u,r*Math.sin(a)).multiplyScalar(rad))}
 const pairs=[];nodes.forEach((p,i)=>{const d=nodes.map((o,j)=>[o.distanceTo(p),j]).sort((a,b)=>a[0]-b[0]);for(let k=1;k<=3;k++){const j=d[k][1];if(j>i||R()<.25)pairs.push(p,nodes[j])}});
 g.userData.lines=pulseLines(pairs,R,.5,6);g.add(g.userData.lines);g.add(dots(nodes,13,1.9));
 const core=addM(g,new THREE.SphereGeometry(.16,24,16),new THREE.MeshBasicMaterial({color:BLUE.clone().multiplyScalar(1.4)}));core.scale.setScalar(.55);return g}

/* Medaille (generisch, ohne Porträt) */
function makeMedal(){const g=new THREE.Group();const gold=new THREE.MeshStandardMaterial({color:0xe2b24c,metalness:1,roughness:.22,envMapIntensity:2.6});const gold2=new THREE.MeshStandardMaterial({color:0xc9983a,metalness:1,roughness:.38,envMapIntensity:2.2});
 const d=addM(g,new THREE.CylinderGeometry(.5,.5,.07,96),gold2);d.rotation.x=Math.PI/2;
 addM(g,new THREE.TorusGeometry(.5,.04,16,96),gold);addM(g,new THREE.TorusGeometry(.4,.012,12,96),gold,0,0,.036);addM(g,new THREE.TorusGeometry(.4,.012,12,96),gold,0,0,-.036);
 for(const z of[.04,-.04]){for(let i=0;i<3;i++){const t=addM(g,new THREE.TorusGeometry(.2,.014,10,64),gold,0,0,z);t.scale.y=.42;t.rotation.z=i*Math.PI/3}addM(g,new THREE.SphereGeometry(.05,20,14),gold,0,0,z)}
 for(let i=0;i<28;i++){const a=i/28*6.283;for(const z of[.037,-.037])addM(g,new THREE.SphereGeometry(.016,8,6),gold,Math.cos(a)*.455,Math.sin(a)*.455,z)}
 return g}

/* Chip (generisch, ohne Logo) */
function makeChip(){const g=new THREE.Group();const pcb=new THREE.MeshStandardMaterial({color:0x0b0f0d,metalness:.3,roughness:.55});const steel=new THREE.MeshStandardMaterial({color:0xaab0bb,metalness:1,roughness:.3,envMapIntensity:2});const gold=new THREE.MeshStandardMaterial({color:0xd2a441,metalness:1,roughness:.3,envMapIntensity:2});
 addM(g,new THREE.BoxGeometry(1.6,1.6,.07),pcb);addM(g,new THREE.BoxGeometry(.92,.92,.08),steel,0,0,.07);
 const c=document.createElement('canvas');c.width=c.height=256;const x=c.getContext('2d');x.fillStyle='#000';x.fillRect(0,0,256,256);x.strokeStyle='#5f86ff';x.lineWidth=2;for(let i=1;i<8;i++){x.beginPath();x.moveTo(i*32,8);x.lineTo(i*32,248);x.stroke();x.beginPath();x.moveTo(8,i*32);x.lineTo(248,i*32);x.stroke()}x.lineWidth=5;x.strokeRect(10,10,236,236);
 const t=new THREE.CanvasTexture(c);t.colorSpace=THREE.SRGBColorSpace;g.userData.grid=new THREE.MeshBasicMaterial({map:t,blending:THREE.AdditiveBlending,transparent:true,depthWrite:false,color:new THREE.Color(2.2,2.2,2.2)});
 addM(g,new THREE.PlaneGeometry(.86,.86),g.userData.grid,0,0,.112);
 const pin=new THREE.BoxGeometry(.045,.13,.03);for(let s=0;s<4;s++)for(let i=0;i<18;i++){const o=addM(g,pin,gold);const p=(i-8.5)*.082;const a=s*Math.PI/2;o.position.set(Math.cos(a)*.72-Math.sin(a)*p,Math.sin(a)*.72+Math.cos(a)*p,.04);o.rotation.z=a+Math.PI/2}
 const R=rng(9);for(let i=0;i<14;i++){const a=R()*6.283;addM(g,new THREE.BoxGeometry(.07,.04,.035),i%2?steel:gold,Math.cos(a)*.58,Math.sin(a)*.58,.05)}
 return g}

/* Punktgitter (Erdős: Punkte mit gleichem Abstand) */
function makeLattice(){const g=new THREE.Group();const R=rng(21);const P=[];const key={};const N=4;
 for(let i=-N;i<=N;i++)for(let j=-N;j<=N;j++){if(Math.abs(i+j)>N)continue;const p=V3((i+j*.5)*.26,j*.26*.866,0);key[i+','+j]=p;P.push(p)}
 const pairs=[];for(let i=-N;i<=N;i++)for(let j=-N;j<=N;j++){const a=key[i+','+j];if(!a)continue;for(const[di,dj]of[[1,0],[0,1],[1,-1]]){const b=key[(i+di)+','+(j+dj)];if(b)pairs.push(a,b)}}
 g.userData.lines=pulseLines(pairs,R,.42,7);g.add(g.userData.lines);g.add(dots(P,15,2.1));return g}

/* Kurs-Kurve mit Rakete an der Spitze */
function makeChart(rocket){const g=new THREE.Group();const R=rng(4);const pts=[];let y=-1;for(let i=0;i<=16;i++){const x=-.62+i/16*1.15;y+=(i%3===2?-.07:.16)+R()*.05+i*.006;pts.push(V3(x,y,0))}
 const hgt=pts[16].y+1;pts.forEach(p=>p.y=(p.y+1)/hgt*1.9-1);
 const curve=new THREE.CatmullRomCurve3(pts,false,'catmullrom',.25);g.userData.curve=curve;
 g.userData.tube=addM(g,new THREE.TubeGeometry(curve,260,.014,8,false),new THREE.MeshBasicMaterial({color:BLUE.clone().multiplyScalar(2.6)}));
 const grid=[];for(let i=0;i<=5;i++){grid.push(V3(-.7,-1+i*.4,-.02),V3(.62,-1+i*.4,-.02))}g.add(new THREE.LineSegments(new THREE.BufferGeometry().setFromPoints(grid),new THREE.LineBasicMaterial({color:0x8fa4d8,transparent:true,opacity:.28})));
 g.add(rocket);g.userData.rocket=rocket;return g}

/* Rechenzentrum: Rack-Reihen */
function makeHall(){const g=new THREE.Group();const R=rng(8);const c=document.createElement('canvas');c.width=128;c.height=512;const x=c.getContext('2d');x.fillStyle='#000';x.fillRect(0,0,128,512);
 for(let r=0;r<42;r++){for(let k=0;k<7;k++){if(R()<.4)continue;const v=R();x.fillStyle=v<.72?'#3f6bff':v<.9?'#ffffff':'#9db4ff';x.fillRect(12+k*15,10+r*12,7,3)}}
 const mk=()=>{const t=new THREE.CanvasTexture(c);t.colorSpace=THREE.SRGBColorSpace;return t};
 const body=new THREE.MeshStandardMaterial({color:0x08090c,metalness:.7,roughness:.45});
 g.userData.led=[];const geo_=new THREE.BoxGeometry(.6,2.1,1);
 for(let k=0;k<4;k++){const lm=new THREE.MeshStandardMaterial({color:0x050608,metalness:.6,roughness:.5,emissiveMap:mk(),emissive:0xffffff,emissiveIntensity:2.4});lm.emissiveMap.offset.y=k*.23;lm.emissiveMap.wrapT=THREE.RepeatWrapping;g.userData.led.push(lm);
  const im=new THREE.InstancedMesh(geo_,[lm,lm,body,body,body,body],130);let n=0;const m4=new THREE.Matrix4();
  for(let row=-5;row<=5;row++)for(let i=0;i<46;i++){if((row+50+i)%4!==k)continue;if(row===0)continue;const sx=row<0?-1:1;m4.makeTranslation(row*1.9-sx*.35,1.05,-i*1.04);im.setMatrixAt(n++,m4)}
  im.count=n;g.add(im)}
 const fl=addM(g,new THREE.PlaneGeometry(40,60),new THREE.MeshStandardMaterial({color:0x06070a,metalness:.9,roughness:.32}),0,0,-24);fl.rotation.x=-Math.PI/2;
 const ln=[];for(let i=-6;i<=6;i++){ln.push(V3(i*1.9-.95,.01,2),V3(i*1.9-.95,.01,-50))}g.add(new THREE.LineSegments(new THREE.BufferGeometry().setFromPoints(ln),new THREE.LineBasicMaterial({color:new THREE.Color(.18,.36,1).multiplyScalar(1.6)})));
 g.userData.lights=[0,1,2].map(i=>{const l=new THREE.PointLight(0x4f7bff,7,14,1.6);l.position.set(0,2.6,-3-i*9);g.add(l);return l});
 g.position.set(0,400,0);return g}

/* Kern mit Agenten-Schwarm (Fable 5.2, abstrakt) */
function makeCore(n=1300){const g=new THREE.Group();const R=rng(52);
 const core=addM(g,new THREE.IcosahedronGeometry(.3,3),new THREE.ShaderMaterial({uniforms:{t:{value:0}},vertexShader:`varying vec3 vN;varying vec3 vV;void main(){vN=normalize(normalMatrix*normal);vec4 mv=modelViewMatrix*vec4(position,1.);vV=normalize(-mv.xyz);gl_Position=projectionMatrix*mv;}`,
  fragmentShader:`uniform float t;varying vec3 vN;varying vec3 vV;void main(){float f=1.-max(dot(normalize(vN),vV),0.);vec3 c=mix(vec3(1.6,1.75,2.2),vec3(.18,.36,1.)*2.6,pow(f,1.4));gl_FragColor=vec4(c*(.9+.1*sin(t*6.)),1.);}`}));g.userData.core=core;
 const halo=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex([[0,'rgba(160,190,255,.9)'],[.3,'rgba(60,100,255,.3)'],[1,'rgba(0,0,0,0)']]),blending:THREE.AdditiveBlending,depthWrite:false,transparent:true}));halo.scale.setScalar(1.9);g.add(halo);
 const orb=new Float32Array(n*4),q=new Float32Array(n*2),pos=new Float32Array(n*3);const rings=[.62,.78,.95,1.12,1.3,1.48];
 for(let i=0;i<n;i++){const k=Math.floor(R()*rings.length);orb[i*4]=rings[k]+(R()-.5)*.03;orb[i*4+1]=(k*37+20)*DEG+(R()-.5)*.25;orb[i*4+2]=k*1.1+(R()-.5)*.2;orb[i*4+3]=R()*6.2832;q[i*2]=Math.pow(R(),.8);q[i*2+1]=.6+R()*.9}
 const mkGeo=(o,qq,cnt,ends)=>{const ge=new THREE.BufferGeometry();ge.setAttribute('position',new THREE.BufferAttribute(new Float32Array(cnt*3),3));ge.setAttribute('orb',new THREE.BufferAttribute(o,4));ge.setAttribute('q',new THREE.BufferAttribute(qq,2));if(ends)ge.setAttribute('e',new THREE.BufferAttribute(ends,1));ge.boundingSphere=new THREE.Sphere(V3(0,0,0),3);return ge};
 const orbitGL=`vec3 orbit(vec4 o,float t){float ang=o.w+t*.9/pow(o.x,1.5);vec3 p=vec3(cos(ang),0.,sin(ang))*o.x;float ci=cos(o.y),si=sin(o.y);p=vec3(p.x,-p.z*si,p.z*ci);float cr=cos(o.z),sr=sin(o.z);return vec3(p.x*cr+p.z*sr,p.y,-p.x*sr+p.z*cr);}`;
 const um={t:{value:0},prog:{value:0},size:{value:7}};g.userData.u=um;
 const pm_=new THREE.ShaderMaterial({uniforms:um,vertexShader:`attribute vec4 orb;attribute vec2 q;uniform float t,prog,size;varying float vK;varying float vB;${orbitGL}
   void main(){float on=smoothstep(q.x-.02,q.x,prog);float born=1.-smoothstep(q.x,q.x+.06,prog);vK=born;vB=on*q.y;vec4 mv=modelViewMatrix*vec4(orbit(orb,t),1.);gl_Position=projectionMatrix*mv;gl_PointSize=on*size*q.y*(1.+born*1.6);}`,
  fragmentShader:`varying float vK;varying float vB;void main(){float r=length(gl_PointCoord-.5);float a=smoothstep(.5,.1,r);gl_FragColor=vec4(mix(vec3(.35,.55,1.),vec3(1.),.3+vK*.6)*a*vB*(.95+vK*1.5),1.);}`,blending:THREE.AdditiveBlending,depthWrite:false,transparent:true});
 const pts=new THREE.Points(mkGeo(orb,q,n),pm_);pts.frustumCulled=false;g.add(pts);
 const nl=90,lo=new Float32Array(nl*2*4),lq=new Float32Array(nl*2*2),le=new Float32Array(nl*2);for(let i=0;i<nl;i++){const s=Math.floor(R()*n);for(let e=0;e<2;e++){lo.set(orb.subarray(s*4,s*4+4),(i*2+e)*4);lq.set(q.subarray(s*2,s*2+2),(i*2+e)*2);le[i*2+e]=e}}
 const lm=new THREE.ShaderMaterial({uniforms:um,vertexShader:`attribute vec4 orb;attribute vec2 q;attribute float e;uniform float t,prog;varying float vA;${orbitGL}
   void main(){float on=smoothstep(q.x-.02,q.x,prog);vA=on*(.25+.75*step(.6,fract(t*.7+q.y*9.)));gl_Position=projectionMatrix*modelViewMatrix*vec4(orbit(orb,t)*e,1.);}`,
  fragmentShader:`varying float vA;void main(){gl_FragColor=vec4(vec3(.25,.45,1.)*vA*.9,1.);}`,blending:THREE.AdditiveBlending,depthWrite:false,transparent:true});
 const ls=new THREE.LineSegments(mkGeo(lo,lq,nl*2,le),lm);ls.frustumCulled=false;g.add(ls);return g}

/* Warp-Linien (an der Kamera) */
let warp,warpMat;
function makeWarp(n=520){const R=rng(77),pos=new Float32Array(n*2*3),a=new Float32Array(n*2),s=new Float32Array(n*2);
 for(let i=0;i<n;i++){const ang=R()*6.283,rad=.5+Math.pow(R(),.7)*7,x=Math.cos(ang)*rad,y=Math.sin(ang)*rad,z=R()*60,sd=R();for(let e=0;e<2;e++){pos.set([x,y,z],(i*2+e)*3);a[i*2+e]=e;s[i*2+e]=sd}}
 const g=new THREE.BufferGeometry();g.setAttribute('position',new THREE.BufferAttribute(pos,3));g.setAttribute('a',new THREE.BufferAttribute(a,1));g.setAttribute('s',new THREE.BufferAttribute(s,1));
 warpMat=new THREE.ShaderMaterial({uniforms:{t:{value:0},len:{value:1},k:{value:0}},vertexShader:`attribute float a;attribute float s;uniform float t,len;varying float vA;void main(){float z=mod(position.z-t,60.);vA=(1.-a*.85)*smoothstep(60.,40.,z)*smoothstep(.5,6.,z)*(.4+s);gl_Position=projectionMatrix*modelViewMatrix*vec4(position.xy,-z-a*len*(.5+s),1.);}`,
  fragmentShader:`uniform float k;varying float vA;void main(){gl_FragColor=vec4(vec3(.55,.7,1.)*vA*k,1.);}`,blending:THREE.AdditiveBlending,depthWrite:false,depthTest:false,transparent:true});
 warp=new THREE.LineSegments(g,warpMat);warp.frustumCulled=false;return warp}

/* ---------- Aufbau ---------- */
const G={};let sunLight,earthLight,fill;
async function init(){
 const [day,night,cloud,spec,mw]=await Promise.all([tex('tex/8k_earth_daymap.jpg'),tex('tex/8k_earth_nightmap.jpg'),tex('tex/8k_earth_clouds.jpg',false),tex('tex/earth_spec.jpg',false),tex('tex/8k_stars_milky_way.jpg')]);
 initMats();
 milky=new THREE.Mesh(new THREE.SphereGeometry(1500,48,32),new THREE.MeshBasicMaterial({map:mw,side:THREE.BackSide,color:0x3a3a40,depthWrite:false}));milky.rotation.set(.6,1.2,.3);scene.add(milky);
 stars=makeStars();scene.add(stars);scene.add(sunCore,sunHalo,streak);
 earthMat=new THREE.ShaderMaterial({uniforms:{dayMap:{value:day},nightMap:{value:night},cloudMap:{value:cloud},specMap:{value:spec},sunDir:uSun,atmo:{value:ATMO},cloudShift:{value:0},sat:{value:.72},lights:{value:2.6}},vertexShader:earthVS,fragmentShader:earthFS});
 earth=reg(new THREE.Mesh(new THREE.SphereGeometry(1,256,128),earthMat));
 earthAtmo=reg(planetAtmo(1,ATMO,2.1));atmoMat=earthAtmo.material;
 earth.add(makePeople(night.image,42000));
 sunLight=new THREE.DirectionalLight(0xfff4e6,3.0);scene.add(sunLight);scene.add(sunLight.target);
 earthLight=new THREE.PointLight(0x7fa6ff,1.1,0,0);scene.add(earthLight);
 fill=new THREE.AmbientLight(0x223355,.25);scene.add(fill);
 G.bubble=reg(makeBubble());G.net=reg(makeNet());
 G.medals=reg(new THREE.Group());G.medals.add(makeMedal(),makeMedal());
 G.chip=reg(makeChip());G.lattice=reg(makeLattice());
 G.rocket=makeRocket();G.chart=reg(makeChart(G.rocket));
 G.hall=reg(makeHall());
 G.hero=reg(makeSat({wingLen:3.6,panels:3,chips:4}));
 G.core=reg(makeCore());
 scene.add(camera);camera.add(makeWarp());
 await document.fonts.ready;window.READY=true;DRAW(0);
}
