from fillpdf import fillpdfs
# Input PDF path
input_pdf_path = 'Form.pdf'

# Output PDF path
output_pdf_path = 'Filled_Form.pdf'

# Data to fill into the PDF fields
data_dict = {
    'Date Requested': '2024-06-15',
    'Requested By': 'John Doe',
    'Company Name': 'ABC Inc.',
    'Firm': 'Law Firm LLC',
    'Claim': 'ABC123',
    'Phone': '555-1234',
    'Claims Examiner': 'Jane Smith',
    'Fax': '555-5678',
    'Examiner Phone': '555-9876',
    'Email': 'jane.smith@example.com',
    'Address': '123 Main St',
    'Signature': 'Jane Doe',
    'City State Zip': 'Anytown, USA',
    'Hard Copy  YES': 'X',
    'NO': '',
    'Sets': '2',
    'Phone_2': '555-4321',
    'YES': '',
    'NO_2': 'X',
    'Sets_2': '3',
    'Fax_2': '555-8765',
    'Email_2': 'john.doe@example.com',
    'Firm_2': 'Doe & Associates',
    # Add all other fields similarly
}

# Fill the PDF with the provided field values and save it
fillpdfs.write_fillable_pdf(input_pdf_path, output_pdf_path, data_dict, flatten=False)

print(f'Filled PDF saved to {output_pdf_path}')
