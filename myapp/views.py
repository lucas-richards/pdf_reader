import re
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .forms import PDFUploadForm
from .models import Client, Invoice
from datetime import datetime
from PyPDF2 import PdfReader  # Updated 


def extract_client_info(pdf_text):
    client_info = {
        'name': '',
        'email': '',
        'phone': '',
        'address': ''
    }
    
    # Use regular expressions to find patterns
    name_match = re.search(r'REFERRED BY:\s*(.*)', pdf_text)
    email_match = re.search(r'Email:\s*(.*)', pdf_text)
    phone_match = re.search(r'Phone:\s*(.*)', pdf_text)
    address_match = re.search(r'Address:\s*(.*)', pdf_text)
    print(name_match)
    print(email_match)
    print(phone_match)
    print(address_match)

    if name_match:
        client_info['name'] = name_match.group(1).strip()
    if email_match:
        client_info['email'] = email_match.group(1).strip()
    if phone_match:
        client_info['phone'] = phone_match.group(1).strip()
    if address_match:
        client_info['address'] = address_match.group(1).strip()

    return client_info

def extract_invoice_info(pdf_text):
    invoice_info = {
        'invoice_number': '',
        'invoice_date': '',
        'due_date': ''
    }

    invoice_number_match = re.search(r'Invoice No:\s*(.*)', pdf_text)
    invoice_date_match = re.search(r'Invoice Date:\s*(.*)', pdf_text)
    due_date_match = re.search(r'Due Date:\s*(.*)', pdf_text)

    if invoice_number_match:
        invoice_info['invoice_number'] = invoice_number_match.group(1).strip()
    if invoice_date_match:
        invoice_info['invoice_date'] = datetime.strptime(invoice_date_match.group(1).strip(), '%m/%d/%y').date()
    if due_date_match:
        invoice_info['due_date'] = datetime.strptime(due_date_match.group(1).strip(), '%m/%d/%y').date()
    
    return invoice_info

def upload_pdf(request):
    if request.method == 'POST':
        form = PDFUploadForm(request.POST, request.FILES)
        if form.is_valid():
            pdf_file = form.cleaned_data['pdf_file']
            fs = FileSystemStorage(location='/Users/lucasrichards/Desktop/projects/westridge_django/myproject/myapp/documents')
            filename = fs.save(pdf_file.name, pdf_file)
            file_path = fs.path(filename)
            
            # Extract text from the PDF
            pdf_text = ""
            with open(file_path, 'rb') as file:
                pdf_reader = PdfReader(file)  # Updated to use PdfReader
                for page in pdf_reader.pages:
                    pdf_text += page.extract_text()
                    print(page.extract_text())
            
            # Extract client and invoice information from the text
            client_info = extract_client_info(pdf_text)
            invoice_info = extract_invoice_info(pdf_text)
            # Save client to the database
            client, created = Client.objects.get_or_create(
                name=client_info['name'],
                defaults={
                    'email': client_info['email'],
                    'phone': client_info['phone'],
                    'address': client_info['address']
                }
            )

            # Save invoice to the database
            invoice = Invoice(
                client=client,
                invoice_number=invoice_info['invoice_number'],
                invoice_date=invoice_info['invoice_date'],
                due_date=invoice_info['due_date']
            )
            invoice.save()
            
            return render(request, 'success.html',{'client': client_info, 'invoice': invoice_info})
    else:
        form = PDFUploadForm()
    
    return render(request, 'upload_pdf.html', {'form': form})


