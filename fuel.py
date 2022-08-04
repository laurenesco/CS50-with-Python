def fuel_level():
    while 1:
        num = user_input("numerator")
        denom = user_input("denominator")
        if denom == 0:
            print("Cannot divide by zero!")
            pass
        elif num < 0 or denom < 0:
            print("Integers must be positive")
            pass
        elif num > denom:
            print("Numerator must be smaller than denominator!")
        else:
            return float(num / denom)


def user_input(name):
    while 1:
        try:
            value = int(input(f"Enter a {name}: "))
            return value
        except ValueError:
            print("Values must be an integers.")


def print_level(amount):
    if amount <= .01:
        print("E")
    elif amount >= .99:
        print("F")
    else:
        percent = int(amount*100)
        print(f"{percent}%")


def main():
    result = fuel_level()
    print_level(result)


main()

## End Program ##

#####################
#   Instructions    #
#####################

# Fuel gauges indicate, often with fractions, just how much fuel is in a tank.
# For instance 1/4 indicates that a tank is 25% full,
# 1/2 indicates that a tank is 50% full, and 3/4 indicates that a tank is 75% full.
#
# In a file called fuel.py, implement a program that prompts the user for a fraction,
# formatted as X/Y, wherein each of X and Y is an integer, and then outputs,
# as a percentage rounded to the nearest integer, how much fuel is in the tank.
# If, though, 1% or less remains, output E instead to indicate that the tank is
# essentially empty. And if 99% or more remains, output F instead to indicate that
# the tank is essentially full.
#
# If, though, X or Y is not an integer, X is greater than Y, or Y is 0,
# instead prompt the user again. (It is not necessary for Y to be 4.)
# Be sure to catch any exceptions like ValueError or ZeroDivisionError.


####################
#   How to Test    #
####################

# Here’s how to test your code manually:
#
#     Run your program with python fuel.py. Type 3/4 and press Enter. Your program should output:
#
#     75%
#
#     Run your program with python fuel.py. Type 1/4 and press Enter. Your program should output:
#
#     25%
#
#     Run your program with python fuel.py. Type 4/4 and press Enter. Your program should output:
#
#     F
#
#     Run your program with python fuel.py. Type 0/4 and press Enter. Your program should output:
#
#     E
#
#     Run your program with python fuel.py. Type 4/0 and press Enter. Your program should handle a ZeroDivisionError and prompt the user again.
#     Run your program with python fuel.py. Type three/four and press Enter. Your program should handle a ValueError and prompt the user again.
#     Run your program with python fuel.py. Type 1.5/3 and press Enter. Your program should handle a ValueError and prompt the user again.
#     Run your program with python fuel.py. Type 5/4 and press Enter. Your program should prompt the user again.
