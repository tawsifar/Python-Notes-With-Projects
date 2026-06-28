

# Python has 3 logical operators: and, or, not

a = True
b = False

# AND - True only if BOTH are True
print(a and a)   # True
print(a and b)   # False
print(b and b)   # False

# OR - True if AT LEAST ONE is True
print(a or b)    # True
print(a or a)    # True
print(b or b)    # False

# NOT - flips the value
print(not a)     # False
print(not b)     # True

# real example
age    = 20
has_id = True

if age >= 18 and has_id:
    print("Access granted")

if age < 18 or not has_id:
    print("Access denied")

# chaining conditions
score = 75
if score >= 60 and score < 90:
    print("Tawsif passed but didnt ace it")

# not with conditions
is_banned = False
if not is_banned:
    print("User allowed")

# CP tricks (optional)
# avoid not in CP, just flip the condition instead for clarity
# not (a and b) == (not a or not b)  , De Morgan's law, useful to know