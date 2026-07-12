# Importing required modules
import os
import shutil

# Folder path which we want to organize
path = r"D:\File Organizer"

# Getting all files and folders from the directory
files = os.listdir(path)

# Dictionary for file extensions and their folder names
folders = {

    # Image files
    ".jpg": "Images",
    ".png": "Images",
    ".jpeg": "Images",

    # Video files
    ".mp4": "Videos",

    # Document files
    ".pdf": "Documents",
    ".docx": "Documents",

    # Audio files
    ".mp3": "Audio",

    # Application files
    ".exe": "Applications",
    ".msi": "Applications",

    # Other files
    ".zip": "Other Files",
    ".py": "Other Files"
}

# Looping through all files
for file in files:

    # Creating full path of the file
    source_path = os.path.join(path, file)

    # Skip folders
    if os.path.isdir(source_path):
        continue

    # Getting file extension
    # .lower() converts extension to lowercase
    extension = os.path.splitext(file)[1].lower()

    # Checking if extension exists in dictionary
    if extension in folders:

        # Getting folder name from dictionary
        folder_name = folders[extension]

        # Creating destination folder path
        destination_folder = os.path.join(path, folder_name)

        # Creating folder if it does not exist
        os.makedirs(destination_folder, exist_ok=True)

        # Creating final destination path
        destination_path = os.path.join(destination_folder, file)

        # Prevent duplicate file error
        if os.path.exists(destination_path):
            print(file, "already exists")
            continue

        # Moving file to destination folder
        shutil.move(source_path, destination_path)

        # Success message
        print(f"{file} moved to {folder_name} folder")

    else:
        # If file type is not supported
        print(file, "type not supported")
