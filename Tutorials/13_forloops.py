# for loops = execute a block of code a fixed number of times
# can iterate over a range, string, list, tuple, etc.

for i in range(5): #range(stop)           -> start=0, step=1   gives 0 to stop-1
    print(i)  # 0 1 2 3 4
# basic range loop - range(start, stop) stop is excluded
for i in range(1, 11):    # 1 to 10
    print(i)

# reversed range
for i in reversed(range(1, 11)):   # 10 to 1
    print(i)

# range with step backwards - range(start, stop, step)
for i in range(11, 1, -1):   # 11 to 2, step -1
    print(i)

# range with custom step
for i in range(1, 11, 3):    # 1, 4, 7, 10
    print(i)

# iterating over a string
cc = "019-271-992"
for x in cc:
    print(x)   # prints each character one by one

# iterating over a list
cuet_depts = ["CSE", "EEE", "ME", "CE"]
for dept in cuet_depts:
    print(dept)

# continue - skips current iteration and moves to next
for i in range(1, 11):
    if i == 3:
        continue    # skips 3, keeps going
    print(i)

# break - stops the loop entirely
for i in range(1, 11):
    if i == 3:
        break       # stops at 3, never reaches 4-10
    print(i)

# enumerate - gives index and value at the same time
names = ["Tawsif", "Rahim", "Karim"]
for index, name in enumerate(names):
    print(index, name)   # 0 Tawsif, 1 Rahim, 2 Karim

# basic CP usage (optional)
# for _ in range(n):          # _ means we dont need the loop variable
#     val = int(input())
# for i in range(0, n, 2):    # even indices only
# for i in range(n-1, -1, -1): # reverse loop from n-1 to 0