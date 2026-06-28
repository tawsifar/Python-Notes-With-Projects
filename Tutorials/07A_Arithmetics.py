
a = 10
b = 3

# addition
print(a + b)   # 13
a += b         # same as a = a + b
print(a)       # 13
a = 10         # reset a back to 10

# subtraction
print(a - b)   # 7
a -= b         # same as a = a - b
print(a)       # 7
a = 10         # reset

# multiplication
print(a * b)   # 30
a *= b         # same as a = a * b
print(a)       # 30
a = 10         # reset

# division - always returns float in Python 3
print(a / b)   # 3.3333333333333335
a /= b         # same as a = a / b
print(a)       # 3.3333333333333335
a = 10         # reset

# floor division - cuts decimal, result is always int
print(a // b)  # 3
a //= b        # same as a = a // b
print(a)       # 3
a = 10         # reset


# modulo - returns remainder after division
print(a % b)   # 1
# even/odd check: if n % 2 == 0 -> even
a %= b         # same as a = a % b
print(a)       # 1
a = 10         # reset

# exponentiation - raises a to the power of b
print(a ** b)  # 1000
a **= b        # same as a = a ** b
print(a)       # 1000
a = 10         # reset

# order of operations follows BODMAS
print((a + b) * 2)  # 26 - parentheses evaluated first
print(a + b * 2)    # 16 - multiplication happens before addition

# Basic CP tricks (VVI)
# use // when you want integer result without typecasting
print(a / b)   # 3.3333  (float)
print(a // b)  # 3       (int, no typecast needed)