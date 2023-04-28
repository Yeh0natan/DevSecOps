import os
import shutil

# Specify the directory to scan
dir_path = input("Enter directory path: ")

# Dictionary to store file types and corresponding folder names
file_types = {
    'png': 'Images',
    'jpg': 'Images',
    'jpeg': 'Images',
    'gif': 'Images',
    'bmp': 'Images',
    'tiff': 'Images',
    'mp4': 'Videos',
    'mkv': 'Videos',
    'avi': 'Videos',
    'mov': 'Videos',
    'wmv': 'Videos',
    'doc': 'Documents',
    'docx': 'Documents',
    'txt': 'Documents',
    "py": "Scripts"
}

# Loop through each file in the directory
for filename in os.listdir(dir_path):
    # Get the file extension
    ext = os.path.splitext(filename)[1][1:].lower()
    
    # If the file extension is in the dictionary, move the file to the corresponding folder
    if ext in file_types:
        folder_name = file_types[ext]
        folder_path = os.path.join(dir_path, folder_name)
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)
        shutil.move(os.path.join(dir_path, filename), os.path.join(folder_path, filename))
