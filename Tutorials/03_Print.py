
name = "Tawsif"

print(name)         # prints the value stored in the variable
print("name")       # prints the word name literally, not the variable

# f-string (formatted string literal) - embeds variable values inside a string
print(f"My name is {name}")   # My name is Tawsif

# f-strings can also do math and expressions inline
age = 20
print(f"In 5 years, {name} will be {age + 5}")   # In 5 years, Tawsif will be 25

# multi-line strings use triple quotes
print('''Twinkle Twinkle, little star,
how I wonder what you are''')   # """ """ works the same way

# print() extras
print("CUET", "CSE", "Tawsif", sep=" | ")  # custom separator -> CUET | CSE | Tawsif
print("Hello", end=" ")                     # end="" prevents newline, default is \n
print("World")                              # prints on same line -> Hello World