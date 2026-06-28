# default arguments = a default value for certain parameters
# used when that argument is omitted during the function call
# order: 1. positional  2. default  3. keyword  4. arbitrary

def net_price(list_price, discount=0, tax=0.05):
    return list_price * (1 - discount) * (1 + tax)

# only list_price given, discount=0 and tax=0.05 used as defaults
print(net_price(500))           # 525.0

# discount overridden, tax still defaults to 0.05
print(net_price(500, 0.1))      # 472.5

# all arguments provided, no defaults used
print(net_price(500, 0.1, 0))   # 450.0

# keyword arguments - pass by name, order doesnt matter
print(net_price(500, tax=0.1))          # 550.0 - skipped discount, named tax
print(net_price(list_price=500, tax=0, discount=0.2))  # 400.0


import time

def count(start, end, step=1):   # step has a default of 1
    for x in range(start, end + 1, step):  # end+1 so last number is included
        print(x)
        time.sleep(0.5)
    print("DONE!")

count(0, 5)         # 0 1 2 3 4 5
count(0, 10, 2)     # 0 2 4 6 8 10 - custom step


# default args are useful for optional behavior
def greet(name, msg="Welcome to CUET!"):
    print(f"{name}: {msg}")

greet("Tawsif")                  # Tawsif: Welcome to CUET!
greet("Tawsif", "Let's code!")   # Tawsif: Let's code!

# basic CP usage (optional)
# def solve(n, mod=1000000007):
#     return (n * (n + 1) // 2) % mod
# default mod saves from passing it every call