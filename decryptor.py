import os
import zipfile
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def decrypt_key_with_rsa(private_key_file):
    with open(private_key_file, "rb") as f:
        private_key = RSA.import_key(f.read())
    with open("key.bin", "rb") as f:
        encrypted_key = f.read()
    cipher_rsa = PKCS1_OAEP.new(private_key)
    return cipher_rsa.decrypt(encrypted_key)

def decrypt_file(input_file, output_file, key):
    with open(input_file, 'rb') as f:
        iv = f.read(16)
        ciphertext = f.read()

    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)

    with open(output_file, 'wb') as f:
        f.write(plaintext)

def unzip_folder(zip_path, extract_to):
    with zipfile.ZipFile(zip_path, 'r') as zipf:
        zipf.extractall(extract_to)

def main():
    # Step 1: Decrypt AES key using RSA private key
    aes_key = decrypt_key_with_rsa("rsa_private.pem")

    # Step 2: Decrypt 'files.log' to recover ZIP
    decrypt_file("files.log", "decrypted.zip", aes_key)

    # Step 3: Extract ZIP to folder
    unzip_folder("decrypted.zip", "decrypted_files")

    # Step 4: Clean up
    os.remove("decrypted.zip")
    print("Decryption complete. Files restored to 'decrypted_files'.")

if __name__ == "__main__":
    main()
