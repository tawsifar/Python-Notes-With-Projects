# Python can write to different file formats
# 'w' mode creates the file if it doesnt exist, or overwrites it if it does
# 'with' statement automatically closes the file when the block ends
# no need to call file.close() manually


# .txt — plain text, simplest format, just writes a string directly
txt_data = "I like pizza!"
file_path = "test.txt"

try:
    with open(file_path, 'w') as file:
        file.write(txt_data)  # writes the string as-is into the file
        print(f".txt file '{file_path}' has been created successfully")
except FileExistsError:
    print("That file already exists")

# note: 'w' mode actually never raises FileExistsError because it overwrites
# to truly prevent overwriting use 'x' mode instead — it throws FileExistsError if file exists
# with open(file_path, 'x') as file: <- safer if you dont want to overwrite


# .json — structured data format, commonly used for APIs and config files
import json

employee = {
    "name": "Spongebob",
    "age": 30,
    "job": "Cook"
}

file_path = "output.json"

try:
    with open(file_path, 'w') as file:
        # json.dump() converts the Python dict to JSON format and writes it to the file
        # indent=4 makes the output human readable with 4 space indentation
        # without indent it would all be on one line
        json.dump(employee, file, indent=4)

    print(f"JSON file '{file_path}' has been created successfully")
except FileExistsError:
    print("That file already exists!")

# output.json will look like:
# {
#     "name": "Spongebob",
#     "age": 30,
#     "job": "Cook"
# }


# .csv — spreadsheet style data, rows and columns separated by commas
import csv

# each inner list is one row, first row is the header
employees = [["Name", "Age", "Job"],
             ["Spongebob", 30, "Cook"],
             ["Patrick", 37, "Unemployed"],
             ["Sandy", 27, "Scientist"]]

file_path = "output.csv"

try:
    # newline="" is required on Windows to prevent csv writer from adding extra blank lines
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)

        # writerow() writes one list as a single comma separated line
        for row in employees:
            writer.writerow(row)

        print(f"csv file '{file_path}' was created")
except FileExistsError:
    print("That file already exists!")

# output.csv will look like:
# Name,Age,Job
# Spongebob,30,Cook
# Patrick,37,Unemployed
# Sandy,27,Scientist