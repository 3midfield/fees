import requests
import json

post_url = 'https://api.hubapi.com/filemanager/api/v3/files/upload'

# Update the filename to point to your PDF file
filename = '/Users/alexanderadams/hiddenfees/Empower Fee Disclosure.pdf'

access_token = 'pat-na1-d0ccbb98-5138-481c-802f-5883dd9e5a2b'
headers = {
    'Accept': 'application/json',
    'Authorization': f'Bearer {access_token}'
}
file_options = {
    'access': 'PUBLIC_INDEXABLE',
    "overwrite": False,
    'duplicateValidationStrategy': 'NONE',
    'duplicateValidationScope': 'EXACT_FOLDER'
}

files_data = {
    'file': ('Empower Fee Disclosure.pdf', open(filename, 'rb'), 'application/pdf'),  # Change MIME type to 'application/pdf'
    'options': (None, json.dumps(file_options), 'text/strings'),
    'folderPath': (None, '/Fee-Disclosure-PDFs', 'text/strings')
}

r = requests.post(post_url, headers=headers, files=files_data)

print(r)
print(r.content)
