# module = a file containing code you want to include in your program
# use import to include a module (built-in or your own)
# helps break large programs into reusable separate files

# print(help("modules"))   # shows all available built-in modules

import math                # access everything as math.something
# import math as m         # rename it, then use m.pi, m.e etc
# from math import pi, e   # import specific things, use directly as pi and e
# from math import *       # imports everything, use directly but can cause name conflicts

print(math.pi)             # 3.141592653589793
print(math.e)              # 2.718281828459045

# assigning e as a variable shadows the math.e import if using "from math import e"
# but since we used "import math", math.e still works fine
a, b, c, d, e = 1, 2, 3, 4, 5
print(math.e ** e)         # math.e to the power of our variable e (5) = 148.41...


# creating your own module
# any .py file can be used as a module
# below is what MyModule.py would contain:

# pi = 3.14159
#
# def square(x):
#     return x * x
#
# def cube(x):
#     return x * x * x
#
# def circumference(r):
#     return 2 * pi * r
#
# def area(r):
#     return pi * r * r


# importing and using your own module
import MyModule

print(MyModule.pi)                  # 3.14159
print(MyModule.square(3))           # 9
print(MyModule.cube(3))             # 27
print(MyModule.circumference(3))    # 18.84954
print(MyModule.area(3))             # 28.27431

# from your own module too
# from MyModule import square, cube
# print(square(4))   # 16
# print(cube(4))     # 64

