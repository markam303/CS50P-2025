### Grocery List ###
# This program allows a user to create a grocery list, add items to it, and view the list.

grocery_list =  {}

try:
    while True:
        item = input("").upper()
        if item not in grocery_list:
            grocery_list.update({item: 1})
        elif item in grocery_list:
            grocery_list.update({item: grocery_list[item] + 1})
           
except EOFError:
    print()
    for item in grocery_list:
        print(grocery_list[item], item )