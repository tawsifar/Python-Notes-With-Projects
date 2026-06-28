
name = input("Enter your full name: ")  # example: John Doe

# length
print(len(name))          # 8 - counts all characters including space

# finding
print(name.find("o"))     # 1 - first occurrence index, -1 if not found
print(name.rfind("o"))    # 5 - last occurrence index, -1 if not found

# case methods
print(name.capitalize())  # John doe - only first letter upper, rest lower
print(name.upper())       # JOHN DOE
print(name.lower())       # john doe
print(name.title())       # John Doe - first letter of each word upper
print(name.swapcase())    # jOHN dOE - flips each letter's case

# checking methods - all return True or False
print(name.isdigit())     # False - checks if all characters are digits
print(name.isalpha())     # False - space fails this check
print(name.isalnum())     # False - space fails this check
print(name.isspace())     # False
print(name.isupper())     # False
print(name.islower())     # False
print(name.istitle())     # True

# stripping whitespace
messy = "   hello   "
print(messy.strip())      # "hello"     - both sides
print(messy.lstrip())     # "hello   "  - left side only
print(messy.rstrip())     # "   hello"  - right side only

# splitting and joining
sentence = "john doe smith"
words = sentence.split(" ")   # splits by space into a list
print(words)                  # ['john', 'doe', 'smith']
print("-".join(words))        # john-doe-smith
print(" ".join(words))        # john doe smith

# starts/ends with
print(name.startswith("John"))   # True
print(name.endswith("Doe"))      # True

# count and replace
ph_num1 = "123-45-61"
print(ph_num1.count("1"))           # 3 - how many times "1" appears
print(ph_num1.replace("1", "9"))    # 923-45-69 - replaces all "1" with "9"

# count works on list and tuple too
ph_num2 = [1, 2, 3, 4, 5, 6, 1]
print(ph_num2.count(1))             # 2

ph_num3 = (1, 2, 3, 4, 5, 6, 1)
print(ph_num3.count(1))             # 2

# for integers, convert to string first
ph_num4 = 12345161
print(str(ph_num4).count("1"))          # 3
print(str(ph_num4).replace("1", "9"))   # 92345969

# formatting
age = 20
print(f"My name is {name} and I am {age} years old")           # f-string, recommended
print("My name is {} and I am {} years old".format(name, age)) # .format() older style
print(f"Pi is {3.14159:.2f}")     # Pi is 3.14 - 2 decimal places
print(f"Score: {95.678:.1f}")     # Score: 95.7

# padding and alignment
print("hello".center(11))         # "   hello   " - centered in 11 chars
print("hello".ljust(11, "-"))     # "hello------" - left aligned, fill with -
print("hello".rjust(11, "-"))     # "------hello" - right aligned, fill with -
print(f"{'Tawsif':^20}")          # centers Tawsif in 20 chars using f-string
print(f"{'CUET':>20}")            # right aligns CUET in 20 chars
print(f"{'CSE':<20}")             # left aligns CSE in 20 chars

# Basic CP tricks:
# s = input().strip()              # always strip input in CP to avoid whitespace issues(VVI)
# words = input().split()          # split by any whitespace without specifying separator
# if s.isdigit(): n = int(s)       # safe conversion check before casting

# "".join(reversed(s))             # reverse a string -But we do also have a better way, lets demonstrate that below:
'''
s = "Tawsif"
print("".join(reversed(s)))   # fiswaT

# reversed() returns an iterator, join() combines it back into a string
# shorter way using slicing:
print(s[::-1])   # fiswaT : slicing trick, start:stop:step where -1 means go backward

'''


