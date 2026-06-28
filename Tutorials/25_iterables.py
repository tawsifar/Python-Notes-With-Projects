# iterable = any object that can return its elements one at a time
# lists, tuples, strings, sets, dictionaries are all iterables

# list iteration
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)

# backwards iteration
for number in reversed(numbers):   # works for list and tuple, not set
    print(number)

# with index using enumerate
for index, number in enumerate(numbers):
    print(f"{index}: {number}")    # 0: 1, 1: 2 ...

# string iteration - every character is an element
name = "Tawsif Azam"
for character in name:
    print(character, end="")   # prints on same line
print()                        # new line after

# tuple iteration - same as list
coords = (10, 20, 30)
for coord in coords:
    print(coord)

# set iteration - unordered, cant reverse
skills = {"Python", "C++", "DSA"}
for skill in skills:
    print(skill)   # order changes every run

# dictionary iteration
my_dictionary = {"A": 1, "B": 2, "C": 3}

# keys only - default when looping a dict
for key in my_dictionary:
    print(key)

# values only
for value in my_dictionary.values():
    print(value)

# keys and values together
for key, value in my_dictionary.items():
    print(f"{key} = {value}")

