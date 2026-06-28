# keyword arguments = passing arguments by their parameter name
# makes code more readable, order no longer matters
# order of types: 1. positional  2. default  3. keyword  4. arbitrary

def hello(greeting, title, first, last):
    print(f"{greeting} {title} {first} {last}")

# positional - order matters
hello("Hello", "Mr.", "Spongebob", "Squarepants")

# keyword - order doesnt matter when you name them
hello("Hello", title="Mr.", last="Squarepants", first="Spongebob")


# print() uses keyword arguments too
print("1", "2", "3", "4", "5", sep="-")    # 1-2-3-4-5
print("1", "2", "3", "4", "5", sep=", ")   # 1, 2, 3, 4, 5
print("Hello", end=" "); print("Tawsif")    # Hello Tawsif - on same line


def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

# positional
print(get_phone(1, 123, 456, 7890))

# keyword - much more readable, no need to remember order
print(get_phone(country=1, area=123, first=456, last=7890))
print(get_phone(area=123, last=7890, country=1, first=456))   # same result


# mixing positional and keyword - positional must come first
print(get_phone(1, 123, last=7890, first=456))   # valid
# print(get_phone(country=1, 123, 456, 7890))    # SyntaxError - keyword before positional


# basic CP usage (optional)
# though keyword args are rarely used in CP
# but print(end="") and print(sep=" ") are very common
# print(*arr, sep="\n")   # prints each element of a list on a new line