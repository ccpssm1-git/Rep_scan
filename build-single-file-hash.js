const https = require('https');
const fs = require('fs');

async function fetchAsset(url) {
    return new Promise((resolve, reject) => {
        https.get(url, (res) => {
            let data = '';
            res.on('data', chunk => data += chunk);
            res.on('end', () => resolve(data));
        }).on('error', reject);
    });
}

async function build() {
    try {
        console.log("Fetching root HTML...");
        let htmlContext = await fetchAsset('https://repsec-core.lovable.app/');

        // Find CSS asset
        const cssUrlMatch = htmlContext.match(/<link rel="stylesheet" crossorigin href="([^"]+)">/);
        if (cssUrlMatch) {
            console.log("Fetching CSS: " + cssUrlMatch[1]);
            const cssContent = await fetchAsset('https://repsec-core.lovable.app' + cssUrlMatch[1]);
            // Replace the <link> tag with raw inline <style>
            htmlContext = htmlContext.replace(
                `<link rel="stylesheet" crossorigin href="${cssUrlMatch[1]}">`,
                `<style>\n${cssContent}\n</style>`
            );
        }

        // Find JS asset
        const jsUrlMatch = htmlContext.match(/<script type="module" crossorigin src="([^"]+)"><\/script>/);
        if (jsUrlMatch) {
            console.log("Fetching JS: " + jsUrlMatch[1]);
            let jsContent = await fetchAsset('https://repsec-core.lovable.app' + jsUrlMatch[1]);
            
            // PATCH REACT ROUTER FOR LOCAL FILE:/// EXECUTION
            console.log("Patching React Router to HashRouter...");
            // React Router v6
            jsContent = jsContent.replace(/createBrowserRouter/g, "createHashRouter");
            jsContent = jsContent.replace(/BrowserRouter/g, "HashRouter");
            // React Router internal hooks
            // jsContent = jsContent.replace(/window\.location\.pathname/g, "('/')");

            // Execute the Arrow Function replace to prevent the $& injection bug!
            htmlContext = htmlContext.replace(
                `<script type="module" crossorigin src="${jsUrlMatch[1]}"></script>`,
                () => `<script type="module">\n${jsContent.replace(/<\/script>/g, '<\\/script>')}\n</script>`
            );
        }

        // Write output
        fs.writeFileSync('index.html', htmlContext);
        console.log("Successfully built perfectly patched self-contained index.html!");

    } catch (e) {
        console.error("Build failed:", e);
    }
}

build();
