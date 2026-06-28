import json
import csv

# .txt — reads the entire file content as one big string
file_path = "C:\\Users\\T4WSIF\\Desktop\\PyNotes\\output.txt"

try:
    with open(file_path, 'r') as file:
        content = file.read()   # reads everything at once into a single string
        print(content)

        # alternatives:
        # file.readline()    reads one line at a time
        # file.readlines()   reads all lines and returns them as a list
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to read that file")


# .json — reads JSON file and converts it directly into a Python dict or list
file_path = "C:\\Users\\T4WSIF\\Desktop\\PyNotes\\output.json"

try:
    with open(file_path, 'r') as file:
        # json.load() parses the file and returns a Python object (dict, list, etc)
        # json.loads() does the same but takes a string instead of a file
        content = json.load(file)
        print(content)

        # access specific fields like a normal dict after loading
        # print(content["name"])
        # print(content["age"])
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to read that file")


# .csv — reads comma separated values line by line
file_path = "C:\\Users\\T4WSIF\\Desktop\\PyNotes\\output.csv"

try:
    with open(file_path, 'r') as file:
        # csv.reader() returns an iterable reader object, not the full content at once
        # each iteration gives one row as a list of strings
        content = csv.reader(file)

        for line in content:
            print(line)   # each line prints as a list e.g. ['Spongebob', '30', 'Cook']

        # to skip the header row and only read data:
        # next(content)   <- skips first row
        # for line in content:
        #     print(line)
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to read that file")