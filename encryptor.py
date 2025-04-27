import os
import zipfile
from cryptography.hazmat.primitives import padding as sym_padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding as rsa_padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes

def zip_folder(folder_path, zip_path):
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(folder_path):
            for file in files:
                full_path = os.path.join(root, file)
                arcname = os.path.relpath(full_path, folder_path)
                zipf.write(full_path, arcname)

def encrypt_file(input_file, output_file, key):
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    with open(input_file, 'rb') as f:
        data = f.read()

    padder = sym_padding.PKCS7(128).padder()
    padded_data = padder.update(data) + padder.finalize()
    encrypted = encryptor.update(padded_data) + encryptor.finalize()

    with open(output_file, 'wb') as f:
        f.write(iv + encrypted)

def encrypt_key_with_rsa(aes_key, public_key_file):
    with open(public_key_file, 'rb') as f:
        public_key = serialization.load_pem_public_key(f.read(), backend=default_backend())

    encrypted_key = public_key.encrypt(
        aes_key,
        rsa_padding.OAEP(
            mgf=rsa_padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    with open("key.bin", "wb") as f:
        f.write(encrypted_key)

def main():
    # Step 1: Zip the folder
    zip_path = "collected.zip"
    zip_folder("collected_files", zip_path)

    # Step 2: AES key generation
    aes_key = os.urandom(32)  # AES-256

    # Step 3: Encrypt the zip file
    encrypt_file(zip_path, "files.log", aes_key)

    # Step 4: Encrypt AES key with RSA public key
    encrypt_key_with_rsa(aes_key, "rsa_public.pem")

    # Step 5: Clean up
    os.remove(zip_path)
    print("Encryption complete. Encrypted output saved as 'files.log'.")

if __name__ == "__main__":
    main()
