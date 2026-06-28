# random module - generate random numbers, choices, and shuffles
import random

# random integer between 1 and 10, both inclusive
number = random.randint(1, 10)
print(number)

# with variables
low  = 1
high = 10
print(random.randint(low, high))

# random float between 0.0 and 1.0
print(random.random())

# random float between any range
print(random.uniform(1.5, 9.5))   # e.g. 4.732...

# random choice from a sequence
options = ("rock", "paper", "scissors")
print(random.choice(options))   # picks one randomly

# random sample - picks multiple unique elements
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
hand  = random.sample(cards, 5)   # picks 5 unique cards, original list unchanged
print(hand)

# shuffle - randomizes the order of the list in place
random.shuffle(cards)
print(cards)

# seeding - makes random results reproducible
# useful for testing, same seed always gives same output
random.seed(42)
print(random.randint(1, 100))   # always 82 with seed 42
random.seed(42)
print(random.randint(1, 100))   # still 82, same seed same result

