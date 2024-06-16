from pdfrw import PdfReader

# Load the PDF
template_path = 'Form.pdf'
reader = PdfReader(template_path)

# Print the field names
for page in reader.pages:
    if page.Annots:
        for annot in page.Annots:
            if annot.Subtype == '/Widget':
                if annot.T:
                    print(annot.T)

# Output: