# membership operators = check if a value exists in a sequence
# works with strings, lists, tuples, sets, dictionaries
# 1. in
# 2. not in

# string membership
word = "APPLE"
letter = input("Guess a letter in the secret word: ")

if letter in word:
    print(f"There is a {letter}")
else:
    print(f"{letter} was not found")

# not in
if letter not in word:
    print(f"{letter} was not found")
else:
    print(f"There is a {letter}")


# list membership
cuet_depts = ["CSE", "EEE", "ME", "CE"]
dept = input("Enter a department: ")

if dept in cuet_depts:
    print(f"{dept} exists in CUET")
else:
    print(f"{dept} not found")


# dictionary membership - checks keys by default
grades = {"Sandy":    "A",
          "Squidward": "B",
          "Spongebob": "C",
          "Patrick":   "D"}

student = input("Enter the name of a student: ")

if student in grades:
    print(f"{student}'s grade is {grades[student]}")
else:
    print(f"{student} was not found")

# checking values instead of keys
if "A" in grades.values():
    print("Someone got an A")


# email validation using membership
email = "tawsif@cuet.ac.bd"
if "@" in email and "." in email:
    print("Valid email")
else:
    print("Invalid email")


# membership with not in for cleaner conditions
banned = ["spam", "bot", "hack"]
username = input("Enter username: ")

if username not in banned:
    print(f"Welcome {username}")
else:
    print("That username is not allowed")

