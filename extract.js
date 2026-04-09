const puppeteer = require('puppeteer');
const fs = require('fs');

async function extractContent() {
    console.log("Launching headless browser...");
    const browser = await puppeteer.launch({
        headless: "new"
    });

    try {
        const page = await browser.newPage();
        await page.goto('https://repsec-core.lovable.app/', { waitUntil: 'networkidle0' });

        const textContent = await page.evaluate(() => {
            return document.body.innerText;
        });

        fs.writeFileSync('content.txt', textContent, 'utf8');
        console.log("Successfully extracted exact text content to content.txt!");

    } catch(e) {
        console.error(e);
    } finally {
        await browser.close();
    }
}
extractContent();
