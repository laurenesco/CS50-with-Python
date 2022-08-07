def make_list(grocery_list, iteration):
    print("Add anything you need from the store!")
    print("Type \"Done\" when finished.")
    while 1:
        item = input("Item: ").title()
        if item == "Done":
            break
        grocery_list[iteration] = item
        iteration += 1
    return grocery_list


def print_list(grocery_list):
    new_list = {}
    for f in grocery_list:
        flag = 0
        current_item = grocery_list[f]
        for s in grocery_list:
            temp = grocery_list[s]
            if current_item == temp:
                flag += 1
        new_list = {grocery_list[f]: flag}
    for i in new_list:
        print(new_list)


def main():
    grocery_list = {}
    grocery_list = (make_list(grocery_list, 1))
    print(grocery_list)
    keep_going = input("Anything else you'd like to add? (Yes or No) ").title()
    if keep_going == "Yes":
        count = next(reversed(grocery_list.keys())) + 1
        make_list(grocery_list, count)
    print_list(grocery_list)


main()

## End of Program ##

#####################
#   Instructions    #
#####################

# Suppose that you’re in the habit of making a list of items you need
# from the grocery store.
#
# In a file called grocery.py, implement a program that prompts the user
# for items, one per line, until the user inputs control-d (which is a
# common way of ending one’s input to a program). Then output the user’s
# grocery list in all uppercase, sorted alphabetically by item, prefixing
# each line with the number of times the user inputted that item. No need
# to pluralize the items. Treat the user’s input case-insensitively.

#############
#   Hints   #
#############


# Note that you can detect when the user has inputted control - d
# by catching an EOFError with code like:
#
# try:
#     item = input()
# except EOFError:
#     ...
#
# Odds are you’ll want to store your grocery list as a dict.
# Note that a dict comes with quite a few methods, per
# docs.python.org/3/library/stdtypes.html#mapping-types-dict,
# among them get, and supports operations like:
#
# d[key]
#
# and
#
# if key in d:
#     ...
#
# wherein d is a dict and key is a str.
# Be sure to avoid or catch any KeyError.

#############
#   Test    #
#############


# Run your program with python grocery.py.Type mango and
# press Enter, then type strawberry and press Enter, followed
# by control-d.Your program should output:
#
# 1
# MANGO
# 1
# STRAWBERRY
#
# Run your program with python grocery.py.Type milk and press Enter,
# then type milk again and press Enter, followed by control-d.Your
# program should output:
#
# 2
# MILK
#
# Run your program with python grocery.py.Type tortilla and press Enter,
# then type sweet potato and press Enter, followed by control-d.Your
# program should output:
#
# 1
# SWEET
# POTATO
# 1
# TORTILLA
