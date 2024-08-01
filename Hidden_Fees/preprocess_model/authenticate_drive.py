from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import io
from googleapiclient.http import MediaIoBaseDownload
from pdfminer.high_level import extract_text
import pdfplumber
from parsing_pdf import pdf_parser
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from google.oauth2 import service_account
import math

#service account: pdf-extractor@pdf-parser-395411.iam.gserviceaccount.com


# Load client secrets
CLIENT_SECRETS_FILE = '/Users/'
SCOPES = ['**********']

REDIRECT_URI = '*********'

# Create OAuth 2.0 flow
flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)

# Set the redirect URI
flow.redirect_uri = REDIRECT_URI

# Run the local server
# credentials = flow.run_local_server(port=8000)
# credentials = Credentials.from_service_account_file('/Users/alexanderadams/hiddenfees/preprocess_model/service_account_credentials.json', scopes=['https://www.googleapis.com/auth/drive'])
credentials_file_path = '*********'
scopes = ['*************']
# Load the credentials from the JSON key file
credentials = service_account.Credentials.from_service_account_file(credentials_file_path, scopes=scopes)
# Create flow and obtain credentials


# Build the Drive API client
drive_service = build('drive', 'v3', credentials=credentials)

with open('***********************') as csv_file:
    dataframe = pd.read_csv(csv_file)
    name = dataframe['RK']
    url = dataframe['PDFLink']
    company = dataframe['Name']
    for i in range(len(dataframe)):
        if name[i] == 'ADP':
            if len(str(url[i])) < 5:
                continue
            shareable_link = url[i]
            # print(shareable_link)
            file_id = shareable_link.split('/')[-2]
            # print(file_id)

            # Request the file
            request = drive_service.files().get_media(fileId=file_id)

            # Download the file
            fh = io.BytesIO()


            downloader = MediaIoBaseDownload(fh, request)
            done = False
            while done is False:
                status, done = downloader.next_chunk()
                print(f"Downloaded {int(status.progress() * 100)}%")

            pdf_parser(fh, name[i], company[i])
    
# Replace with your file ID