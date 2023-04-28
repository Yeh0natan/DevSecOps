import os
import shutil

# Step 1: Get the input directory path from the user
dir_path = "/home/yehonatan/Downloads"

# Step 2: Create a dictionary to map file extensions to folder names
ext_to_folder = {
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".bmp": "Images",
    ".mp4": "Videos",
    ".avi": "Videos",
    ".mkv": "Videos",
    ".pdf": "Documents",
    ".doc": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    ".py": "Scripts"
}

# Step 3: Loop through all the files in the directory and move them to the appropriate folder
for filename in os.listdir(dir_path):
    if os.path.isfile(os.path.join(dir_path, filename)):
        # Get the file extension
        file_ext = os.path.splitext(filename)[1].lower()
        
        # Check if the file extension is in the dictionary
        if file_ext in ext_to_folder:
            # Get the folder name for the file extension
            folder_name = ext_to_folder[file_ext]
            
            # Create the folder if it doesn't exist
            folder_path = os.path.join(dir_path, folder_name)
            if not os.path.exists(folder_path):
                os.mkdir(folder_path)
            
            # Move the file to the folder
            src_path = os.path.join(dir_path, filename)
            dst_path = os.path.join(folder_path, filename)
            shutil.move(src_path, dst_path)
