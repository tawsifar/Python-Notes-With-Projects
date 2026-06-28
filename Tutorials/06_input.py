# input() always returns a string, typecast if you need a number

name = input("What is your name?: ")
age = int(input("How old are you?: "))  # typecast to int so math works
age = age + 3
print(f"Hello {name}! you are {age} years old")

# float input
gpa = float(input("Enter your GPA: "))
print(f"GPA: {gpa}")

# Basic CP tricks (VVI) :

# now we know that for single integer
# n = int(input())

# But we must know this for cp too:
# multiple integers in one line
# a, b = map(int, input().split())

# whole line as list of integers
# arr = list(map(int, input().split()))

# n integers each on a new line
# arr = [int(input()) for _ in range(n)] 
#the above one is same as writing :
# arr = []
# for _ in range(n):
#     arr.append(int(input()))