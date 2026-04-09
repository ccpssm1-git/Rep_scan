const fs = require('fs');

try {
    let html = fs.readFileSync('index.html', 'utf-8');
    
    // We will animate the paragraph text "Your reputation is your identity. Don't leave it unprotected."
    const oldStr1 = "Your reputation is your identity. Don't leave it unprotected.";
    const oldStr2 = "Get a free confidential assessment of your digital risk exposure. No credit card required. Results in minutes.";
    
    // Adding GSAP classes and an inline animation class
    const newStr1 = "<span class=\"shimmer-text inline-block\" style=\"animation-duration: 4s;\">Your reputation is your identity. Don't leave it unprotected.</span>";
    const newStr2 = "<span class=\"inline-block hover:text-primary transition-colors duration-300\">Get a free confidential assessment of your digital risk exposure. No credit card required. Results in minutes.</span>";
    
    if(html.includes(oldStr1)) {
        html = html.replace(oldStr1, newStr1);
        console.log("✅ Replaced String 1");
    } else {
        console.log("❌ Could not find String 1. Trying fallback regex.");
        // Sometimes HTML entities or spaces differ
        html = html.replace(/Your reputation is your identity\.\s*Don't leave it unprotected\./i, newStr1);
    }

    if(html.includes(oldStr2)) {
        html = html.replace(oldStr2, newStr2);
        console.log("✅ Replaced String 2");
    } else {
        console.log("❌ Could not find String 2. Trying fallback regex.");
        html = html.replace(/Get a free confidential assessment of your digital risk exposure\.\s*No credit card required\.\s*Results in minutes\./i, newStr2);
    }
    
    // Also, we can add GSAP animation class to the whole CTA container
    // Let's find "Protect What Matters Most" and wrap it in a pulse-glow effect or add a CSS class to its container snippet
    const ctaHeaderMatch = /<h2[^>]*>\s*Protect What Matters Most\s*<\/h2>/i;
    if (ctaHeaderMatch.test(html)) {
        html = html.replace(ctaHeaderMatch, (match) => {
            // Replace class of h2 to add some animation
            if (match.includes('class="')) {
                return match.replace('class="', 'class="pulse-glow-3d ');
            }
            return match;
        });
        console.log("✅ Animated CTA Header");
    }

    fs.writeFileSync('index.html', html);
    console.log("Done updating CTA.");
} catch (e) {
    console.error(e);
}
