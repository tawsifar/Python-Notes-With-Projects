# dictionary and set comprehension
# same idea as list comprehension but for dict and set
# dict format: {key: value for item in iterable if condition}
# set format:  {expression for item in iterable if condition}


# DICTIONARY COMPREHENSION

# traditional way
squares_dict = {}
for x in range(1, 6):
    squares_dict[x] = x * x
print(squares_dict)   # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# comprehension way
squares_dict = {x: x * x for x in range(1, 6)}
print(squares_dict)   # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# with condition
even_squares = {x: x * x for x in range(1, 11) if x % 2 == 0}
print(even_squares)   # {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}

# transforming an existing dictionary
grades = {"Tawsif": 95, "Rahim": 80, "Karim": 55, "Nadia": 70}

# filter passing students only
passing = {name: grade for name, grade in grades.items() if grade >= 60}
print(passing)   # {'Tawsif': 95, 'Rahim': 80, 'Nadia': 70}

# add grade letter to each
def get_letter(g):
    return "A" if g >= 90 else "B" if g >= 75 else "C" if g >= 60 else "F"

with_letters = {name: get_letter(grade) for name, grade in grades.items()}
print(with_letters)   # {'Tawsif': 'A', 'Rahim': 'B', 'Karim': 'F', 'Nadia': 'C'}

# swapping keys and values
flipped = {value: key for key, value in grades.items()}
print(flipped)   # {95: 'Tawsif', 80: 'Rahim', 55: 'Karim', 70: 'Nadia'}


# SET COMPREHENSION

# traditional way
unique_squares = set()
for x in [1, 2, 2, 3, 3, 4]:
    unique_squares.add(x * x)
print(unique_squares)   # {1, 4, 9, 16}

# comprehension way - duplicates automatically removed
unique_squares = {x * x for x in [1, 2, 2, 3, 3, 4]}
print(unique_squares)   # {1, 4, 9, 16}

# with condition
nums = [1, -2, 3, -4, 5, -6, 3, 5]
positive_unique = {x for x in nums if x > 0}
print(positive_unique)   # {1, 3, 5} - unique positives only

# basic CP usage (optional)
# freq = {x: nums.count(x) for x in set(nums)}  # frequency dict in one line
# seen = {x for x in arr if arr.count(x) > 1}   # elements that appear more than once