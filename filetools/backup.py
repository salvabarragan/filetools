import os


def backup(where, file=None, folder=None):
    if (file is None and folder is None) or (file and folder):
        raise ValueError("You must specify either a file or a folder, but not both or neither.")
    elif file:
        if not os.path.exists(file):
            raise FileNotFoundError(f"The file does not exist: {file}")
        if not os.path.exists(where):
            os.makedirs(where)
        filename = os.path.basename(file)
        dest_path = os.path.join(where, filename)
        with open(file, "rb") as src, open(dest_path, "wb") as dst:
            dst.write(src.read())
    elif folder:
        if not os.path.exists(folder):
            raise FileNotFoundError(f"The folder does not exist: {folder}")
        foldername = os.path.basename(folder)
        if not os.path.exists(os.path.join(where, foldername)):
            os.makedirs(os.path.join(where, foldername))
        folder_files = os.listdir(folder)
        for file in folder_files:
            current_file = os.path.join(folder, file)
            dest_path = os.path.join(where, foldername, file)
            with open(current_file, "rb") as src, open(dest_path, "wb") as dst:
                dst.write(src.read())
                