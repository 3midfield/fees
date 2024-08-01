import requests
import json 

pdf_url = 'https://5352904.fs1.hubspotusercontent-na1.net/hubfs/5352904/Fee-Disclosure-PDFs/231285%20STEDMAN_WEST_INTERESTS%2c_INC._408b2_10026296-2.pdf'

access_token = 'pat-na1-d0ccbb98-5138-481c-802f-5883dd9e5a2b'
headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': f'Bearer {access_token}'
    }

data = {
        "fields": [
        {
        "objectTypeId": "0-1",
        "name": "email",
        "value": "alexander.adams@forusall.com"
        },
        {
        "objectTypeId": "0-1",
        "name": "firstname",
        "value": "Alex"
        },
        {
        "objectTypeId": "0-1",
        "name": "lastname",
        "value": "Adams"
        },
        {
        "objectTypeId": "0-1",
        "name": "jobtitle",
        "value": "Second Attempt"
        },
        {
        "objectTypeId": "0-1",
        "name": "pdf_url",
        "value": pdf_url
        }]
}
submission = requests.post('https://api.hsforms.com/submissions/v3/integration/submit/5352904/e318ff3b-31d7-4d84-961f-ca6f3b5a3c72', headers=headers, data = json.dumps(data))
print(submission)