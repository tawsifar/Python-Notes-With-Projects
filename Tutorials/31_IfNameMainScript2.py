# script2.py

# imports everything from script1 (all functions, variables)
# because script1 uses if __name__ == "__main__", its main() does NOT run here
# only the functions become available, nothing else executes
from Tutorials.MyIfNameMainScript1 import *


def favorite_drink(drink):
    print(f"Your favorite drink is {drink}")


# these lines are at module level, not inside a function or if __name__ block
# so they run immediately whenever script2.py is executed or imported
# this is an example of what NOT to do if you want a reusable module
# any script that imports script2 would trigger these prints unintentionally
print("This is script2")
favorite_food("sushi")      # borrowed from script1 via the star import
favorite_drink("coffee")
print("Goodbye!")


# output when running script2.py directly:
# This is script2
# Your favorite food is sushi
# Your favorite drink is coffee
# Goodbye!

# output when running script1.py directly:
# This is script1
# Your favorite food is pizza
# Goodbye!