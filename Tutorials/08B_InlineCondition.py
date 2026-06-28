
a = -5
# ternary / inline if-else
# format: value_if_true if condition else value_if_false
status = "Negative" if a < 0 else "Positive"
print(status)   # Negative

# can also use directly inside print
print("Negative" if a < 0 else "Positive")   # Negative

# works with any expression, not just strings
print(a * -1 if a < 0 else a)   # 5 - inline abs()

# nested ternary - use sparingly, gets hard to read quickly
score = 75
grade = "A" if score >= 90 else "B" if score >= 75 else "C" if score >= 60 else "F"
print(grade)   # B

# Basic CP tricks 
# print("YES" if condition else "NO")   # very common output format in CP problems
