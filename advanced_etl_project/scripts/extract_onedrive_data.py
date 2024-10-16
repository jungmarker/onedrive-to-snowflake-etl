import requests
from config import ONEDRIVE

def get_onedrive_access_token():
    token_data = {
        'client_id': ONEDRIVE['client_id'],
        'scope': 'https://graph.microsoft.com/.default',
        'client_secret': ONEDRIVE['client_secret'],
        'grant_type': 'client_credentials'
    }
    token_r = requests.post(f"https://login.microsoftonline.com/{ONEDRIVE['tenant_id']}/oauth2/v2.0/token", data=token_data)
    token_r.raise_for_status()
    return token_r.json()['access_token']

def download_file_from_onedrive(file_name):
    access_token = get_onedrive_access_token()
    headers = {'Authorization': f'Bearer {access_token}'}
    download_url = f"https://graph.microsoft.com/v1.0/me/drive/root:/path/to/{file_name}:/content"

    response = requests.get(download_url, headers=headers)
    if response.status_code == 200:
        file_extension = file_name.split('.')[-1]
        file_path = f'/tmp/{file_name}'
        
        # Save the file based on its extension
        with open(file_path, 'wb') as f:
            f.write(response.content)
        
        return file_path, file_extension
    else:
        raise Exception(f"Failed to download file: {response.content}")
