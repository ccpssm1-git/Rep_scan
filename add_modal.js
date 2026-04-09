const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

// 1. Revert anchor tags and wire "Get Protected" to open the modal
html = html.replace(/<a href="mailto:info@repscan\.ai"[^>]*>\s*(<button[^>]*>\s*Get Protected\s*<\/button>)\s*<\/a>/gi, (match, button) => {
    return button.replace(/<button/, '<button onclick="event.preventDefault(); document.getElementById(\\\'contact-modal\\\').classList.remove(\\\'hidden\\\')"');
});
// Also catch if the button wasn't wrapped in the a tag but is standalone (just in case)
html = html.replace(/(<button[^>]*>)\s*Get Protected\s*<\/button>/gi, (match, p1) => {
    if (p1.includes('onclick')) return match;
    return `${p1.replace(/<button/, '<button onclick="event.preventDefault(); document.getElementById(\\\'contact-modal\\\').classList.remove(\\\'hidden\\\')"')}Get Protected</button>`;
});

// 2. Add Modal CSS & JS to head if not present
if (!html.includes('contact-modal')) {
    const modalHTML = `
    <!-- Contact Modal -->
    <div id="contact-modal" class="hidden fixed inset-0 z-[100] flex items-center justify-center bg-black/60 backdrop-blur-sm transition-all duration-300">
      <div class="bg-gray-900 border border-white/10 p-8 rounded-xl w-full max-w-md shadow-2xl relative text-white">
        <button onclick="document.getElementById('contact-modal').classList.add('hidden')" class="absolute top-4 right-4 text-gray-400 hover:text-white transition-colors">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
        </button>
        <h3 class="text-2xl font-bold mb-2">Get Protected</h3>
        <p class="text-gray-400 text-sm mb-6">Leave us a message and our defense team will contact you shortly.</p>
        
        <form action="https://formsubmit.co/info@repscan.ai" method="POST" class="flex flex-col gap-4">
          <!-- Honeypot -->
          <input type="text" name="_honey" style="display:none">
          <!-- Disable Captcha -->
          <input type="hidden" name="_captcha" value="false">
          <!-- Next Page (Redirect back) -->
          <input type="hidden" name="_next" value="https://repscan.ai/">

          <div>
            <label class="block text-sm font-medium mb-1 text-gray-300">Your Name</label>
            <input type="text" name="name" required class="w-full bg-gray-800 border border-white/10 rounded-lg px-4 py-2.5 outline-none focus:border-[#00D8FF] transition-colors" placeholder="John Doe">
          </div>
          <div>
            <label class="block text-sm font-medium mb-1 text-gray-300">Email Address</label>
            <input type="email" name="email" required class="w-full bg-gray-800 border border-white/10 rounded-lg px-4 py-2.5 outline-none focus:border-[#00D8FF] transition-colors" placeholder="john@company.com">
          </div>
          <div>
            <label class="block text-sm font-medium mb-1 text-gray-300">Your Message</label>
            <textarea name="message" required rows="4" class="w-full bg-gray-800 border border-white/10 rounded-lg px-4 py-2.5 outline-none focus:border-[#00D8FF] transition-colors resize-none" placeholder="Tell us how we can help..."></textarea>
          </div>
          <button type="submit" class="mt-2 w-full bg-[#00D8FF] hover:bg-[#00D8FF]/90 text-black font-semibold py-3 rounded-lg transition-colors">
            Send Message
          </button>
        </form>
      </div>
    </div>
    </body>`;
    
    // Inject before closing body
    html = html.replace(/<\/body>/i, modalHTML);
}

fs.writeFileSync('index.html', html, 'utf8');
console.log('Added beautiful modal form linked to FormSubmit.');
