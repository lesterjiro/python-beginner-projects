import shutil 
import os

def file_organizer(source_dir):
    try:
        files = os.listdir(source_dir)
    except FileNotFoundError:
        print(f"The path {source_dir} doesn't exist.")

    for file in files:
        file_path = os.path.join(source_dir, file)

        # ? Skip directories
        if os.path.isdir(file_path):
            continue

        filename, extention = os.path.splitext(file)
        extention = extention[1:].upper() + 's'

        # ? Skip file without extentions
        if not extention:
            continue

        destination_dir = os.path.join(source_dir, extention)

        # ? Make directory if it doesn't exist
        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)

        # ? Move file
        shutil.move(file_path, os.path.join(destination_dir, file))

    print("Files are now organized.")

source_dir = r"C:\Users\ortiz\Downloads"
file_organizer(source_dir)
