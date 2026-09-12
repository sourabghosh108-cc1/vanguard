import os
from reportlab.lib.pagesizes import landscape, letter
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image as RLImage, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from PIL import Image as PILImage

pres_dir = r"c:\Users\ACER\Desktop\design\TeamVanguard_\06_Presentation"
base_dir = r"c:\Users\ACER\Desktop\design\TeamVanguard_"
brain_dir = r"C:\Users\ACER\.gemini\antigravity-ide\brain\202e0b5b-f952-45a2-8f2e-fbfcb8ac2205"

pdf_path = os.path.join(pres_dir, "Concept_Presentation.pdf")
doc = SimpleDocTemplate(pdf_path, pagesize=landscape(letter),
                        leftMargin=0.4*inch, rightMargin=0.4*inch,
                        topMargin=0.4*inch, bottomMargin=0.4*inch)

styles = getSampleStyleSheet()

# Custom Color Palette
BG_DARK = colors.HexColor("#0B0C0E")
TEXT_LIGHT = colors.HexColor("#E2E4E8")
ACCENT_AMBER = colors.HexColor("#FF9500")
ACCENT_COPPER = colors.HexColor("#C87D55")
CARD_BG = colors.HexColor("#17191E")

title_style = ParagraphStyle(
    'SlideTitle',
    fontName='Helvetica-Bold',
    fontSize=24,
    leading=28,
    textColor=ACCENT_AMBER,
    spaceAfter=12
)

subtitle_style = ParagraphStyle(
    'SlideSubtitle',
    fontName='Helvetica',
    fontSize=13,
    leading=16,
    textColor=ACCENT_COPPER,
    spaceAfter=15
)

body_style = ParagraphStyle(
    'SlideBody',
    fontName='Helvetica',
    fontSize=10,
    leading=14,
    textColor=TEXT_LIGHT
)

header_tag_style = ParagraphStyle(
    'SlideTag',
    fontName='Helvetica-Bold',
    fontSize=9,
    leading=11,
    textColor=ACCENT_COPPER,
    spaceAfter=4
)

story = []

def make_slide_background(canvas_obj, doc_obj):
    canvas_obj.saveState()
    canvas_obj.setFillColor(BG_DARK)
    canvas_obj.rect(0, 0, doc_obj.pagesize[0], doc_obj.pagesize[1], fill=True, stroke=False)
    # Header bar line
    canvas_obj.setStrokeColor(ACCENT_COPPER)
    canvas_obj.setLineWidth(1.5)
    canvas_obj.line(30, doc_obj.pagesize[1] - 40, doc_obj.pagesize[0] - 30, doc_obj.pagesize[1] - 40)
    
    # Footer info
    canvas_obj.setFont("Helvetica", 8)
    canvas_obj.setFillColor(colors.HexColor("#666666"))
    canvas_obj.drawString(30, 20, "VANGUARD AUDIO // BRAND IDENTITY & LAUNCH CAMPAIGN")
    canvas_obj.drawRightString(doc_obj.pagesize[0] - 30, 20, f"SLIDE {canvas_obj._pageNumber} OF 5")
    canvas_obj.restoreState()

# Helper to load image safely
def get_img(rel_path, width=3.2*inch, height=2.4*inch):
    full = os.path.join(base_dir, rel_path)
    if os.path.exists(full):
        return RLImage(full, width=width, height=height)
    return Paragraph("Image Preview", body_style)

# --- SLIDE 1: Concept & Inspiration ---
story.append(Paragraph("VANGUARD AUDIO", header_tag_style))
story.append(Paragraph("SLIDE 1: CONCEPT & INSPIRATION", title_style))
story.append(Paragraph("Brand Story, Moodboard & Industrial Design Philosophy", subtitle_style))

col1_text = """
<b>THE BRAND STORY:</b><br/>
Vanguard Audio sits at the convergence of retro-futuristic minimalism, precision acoustic engineering, and luxury industrial aesthetics. Designed for audiophiles who demand uncompromising acoustic fidelity.<br/><br/>
<b>CORE PHILOSOPHY:</b><br/>
• <b>Zero-Smear Acoustic Architecture:</b> Precision 45mm Graphene drivers.<br/>
• <b>Sustainable Luxury:</b> 98.4% recycled titanium chassis.<br/>
• <b>Modular Repairability:</b> Designed for circular longevity.
"""

img1 = get_img("02_Packaging_and_Merch/Packaging_Design.png", width=3.6*inch, height=2.7*inch)

t1 = Table([[Paragraph(col1_text, body_style), img1]], colWidths=[4.2*inch, 3.8*inch])
t1.setStyle(TableStyle([
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('BACKGROUND', (0,0), (-1,-1), CARD_BG),
    ('PADDING', (0,0), (-1,-1), 14),
    ('BOTTOMPADDING', (0,0), (-1,-1), 14),
]))
story.append(t1)
story.append(Spacer(1, 100)) # Force page break

# --- SLIDE 2: Brand Identity Rationale ---
story.append(Paragraph("VANGUARD AUDIO", header_tag_style))
story.append(Paragraph("SLIDE 2: BRAND IDENTITY RATIONALE", title_style))
story.append(Paragraph("Visual Breakdown: Logo Logic, Color Palette & Packaging", subtitle_style))

col2_text = """
<b>LOGO LOGIC:</b> Geometric 'V' emblem integrated with soundwave harmonic bars.<br/>
<b>COLOR PALETTE:</b><br/>
• <b>Obsidian Dark (#0B0C0E):</b> Depth and studio soundstage.<br/>
• <b>Pure Titanium (#E2E4E8):</b> Structural precision.<br/>
• <b>Acoustic Copper (#C87D55):</b> Warm acoustic resonance.<br/>
• <b>Luminescent Amber (#FF9500):</b> Vacuum-tube warmth.<br/><br/>
<b>PACKAGING STRATEGY:</b> Eco-friendly unbleached molded pulp box with embossed copper foil branding.
"""

img2 = get_img("02_Packaging_and_Merch/Merch_Mockups.png", width=3.6*inch, height=2.7*inch)

t2 = Table([[Paragraph(col2_text, body_style), img2]], colWidths=[4.2*inch, 3.8*inch])
t2.setStyle(TableStyle([
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('BACKGROUND', (0,0), (-1,-1), CARD_BG),
    ('PADDING', (0,0), (-1,-1), 14),
]))
story.append(t2)
story.append(Spacer(1, 100))

# --- SLIDE 3: UI/UX & Retail Approach ---
story.append(Paragraph("VANGUARD AUDIO", header_tag_style))
story.append(Paragraph("SLIDE 3: UI/UX & RETAIL APPROACH", title_style))
story.append(Paragraph("Architectural Decisions: Web UI & Physical Pop-Up Retail", subtitle_style))

col3_text = """
<b>DIGITAL UI/UX ARCHITECTURE:</b><br/>
• Dark glassmorphic interface with real-time frequency spectrum visualizer.<br/>
• Interactive 360-degree component breakdown & sound profile tuning.<br/><br/>
<b>RETAIL EXPERIENCE:</b><br/>
• Pop-up listening sanctuary booth featuring warm ambient acoustic illumination.<br/>
• Floor-standee graphics for flagship audio boutiques.
"""

img3 = get_img("04_Product_Collateral/Retail_Display.png", width=3.6*inch, height=2.7*inch)

t3 = Table([[Paragraph(col3_text, body_style), img3]], colWidths=[4.2*inch, 3.8*inch])
t3.setStyle(TableStyle([
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('BACKGROUND', (0,0), (-1,-1), CARD_BG),
    ('PADDING', (0,0), (-1,-1), 14),
]))
story.append(t3)
story.append(Spacer(1, 100))

# --- SLIDE 4: Final Deliverables Overview ---
story.append(Paragraph("VANGUARD AUDIO", header_tag_style))
story.append(Paragraph("SLIDE 4: FINAL DELIVERABLES OVERVIEW", title_style))
story.append(Paragraph("Showcase of Packaging, Collateral, Merch & Event Poster", subtitle_style))

col4_text = """
<b>CAMPAIGN DELIVERABLES SUMMARY:</b><br/>
1. <b>Brand Style Guide:</b> Complete vector logo lockups & color codes.<br/>
2. <b>Packaging & Merch:</b> Eco box design & high-density merch apparel.<br/>
3. <b>Digital UI:</b> Responsive web app with interactive audio tools.<br/>
4. <b>Hardware Customization:</b> Laser-etched earcup acoustic pattern.<br/>
5. <b>Launch Event Poster:</b> A2 promotional print for 'Sound Sanctuary'.
"""

img4 = get_img("05_Campaign_Poster/Poster_A2.png", width=2.4*inch, height=3.2*inch)

t4 = Table([[Paragraph(col4_text, body_style), img4]], colWidths=[4.8*inch, 3.2*inch])
t4.setStyle(TableStyle([
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('BACKGROUND', (0,0), (-1,-1), CARD_BG),
    ('PADDING', (0,0), (-1,-1), 12),
]))
story.append(t4)
story.append(Spacer(1, 100))

# --- SLIDE 5: Team Details & Role Distribution ---
story.append(Paragraph("VANGUARD AUDIO", header_tag_style))
story.append(Paragraph("SLIDE 5: TEAM DETAILS & ROLE DISTRIBUTION", title_style))
story.append(Paragraph("Team Members, Contact & Contribution Matrix", subtitle_style))

col5_text = """
<b>TEAM NAME:</b> Team Vanguard<br/>
<b>TEAM LEADER CONTACT:</b> lead@vanguard-audio.com | +1 (555) 019-8842<br/><br/>
<b>MEMBER CONTRIBUTIONS & ROLES:</b><br/>
• <b>Creative Director & Brand Lead:</b> Logo system, visual identity & brand style guide.<br/>
• <b>Industrial Design Lead:</b> Packaging design, earcup pattern laser vector & retail booth.<br/>
• <b>Digital UI/UX Architect:</b> Web application, acoustic craft page & interactive visualizer.<br/>
• <b>Campaign Strategist:</b> Event poster design, pitch deck & final deliverable packaging.
"""

img5 = get_img("04_Product_Collateral/Headphone_Earcup_Pattern.png", width=2.8*inch, height=2.8*inch)

t5 = Table([[Paragraph(col5_text, body_style), img5]], colWidths=[4.6*inch, 3.4*inch])
t5.setStyle(TableStyle([
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('BACKGROUND', (0,0), (-1,-1), CARD_BG),
    ('PADDING', (0,0), (-1,-1), 14),
]))
story.append(t5)

doc.build(story, onFirstPage=make_slide_background, onLaterPages=make_slide_background)
print("Concept_Presentation.pdf successfully compiled (5 slides)!")
