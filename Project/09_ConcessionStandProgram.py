# Concession stand program
menu = {"pizza": 3.00,
"nachos": 4.50,
"popcorn": 6.00,
"fries": 2.50,
"chips": 1.00,
"pretzel": 3.50,
"soda": 3.00,
"lemonade": 4.25}
cart = []
total = 0
print("---------- MENU ----------")

for key, value in menu.items(): # using , to use key and value at the same time and make sure we use dictionary.items() to iterate through both of them
 print(f"{key:10}: ${value:.2f}") # key uses 10 spaces to look organized and value can show up to 2 decimal points
 print("------------------------")


while True:
    food = input("Select an item (q to quit): ").lower() # we lower case the input to match the strings in every circumstances
    if food == "q":
        break
    elif menu.get(food) is not None:  #is not none means not empty
        cart.append(food)


print("----YOUR ORDER ----")
for food in cart:
    total += menu.get(food)# by menu.get() we call the values of those keys
    print(food, end=" ")

print()
print(f"Total is: ${total:.2f}")
