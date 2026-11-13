"""Generates the animated SVG artwork used by the profile README.

Run:  python scripts/build_assets.py
Every SVG adapts to light/dark mode and stops animating for reduced-motion users.
"""
import math
import random
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "assets"
OUT.mkdir(exist_ok=True)

SERIF = "Georgia, 'Iowan Old Style', 'Times New Roman', serif"
MONO = "ui-monospace, 'SF Mono', 'JetBrains Mono', Menlo, Consolas, monospace"
SANS = "-apple-system, 'Segoe UI', Helvetica, Arial, sans-serif"

BASE_CSS = f"""
  svg {{ --bg:#efe9dd; --fg:#15130f; --mu:#655f54; --ln:rgba(21,19,15,.17); --card:rgba(21,19,15,.035); }}
  @media (prefers-color-scheme: dark) {{
    svg {{ --bg:#100f0d; --fg:#efe9dd; --mu:#a39d90; --ln:rgba(239,233,221,.18); --card:rgba(239,233,221,.045); }}
  }}
  .bg {{ fill:var(--bg); }} .fg {{ fill:var(--fg); }} .mu {{ fill:var(--mu); }}
  .ln {{ stroke:var(--ln); fill:none; }} .sfg {{ stroke:var(--fg); fill:none; }}
  .card {{ fill:var(--card); stroke:var(--ln); }}
  .serif {{ font-family:{SERIF}; }} .it {{ font-style:italic; }}
  .mono {{ font-family:{MONO}; letter-spacing:.14em; }}
  .sans {{ font-family:{SANS}; }}
  .dash {{ stroke-dasharray:4 7; animation:dash 1.6s linear infinite; }}
  .pulse {{ transform-box:fill-box; transform-origin:center; animation:pulse 3.2s ease-in-out infinite; }}
  .rise {{ animation:rise 1.1s cubic-bezier(.2,.7,.1,1) both; }}
  .fade {{ animation:fade 1.4s ease both; }}
  @keyframes dash {{ to {{ stroke-dashoffset:-22; }} }}
  @keyframes pulse {{ 50% {{ transform:scale(1.2); }} }}
  @keyframes rise {{ from {{ transform:translateY(46px); opacity:0; }} }}
  @keyframes fade {{ from {{ opacity:0; }} }}
  @media (prefers-reduced-motion: reduce) {{ * {{ animation:none !important; }} }}
"""

RAMP = """
    <linearGradient id="ramp" x1="0" x2="1" y1="0" y2="0">
      <stop offset="0" stop-color="#6d4bff"/><stop offset=".36" stop-color="#d23bb0"/>
      <stop offset=".68" stop-color="#fa5433"/><stop offset="1" stop-color="#ffb321"/>
    </linearGradient>"""


def heat(id_, cx, cy, r, path=None, dur=16):
    """A thermal radial gradient in user space. If `path` is given, its centre drifts."""
    anim = ""
    if path:
        xs = ";".join(str(p[0]) for p in path)
        ys = ";".join(str(p[1]) for p in path)
        spl = ";".join([".4 0 .6 1"] * (len(path) - 1))
        anim = (
            f'<animate attributeName="cx" values="{xs}" dur="{dur}s" repeatCount="indefinite" calcMode="spline" keySplines="{spl}"/>'
            f'<animate attributeName="cy" values="{ys}" dur="{dur}s" repeatCount="indefinite" calcMode="spline" keySplines="{spl}"/>'
        )
    return f"""
    <radialGradient id="{id_}" gradientUnits="userSpaceOnUse" cx="{cx}" cy="{cy}" r="{r}">
      <stop offset="0" stop-color="#ffbd2e"/><stop offset=".3" stop-color="#fa5433"/>
      <stop offset=".58" stop-color="#c22fa6"/><stop offset=".84" stop-color="#5b3fe0" stop-opacity=".75"/>
      <stop offset="1" stop-color="#5b3fe0" stop-opacity="0"/>{anim}
    </radialGradient>"""


def svg(w, h, label, defs, body, radius=20):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="{label}">
  <style>{BASE_CSS}</style>
  <defs>{RAMP}{defs}
    <clipPath id="frame"><rect width="{w}" height="{h}" rx="{radius}"/></clipPath>
  </defs>
  <g clip-path="url(#frame)">
    <rect class="bg" width="{w}" height="{h}"/>
{body}
  </g>
  <rect class="ln" x=".5" y=".5" width="{w - 1}" height="{h - 1}" rx="{radius}"/>
</svg>
"""


def field(rng, w, top, bottom, rows=24, x0=-20, density=1.0):
    """A perspective plane of points: sparse and tiny far away, large and loose up close."""
    out = []
    for r in range(rows):
        t = r / (rows - 1)
        y = top + (t ** 1.7) * (bottom - top)
        gap = (9 + t * 25) / density
        size = 0.7 + t * 2.3
        x = x0 + rng.random() * gap
        row = []
        while x < w + 20:
            jx = x + (rng.random() - 0.5) * gap * 0.7
            jy = y + (rng.random() - 0.5) * gap * 0.5
            row.append(f'<circle cx="{jx:.0f}" cy="{jy:.0f}" r="{size * (0.7 + rng.random() * 0.6):.1f}"/>')
            x += gap
        out.append(f'<g opacity="{0.25 + t * 0.6:.2f}">{"".join(row)}</g>')
    return "\n".join(out)


# ---------------------------------------------------------------- hero
def hero():
    rng = random.Random(11)
    w, h = 1200, 470
    dots = field(rng, w, 150, 480, rows=25)
    defs = heat("heat", 880, 250, 250, path=[(880, 250), (1020, 320), (700, 300), (940, 210), (880, 250)], dur=18) + """
    <linearGradient id="sideg" x1="0" x2="1" y1="0" y2="0">
      <stop offset=".3" stop-color="#fff" stop-opacity=".16"/><stop offset=".62" stop-color="#fff"/>
    </linearGradient>
    <mask id="side"><rect width="1200" height="470" fill="url(#sideg)"/></mask>"""
    body = f"""
    <g mask="url(#side)">
      <g id="dots" class="fade">{dots}</g>
      <use xlink:href="#dots" href="#dots" fill="url(#heat)" stroke="url(#heat)" stroke-width="3.2"/>
    </g>
    <rect width="{w}" height="{h}" fill="url(#heat)" opacity=".07"/>
    <rect class="bg" y="398" width="{w}" height="{h - 398}"/>

    <g class="mono mu fade" font-size="12.5">
      <text x="56" y="58"><tspan class="fg">PORTFOLIO 2026</tspan>  /  CHENNAI, INDIA</text>
      <text x="{w - 56}" y="58" text-anchor="end">AI/ML ENGINEER  ·  SOFTWARE DEVELOPER</text>
    </g>

    <g class="serif fg" font-size="158" letter-spacing="-7">
      <text class="it rise" x="128" y="226">Saaketh</text>
      <text class="rise" x="50" y="358" style="animation-delay:.12s">Gadepalli</text>
    </g>

    <path class="ln" d="M56 398 H{w - 56}"/>
    <g class="fade" style="animation-delay:.5s">
      <text class="serif fg" x="56" y="438" font-size="27" letter-spacing="-.5">I build models that <tspan class="it" fill="url(#ramp)">show their work</tspan>.</text>
      <rect class="bg" x="{w - 372}" y="414" width="330" height="32" rx="16" opacity=".86"/>
      <rect class="ln" x="{w - 372}" y="414" width="330" height="32" rx="16"/>
      <g class="mono fg" font-size="10.5">
        <circle class="pulse" cx="{w - 352}" cy="430" r="4" fill="#f0432a"/>
        <text x="{w - 60}" y="434" text-anchor="end">ATTENTION  X 0.72  Y 0.53  ACT 0.91</text>
      </g>
    </g>"""
    return svg(w, h, "Saaketh Gadepalli. AI/ML engineer and software developer. I build models that show their work.", defs, body, 22)


# ---------------------------------------------------------------- cards
def card(no, title, sub, metric, metric_label, accent, art, label):
    w, h = 588, 372
    body = f"""
    <rect width="{w}" height="{h}" fill="url(#glow)" opacity=".16"/>
    <text class="mono" x="32" y="46" font-size="12" fill="{accent}">{no}</text>
    <text class="mono mu" x="{w - 32}" y="46" font-size="11" text-anchor="end">OPEN REPOSITORY  ↗</text>
    <g transform="translate(0 62)">{art}</g>
    <text class="serif fg" x="32" y="262" font-size="38" letter-spacing="-1.2">{title}</text>
    <text class="sans mu" x="32" y="290" font-size="15">{sub}</text>
    <path class="ln" d="M32 310 H{w - 32}"/>
    <text class="serif fg" x="32" y="348" font-size="27" letter-spacing="-.6">{metric}</text>
    <text class="mono mu" x="{w - 32}" y="345" font-size="10.5" text-anchor="end">{metric_label}</text>"""
    defs = f"""
    <radialGradient id="glow" cx="78%" cy="26%" r="62%">
      <stop offset="0" stop-color="{accent}"/><stop offset="1" stop-color="{accent}" stop-opacity="0"/>
    </radialGradient>"""
    return svg(w, h, label, defs, body.replace("ACC", accent), 20)


def art_oncoscan():
    rng = random.Random(3)
    noise = "".join(
        f'<circle class="fg" cx="{40 + rng.random() * 90:.0f}" cy="{20 + rng.random() * 130:.0f}" r="{1 + rng.random() * 1.6:.1f}" opacity=".35"/>'
        for _ in range(26)
    )
    outs = [(30, "LEUKEMIA CNN"), (86, "POLYP U-NET"), (142, "MULTI-CANCER")]
    branches = "".join(
        f'<path class="sfg dash" d="M262 86 C 320 86, 318 {y}, 372 {y}" stroke-width="1.3" style="animation-delay:{i * .3}s"/>'
        f'<rect class="card" x="372" y="{y - 15}" width="150" height="30" rx="7"/>'
        f'<text class="mono fg" x="386" y="{y + 4}" font-size="9.5">{name}</text>'
        f'<circle cx="508" cy="{y}" r="4" fill="ACC" class="pulse" style="animation-delay:{i * .5}s"/>'
        for i, (y, name) in enumerate(outs)
    )
    return f"""{noise}
    <path class="sfg dash" d="M140 86 H206" stroke-width="1.3"/>
    <circle cx="236" cy="86" r="44" fill="ACC" opacity=".14" class="pulse"/>
    <circle cx="236" cy="86" r="27" fill="ACC" opacity=".32"/>
    <circle cx="236" cy="86" r="13" fill="ACC"/>
    <text class="mono mu" x="236" y="152" font-size="9.5" text-anchor="middle">MODALITY ROUTER</text>
    {branches}"""


def art_research():
    rows = [("GRAPHSHIELD", 0.62, 0.10), ("PREDICTIQ", 0.48, 0.07), ("PAPERMIND", 0.78, 0.05), ("TERRAVISION", 0.34, 0.11), ("VISIONFORGE", 0.70, 0.06)]
    x0, x1 = 196, 540
    out = [f'<path class="ln" d="M{x0} 6 V166"/>', f'<path class="ln" d="M{x1} 6 V166" stroke-dasharray="2 5"/>']
    for i, (name, mid, half) in enumerate(rows):
        y = 22 + i * 32
        cx = x0 + (x1 - x0) * mid
        hw = (x1 - x0) * half
        out.append(
            f'<text class="mono mu" x="32" y="{y + 4}" font-size="10">{name}</text>'
            f'<path class="ln" d="M{x0} {y} H{x1}" stroke-dasharray="1 6"/>'
            f'<path d="M{cx - hw:.0f} {y} H{cx + hw:.0f}" stroke="ACC" stroke-width="2"/>'
            f'<path d="M{cx - hw:.0f} {y - 5} v10 M{cx + hw:.0f} {y - 5} v10" stroke="ACC" stroke-width="1.4"/>'
            f'<circle cx="{cx:.0f}" cy="{y}" r="5.5" fill="ACC" class="pulse" style="animation-delay:{i * .4}s"/>'
        )
    return "".join(out)


def art_lsm():
    layers = [("WRITE-AHEAD LOG", 8, 300), ("MEMTABLE", 50, 240), ("SSTABLES", 92, 400)]
    out = []
    for i, (name, y, wd) in enumerate(layers):
        out.append(f'<rect class="card" x="150" y="{y}" width="{wd}" height="30" rx="6"/>')
        out.append(f'<text class="mono fg" x="164" y="{y + 19}" font-size="10">{name}</text>')
    cells = "".join(
        f'<rect x="{300 + i * 30}" y="100" width="22" height="14" rx="3" fill="ACC" opacity="{0.25 + (i % 3) * 0.25}" class="pulse" style="animation-delay:{i * .25}s"/>'
        for i in range(8)
    )
    return f"""
    <text class="mono mu" x="32" y="27" font-size="10">PUT(K, V)</text>
    <path class="sfg dash" d="M104 23 H150" stroke-width="1.3"/>
    {''.join(out)}{cells}
    <path class="sfg dash" d="M300 38 V50 M270 80 V92" stroke-width="1.3"/>
    <path class="sfg dash" d="M350 122 V146" stroke-width="1.3"/>
    <rect x="150" y="146" width="400" height="22" rx="6" fill="none" stroke="ACC" stroke-width="1.3"/>
    <text class="mono fg" x="164" y="161" font-size="10">COMPACTION  ·  RAFT REPLICATION</text>"""


def art_city():
    rng = random.Random(8)
    roads = "".join(
        f'<path class="ln" d="M{20 + rng.random() * 40:.0f} {10 + i * 26 + rng.random() * 14:.0f} L {568 - rng.random() * 40:.0f} {4 + i * 27 + rng.random() * 30:.0f}" stroke-width="1.2"/>'
        for i in range(7)
    ) + "".join(
        f'<path class="ln" d="M{60 + i * 82 + rng.random() * 30:.0f} 0 L {40 + i * 84 + rng.random() * 50:.0f} 178" stroke-width="1.2"/>'
        for i in range(7)
    )
    spots = [(170, 70, 46), (392, 112, 34), (300, 40, 22)]
    hot = "".join(
        f'<circle cx="{x}" cy="{y}" r="{r}" fill="ACC" opacity=".14" class="pulse" style="animation-delay:{i * .7}s"/>'
        f'<circle cx="{x}" cy="{y}" r="{r * .5:.0f}" fill="ACC" opacity=".3"/><circle cx="{x}" cy="{y}" r="6" fill="ACC"/>'
        for i, (x, y, r) in enumerate(spots)
    )
    return roads + hot


# ---------------------------------------------------------------- stats band
def stats():
    w, h = 1200, 210
    cells = [("1,232", "+", "CODECHEF PROBLEMS SOLVED"), ("350", "+", "LEETCODE PROBLEMS SOLVED"), ("Blue", "", "CODECHEF RATING · SILVER BADGE"), ("10", "+", "PROJECTS BUILT AND DEPLOYED")]
    cw = (w - 112) / 4
    body = ['<rect width="1200" height="210" fill="url(#heat)" opacity=".1"/>']
    for i, (num, suf, lab) in enumerate(cells):
        x = 56 + i * cw
        body.append(
            f'<path class="sfg" d="M{x:.0f} 44 H{x + cw - 28:.0f}" stroke-width="1"/>'
            f'<text class="serif fg rise" x="{x:.0f}" y="138" font-size="76" letter-spacing="-3.2" style="animation-delay:{i * .12}s">{num}<tspan class="it" fill="url(#ramp)">{suf}</tspan></text>'
            f'<text class="mono mu" x="{x:.0f}" y="174" font-size="10.5">{lab}</text>'
        )
    defs = heat("heat", 600, 105, 520, path=[(200, 105), (1000, 105), (200, 105)], dur=20)
    return svg(w, h, "1,232+ CodeChef problems solved, 350+ LeetCode problems solved, Blue-rated on CodeChef with a Silver Badge, 10+ projects built and deployed.", defs, "\n".join(body), 20)


# ---------------------------------------------------------------- universe map
def universe():
    w, h = 1200, 560
    cx, cy = 600, 285
    clusters = [
        ("HEALTHCARE AI", "#ff5a3c", 320, 150, [("OncoScan-AI", -110, -58), ("Leukemia Detection", -128, 22), ("Polyp Detection", -84, 92)]),
        ("RESEARCH ENGINEERING", "#8a6cff", 950, 150, [("GraphShield", 70, -62), ("PredictIQ", 150, -6), ("PaperMind", 128, 58), ("TerraVision", 66, 104), ("VisionForge", -56, -84)]),
        ("SYSTEMS", "#00a3c4", 270, 420, [("LSM-tree + Raft", -120, 40), ("City Insights", -20, 92)]),
        ("PRODUCTS", "#19b89a", 930, 425, [("AdhikarAI", 110, -30), ("SilentSync", 130, 44), ("BhoomiSetu", 20, 92)]),
    ]
    rng = random.Random(5)
    bgdots = "".join(
        f'<circle class="fg" cx="{rng.random() * w:.0f}" cy="{rng.random() * h:.0f}" r="{0.8 + rng.random() * 1.2:.1f}" opacity=".16"/>' for _ in range(260)
    )
    out = [bgdots]
    for ci, (name, col, x, y, nodes) in enumerate(clusters):
        mx, my = (cx + x) / 2, (cy + y) / 2 + (40 if y < cy else -40)
        out.append(f'<path class="dash" d="M{cx} {cy} Q {mx:.0f} {my:.0f} {x} {y}" stroke="{col}" stroke-width="1.5" fill="none" style="animation-delay:{ci * .3}s"/>')
        out.append(f'<circle cx="{x}" cy="{y}" r="62" fill="{col}" opacity=".13" class="pulse" style="animation-delay:{ci * .8}s"/>')
        for ni, (label, dx, dy) in enumerate(nodes):
            nx, ny = x + dx, y + dy
            anchor = "end" if dx < -10 else "start"
            tx = nx - 12 if anchor == "end" else nx + 12
            out.append(f'<path class="ln" d="M{x} {y} L{nx} {ny}" stroke-width="1.1"/>')
            out.append(f'<circle cx="{nx}" cy="{ny}" r="5.5" fill="{col}"/>')
            out.append(f'<text class="serif fg" x="{tx}" y="{ny + 6}" font-size="19" letter-spacing="-.3" text-anchor="{anchor}">{label}</text>')
        out.append(f'<circle cx="{x}" cy="{y}" r="15" fill="{col}"/>')
    # cluster captions sit on the centre axis so they never collide with node labels
    caps = [(320, 150, "HEALTHCARE AI", "#ff5a3c", 50, 96), (950, 150, "RESEARCH ENGINEERING", "#8a6cff", -70, 98), (270, 420, "SYSTEMS", "#00a3c4", 0, -80), (930, 425, "PRODUCTS", "#19b89a", 0, -80)]
    for x, y, name, col, dx, dy in caps:
        out.append(f'<text class="mono" x="{x + dx}" y="{y + dy}" font-size="10.5" text-anchor="middle" fill="{col}">{name}</text>')
    out.append(f'<circle cx="{cx}" cy="{cy}" r="120" fill="url(#heat)" opacity=".5" class="pulse"/>')
    out.append(f'<circle class="fg" cx="{cx}" cy="{cy}" r="44"/>')
    out.append(f'<text class="serif it" x="{cx}" y="{cy + 13}" font-size="38" text-anchor="middle" style="fill:var(--bg)">SG</text>')
    out.append('<text class="mono mu" x="56" y="50" font-size="11.5"><tspan class="fg">THE ECOSYSTEM</tspan>  /  HOW THE WORK CONNECTS</text>')
    defs = heat("heat", cx, cy, 130)
    return svg(w, h, "Map of Saaketh's projects in four clusters: healthcare AI, research engineering, systems and products.", defs, "\n".join(out), 22)


# ---------------------------------------------------------------- footer
def footer():
    rng = random.Random(21)
    w, h = 1200, 300
    dots = field(rng, w, 196, 320, rows=11)
    defs = heat("heat", 900, 260, 300, path=[(900, 260), (300, 270), (900, 260)], dur=24)
    body = f"""
    <g id="fdots">{dots}</g>
    <use xlink:href="#fdots" href="#fdots" fill="url(#heat)" stroke="url(#heat)" stroke-width="3"/>
    <text class="mono mu" x="56" y="58" font-size="11.5"><tspan fill="#f0432a">06</tspan>  LET'S BUILD SOMETHING</text>
    <text class="serif fg rise" x="56" y="138" font-size="62" letter-spacing="-2.4">Have a model that needs to <tspan class="it" fill="url(#ramp)">explain itself</tspan>?</text>
    <text class="mono fg" x="56" y="190" font-size="13">SAAKETHCSE05@GMAIL.COM</text>"""
    return svg(w, h, "Have a model that needs to explain itself? Email saakethcse05@gmail.com", defs, body, 22)


FILES = {
    "hero.svg": hero(),
    "stats.svg": stats(),
    "universe.svg": universe(),
    "footer.svg": footer(),
    "card-oncoscan.svg": card("01  HEALTHCARE AI", "OncoScan-AI", "Autonomous multi-modality cancer screening", "100% · 91.7% · 0.78", "ROUTER · LEUKEMIA · POLYP DICE", "#ff5a3c", art_oncoscan(), "OncoScan-AI: autonomous multi-modality cancer screening. Router 100%, leukemia 91.7%, polyp Dice 0.78."),
    "card-research.svg": card("02  RESEARCH ENGINEERING", "Five audited studies", "Graphs, time series, retrieval, satellite imagery", "Measured, with intervals", "LEAK-AUDITED · MULTI-SEED", "#8a6cff", art_research(), "Five research studies: GraphShield, PredictIQ, PaperMind, TerraVision, VisionForge."),
    "card-lsm.svg": card("03  SYSTEMS", "LSM-tree + Raft", "A storage engine written from scratch", "No database library", "WAL · SSTABLES · BLOOM · RAFT", "#00a3c4", art_lsm(), "LSM-tree key-value store with Raft replication, written from scratch."),
    "card-city.svg": card("04  SYSTEMS", "City Insights", "Live congestion hotspots on a real road network", "28 road segments", "DBSCAN · FASTAPI · LEAFLET", "#19b89a", art_city(), "Real-time city insights dashboard: DBSCAN congestion hotspots on 28 real road segments."),
}

for name, content in FILES.items():
    (OUT / name).write_text(content, encoding="utf-8")
    print(f"{name:22s} {len(content) / 1024:6.1f} KB")
