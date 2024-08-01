import requests
import PyPDF2
from io import BytesIO
from parsing_pdf import pdf_parser
import pdfplumber
import io
from googleapiclient.http import MediaIoBaseDownload

# Replace with your file ID
FILE_ID = '1p0XoWfKv9ft8oHkuL86Zaho9qv2Euzvg'

# Request the file
request = drive_service.files().get_media(fileId=FILE_ID)

# Download the file
fh = io.BytesIO()
downloader = MediaIoBaseDownload(fh, request)
done = False
while done is False:
    status, done = downloader.next_chunk()
    print(f"Downloaded {int(status.progress() * 100)}%")

# Save or use the BytesIO object (fh) containing the PDF
with open('output.pdf', 'wb') as f:
    fh.seek(0)
    f.write(fh.read())


# shareable_link = 'https://drive.google.com/file/d/1p0XoWfKv9ft8oHkuL86Zaho9qv2Euzvg/view'
# file_id = shareable_link.split('/')[-2]
# print(file_id)
# direct_link = f'https://drive.google.com/uc?export=download&id={file_id}'

# # Download the PDF
# response = requests.get(direct_link)

# # Check if the download was successful
# if response.status_code == 200:
#     # Read the PDF from the response
#     pdf_file = BytesIO(response.content)
#     pdf_parser(pdf_file)

#     # Extract the text
    
