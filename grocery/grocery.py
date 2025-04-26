### Grocery List ###
# This program allows a user to create a grocery list, add items to it, and view the list.

grocery_list = []  # Initialize an empty grocery list
while True:
    item = input("").upper()
    grocery_list.append(item)
    grocery_list = sorted(grocery_list)
