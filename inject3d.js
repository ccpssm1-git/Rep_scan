const fs = require('fs');

try {
    let html = fs.readFileSync('index.html', 'utf-8');

    // Make sure we haven't already injected it to avoid duplicates
    if (html.includes('id="cyber-bg"')) {
        console.log('Already injected, skipping.');
        process.exit(0);
    }

    const threeInjection = `
<!-- 3D Parallax Three.js Background -->
<canvas id="cyber-bg" style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; z-index: -1; pointer-events: none;"></canvas>
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r134/three.min.js"></script>
<script>
    document.addEventListener("DOMContentLoaded", () => {
        const canvas = document.getElementById('cyber-bg');
        if (!canvas) return;
        
        // Scene setup
        const scene = new THREE.Scene();
        // Light clean white background
        scene.background = new THREE.Color(0xffffff);

        const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
        camera.position.z = 150;

        const renderer = new THREE.WebGLRenderer({ canvas: canvas, antialias: true, alpha: true });
        renderer.setPixelRatio(window.devicePixelRatio);
        renderer.setSize(window.innerWidth, window.innerHeight);

        // Network connection lines
        const particlesCount = 300; // far fewer points for elegance
        const posArray = new Float32Array(particlesCount * 3);
        const velocities = [];

        for(let i = 0; i < particlesCount; i++) {
            posArray[i * 3] = (Math.random() - 0.5) * 400;
            posArray[i * 3 + 1] = (Math.random() - 0.5) * 400;
            posArray[i * 3 + 2] = (Math.random() - 0.5) * 200;
            velocities.push({
                x: (Math.random() - 0.5) * 0.2,
                y: (Math.random() - 0.5) * 0.2,
                z: (Math.random() - 0.5) * 0.2
            });
        }

        const geometry = new THREE.BufferGeometry();
        geometry.setAttribute('position', new THREE.BufferAttribute(posArray, 3));

        // Invisible dots but connected by lines
        const material = new THREE.PointsMaterial({ size: 0, transparent: true, opacity: 0 });
        const points = new THREE.Points(geometry, material);
        scene.add(points);

        // Lines container
        const lineMaterial = new THREE.LineBasicMaterial({
            color: 0x0284c7, // deeper blue
            transparent: true,
            opacity: 0.15
        });

        const linesMesh = new THREE.LineSegments(new THREE.BufferGeometry(), lineMaterial);
        scene.add(linesMesh);

        // Subtle ambient movement
        let mouseX = 0;
        let mouseY = 0;
        let windowHalfX = window.innerWidth / 2;
        let windowHalfY = window.innerHeight / 2;

        document.addEventListener('mousemove', (event) => {
            mouseX = (event.clientX - windowHalfX);
            mouseY = (event.clientY - windowHalfY);
        });

        // Animation Loop
        function animate() {
            requestAnimationFrame(animate);

            const positions = points.geometry.attributes.position.array;
            
            // Move points
            for(let i = 0; i < particlesCount; i++) {
                positions[i*3] += velocities[i].x;
                positions[i*3+1] += velocities[i].y;
                positions[i*3+2] += velocities[i].z;
                
                // Bounce off invisible walls
                if(positions[i*3] > 200 || Math.abs(positions[i*3]) > 200) velocities[i].x *= -1;
                if(positions[i*3+1] > 200 || Math.abs(positions[i*3+1]) > 200) velocities[i].y *= -1;
                if(positions[i*3+2] > 100 || Math.abs(positions[i*3+2]) > 100) velocities[i].z *= -1;
            }
            points.geometry.attributes.position.needsUpdate = true;

            // Update connections
            const linePositions = [];
            for ( let i = 0; i < particlesCount; i ++ ) {
                for ( let j = i + 1; j < particlesCount; j ++ ) {
                    const dx = positions[ i * 3 ] - positions[ j * 3 ];
                    const dy = positions[ i * 3 + 1 ] - positions[ j * 3 + 1 ];
                    const dz = positions[ i * 3 + 2 ] - positions[ j * 3 + 2 ];
                    const dist = Math.sqrt( dx * dx + dy * dy + dz * dz );

                    if ( dist < 45 ) {
                        linePositions.push(
                            positions[ i * 3 ], positions[ i * 3 + 1 ], positions[ i * 3 + 2 ],
                            positions[ j * 3 ], positions[ j * 3 + 1 ], positions[ j * 3 + 2 ]
                        );
                    }
                }
            }
            linesMesh.geometry.setAttribute('position', new THREE.Float32BufferAttribute(linePositions, 3));

            // Setup Parallax for camera
            camera.position.x += (mouseX * 0.05 - camera.position.x) * 0.05;
            camera.position.y += (-mouseY * 0.05 - camera.position.y) * 0.05;
            camera.lookAt(scene.position);

            renderer.render(scene, camera);
        }

        animate();

        window.addEventListener('resize', () => {
            windowHalfX = window.innerWidth / 2;
            windowHalfY = window.innerHeight / 2;
            camera.aspect = window.innerWidth / window.innerHeight;
            camera.updateProjectionMatrix();
            renderer.setSize(window.innerWidth, window.innerHeight);
        });
    });
</script>
</body>`;

    html = html.replace(/<\/body>(\s*)<\/html>/, threeInjection + '$1</html>');

    const cssOverride = `
<style>
  body, .bg-background { background-color: transparent !important; }
  .bg-card { background-color: rgba(255, 255, 255, 0.75) !important; backdrop-filter: blur(12px) !important; -webkit-backdrop-filter: blur(12px) !important; border-color: rgba(0, 0, 0, 0.05) !important;}
  /* DO NOT touch opacity of bg-grid-pattern, just ensure background is clear */
  .bg-grid-pattern { background-color: transparent !important; }
</style>
`;
    html = html.replace('</head>', cssOverride + '</head>');

    fs.writeFileSync('index.html', html);
    console.log('Successfully injected 3D parallax webgl! 🚀');
} catch (e) {
    console.error('Failed:', e);
}
