# your_app/management/commands/fill_pdf.py
# django settings


from django.core.management.base import BaseCommand
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.conf import settings
import os

# Requested setting BASE_DIR but settings are not configured. You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.




BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# help = 'Fill out the PDF form with predetermined data'

def handle( *args, **kwargs):
    print('filling pdf')
    # Path to the existing PDF
    pdf_template_path = os.path.join(settings.BASE_DIR, 'Alvandi Order Form.pdf')
    
    # Path to save the new filled PDF
    filled_pdf_path = os.path.join(settings.BASE_DIR, 'Filled_Alvandi_Order_Form.pdf')
    
    # Data to be filled in
    data = {
        'Date Requested': '06/13/2024',
        'Requested By': 'Gil Alvandi',
        'Firm': 'Alvandi Law Group',
        'Phone': '949-777-9897',
        'Fax': '949-777-9448',
        'Email': 'gil@alvandigroup.com',
    }

    fill_pdf(pdf_template_path, filled_pdf_path, data)

def fill_pdf( template_path, output_path, data):
    # Create a canvas to draw the filled form
    c = canvas.Canvas(output_path, pagesize=letter)

    # Draw the form fields
    c.drawString(150, 750, data['Date Requested'])
    c.drawString(150, 730, data['Requested By'])
    c.drawString(150, 710, data['Firm'])
    c.drawString(150, 690, data['Phone'])
    c.drawString(150, 670, data['Fax'])
    c.drawString(150, 650, data['Email'])

    # Save the filled PDF
    c.save()

    print(f'Successfully filled the PDF and saved to {output_path}')


if __name__ == "__main__":
    handle()