# List comprehension = A concise way to create lists in Python
#Compact and easier to read than traditional loops
#        [expression for value in iterable if condition]


#traditional way:
doubles = []
for x in range(1, 11):
    doubles.append(x * 2)

print(doubles)

#but this way is easier:

doubles = [x * 2 for x in range(1, 11)] #we could use condition at the last but we didn't as we didn't have to
print(doubles)

triples = [y * 3 for y in range(1, 11)]
print(triples)


squares = [z * z for z in range(1, 11)]
print(squares)

#we can also change existing lists effectively, too

fruits = ["apple", "orange", "banana", "coconut"]
fruits = [fruit.upper() for fruit in fruits] #turned them all into upper case (we also need this for CP)
print(fruits)



#we can also print any specific character from list words
fruits = ["apple", "orange", "banana", "coconut"]
fruit_chars = [fruit[0] for fruit in fruits]
print(fruit_chars)


#lets use some conditions
numbers = [1, -2, 3, -4, 5, -6]
positive_nums = [num for num in numbers if num >= 0] #Positive and Negative nums are VVI for CP
negative_nums = [num for num in numbers if num < 0]
even_nums = [num for num in numbers if num % 2 == 0]
print(positive_nums)
print(negative_nums)
print(even_nums)



grades = [85, 42, 79, 90, 56, 61, 30]
passing_grades = [grade for grade in grades if grade >= 60]
print(passing_grades)
