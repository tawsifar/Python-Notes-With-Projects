questions = (
    "Who's the GOAT?: ",
    "Who's the fastest man on earth?: ",
    "Who is the richest man on Earth?: ",
    "Who landed on the moon first?: ",
    "Which planet in the solar system is the hottest?: "
)

options = (
    ("A. Messi", "B. Ronaldo", "C. Neymar", "D. Tawsif"),
    ("A. Usain Bolt", "B. Tawsif", "C. Ashton", "D. IshowSpeed"),
    ("A. Jeff Bezos", "B. Elon Musk", "C. Tawsif", "D. Jack Ma"),
    ("A. Armstrong", "B. Edwin", "C. Collins", "D. Tawsif"),
    ("A. Tawsif", "B. Venus", "C. Earth", "D. Mars")
)

answers = ("D", "B", "C", "D", "A")

guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------------")
    print(question)

    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper() # we used .upper so that if the user inputs smaller case, then it will automatically convert to capital case
    guesses.append(guess) #we store the guesses in the guess list

    # These lines must be INSIDE the loop
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")

    question_num += 1

print("--------------------")
print("RESULTS")
print("--------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")