const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

// The original ticker had <section class="py-12 bg-background relative overflow-hidden" style="border-top: 1px solid rgba(255,255,255,0.05);">
html = html.replace(
  /<section class="py-12 bg-background relative overflow-hidden"/g,
  '<section class="py-12 bg-[#050B14] relative overflow-hidden"'
);

html = html.replace(/text-foreground tracking-wide opacity-90/g, 'text-white tracking-wide opacity-90');
html = html.replace(/bg-\[#030712\]/g, 'bg-[#000000]');

fs.writeFileSync('index.html', html, 'utf8');
console.log('Ticker Colors Fixed');
