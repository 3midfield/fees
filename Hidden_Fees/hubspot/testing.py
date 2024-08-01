import requests


file_path = '/Users/alexanderadams/hiddenfees/Human Interest 408b - 2022.pdf'
access_token = 'pat-na1-d0ccbb98-5138-481c-802f-5883dd9e5a2b'
headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'Bearer {access_token}'
        }
with open(file_path, "rb") as f:
        
        files = {
            "file": (file_path, f),
            "folder_paths": ("Fee-Disclosure-PDFs",)  # Optional: specify a folder path if you want to organize the file
        }
        
response = requests.post('https://api.hubapi.com/filemanager/api/v2/files', headers=headers,  files=files)

if response.status_code == 200:
    data = response.json()
    file_url = data["objects"][0]["url"]
    print(file_url)
else:
    print(f"Error uploading file: {response.text}")