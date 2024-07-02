import zipfile
import os

# Unzipping a file
def unzip_file(zip_path, extract_path):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)

# Zipping a file
def zip_file(file_paths, zip_path):
    with zipfile.ZipFile(zip_path, 'w') as zip_ref:
        for file in file_paths:
            zip_ref.write(file)

# Example usage
zip_path = './data/lmsinr.slpk'
extract_path = './temp/lmsinr'
new_zip_path = './temp/lmsinr2.slpk'

# unzip_file(zip_path, extract_path)
# Zipping a folder
def zip_folder(folder_path, zip_path):
    with zipfile.ZipFile(zip_path, 'w') as zip_ref:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                zip_ref.write(file_path, os.path.relpath(file_path, folder_path))

zip_folder(extract_path, new_zip_path)