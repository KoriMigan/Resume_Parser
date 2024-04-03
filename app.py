import os
import re
import pdfplumber
from docx import Document
import csv

name_regex = r'([A-Z][a-z]+(?: [A-Z][a-z]+)*)'
phone_regex = r'(\+?(\d{1,3})?[\s.-]?\(?(\d{3})\)?[\s.-]?(\d{3})[\s.-]?(\d{4})(?:\s?(?:ext|x|ex|exd|exdt|extn|extnsn|extens|extensn)\s?\d+)?)'

email_regex = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

def parse_pdf(file):
    with pdfplumber.open(file) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text()
        return text

def parse_docx(file):
    doc = Document(file)
    text = '\n'.join([paragraph.text for paragraph in doc.paragraphs])
    return text

def parse_text(file):
    with open(file, 'r') as file:
        text = file.read()
    return text

def extract_contact_info(text):
    name_match = re.search(name_regex, text)
    phone_match = re.search(phone_regex, text)
    email_match = re.search(email_regex, text)

    # Check if any of the matches is None
    if name_match and phone_match and email_match:
        name = name_match.group()
        phone = phone_match.group()
        email = email_match.group()
        return name, phone, email
    else:
        raise ValueError('Unable to extract contact information. Check resume content.')


def save_to_csv(data):
    headers = ['Candidate Name', 'Phone Number', 'Email Address']
    file_exists = os.path.isfile('Contact_information.csv')
    with open('Contact_information.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists or os.path.getsize('Contact_information.csv') == 0:
            writer.writerow(headers)
        writer.writerow(data)


def parse_resume(file):
    try:
        if file.endswith('.pdf'):
            text = parse_pdf(file)
        elif file.endswith('.docx'):
            text = parse_docx(file)
        else:
            text = parse_text(file)
        
        name, phone, email = extract_contact_info(text)
        
        # Check if the data already exists in the CSV file
        if not data_exists_in_csv(name, phone, email):
            save_to_csv([name, phone, email])
            print(f'Contact information extracted from {os.path.basename(file)} and saved successfully.')
        else:
            print(f'Contact information already exists in CSV for {os.path.basename(file)}. Skipping.')
    except Exception as e:
        print(f'Error processing {os.path.basename(file)}:', e)


def data_exists_in_csv(name, phone, email):
    with open('Contact_information.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == name and row[1] == phone and row[2] == email:
                return True
    return False


if __name__ == '__main__':
    # Directory containing sample resumes
    sample_resume_dir = 'sample_resumes'

    # Iterate through sample resumes and parse each one
    for filename in os.listdir(sample_resume_dir):
        resume_path = os.path.join(sample_resume_dir, filename)
        if os.path.isfile(resume_path):
            parse_resume(resume_path)

