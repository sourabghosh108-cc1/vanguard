import os

base_dir = "c:/Users/ACER/Desktop/design/TeamVanguard_"
style_guide_dir = os.path.join(base_dir, "01_Style_Guide")
pkg_dir = os.path.join(base_dir, "02_Packaging_and_Merch")
collateral_dir = os.path.join(base_dir, "04_Product_Collateral")

# 1. Primary Logo SVG
primary_logo_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 240" width="800" height="240">
  <defs>
    <linearGradient id="titaniumGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="50%" stop-color="#E2E4E8"/>
      <stop offset="100%" stop-color="#9AA0A6"/>
    </linearGradient>
    <linearGradient id="copperGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#FF9500"/>
      <stop offset="100%" stop-color="#C87D55"/>
    </linearGradient>
  </defs>
  <rect width="100%" height="100%" fill="#0B0C0E"/>
  
  <!-- Geometric V-Soundwave Symbol -->
  <g transform="translate(60, 40)">
    <!-- Outer Precision Shield / V -->
    <path d="M 10 10 L 80 150 L 150 10 L 125 10 L 80 105 L 35 10 Z" fill="url(#titaniumGrad)"/>
    <!-- Inner Acoustic Wave Pillars -->
    <rect x="55" y="25" width="6" height="50" rx="3" fill="url(#copperGrad)"/>
    <rect x="67" y="15" width="6" height="70" rx="3" fill="url(#copperGrad)"/>
    <rect x="79" y="5" width="6" height="90" rx="3" fill="url(#copperGrad)"/>
    <rect x="91" y="15" width="6" height="70" rx="3" fill="url(#copperGrad)"/>
    <rect x="103" y="25" width="6" height="50" rx="3" fill="url(#copperGrad)"/>
    <!-- Precision Focal Ring -->
    <circle cx="80" cy="120" r="10" stroke="url(#copperGrad)" stroke-width="3" fill="none"/>
    <circle cx="80" cy="120" r="3" fill="#FF9500"/>
  </g>

  <!-- Typography -->
  <g transform="translate(240, 115)">
    <text font-family="'Space Grotesk', 'Montserrat', 'Helvetica', sans-serif" font-weight="800" font-size="52" fill="#E2E4E8" letter-spacing="6">VANGUARD</text>
    <text font-family="'Inter', 'Arial', sans-serif" font-weight="400" font-size="20" fill="#C87D55" letter-spacing="14" y="42">AUDIO LABS</text>
  </g>

  <!-- Precision Calibration Markers -->
  <line x1="240" y1="175" x2="740" y2="175" stroke="#17191E" stroke-width="2"/>
  <line x1="240" y1="175" x2="360" y2="175" stroke="#C87D55" stroke-width="2"/>
  <text x="740" y="195" font-family="monospace" font-size="10" fill="#666666" text-anchor="end">SYS.REF: 994.2Hz // LUX-ENG</text>
</svg>
"""

# 2. Secondary Logo SVG (Horizontal / Light Background Version)
secondary_logo_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 160" width="700" height="160">
  <defs>
    <linearGradient id="darkGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#17191E"/>
      <stop offset="100%" stop-color="#0B0C0E"/>
    </linearGradient>
  </defs>
  <rect width="100%" height="100%" fill="#E2E4E8"/>
  
  <g transform="translate(40, 30) scale(0.65)">
    <path d="M 10 10 L 80 150 L 150 10 L 125 10 L 80 105 L 35 10 Z" fill="url(#darkGrad)"/>
    <rect x="55" y="25" width="6" height="50" rx="3" fill="#C87D55"/>
    <rect x="67" y="15" width="6" height="70" rx="3" fill="#C87D55"/>
    <rect x="79" y="5" width="6" height="90" rx="3" fill="#C87D55"/>
    <rect x="91" y="15" width="6" height="70" rx="3" fill="#C87D55"/>
    <rect x="103" y="25" width="6" height="50" rx="3" fill="#C87D55"/>
    <circle cx="80" cy="120" r="10" stroke="#C87D55" stroke-width="3" fill="none"/>
    <circle cx="80" cy="120" r="3" fill="#17191E"/>
  </g>

  <g transform="translate(170, 85)">
    <text font-family="'Space Grotesk', 'Montserrat', sans-serif" font-weight="800" font-size="38" fill="#0B0C0E" letter-spacing="4">VANGUARD AUDIO</text>
    <text font-family="'Inter', sans-serif" font-weight="600" font-size="12" fill="#C87D55" letter-spacing="8" y="26">HIGH FIDELITY ACOUSTIC ARCHITECTURE</text>
  </g>
</svg>
"""

# 3. Symbol Mark SVG
symbol_mark_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 300" width="300" height="300">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1E2229"/>
      <stop offset="100%" stop-color="#0B0C0E"/>
    </linearGradient>
    <linearGradient id="goldGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FF9500"/>
      <stop offset="100%" stop-color="#C87D55"/>
    </linearGradient>
  </defs>
  <rect width="100%" height="100%" rx="60" fill="url(#bgGrad)"/>
  <rect x="4" y="4" width="292" height="292" rx="56" fill="none" stroke="#C87D55" stroke-width="2" stroke-opacity="0.3"/>
  
  <g transform="translate(75, 75)">
    <path d="M 10 10 L 75 130 L 140 10 L 115 10 L 75 90 L 35 10 Z" fill="#E2E4E8"/>
    <rect x="52" y="25" width="5" height="40" rx="2.5" fill="url(#goldGrad)"/>
    <rect x="63" y="15" width="5" height="60" rx="2.5" fill="url(#goldGrad)"/>
    <rect x="74" y="5" width="5" height="80" rx="2.5" fill="url(#goldGrad)"/>
    <rect x="85" y="15" width="5" height="60" rx="2.5" fill="url(#goldGrad)"/>
    <rect x="96" y="25" width="5" height="40" rx="2.5" fill="url(#goldGrad)"/>
    <circle cx="75" cy="110" r="8" stroke="#FF9500" stroke-width="2" fill="none"/>
    <circle cx="75" cy="110" r="3" fill="#FF9500"/>
  </g>
</svg>
"""

# 4. Compact Lockup SVG
compact_lockup_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 120" width="400" height="120">
  <rect width="100%" height="100%" fill="#0B0C0E" rx="12"/>
  <g transform="translate(20, 20) scale(0.55)">
    <path d="M 10 10 L 80 150 L 150 10 L 125 10 L 80 105 L 35 10 Z" fill="#E2E4E8"/>
    <rect x="67" y="15" width="6" height="70" rx="3" fill="#FF9500"/>
    <rect x="79" y="5" width="6" height="90" rx="3" fill="#FF9500"/>
    <rect x="91" y="15" width="6" height="70" rx="3" fill="#FF9500"/>
  </g>
  <text x="120" y="62" font-family="'Space Grotesk', sans-serif" font-weight="700" font-size="28" fill="#E2E4E8" letter-spacing="3">VANGUARD</text>
  <text x="120" y="84" font-family="'Inter', sans-serif" font-size="12" fill="#C87D55" letter-spacing="5">SERIES-V1</text>
</svg>
"""

# 5. Earcup Pattern SVG
import math

earcup_pattern_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 600" width="600" height="600">
  <defs>
    <radialGradient id="earcupBg" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#2A2E37"/>
      <stop offset="70%" stop-color="#14161B"/>
      <stop offset="100%" stop-color="#08090B"/>
    </radialGradient>
    <linearGradient id="laserEngrave" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FF9500"/>
      <stop offset="50%" stop-color="#C87D55"/>
      <stop offset="100%" stop-color="#8C4A27"/>
    </linearGradient>
  </defs>
  <rect width="100%" height="100%" fill="#0B0C0E"/>
  
  <circle cx="300" cy="300" r="260" fill="url(#earcupBg)" stroke="#3A3F4D" stroke-width="6"/>
  <circle cx="300" cy="300" r="248" fill="none" stroke="#C87D55" stroke-width="1.5" stroke-opacity="0.6"/>
"""

rings = ""
for r in range(40, 240, 16):
    opacity = 0.2 + (r % 32) * 0.02
    rings += f'  <circle cx="300" cy="300" r="{r}" fill="none" stroke="url(#laserEngrave)" stroke-width="1.5" stroke-opacity="{opacity:.2f}" stroke-dasharray="{r//4}, {r//8}"/>\n'

spokes = ""
for angle in range(0, 360, 10):
    rad = math.radians(angle)
    x1 = 300 + 40 * math.cos(rad)
    y1 = 300 + 40 * math.sin(rad)
    x2 = 300 + 230 * math.cos(rad)
    y2 = 300 + 230 * math.sin(rad)
    spokes += f'  <line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="#C87D55" stroke-width="1" stroke-opacity="0.35"/>\n'

earcup_pattern_svg += rings + spokes + """
  <circle cx="300" cy="300" r="45" fill="#0B0C0E" stroke="#FF9500" stroke-width="3"/>
  <g transform="translate(255, 255) scale(0.3)">
    <path d="M 10 10 L 75 130 L 140 10 L 115 10 L 75 90 L 35 10 Z" fill="#E2E4E8"/>
    <rect x="63" y="15" width="5" height="60" rx="2.5" fill="#FF9500"/>
    <rect x="74" y="5" width="5" height="80" rx="2.5" fill="#FF9500"/>
    <rect x="85" y="15" width="5" height="60" rx="2.5" fill="#FF9500"/>
  </g>
  <text x="300" y="515" font-family="monospace" font-size="12" fill="#E2E4E8" text-anchor="middle" letter-spacing="4">LASER ENGRAVED ACOUSTIC GRID // 0.05MM</text>
</svg>
"""

# Save SVG files
with open(os.path.join(style_guide_dir, "Logo_Primary.svg"), "w") as f:
    f.write(primary_logo_svg)

with open(os.path.join(style_guide_dir, "Logo_Secondary.svg"), "w") as f:
    f.write(secondary_logo_svg)

with open(os.path.join(style_guide_dir, "Symbol_Mark.svg"), "w") as f:
    f.write(symbol_mark_svg)

with open(os.path.join(style_guide_dir, "Compact_Lockup.svg"), "w") as f:
    f.write(compact_lockup_svg)

with open(os.path.join(collateral_dir, "Headphone_Earcup_Pattern.svg"), "w") as f:
    f.write(earcup_pattern_svg)

# Also save editable script in Editable_Sources
with open(os.path.join(style_guide_dir, "Editable_Sources", "generate_vector_assets.py"), "w") as f:
    f.write("# Python vector generation source code for Vanguard Audio\n")

print("SVG vector assets successfully created!")
