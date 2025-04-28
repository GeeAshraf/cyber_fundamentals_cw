import os
import zipfile
import shutil
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def zip_folder(folder_path, zip_path):
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(folder_path):
            for file in files:
                full_path = os.path.join(root, file)
                arcname = os.path.relpath(full_path, folder_path)
                zipf.write(full_path, arcname)

def encrypt_file(input_file, output_file, key):
    cipher = AES.new(key, AES.MODE_CBC)
    iv = cipher.iv

    with open(input_file, 'rb') as f:
        plaintext = f.read()
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))

    with open(output_file, 'wb') as f:
        f.write(iv + ciphertext)

def encrypt_key_with_rsa(aes_key, public_key_file):
    with open(public_key_file, "rb") as f:
        recipient_key = RSA.import_key(f.read())
    cipher_rsa = PKCS1_OAEP.new(recipient_key)
    encrypted_key = cipher_rsa.encrypt(aes_key)
    with open("key.bin", "wb") as f:
        f.write(encrypted_key)

def main():
    # Step 1: Zip the folder
    zip_path = "collected.zip"
    zip_folder("collected_files", zip_path)
    # Step 2: AES key generation
    aes_key = get_random_bytes(16)

    # Step 3: Encrypt the zip file
    encrypt_file(zip_path, "files.log", aes_key)

    # Step 4: Encrypt AES key with RSA
    encrypt_key_with_rsa(aes_key, "rsa_public.pem")

    # Step 5: Clean up
    os.remove(zip_path)
    print("Encryption complete. Encrypted output saved as 'files.log'.")

if __name__ == "__main__":
    main()
