# LEGB = order Python follows when looking up a variable name
# L = Local      : inside the current function
# E = Enclosing  : inside any outer/enclosing function
# G = Global     : top level of the script
# B = Built-in   : Python's built-in names like print, len, range etc
# Python stops as soon as it finds the name, if not found anywhere -> NameError


# 1. LOCAL SCOPE
# variables created inside a function exist only inside that function
def local_example():
    x = "I am local"   # x only exists inside this function
    print(x)

local_example() #I am local
# but if we try to print(x)   # NameError - x doesnt exist outside the function


# 2. ENCLOSING SCOPE
# inner function can read variables from the outer function
def outer():
    msg = "I am from the enclosing scope"

    def inner():
        print(msg)   # not found locally, Python checks enclosing scope

    inner()

outer()# I am from the enclosing scope


# 3. GLOBAL SCOPE
# variables defined at the top level, any function can read them
count = 100

def show_global():
    print(count)   # no local count, so Python looks at global scope

show_global()   # 100

# to MODIFY a global variable inside a function, use global keyword
def change_global():
    global count
    count += 1   # without global keyword this would create a new local count instead

change_global()
print(count)   # 101


# 4. BUILT-IN SCOPE
# names Python provides automatically, no import needed
print(len("hello"))   # print and len both come from built-in scope


# LEGB all together
x = "global x"

def outer_func():
    x = "enclosing x"

    def inner_func():
        x = "local x"
        print(x)   # found in local -> "local x"

    inner_func()
    print(x)       # found in enclosing -> "enclosing x"

outer_func()
print(x)           # found in global -> "global x"


# if a name doesnt exist in any scope
# print(does_not_exist)   # NameError: name 'does_not_exist' is not defined
# Python checked L -> E -> G -> B and found nothing


# nonlocal keyword - modify an enclosing variable from inner function
# similar to global but for enclosing scope
def outer2():
    count = 0

    def inner2():
        nonlocal count   # without this, count += 1 would cause UnboundLocalError
        count += 1
        print(count)

    inner2()   # 1
    inner2()   # 2
    inner2()   # 3

outer2()