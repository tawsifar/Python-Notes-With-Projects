# Exception = an event that interrupts the normal flow of a program
# Common exceptions: ZeroDivisionError, TypeError, ValueError
# try    = the code that might cause an error goes here
# except = what to do if a specific error occurs
# finally = always runs no matter what, error or not

try:
    number = int(input("Enter a number: "))  # ValueError if user types "abc" instead of a number
    print(1 / number)                        # ZeroDivisionError if user enters 0

except ValueError:
    print("Please enter a valid number")     # runs if int() conversion fails

except ZeroDivisionError:
    print("You cannot divide by zero you fool")  # runs if number is 0

except Exception:
    print("Something went wrong")            # catches anything else not covered above
                                             # Exception is the base class of all exceptions
                                             # always put this LAST, most specific errors first
else:
    print("No errors occurred!")  # runs ONLY if try block succeeded with zero exceptions

finally:
    print("Done with exception handling")  # runs always, error or not