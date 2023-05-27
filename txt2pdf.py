"""
sudo apt-get install libcairo2-dev
sudo apt-get install fonts-dejavu
pip install reportlab
pip install svglib
"""

from reportlab.lib.pagesizes import A4
#!/usr/bin/env python3
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from reportlab.lib.utils import simpleSplit
#from reportlab.graphics.shapes import Drawing
#from reportlab.platypus import Image
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF


__version__ = "0.2.0" # 2023/02

x0 = 50
y0 = A4[1] - 50


svg_logo = "imgs/nostr_32x32.svg"
svg_file = "imgs/nostr_320x240.svg"
pdf_file = "data/example_nostr1.pdf"
title = "Nostr - shrnutí"
perex = "(NOSTR = Notes and Other Stuff Transmitted by Relays)"
footer = "(AgamaPoint 2023/03)"
input_file = "data/nostr1b.txt"


def create_pdf():
    c = canvas.Canvas(pdf_file, pagesize=A4)

    font_name = "DejaVuSans"
    font_name_bold = "DejaVuSans-Bold"
    pdfmetrics.registerFont(TTFont(font_name_bold, 'DejaVuSans-Bold.ttf'))
    pdfmetrics.registerFont(TTFont(font_name, "DejaVuSans.ttf"))

    x, y = x0, y0
    width = A4[0] - 2 * x
    height = A4[1] - 100

    c.setFont(font_name_bold, 20)
    c.drawString(x +35, y, title)
    
    drawing = svg2rlg(svg_logo)
    renderPDF.draw(drawing, c, x-3, y-10)

    y -= 30

    c.setFont(font_name_bold, 12)
    c.drawString(x, height +30, perex)

    c.setStrokeColor(colors.red)
    c.setLineWidth(1)
    c.line(x, y, x + width, y)
    y -= 20  # Space between line and text

    
    with open(input_file, "r", encoding="utf-8") as file:
        #text = file.read().replace("\n", " ")
        text = file.read()

    # Dividing text into paragraphs
    paragraphs = text.split("\n\n")
    c.setFont(font_name, 12)

    for paragraph in paragraphs:
        lines = simpleSplit(paragraph, font_name, 12, width)  # Text line breaks
        for line in lines:
            c.drawString(x, y, line)
            y -= 16  # Line height
        y -= 10  # Space between paragraphs

    y -= 200
    width = 50
    height = 30
   
    drawing = svg2rlg(svg_file)
    renderPDF.draw(drawing, c, x, y)
    
    hl = 800 # bottom
    c.line(50, A4[1] - hl, A4[0] - 50, A4[1] - hl)

    c.setFont(font_name, 12)
    c.drawString(x, height -800, footer)

    c.save()
    print("PDF document - OK")

# ======================================================
create_pdf()
