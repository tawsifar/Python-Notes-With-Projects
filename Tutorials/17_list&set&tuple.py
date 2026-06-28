# collection = single variable used to store multiple values
# List  = [] ordered, changeable, duplicates allowed
# Set   = {} unordered, no duplicates, can add/remove but cant change existing
# Tuple = () ordered, unchangeable, duplicates allowed, faster than list

# LIST
fruits = ["apple", "orange", "banana", "coconut"]

print(fruits[1])   # orange - index based access like C/C++

for x in fruits:   # iterate over all elements
    print(x)

print(len(fruits))          # 4 - number of elements
print("apple" in fruits)    # True - check if element exists

# changing an element
fruits[0] = "hello"         # replaces apple with hello
print(fruits)

fruits[0] = "apple"         # reset back

# adding elements
fruits.append("pineapple")  # adds to the end
fruits.insert(3, "mango")   # inserts at index 3, shifts rest right
print(fruits)

# removing elements
fruits.remove("apple")      # removes first occurrence of apple
fruits.pop()                # removes last element
fruits.pop(0)               # removes element at index 0
print(fruits)

# other useful list methods
fruits.sort()               # sorts alphabetically
fruits.reverse()            # reverses the order
print(fruits.index("banana"))  # returns index of banana
print(fruits.count("banana"))  # counts occurrences of banana
# fruits.clear()            # removes all elements

# list slicing works same as string slicing
nums = [1, 2, 3, 4, 5]
print(nums[1:4])    # [2, 3, 4]
print(nums[::-1])   # [5, 4, 3, 2, 1] - reversed list


# SET
fruitsS = {"apple", "orange", "banana", "coconut", "coconut"}  # duplicate coconut ignored
print(fruitsS)      # order changes every time, set is unordered
print(len(fruitsS)) # 4 - coconut counted once

# print(fruitsS[1]) -> TypeError, sets have no index
fruitsS.add("pineapple")     # use add() not append()
fruitsS.remove("pineapple")  # removes specific element
fruitsS.discard("mango")     # like remove() but no error if element doesnt exist
fruitsS.pop()                # removes a random(last) element since set is unordered
# fruitsS.clear()            # removes all elements

# set operations - useful for comparisons
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a | b)   # {1,2,3,4,5,6} - union, all elements
print(a & b)   # {3,4}         - intersection, common elements
print(a - b)   # {1,2}         - difference, in a but not b


# TUPLE
fruitsT = ("apple", "orange", "banana", "coconut", "coconut")  # duplicates allowed
print(len(fruitsT))             # 5
print("apple" in fruitsT)       # True
print(fruitsT.index("apple"))   # 0
print(fruitsT.count("coconut")) # 2
print(fruitsT[1])               # orange - index access works like list

# tuples are immutable - this will throw TypeError
# fruitsT[0] = "mango"   -> TypeError: tuple object does not support item assignment (but c++ does)

# when to use what
# list  -> when you need to change the data
# set   -> when you need unique values or fast lookup
# tuple -> when data should not change, or for slightly better performance

# basic CP usage (optional)
# arr = list(map(int, input().split()))   # most common way to read a list in CP
# unique = set(arr)                       # instantly remove duplicates
# if x in my_set                         # O(1) lookup, much faster than list in CP
# tuple used to store coordinates: pos = (row, col) then put in set/dict