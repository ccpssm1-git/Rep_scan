const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

const startMarker = '<section class="py-12 border-y border-border/40 bg-background/50 overflow-hidden relative">';
const endSearchStr = '</section>';

const startIdx = html.indexOf(startMarker);
if (startIdx !== -1) {
    const endIdx = html.indexOf(endSearchStr, startIdx);
    if (endIdx !== -1) {
        html = html.slice(0, startIdx) + html.slice(endIdx + endSearchStr.length);
        fs.writeFileSync('index.html', html, 'utf8');
        console.log("First duplicate ticker removed.");
    } else {
        console.log("Could not find end of first ticker.");
    }
} else {
    console.log("Could not find start marker for first ticker.");
}
