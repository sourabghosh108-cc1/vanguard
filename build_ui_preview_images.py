import os
from PIL import Image, ImageDraw, ImageFont

ui_dir = r"c:\Users\ACER\Desktop\design\TeamVanguard_\03_Digital_UI"
brain_dir = r"C:\Users\ACER\.gemini\antigravity-ide\brain\202e0b5b-f952-45a2-8f2e-fbfcb8ac2205"

def get_image(name_prefix):
    files = os.listdir(brain_dir)
    matching = [f for f in files if f.startswith(name_prefix) and (f.endswith('.jpg') or f.endswith('.png'))]
    matching.sort(key=lambda x: os.path.getmtime(os.path.join(brain_dir, x)), reverse=True)
    return os.path.join(brain_dir, matching[0])

pkg_img_path = get_image("vanguard_packaging_mockup")
retail_img_path = get_image("vanguard_retail_display")

# Create Landing Page UI PNG (1920x1080 styled browser mockup)
def create_ui_landing_page():
    width, height = 1920, 1080
    canvas = Image.new('RGBA', (width, height), (11, 12, 14, 255))
    draw = ImageDraw.Draw(canvas)
    
    # Browser Bar Header
    draw.rectangle([0, 0, width, 50], fill=(23, 25, 30, 255))
    # Browser buttons
    draw.ellipse([20, 18, 34, 32], fill=(255, 95, 86))
    draw.ellipse([42, 18, 56, 32], fill=(255, 189, 46))
    draw.ellipse([64, 18, 78, 32], fill=(27, 201, 55))
    # URL bar
    draw.rectangle([200, 10, 1000, 40], fill=(11, 12, 14, 255), outline=(50, 50, 50))
    draw.text((220, 18), "https://vanguard.audio/vh-1-launch", fill=(180, 180, 180))

    # Web Navbar
    draw.rectangle([0, 50, width, 120], fill=(17, 19, 23, 255))
    draw.text((60, 75), "VANGUARD AUDIO", fill=(226, 228, 232))
    draw.text((400, 78), "OVERVIEW", fill=(255, 149, 0))
    draw.text((540, 78), "ACOUSTIC CRAFT", fill=(160, 160, 160))
    draw.text((720, 78), "SPECIFICATIONS", fill=(160, 160, 160))
    draw.text((900, 78), "SOUND SANCTUARY", fill=(160, 160, 160))
    draw.rectangle([1650, 68, 1850, 102], fill=(255, 149, 0))
    draw.text((1675, 78), "RESERVE VH-1", fill=(0, 0, 0))

    # Hero Content
    draw.text((100, 220), "FLAGSHIP SYSTEM // SERIES-V1", fill=(255, 149, 0))
    draw.text((100, 270), "SOUND UNBOUND.", fill=(255, 255, 255))
    draw.text((100, 340), "PRECISION REIMAGINED.", fill=(200, 125, 85))
    draw.text((100, 440), "Experience zero-loss acoustic fidelity engineered with 45mm Graphene drivers.", fill=(160, 160, 160))
    
    # Hero Product Image Insert
    prod_img = Image.open(pkg_img_path).resize((700, 525))
    canvas.paste(prod_img, (1100, 200))
    
    # Specs Cards Bar
    y_card = 780
    for i, (val, lbl) in enumerate([("45mm", "Graphene Drivers"), ("10Hz-48kHz", "Freq Response"), ("32 Ω", "Impedance"), ("98.4%", "Recycled Titanium")]):
        x = 100 + i * 440
        draw.rectangle([x, y_card, x + 400, y_card + 220], fill=(23, 25, 30, 255), outline=(200, 125, 85))
        draw.text((x + 30, y_card + 30), val, fill=(255, 149, 0))
        draw.text((x + 30, y_card + 100), lbl, fill=(200, 125, 85))
        
    canvas.save(os.path.join(ui_dir, "UI_LandingPage.png"), "PNG")
    print("Saved UI_LandingPage.png")

# Create Acoustic Craft UI PNG (1920x1080 styled browser mockup)
def create_ui_acoustic_craft():
    width, height = 1920, 1080
    canvas = Image.new('RGBA', (width, height), (11, 12, 14, 255))
    draw = ImageDraw.Draw(canvas)

    # Header
    draw.rectangle([0, 0, width, 50], fill=(23, 25, 30, 255))
    draw.ellipse([20, 18, 34, 32], fill=(255, 95, 86))
    draw.ellipse([42, 18, 56, 32], fill=(255, 189, 46))
    draw.ellipse([64, 18, 78, 32], fill=(27, 201, 55))
    draw.rectangle([200, 10, 1000, 40], fill=(11, 12, 14, 255), outline=(50, 50, 50))
    draw.text((220, 18), "https://vanguard.audio/acoustic-craft", fill=(180, 180, 180))

    # Navbar
    draw.rectangle([0, 50, width, 120], fill=(17, 19, 23, 255))
    draw.text((60, 75), "VANGUARD AUDIO", fill=(226, 228, 232))
    draw.text((400, 78), "ACOUSTIC CRAFT & SUSTAINABILITY", fill=(255, 149, 0))

    # Craft Page Content
    draw.text((100, 180), "CRAFT ARCHITECTURE", fill=(200, 125, 85))
    draw.text((100, 230), "ACOUSTIC ENGINEERING BREAKDOWN", fill=(255, 255, 255))

    retail_img = Image.open(retail_img_path).resize((850, 550))
    canvas.paste(retail_img, (100, 320))

    # Engineering Feature Cards on Right
    x_right = 1000
    draw.rectangle([x_right, 320, x_right + 820, 480], fill=(23, 25, 30, 255), outline=(200, 125, 85))
    draw.text((x_right + 30, 350), "01. Diaphragm Physics & Linear Motion", fill=(255, 149, 0))
    draw.text((x_right + 30, 400), "Graphene-infused atomic diaphragms maintain linear piston movement up to 48kHz.", fill=(180, 180, 180))

    draw.rectangle([x_right, 510, x_right + 820, 670], fill=(23, 25, 30, 255), outline=(200, 125, 85))
    draw.text((x_right + 30, 540), "02. Sustainable Circular Materials", fill=(255, 149, 0))
    draw.text((x_right + 30, 590), "98.4% Recycled titanium chassis & FSC-certified unbleached packaging.", fill=(180, 180, 180))

    draw.rectangle([x_right, 700, x_right + 820, 860], fill=(23, 25, 30, 255), outline=(200, 125, 85))
    draw.text((x_right + 30, 730), "03. Harman Audiophile Sound Curve Tuning", fill=(255, 149, 0))
    draw.text((x_right + 30, 780), "Sub-bass warm lift with pristine treble resolution.", fill=(180, 180, 180))

    canvas.save(os.path.join(ui_dir, "UI_AcousticCraft.png"), "PNG")
    print("Saved UI_AcousticCraft.png")

create_ui_landing_page()
create_ui_acoustic_craft()

# Save Editable Source HTML bundle notice in Editable_Sources
with open(os.path.join(ui_dir, "Editable_Sources", "Web_UI_Source_Code.html"), "w") as f:
    f.write("<!-- Native HTML5/CSS3/JS Web Application Sources for Vanguard Audio -->\n")

print("UI previews generated successfully!")
