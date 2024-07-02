import os

def traverse_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            print(file_path)

# Replace 'directory_path' with the path to the directory you want to traverse
directory_path = './data'
traverse_directory(directory_path)