const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

const footerRegex = /<footer[^>]*>[\s\S]*?<\/footer>/i;

const newFooter = `
<style>
  .custom-footer {
    background-color: #000000 !important;
    color: white !important;
    border-top: 1px solid rgba(255,255,255,0.1);
    font-family: 'Inter', sans-serif;
    padding-top: 6rem;
    padding-bottom: 4rem;
  }
  .custom-footer h4 { 
    color: white !important; 
    font-size: 0.85rem;
    font-weight: 700;
    letter-spacing: 0.2em;
    margin-bottom: 2rem;
    text-transform: uppercase;
  }
  .custom-footer-link {
    color: rgba(255, 255, 255, 0.45) !important;
    font-size: 0.95rem;
    transition: all 0.2s;
    text-decoration: none;
    display: inline-block;
  }
  .custom-footer-link:hover { 
    color: #00D8FF !important;
    transform: translateX(4px);
  }
  .custom-social-icon {
    width: 44px;
    height: 44px;
    background-color: white;
    border-radius: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  }
  .custom-social-icon:hover {
    transform: translateY(-5px);
    background-color: #00D8FF;
  }
  .custom-social-icon:hover svg {
    fill: white;
  }
  .custom-social-icon svg {
    width: 20px;
    height: 20px;
    fill: #000000;
    transition: fill 0.3s;
  }
</style>
<footer class="custom-footer">
  <div class="container max-w-7xl mx-auto px-6">
    <!-- Top Section: Logo (Left) and Links (Right Grouped) -->
    <div class="flex flex-col lg:flex-row justify-between gap-16 mb-24">
      
      <!-- Logo Side -->
      <div class="flex flex-col items-start max-w-sm">
        <div class="flex items-center gap-4 mb-8">
          <div class="w-12 h-12 bg-[#00D8FF] rounded-full flex items-center justify-center p-2.5 shadow-[0_0_20px_rgba(0,216,255,0.3)]">
            <img src="logo.png" alt="" class="w-full h-full object-contain brightness-0 invert">
          </div>
          <span class="font-heading text-3xl font-bold tracking-tight text-white">Rep<span style="color: #00D8FF;">Guard</span></span>
        </div>
        <p class="text-white/40 text-sm leading-relaxed">
          The ultimate cyber defense protocol for your digital reputation. Active intelligence and proactive protection for global innovators.
        </p>
      </div>

      <!-- Links Side (Tightly Grouped on Right) -->
      <div class="flex flex-wrap gap-12 lg:gap-24">
        <div>
          <h4>SERVICES</h4>
          <ul class="flex flex-col space-y-4 list-none p-0 m-0">
            <li><a href="#" class="custom-footer-link">Reputation Protection</a></li>
            <li><a href="#" class="custom-footer-link">Anti-Piracy Control</a></li>
            <li><a href="#" class="custom-footer-link">Crisis Mitigation</a></li>
            <li><a href="#" class="custom-footer-link">SOC Monitoring</a></li>
          </ul>
        </div>
        <div>
          <h4>RESOURCES</h4>
          <ul class="flex flex-col space-y-4 list-none p-0 m-0">
            <li><a href="#" class="custom-footer-link">Intelligence Insights</a></li>
            <li><a href="#" class="custom-footer-link">Threat Analysis</a></li>
            <li><a href="#" class="custom-footer-link">Help Center</a></li>
            <li><a href="#" class="custom-footer-link">Pricing Plans</a></li>
          </ul>
        </div>
        <div>
          <h4>COMPANY</h4>
          <ul class="flex flex-col space-y-4 list-none p-0 m-0">
            <li><a href="#" class="custom-footer-link">Terms & Service</a></li>
            <li><a href="#" class="custom-footer-link">Privacy Policy</a></li>
            <li><a href="#" class="custom-footer-link">About RepGuard</a></li>
          </ul>
        </div>
      </div>

    </div>

    <!-- Bottom Bar: Copyright (Left) and Socials (Right) -->
    <div class="pt-10 flex flex-col md:flex-row items-center justify-between border-t border-white/10 gap-8">
      <div class="text-sm text-white/30 tracking-wide font-medium">
        repscan.ai &copy; 2026. ALL RIGHTS RESERVED.
      </div>
      
      <div class="flex items-center gap-5">
        <a href="https://www.linkedin.com/company/rep-guard/" target="_blank" class="custom-social-icon" title="LinkedIn">
          <svg viewBox="0 0 24 24"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.761 0 5-2.239 5-5v-14c0-2.761-2.239-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>
        </a>
        <a href="#" target="_blank" class="custom-social-icon" title="Instagram">
          <svg viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
        </a>
        <a href="#" target="_blank" class="custom-social-icon" title="Facebook">
          <svg viewBox="0 0 24 24"><path d="M22.675 0h-21.35c-.732 0-1.325.593-1.325 1.325v21.351c0 .731.593 1.324 1.325 1.324h11.495v-8.74h-2.94v-3.403h2.94v-2.511c0-2.91 1.777-4.496 4.376-4.496 1.244 0 2.315.092 2.627.134v3.044h-1.803c-1.412 0-1.685.671-1.685 1.655v2.174h3.371l-.439 3.403h-2.932v8.74h6.104c.733 0 1.326-.593 1.326-1.324v-21.351c0-.732-.593-1.325-1.326-1.325z"/></svg>
        </a>
      </div>
    </div>
  </div>
</footer>
`;

if (footerRegex.test(html)) {
  html = html.replace(footerRegex, newFooter);
  fs.writeFileSync('index.html', html, 'utf8');
  console.log("Footer replaced successfully with proper alignment.");
} else {
  console.log("Could not find footer tag.");
}
