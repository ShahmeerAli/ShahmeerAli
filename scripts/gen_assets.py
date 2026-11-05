"""Generate the SVG assets for the GitHub profile README."""
import os, sys, textwrap
from xml.sax.saxutils import escape

OUT = sys.argv[1]
os.makedirs(os.path.join(OUT, "assets", "cards"), exist_ok=True)

INK = "#07090C"
PANEL = "#0C1118"
EDGE = "#1B2430"
TEXT = "#E8EDF2"
MIST = "#8C99A7"
ICE = "#7DD3EA"
GOLD = "#D4A24C"
SANS = "'Segoe UI', 'Helvetica Neue', Helvetica, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace"


def write(name, svg):
    with open(os.path.join(OUT, "assets", name), "w", encoding="utf-8") as f:
        f.write(svg)


# ---------------------------------------------------------------- hero
hero = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 420" width="1280" height="420" role="img" aria-label="Shahmeer Ali. App developer, Islamabad.">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#0B1118"/><stop offset="1" stop-color="{INK}"/>
    </linearGradient>
    <linearGradient id="rock" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#16202A"/><stop offset="1" stop-color="#080B0F"/>
    </linearGradient>
    <linearGradient id="far" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#101820"/><stop offset="1" stop-color="#0A0E13"/>
    </linearGradient>
    <linearGradient id="fall" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="{ICE}" stop-opacity="0"/>
      <stop offset="0.35" stop-color="{ICE}" stop-opacity="0.9"/>
      <stop offset="1" stop-color="{ICE}" stop-opacity="0.15"/>
    </linearGradient>
    <radialGradient id="glow" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0" stop-color="{ICE}" stop-opacity="0.22"/>
      <stop offset="1" stop-color="{ICE}" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="fade" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0.7" stop-color="{INK}" stop-opacity="0"/><stop offset="1" stop-color="{INK}" stop-opacity="1"/>
    </linearGradient>
    <filter id="blur6" x="-300%" y="-20%" width="700%" height="140%"><feGaussianBlur stdDeviation="6"/></filter>
    <filter id="blur30" x="-50%" y="-300%" width="200%" height="700%"><feGaussianBlur stdDeviation="30"/></filter>
    <style>
      .pulse {{ animation: pulse 6s ease-in-out infinite; }}
      .drift {{ animation: drift 22s ease-in-out infinite alternate; }}
      .drift2 {{ animation: drift 30s ease-in-out infinite alternate-reverse; }}
      @keyframes pulse {{ 0%,100% {{ opacity: .55; }} 50% {{ opacity: 1; }} }}
      @keyframes drift {{ from {{ transform: translateX(-50px); }} to {{ transform: translateX(50px); }} }}
    </style>
  </defs>

  <rect width="1280" height="420" fill="url(#bg)"/>
  <ellipse cx="962" cy="250" rx="260" ry="210" fill="url(#glow)" class="pulse"/>

  <!-- far ridge -->
  <path d="M520 420 L640 330 L730 300 L820 250 L880 210 L930 230 L1000 190 L1080 170 L1160 200 L1280 160 L1280 420 Z" fill="url(#far)" opacity="0.8"/>

  <!-- the light falling through the gap -->
  <g class="pulse">
    <rect x="955" y="120" width="16" height="300" fill="url(#fall)" filter="url(#blur6)"/>
    <rect x="961.5" y="140" width="3" height="280" fill="url(#fall)"/>
  </g>

  <!-- near ridges forming the canyon -->
  <path d="M600 420 L720 300 L790 245 L860 150 L920 70 L944 120 L950 180 L957 420 Z" fill="url(#rock)"/>
  <path d="M600 420 L720 300 L790 245 L860 150 L920 70 L944 120" fill="none" stroke="#34475A" stroke-width="1.2" opacity="0.85"/>
  <path d="M1280 420 L1280 95 L1205 62 L1120 34 L1050 92 L992 150 L976 210 L969 420 Z" fill="url(#rock)"/>
  <path d="M1280 95 L1205 62 L1120 34 L1050 92 L992 150 L976 210" fill="none" stroke="#34475A" stroke-width="1.2" opacity="0.85"/>

  <!-- fog -->
  <g class="drift"><ellipse cx="900" cy="200" rx="260" ry="40" fill="#A9BCCB" opacity="0.07" filter="url(#blur30)"/></g>
  <g class="drift2"><ellipse cx="1080" cy="300" rx="300" ry="45" fill="#A9BCCB" opacity="0.06" filter="url(#blur30)"/></g>

  <rect width="1280" height="420" fill="url(#fade)"/>

  <!-- text -->
  <text x="84" y="150" font-family="{MONO}" font-size="14" letter-spacing="4" fill="{ICE}">APP DEVELOPER  ·  ISLAMABAD</text>
  <text x="80" y="228" font-family="{SANS}" font-size="56" font-weight="300" letter-spacing="8" fill="{TEXT}">SHAHMEER ALI</text>
  <text x="84" y="276" font-family="{SANS}" font-size="21" fill="{MIST}">I build quietly and let the work do the talking.</text>
  <rect x="84" y="318" width="56" height="1.5" fill="{GOLD}"/>
  <text x="156" y="324" font-family="{MONO}" font-size="13" letter-spacing="1.5" fill="#6F7C8A">flutter  ·  kotlin  ·  langgraph  ·  pixels pushed</text>
</svg>
"""
write("hero.svg", hero)

# ---------------------------------------------------------------- divider
divider = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 28" width="1280" height="28" aria-hidden="true">
  <defs>
    <linearGradient id="l" x1="0" x2="1">
      <stop offset="0" stop-color="#1E2A36" stop-opacity="0"/>
      <stop offset="0.5" stop-color="#2C3D4C"/>
      <stop offset="1" stop-color="#1E2A36" stop-opacity="0"/>
    </linearGradient>
    <filter id="b"><feGaussianBlur stdDeviation="3"/></filter>
  </defs>
  <rect x="0" y="13.5" width="1280" height="1" fill="url(#l)"/>
  <rect x="634" y="8" width="12" height="12" transform="rotate(45 640 14)" fill="{ICE}" opacity="0.5" filter="url(#b)"/>
  <rect x="636" y="10" width="8" height="8" transform="rotate(45 640 14)" fill="{INK}" stroke="{ICE}" stroke-width="1.2"/>
</svg>
"""
write("divider.svg", divider)

# ---------------------------------------------------------------- footer
footer = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 200" width="1280" height="200" role="img" aria-label="Less noise. More shipped.">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="{INK}" stop-opacity="0"/><stop offset="1" stop-color="{INK}"/>
    </linearGradient>
    <linearGradient id="rock" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#121A22"/><stop offset="1" stop-color="{INK}"/>
    </linearGradient>
    <radialGradient id="glow" cx="0.5" cy="1" r="0.6">
      <stop offset="0" stop-color="{ICE}" stop-opacity="0.16"/><stop offset="1" stop-color="{ICE}" stop-opacity="0"/>
    </radialGradient>
    <style>
      .pulse {{ animation: pulse 6s ease-in-out infinite; }}
      @keyframes pulse {{ 0%,100% {{ opacity: .6; }} 50% {{ opacity: 1; }} }}
    </style>
  </defs>
  <rect width="1280" height="200" fill="{INK}"/>
  <rect width="1280" height="200" fill="url(#glow)" class="pulse"/>
  <path d="M0 200 L0 150 L120 120 L230 140 L340 100 L450 130 L560 95 L640 120 L720 92 L830 128 L940 104 L1050 138 L1160 112 L1280 140 L1280 200 Z" fill="url(#rock)"/>
  <text x="640" y="60" text-anchor="middle" font-family="{MONO}" font-size="15" letter-spacing="5" fill="{ICE}">LESS NOISE. MORE SHIPPED.</text>
</svg>
"""
write("footer.svg", footer)

# ---------------------------------------------------------------- cards
STATUS = {
    "live": ("LIVE ON GOOGLE PLAY", GOLD),
    "oss": ("OPEN SOURCE", ICE),
    "wip": ("IN THE WORKSHOP", MIST),
    "game": ("GAME  ·  IN THE WORKSHOP", MIST),
    "app": ("APP  ·  IN THE WORKSHOP", MIST),
    "fyp": ("FINAL YEAR PROJECT  ·  TEAM OF 3", MIST),
}


def card(slug, status, title, desc, tags, arrow=True):
    label, color = STATUS[status]
    W, H = 560, 250
    lines = textwrap.wrap(desc, 56)
    assert len(lines) <= 3, (slug, lines)
    desc_svg = "\n".join(
        f'  <text x="32" y="{124 + i * 25}" font-family="{SANS}" font-size="16.5" fill="{MIST}">{escape(l)}</text>'
        for i, l in enumerate(lines)
    )
    # tag pills
    x, pills = 32, []
    for t in tags:
        w = len(t) * 7.3 + 22
        pills.append(
            f'  <rect x="{x:.1f}" y="204" width="{w:.1f}" height="24" rx="12" fill="#101922" stroke="#1E2C38"/>\n'
            f'  <text x="{x + w / 2:.1f}" y="220.5" text-anchor="middle" font-family="{MONO}" font-size="12" fill="{ICE}">{escape(t)}</text>'
        )
        x += w + 8
    assert x < W - 20, (slug, x)
    arrow_svg = (
        f'  <path d="M512 34 L526 34 L526 48 M526 34 L510 50" fill="none" stroke="{MIST}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>'
        if arrow else ""
    )
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="{escape(title)}: {escape(desc)}">
  <defs>
    <radialGradient id="g" cx="1" cy="0" r="0.9">
      <stop offset="0" stop-color="{color}" stop-opacity="0.13"/><stop offset="1" stop-color="{color}" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect x="0.75" y="0.75" width="{W - 1.5}" height="{H - 1.5}" rx="14" fill="{PANEL}" stroke="{EDGE}" stroke-width="1.5"/>
  <rect x="0.75" y="0.75" width="{W - 1.5}" height="{H - 1.5}" rx="14" fill="url(#g)"/>
  <circle cx="38" cy="41" r="4" fill="{color}"/>
  <text x="52" y="45.5" font-family="{MONO}" font-size="12" letter-spacing="2.5" fill="{color}">{label}</text>
{arrow_svg}
  <text x="32" y="88" font-family="{SANS}" font-size="27" font-weight="600" fill="{TEXT}">{escape(title)}</text>
{desc_svg}
{chr(10).join(pills)}
</svg>
"""
    with open(os.path.join(OUT, "assets", "cards", f"{slug}.svg"), "w", encoding="utf-8") as f:
        f.write(svg)


card("calorica", "live", "Calorica",
     "Calorie, water and mood tracker that sets personal daily goals and keeps the logging quick.",
     ["Android", "Pixels Pushed"])
card("pixelfit", "live", "PixelFit",
     "Compress photos to an exact KB size, resize for passport and visa forms, convert HEIC to JPG. Fully offline.",
     ["Android", "On-device", "Pixels Pushed"])
card("quizkai", "app", "QuizKai",
     "Real-time, head-to-head anime quiz battles. Server-side scoring, matchmaking in under 8 seconds, leaderboards.",
     ["Flutter", "Node.js", "Socket.IO", "Redis", "Supabase"], arrow=False)
card("quack-rapids", "game", "Quack Rapids",
     "A one-thumb river adventure for kids: rescue ducklings, solve gentle water puzzles, race rivals. Nothing ever gets hurt.",
     ["Godot", "Android", "Web"], arrow=False)
card("humsafar", "oss", "Humsafar",
     "Matrimonial app with face liveness checks, Stripe and PayFast payments, and an LLM that keeps chats respectful.",
     ["Flutter", "ML Kit", "FastAPI", "LangGraph"])
card("support-agent", "oss", "AI Support Ticket Agent",
     "Classifies tickets, answers from a knowledge base, scores its own confidence and hands the hard ones to a human.",
     ["LangGraph", "RAG", "ChromaDB", "FastAPI"])
card("decentralized-chatbot", "oss", "DeCentralized Chatbot",
     "Several agents debate and verify each answer, pull evidence through MCP servers, and ship it with citations.",
     ["LangGraph", "MCP", "Multi-agent"])
card("animation-turf", "oss", "Animation Turf",
     "An agent-select screen built for motion: Lottie splash, a fluid PageView slider and gradient themes that shift per character.",
     ["Flutter", "Lottie", "Animations"])

card("voiceledger", "app", "VoiceLedger",
     "Shopkeepers say a sale out loud and it becomes a ledger entry with one tap. Sales, expenses and who owes what, in many languages.",
     ["Flutter", "Riverpod", "Drift", "Speech-to-text"], arrow=False)

card("zarailink", "fyp", "ZaraiLink",
     "Farming app for growers in Pakistan: on-device crop disease detection, soil analysis, a marketplace, and voice commands in Urdu and Punjabi.",
     ["Flutter", "TFLite", "Whisper", "Supabase"], arrow=False)
card("medup", "app", "MedUp",
     "Head-to-head medical quiz battles. Live matchmaking, rankings and friends, wrapped in a clinical, ECG-inspired interface.",
     ["Flutter", "Riverpod", "Firebase", "Socket.IO"], arrow=False)

# ---- games in the workshop
card("zero-hour", "game", "Zero Hour",
     "A party deduction game for 4 to 10 phones. Everyone holds private clues, and the group has to crack the case before the clock hits zero.",
     ["TypeScript", "Preact", "Cloudflare", "Capacitor"], arrow=False)
card("gizmorun", "game", "GizmoRun",
     "Place ramps, springs, fans and seesaws, press Play, and let physics carry the ball home. 112 solver-checked levels across 14 worlds.",
     ["Godot", "GDScript", "Physics"], arrow=False)
card("mosaic-rush", "game", "Mosaic Rush",
     "Restore old mosaics by sending polish carriers around a conveyor. Procedural symmetric levels, every one verified solvable.",
     ["Godot", "Procedural", "Solver"], arrow=False)
card("bladespan", "game", "Bladespan",
     "A top-down sword arena where your blade is your health. Every win makes it longer, every hit chops it shorter.",
     ["Godot", "Arena", "Bots"], arrow=False)
card("sky-convoy", "game", "Sky Convoy",
     "Steer a convoy of cars across floating sky tracks, grow it through ×2 and +10 gates, and jump the gaps to the finish.",
     ["Godot", "Android", "Web"], arrow=False)
card("balloon-bounty", "game", "Balloon Bounty",
     "Pop the right balloons so their prizes bounce, roll and drop into the buckets. Delivery, not destruction.",
     ["Godot", "Physics", "Android"], arrow=False)
print("ok")
