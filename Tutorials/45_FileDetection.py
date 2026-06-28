# Python file detection
# os module lets you interact with the operating system: paths, files, directories

import os

file_path = r'C:\Users\T4WSIF\Desktop\PyNotes\Tutorials\test.txt'  # file in the same folder, no need for full path

# os.path.exists() checks if the path exists at all, file or folder
if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")

    # os.path.isfile() checks if it is specifically a file
    if os.path.isfile(file_path):
        print("That is a file")

        # os.path.getsize() returns size in bytes
        size = os.path.getsize(file_path)
        print(f"File size: {size} bytes")

        # os.path.abspath() gives the full absolute path
        print(f"Full path: {os.path.abspath(file_path)}")

        # os.path.splitext() splits name and extension into a tuple
        name, extension = os.path.splitext(file_path)
        print(f"File name: {name}")
        print(f"File extension: {extension}")

    # os.path.isdir() checks if it is specifically a directory/folder
    elif os.path.isdir(file_path):
        print("That is a directory")

        # os.listdir() lists everything inside the folder(try this with a folder path instead of a file path)
        contents = os.listdir(file_path)
        print(f"Contents: {contents}")

        # os.path.join() safely builds a path for any OS (windows/mac/linux) by joining parts together with the correct separator
        for item in contents:
            full_item_path = os.path.join(file_path, item)
            if os.path.isfile(full_item_path):
                print(f"  file      -> {item}")
            elif os.path.isdir(full_item_path):
                print(f"  directory -> {item}")

else:
    print(f"The location '{file_path}' doesn't exist")

# output if test.txt exists and has some content:
# The location 'test.txt' exists
# That is a file
# File size: 42 bytes
# Full path: C:/Users/HP/Desktop/test.txt
# File name: test
# File extension: .txt