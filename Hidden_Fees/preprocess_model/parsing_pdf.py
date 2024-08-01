import PyPDF2
from pdfminer.high_level import extract_text
import pandas as pd
import pdfquery
import pdfplumber
import ocrmypdf
import pytesseract
from langchain.document_loaders import PyPDFLoader
from preprocess_model.extract_fee_text import extract_info
from preprocess_model.mongo_documents import add_to_mongo
from preprocess_model.adp_calculations import parse_adp
from flask import Flask, request, jsonify
from preprocess_model.fidelity_calculations import parse_fidelity

#LANGCHAIN PDF LOADER(does not work well with tables)
# loader = PyPDFLoader("/Users/alexanderadams/hiddenfees/Empower Fee Disclosure.pdf")
# pages = loader.load_and_split()
# print(pages[4])

def is_scanned_pdf(file_path):
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text and text.strip():
                # If any selectable text is found, return False
                return False
    # If no selectable text is found, return True
    return True

# file_path = '/Users/alexanderadams/hiddenfees/SilkScreen2023.pdf'

def pdf_parser(file_path, provider, company):
    if is_scanned_pdf(file_path):
        print("The PDF likely contains scanned images.")
        output_pdf_path = 'outputrkd.pdf'

            # Run OCR on the scanned PDF
        ocrmypdf.ocr(file_path, output_pdf_path, force_ocr=True)

            # Open the OCR'd PDF and extract the text
        with pdfplumber.open(output_pdf_path) as pdf:
            text = ''
            tables = []
            for page in pdf.pages:
                text += page.extract_text()
                print(page.extract_tables())
                tables.append(page.extract_tables())

            # Print the extracted text
            print(text)
            extract_info(text,tables)
        if company == 'ADP':   
            parse_adp(text)   
    else:
        print("The PDF contains selectable text.")

        with pdfplumber.open(file_path) as f:
            text = ''
            tables = []
            for i in f.pages:
                tables.append(i.extract_tables())
                # print(i.extract_tables())
                text += i.extract_text()
                # print(i.extract_text())
                for table in i.extract_tables():
                    if table is not None:
                        # print(table)
                        # table_str = '\n'.join(['\t'.join(row) for row in table])
                        table_str = '\n'.join(['\t'.join(str(cell) if cell is not None else '' for cell in row) for row in table])
                        text += table_str
        if company == 'ADP':   
            parse_adp(text)             
        # extract_info(text, tables)
        # add_to_mongo(provider, company ,text)
        
def document_parser(file_path):
    print(file_path)
    print('it has been called')
    if is_scanned_pdf(file_path):
        print("The PDF likely contains scanned images.")
        output_pdf_path = 'outputrkd.pdf'

            # Run OCR on the scanned PDF
        ocrmypdf.ocr(file_path, output_pdf_path, force_ocr=True)

            # Open the OCR'd PDF and extract the text
        with pdfplumber.open(output_pdf_path) as pdf:
            text = ''
            tables = []
            for page in pdf.pages:
                text += page.extract_text()
                print(page.extract_tables())
                tables.append(page.extract_tables())

            # Print the extracted text
            print(text)
            extract_info(text,tables)
        index = text.find('ADP')
        if index != -1:   
            parse_adp(text)   
    else:
        print("The PDF contains selectable text.")

        with pdfplumber.open(file_path) as f:
            text = ''
            tables = []
            for i in f.pages:
                tables.append(i.extract_tables())
                # print(i.extract_tables())
                text += i.extract_text()
                # print(i.extract_text())
                for table in i.extract_tables():
                    if table is not None:
                        # print(table)
                        # table_str = '\n'.join(['\t'.join(row) for row in table])
                        table_str = '\n'.join(['\t'.join(str(cell) if cell is not None else '' for cell in row) for row in table])
                        text += table_str
        index = text.find('ADP')
        if index != -1:   
            answer = parse_adp(text) 
            return str(answer)
        else:
            return 'None'

