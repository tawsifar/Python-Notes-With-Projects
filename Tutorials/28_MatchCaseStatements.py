# match-case = cleaner alternative to long if-elif chains
# available from Python 3.10+
# executes code when a value matches a case

# traditional if-elif way
def day_of_week_if(day):
    if day == 1:
        return "Sunday"
    elif day == 2:
        return "Monday"
    elif day == 3:
        return "Tuesday"
    elif day == 4:
        return "Wednesday"
    elif day == 5:
        return "Thursday"
    elif day == 6:
        return "Friday"
    elif day == 7:
        return "Saturday"
    else:
        return "Not a valid day"

print(day_of_week_if(1))   # Sunday


# match-case way - same result, cleaner syntax
def day_of_week(day):
    match day:
        case 1: return "Sunday"
        case 2: return "Monday"
        case 3: return "Tuesday"
        case 4: return "Wednesday"
        case 5: return "Thursday"
        case 6: return "Friday"
        case 7: return "Saturday"
        case _: return "Not a valid day"   # _ is wildcard, matches anything else

print(day_of_week(1))    # Sunday
print(day_of_week(8))    # Not a valid day


# multiple values in one case using |
def is_weekend(day):
    match day:
        case "Saturday" | "Sunday":
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case _:
            return "Not a valid day"

print(is_weekend("Saturday"))   # True
print(is_weekend("Friday"))     # False
print(is_weekend("Tawsif"))     # Not a valid day


# match-case with multiple variables
def check_point(x, y):
    match (x, y):
        case (0, 0):
            return "Origin"
        case (0, y):
            return f"On Y axis at {y}"
        case (x, 0):
            return f"On X axis at {x}"
        case (x, y):
            return f"Point at {x}, {y}"

print(check_point(0, 0))    # Origin
print(check_point(0, 5))    # On Y axis at 5
print(check_point(3, 0))    # On X axis at 3
print(check_point(3, 5))    # Point at 3, 5

