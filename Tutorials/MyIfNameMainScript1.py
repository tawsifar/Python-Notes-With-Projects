# script1.py

# functions defined here can be reused by other scripts via import
# they have no side effects — they just do their job when called
def favorite_food(food):
    print(f"Your favorite food is {food}")


def main():
    print("This is script1")
    favorite_food("pizza")
    print("Goodbye!")


# __name__ is a built-in variable Python sets automatically
# when this file is run directly:    __name__ == "__main__"
# when this file is imported:        __name__ == "script1"
# so this block only runs when script1.py is executed directly
# if another script imports script1, main() is NOT called automatically
if __name__ == '__main__':
    main()