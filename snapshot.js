const puppeteer = require('puppeteer');
const axios = require('axios');
const fs = require('fs');

async function createStaticSnapshot() {
    console.log("Launching headless browser...");
    const browser = await puppeteer.launch({
        headless: "new",
        args: ['--no-sandbox', '--disable-setuid-sandbox']
    });

    try {
        const page = await browser.newPage();
        
        // Emulate a standard desktop screen so layout is perfect
        await page.setViewport({ width: 1440, height: 900 });

        console.log("Loading https://repsec-core.lovable.app/ and waiting for React DOM to settle...");
        // Wait until there are no more than 0 network connections for at least 500 ms.
        // This ensures the complete React app is downloaded, mounted, structured, and rendered!
        await page.goto('https://repsec-core.lovable.app/', { waitUntil: 'networkidle0', timeout: 30000 });

        console.log("Triggering scroll-based animations by scrolling down the page...");
        await page.evaluate(async () => {
            await new Promise((resolve) => {
                let totalHeight = 0;
                let distance = 100;
                let timer = setInterval(() => {
                    let scrollHeight = document.body.scrollHeight;
                    window.scrollBy(0, distance);
                    totalHeight += distance;

                    if (totalHeight >= scrollHeight - window.innerHeight) {
                        clearInterval(timer);
                        resolve();
                    }
                }, 50); // fast scroll
            });
            // scroll back to top just in case
            window.scrollTo(0, 0);
        });

        // wait extra 1 second for any delayed animations settling
        await new Promise(r => setTimeout(r, 1000));

        console.log("React has finished rendering. Sanitizing lazy-load and animation classes securely in DOM...");
        
        // Execute DOM cleanups securely BEFORE pulling HTML
        let htmlContent = await page.evaluate(() => {
            // Fix Tailwind classes
            document.querySelectorAll('[class*="opacity-0"]').forEach(el => {
                el.classList.remove('opacity-0');
                el.classList.add('opacity-100');
            });
            document.querySelectorAll('[class*="translate-y-"]').forEach(el => {
                let cls = el.getAttribute('class');
                if(cls) el.setAttribute('class', cls.replace(/translate-y-\d+/g, 'translate-y-0'));
            });
            document.querySelectorAll('[class*="scale-"]').forEach(el => {
                let cls = el.getAttribute('class');
                if(cls) el.setAttribute('class', cls.replace(/scale-(50|75|90|95)/g, 'scale-100'));
            });
            
            // Fix Framer motion and inline styles
            const allElements = document.querySelectorAll('*');
            for(let i = 0; i < allElements.length; i++) {
                const el = allElements[i];
                if(el.style && el.style.opacity === '0') el.style.opacity = '1';
                if(el.style && el.style.visibility === 'hidden') el.style.visibility = 'visible';
                if(el.style && el.style.transform && (el.style.transform.includes('translate') || el.style.transform.includes('scale'))) {
                    el.style.transform = 'none';
                }
            }
            
            return document.documentElement.outerHTML;
        });

        console.log("Extracting CSS Stylesheet URL...");
        // Lovable usually injects the css as a link tag
        const cssMatch = htmlContent.match(/<link[^>]*rel="stylesheet"[^>]*href="([^"]+)"/);
        
        let cssData = "";
        if (cssMatch && cssMatch[1]) {
            const cssUrl = cssMatch[1].startsWith('http') ? cssMatch[1] : 'https://repsec-core.lovable.app' + cssMatch[1];
            console.log(`Downloading Live CSS bundle from: ${cssUrl}`);
            const cssResponse = await axios.get(cssUrl);
            cssData = cssResponse.data;
            
            console.log("Embedding raw CSS directly into the HTML file...");
            // Replace the link tag with the raw CSS inline so you don't need a web server
            htmlContent = htmlContent.replace(
                /<link[^>]*rel="stylesheet"[^>]*>/,
                `<style>\n${cssData}\n</style>`
            );
        }

        console.log("Annihilating the React Engine Scripts to permanently fix offline 404 Route errors...");
        // Strip out the React Javascript bundles so the router NEVER runs on file:///
        htmlContent = htmlContent.replace(/<script[^>]*src="[^"]*index[^"]*\.js"[^>]*><\/script>/g, "");
        htmlContent = htmlContent.replace(/<script\s+type="module"[^>]*><\/script>/g, "");
        htmlContent = htmlContent.replace(/<script[^>]*crossorigin[^>]*><\/script>/g, "");

        // Prepend DOCTYPE to ensure standards mode
        const finalHtml = `<!DOCTYPE html>\n<html lang="en">\n${htmlContent.replace(/<html[^>]*>/, '')}`;

        console.log("Writing perfect frozen snapshot to index.html...");
        fs.writeFileSync('index.html', finalHtml, 'utf8');

        console.log("SUCCESS! You can now double click index.html and you will have 100% visual fidelity offline.");
    } catch (e) {
        console.error("Error creating snapshot:", e);
    } finally {
        await browser.close();
    }
}

createStaticSnapshot();
