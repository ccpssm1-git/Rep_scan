const fs = require('fs');

try {
    let html = fs.readFileSync('index.html', 'utf-8');
    
    // Pattern to match the shield generation code block
    const shieldCreationRegex = /\/\/\s*===\s*Enhanced 3D:\s*Rotating shield wireframe\s*===[\s\S]*?(?=\/\/\s*Subtle ambient movement)/;
    
    // Pattern to match the shield rotation code block inside the animate function
    const shieldRotationRegex = /\/\/\s*Rotate shield\s*if\s*\(\s*typeof\s*shieldGroup\s*!==\s*'undefined'\s*&&\s*shieldGroup\s*\)[\s\S]*?(?=\/\/\s*Setup Parallax for camera)/;
    
    // An alternative regex for rotation just to be safe, since typeof might not be what I wrote
    const shieldRotationRegex2 = /\/\/\s*Rotate shield[\s\S]*?(?=\/\/\s*Setup Parallax for camera)/;

    let initialLength = html.length;

    html = html.replace(shieldCreationRegex, '');
    html = html.replace(shieldRotationRegex2, '');

    if (html.length < initialLength) {
        fs.writeFileSync('index.html', html);
        console.log("✅ Successfully removed the 3D wireframe shield.");
    } else {
        console.log("❌ Could not find the 3D wireframe shield code to remove. Please verify if it was already removed.");
    }

} catch (e) {
    console.error(e);
}
