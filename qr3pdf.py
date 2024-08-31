import os
import qrcode
from fpdf import FPDF
import random
import datetime

"""
from lib.qr3pdf import generate_qr_pdf

a = "Toto je první text pro QR kód"
b = "Toto je druhý text pro QR kód 123456789123456789"
c = "Toto je 3. text pro QR kód 333 333 333"

nadpis = "test QR PDF"
pdf_filename = generate_qr_pdf(a, b, c, nadpis)
print(f"PDF soubor byl uložen jako: {pdf_filename}")
"""


def generate_qr_pdf(a: str, b: str, c: str, nadpis: str, save_dir: str = "data_pdf") -> str:
    # Vytvoření QR kódů
    qr_a = qrcode.make(a)
    qr_b = qrcode.make(b)
    qr_c = qrcode.make(c)
    
    # Generování souborového jména
    now = datetime.datetime.now()
    rr = now.year
    mm = f'{now.month:02d}'
    random_number = random.randint(1000, 9999)
    filename = f"{save_dir}/{rr}{mm}{random_number}.pdf"

    # Vytvoření PDF souboru
    pdf = FPDF()
    pdf.add_page()

    # Správná cesta k fontu
    font_path = os.path.join(os.path.dirname(__file__), '', 'DejaVuSansMono.ttf')
    
    # Přidání vlastního fontu
    pdf.add_font('DejaVu', '', font_path, uni=True)
    
    # Nastavení nadpisu
    pdf.set_font('DejaVu', size=16)
    pdf.cell(200, 10, txt=nadpis, ln=True, align="C")
    pdf.ln(10)

    # Vložení prvního QR kódu a textu pod něj
    qr_a_filename = "qr_a.png"
    qr_a.save(qr_a_filename)
    pdf.image(qr_a_filename, x=10, y=30, w=50)
    pdf.set_font('DejaVu', size=9)
    pdf.set_y(85)
    pdf.cell(0, 10, txt=a, ln=True, align="L")  # Zarovnání textu vlevo
    
    # Vložení druhého QR kódu a textu pod něj
    qr_b_filename = "qr_b.png"
    qr_b.save(qr_b_filename)
    pdf.image(qr_b_filename, x=10, y=100, w=50)
    pdf.set_y(155)
    pdf.cell(0, 10, txt=b, ln=True, align="L")  # Zarovnání textu vlevo
    
    # Vložení třetího QR kódu a textu pod něj
    qr_c_filename = "qr_c.png"
    qr_c.save(qr_c_filename)
    pdf.image(qr_c_filename, x=10, y=170, w=50)
    pdf.set_y(225)
    pdf.cell(0, 10, txt=c, ln=True, align="L")  # Zarovnání textu vlevo

    # Uložení PDF
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    
    pdf.output(filename)
    
    # Smazání dočasných QR obrázků
    os.remove(qr_a_filename)
    os.remove(qr_b_filename)
    os.remove(qr_c_filename)
    
    return filename
