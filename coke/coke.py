### Coke machine that checks for amount due from the user. Cost of 1 cola is 50 cents ###

def main():
    amount_due = 50
    coins = [25, 10, 5]
    
    while amount_due:
        print(f"Amount Due: {amount_due}")
        insert = int(input("Insert Coin: "))


def calc_amount_due(insert):
    return amount_due - insert
    


main()