# Decorator = a function that wraps another function
# adds extra behavior before or after the original function runs
# without changing the original function itself
# works by passing the original function as an argument to the decorator

# *args and **kwargs are used in the wrapper so it can accept
# any arguments that the original function expects
# without them, the decorator would break if the wrapped function takes parameters

def add_sprinkles(func):
    # wrapper is the new function that replaces the original
    # it runs extra code then calls the original func inside
    def wrapper(*args, **kwargs):
        print("*You add sprinkles*")
        func(*args, **kwargs)   # calls the original function with its original arguments
    return wrapper              # returns wrapper, not wrapper() — we return the function itself, not its result


def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("*You add fudge*")
        func(*args, **kwargs)
    return wrapper


# stacking decorators — applied bottom up, executed top down
# @add_fudge wraps get_ice_cream first
# @add_sprinkles then wraps the already-fudged version
# so when called: sprinkles runs first, then fudge, then the original
@add_sprinkles
@add_fudge
def get_ice_cream(flavor):
    print(f"Here is your {flavor} ice cream")


get_ice_cream("vanilla")
# *You add sprinkles*
# *You add fudge*
# Here is your vanilla ice cream


# what @add_sprinkles @add_fudge actually does behind the scenes:
# get_ice_cream = add_sprinkles(add_fudge(get_ice_cream))
# the @ syntax is just a cleaner way to write that


# practical example — a decorator that measures how long a function takes
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
    return wrapper


@timer
def make_pasta():
    time.sleep(1)   # simulates a slow task
    print("Pasta is ready")


make_pasta()
# Pasta is ready
# make_pasta took 1.001 seconds


# decorator with a return value
# if the original function returns something, wrapper must return it too
# otherwise the result gets swallowed and None comes back

def shout(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)  # capture the return value
        return result.upper()           # modify and return it
    return wrapper


@shout
def greet(name):
    return f"hello {name}"


print(greet("Tawsif"))   # HELLO TAWSIF