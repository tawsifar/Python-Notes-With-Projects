# *args   = arbitrary positional arguments, stored as a tuple
# **kwargs = arbitrary keyword arguments, stored as a dictionary
# order: 1. positional  2. default  3. keyword  4. arbitrary (*args, **kwargs)
# the * matters, not the name - but args and kwargs are convention

# *args example
def add(*args):         # all passed values collected into a tuple
    total = 0
    for arg in args:
        total += arg
    return total

print(add(1, 2, 3))        # 6
print(add(10, 9, 7))       # 26
print(add(1, 2, 3, 4, 5))  # 15 - works with any number of arguments


def display_name(*args):
    for arg in args:
        print(arg, end=" ")
    print()

display_name("Dr.", "Spongebob", "Harold", "Squarepants", "III")
# Dr. Spongebob Harold Squarepants III


# **kwargs example
def print_address(**kwargs):    # all key=value pairs collected into a dict
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(street="123 Fake St.",
              city="Detroit",
              state="MI",
              zip="54321")
# street: 123 Fake St.
# city: Detroit
# state: MI
# zip: 54321


# *args and **kwargs together
def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    # formatted address using .get() so missing keys return None safely
    print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')}, {kwargs.get('state')} {kwargs.get('zip')}")

shipping_label("Dr.", "Tawsif", "Azam",
               street="CUET Campus",
               city="Chittagong",
               state="BD",
               zip="4214")
# Dr. Tawsif Azam
# CUET Campus
# Chittagong, BD 4214


# unpacking operator * can also unpack a list into arguments
nums = [1, 2, 3]
print(add(*nums))   # same as add(1, 2, 3) -> 6

# unpacking ** can unpack a dict into keyword arguments
address = {"street": "CUET Campus", "city": "Chittagong", "state": "BD", "zip": "4214"}
print_address(**address)   # same as passing each key=value manually

