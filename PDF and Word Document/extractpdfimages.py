import pypdf
PDF_FILENAME = 'Recursion_Chapter1.pdf'

reader = pypdf.PdfReader(PDF_FILENAME)
image_num = 0

for i, page in enumerate(reader.pages):
    print(f"Reading page {i+1} - {len(page.images)} images found...")
