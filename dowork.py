import zipfile
import os

# Unzipping a file
def unzip_file(zip_path, extract_path):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)

# Zipping a folder
def zip_folder(folder_path, zip_path):
    with zipfile.ZipFile(zip_path, 'w') as zip_ref:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                zip_ref.write(file_path, os.path.relpath(file_path, folder_path))

# 第一步，解压slpk文件
# zip_path='./data/lmsinr.slpk'
# extract_path = './temp/lmsinr'
# unzip_file(zip_path, extract_path)

# 第二步，设置移动向量，移动slpk
normal = {
    'x': 0,
    'y': 0,
    'z': 0
}

# 改变nodes文件夹里的每个数字文件夹的features文件夹下的0.json.gz文件

# # 最后一步，将解压后的文件夹打包为slpk文件
# new_slpk_path = './temp/lmsinr2.slpk'
# zip_folder(extract_path, zip_path)