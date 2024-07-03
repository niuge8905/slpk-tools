import zipfile
import os
import json
import gzip

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
zip_path='./data/test01.slpk'
extract_path = './temp/test01'
# unzip_file(zip_path, extract_path)

# 第二步，设置移动向量，改移动slpk
normal = {
    'x': 1000,
    'y': 1000,
    'z': 0
}

# 改变nodes文件夹里的每个数字文件夹的features文件夹下的0.json.gz文件
# 改变里面的geometryData下的transformation第12、13、14个数字，分别代表x、y、z方向的移动
nodes_path = os.path.join(extract_path, 'nodes')
for root, dirs, files in os.walk(nodes_path):
    for file in files:
        if file == '0.json.gz' and root.find('features')!=-1:
            file_path = os.path.join(root, file)
            #with open(file_path, 'r') as f:
            with gzip.open(file_path, 'rt') as f:
                data = json.load(f)
                for i in range(len(data['geometryData'])):
                    data['geometryData'][i]['transformation'][12] += normal['x']
                    data['geometryData'][i]['transformation'][13] += normal['y']
                    data['geometryData'][i]['transformation'][14] += normal['z']
            with gzip.open(file_path, 'wt') as f:
                json.dump(data, f)

# 最后一步，将解压后的文件夹打包为slpk文件
new_slpk_path = './temp/test2.slpk'
zip_folder(extract_path, new_slpk_path)