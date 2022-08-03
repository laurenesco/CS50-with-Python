#########################################
#  error handling: try, except, else    #
#########################################
def main():
    x = get_int("What's x? ")
    print(f"x is {x}")


def get_int(prompt):
    while True:
        try:
            x = int(input(prompt))  # could also do 'return int(input("What's x? "))'
            # break/return could also go here.
            # if a ValueError occurs, it would prevent it from executing anyway
        except ValueError:
            pass  # pass is like continue or next
            # print("x must be an integer")
            # error messages would go here ^^
        else:
            # break would go here if not in function
            # in this case return will break and return at once
            return x


main()
