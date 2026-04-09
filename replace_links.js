const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

// Update social icons in footer-v2
const socialStripRegex = /<div class="footer-v2-social-strip">[\s\S]*?<\/div>/;
const newSocialStrip = `<div class="footer-v2-social-strip">
          <a href="https://www.linkedin.com/in/rg-admin-38aa823b1/" target="_blank" class="footer-v2-social-link" title="LinkedIn"><svg viewBox="0 0 24 24"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.761 0 5-2.239 5-5v-14c0-2.761-2.239-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg></a>
          <a href="https://www.youtube.com/@RepGuard" target="_blank" class="footer-v2-social-link" title="YouTube"><svg viewBox="0 0 24 24"><path d="M19.615 3.184c-3.604-.246-11.631-.245-15.23 0-3.897.266-4.356 2.62-4.385 8.816.029 6.185.484 8.549 4.385 8.816 3.6.245 11.626.246 15.23 0 3.897-.266 4.356-2.62 4.385-8.816-.029-6.185-.484-8.549-4.385-8.816zm-10.615 12.816v-8l8 3.993-8 4.007z"/></svg></a>
          <a href="https://x.com/RepGuard999" target="_blank" class="footer-v2-social-link" title="X (Twitter)"><svg viewBox="0 0 24 24"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg></a>
        </div>`;

html = html.replace(socialStripRegex, newSocialStrip);

// Update info email
// Find Contact Us link
html = html.replace(/>Contact Us<\/a>/g, 'href="mailto:info@repscan.ai">Contact Us</a>');
// To be safe, let's use a regex that matches `<a href="#" class="footer-v2-link">Contact Us</a>`
html = html.replace(/<a href="#" class="footer-v2-link">Contact Us<\/a>/g, '<a href="mailto:info@repscan.ai" class="footer-v2-link">Contact Us</a>');


fs.writeFileSync('index.html', html, 'utf8');
console.log("Updated social links and email.");
