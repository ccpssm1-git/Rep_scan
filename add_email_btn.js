const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

// Replace all instances of the "Get Protected" button
// It looks like: <button class="...">Get Protected</button>
html = html.replace(/(<button[^>]*>)\s*Get Protected\s*<\/button>/gi, (match, p1) => {
    // Check if it already has onclick
    if (p1.includes('onclick')) {
        return match;
    }
    // Add onclick handler
    return `${p1.replace(/>$/, ' onclick="window.location.href=\\\'mailto:info@repscan.ai\\\'">')}Get Protected</button>`;
});

fs.writeFileSync('index.html', html, 'utf8');
console.log('Added email link to Get Protected button.');
