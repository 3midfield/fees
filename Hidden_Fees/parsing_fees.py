import pdfplumber
import ocrmypdf
import json
from io import BytesIO
import base64
import pytesseract
from pdf2image import convert_from_bytes

def find_value(text, index):
    if index != -1:
        substring = text[index:]

        # Split the substring by whitespace and look for a numerical value
        for word in substring.split():
            if '$' in word or '%' in word or word.replace(',', '').replace('.', '').isdigit():
                number = word
                # print(f"Number associated with key: {number}")
                number = number.replace('$', '').replace('%', '').replace(',', '')
                return number
    else:
        return 0

def parse_adp(text):
    plan_assets = float(find_value(text, text.find('Plan Assets')))
    print(plan_assets)
    participants = float(find_value(text, text.find('Number of Participants')))
    print(participants)
    assets_minus_loans = float(find_value(text, text.find('Total Plan Assets (minus loans)')))
    print(assets_minus_loans)
    rev_share_percent = float(find_value(text, text.find('Services to Investment Funds')))/100
    print(rev_share_percent)
    net_investments_percent = float(find_value(text, text.find('Net Expense Ratio')))/100
    print(net_investments_percent)
    
    monthly_rk = float(find_value(text, text.find('Administrative Services Fees:')))
    print(monthly_rk)
    annual_rk = monthly_rk * 12 
    print('Annual RK: ' + str(annual_rk))
    # print(annual_rk)
    net_investments = net_investments_percent * assets_minus_loans
    print(net_investments)
    
    # print(net_investments)
    rev_share =  rev_share_percent * assets_minus_loans
    print(rev_share)
    total_investments = net_investments + rev_share
    print(total_investments)
    
    total_cost = annual_rk + total_investments
    print(total_cost)
    rounded_number = round(total_cost, 2)
    print(rounded_number)
    return rounded_number

def is_scanned_pdf(file_content):
    with pdfplumber.open(BytesIO(file_content)) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text and text.strip():
                # If any selectable text is found, return False
                return False
    # If no selectable text is found, return True
    return True

# file_path = '/Users/alexanderadams/hiddenfees/SilkScreen2023.pdf'

        
def document_parser(event, context):
    print('it is working')
    body_data = json.loads(event['body'])
    
    file_content_base64 = body_data['file']
    
    # Extract the base64-encoded file from the event
    file_content = base64.b64decode(file_content_base64)
    if is_scanned_pdf(file_content):
        print('ocr pdf')
    #     file_stream = BytesIO(file_content)
    #     output_file_path = "/tmp/output"
    #     #
    #     ocrmypdf.ocr(input_file=file_stream, output_file=output_file_path, force_ocr=True)
    #     print('gets passed ocr')
    # # Reset the position of the output stream to the beginning
    
    #     # Use pdfplumber to extract text from the OCR'd stream
    #     with pdfplumber.open(output_file_path) as pdf:
    #         text = ''
    #         tables = []
    #         for page in pdf.pages:
    #             text += page.extract_text()
    #             tables.append(page.extract_tables())
    #             for table in page.extract_tables():
    #                 if table is not None:
    #                     # print(table)
    #                     # table_str = '\n'.join(['\t'.join(row) for row in table])
    #                     table_str = '\n'.join(['\t'.join(str(cell) if cell is not None else '' for cell in row) for row in table])
    #                     text += table_str
        
    # Use ocrmypdf to process the stream
        file_stream = BytesIO(file_content)
          # Replace 'your_pdf_data' with the actual byte content of your PDF
        
        # Convert the PDF stream to a list of images
        images = convert_from_bytes(file_stream.getvalue())
        print('converted into an image')
        # Loop through the images and extract text
        text = ''
        for image in images:
            print('made it into the for loop')
            extracted_text = pytesseract.image_to_string(image)
            text += extracted_text
            print(extracted_text)
        index = text.find('ADP')
        if index != -1:   
            answer = parse_adp(text) 
            response = {
                "statusCode": 200,
                "headers": {
                    "Access-Control-Allow-Origin": "https://fee-disclosure-agent.webflow.io",
                    "Access-Control-Allow-Headers": "Content-Type",
                    "Access-Control-Allow-Methods": "OPTIONS,POST,GET"
                },
                "body":json.dumps({
                    "eventData": str(answer)
                })
            }   
            
            return response
            print(answer)
        else:
            
            response = {
                "statusCode": 200,
                "headers": {
                    "Access-Control-Allow-Origin": "https://fee-disclosure-agent.webflow.io",
                    "Access-Control-Allow-Headers": "Content-Type",
                    "Access-Control-Allow-Methods": "OPTIONS,POST,GET"
                },
                "body":json.dumps({
                    "eventData": '0'
                })
            }
            print('0')
            return response
    # Process the PDF with pdfplumber
    else:
        with pdfplumber.open(BytesIO(file_content)) as f:
            print('it is still working')
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
            response = {
                "statusCode": 200,
                "headers": {
                    "Access-Control-Allow-Origin": "https://fee-disclosure-agent.webflow.io",
                    "Access-Control-Allow-Headers": "Content-Type",
                    "Access-Control-Allow-Methods": "OPTIONS,POST,GET"
                },
                "body":json.dumps({
                    "eventData": str(answer)
                })
            }
            
            return response
        else:
            
            response = {
                "statusCode": 200,
                "headers": {
                    "Access-Control-Allow-Origin": "https://fee-disclosure-agent.webflow.io",
                    "Access-Control-Allow-Headers": "Content-Type",
                    "Access-Control-Allow-Methods": "OPTIONS,POST,GET"
                },
                "body":json.dumps({
                    "eventData": '0'
                })
            }
            
            return response