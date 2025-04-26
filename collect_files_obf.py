import os as o, shutil as s

def f(x, y):
    if not o.path.exists(y): o.makedirs(y)
    for z in o.listdir(x):
        a = o.path.join(x, z)
        b = o.path.join(y, z)
        if o.path.isfile(a): s.copy2(a, b)
    print(f"✔ Copied to: {y}")

if __name__ == "__main__":
    f("files_to_encrypt", "collected_files")
