# FAST8 saim 10.03.2023
# Скрипт установки штампа регистрации в PDF-файле для 1С:Документооборот
# Устанавливает текстовый штамп регистрации в 2 строки в указанном месте на каждой странице файла
# Основной скрипт. НЕ ПРЕДНАЗНАЧЕН ДЛЯ САМОСТОЯТЕЛЬНОГО ЗАПУСКА! ТОЛЬКО ИЗ БАЗОВОГО СКРИПТА

import io

from PyPDF2 import PdfWriter, PdfReader

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

#source_file = ''
#result_file = ''
#x_coordinat = 0
#y_coordinat = 0
#sting_one = ''
#sting_two = ''
#font_size = 8

pdfmetrics.registerFont(TTFont('Arial', 'Arial.ttf'))
 
packet = io.BytesIO()
# Create a new PDF with Reportlab
can = canvas.Canvas(packet, pagesize=letter)
can.setFont('Arial', font_size)
can.drawString(x_coordinat, y_coordinat, string_one)
can.drawString(x_coordinat, y_coordinat - 25, string_two)
can.showPage()
can.save()
 
# Move to the beginning of the StringIO buffer
packet.seek(0)
new_pdf = PdfReader(packet)
# Read your existing PDF
existing_pdf = PdfReader(open(source_file, "rb"))
output = PdfWriter()
# Add the "watermark" (which is the new pdf) on the existing page
page_indices = list(range(0, len(existing_pdf.pages)))
for index in page_indices:
    page = existing_pdf.pages[index]
    if index == 0:
        page.merge_page(new_pdf.pages[0])
    output.add_page(page)
# Finally, write "output" to a real file
outputStream = open(result_file, "wb")
output.write(outputStream)
outputStream.close()