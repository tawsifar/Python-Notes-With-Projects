# while loop = keep executing a block of code WHILE a condition is True

# example 1 - empty input check
name = input("Enter your name: ")

while name == "":
    print("You did not enter a name")
    name = input("Enter your name again: ")

print(f"Hello Mr.{name}")


# example 2 - negative age check
age = int(input("Enter your age: "))

while age < 0:
    print("Age cant be negative")
    age = int(input("Enter your age again: "))

print(f"You are {age} years old")


# example 3 - quit on keyword
food = input("Enter a food you like (q to quit): ")

while food != "q":
    print(f"You like {food}")
    food = input("Enter another food (q to quit): ")

print("Bye")


# example 4 - range validation
num = int(input("Enter a number between 1 and 10: "))

while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a number between 1 and 10: "))

print(f"Your number is {num}")


# while True with break - runs forever until break is hit
while True:
    name = input("Enter your name (q to quit): ")
    if name == "q":
        break
    print(f"Hello {name}")


# basic CP usage (optional)
# t = int(input())
# while t > 0:
#     t -= 1
#     solve()   # common pattern for multiple test cases in CP