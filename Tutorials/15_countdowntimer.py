import time

# time.sleep(n) pauses the program for n seconds

# basic delay example
# time.sleep(3)
# print("Hello world after 3 sec, did u miss me already?")

# simple countdown - just numbers
# my_time = int(input("Enter the time in seconds: "))
# for x in range(my_time, 0, -1):
#     print(x)
#     time.sleep(1)
# print("TIME'S UP!")

# formatted countdown - HH:MM:SS
my_time = int(input("Enter the time in seconds: "))

for x in range(my_time, 0, -1):
    seconds = x % 60          # remainder after removing full minutes
    minutes = (x // 60) % 60  # remainder after removing full hours
    hours   = x // 3600       # total full hours, // gives int directly, no typecast needed

    print(f"{hours:02}:{minutes:02}:{seconds:02}")  # :02 ensures 2 digits, pads with 0
    time.sleep(1)

print("Time's UP!")

# basic CP usage (optional)
# time.sleep() is rarely used in CP
# but the HH:MM:SS conversion logic is common in time-based problems
# seconds to H:M:S breakdown:
# h = total_seconds // 3600
# m = (total_seconds % 3600) // 60
# s = total_seconds % 60