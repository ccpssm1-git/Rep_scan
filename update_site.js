const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

// 1. Update stats text size
// Look for text-xs text-muted-foreground and make it larger.
html = html.replace('class="mt-16 flex items-center justify-center gap-6 text-xs text-muted-foreground"', 'class="mt-16 flex items-center justify-center gap-6 text-base font-semibold text-foreground"');

// 2. Insert Client Ticker
const targetSectionEnd = '</section><section id="problem" class="py-24 relative">';
const tickerHTML = `
    <!-- Client Ticker Section -->
    <section class="py-12 border-y border-border/40 bg-background/50 overflow-hidden relative">
      <div class="text-center mb-10">
        <span class="text-sm tracking-[0.2em] font-heading font-medium text-muted-foreground uppercase opacity-80" style="letter-spacing: 0.15em;">Trusted by Global Innovators</span>
      </div>
      <div class="flex overflow-hidden group">
        <div class="flex space-x-16 items-center animate-scroll group-hover:[animation-play-state:paused] whitespace-nowrap px-8">
          <!-- Double items for infinite scroll effect -->
          <div class="text-center mx-12">
            <h3 class="font-heading font-bold text-xl md:text-3xl text-foreground/90 tracking-wide">FEEMONK</h3>
            <p class="text-[10px] md:text-xs text-muted-foreground uppercase tracking-widest mt-2 font-medium">Education Fintech</p>
          </div>
          <div class="text-center mx-12">
            <h3 class="font-heading font-bold text-xl md:text-3xl text-foreground/90 tracking-wide">DOCTUTORIALS</h3>
            <p class="text-[10px] md:text-xs text-muted-foreground uppercase tracking-widest mt-2 font-medium">Medical Edtech</p>
          </div>
          <div class="text-center mx-12">
            <h3 class="font-heading font-bold text-xl md:text-3xl text-foreground/90 tracking-wide">ORBICULAR</h3>
            <p class="text-[10px] md:text-xs text-muted-foreground uppercase tracking-widest mt-2 font-medium">Pharma Giant</p>
          </div>
          <div class="text-center mx-12">
            <h3 class="font-heading font-bold text-xl md:text-3xl text-foreground/90 tracking-wide">RE-SUSTAINABILITY</h3>
            <p class="text-[10px] md:text-xs text-muted-foreground uppercase tracking-widest mt-2 font-medium">Ramky Group</p>
          </div>
          <div class="text-center mx-12">
            <h3 class="font-heading font-bold text-xl md:text-3xl text-foreground/90 tracking-wide">BTP ICON</h3>
            <p class="text-[10px] md:text-xs text-muted-foreground uppercase tracking-widest mt-2 font-medium">Singapore Fintech</p>
          </div>
          
          <div class="text-center mx-12">
            <h3 class="font-heading font-bold text-xl md:text-3xl text-foreground/90 tracking-wide">FEEMONK</h3>
            <p class="text-[10px] md:text-xs text-muted-foreground uppercase tracking-widest mt-2 font-medium">Education Fintech</p>
          </div>
          <div class="text-center mx-12">
            <h3 class="font-heading font-bold text-xl md:text-3xl text-foreground/90 tracking-wide">DOCTUTORIALS</h3>
            <p class="text-[10px] md:text-xs text-muted-foreground uppercase tracking-widest mt-2 font-medium">Medical Edtech</p>
          </div>
          <div class="text-center mx-12">
            <h3 class="font-heading font-bold text-xl md:text-3xl text-foreground/90 tracking-wide">ORBICULAR</h3>
            <p class="text-[10px] md:text-xs text-muted-foreground uppercase tracking-widest mt-2 font-medium">Pharma Giant</p>
          </div>
          <div class="text-center mx-12">
            <h3 class="font-heading font-bold text-xl md:text-3xl text-foreground/90 tracking-wide">RE-SUSTAINABILITY</h3>
            <p class="text-[10px] md:text-xs text-muted-foreground uppercase tracking-widest mt-2 font-medium">Ramky Group</p>
          </div>
          <div class="text-center mx-12">
            <h3 class="font-heading font-bold text-xl md:text-3xl text-foreground/90 tracking-wide">BTP ICON</h3>
            <p class="text-[10px] md:text-xs text-muted-foreground uppercase tracking-widest mt-2 font-medium">Singapore Fintech</p>
          </div>
        </div>
        
        <style>
          @keyframes scroll {
            0% { transform: translateX(0); }
            100% { transform: translateX(-50%); }
          }
          .animate-scroll {
            width: max-content;
            animation: scroll 25s linear infinite;
          }
        </style>
      </div>
    </section>
    <section id="problem" class="py-24 relative">
`;

if(html.includes('id="problem"')) {
  html = html.replace('</section><section id="problem" class="py-24 relative">', tickerHTML);
} else {
  console.log("Could not find section#problem");
}

// 3. Footer replace
const startFooter = '<footer class="border-t border-border py-12">';
const endFooter = '</footer></div></div>';

const footerStartIdx = html.indexOf(startFooter);
if(footerStartIdx !== -1) {
  const footerEndIdx = html.indexOf(endFooter, footerStartIdx);
  if(footerEndIdx !== -1) {
    const originalFooter = html.substring(footerStartIdx, footerEndIdx + '</footer>'.length);
    const newFooter = `
<footer class="border-t border-white/5 py-16 bg-background relative overflow-hidden">
  <div class="container mx-auto px-6 relative z-10">
    <div class="grid grid-cols-1 md:grid-cols-4 gap-12 lg:gap-24 mb-16">
      
      <!-- Brand -->
      <div class="flex flex-col items-start gap-4">
        <div class="flex items-center gap-2">
          <img src="logo.png" alt="RepGuard Logo" class="h-6 w-auto object-contain">
          <span class="font-heading text-xl font-bold text-foreground">RepGuard</span>
        </div>
      </div>
      
      <!-- Services -->
      <div class="space-y-6">
        <h4 class="text-sm font-bold tracking-widest text-foreground uppercase">SERVICES</h4>
        <div class="flex flex-col space-y-4">
          <a href="#" class="text-sm text-muted-foreground hover:text-foreground transition-colors duration-200 inline-block w-max">Reputation Protection</a>
          <a href="#" class="text-sm text-muted-foreground hover:text-foreground transition-colors duration-200 inline-block w-max">Anti-Piracy</a>
          <a href="#" class="text-sm text-muted-foreground hover:text-foreground transition-colors duration-200 inline-block w-max">Crisis Mitigation</a>
          <a href="#" class="text-sm text-muted-foreground hover:text-foreground transition-colors duration-200 inline-block w-max">Monitoring</a>
        </div>
      </div>

      <!-- Resources -->
      <div class="space-y-6">
        <h4 class="text-sm font-bold tracking-widest text-foreground uppercase">RESOURCES</h4>
        <div class="flex flex-col space-y-4">
          <a href="#" class="text-sm text-muted-foreground hover:text-foreground transition-colors duration-200 inline-block w-max">Insights</a>
          <a href="#" class="text-sm text-muted-foreground hover:text-foreground transition-colors duration-200 inline-block w-max">Help Center</a>
          <a href="#" class="text-sm text-muted-foreground hover:text-foreground transition-colors duration-200 inline-block w-max">Pricing</a>
          <a href="#" class="text-sm text-muted-foreground hover:text-foreground transition-colors duration-200 inline-block w-max">Contact Us</a>
        </div>
      </div>

      <!-- Company -->
      <div class="space-y-6">
        <h4 class="text-sm font-bold tracking-widest text-foreground uppercase">COMPANY</h4>
        <div class="flex flex-col space-y-4">
          <a href="#" class="text-sm text-muted-foreground hover:text-foreground transition-colors duration-200 inline-block w-max">Terms & Conditions</a>
          <a href="#" class="text-sm text-muted-foreground hover:text-foreground transition-colors duration-200 inline-block w-max">Privacy Policy</a>
          <a href="#" class="text-sm text-muted-foreground hover:text-foreground transition-colors duration-200 inline-block w-max">About Us</a>
        </div>
      </div>

    </div>

    <!-- Bottom Bar -->
    <div class="pt-8 border-t border-white/5 flex flex-col md:flex-row items-center justify-between gap-6">
      <div class="text-sm text-muted-foreground leading-relaxed">
        repscan.ai &copy; 2026.<br>All Rights Reserved
      </div>
      
      <!-- Socials -->
      <div class="flex items-center gap-4">
        <a href="#" class="w-10 h-10 rounded-md bg-white hover:bg-white/90 flex items-center justify-center transition-colors group">
          <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="black" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-linkedin"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"/><rect width="4" height="12" x="2" y="9"/><circle cx="4" cy="4" r="2"/></svg>
        </a>
        <a href="#" class="w-10 h-10 rounded-md bg-white hover:bg-white/90 flex items-center justify-center transition-colors group">
          <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="black" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-instagram"><rect width="20" height="20" x="2" y="2" rx="5" ry="5"/><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/><line x1="17.5" x2="17.51" y1="6.5" y2="6.5"/></svg>
        </a>
        <a href="#" class="w-10 h-10 rounded-md bg-white hover:bg-white/90 flex items-center justify-center transition-colors group">
          <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="black" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-facebook"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/></svg>
        </a>
      </div>
    </div>
  </div>
</footer>`;
    html = html.replace(originalFooter, newFooter);
  } else {
    console.log("Could not find end of footer section.");
  }
} else {
  console.log("Could not find start of footer section.");
}

fs.writeFileSync('index.html', html, 'utf8');
console.log('Update Complete.');
