# combine_pdfs.py - Combine all PDFs in the current working directory into one
# pdf.

import pypdf, os

pdf_filenames = []

for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdf_filenames.append(filename)
pdf_filenames.sort(key=str.lower)

writer = pypdf.PdfWriter()

for pdf_filename in pdf_filenames:
    reader = pypdf.PdfReader(pdf_filename)
    writer.append(pdf_filename, (1, len(reader.pages)))

with open('combined.pdf', 'wb') as file:
    writer.write(file)
