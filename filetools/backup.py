import os


def backup(file, where):
    if not os.path.exists(file):
        raise FileNotFoundError(f"El archivo origen no existe: {file}")
    if not os.path.exists(where):
        os.makedirs(where)
    filename = os.path.basename(file)
    dest_path = os.path.join(where, filename)
    with open(file, "rb") as src, open(dest_path, "wb") as dst:
        dst.write(src.read())
