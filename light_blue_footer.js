const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

// The footer currently has bg-[#030712] and text-white. We'll change it to bg-blue-50 with dark text.
html = html.replace(/bg-\[#030712\]/g, 'bg-blue-50 z-20');
html = html.replace(/<footer class="border-t border-white\/5 py-16 bg-blue-50 z-20 text-white/g, '<footer class="border-t border-blue-200 py-16 bg-blue-50 text-gray-900 z-20');

// Replace standard white headings
html = html.replace(/text-white/g, 'text-gray-900');

// Replace standard text-gray-400 links with darker ones
html = html.replace(/text-gray-400 hover:text-gray-900/g, 'text-gray-600 hover:text-blue-700'); 
// (We just changed text-white to text-gray-900, so hover:text-white became hover:text-gray-900)
html = html.replace(/text-gray-400/g, 'text-gray-600'); 

// The social icons had bg-white, let's remove the background or make them blend in
html = html.replace(/bg-white hover:bg-white\/90/g, 'hover:bg-blue-200/50 text-gray-800');

fs.writeFileSync('index.html', html, 'utf8');
console.log('Footer updated to light blue');
