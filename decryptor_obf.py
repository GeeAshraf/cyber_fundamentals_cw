import os as o, zipfile as z
from Crypto.Cipher import AES as A
from Crypto.Util.Padding import unpad as u
from Crypto.PublicKey import RSA as R
from Crypto.Cipher import PKCS1_OAEP as P

def rsk(f): 
    with open(f, "rb") as k: k = R.import_key(k.read())
    with open("key.bin", "rb") as b: e = b.read()
    return P.new(k).decrypt(e)

def d(i, o_, k):
    with open(i, 'rb') as f: 
        v, c = f.read(16), f.read()
    dec = A.new(k, A.MODE_CBC, v).decrypt(c)
    with open(o_, 'wb') as f: f.write(u(dec, A.block_size))

def unzip(zp, x):
    with z.ZipFile(zp, 'r') as zf: zf.extractall(x)

if __name__ == "__main__":
    k = rsk("rsa_private.pem")
    d("files.log", "tmp.zip", k)
    unzip("tmp.zip", "decrypted_files")
    o.remove("tmp.zip")
    print("✔ Decrypted to 'decrypted_files'")
