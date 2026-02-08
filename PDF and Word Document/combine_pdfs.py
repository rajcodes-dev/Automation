# combine_pdfs.py - Combine all PDFs in the current working directory into one
# pdf.

import pypdf, os

pdf_filenames = []

for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdf_filenames.append(filename)
pdf_filenames.sort(key=str.lower)

writer = pypdf.PdfWriter()


