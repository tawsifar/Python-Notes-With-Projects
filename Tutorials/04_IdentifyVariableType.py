

Age = 3.5 #lol
page = 12
name = "tawsif"

print(type(Age))    # <class 'float'>
print(type(page))   # <class 'int'>
print(type(name))   # <class 'str'>

# you can also check type directly without a variable
print(type(True))   # <class 'bool'>
print(type(None))   # <class 'NoneType'>

# isinstance() checks if a variable is a specific type, returns True or False
# more useful than type() when doing validation
print(isinstance(Age, float))   # True
print(isinstance(page, int))    # True
print(isinstance(name, str))    # True