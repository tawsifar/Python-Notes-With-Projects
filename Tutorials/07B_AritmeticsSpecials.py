# 08_ArithmeticSpecials.py

x = 3.99
y = 7.88
z = -6.22

# built-in functions, no import needed
print(round(x))      # 4   - rounds to nearest int
print(round(y, 1))   # 7.9 - rounds to 1 decimal place
print(abs(z))        # 6.22 - removes negative sign
print(max(x, y, z))  # 7.88 - largest value
print(min(x, y, z))  # -6.22 - smallest value
print(pow(2, 10))    # 1024 - same as 2 ** 10

# math module for advanced operations
import math

print(math.pi)          # 3.141592653589793
print(math.e)           # 2.718281828459045 - Euler's number
print(math.sqrt(9))     # 3.0 - square root
print(math.ceil(x))     # 4 - rounds UP to nearest int
print(math.floor(x))    # 3 - rounds DOWN to nearest int
print(math.log(math.e)) # 1.0 - natural log
print(math.log2(8))     # 3.0 - log base 2, useful in CP
print(math.log10(1000)) # 3.0 - log base 10

# CP tricks (Good to know)
# math.gcd(a, b)   - greatest common divisor
# math.lcm(a, b)   - least common multiple (Python 3.9+)

# math.inf acts as infinity, useful for initializing min/max(Most of the time we will just directly use the max/min function though, so it's optional)- u can skip it if u want to 
# smallest = math.inf
# largest = -math.inf
# then start comparing in loop 


