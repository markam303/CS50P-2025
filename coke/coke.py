### Coke machine that checks for amount due from the user. Cost of 1 cola is 50 cents ###
coins = [25, 10, 5]
amount_due = 50

def main():
    # amount_due = 50
    
    while amount_due >= 0:
        print(f"Amount Due: {amount_due}")
        insert = get_coin()
        calc_amount_due(insert)
        

def get_coin():
    while True:
        insert = int(input("Insert Coin: "))
        if insert in coins:
            return insert
        


def calc_amount_due(insert):
    return amount_due - insert
    


main()