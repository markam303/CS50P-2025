### Place an order at Felipe's Taqueria ###

menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    while True:
        try:
            total = 0
            for item in menu:
                item = input("Item: ").title()
                price = menu.get(item)
                if price != None:
                    total += price
                    print(f"Total: ${total:.2f}")

        except EOFError:
            break
            print()


main()