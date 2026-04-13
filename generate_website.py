import json
import os

case_studies = [
  { "name": "KANYE WEST", "loss": "$1.5 Billion", "what": "One narrative shift", "time": "Within weeks", "lesson": "One public statement. One brand partnership gone. Billions erased.", "icon": "alert-triangle" },
  { "name": "FACEBOOK", "loss": "$100+ Billion", "what": "Data breach + trust collapse", "time": "Days to market impact", "lesson": "Data trust = brand value. Lose it, lose billions.", "icon": "shield-alert" },
  { "name": "BOEING", "loss": "$60+ Billion", "what": "Safety reputation destroyed", "time": "Accelerated after second crash", "lesson": "Reputation failure can shut down entire product lines.", "icon": "plane" },
  { "name": "VOLKSWAGEN", "loss": "€25-30 Billion", "what": "Environmental trust shattered", "time": "Within weeks of discovery", "lesson": "One hidden issue → global trust collapse → billions erased.", "icon": "car" },
  { "name": "MAGGI (India)", "loss": "₹450+ Crore", "what": "Food safety concerns", "time": "Ban lasted months", "lesson": "Local reputation issues go global instantly.", "icon": "utensils" },
  { "name": "JOHNNY DEPP", "loss": "Major Franchises", "what": "Allegations + online backlash", "time": "Career stalled for years", "lesson": "Allegations + online sentiment can freeze even global icons.", "icon": "film" },
  { "name": "KEVIN SPACEY", "loss": "$39M+", "what": "Reputation collapse", "time": "Immediate removal", "lesson": "Reputation collapse can mean total market exit.", "icon": "user-x" },
  { "name": "DAVID WARNER", "loss": "Captaincy", "what": "1-year cricket ban", "time": "Immediate suspension", "lesson": "Trust loss directly impacts leadership value.", "icon": "activity" },
  { "name": "WILL SMITH", "loss": "Tens of Millions", "what": "Oscars stage incident", "time": "Immediate", "lesson": "A single live moment can trigger long-term brand penalties.", "icon": "video" },
  { "name": "UBER", "loss": "Valuation", "what": "Leadership scandals", "time": "Weeks", "lesson": "Viral sentiment directly impacts user base and revenue.", "icon": "car-taxi-front" }
]

failures = [
  { "title": "LATE RESPONSE", "prob": "Traditional ORM tools detect threats 24-48 hours later. By then: Crisis is viral, news picked it up, AI summarized it, search poisoned.", "cost": "Every hour you wait costs millions." },
  { "title": "NO REAL-TIME DETECTION", "prob": "Manual monitoring = blind spots. They track yesterday's mentions, miss emerging threats, AI content goes undetected.", "cost": "You don't see the threat until it's unstoppable." },
  { "title": "NO ACTIVE DEFENSE", "prob": "They report damage. They don't prevent it. No automated playbooks, no threat mitigation, reactiveness looks like damage control.", "cost": "Reactive = defeated." }
]

comp_rows = [
  { "f": "Detection Speed", "a": "24-48 hours", "b": "6-12 hours", "c": "Real-time (seconds)", "h": True },
  { "f": "Response Type", "a": "Monthly reports", "b": "Alerts only", "c": "Active automated defense", "h": False },
  { "f": "AI Analysis", "a": "None", "b": "Basic sentiment", "c": "Predicts risk & financial impact", "h": False },
  { "f": "Real-Time Dashboard", "a": "No", "b": "Limited", "c": "Yes, full visibility", "h": False },
  { "f": "Automated Response", "a": "No", "b": "No", "c": "Yes, with approval", "h": False },
  { "f": "Threat Prediction", "a": "No", "b": "No", "c": "Yes, viral probability", "h": False },
  { "f": "Positioning", "a": "ORM tool", "b": "Monitoring SaaS", "c": "Security platform", "h": False }
]

use_cases = [
    {"title": "Enterprise & Brands", "chal": "Defend market position against competitor disinformation and review warfare.", "icon": "building-2"},
    {"title": "Public Figures", "chal": "Protect personal brand from targeted attacks, deepfakes, and media manipulation.", "icon": "clapperboard"},
    {"title": "Influencers", "chal": "Shield your community from trolling campaigns and narrative hijacking.", "icon": "megaphone"},
    {"title": "Executives & Founders", "chal": "Secure digital profiles for due diligence, fundraising, and board-level trust.", "icon": "briefcase"},
    {"title": "Personal Safety", "chal": "Combat online harassment, doxxing, and reputation-based intimidation campaigns.", "icon": "shield-check"}
]

html = """<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>RepGuard | Reputation Isn't PR. It's Crisis.</title>
    <meta name="description" content="RepGuard is the lead reputation defense platform. We detect, analyze, and neutralize viral threats before they damage your brand. Not just PR—Crisis.">
    <meta property="og:title" content="RepGuard | Reputation Defense Platform">
    <meta property="og:description" content="Secure your reputation with real-time threat detection and active defense.">
    <meta property="og:image" content="logo.png">
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/lucide@latest/dist/umd/lucide.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700;900&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-color: #ffffff;
            --text-color: #0f172a;
            --muted-color: #64748b;
            --border-color: #e2e8f0;
        }
        body { font-family: 'Inter', sans-serif; background: var(--bg-color); color: var(--text-color); overflow-x: hidden; }
        h1, h2, h3, h4, .font-heading { font-family: 'Space Grotesk', sans-serif; }
        
        .card-3d {
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            transform-style: preserve-3d;
        }
        .card-3d:hover {
            transform: translateY(-8px) scale(1.02);
            box-shadow: 0 20px 40px -10px rgba(37, 99, 235, 0.15), 0 0 20px rgba(37, 99, 235, 0.05);
            border-color: rgba(37, 99, 235, 0.3);
        }
        
        .floating-alert { animation: float-up 6s infinite ease-in-out; }
        @keyframes float-up {
            0%, 100% { transform: translateY(0) scale(1); }
            50% { transform: translateY(-15px) scale(1.02); }
        }
        
        .text-gradient {
            background: linear-gradient(135deg, #2563eb 0%, #3b82f6 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        
        .bg-grid {
            background-size: 40px 40px;
            background-image: linear-gradient(to right, rgba(0, 0, 0, 0.05) 1px, transparent 1px),
                              linear-gradient(to bottom, rgba(0, 0, 0, 0.05) 1px, transparent 1px);
            mask-image: radial-gradient(ellipse at center, black 40%, transparent 80%);
            -webkit-mask-image: radial-gradient(ellipse at center, black 40%, transparent 80%);
        }

        .glass-panel {
            background: rgba(239, 246, 255, 0.85); /* tailwind blue-50 */
            backdrop-filter: blur(16px);
            border: 1px solid rgba(219, 234, 254, 0.6); /* tailwind blue-100 */
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.05);
        }

        @keyframes scroll {
            0% { transform: translateX(0); }
            100% { transform: translateX(-50%); }
        }

        .hero-dashboard {
            transform: perspective(1000px) rotateX(15deg) rotateY(-5deg);
            transform-style: preserve-3d;
            box-shadow: 20px 40px 80px rgba(0,0,0,0.15);
        }

        .parallax-shape { position: absolute; border-radius: 50%; opacity: 0.15; filter: blur(40px); z-index: -1; }

        /* Dashboard Styles */
        .gauge-container { position: relative; width: 140px; height: 140px; }
        .gauge-svg { transform: rotate(-90deg); }
        .gauge-circle-bg { fill: none; stroke: #f1f5f9; stroke-width: 8; }
        .gauge-circle-fill { 
            fill: none; stroke: #3b82f6; stroke-width: 8; stroke-linecap: round;
            stroke-dasharray: 283; stroke-dashoffset: 283;
            transition: stroke-dashoffset 2s cubic-bezier(0.1, 0.5, 0.2, 1);
        }
        
        .progress-bar-container { width: 100%; height: 6px; background: #f1f5f9; border-radius: 99px; overflow: hidden; }
        .progress-bar-fill { height: 100%; background: #3b82f6; width: 0; transition: width 1.5s cubic-bezier(0.1, 0.5, 0.2, 1); }
        
        .findings-list { max-height: 200px; overflow-y: auto; }
        .finding-item { filter: blur(4px); opacity: 0.5; transition: all 0.5s ease; cursor: default; }
        .finding-item:hover { filter: blur(0); opacity: 1; }
    </style>
</head>
<body class="antialiased selection:bg-blue-200">
    <div class="fixed inset-0 z-[-2] bg-blue-50"></div>

    
    <div class="parallax-shape bg-blue-500 w-[500px] h-[500px] top-[-100px] left-[-100px]" data-speed="0.2"></div>
    <div class="parallax-shape bg-orange-400 w-[600px] h-[600px] bottom-[-200px] right-[-100px]" data-speed="0.3"></div>
    <div class="parallax-shape bg-green-400 w-[400px] h-[400px] top-[40%] left-[20%]" data-speed="-0.1"></div>

    <nav class="fixed top-0 w-full z-50 glass-panel border-b border-gray-100 transition-all duration-300">
        <div class="container mx-auto px-6 h-20 flex items-center justify-between relative">
            <div class="flex items-center gap-2 cursor-pointer" onclick="window.location.href='index.html'">
                <img src="logo.png" alt="RepGuard Logo" class="h-16 w-auto object-contain">
                <span class="text-2xl font-bold tracking-tight text-slate-900 ml-1">RepGuard</span>
            </div>
            
            <!-- Desktop Nav -->
            <div class="hidden md:flex items-center gap-8 text-sm font-medium text-slate-600 h-full">
                <!-- Mega Menu -->
                <div class="group h-full flex items-center">
                    <button class="flex items-center gap-1 hover:text-blue-600 transition-colors cursor-pointer font-semibold py-8 text-slate-700">
                        Services <i data-lucide="chevron-down" class="w-4 h-4 text-slate-400 group-hover:rotate-180 transition-transform duration-300"></i>
                    </button>
                    
                    <div class="absolute top-[80px] left-1/2 -translate-x-[35%] w-[900px] bg-white rounded-2xl shadow-2xl shadow-slate-200/60 border border-slate-100 p-8 opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-300 transform group-hover:translate-y-0 translate-y-3 z-[100] pointer-events-none group-hover:pointer-events-auto">
                        <div class="absolute -top-2 left-[35%] w-4 h-4 bg-white border-t border-l border-slate-100 transform rotate-45"></div>
                        
                        <div class="grid grid-cols-3 gap-8 relative z-10 bg-white">
                            <!-- Column 1 -->
                            <div>
                                <h4 class="text-xs font-bold text-slate-900 uppercase tracking-widest mb-1">REPAIR REPUTATION</h4>
                                <p class="text-[11px] text-slate-500 mb-6 leading-tight">Remove & suppress negative search results</p>
                                <ul class="space-y-6">
                                    <li>
                                        <a href="#services" class="flex items-start gap-4 group/item">
                                            <div class="bg-blue-50 text-blue-600 p-2.5 rounded-xl group-hover/item:bg-blue-600 group-hover/item:text-white transition-colors shrink-0"><i data-lucide="arrow-down-to-line" class="w-4 h-4"></i></div>
                                            <div>
                                                <div class="text-sm font-bold text-slate-900 group-hover/item:text-blue-600 transition-colors">Push Down Results</div>
                                                <div class="text-[11px] font-medium text-slate-500 mt-0.5 leading-snug">Suppress negatives</div>
                                            </div>
                                        </a>
                                    </li>
                                    <li>
                                        <a href="#services" class="flex items-start gap-4 group/item">
                                            <div class="bg-blue-50 text-blue-600 p-2.5 rounded-xl group-hover/item:bg-blue-600 group-hover/item:text-white transition-colors shrink-0"><i data-lucide="edit-3" class="w-4 h-4"></i></div>
                                            <div>
                                                <div class="text-sm font-bold text-slate-900 group-hover/item:text-blue-600 transition-colors">Correct Info Online</div>
                                                <div class="text-[11px] font-medium text-slate-500 mt-0.5 leading-snug">Set the record straight</div>
                                            </div>
                                        </a>
                                    </li>
                                    <li>
                                        <a href="#services" class="flex items-start gap-4 group/item">
                                            <div class="bg-blue-50 text-blue-600 p-2.5 rounded-xl group-hover/item:bg-blue-600 group-hover/item:text-white transition-colors shrink-0"><i data-lucide="star" class="w-4 h-4"></i></div>
                                            <div>
                                                <div class="text-sm font-bold text-slate-900 group-hover/item:text-blue-600 transition-colors">Improve Reviews</div>
                                                <div class="text-[11px] font-medium text-slate-500 mt-0.5 leading-snug">Ratings & reviews</div>
                                            </div>
                                        </a>
                                    </li>
                                    <li>
                                        <a href="#services" class="flex items-start gap-4 group/item">
                                            <div class="bg-blue-50 text-blue-600 p-2.5 rounded-xl group-hover/item:bg-blue-600 group-hover/item:text-white transition-colors shrink-0"><i data-lucide="shield" class="w-4 h-4"></i></div>
                                            <div>
                                                <div class="text-sm font-bold text-slate-900 group-hover/item:text-blue-600 transition-colors">Protect Reputation</div>
                                                <div class="text-[11px] font-medium text-slate-500 mt-0.5 leading-snug">Proactive defense</div>
                                            </div>
                                        </a>
                                    </li>
                                </ul>
                            </div>
                            
                            <!-- Column 2 -->
                            <div>
                                <h4 class="text-xs font-bold text-slate-900 uppercase tracking-widest mb-1">IMPROVE ONLINE BRAND</h4>
                                <p class="text-[11px] text-slate-500 mb-6 leading-tight">Improve how your brand is seen online</p>
                                <ul class="space-y-6">
                                    <li>
                                        <a href="#strategy" class="flex items-start gap-4 group/item">
                                            <div class="bg-blue-50 text-blue-600 p-2.5 rounded-xl group-hover/item:bg-blue-600 group-hover/item:text-white transition-colors shrink-0"><i data-lucide="crown" class="w-4 h-4"></i></div>
                                            <div>
                                                <div class="text-sm font-bold text-slate-900 group-hover/item:text-blue-600 transition-colors">Reputation Strategy</div>
                                                <div class="text-[11px] font-medium text-slate-500 mt-0.5 leading-snug">Full roadmap</div>
                                            </div>
                                        </a>
                                    </li>
                                    <li>
                                        <a href="#strategy" class="flex items-start gap-4 group/item">
                                            <div class="bg-blue-50 text-blue-600 p-2.5 rounded-xl group-hover/item:bg-blue-600 group-hover/item:text-white transition-colors shrink-0"><i data-lucide="chart-no-axes-combined" class="w-4 h-4"></i></div>
                                            <div>
                                                <div class="text-sm font-bold text-slate-900 group-hover/item:text-blue-600 transition-colors">Reputation Marketing</div>
                                                <div class="text-[11px] font-medium text-slate-500 mt-0.5 leading-snug">Amplify your brand</div>
                                            </div>
                                        </a>
                                    </li>
                                    <li>
                                        <a href="#strategy" class="flex items-start gap-4 group/item">
                                            <div class="bg-blue-50 text-blue-600 p-2.5 rounded-xl group-hover/item:bg-blue-600 group-hover/item:text-white transition-colors shrink-0"><i data-lucide="search-check" class="w-4 h-4"></i></div>
                                            <div>
                                                <div class="text-sm font-bold text-slate-900 group-hover/item:text-blue-600 transition-colors">Knowledge Panel</div>
                                                <div class="text-[11px] font-medium text-slate-500 mt-0.5 leading-snug">Correct and improve</div>
                                            </div>
                                        </a>
                                    </li>
                                    <li>
                                        <a href="#strategy" class="flex items-start gap-4 group/item">
                                            <div class="bg-blue-50 text-blue-600 p-2.5 rounded-xl group-hover/item:bg-blue-600 group-hover/item:text-white transition-colors shrink-0"><i data-lucide="bot" class="w-4 h-4"></i></div>
                                            <div>
                                                <div class="text-sm font-bold text-slate-900 group-hover/item:text-blue-600 transition-colors">AI Search (GEO)</div>
                                                <div class="text-[11px] font-medium text-slate-500 mt-0.5 leading-snug">Optimize for AI answers</div>
                                            </div>
                                        </a>
                                    </li>
                                </ul>
                            </div>
                            
                            <!-- Column 3 -->
                            <div class="border-l border-slate-100 pl-8">
                                <h4 class="text-xs font-bold text-slate-900 uppercase tracking-widest mb-1">WIKIPEDIA SERVICES</h4>
                                <p class="text-[11px] text-slate-500 mb-6 leading-tight">Create, edit, and monitor Wikipedia pages</p>
                                <ul class="space-y-6">
                                    <li>
                                        <a href="#wiki" class="flex items-start gap-4 group/item">
                                            <div class="bg-slate-100 text-slate-600 p-2.5 rounded-xl group-hover/item:bg-slate-800 group-hover/item:text-white transition-colors shrink-0 font-serif font-black text-sm w-9 h-9 flex items-center justify-center">W</div>
                                            <div>
                                                <div class="text-sm font-bold text-slate-900 group-hover/item:text-blue-600 transition-colors">Wikipedia Editing</div>
                                                <div class="text-[11px] font-medium text-slate-500 mt-0.5 leading-snug">Correct and improve</div>
                                            </div>
                                        </a>
                                    </li>
                                    <li>
                                        <a href="#wiki" class="flex items-start gap-4 group/item">
                                            <div class="bg-blue-50 text-blue-600 p-2.5 rounded-xl group-hover/item:bg-blue-600 group-hover/item:text-white transition-colors shrink-0"><i data-lucide="file-plus" class="w-4 h-4"></i></div>
                                            <div>
                                                <div class="text-sm font-bold text-slate-900 group-hover/item:text-blue-600 transition-colors">Create Wikipedia Page</div>
                                                <div class="text-[11px] font-medium text-slate-500 mt-0.5 leading-snug">New article creation</div>
                                            </div>
                                        </a>
                                    </li>
                                </ul>
                                
                                <div class="mt-10 pt-8 border-t border-slate-100">
                                    <a href="#services" class="text-blue-600 text-sm font-bold flex items-center gap-2 hover:text-blue-700 transition-colors w-max">View All Services <i data-lucide="arrow-right" class="w-4 h-4"></i></a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                
                <a href="#problem" class="hover:text-blue-600 transition-colors font-medium">The Risk</a>
                <a href="#solution" class="hover:text-blue-600 transition-colors font-medium">Platform</a>
                <button onclick="window.location.href='https://repscan-1kbq.vercel.app/reputation-os'" class="bg-blue-600 text-white px-6 py-2.5 rounded-full hover:bg-blue-700 transition-all shadow-lg hover:shadow-xl hover:-translate-y-0.5 font-semibold card-3d ml-4">Start Your Free Reputation Scan</button>
            </div>

            <!-- Mobile Menu Button -->
            <button class="md:hidden p-2 text-slate-600 hover:text-blue-600 transition-colors" id="mobile-menu-btn">
                <i data-lucide="menu" class="w-6 h-6"></i>
            </button>
        </div>

        <!-- Mobile Menu Overlay -->
        <div class="fixed inset-0 bg-white z-[60] hidden flex flex-col items-center justify-center space-y-8 text-2xl font-bold text-slate-900 transition-all duration-300 transform translate-x-full" id="mobile-menu-overlay">
            <button class="absolute top-6 right-6 p-4 text-slate-400 hover:text-slate-900" id="close-mobile-menu">
                <i data-lucide="x" class="w-8 h-8"></i>
            </button>
            <a href="#problem" class="hover:text-blue-600 transition-colors">The Risk</a>
            <a href="#solution" class="hover:text-blue-600 transition-colors">Platform</a>
            <a href="#services" class="hover:text-blue-600 transition-colors">Services</a>
            <button onclick="window.location.href='https://repscan-1kbq.vercel.app/reputation-os'" class="bg-blue-600 text-white px-10 py-4 rounded-full shadow-xl">Start Your Free Reputation Scan</button>
        </div>
    </nav>

    <!-- 1. HERO SECTION -->
    <section class="min-h-screen pt-32 pb-20 px-6 flex flex-col items-center justify-center relative overflow-hidden">
        <div class="container mx-auto text-center z-10 max-w-5xl">
            <div class="inline-flex items-center gap-2 px-4 py-2 rounded-full border border-blue-100 bg-blue-50 text-blue-600 text-xs font-bold uppercase tracking-widest mb-6 shadow-sm">
                <span class="w-2 h-2 rounded-full bg-blue-600 animate-pulse"></span>
                Reputation Isn't PR. It's Crisis.
            </div>
            <h1 class="font-heading text-5xl md:text-7xl font-bold tracking-tight text-slate-900 mb-6 leading-[1.1]">
                Your Reputation Is Under Attack.<br>
                <span class="text-gradient">We Defend It In Real Time</span>
            </h1>
            <p class="text-xl md:text-2xl text-slate-600 mb-10 max-w-3xl mx-auto leading-relaxed">
                One negative post. One viral moment. One AI summary—and everything changes. We don't wait for crises. We detect threats in real-time, analyze the risk, and neutralize them before they become your next billion-dollar problem.
            </p>
            <div class="flex flex-col sm:flex-row items-center justify-center gap-4 mb-4">
                <button onclick="window.location.href='https://repscan-1kbq.vercel.app/reputation-os'" class="w-full sm:w-auto px-8 py-4 bg-green-500 text-white rounded-lg font-bold text-lg hover:bg-green-600 transition-all shadow-lg hover:shadow-green-500/30 flex items-center justify-center gap-2 card-3d">
                    <i data-lucide="radar" class="w-5 h-5"></i> Start Your Free Reputation Scan
                </button>
                <button class="w-full sm:w-auto px-8 py-4 bg-white text-slate-900 border-2 border-slate-200 rounded-lg font-bold text-lg hover:border-slate-400 hover:bg-slate-50 transition-all flex items-center justify-center gap-2 card-3d">
                    <i data-lucide="play-circle" class="w-5 h-5"></i> See How It Works
                </button>
            </div>
            <p class="text-sm text-slate-500 mb-20 font-medium">No credit card required. See threats in 2 minutes.</p>

            <!-- Hero Visual: 3D Dashboard Mockup -->
            <div class="relative w-full max-w-5xl mx-auto mt-8">
                <div class="hero-dashboard bg-white border border-gray-200 rounded-2xl overflow-hidden p-2">
                    <div class="bg-slate-50 rounded-xl border border-gray-100 p-6 shadow-inner">
                        <div class="flex items-center justify-between mb-8 pb-4 border-b border-gray-200">
                            <div class="flex items-center gap-3">
                                <div class="w-3 h-3 rounded-full bg-red-400"></div><div class="w-3 h-3 rounded-full bg-orange-400"></div><div class="w-3 h-3 rounded-full bg-green-400"></div>
                            </div>
                            <span class="text-xs font-mono text-slate-400 font-bold tracking-widest text-center flex-grow">REPGUARD // ACTIVE DEFENSE DASHBOARD</span>
                        </div>
                        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 text-left">
                            <div class="bg-white p-5 rounded-xl border border-red-100 shadow-sm relative overflow-hidden group hover:border-red-300 transition-colors">
                                <div class="absolute top-0 right-0 w-16 h-16 bg-red-50 rounded-bl-full z-0 transition-transform group-hover:scale-110"></div>
                                <span class="text-xs font-bold text-red-500 relative z-10 block mb-2 uppercase tracking-widest">Critical Alert</span>
                                <div class="font-heading text-xl font-bold text-slate-900 relative z-10">Glassdoor Viral Spike</div>
                                <div class="text-xs font-medium text-slate-500 mt-3 relative z-10 flex items-center gap-2"><i data-lucide="clock" class="w-4 h-4 text-red-400"></i> T-Minus 4m to containment</div>
                            </div>
                            <div class="bg-white p-5 rounded-xl border border-orange-100 shadow-sm group hover:border-orange-300 transition-colors">
                                <span class="text-xs font-bold text-orange-500 block mb-2 uppercase tracking-widest">AI Intelligence</span>
                                <div class="font-heading text-xl font-bold text-slate-900">85% Viral Prob.</div>
                                <div class="text-xs font-medium text-slate-500 mt-3 flex items-center gap-2"><i data-lucide="trending-down" class="w-4 h-4 text-orange-400"></i> $2.4M Estimated Loss</div>
                            </div>
                            <div class="bg-gradient-to-br from-green-500 to-green-600 p-5 rounded-xl border border-green-600 shadow-md text-white card-3d cursor-default">
                                <span class="text-[10px] font-bold text-green-100 block mb-2 uppercase tracking-widest">Active Defense Protocol</span>
                                <div class="font-heading text-xl font-bold text-white mb-3">Neutralizing</div>
                                <div class="flex items-center justify-between text-xs font-bold bg-black/10 p-2 rounded-lg">
                                    <span>Deploying Playbook...</span>
                                    <span class="px-2 py-1 bg-white text-green-600 rounded">APPROVED</span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                
                <!-- Floating Alert Cards (Parallax Elements) -->
                <div class="absolute -right-8 md:-right-16 top-16 glass-panel p-4 rounded-xl shadow-xl flex items-center gap-3 floating-alert hidden md:flex" style="animation-delay: 0s;">
                    <div class="bg-red-100/50 p-2.5 rounded-full text-red-600"><i data-lucide="alert-triangle" class="w-5 h-5"></i></div>
                    <div class="text-left">
                        <div class="text-sm font-bold text-slate-900">Deepfake Detected</div>
                        <div class="text-xs font-semibold text-slate-500">TikTok • 12s ago</div>
                    </div>
                </div>
                 <div class="absolute -left-6 md:-left-12 bottom-12 glass-panel p-4 rounded-xl shadow-xl flex items-center gap-3 floating-alert hidden md:flex" style="animation-delay: 2s;">
                    <div class="bg-blue-100/50 p-2.5 rounded-full text-blue-600"><i data-lucide="check-square" class="w-5 h-5"></i></div>
                    <div class="text-left">
                        <div class="text-sm font-bold text-slate-900">Counter-Narrative Live</div>
                        <div class="text-xs font-semibold text-slate-500">Sentiment Shifting +42%</div>
                    </div>
                </div>
            </div>
        </div>
    </section>
"""

html += """
    <!-- 2. PROBLEM SECTION -->
    <section id="problem" class="py-24 bg-slate-50 border-y border-slate-200 relative overflow-hidden">
        <div class="container mx-auto px-6 z-10 relative">
            <div class="text-center mb-16 max-w-3xl mx-auto">
                <span class="inline-flex items-center gap-2 px-4 py-2 rounded-full border border-red-200 bg-red-50 text-red-600 text-xs font-bold uppercase tracking-widest mb-6">Reputation Risk = Financial Risk</span>
                <h2 class="font-heading text-4xl md:text-6xl font-bold text-slate-900 mb-6 tracking-tight">Global Giants Lost Billions.<br/><span class="text-slate-400">In Days.</span></h2>
                <p class="text-lg md:text-xl text-slate-600 leading-relaxed font-medium">Perception moves faster than truth. One incident. Minutes to viral. Billions in losses.</p>
            </div>
            
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-4 max-w-7xl mx-auto">
"""

for c in case_studies:
    html += f"""
                <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm hover:shadow-xl transition-all card-3d flex flex-col h-full group">
                    <div class="flex items-center justify-between mb-4 pb-4 border-b border-slate-100">
                        <h3 class="font-heading font-black tracking-tight text-lg text-slate-900 uppercase">{c['name']}</h3>
                        <div class="bg-red-50 text-red-600 p-2 rounded-xl group-hover:bg-red-600 group-hover:text-white transition-colors duration-300">
                            <i data-lucide="{c['icon']}" class="w-4 h-4"></i>
                        </div>
                    </div>
                    <div class="mb-4">
                        <div class="text-[10px] text-slate-400 uppercase tracking-[0.2em] font-bold mb-1">Financial Impact</div>
                        <div class="text-2xl font-black tracking-tighter text-red-500">{c['loss']}</div>
                    </div>
                    <div class="space-y-3 mb-6 flex-grow">
                        <div>
                            <div class="text-[10px] font-bold tracking-wider text-slate-400 uppercase mb-1 flex items-center gap-1"><i data-lucide="zap" class="w-3 h-3"></i> What Happened</div>
                            <div class="text-xs font-semibold text-slate-800 leading-snug">{c['what']}</div>
                        </div>
                    </div>
                    <div class="bg-slate-50 p-3 rounded-lg mt-auto border border-slate-100">
                        <div class="text-[10px] text-slate-600 italic font-medium">"{c['lesson']}"</div>
                    </div>
                </div>
"""

html += """
            </div>

            <div class="mt-20 text-center max-w-4xl mx-auto glass-panel p-10 md:p-14 rounded-[2rem] border border-blue-100 shadow-xl relative overflow-hidden card-3d">
                <div class="absolute inset-0 bg-gradient-to-br from-blue-50/80 to-transparent z-0"></div>
                <h3 class="font-heading text-3xl md:text-4xl font-bold text-slate-900 mb-6 relative z-10 tracking-tight leading-tight">If global giants can lose billions to unmanaged perception, what's protecting <span class="text-blue-600">YOUR</span> brand?</h3>
                <p class="text-lg md:text-xl text-slate-600 relative z-10 font-medium">These weren't accidents. They were predictable crises that could have been prevented. They all had the same three failures in common.</p>
            </div>
        </div>
    </section>
"""

html += """
    <!-- 3. THE GAP -->
    <section class="py-24 bg-white relative">
        <div class="container mx-auto px-6">
            <div class="text-center mb-20">
                <span class="inline-flex items-center gap-2 px-4 py-2 rounded-full border border-slate-200 bg-slate-50 font-bold uppercase tracking-widest text-[10px] text-slate-500 mb-6 shadow-sm"><i data-lucide="x" class="w-3 h-3 text-red-500"></i> The Three Deadly Failures</span>
                <h2 class="font-heading text-4xl md:text-5xl font-bold text-slate-900 mb-4 tracking-tight">Why Traditional ORM Fails</h2>
                <p class="text-xl text-slate-600 font-medium md:max-w-2xl mx-auto">(And Costs You Billions)</p>
            </div>
            
            <div class="grid md:grid-cols-3 gap-8 max-w-6xl mx-auto">
"""

for i, f in enumerate(failures):
    html += f"""
                <div class="card-3d bg-white border border-slate-200 rounded-[2rem] p-8 md:p-10 relative overflow-hidden shadow-lg hover:shadow-xl hover:border-red-200 group">
                    <div class="absolute top-0 left-0 w-full h-1.5 bg-red-500 opacity-0 group-hover:opacity-100 transition-opacity"></div>
                    <div class="w-14 h-14 bg-red-50 rounded-2xl flex items-center justify-center text-red-500 mb-8 font-black text-2xl border border-red-100 shadow-sm">{i+1}</div>
                    <h3 class="font-heading text-xl font-bold text-slate-900 mb-4 flex items-center gap-3">
                         {f['title']}
                    </h3>
                    <p class="text-slate-600 mb-8 text-sm md:text-base leading-relaxed font-medium">{f['prob']}</p>
                    <div class="mt-auto bg-red-50 p-4 rounded-xl border border-red-100 text-red-700 text-sm font-bold flex items-start gap-2">
                        <i data-lucide="alert-circle" class="w-5 h-5 shrink-0 mt-0.5"></i>
                        <span>The Cost: {f['cost']}</span>
                    </div>
                </div>
"""

html += """
            </div>
            
            <div class="mt-20 flex justify-center">
                <div class="bg-slate-900 text-white rounded-3xl p-1 shadow-2xl card-3d">
                    <div class="border border-white/10 rounded-[22px] px-8 py-6 flex flex-col md:flex-row items-center gap-8 justify-center">
                        <div class="text-center md:text-right">
                           <div class="font-bold text-slate-400 uppercase tracking-widest text-xs mb-1">Traditional ORM</div>
                           <div class="font-heading text-lg font-bold text-white">Monitoring is <span class="text-slate-500 line-through decoration-red-500">passive.</span></div>
                        </div>
                        <div class="hidden md:block w-px h-12 bg-white/20"></div>
                        <div class="text-center md:text-left">
                           <div class="font-bold text-blue-400 uppercase tracking-widest text-xs mb-1">RepGuard</div>
                           <div class="font-heading text-lg font-bold text-white">Defense is <span class="text-blue-400">active.</span></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 4. SOLUTION -->
    <section id="solution" class="py-24 bg-blue-50 border-y border-blue-100 relative overflow-hidden">
        <div class="absolute top-0 right-0 w-[800px] h-[800px] bg-blue-200 rounded-full mix-blend-multiply filter blur-3xl opacity-30 pointer-events-none transform translate-x-1/3 -translate-y-1/3"></div>
        <div class="absolute bottom-0 left-0 w-[600px] h-[600px] bg-sky-200 rounded-full mix-blend-multiply filter blur-3xl opacity-40 pointer-events-none transform -translate-x-1/3 translate-y-1/3"></div>
        
        <div class="container mx-auto px-6 relative z-10">
            <div class="text-center mb-20 max-w-4xl mx-auto">
                <span class="inline-flex items-center gap-2 px-4 py-2 rounded-full border border-blue-200 bg-white shadow-sm text-blue-600 text-[10px] font-bold uppercase tracking-[0.2em] mb-8">
                    <i data-lucide="shield-check" class="w-4 h-4"></i> Meet RepGuard
                </span>
                <h2 class="font-heading text-4xl md:text-6xl font-bold text-slate-900 mb-6 tracking-tight">Reputation Isn't PR. <br/><span class="text-blue-600">It's Digital Security.</span></h2>
                <p class="text-xl text-slate-600 max-w-3xl mx-auto leading-relaxed font-medium mb-8">
                    We don't manage reputation after crises. We prevent crises before they start. RepGuard is a <strong class="text-slate-900">Reputation Defense Platform</strong>. Real-time. Automated. Strategic.
                </p>
            </div>

            <div class="space-y-8 max-w-6xl mx-auto">
"""

pillars = [
  {"title": "REAL-TIME DETECTION", "sub": "Spot Threats in Seconds, Not Days", "icon": "zap", "points": ["Monitor 100+ data sources simultaneously", "AI flags threats within seconds", "Zero blind spots before viral spread"], "metric": "If a negative post takes 1 hour to go viral normally, we catch it in 60 seconds."},
  {"title": "INTELLIGENT ANALYSIS", "sub": "Understand Risk Before It Explodes", "icon": "brain", "points": ["AI predicts if it will go viral", "Estimates financial impact", "Identifies coordinated attacks"], "metric": "We accurately forecast the financial impact of sentiment collapse within a 90% confidence interval."},
  {"title": "ACTIVE DEFENSE", "sub": "Neutralize Threats, Don't Just Report", "icon": "shield-check", "points": ["Automated response playbooks", "Content removal coordination", "Deploy counter-narratives automatically"], "metric": "Automatically suppress false claims, deploy counter-narrative, and alert legal teams."}
]

for i, p in enumerate(pillars):
    pts_html = "".join([f'<li class="flex items-start gap-3"><div class="mt-1 w-5 h-5 rounded-full bg-green-100 flex items-center justify-center shrink-0"><i data-lucide="check" class="w-3 h-3 text-green-600"></i></div><span class="text-slate-700 font-medium">{pt}</span></li>' for pt in p['points']])
    html += f"""
                <div class="flex flex-col lg:flex-row items-center gap-10 bg-white p-8 md:p-12 rounded-[2.5rem] border border-slate-200 shadow-lg card-3d relative overflow-hidden group">
                    <div class="absolute top-0 right-0 w-64 h-64 bg-blue-50 rounded-bl-[100%] opacity-0 group-hover:opacity-100 transition-opacity duration-500 pointer-events-none"></div>
                    <div class="w-24 h-24 shrink-0 rounded-2xl bg-gradient-to-br from-blue-50 to-blue-100/50 border border-blue-100 flex items-center justify-center text-blue-600 shadow-inner relative z-10">
                        <i data-lucide="{p['icon']}" class="w-10 h-10"></i>
                    </div>
                    <div class="flex-grow relative z-10">
                        <div class="text-blue-600 text-[10px] font-black uppercase tracking-[0.2em] mb-3">PILLAR {i+1}</div>
                        <h3 class="font-heading text-2xl md:text-3xl font-bold text-slate-900 mb-3 tracking-tight">{p['title']}</h3>
                        <p class="text-slate-500 font-semibold mb-8 text-lg">"{p['sub']}"</p>
                        <div class="grid md:grid-cols-2 gap-4">
                            <ul class="space-y-4">
                                {pts_html}
                            </ul>
                        </div>
                    </div>
                    <div class="w-full lg:w-1/3 mt-6 lg:mt-0 relative z-10">
                        <div class="bg-slate-50 rounded-2xl p-6 md:p-8 border border-slate-100 shadow-sm hover:border-blue-200 transition-colors">
                            <i data-lucide="zap-fast" class="w-6 h-6 mb-4 text-blue-500"></i>
                            <div class="text-[10px] font-bold text-slate-400 tracking-[0.15em] uppercase mb-2">Real Impact</div>
                            <p class="text-sm font-semibold text-slate-800 leading-relaxed">{p['metric']}</p>
                        </div>
                    </div>
                </div>
"""

html += """
            </div>
            
            <div class="mt-20 text-center">
                <button class="px-10 py-5 bg-blue-600 text-white rounded-xl font-bold text-lg hover:bg-blue-700 transition-all shadow-xl hover:shadow-2xl hover:shadow-blue-500/30 card-3d inline-flex items-center gap-3">
                    <i data-lucide="shield-check" class="w-6 h-6"></i> Let's Treat Your Brand Like Digital Security
                </button>
            </div>
        </div>
    </section>

    <!-- 5. HOW IT WORKS -->
    <section class="py-24 bg-white relative overflow-hidden">
        <div class="container mx-auto px-6 max-w-7xl">
            <div class="text-center mb-24 lg:mb-32">
                <h2 class="font-heading text-4xl md:text-6xl font-bold text-slate-900 mb-6 tracking-tight">Three Steps to Reputation Security</h2>
                <p class="text-xl text-slate-600 font-medium">We don't just report damage. We prevent it.</p>
            </div>
            
            <div class="relative">
                <div class="absolute top-24 left-[10%] right-[10%] h-0.5 bg-gradient-to-r from-blue-100 via-slate-200 to-green-100 hidden lg:block z-0"></div>
                <div class="grid lg:grid-cols-3 gap-12 relative z-10">
                    <div class="relative bg-white pt-16 px-10 pb-12 rounded-[2.5rem] border border-slate-200 shadow-lg card-3d text-center hover:border-blue-300 transition-colors">
                        <div class="absolute -top-10 left-1/2 -translate-x-1/2 w-20 h-20 rounded-2xl bg-blue-50 border border-slate-100 shadow-md flex items-center justify-center font-heading font-black text-3xl text-blue-600 rotate-3 hover:rotate-0 transition-transform">1</div>
                        <h3 class="font-heading text-3xl font-black tracking-tight text-slate-900 mb-2">SCAN</h3>
                        <p class="text-[10px] font-bold text-slate-400 uppercase tracking-[0.2em] mb-6">24/7 Digital Monitoring</p>
                        <p class="text-slate-600 text-sm md:text-base font-medium leading-relaxed">Our AI crawls 100+ data sources simultaneously. Every mention is logged, analyzed, and scored in real-time.</p>
                    </div>
                    <div class="relative bg-white pt-16 px-10 pb-12 rounded-[2.5rem] border border-slate-200 shadow-lg card-3d text-center hover:border-orange-300 transition-colors">
                        <div class="absolute -top-10 left-1/2 -translate-x-1/2 w-20 h-20 rounded-2xl bg-orange-50 border border-slate-100 shadow-md flex items-center justify-center font-heading font-black text-3xl text-orange-600 rotate-3 hover:rotate-0 transition-transform">2</div>
                        <h3 class="font-heading text-3xl font-black tracking-tight text-slate-900 mb-2">ANALYZE</h3>
                        <p class="text-[10px] font-bold text-slate-400 uppercase tracking-[0.2em] mb-6">AI Risk Intelligence</p>
                        <p class="text-slate-600 text-sm md:text-base font-medium leading-relaxed">Identify source credibility, audience reach, viral probability, and estimated financial impact before it escalates.</p>
                    </div>
                    <div class="relative bg-white pt-16 px-10 pb-12 rounded-[2.5rem] border border-slate-200 shadow-lg card-3d text-center hover:border-green-300 transition-colors">
                        <div class="absolute -top-10 left-1/2 -translate-x-1/2 w-20 h-20 rounded-2xl bg-green-50 border border-slate-100 shadow-md flex items-center justify-center font-heading font-black text-3xl text-green-600 rotate-3 hover:rotate-0 transition-transform">3</div>
                        <h3 class="font-heading text-3xl font-black tracking-tight text-slate-900 mb-2">DEFEND</h3>
                        <p class="text-[10px] font-bold text-slate-400 uppercase tracking-[0.2em] mb-6">Active Response</p>
                        <p class="text-slate-600 text-sm md:text-base font-medium leading-relaxed">Approve or customize our AI-recommended response playbooks to suppress, counter, amplify, or escalate instantly.</p>
                    </div>
                </div>
            </div>
            <div class="mt-24 border border-slate-200 rounded-[2.5rem] bg-slate-50 p-3 shadow-xl relative overflow-hidden card-3d mx-auto max-w-5xl group">
                <div class="bg-white rounded-[2rem] border border-slate-100 shadow-inner overflow-hidden">
                    <div class="bg-slate-100/50 px-6 py-4 flex items-center justify-between border-b border-slate-100">
                        <div class="flex items-center gap-2">
                            <div class="w-3 h-3 rounded-full bg-slate-300 group-hover:bg-red-400 transition-colors"></div>
                            <div class="w-3 h-3 rounded-full bg-slate-300 group-hover:bg-orange-400 transition-colors"></div>
                            <div class="w-3 h-3 rounded-full bg-slate-300 group-hover:bg-green-400 transition-colors"></div>
                        </div>
                        <div class="text-xs font-mono text-slate-400 font-bold tracking-widest uppercase flex items-center gap-2">
                            <span class="w-1.5 h-1.5 rounded-full bg-green-500 animate-pulse inline-block"></span> RepGuard Active Defense Demo
                        </div>
                    </div>
                    
                    <div class="p-8 md:p-12">
                        <div class="flex flex-col space-y-6">
                            <div class="flex flex-col md:flex-row md:items-start gap-4">
                                <span class="text-xs font-mono text-slate-400 w-24 shrink-0 mt-1 md:text-right">2:00 PM</span>
                                <div class="bg-slate-50 border border-slate-200 rounded-2xl p-6 flex-grow shadow-sm">
                                    <div class="text-[10px] font-bold uppercase tracking-widest text-slate-500 mb-2"><i data-lucide="eye" class="w-3 h-3 inline"></i> STEP 1: SCAN</div>
                                    <p class="text-sm font-semibold text-slate-800">Controversial tweet posted by C-level executive on personal account.</p>
                                </div>
                            </div>
                            <div class="flex flex-col md:flex-row md:items-start gap-4 transform md:translate-x-4">
                                <span class="text-xs font-mono text-orange-400 w-24 shrink-0 mt-1 md:text-right">2:00:15 PM</span>
                                <div class="bg-orange-50 border border-orange-200 rounded-2xl p-6 flex-grow shadow-sm">
                                    <div class="text-[10px] font-bold uppercase tracking-widest text-orange-600 mb-2"><i data-lucide="brain" class="w-3 h-3 inline"></i> STEP 2: ANALYZE</div>
                                    <p class="text-sm font-bold text-orange-800 mb-2">Threat Flagged: CRITICAL. 90% Probability of going viral.</p>
                                    <p class="text-xs font-medium text-orange-700/80">Estimated Financial Impact: $50M+ if unaddressed for 12 hours.</p>
                                </div>
                            </div>
                            <div class="flex flex-col md:flex-row md:items-start gap-4 transform md:translate-x-8">
                                <span class="text-xs font-mono text-green-500 w-24 shrink-0 mt-1 md:text-right font-bold">2:01 PM</span>
                                <div class="bg-gradient-to-br from-green-50 to-emerald-50 border border-green-200 rounded-2xl p-6 flex-grow shadow-md">
                                    <div class="text-[10px] font-bold uppercase tracking-widest text-green-600 mb-2"><i data-lucide="shield-check" class="w-3 h-3 inline"></i> STEP 3: DEFEND</div>
                                    <div class="flex items-center justify-between flex-wrap gap-4">
                                        <p class="text-sm font-bold text-green-800">Executed Playbook: "Immediate Takedown & Apology Sync"</p>
                                        <span class="bg-green-500 text-white text-[10px] uppercase tracking-widest px-3 py-1 rounded-full font-bold shadow-sm">Crisis Averted</span>
                                    </div>
                                    <p class="text-xs font-medium text-green-700 mt-4 pt-4 border-t border-green-200/50">Next Day: Traditional ORM finally sends the alert report. By then, the event is already over.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 6. COMPARISON TABLE -->
    <section id="comparison" class="py-24 bg-slate-50 border-y border-slate-200">
        <div class="container mx-auto px-6 max-w-6xl">
            <div class="text-center mb-16">
                <h2 class="font-heading text-4xl md:text-6xl font-bold text-slate-900 mb-6 tracking-tight">RepGuard vs The Competition</h2>
                <p class="text-xl text-slate-600 font-medium">Why wait for a report when we can prevent the crisis?</p>
            </div>
            
            <div class="bg-white rounded-[2.5rem] border border-slate-200 shadow-xl overflow-hidden card-3d">
                <div class="overflow-x-auto">
                    <table class="w-full text-left border-collapse min-w-[800px]">
                        <thead>
                            <tr class="bg-slate-50/80 border-b border-slate-200">
                                <th class="py-8 px-6 text-[10px] font-black text-slate-400 uppercase tracking-[0.2em] w-1/4 border-r border-slate-100">Differentiator</th>
                                <th class="py-8 px-6 text-xs font-bold text-slate-600 uppercase tracking-widest w-1/4 text-center border-r border-slate-100">Traditional ORM</th>
                                <th class="py-8 px-6 text-xs font-bold text-slate-600 uppercase tracking-widest w-1/4 text-center border-r border-slate-100">Modern SaaS</th>
                                <th class="py-8 px-6 text-sm font-black text-blue-700 uppercase tracking-widest w-1/4 text-center bg-blue-50/50">RepGuard</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-slate-100">
"""

for r in comp_rows:
    html += f"""
                            <tr class="hover:bg-slate-50 transition-colors {'bg-blue-50/30 font-bold' if r['h'] else ''}">
                                <td class="py-6 px-6 text-sm font-bold {'text-slate-900' if r['h'] else 'text-slate-700'} border-r border-slate-100">{r['f']}</td>
                                <td class="py-6 px-6 text-sm text-center font-medium text-slate-500 border-r border-slate-100">{r['a']}</td>
                                <td class="py-6 px-6 text-sm text-center font-medium text-slate-500 border-r border-slate-100">{r['b']}</td>
                                <td class="py-6 px-6 text-sm text-center font-black text-blue-700 bg-blue-50/20">{r['c']}</td>
                            </tr>
"""

html += """
                        </tbody>
                    </table>
                </div>
                <div class="bg-slate-900 px-8 py-12 flex flex-col md:flex-row items-center justify-between gap-8">
                    <div class="text-left max-w-xl">
                        <div class="inline-flex items-center gap-2 px-3 py-1 rounded bg-blue-900/50 text-blue-300 text-[10px] font-bold uppercase tracking-widest mb-4 border border-blue-400/20">The Real Difference</div>
                        <h3 class="font-heading text-2xl md:text-3xl font-bold text-white mb-2 tracking-tight">You have a problem.</h3>
                        <p class="text-slate-400 font-medium leading-relaxed">Traditional ORM sends you a report in 48 hours. By then, it's a crisis.<br>With RepGuard: Detected in 0.5s. Analyzed in 2s. Neutralized before spread.</p>
                    </div>
                    <div class="flex flex-col sm:flex-row gap-4 shrink-0">
                        <button onclick="window.location.href='#analysis-tool'" class="px-8 py-4 bg-blue-600 border border-blue-500 text-white font-bold rounded-xl hover:bg-blue-500 transition-all shadow-lg hover:shadow-blue-500/50 card-3d">Try It Yourself</button>
                        <button onclick="openDemoModal(); return false;" class="px-8 py-4 bg-white/10 border border-white/20 text-white font-bold rounded-xl hover:bg-white/20 transition-all card-3d">Schedule Demo</button>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 7. USE CASES -->
    <section class="py-24 bg-white relative overflow-hidden">
        <div class="container mx-auto px-6 z-10 relative">
            <div class="text-center mb-20 max-w-4xl mx-auto">
                <span class="inline-flex items-center gap-2 px-4 py-2 rounded-full border border-slate-200 bg-slate-50 text-slate-500 text-[10px] font-bold uppercase tracking-widest mb-6">Who needs this?</span>
                <h2 class="font-heading text-4xl md:text-6xl font-bold text-slate-900 mb-6 tracking-tight">Who Needs Reputation Defense?</h2>
                <p class="text-xl text-slate-600 font-medium">The stakes change. The defense mechanism doesn't.</p>
            </div>
            
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-6 max-w-7xl mx-auto">
"""

for u in use_cases:
    html += f"""
                <div class="bg-slate-50 border border-slate-100 p-8 rounded-3xl hover:bg-white hover:shadow-2xl hover:shadow-blue-500/10 transition-all duration-500 group card-3d flex flex-col items-center text-center">
                    <div class="w-14 h-14 bg-white rounded-2xl flex items-center justify-center mb-6 shadow-sm border border-slate-100 group-hover:bg-blue-600 group-hover:text-white transition-colors">
                        <i data-lucide="{u['icon']}" class="w-6 h-6"></i>
                    </div>
                    <h3 class="text-lg font-bold text-slate-900 mb-4">{u['title']}</h3>
                    <p class="text-slate-500 text-xs leading-relaxed font-medium">{u['chal']}</p>
                </div>
"""

html += """
            </div>
        </div>
    </section>


    <!-- 9. FINAL CTA -->
    <section class="py-32 bg-white relative overflow-hidden text-center border-b border-slate-100">
        <div class="absolute inset-0 bg-gradient-to-b from-transparent to-blue-50/50 z-0"></div>
        <div class="container mx-auto px-6 max-w-4xl relative z-10">
            <div class="w-32 h-32 mx-auto mb-6 flex items-center justify-center">
                <img src="logo.png" alt="RepGuard Logo" class="w-full h-full object-contain">
            </div>
            <h2 class="font-heading text-5xl md:text-7xl font-bold text-slate-900 mb-8 tracking-tight">Don't Manage Reputation. <br><span class="text-blue-600">Secure It.</span></h2>
            <p class="text-xl md:text-2xl text-slate-600 mb-12 font-medium max-w-2xl mx-auto leading-relaxed">Billion-dollar reputations are lost between midnight and 9 AM. Stop reacting to crises. Start preventing them.</p>
            
            <div class="flex flex-col sm:flex-row justify-center items-center gap-4 mb-8">
                <button onclick="window.location.href='https://repscan-1kbq.vercel.app/reputation-os'" class="w-full sm:w-auto px-10 py-5 bg-green-500 text-white rounded-xl font-bold text-lg hover:bg-green-600 transition-all shadow-xl hover:shadow-green-500/30 card-3d flex justify-center items-center gap-2">
                    Start Your Free Reputation Scan
                </button>
                <button onclick="openDemoModal(); return false;" class="w-full sm:w-auto px-10 py-5 bg-white text-slate-900 border border-slate-200 shadow-sm rounded-xl font-bold text-lg hover:border-slate-400 hover:bg-slate-50 transition-all card-3d flex justify-center items-center gap-2">
                    Schedule Demo
                </button>
            </div>
            <p class="text-sm text-slate-500 font-bold uppercase tracking-widest"><i data-lucide="check" class="w-4 h-4 inline text-green-500"></i> No credit card. Cancel anytime. Full feature access.</p>
        </div>
    </section>

    <!-- 10. REPUTATION ANALYSIS TOOL SECTION -->
    <section id="analysis-tool" class="py-24 bg-slate-50 border-t border-slate-200">
        <div class="container mx-auto px-6 max-w-5xl">
            <div class="text-center mb-16">
                <h2 class="font-heading text-4xl font-bold text-slate-900 mb-4 tracking-tight">Free Online Reputation Score</h2>
                <p class="text-slate-600 font-medium max-w-2xl mx-auto">Get an instant, automated estimate of your search visibility and sentiment score. No account required.</p>
            </div>

            <div class="bg-white rounded-[2rem] shadow-2xl border border-slate-100 p-8 md:p-12 relative overflow-hidden" id="tool-container">
                <!-- Tool Entry State -->
                <div id="tool-entry" class="flex flex-col items-center py-10">
                    <div class="flex flex-col sm:flex-row items-center gap-4 w-full max-w-2xl">
                        <input type="text" id="tool-target-name" class="flex-grow w-full px-6 py-4 bg-slate-50 border border-slate-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-all font-medium" placeholder="Enter your name or brand...">
                        <button id="tool-analyze-btn" class="w-full sm:w-auto px-10 py-4 bg-blue-600 text-white rounded-xl font-bold hover:bg-blue-700 transition-all shadow-lg flex items-center justify-center gap-2 whitespace-nowrap min-w-max">
                            Run Scan
                        </button>
                    </div>
                </div>

                <!-- Tool Loading State (Hidden) -->
                <div id="tool-loading" class="hidden flex flex-col items-center py-10 text-center">
                    <div class="w-16 h-16 border-4 border-blue-600 border-t-transparent rounded-full animate-spin mb-6"></div>
                    <h3 class="font-heading text-2xl font-bold text-slate-900 mb-2">Analyzing Data...</h3>
                    <p class="text-slate-500 font-medium">Scanning 100+ public sources and news archives</p>
                </div>

                <!-- Tool Dashboard State (Hidden) -->
                <div id="tool-dashboard" class="hidden">
                    <div class="flex flex-col md:flex-row gap-12 items-center mb-10">
                        <div class="w-full md:w-1/3 flex flex-col items-center">
                             <div class="relative w-48 h-48">
                                <svg class="w-full h-full transform -rotate-90" viewBox="0 0 100 100">
                                    <circle class="fill-none stroke-slate-100 stroke-[8]" cx="50" cy="50" r="45"></circle>
                                    <circle class="fill-none stroke-blue-600 stroke-[8] stroke-linecap-round transition-all duration-[2000ms]" id="tool-score-gauge" cx="50" cy="50" r="45" style="stroke-dasharray: 283; stroke-dashoffset: 283;"></circle>
                                </svg>
                                <div class="absolute inset-0 flex flex-col items-center justify-center">
                                    <span class="text-6xl font-black text-slate-900 leading-none" id="tool-score-val">0</span>
                                    <span class="text-xs font-bold text-slate-400 uppercase tracking-widest mt-2">NEEDS ATTENTION</span>
                                </div>
                            </div>
                        </div>
                        <div class="w-full md:w-2/3 space-y-6" id="tool-metrics-container">
                            <!-- Populated by JS -->
                        </div>
                    </div>
                </div>

                <!-- Tool Detailed Findings State (Hidden) -->
                <div id="tool-findings" class="hidden border-t border-slate-100 pt-8 mb-8">
                    <h4 class="font-heading font-bold text-slate-900 mb-6 flex items-center gap-2">
                        <i data-lucide="search-code" class="w-5 h-5 text-blue-600"></i> Found Potential Risk Sources
                    </h4>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4" id="tool-findings-grid">
                        <!-- Populated by JS -->
                    </div>
                </div>

                <div id="tool-capture" class="hidden">
                    <div class="pt-8 border-t border-slate-100">
                        <div class="flex flex-col md:flex-row items-center justify-between gap-6">
                            <div class="flex items-center gap-3 bg-red-50 px-4 py-2 rounded-lg border border-red-100 text-red-600 text-sm font-bold">
                                <i data-lucide="alert-circle" class="w-5 h-5"></i> 15 negative results detected.
                            </div>
                            <div class="flex flex-col sm:flex-row items-center gap-4 w-full md:w-auto">
                                <input type="email" id="tool-unlock-email" class="w-full sm:w-auto px-4 py-2.5 bg-slate-50 border border-slate-200 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-blue-500" placeholder="your@email.com">
                                <button id="tool-unlock-btn" class="w-full sm:w-auto px-6 py-2.5 bg-blue-600 text-white rounded-lg font-bold text-sm hover:bg-blue-700 transition-all shadow-md">Unlock Detailed Findings</button>
                            </div>
                        </div>
                    </div>
                </div>
                </div>
                
                <!-- Success Messaging (Hidden) -->
                <div id="tool-success" class="hidden flex flex-col items-center py-10 text-center">
                    <div class="w-16 h-16 bg-green-100 text-green-600 rounded-full flex items-center justify-center mb-6">
                        <i data-lucide="check" class="w-8 h-8"></i>
                    </div>
                    <h3 class="font-heading text-2xl font-bold text-slate-900 mb-2">Report Unlocked</h3>
                    <p class="text-slate-500 font-medium">Check your inbox for the detailed breakdown.</p>
                </div>
            </div>
            
            <div class="mt-8 text-center text-[10px] font-medium text-slate-400 max-w-2xl mx-auto uppercase tracking-widest leading-relaxed">
                This score is an automated estimate based on publicly available search data. It is not a substitute for professional reputation analysis.
            </div>
        </div>
    </section>

    <!-- TRUSTED PARTNERS -->
    <section class="py-20 bg-slate-50 mb-[-1px] overflow-hidden relative border-t border-slate-200">
        <div class="absolute inset-y-0 left-0 w-48 bg-gradient-to-r from-slate-50 to-transparent z-10 pointer-events-none"></div>
        <div class="absolute inset-y-0 right-0 w-48 bg-gradient-to-l from-slate-50 to-transparent z-10 pointer-events-none"></div>
        
        <div class="text-center mb-16 relative z-20">
            <h2 class="font-heading text-3xl md:text-5xl font-semibold text-slate-800 mb-4 tracking-tight uppercase">JOIN OUR TRUSTED PARTNERS</h2>
            <p class="text-slate-600 font-medium text-lg md:text-xl">Protecting diverse individuals, professionals, and global innovators.</p>
        </div>

        <div class="flex w-max" style="animation: scroll 30s linear infinite;">
            <!-- Items -->
            <div class="flex gap-24 items-center px-12">
                <div class="text-center group cursor-default">
                    <div class="font-heading text-3xl font-medium text-slate-700 transition-colors group-hover:text-blue-600">BTP ICON</div>
                    <div class="text-[11px] font-bold text-slate-500 uppercase tracking-[0.2em] mt-3">SINGAPORE FINTECH</div>
                </div>
                <div class="text-center group cursor-default">
                    <div class="font-heading text-3xl font-medium text-slate-700 transition-colors group-hover:text-blue-600">FEEMONK</div>
                    <div class="text-[11px] font-bold text-slate-500 uppercase tracking-[0.2em] mt-3">EDUCATION FINTECH</div>
                </div>
                <div class="text-center group cursor-default">
                    <div class="font-heading text-3xl font-medium text-slate-700 transition-colors group-hover:text-blue-600">DOCTUTORIALS</div>
                    <div class="text-[11px] font-bold text-slate-500 uppercase tracking-[0.2em] mt-3">MEDICAL EDTECH</div>
                </div>
                <div class="text-center group cursor-default">
                    <div class="font-heading text-3xl font-medium text-slate-700 transition-colors group-hover:text-blue-600">ORBICULAR</div>
                    <div class="text-[11px] font-bold text-slate-500 uppercase tracking-[0.2em] mt-3">PHARMA GIANT</div>
                </div>
                <div class="text-center group cursor-default">
                    <div class="font-heading text-3xl font-medium text-slate-700 transition-colors group-hover:text-blue-600">RE-SUSTAINABILITY</div>
                    <div class="text-[11px] font-bold text-slate-500 uppercase tracking-[0.2em] mt-3">RAMKY GROUP</div>
                </div>
            </div>
            <!-- Duplicated Set -->
            <div class="flex gap-24 items-center px-12">
                <div class="text-center group cursor-default">
                    <div class="font-heading text-3xl font-medium text-slate-700 transition-colors group-hover:text-blue-600">BTP ICON</div>
                    <div class="text-[11px] font-bold text-slate-500 uppercase tracking-[0.2em] mt-3">SINGAPORE FINTECH</div>
                </div>
                <div class="text-center group cursor-default">
                    <div class="font-heading text-3xl font-medium text-slate-700 transition-colors group-hover:text-blue-600">FEEMONK</div>
                    <div class="text-[11px] font-bold text-slate-500 uppercase tracking-[0.2em] mt-3">EDUCATION FINTECH</div>
                </div>
                <div class="text-center group cursor-default">
                    <div class="font-heading text-3xl font-medium text-slate-700 transition-colors group-hover:text-blue-600">DOCTUTORIALS</div>
                    <div class="text-[11px] font-bold text-slate-500 uppercase tracking-[0.2em] mt-3">MEDICAL EDTECH</div>
                </div>
                <div class="text-center group cursor-default">
                    <div class="font-heading text-3xl font-medium text-slate-700 transition-colors group-hover:text-blue-600">ORBICULAR</div>
                    <div class="text-[11px] font-bold text-slate-500 uppercase tracking-[0.2em] mt-3">PHARMA GIANT</div>
                </div>
                <div class="text-center group cursor-default">
                    <div class="font-heading text-3xl font-medium text-slate-700 transition-colors group-hover:text-blue-600">RE-SUSTAINABILITY</div>
                    <div class="text-[11px] font-bold text-slate-500 uppercase tracking-[0.2em] mt-3">RAMKY GROUP</div>
                </div>
            </div>
        </div>
    </section>

    <!-- FOOTER -->
    <footer class="bg-white pt-20 pb-10 text-slate-600 relative z-10">
        <div class="container mx-auto px-6 grid md:grid-cols-12 gap-12 lg:gap-8 mb-16 max-w-7xl">
            <div class="md:col-span-5 lg:col-span-4">
                 <div class="flex items-center gap-2 mb-6 cursor-pointer group w-max" onclick="window.location.href='index.html'">
                    <img src="logo.png" alt="RepGuard Logo" class="h-12 w-auto object-contain group-hover:scale-105 transition-transform">
                    <span class="font-heading font-black text-xl tracking-tighter text-slate-900 group-hover:text-blue-600 transition-colors">REPGUARD</span>
                </div>
                <p class="text-sm mb-8 max-w-xs leading-relaxed font-medium">Reputation isn't PR. It's Crisis.<br>The internet doesn't wait. Neither should you.</p>
                <div class="flex gap-3">
                    <a href="https://x.com/RepGuard999" target="_blank" class="w-10 h-10 rounded-xl bg-slate-50 border border-slate-200 flex items-center justify-center hover:text-blue-600 hover:border-blue-600 hover:bg-blue-50 transition-colors shadow-sm"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16" class="w-4 h-4"><path d="M12.6.75h2.454l-5.36 6.142L16 15.25h-4.937l-3.867-5.07-4.425 5.07H.316l5.733-6.57L0 .75h5.063l3.495 4.633L12.601.75Zm-.86 13.028h1.36L4.323 2.145H2.865l8.875 11.633Z"/></svg></a>
                    <a href="https://www.linkedin.com/in/rg-admin-38aa823b1/" target="_blank" class="w-10 h-10 rounded-xl bg-slate-50 border border-slate-200 flex items-center justify-center hover:text-blue-600 hover:border-blue-600 hover:bg-blue-50 transition-colors shadow-sm"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 24 24" class="w-4 h-4"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg></a>
                    <a href="https://www.youtube.com/@RepGuard" target="_blank" class="w-10 h-10 rounded-xl bg-slate-50 border border-slate-200 flex items-center justify-center hover:text-blue-600 hover:border-blue-600 hover:bg-blue-50 transition-colors shadow-sm"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 24 24" class="w-4 h-4"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg></a>
                    <a href="#" target="_blank" class="w-10 h-10 rounded-xl bg-slate-50 border border-slate-200 flex items-center justify-center hover:text-blue-600 hover:border-blue-600 hover:bg-blue-50 transition-colors shadow-sm"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 24 24" class="w-4 h-4"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 100 12.324 6.162 6.162 0 000-12.324zM12 16a4 4 0 110-8 4 4 0 010 8zm6.406-11.845a1.44 1.44 0 100 2.881 1.44 1.44 0 000-2.881z"/></svg></a>
                </div>
            </div>
            <div class="md:col-span-7 lg:col-span-8 grid grid-cols-2 md:grid-cols-3 gap-8">
                <div>
                    <h4 class="font-bold text-slate-900 mb-6 uppercase tracking-[0.15em] text-[10px]">Product</h4>
                    <ul class="space-y-4 text-sm font-semibold text-slate-500">
                        <li><a href="#" class="hover:text-blue-600 transition-colors flex items-center gap-1 w-max"><i data-lucide="chevron-right" class="w-3 h-3 text-slate-300"></i> Platform Features</a></li>
                        <li><a href="#" class="hover:text-blue-600 transition-colors flex items-center gap-1 w-max"><i data-lucide="chevron-right" class="w-3 h-3 text-slate-300"></i> Pricing</a></li>
                        <li><a href="#" class="hover:text-blue-600 transition-colors flex items-center gap-1 w-max"><i data-lucide="chevron-right" class="w-3 h-3 text-slate-300"></i> API Integrations</a></li>
                        <li><a href="#" class="hover:text-blue-600 transition-colors flex items-center gap-1 w-max"><i data-lucide="chevron-right" class="w-3 h-3 text-slate-300"></i> Threat Glossary</a></li>
                    </ul>
                </div>
                <div>
                    <h4 class="font-bold text-slate-900 mb-6 uppercase tracking-[0.15em] text-[10px]">Company</h4>
                    <ul class="space-y-4 text-sm font-semibold text-slate-500">
                        <li><a href="#" class="hover:text-blue-600 transition-colors flex items-center gap-1 w-max"><i data-lucide="chevron-right" class="w-3 h-3 text-slate-300"></i> About RepGuard</a></li>
                        <li><a href="#" class="hover:text-blue-600 transition-colors flex items-center gap-1 w-max"><i data-lucide="chevron-right" class="w-3 h-3 text-slate-300"></i> Case Studies</a></li>
                        <li><a href="#" class="hover:text-blue-600 transition-colors flex items-center gap-1 w-max"><i data-lucide="chevron-right" class="w-3 h-3 text-slate-300"></i> Security</a></li>
                        <li><a href="#" class="hover:text-blue-600 transition-colors flex items-center gap-1 w-max"><i data-lucide="chevron-right" class="w-3 h-3 text-slate-300"></i> Trust Center</a></li>
                    </ul>
                </div>
                <div class="col-span-2 md:col-span-1">
                    <h4 class="font-bold text-slate-900 mb-6 uppercase tracking-[0.15em] text-[10px]">Contact & Support</h4>
                    <ul class="space-y-4 text-sm font-semibold text-slate-500">
                        <li><a href="mailto:info@repscan.ai" class="hover:text-blue-600 transition-colors text-blue-600 flex items-center gap-2 w-max bg-blue-50 px-3 py-1.5 rounded-lg border border-blue-100"><i data-lucide="mail" class="w-3 h-3"></i> info@repscan.ai</a></li>
                        <li><a href="#" onclick="openDemoModal(); return false;" class="hover:text-blue-600 transition-colors flex items-center gap-2 w-max border border-slate-200 px-3 py-1.5 rounded-lg shadow-sm"><i data-lucide="calendar" class="w-3 h-3"></i> Schedule Demo</a></li>
                        <li><a href="#" class="hover:text-blue-600 transition-colors flex items-center gap-2 w-max"><i data-lucide="headset" class="w-3 h-3"></i> 24/7 SOC Support</a></li>
                    </ul>
                </div>
            </div>
        </div>
        <div class="container mx-auto px-6 pt-8 border-t border-slate-100 flex flex-col md:flex-row justify-between items-center max-w-7xl">
            <div class="flex items-center gap-2 text-xs font-semibold text-slate-400 mb-4 md:mb-0">
                <span class="w-2 h-2 rounded-full bg-green-500 block"></span> Systems Operational
            </div>
            <p class="text-xs font-semibold text-slate-400 tracking-wide text-center md:text-left mb-4 md:mb-0">
                &copy; 2026 RepGuard. All rights reserved.
            </p>
            <div class="flex items-center gap-6 text-xs font-semibold text-slate-400">
                <a href="#" class="hover:text-slate-900 transition-colors">Terms of Service</a>
                <a href="#" class="hover:text-slate-900 transition-colors">Privacy Policy</a>
                <div class="flex items-center gap-4 ml-2 border-l border-slate-200 pl-4">
                    <a href="https://www.linkedin.com/in/rg-admin-38aa823b1/" target="_blank" class="hover:text-blue-600 transition-colors"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 24 24" class="w-4 h-4"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg></a>
                    <a href="https://www.youtube.com/@RepGuard" target="_blank" class="hover:text-red-500 transition-colors"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 24 24" class="w-4 h-4"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg></a>
                    <a href="#" target="_blank" class="hover:text-pink-600 transition-colors"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 24 24" class="w-4 h-4"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 100 12.324 6.162 6.162 0 000-12.324zM12 16a4 4 0 110-8 4 4 0 010 8zm6.406-11.845a1.44 1.44 0 100 2.881 1.44 1.44 0 000-2.881z"/></svg></a>
                    <a href="https://x.com/RepGuard999" target="_blank" class="hover:text-slate-900 transition-colors"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16" class="w-4 h-4"><path d="M12.6.75h2.454l-5.36 6.142L16 15.25h-4.937l-3.867-5.07-4.425 5.07H.316l5.733-6.57L0 .75h5.063l3.495 4.633L12.601.75Zm-.86 13.028h1.36L4.323 2.145H2.865l8.875 11.633Z"/></svg></a>
                </div>
                <a href="#" class="hover:text-slate-900 transition-colors">Cookie Policy</a>
            </div>
        </div>
    </footer>

    <!-- STICKY HEADER CTA -->
    <div class="fixed bottom-6 right-6 z-50 card-3d">
        <button class="open-scan-modal bg-blue-600 text-white rounded-full pl-5 pr-6 py-3.5 font-bold shadow-2xl border border-blue-500 flex items-center gap-3 hover:bg-blue-700 hover:scale-105 transition-all outline-none focus:ring-4 focus:ring-blue-500/30">
            <span class="relative flex h-3 w-3">
              <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-white opacity-75"></span>
              <span class="relative inline-flex rounded-full h-3 w-3 bg-white"></span>
            </span>
            Start Free Scan
        </button>
    </div>

    <!-- MODAL OVERLAY -->
    <div id="scan-modal" class="fixed inset-0 z-[100] hidden flex items-center justify-center">
        <div class="absolute inset-0 bg-slate-900/40 backdrop-blur-sm transition-opacity opacity-0" id="scan-modal-backdrop"></div>
        <div class="bg-white rounded-2xl w-full max-w-md mx-4 relative z-10 shadow-2xl border border-slate-200 transform scale-95 opacity-0 transition-all" id="scan-modal-content">
            <button id="close-modal" class="absolute top-4 right-4 text-slate-400 hover:text-slate-600 transition-colors">
                <i data-lucide="x" class="w-5 h-5"></i>
            </button>
            <div class="p-8" id="modal-body">
                <div class="w-12 h-12 bg-blue-50 text-blue-600 rounded-full flex items-center justify-center mb-6 border border-blue-100">
                    <i data-lucide="radar" class="w-6 h-6"></i>
                </div>
                <h3 class="font-heading text-2xl font-bold text-slate-900 mb-2">Initialize Reputation Scan</h3>
                <p class="text-slate-500 text-sm mb-6">Enter your details to generate a real-time threat map for your brand across 100+ sources.</p>
                
                <form class="space-y-4" id="initial-scan-form">
                    <div>
                        <label class="block text-xs font-bold text-slate-700 uppercase tracking-widest mb-1">Target Name</label>
                        <input type="text" id="target-name" class="w-full px-4 py-3 rounded-lg border border-slate-200 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-all" placeholder="E.g., John Doe or Acme Corp">
                    </div>
                    <div>
                        <label class="block text-xs font-bold text-slate-700 uppercase tracking-widest mb-1">Work Email</label>
                        <input type="email" id="target-email" class="w-full px-4 py-3 rounded-lg border border-slate-200 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-all" placeholder="john@company.com">
                    </div>
                    <button type="submit" class="w-full px-6 py-4 bg-blue-600 text-white rounded-xl font-bold hover:bg-blue-700 transition-all shadow-lg hover:shadow-blue-500/30 flex justify-center items-center gap-2 mt-6 whitespace-nowrap min-w-max">
                        <i data-lucide="zap" class="w-4 h-4"></i> Run Scan
                    </button>
                </form>
                <div class="mt-4 text-center">
                    <span class="text-[10px] text-slate-400 font-medium"><i data-lucide="lock" class="w-3 h-3 inline"></i> Secure 256-bit connection</span>
                </div>
            </div>
        </div>
    </div>

    <!-- Scripts -->
    <script>
        lucide.createIcons();
        
        // Modal Logic
        const modal = document.getElementById('scan-modal');
        const modalBackdrop = document.getElementById('scan-modal-backdrop');
        const modalContent = document.getElementById('scan-modal-content');
        const modalBody = document.getElementById('modal-body');
        const closeBtn = document.getElementById('close-modal');
        const openBtns = document.querySelectorAll('.open-scan-modal');

        function openModal() {
            modal.classList.remove('hidden');
            setTimeout(() => {
                modalBackdrop.classList.remove('opacity-0');
                modalBackdrop.classList.add('opacity-100');
                modalContent.classList.remove('scale-95', 'opacity-0');
                modalContent.classList.add('scale-100', 'opacity-100');
            }, 10);
        }

        function closeModal() {
            modalBackdrop.classList.remove('opacity-100');
            modalBackdrop.classList.add('opacity-0');
            modalContent.classList.remove('scale-100', 'opacity-100');
            modalContent.classList.add('scale-95', 'opacity-0');
            setTimeout(() => {
                modal.classList.add('hidden');
                // Reset modal to initial state if needed
            }, 300);
        }

        function renderLoading() {
            modalBody.innerHTML = `
                <div class="text-center py-10">
                    <div class="inline-flex items-center justify-center w-20 h-20 rounded-full bg-blue-50 text-blue-600 mb-8 animate-pulse border-2 border-blue-100">
                        <i data-lucide="cpu" class="w-10 h-10"></i>
                    </div>
                    <h4 class="font-heading font-bold text-slate-900 text-2xl mb-4">Analyzing Brand Footprint...</h4>
                    <p class="text-slate-500 text-sm font-medium mb-8">RepGuard AI is scanning dark web forums, social mentions, and global news archives.</p>
                    <div class="w-full bg-slate-100 rounded-full h-2 overflow-hidden mb-4">
                        <div class="bg-blue-600 h-full rounded-full transition-all duration-3000 ease-out" id="scan-bar" style="width: 0%"></div>
                    </div>
                    <div class="text-[10px] font-mono text-blue-600 font-bold tracking-widest">MAPPING THREAT VECTORS...</div>
                </div>
            `;
            lucide.createIcons();
            setTimeout(() => document.getElementById('scan-bar').style.width = '100%', 50);
            setTimeout(renderDashboard, 3200);
        }

        function renderDashboard() {
            const name = document.getElementById('target-name')?.value || 'Your Brand';
            modalContent.classList.remove('max-w-md');
            modalContent.classList.add('max-w-2xl');
            
            modalBody.innerHTML = `
                <div class="flex flex-col md:flex-row gap-10 items-start">
                    <div class="w-full md:w-1/2 flex flex-col items-center text-center">
                        <div class="gauge-container mb-6">
                            <svg class="gauge-svg w-full h-full" viewBox="0 0 100 100">
                                <circle class="gauge-circle-bg" cx="50" cy="50" r="45"></circle>
                                <circle class="gauge-circle-fill" id="score-gauge" cx="50" cy="50" r="45"></circle>
                            </svg>
                            <div class="absolute inset-0 flex flex-col items-center justify-center">
                                <span class="text-4xl font-black text-slate-900 leading-none" id="score-val">0</span>
                                <span class="text-[10px] font-bold text-slate-400 uppercase tracking-widest mt-1">Rep Score</span>
                            </div>
                        </div>
                        <div class="bg-orange-50 text-orange-600 px-4 py-1.5 rounded-full text-[10px] font-bold uppercase tracking-widest mb-6 border border-orange-100">
                            NEEDS ATTENTION
                        </div>
                        <div class="w-full space-y-5 text-left">
                            ${renderMetric('Search Visibility', 85, 'blue')}
                            ${renderMetric('Sentiment Score', 42, 'orange')}
                            ${renderMetric('Risk Level', 65, 'red')}
                        </div>
                    </div>
                    <div class="w-full md:w-1/2">
                        <h4 class="font-heading font-bold text-slate-900 text-lg mb-4 flex items-center gap-2">
                            <i data-lucide="list-checks" class="w-5 h-5 text-blue-600"></i> Detailed Findings
                        </h4>
                        <div class="space-y-3 findings-list mb-8">
                            ${renderFinding('Negative Glassdoor review gaining traction')}
                            ${renderFinding('Twitter thread regarding service delay (Viral Prob: 75%)')}
                            ${renderFinding('AI summary on Google Search includes outdated scandal')}
                            ${renderFinding('Deepfake candidate mentioning your brand on TikTok')}
                        </div>
                        <div class="bg-blue-600 rounded-2xl p-6 text-white shadow-xl">
                            <h5 class="font-bold mb-2">Unlock Full Analysis</h5>
                            <p class="text-xs text-blue-100 mb-4 font-medium leading-relaxed">We've identified 12 specific threat vectors. Get the complete 18-page PDF report with mitigation playbooks.</p>
                            <button id="unlock-btn" class="w-full bg-white text-blue-600 py-3 rounded-xl font-bold text-sm hover:bg-blue-50 transition-colors flex items-center justify-center gap-2">
                                <i data-lucide="lock-open" class="w-4 h-4"></i> Unlock Full Report
                            </button>
                        </div>
                    </div>
                </div>
            `;
            lucide.createIcons();
            
            // Animate dashboard
            setTimeout(() => {
                const score = 53;
                document.getElementById('score-gauge').style.strokeDashoffset = 283 - (283 * score / 100);
                animateNumber('score-val', score);
                document.querySelectorAll('.progress-bar-fill').forEach(bar => {
                    bar.style.width = bar.getAttribute('data-val') + '%';
                });
            }, 100);

            document.getElementById('unlock-btn').addEventListener('click', renderSuccess);
        }

        function renderMetric(label, val, color) {
            const colorClass = color === 'blue' ? 'bg-blue-600' : color === 'orange' ? 'bg-orange-500' : 'bg-red-500';
            return `
                <div>
                    <div class="flex justify-between text-[11px] font-bold text-slate-500 mb-1.5 uppercase tracking-widest">
                        <span>${label}</span>
                        <span>${val}%</span>
                    </div>
                    <div class="progress-bar-container">
                        <div class="progress-bar-fill ${colorClass}" data-val="${val}"></div>
                    </div>
                </div>
            `;
        }

        function renderFinding(text) {
            return `
                <div class="finding-item bg-slate-50 border border-slate-100 p-3 rounded-xl text-xs font-semibold text-slate-700">
                    <i data-lucide="alert-circle" class="w-3 h-3 inline mr-1 text-slate-400"></i> ${text}
                </div>
            `;
        }

        function renderSuccess() {
            modalContent.classList.remove('max-w-2xl');
            modalContent.classList.add('max-w-md');
            modalBody.innerHTML = `
                <div class="text-center py-10">
                    <div class="inline-flex items-center justify-center w-20 h-20 rounded-full bg-green-50 text-green-600 mb-8 border-2 border-green-100">
                        <i data-lucide="mail-check" class="w-10 h-10"></i>
                    </div>
                    <h4 class="font-heading font-bold text-slate-900 text-2xl mb-4">Report Dispatched</h4>
                    <p class="text-slate-500 text-sm font-medium mb-8">The full 18-page reputation breakdown and defense roadmap is being sent to your inbox right now.</p>
                    <button onclick="closeModal()" class="w-full bg-slate-900 text-white py-4 rounded-xl font-bold hover:bg-slate-800 transition-all shadow-lg">
                        Return to Site
                    </button>
                </div>
            `;
            lucide.createIcons();
        }

        function animateNumber(id, val) {
            let start = 0;
            const end = val;
            const duration = 2000;
            const obj = document.getElementById(id);
            const startTime = performance.now();
            
            function update(currentTime) {
                const elapsed = currentTime - startTime;
                const progress = Math.min(elapsed / duration, 1);
                const current = Math.floor(progress * end);
                obj.innerText = current;
                if (progress < 1) requestAnimationFrame(update);
            }
            requestAnimationFrame(update);
        }

        // Form Submit Handler
        document.addEventListener('submit', (e) => {
            if (e.target.id === 'initial-scan-form') {
                e.preventDefault();
                renderLoading();
            }
        });

        openBtns.forEach(btn => btn.addEventListener('click', openModal));
        if(closeBtn) closeBtn.addEventListener('click', closeModal);
        if(modalBackdrop) modalBackdrop.addEventListener('click', closeModal);

        
        document.addEventListener('DOMContentLoaded', () => {
            const parallaxShapes = document.querySelectorAll('.parallax-shape');
            window.addEventListener('mousemove', (e) => {
                const mouseX = (e.clientX - window.innerWidth / 2) / 100;
                const mouseY = (e.clientY - window.innerHeight / 2) / 100;
                
                parallaxShapes.forEach(shape => {
                    const speed = shape.getAttribute('data-speed');
                    const x = mouseX * speed * 10;
                    const y = mouseY * speed * 10;
                    shape.style.transform = `translate3d(${x}px, ${y}px, 0)`;
                });
            });

            gsap.registerPlugin(ScrollTrigger);

            const revealElements = document.querySelectorAll('h2, .card-3d, p:not(small p), .floating-alert');
            revealElements.forEach(el => {
                if(el.classList.contains('floating-alert')) return;
                gsap.from(el, {
                    scrollTrigger: {
                        trigger: el,
                        start: "top 90%",
                        toggleActions: "play none none reverse"
                    },
                    y: 40,
                    opacity: 0,
                    duration: 0.8,
                    ease: "power3.out"
                });
            });

            const nav = document.querySelector('nav');
            window.addEventListener('scroll', () => {
                if(window.scrollY > 50) {
                    nav.classList.add('bg-white/95', 'shadow-sm', 'border-slate-200');
                    nav.classList.remove('glass-panel');
                } else {
                    nav.classList.remove('bg-white/95', 'shadow-sm', 'border-slate-200');
                    nav.classList.add('glass-panel');
                }
            });
        });
        // --- STANDALONE TOOL LOGIC ---
        function renderToolMetric(label, val, color) {
            const colorClass = color === 'blue' ? 'bg-blue-600' : color === 'orange' ? 'bg-orange-500' : color === 'pink' ? 'bg-pink-500' : 'bg-cyan-500';
            return `
                <div>
                    <div class="flex justify-between text-[11px] font-bold text-slate-500 mb-1.5 uppercase tracking-widest">
                        <span>${label}</span>
                        <span>${val}%</span>
                    </div>
                    <div class="progress-bar-container">
                        <div class="progress-bar-fill ${colorClass}" data-val="${val}"></div>
                    </div>
                </div>
            `;
        }

        const toolAnalyzeBtn = document.getElementById('tool-analyze-btn');
        const toolEntry = document.getElementById('tool-entry');
        const toolLoading = document.getElementById('tool-loading');
        const toolDashboard = document.getElementById('tool-dashboard');
        const toolSuccess = document.getElementById('tool-success');

        if(toolAnalyzeBtn) {
            toolAnalyzeBtn.addEventListener('click', () => {
                toolEntry.classList.add('hidden');
                toolLoading.classList.remove('hidden');
                
                setTimeout(() => {
                    toolLoading.classList.add('hidden');
                    toolDashboard.classList.remove('hidden');
                    document.getElementById('tool-findings').classList.remove('hidden');
                    document.getElementById('tool-capture').classList.remove('hidden');
                    
                    const metricsContainer = document.getElementById('tool-metrics-container');
                    const findingsGrid = document.getElementById('tool-findings-grid');

                    if(metricsContainer) {
                        metricsContainer.innerHTML = `
                            ${renderToolMetric('Search Visibility', 85, 'blue')}
                            ${renderToolMetric('Sentiment Score', 42, 'orange')}
                            ${renderToolMetric('Review Rating', 60, 'pink')}
                            ${renderToolMetric('Content Control', 40, 'blue')}
                            ${renderToolMetric('Risk Level', 65, 'red')}
                        `;
                    }

                    if(findingsGrid) {
                        findingsGrid.innerHTML = `
                            ${renderFinding('Glassdoor Negative Sentiment Cluster')}
                            ${renderFinding('Twitter Thread regarding legacy policy')}
                            ${renderFinding('Outdated News Archive mapping to current name')}
                            ${renderFinding('Reddit Mention in high-volatility community')}
                        `;
                    }
                    
                    lucide.createIcons();
                    
                    // Animate score and bars
                    setTimeout(() => {
                        const score = 53;
                        document.getElementById('tool-score-gauge').style.strokeDashoffset = 283 - (283 * score / 100);
                        animateNumber('tool-score-val', score);
                        toolDashboard.querySelectorAll('.progress-bar-fill').forEach(bar => {
                            bar.style.width = bar.getAttribute('data-val') + '%';
                        });
                    }, 100);
                }, 2500);
            });
        }

        const toolUnlockBtn = document.getElementById('tool-unlock-btn');
        if(toolUnlockBtn) {
            toolUnlockBtn.addEventListener('click', () => {
                toolDashboard.classList.add('hidden');
                document.getElementById('tool-findings').classList.add('hidden');
                document.getElementById('tool-capture').classList.add('hidden');
                toolSuccess.classList.remove('hidden');
                lucide.createIcons();
            });
        }

        // --- END STANDALONE TOOL LOGIC ---

        // Mobile Menu Logic
        const mobileMenuBtn = document.getElementById('mobile-menu-btn');
        const mobileMenuOverlay = document.getElementById('mobile-menu-overlay');
        const closeMobileMenu = document.getElementById('close-mobile-menu');
        const mobileLinks = mobileMenuOverlay.querySelectorAll('a, button');

        function openMobileMenu() {
            mobileMenuOverlay.classList.remove('hidden');
            setTimeout(() => {
                mobileMenuOverlay.classList.remove('translate-x-full');
            }, 10);
        }

        function toggleMobileMenu() {
            mobileMenuOverlay.classList.add('translate-x-full');
            setTimeout(() => {
                mobileMenuOverlay.classList.add('hidden');
            }, 300);
        }

        mobileMenuBtn.addEventListener('click', openMobileMenu);
        closeMobileMenu.addEventListener('click', toggleMobileMenu);
        mobileLinks.forEach(link => link.addEventListener('click', toggleMobileMenu));
    </script>
    <!-- Demo Schedule Modal -->
    <div id="demo-modal-overlay" onclick="if(event.target===this) closeDemoModal()" class="fixed inset-0 z-[100] bg-slate-900/60 backdrop-blur-sm hidden opacity-0 transition-opacity duration-300 items-center justify-center p-4">
        <div class="bg-white rounded-3xl shadow-2xl max-w-md w-full p-8 relative transform scale-95 transition-transform duration-300">
            <button type="button" onclick="closeDemoModal()" class="absolute top-6 right-6 text-slate-500 hover:text-slate-900 transition-colors flex items-center gap-1.5 font-bold text-xs uppercase tracking-wider bg-slate-100 hover:bg-slate-200 px-3 py-2 rounded-full cursor-pointer z-50">
                <i data-lucide="x" class="w-3.5 h-3.5"></i> Close
            </button>
            <div class="w-12 h-12 bg-blue-50 text-blue-600 rounded-xl flex items-center justify-center mb-6">
                <i data-lucide="calendar" class="w-6 h-6"></i>
            </div>
            <h3 class="font-heading text-2xl font-bold text-slate-900 mb-2">Schedule Your Demo</h3>
            <p class="text-slate-500 font-medium mb-6 text-sm">Pick a date and time to see RepGuard in action. No commitment.</p>
            
            <form id="demo-form" class="space-y-4" onsubmit="event.preventDefault(); document.getElementById('demo-form').innerHTML='<div class=\\'text-center py-8\\'><div class=\\'w-16 h-16 bg-blue-100 text-blue-600 rounded-full flex items-center justify-center mx-auto mb-4\\'><i data-lucide=\\'check\\' class=\\'w-8 h-8\\'></i></div><h4 class=\\'text-xl font-bold text-slate-900 mb-2\\'>Demo Scheduled!</h4><p class=\\'text-slate-500 text-sm mb-6\\'>We\\'ll email you the calendar invite.</p><button type=\\'button\\' onclick=\\'closeDemoModal()\\' class=\\'w-full bg-slate-100 text-slate-700 font-bold py-3.5 rounded-xl hover:bg-slate-200 transition-colors\\'>Back to Website</button></div>'; setTimeout(()=>{lucide.createIcons();}, 100);">
                <div class="grid grid-cols-2 gap-4">
                    <div>
                        <label class="block text-[10px] font-bold text-slate-400 uppercase tracking-widest mb-1.5">Date</label>
                        <input type="date" required class="w-full px-4 py-2.5 bg-slate-50 border border-slate-200 rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none transition-all text-sm font-medium text-slate-800">
                    </div>
                    <div>
                        <label class="block text-[10px] font-bold text-slate-400 uppercase tracking-widest mb-1.5">Time</label>
                        <input type="time" required class="w-full px-4 py-2.5 bg-slate-50 border border-slate-200 rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none transition-all text-sm font-medium text-slate-800">
                    </div>
                </div>
                <div>
                    <label class="block text-[10px] font-bold text-slate-400 uppercase tracking-widest mb-1.5">Work Email</label>
                    <input type="email" placeholder="you@company.com" required class="w-full px-4 py-2.5 bg-slate-50 border border-slate-200 rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none transition-all text-sm font-medium text-slate-800">
                </div>
                <button type="submit" class="w-full mt-4 bg-blue-600 text-white font-bold py-3.5 rounded-xl hover:bg-blue-700 transition-all shadow-lg hover:shadow-blue-500/30 flex items-center justify-center gap-2">
                    Confirm Booking
                </button>
            </form>
        </div>
    </div>
    <script>
        function openDemoModal() {
            const modal = document.getElementById('demo-modal-overlay');
            modal.classList.remove('hidden', 'opacity-0');
            modal.classList.add('flex', 'opacity-100');
        }
        function closeDemoModal() {
            const modal = document.getElementById('demo-modal-overlay');
            modal.classList.add('hidden', 'opacity-0');
            modal.classList.remove('flex', 'opacity-100');
        }
    </script>
</body>
</html>
"""


variations = {
    'index.html': { 'headline': 'Your Reputation Is Under Attack.<br><span class="text-gradient">We Defend It In Real Time</span>', 'sub': 'One negative post. One viral moment. One AI summary—and everything changes. We don\'t wait for crises. We detect threats in real-time, analyze the risk, and neutralize them before they become your next billion-dollar problem.' },
    'fear-angle.html': { 'headline': 'You\'re 1 viral tweet away from a<br><span class="text-gradient"> loss.</span>', 'sub': 'Traditional PR waits for the newspaper. We don\'t. At RepGuard, we treat your reputation like a crisis threat. Our AI monitors the dark web, Reddit, and global media to detect, analyze, and neutralize viral threats before they reach your stakeholders.' },
    'logic-angle.html': { 'headline': 'Why use PR tools to fight a<br><span class="text-gradient">crisis war?</span>', 'sub': 'PR agencies send you a report 48 hours after you’ve already gone viral. The internet moves in seconds. Your defense should too. RepGuard detects threats within seconds and deploys automated counter-measures. Don\'t report on the crisis—prevent it.' },
    'public-figure.html': { 'headline': 'Cancel culture isn\'t a PR problem.<br><span class="text-gradient">It\'s an attack.</span>', 'sub': 'One coordinated online attack can erase a decade of career building. You need a shield that predicts and neutralizes threats before they trend. RepGuard protects the names that power billion-dollar industries.' },
}

for filename, var_data in variations.items():
    vhtml = html.replace('Your Reputation Is Under Attack.<br>\n                <span class="text-gradient">We Defend It In Real Time</span>', var_data['headline'])
    vhtml = vhtml.replace('One negative post. One viral moment. One AI summary—and everything changes. We don\'t wait for crises. We detect threats in real-time, analyze the risk, and neutralize them before they become your next billion-dollar problem.', var_data['sub'])
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(vhtml)
    print(f'Successfully generated {filename}')

