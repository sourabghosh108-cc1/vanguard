import os
from reportlab.lib.pagesizes import A2, portrait
from reportlab.lib import colors
from reportlab.pdfgen import canvas

poster_dir = r"c:\Users\ACER\Desktop\design\TeamVanguard_\05_Campaign_Poster"
poster_img_path = os.path.join(poster_dir, "Poster_A2.png")
pdf_path = os.path.join(poster_dir, "Poster_Print.pdf")

c = canvas.Canvas(pdf_path, pagesize=portrait(A2))
w, h = A2

if os.path.exists(poster_img_path):
    c.drawImage(poster_img_path, 0, 0, width=w, height=h)

# Draw subtle crop marks
c.setStrokeColor(colors.HexColor("#FF9500"))
c.setLineWidth(1)
c.line(10, h-30, 40, h-30)
c.line(30, h-10, 30, h-40)
c.line(w-40, h-30, w-10, h-30)
c.line(w-30, h-10, w-30, h-40)
c.line(10, 30, 40, 30)
c.line(30, 10, 30, 40)
c.line(w-40, 30, w-10, 30)
c.line(w-30, 10, w-30, 40)

c.save()
print("Poster_Print.pdf successfully generated with exact A2 dimensions!")
