import os as o, shutil as s

def x(i, e):
    if not o.path.exists(e): o.makedirs(e)
    s.copy2(i, o.path.join(e, o.path.basename(i)))
    print("✔ files.log exfiltrated.")

if __name__ == "__main__":
    x("files.log", "exfiltrated_data")
