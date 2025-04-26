# Malware Simulation Project

This project simulates a basic malware behavior for educational purposes.

## Files

- file_collector.py: Collects files into a local folder.
- encryptor.py: Encrypts the collected folder into 'files.log'.
- decryptor.py: Decrypts 'files.log' to restore original files.
- exfiltrate.py: Sends 'files.log' to the server.
- exfiltrate_obf.py: Same as exfiltrate.py but with code obfuscation for evasion.

## How to Run

1. Run file_collector.py to collect files.
2. Run encryptor.py to encrypt the collected folder.
3. Run exfiltrate.py (or exfiltrate_obf.py) to exfiltrate 'files.log'.
4. Run decryptor.py to decrypt 'files.log' back to files.

Ensure Python 3.x is installed and required modules like 'cryptography' and 'requests' are installed.
