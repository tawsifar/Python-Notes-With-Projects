import random

# dictionary where each key is a dice face (1-6)
# each value is a tuple of 5 strings representing one row of the dice art
# printed line by line to draw the dice shape in the terminal
dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}

dice = []   # stores the random roll result for each die
total = 0
num_of_dice = int(input("How many dice?: "))

# roll each die and store the result (1-6) in the dice list
for die in range(num_of_dice):
    dice.append(random.randint(1, 6))


# VERTICAL printing — one die fully drawn before moving to the next
# result: dice appear stacked on top of each other
# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)


# HORIZONTAL printing — all dice appear side by side on the same row
# logic: print row 0 of every die, then row 1 of every die, and so on
# end="" prevents newline after each piece so they join on the same line
# print() at the end of each row moves to the next line
for line in range(5):              # 5 rows per die (top to bottom)
    for die in dice:               # for each rolled value
        print(dice_art.get(die)[line], end="")  # print that row of that die, no newline
    print()                        # move to next line after all dice finish that row


# add up all rolled values for the total
for die in dice:
    total += die

print(f"total: {total}")