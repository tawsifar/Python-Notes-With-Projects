# function = a block of reusable code
# defined once, called as many times as needed
# use def keyword, followed by the function name and ()

def happy_birthday(name, age):
    print(f"Happy birthday to {name}!")
    print(f"You are {age} years old!")
    print("Happy birthday to you!")
    print()

# argument order matters when calling positionally
happy_birthday("Tawsif", 20)
happy_birthday("Johan",  30)
happy_birthday("Cena",   40)

# keyword arguments - order doesnt matter if you name them
happy_birthday(age=20, name="Tawsif")


def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")

display_invoice("Tawsif", 100.01, "01/02")


# return = sends a result back to the caller and exits the function
def add(x, y):
    return x + y   # can return the expression directly without a temp variable

print(add(1, 2))   # 3


# default parameter value - used when argument is not provided
def greet(name, greeting="Hello"):
    print(f"{greeting} {name}!")

greet("Tawsif")            # Hello Tawsif!  - uses default
greet("Tawsif", "Howdy")   # Howdy Tawsif!  - overrides default


def create_name(first, last):
    first = first.capitalize()
    last  = last.capitalize()
    return first + " " + last

full_name = create_name("tawsif", "azam")
print(full_name)   # Tawsif Azam


# returning multiple values - Python returns them as a tuple
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([3, 1, 9, 2, 7])
print(low, high)   # 1 9


