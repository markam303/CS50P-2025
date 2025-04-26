### Grocery List ###
# This program allows a user to create a grocery list, add items to it, and view the list.

grocery_list = {"item":"amount",
                }  # Initialize an empty grocery list as a dictionary

try:
    while True:
        item = input("").upper()
        if item not in grocery_list:
            grocery_list.append(item)  # Add the item to the grocery list
            amount += 1 
            grocery_list[item] = amount  
            
        grocery_list = sorted(grocery_list)
except EOFError:
    print()
    for item in grocery_list:
        print(amount, item)