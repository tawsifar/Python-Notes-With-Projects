# 08_IfElseCondition.py

# integer condition
a = int(input("Enter your age: "))

if a >= 18:
    print("Welcome")
elif a < 0:
    print("Enter a valid age!")
else:
    print("Get lost, kid")


# string condition
p = input("Do you want to proceed? (Y/N): ")

if p == "Y":
    print("Welcome again")
elif p == "":          # catches empty input, user just pressed enter
    print("Write something mann!")
else:
    print("Get lost again")


# boolean condition
online = True

if online:
    print("The user is online")
else:
    print("The user is offline")


