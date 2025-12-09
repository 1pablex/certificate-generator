import os
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from PyPDF2 import PdfReader, PdfWriter, PdfMerger
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import landscape, A4

template = "docBranco2.pdf"  
nomes = "names.txt"
output_folder = "certificados_Gerados"

os.makedirs(output_folder, exist_ok=True)

page_widht, page_height = landscape(A4)

#Posição
x = 100
y = 283.03

# tamnanho e cor 
font_size = 30
color_r = 0 / 255
color_g = 84 / 255
color_b = 153 / 255

#fonte
pdfmetrics.registerFont(TTFont('Montserrat-SemiBold', 'Montserrat-SemiBold.ttf'))

def gerar_overlay(nome, output_file):
    #Cria PDF transparente só com o nome no lugar correto
    c = canvas.Canvas(output_file, pagesize=(page_widht, page_height))

    # Cor 
    c.setFillColorRGB(color_r, color_g, color_b)
    c.setFont("Montserrat-SemiBold", font_size)

    # Escreve o nome 
    c.drawCentredString( 421, 285, nome)
    c.save()


def aplicar_nome(nome):
    overlay_pdf = "overlay.pdf"
    gerar_overlay(nome, overlay_pdf)

    reader_template = PdfReader(template)
    reader_overlay = PdfReader(overlay_pdf)

    writer = PdfWriter()
    base_page = reader_template.pages[0]
    overlay_page = reader_overlay.pages[0]

    base_page.merge_page(overlay_page)
    writer.add_page(base_page)

    with open(os.path.join(output_folder, f"{nome}.pdf"), "wb") as f:
        writer.write(f)

    os.remove(overlay_pdf)


#processa os nomes do arquivo
with open(nomes, "r", encoding="utf-8") as f:
    nomes = [linha.strip() for linha in f if linha.strip()]

for nome in nomes:
    aplicar_nome(nome)

print("PDFs gerados")

#junta os PDFs em um só

Pasta = "certificadosGerados16hrs" 
SAIDA = "certificados_concluidos.pdf"

merger = PdfMerger()

arquivos = sorted([
    f for f in os.listdir(Pasta)
    if f.lower().endswith(".pdf")
])

print(f"Encontrados {len(arquivos)} PDFs. Juntando...")

for pdf in arquivos:
    caminho = os.path.join(Pasta, pdf)
    merger.append(caminho)

# Salva o PDF final
with open(SAIDA, "wb") as f:
    merger.write(f)

print(f"✔ PDF final gerado: {SAIDA}")