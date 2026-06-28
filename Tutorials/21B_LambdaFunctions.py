# lambda = a small anonymous function defined in one line
# format: lambda parameters: expression
# useful when you need a short function without formally defining it with def

# normal function
def add(x, y):
    return x + y

print(add(3, 4))   # 7

# same thing as lambda
add = lambda x, y: x + y
print(add(3, 4))   # 7

# lambda with one parameter
square = lambda x: x * x
print(square(5))   # 25

# lambda with condition
even_odd = lambda x: "even" if x % 2 == 0 else "odd"
print(even_odd(4))   # even
print(even_odd(7))   # odd

# most common use - passing lambda as argument to another function
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# sorted() with lambda as key
print(sorted(numbers))                          # [1, 1, 2, 3, 4, 5, 6, 9]

students = [("Tawsif", 95), ("Rahim", 80), ("Karim", 90)]
print(sorted(students, key=lambda s: s[1]))     # sort by grade ascending
print(sorted(students, key=lambda s: s[1], reverse=True))  # descending

# map() - applies a function to every element
nums = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, nums))
print(squared)   # [1, 4, 9, 16, 25]

# filter() - keeps elements where function returns True
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)     # [2, 4]

# reduce() - applies function cumulatively to get a single value
from functools import reduce
total = reduce(lambda x, y: x + y, nums)
print(total)     # 15  (1+2+3+4+5)

# basic CP usage (optional)
# arr.sort(key=lambda x: x[1])         # sort list of tuples by second element
# arr.sort(key=lambda x: (-x[1], x[0]))# sort by second desc, first asc