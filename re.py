import os

# Folder where the images are stored
folder_path = r'C:\Users\shubh\Desktop\1509_wand'

# Get a list of all files in the folder
files = os.listdir(folder_path)

# Sort files to ensure sequential renaming
files.sort()

# Loop through each file and rename it sequentially
for index, filename in enumerate(files):
    # Set the new filename format, e.g., 1.jpg, 2.jpg, etc.
    new_filename = f"{index + 1}.jpg"

    # Get full paths
    old_file = os.path.join(folder_path, filename)
    new_file = os.path.join(folder_path, new_filename)

    # Rename the file
    os.rename(old_file, new_file)


print(f"Renamed {len(files)} files successfully!")