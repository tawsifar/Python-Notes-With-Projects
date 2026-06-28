
# a variable is a named container in memory that stores a value
# rules:
# must start with a letter or underscore, not a number
# can only contain letters, numbers, and underscores
# case-sensitive: age, Age, AGE are three different variables
# cannot be a Python keyword like if, for, while, class etc

# Integer
age = 21
print(age)

# Float
price = 19.99
print(price)

# Complex
signal = 3 + 4j
print(signal)

# String
name = "Tawsif"
print(name)

# Boolean
is_student = True
print(is_student)

# List - ordered, mutable
fruits = ["apple", "banana", "mango"]
print(fruits)

# Tuple - ordered, immutable
coords = (22.35, 91.78)
print(coords)

# Set - unordered, no duplicates
skills = {"Python", "C++", "DSA"}
print(skills)

# Dictionary - key value pairs
student = {"name": "Tawsif", "dept": "CSE"}
print(student)

# multiple assignment in one line
x, y, z = 1, 2, 3
print(x, y, z)  # 1 2 3

# swap two variables without a temp variable
x, y = y, x
print(x, y)     # 2 1