def fuel_level():
    while 1:
        try:
            num = user_input("numerator")
            denom = user_input("denominator")
            return float(num / denom)
        except ZeroDivisionError:
            print("Cannot divide by zero!")


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
