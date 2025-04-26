import os
import shutil

def simulate_exfiltration(encrypted_file, exfil_folder):
    if not os.path.exists(exfil_folder):
        os.makedirs(exfil_folder)

    destination = os.path.join(exfil_folder, os.path.basename(encrypted_file))
    shutil.copy2(encrypted_file, destination)
    print(f"Encrypted file exfiltrated to: {destination}")

if __name__ == "__main__":
    simulate_exfiltration("files.log", "exfiltrated_data")
