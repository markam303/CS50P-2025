### Grocery List ###
# This program allows a user to create a grocery list, add items to it, and view the list.

grocery_list = [
    {"item":"amount"},
]# Initialize an empty grocery list as a dictionary

try:
    while True:
        item = input("").upper()
        if item not in grocery_list:
            grocery_list.append(item) 
        elif item in grocery_list:
            grocery_list[item] += 1
           
except EOFError:
    print()
    grocery_list = sorted(grocery_list)
    for item in grocery_list:
        print(grocery_list[item], item )