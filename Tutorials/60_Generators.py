# generator = a function that yields values one at a time instead of returning all at once
# uses yield instead of return
# memory efficient - doesnt store all values at once, generates them on demand
# useful for large sequences you dont want to load entirely into memory

# normal function - returns all values at once as a list
def get_squares_list(n):
    result = []
    for x in range(n):
        result.append(x * x)
    return result

print(get_squares_list(5))   # [0, 1, 4, 9, 16] - all stored in memory at once

# generator function - yields one value at a time
def get_squares_gen(n):
    for x in range(n):
        yield x * x   # pauses here, returns value, resumes on next call

gen = get_squares_gen(5)
print(gen)             # <generator object> - not the values yet

print(next(gen))   # 0 - gets first value
print(next(gen))   # 1 - gets second value
print(next(gen))   # 4 - gets third value
# StopIteration error if you call next() after all values are exhausted

# iterate over generator with for loop
for val in get_squares_gen(5):
    print(val, end=" ")   # 0 1 4 9 16
print()

# convert to list if needed
print(list(get_squares_gen(5)))   # [0, 1, 4, 9, 16]

# generator expression - like list comprehension but with ()
gen_exp = (x * x for x in range(5))
print(list(gen_exp))   # [0, 1, 4, 9, 16]

# memory comparison
# list comprehension   - stores everything in memory immediately
squares_list = [x * x for x in range(1000000)]   # uses a lot of memory

# generator expression - generates values one by one, very low memory
squares_gen  = (x * x for x in range(1000000))   # barely uses any memory

# practical example - reading a huge file line by line
def read_large_file(filepath):
    with open(filepath, "r") as f:
        for line in f:
            yield line.strip()   # one line at a time, never loads whole file

# for line in read_large_file("bigfile.txt"):
#     print(line)

# infinite generator - generates values forever, you control when to stop
def count_up(start=0):
    while True:
        yield start
        start += 1

counter = count_up(1)
print(next(counter))   # 1
print(next(counter))   # 2
print(next(counter))   # 3
# never runs out, you just stop calling next()

