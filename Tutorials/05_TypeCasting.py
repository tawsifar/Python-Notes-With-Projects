
# converting a variable from one data type to another

age = 3.5   # float
print(int(3.5))    # 3 - decimal part is cut off, not rounded

# float to int always truncates (floors toward zero)
print(int(-3.9))   # -3, not -4

# number to string
age1 = 25
age1 = str(age1)
print(age1 + "1")  # "251" - string concatenation, not math

# string to int/float (only works if the string actually contains a number)
num = "42"
print(int(num) + 1)    # 43
# print(int("hello"))  # ValueError - cant convert non-numeric string

# bool conversion
# empty string, 0, None, empty list = False
# anything with a value = True
name = "Tawsif"
print(bool(name))   # True
print(bool(""))     # False
print(bool(0))      # False
print(bool(42))     # True

# Basic CP trick 
# input always returns a string, so typecast immediately
# n = int(input())
