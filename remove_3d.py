import re

# Read the file
with open(r'c:\Users\Rani\OneDrive\Desktop\R\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Remove the three.js script import
text = re.sub(r'<script src="https://cdnjs\.cloudflare\.com/ajax/libs/three\.js[^>]+></script>', '', text)

# Remove the canvas container
text = re.sub(r'<!-- 3D: reputation perimeter.*?<div id="canvas-container".*?</div>\s*</div>', '', text, flags=re.DOTALL)

# Remove the globe container
text = re.sub(r'<div class="w-full">\s*<div id="globe-container".*?</div>\s*</div>', '', text, flags=re.DOTALL)

# Remove Scene 1 and Scene 2 javascript
text = re.sub(r'// --- SCENE 1: Reputation perimeter.*?// --- SCENE 3: GSAP 3D Floating Timeline Cards ---', '// --- SCENE 3: GSAP 3D Floating Timeline Cards ---', text, flags=re.DOTALL)

# Write back the changes
with open(r'c:\Users\Rani\OneDrive\Desktop\R\index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Replacement successful")
