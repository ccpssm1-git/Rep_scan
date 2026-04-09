const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf-8');
console.log('Starting transformation...');

// ========== 1. Hero: "Scan My Reputation" → "Know Your Online Reputation Score" ==========
html = html.replace('>Scan My Reputation<', '>Know Your Online Reputation Score<');
console.log('✅ Hero button text updated');

// ========== 2. Swap Pages 3 (Paradigm Shift) and 4 (RepGuard Protocol) ==========
const s3Marker = '<section class="py-24 relative overflow-hidden"><div class="absolute top-0 left-1/2';
const s4Marker = '<section id="solution"';
const s5Marker = '<section id="intelligence"';
const i3 = html.indexOf(s3Marker);
const i4 = html.indexOf(s4Marker);
const i5 = html.indexOf(s5Marker);
if (i3 > 0 && i4 > i3 && i5 > i4) {
  const sec3 = html.substring(i3, i4);
  const sec4 = html.substring(i4, i5);
  html = html.substring(0, i3) + sec4 + sec3 + html.substring(i5);
  console.log('✅ Swapped pages 3 and 4');
} else {
  console.log('❌ Section swap failed:', i3, i4, i5);
}

// ========== 3. "Recover" → "Sustain" ==========
html = html.replace('>05.</span> Recover<', '>05.</span> Sustain<');
html = html.replace(
  'Strategic reputation rebuilding. Trust restoration, authority reinforcement, and long-term digital presence strengthening.',
  'Ongoing reputation fortification. Continuous trust reinforcement, authority amplification, and long-term digital resilience to maintain your permanently protected status.'
);
html = html.replace('detect, analyze, protect, respond, and recover', 'detect, analyze, protect, respond, and sustain');
// Change the rotate-ccw icon to a trending-up style icon for Sustain
html = html.replace('lucide lucide-rotate-ccw h-7 w-7 text-cyber-amber', 'lucide lucide-infinity h-7 w-7 text-cyber-amber');
html = html.replace(
  '<path d="M3 12a9 9 0 1 0 9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"></path><path d="M3 3v5h5"></path>',
  '<path d="M12 12c-2-2.67-4-4-6-4a4 4 0 1 0 0 8c2 0 4-1.33 6-4Zm0 0c2 2.67 4 4 6 4a4 4 0 0 0 0-8c-2 0-4 1.33-6 4Z"></path>'
);
console.log('✅ Recover → Sustain');

// ========== 4. "Predictive" → "Proactive Risk Analysis" + explanations ==========
html = html.replace('>Predictive Risk Analysis<', '>Proactive Risk Analysis<');
html = html.replace(
  'AI models forecast reputation threats before they materialize. Stay ahead of the crisis curve.',
  'Our AI engine proactively identifies emerging risk patterns, maps vulnerability windows, and deploys preemptive countermeasures before crises materialize. Designed for client-facing intelligence briefs that drive executive decision-making and stakeholder confidence.'
);
console.log('✅ Proactive Risk Analysis updated');

// ========== 5. Reorder "Who We Protect" ==========
// Current: Public Figures(film), Influencers(megaphone), Enterprise(building2), Executives(briefcase), Personal Safety(shield-check)
// New: Enterprise, Public Figures, Influencers, Executives, Personal Safety
const gridMarker = '<div class="grid md:grid-cols-5 gap-4 max-w-5xl mx-auto">';
const gridStart = html.indexOf(gridMarker);
if (gridStart > 0) {
  const contentStart = gridStart + gridMarker.length;
  const cardPrefix = '<div class="p-6 rounded-lg border border-border bg-card text-center group';
  let cardStarts = [];
  let sp = contentStart;
  for (let i = 0; i < 6; i++) {
    const pos = html.indexOf(cardPrefix, sp);
    if (pos === -1 || pos > contentStart + 15000) break;
    cardStarts.push(pos);
    sp = pos + 1;
  }
  if (cardStarts.length === 5) {
    const cards = [];
    for (let i = 0; i < 5; i++) {
      const end = i < 4 ? cardStarts[i + 1] : (() => {
        // Find closing </div></div></section> after last card
        let depth = 0, j = cardStarts[4];
        // Find the end of the last card div - look for closing pattern
        const afterCard = html.indexOf('</p></div>', cardStarts[4]);
        return afterCard + '</p></div>'.length;
      })();
      cards.push(html.substring(cardStarts[i], end));
    }
    // New order: Enterprise(2), Public Figures(0), Influencers(1), Executives(3), Personal Safety(4)
    const reordered = [cards[2], cards[0], cards[1], cards[3], cards[4]].join('');
    const oldCards = html.substring(cardStarts[0], cardStarts[4] + cards[4].length);
    html = html.replace(oldCards, reordered);
    console.log('✅ Reordered Who We Protect cards');
  } else {
    console.log('❌ Found', cardStarts.length, 'cards');
  }
}
// Rename "Influencers &amp; Creators" → "Influencers"
html = html.replace('>Influencers &amp; Creators<', '>Influencers<');
console.log('✅ Renamed Influencers');

// ========== 6. Command Center → Command Center 24×7 / 365 Days ==========
html = html.replace('> Command Center</span>', '> Command Center 24×7 / 365 Days</span>');
html = html.replace(
  '>Your Reputation <span class="text-gradient-primary">Command Center</span></h2>',
  '>Your Reputation <span class="text-gradient-primary">Command Center</span><br><span class="text-xl font-normal text-muted-foreground">24×7 / 365 Days</span></h2>'
);
console.log('✅ Command Center updated');

// ========== 7. Add GSAP + 3D Animation Libraries ==========
const animCSS = `
<style>
@keyframes float-icon{0%,100%{transform:translateY(0) rotate(0deg)}50%{transform:translateY(-15px) rotate(3deg)}}
@keyframes float-icon-alt{0%,100%{transform:translateY(0) rotate(0deg)}50%{transform:translateY(-10px) rotate(-2deg)}}
@keyframes spin-slow{from{transform:rotate(0deg)}to{transform:rotate(360deg)}}
@keyframes pulse-glow-3d{0%,100%{box-shadow:0 0 20px rgba(2,132,199,0.15)}50%{box-shadow:0 0 40px rgba(2,132,199,0.35),0 0 80px rgba(2,132,199,0.1)}}
@keyframes shimmer-grad{0%{background-position:-200% 0}100%{background-position:200% 0}}
@keyframes dash-march{to{stroke-dashoffset:-100}}
@keyframes gradient-morph{0%,100%{background-position:0% 50%}50%{background-position:100% 50%}}
@keyframes icon-bounce{0%,100%{transform:translateY(0) scale(1)}50%{transform:translateY(-8px) scale(1.05)}}
@keyframes orbit-dot{from{transform:rotate(0deg) translateX(var(--orbit-r)) rotate(0deg)}to{transform:rotate(360deg) translateX(var(--orbit-r)) rotate(-360deg)}}
@keyframes glow-ring{0%,100%{opacity:0.3;transform:scale(1)}50%{opacity:0.6;transform:scale(1.05)}}
.card-3d{transition:transform 0.5s cubic-bezier(0.23,1,0.32,1),box-shadow 0.5s ease;transform-style:preserve-3d}
.card-3d:hover{transform:translateY(-8px) rotateX(5deg) rotateY(-5deg) scale(1.02);box-shadow:0 25px 50px rgba(2,132,199,0.15),0 0 30px rgba(2,132,199,0.1)}
.icon-float svg{animation:icon-bounce 3s ease-in-out infinite}
.icon-float:nth-child(2) svg{animation-delay:0.5s}.icon-float:nth-child(3) svg{animation-delay:1s}
.icon-float:nth-child(4) svg{animation-delay:1.5s}.icon-float:nth-child(5) svg{animation-delay:2s}
.pulse-glow-3d{animation:pulse-glow-3d 3s ease-in-out infinite}
.shimmer-text{background:linear-gradient(90deg,hsl(var(--primary)) 0%,hsl(var(--cyber-green)) 50%,hsl(var(--primary)) 100%);background-size:200% auto;-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;animation:shimmer-grad 3s linear infinite}
.orbit-ring-3d{position:absolute;border:1px dashed rgba(2,132,199,0.15);border-radius:50%;animation:spin-slow 25s linear infinite}
.orbit-ring-3d::after{content:'';position:absolute;top:-4px;left:50%;width:8px;height:8px;background:hsl(var(--primary));border-radius:50%;box-shadow:0 0 10px rgba(2,132,199,0.5)}
.orbit-ring-rev{animation-direction:reverse;animation-duration:30s}
.orbit-ring-rev::after{background:hsl(var(--cyber-green));box-shadow:0 0 10px rgba(16,185,129,0.5)}
.moving-icon-bg{position:absolute;opacity:0.04;color:hsl(var(--primary));animation:float-icon 8s ease-in-out infinite;pointer-events:none}
.moving-icon-bg:nth-child(2n){animation:float-icon-alt 10s ease-in-out infinite;animation-delay:2s}
.moving-icon-bg:nth-child(3n){animation-delay:4s;animation-duration:12s}
.workflow-step-icon{animation:pulse-glow-3d 3s ease-in-out infinite}
.gradient-animated-bg{background-size:200% 200%;animation:gradient-morph 8s ease infinite}
</style>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"><\/script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"><\/script>
`;
html = html.replace('</head>', animCSS + '</head>');

// Add GSAP animation script before the 3D canvas
const gsapInit = `
<script>
document.addEventListener('DOMContentLoaded',()=>{
  if(typeof gsap==='undefined')return;
  gsap.registerPlugin(ScrollTrigger);

  // Hero entrance
  gsap.from('.min-h-screen h1',{opacity:0,y:60,duration:1.2,ease:'power3.out',delay:0.3});
  gsap.from('.min-h-screen p',{opacity:0,y:40,duration:1,ease:'power3.out',delay:0.6});
  gsap.from('.min-h-screen button',{opacity:0,y:30,duration:0.8,ease:'power3.out',stagger:0.15,delay:0.9});

  // Stat cards
  document.querySelectorAll('.glow-border').forEach((el,i)=>{
    el.classList.add('card-3d');
    gsap.from(el,{scrollTrigger:{trigger:el,start:'top 85%',toggleActions:'play none none reverse'},
      opacity:0,y:50,rotationX:15,duration:0.8,delay:i*0.1,ease:'power3.out'});
  });

  // Threat cards
  document.querySelectorAll('#problem .bg-card').forEach((el,i)=>{
    el.classList.add('card-3d','icon-float');
    gsap.from(el,{scrollTrigger:{trigger:el,start:'top 85%',toggleActions:'play none none reverse'},
      opacity:0,y:60,scale:0.9,duration:0.7,delay:i*0.12,ease:'back.out(1.4)'});
  });

  // Section headings
  document.querySelectorAll('section h2').forEach(h=>{
    gsap.from(h,{scrollTrigger:{trigger:h,start:'top 80%',toggleActions:'play none none reverse'},
      opacity:0,y:40,duration:1,ease:'power3.out'});
  });

  // Section badges
  document.querySelectorAll('section .inline-flex.rounded-full').forEach(b=>{
    gsap.from(b,{scrollTrigger:{trigger:b,start:'top 85%',toggleActions:'play none none reverse'},
      opacity:0,scale:0.8,duration:0.6,ease:'back.out(1.7)'});
  });

  // Workflow steps
  document.querySelectorAll('#solution .flex.gap-6').forEach((s,i)=>{
    gsap.from(s,{scrollTrigger:{trigger:s,start:'top 80%',toggleActions:'play none none reverse'},
      opacity:0,x:-50,duration:0.8,delay:i*0.15,ease:'power3.out'});
    const ic=s.querySelector('.w-16');
    if(ic)ic.classList.add('pulse-glow-3d');
  });

  // Intelligence cards
  document.querySelectorAll('#intelligence .bg-card').forEach((el,i)=>{
    el.classList.add('card-3d');
    gsap.from(el,{scrollTrigger:{trigger:el,start:'top 85%',toggleActions:'play none none reverse'},
      opacity:0,y:50,rotationY:-10,duration:0.8,delay:i*0.15,ease:'power3.out'});
  });

  // Who We Protect cards
  document.querySelectorAll('.grid.md\\\\:grid-cols-5 .p-6').forEach((el,i)=>{
    el.classList.add('card-3d','icon-float');
    gsap.from(el,{scrollTrigger:{trigger:el,start:'top 85%',toggleActions:'play none none reverse'},
      opacity:0,y:40,scale:0.85,duration:0.7,delay:i*0.1,ease:'back.out(1.5)'});
  });

  // Dashboard console
  const dash=document.querySelector('#dashboard .max-w-5xl');
  if(dash){
    gsap.from(dash,{scrollTrigger:{trigger:dash,start:'top 80%',toggleActions:'play none none reverse'},
      opacity:0,y:60,scale:0.95,rotationX:8,duration:1.2,ease:'power3.out',transformOrigin:'center top'});
  }

  // Comparison table rows
  document.querySelectorAll('.grid.grid-cols-3.border-b').forEach((r,i)=>{
    gsap.from(r,{scrollTrigger:{trigger:r,start:'top 90%',toggleActions:'play none none reverse'},
      opacity:0,x:-30,duration:0.5,delay:i*0.08,ease:'power2.out'});
  });

  // CTA section
  const cta=document.querySelector('.py-32');
  if(cta){
    gsap.from(cta.querySelector('h2'),{scrollTrigger:{trigger:cta,start:'top 75%',toggleActions:'play none none reverse'},
      opacity:0,y:50,scale:0.9,duration:1,ease:'power3.out'});
    gsap.from(cta.querySelectorAll('button'),{scrollTrigger:{trigger:cta,start:'top 70%',toggleActions:'play none none reverse'},
      opacity:0,y:30,stagger:0.15,duration:0.8,delay:0.3,ease:'back.out(1.3)'});
  }

  // 3D tilt on mouse move
  document.querySelectorAll('.card-3d').forEach(card=>{
    card.addEventListener('mousemove',e=>{
      const r=card.getBoundingClientRect();
      const rx=(e.clientY-r.top-r.height/2)/(r.height/2)*-8;
      const ry=(e.clientX-r.left-r.width/2)/(r.width/2)*8;
      card.style.transform='translateY(-8px) rotateX('+rx+'deg) rotateY('+ry+'deg) scale(1.02)';
    });
    card.addEventListener('mouseleave',()=>{card.style.transform='';});
  });

  // Add orbit rings to hero
  const hero=document.querySelector('.min-h-screen');
  if(hero){
    const oc=document.createElement('div');
    oc.style.cssText='position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);pointer-events:none;z-index:0;';
    ['300','450'].forEach((s,i)=>{
      const r=document.createElement('div');
      r.className='orbit-ring-3d'+(i?' orbit-ring-rev':'');
      r.style.cssText='width:'+s+'px;height:'+s+'px;top:-'+(s/2)+'px;left:-'+(s/2)+'px;position:absolute;';
      oc.appendChild(r);
    });
    hero.appendChild(oc);
  }

  // Add floating background icons to sections
  const iconSVGs=[
    '<svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1"><path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/></svg>',
    '<svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></svg>',
    '<svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10"/></svg>',
    '<svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/></svg>'
  ];
  document.querySelectorAll('section').forEach(sec=>{
    if(!sec.querySelector('.moving-icon-bg')){
      sec.style.position=sec.style.position||'relative';
      for(let i=0;i<3;i++){
        const d=document.createElement('div');
        d.className='moving-icon-bg';
        d.innerHTML=iconSVGs[i%iconSVGs.length];
        d.style.top=(15+Math.random()*60)+'%';
        d.style.left=(5+Math.random()*85)+'%';
        d.style.animationDelay=(i*2.5)+'s';
        sec.insertBefore(d,sec.firstChild);
      }
    }
  });
});
<\/script>
`;
html = html.replace('<!-- 3D Parallax Three.js Background -->', gsapInit + '\n<!-- 3D Parallax Three.js Background -->');
console.log('✅ Added GSAP + 3D animations');

// ========== 8. Enhance Three.js with rotating 3D shield ==========
const enhancedThreeJS = `
    // === Enhanced 3D: Rotating shield wireframe ===
    const shieldGroup = new THREE.Group();
    scene.add(shieldGroup);
    
    // Create shield shape
    const shieldShape = new THREE.Shape();
    shieldShape.moveTo(0, 6);
    shieldShape.bezierCurveTo(0, 6, 5, 5, 5, 2);
    shieldShape.lineTo(5, -2);
    shieldShape.bezierCurveTo(5, -5, 0, -7, 0, -7);
    shieldShape.bezierCurveTo(0, -7, -5, -5, -5, -2);
    shieldShape.lineTo(-5, 2);
    shieldShape.bezierCurveTo(-5, 5, 0, 6, 0, 6);
    
    const shieldGeo = new THREE.ExtrudeGeometry(shieldShape, {depth:1, bevelEnabled:false});
    const shieldMat = new THREE.MeshBasicMaterial({color:0x0284c7, wireframe:true, transparent:true, opacity:0.08});
    const shieldMesh = new THREE.Mesh(shieldGeo, shieldMat);
    shieldMesh.scale.set(4, 4, 4);
    shieldGroup.add(shieldMesh);
    
    // Glowing particles around shield
    const glowCount = 50;
    const glowGeo = new THREE.BufferGeometry();
    const glowPos = new Float32Array(glowCount * 3);
    for(let i=0;i<glowCount;i++){
      const angle = (i/glowCount)*Math.PI*2;
      const r = 25 + Math.random()*15;
      glowPos[i*3] = Math.cos(angle)*r;
      glowPos[i*3+1] = Math.sin(angle)*r;
      glowPos[i*3+2] = (Math.random()-0.5)*10;
    }
    glowGeo.setAttribute('position', new THREE.BufferAttribute(glowPos, 3));
    const glowMat = new THREE.PointsMaterial({color:0x0284c7, size:2, transparent:true, opacity:0.3});
    const glowPts = new THREE.Points(glowGeo, glowMat);
    shieldGroup.add(glowPts);
`;

const enhancedAnimate = `
            // Rotate shield
            if(shieldGroup){
              shieldGroup.rotation.y += 0.003;
              shieldGroup.rotation.x = Math.sin(Date.now()*0.001)*0.1;
            }
`;

// Insert shield creation after linesMesh
html = html.replace(
  "// Subtle ambient movement",
  enhancedThreeJS + "\n        // Subtle ambient movement"
);
// Insert shield rotation in animation loop
html = html.replace(
  "// Setup Parallax for camera",
  enhancedAnimate + "\n            // Setup Parallax for camera"
);
console.log('✅ Enhanced Three.js with 3D shield');

fs.writeFileSync('index.html', html);
console.log('\n🎉 All transformations complete!');
