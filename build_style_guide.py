import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

style_guide_dir = r"c:\Users\ACER\Desktop\design\TeamVanguard_\01_Style_Guide"
pdf_path = os.path.join(style_guide_dir, "Brand_Style_Guide.pdf")

doc = SimpleDocTemplate(pdf_path, pagesize=letter,
                        leftMargin=0.5*inch, rightMargin=0.5*inch,
                        topMargin=0.5*inch, bottomMargin=0.5*inch)

BG_DARK = colors.HexColor("#0B0C0E")
TEXT_LIGHT = colors.HexColor("#E2E4E8")
ACCENT_AMBER = colors.HexColor("#FF9500")
ACCENT_COPPER = colors.HexColor("#C87D55")
CARD_BG = colors.HexColor("#17191E")

styles = getSampleStyleSheet()

title_style = ParagraphStyle(
    'DocTitle',
    fontName='Helvetica-Bold',
    fontSize=26,
    leading=30,
    textColor=ACCENT_AMBER,
    spaceAfter=6
)

h2_style = ParagraphStyle(
    'SectionHeader',
    fontName='Helvetica-Bold',
    fontSize=16,
    leading=20,
    textColor=ACCENT_COPPER,
    spaceBefore=14,
    spaceAfter=8
)

body_style = ParagraphStyle(
    'BodyTextCustom',
    fontName='Helvetica',
    fontSize=10,
    leading=14,
    textColor=TEXT_LIGHT
)

code_style = ParagraphStyle(
    'CodeText',
    fontName='Courier',
    fontSize=9,
    leading=12,
    textColor=ACCENT_AMBER
)

story = []

# Title Banner
story.append(Paragraph("VANGUARD AUDIO", ParagraphStyle('SubHeader', fontName='Helvetica-Bold', fontSize=10, leading=12, textColor=ACCENT_COPPER)))
story.append(Paragraph("OFFICIAL BRAND STYLE GUIDE", title_style))
story.append(Paragraph("Comprehensive Visual Identity System & Design Specifications", body_style))
story.append(Spacer(1, 12))
story.append(HRFlowable(width="100%", thickness=1.5, color=ACCENT_COPPER, spaceAfter=15))

# 1. Brand Philosophy
story.append(Paragraph("1. BRAND PROFILE & MISSION STATEMENT", h2_style))
story.append(Paragraph(
    "Vanguard Audio is a premier high-fidelity sound hardware brand sitting at the intersection of "
    "retro-futuristic minimalism, precision acoustic engineering, and luxury industrial aesthetics. "
    "Our design language balances technical perfection with sustainable circular craftsmanship.",
    body_style
))
story.append(Spacer(1, 10))

# 2. Color Palette System
story.append(Paragraph("2. COLOR PALETTE SYSTEM", h2_style))

color_data = [
    [Paragraph("<b>COLOR NAME</b>", body_style), Paragraph("<b>HEX CODE</b>", body_style), Paragraph("<b>RGB SPEC</b>", body_style), Paragraph("<b>CMYK (PRINT)</b>", body_style), Paragraph("<b>ROLE</b>", body_style)],
    [Paragraph("Obsidian Dark", body_style), Paragraph("#0B0C0E", code_style), Paragraph("11, 12, 14", body_style), Paragraph("75, 68, 67, 90", body_style), Paragraph("Primary Dark Surface", body_style)],
    [Paragraph("Pure Titanium", body_style), Paragraph("#E2E4E8", code_style), Paragraph("226, 228, 232", body_style), Paragraph("8, 5, 4, 0", body_style), Paragraph("Primary Light / Text", body_style)],
    [Paragraph("Acoustic Copper", body_style), Paragraph("#C87D55", code_style), Paragraph("200, 125, 85", body_style), Paragraph("20, 56, 73, 8", body_style), Paragraph("Primary Accent 1", body_style)],
    [Paragraph("Luminescent Amber", body_style), Paragraph("#FF9500", code_style), Paragraph("255, 149, 0", body_style), Paragraph("0, 47, 100, 0", body_style), Paragraph("High-Contrast Glow", body_style)],
    [Paragraph("Studio Slate", body_style), Paragraph("#17191E", code_style), Paragraph("23, 25, 30", body_style), Paragraph("74, 66, 62, 80", body_style), Paragraph("Background Surface", body_style)]
]

t_color = Table(color_data, colWidths=[1.5*inch, 1.2*inch, 1.3*inch, 1.4*inch, 2.1*inch])
t_color.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), ACCENT_COPPER),
    ('TEXTCOLOR', (0,0), (-1,0), colors.black),
    ('BACKGROUND', (0,1), (-1,-1), CARD_BG),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#333333")),
    ('PADDING', (0,0), (-1,-1), 6),
]))
story.append(t_color)
story.append(Spacer(1, 14))

# 3. Typography Hierarchy
story.append(Paragraph("3. TYPOGRAPHY HIERARCHY", h2_style))
typo_data = [
    [Paragraph("<b>ROLE</b>", body_style), Paragraph("<b>TYPEFACE</b>", body_style), Paragraph("<b>USAGE / WEIGHT</b>", body_style)],
    [Paragraph("Display / Headline", body_style), Paragraph("Space Grotesk / Syne", body_style), Paragraph("Bold / ExtraBold (800), Uppercase", body_style)],
    [Paragraph("Body & UI Copy", body_style), Paragraph("Inter / Plus Jakarta Sans", body_style), Paragraph("Regular (400) & Medium (500)", body_style)],
    [Paragraph("Technical Specs", body_style), Paragraph("JetBrains Mono", body_style), Paragraph("Monospaced metrics & frequency numbers", body_style)]
]
t_typo = Table(typo_data, colWidths=[2.0*inch, 2.5*inch, 3.0*inch])
t_typo.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), CARD_BG),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#333333")),
    ('PADDING', (0,0), (-1,-1), 6),
]))
story.append(t_typo)
story.append(Spacer(1, 14))

# 4. Brand Strategy & Prohibited Usage
story.append(Paragraph("4. BRAND USAGE GUIDELINES & PROHIBITED TREATMENTS", h2_style))
usage_text = """
<b>CLEAR SPACE:</b> Always maintain a minimum clear space equal to 1.5x the width of the central 'V' emblem around all logo lockups.<br/><br/>
<b>PROHIBITED TREATMENTS:</b><br/>
• <b>DO NOT</b> stretch, skew, or alter the aspect ratio of vector logo marks.<br/>
• <b>DO NOT</b> change the copper gradient angle or replace Luminescent Amber with unapproved neon colors.<br/>
• <b>DO NOT</b> place low-contrast text on bright backgrounds without proper dark container backing.<br/>
• <b>DO NOT</b> remove the technical calibration markers from official hardware packaging labels.
"""
story.append(Paragraph(usage_text, body_style))

def make_bg(canvas_obj, doc_obj):
    canvas_obj.saveState()
    canvas_obj.setFillColor(BG_DARK)
    canvas_obj.rect(0, 0, doc_obj.pagesize[0], doc_obj.pagesize[1], fill=True, stroke=False)
    canvas_obj.restoreState()

doc.build(story, onFirstPage=make_bg, onLaterPages=make_bg)
print("Brand_Style_Guide.pdf successfully generated!")
