# file_organizer.py
import os, shutil

folder = input("Enter folder path: ")

for file in os.listdir(folder):
    ext = file.split('.')[-1]
    dest_folder = os.path.join(folder, ext)
    os.makedirs(dest_folder, exist_ok=True)
    shutil.move(os.path.join(folder, file), os.path.join(dest_folder, file))

print("📁 Files organized by type!")
