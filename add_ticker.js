const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

const tickerHTML = `
    <!-- Client Ticker Section -->
    <section class="py-12 bg-background relative overflow-hidden" style="border-top: 1px solid rgba(255,255,255,0.05);">
      <div class="text-center mb-10 mt-10">
        <span class="text-sm tracking-[0.2em] font-heading font-medium text-muted-foreground uppercase opacity-80" style="letter-spacing: 0.15em;">Trusted by Global Innovators</span>
      </div>
      <div class="flex overflow-hidden group">
        <div class="flex space-x-16 items-center animate-scroll whitespace-nowrap px-8">
          <!-- Item 1 -->
          <div class="text-center mx-12">
            <h3 class="font-heading font-[800] text-2xl md:text-4xl text-foreground tracking-wide opacity-90">FEEMONK</h3>
            <p class="text-[10px] md:text-xs text-muted-foreground uppercase tracking-[0.2em] mt-2 font-semibold">Education Fintech</p>
          </div>
          <!-- Item 2 -->
          <div class="text-center mx-12">
            <h3 class="font-heading font-[800] text-2xl md:text-4xl text-foreground tracking-wide opacity-90">DOCTUTORIALS</h3>
            <p class="text-[10px] md:text-xs text-muted-foreground uppercase tracking-[0.2em] mt-2 font-semibold">Medical Edtech</p>
          </div>
          <!-- Item 3 -->
          <div class="text-center mx-12">
            <h3 class="font-heading font-[800] text-2xl md:text-4xl text-foreground tracking-wide opacity-90">ORBICULAR</h3>
            <p class="text-[10px] md:text-xs text-muted-foreground uppercase tracking-[0.2em] mt-2 font-semibold">Pharma Giant</p>
          </div>
          <!-- Item 4 -->
          <div class="text-center mx-12">
            <h3 class="font-heading font-[800] text-2xl md:text-4xl text-foreground tracking-wide opacity-90">RE-SUSTAINABILITY</h3>
            <p class="text-[10px] md:text-xs text-muted-foreground uppercase tracking-[0.2em] mt-2 font-semibold">Ramky Group</p>
          </div>
          <!-- Item 5 -->
          <div class="text-center mx-12">
            <h3 class="font-heading font-[800] text-2xl md:text-4xl text-foreground tracking-wide opacity-90">BTP ICON</h3>
            <p class="text-[10px] md:text-xs text-muted-foreground uppercase tracking-[0.2em] mt-2 font-semibold">Singapore Fintech</p>
          </div>
          
          <!-- Duplicated for infinite scroll -->
          <div class="text-center mx-12">
            <h3 class="font-heading font-[800] text-2xl md:text-4xl text-foreground tracking-wide opacity-90">FEEMONK</h3>
            <p class="text-[10px] md:text-xs text-muted-foreground uppercase tracking-[0.2em] mt-2 font-semibold">Education Fintech</p>
          </div>
          <div class="text-center mx-12">
            <h3 class="font-heading font-[800] text-2xl md:text-4xl text-foreground tracking-wide opacity-90">DOCTUTORIALS</h3>
            <p class="text-[10px] md:text-xs text-muted-foreground uppercase tracking-[0.2em] mt-2 font-semibold">Medical Edtech</p>
          </div>
          <div class="text-center mx-12">
            <h3 class="font-heading font-[800] text-2xl md:text-4xl text-foreground tracking-wide opacity-90">ORBICULAR</h3>
            <p class="text-[10px] md:text-xs text-muted-foreground uppercase tracking-[0.2em] mt-2 font-semibold">Pharma Giant</p>
          </div>
          <div class="text-center mx-12">
            <h3 class="font-heading font-[800] text-2xl md:text-4xl text-foreground tracking-wide opacity-90">RE-SUSTAINABILITY</h3>
            <p class="text-[10px] md:text-xs text-muted-foreground uppercase tracking-[0.2em] mt-2 font-semibold">Ramky Group</p>
          </div>
          <div class="text-center mx-12">
            <h3 class="font-heading font-[800] text-2xl md:text-4xl text-foreground tracking-wide opacity-90">BTP ICON</h3>
            <p class="text-[10px] md:text-xs text-muted-foreground uppercase tracking-[0.2em] mt-2 font-semibold">Singapore Fintech</p>
          </div>
        </div>
        
        <style>
          @keyframes scroll {
            0% { transform: translateX(0); }
            100% { transform: translateX(-50%); }
          }
          .animate-scroll {
            width: max-content;
            animation: scroll 20s linear infinite;
          }
        </style>
      </div>
    </section>
`;

const footerMarker = '<footer class="border-t border-white/5 py-16 bg-[#030712] text-white relative overflow-hidden">';
if (html.includes(footerMarker)) {
  html = html.replace(footerMarker, tickerHTML + '\n' + footerMarker);
  fs.writeFileSync('index.html', html, 'utf8');
  console.log("Ticker inserted successfully before footer.");
} else {
  console.log("Could not find new footer marker.");
}
