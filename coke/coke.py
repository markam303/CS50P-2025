### Coke machine that checks for amount due from the user. Cost of 1 cola is 50 cents ###

coins = [25, 10, 5]


def main():
    # Initial cost of 1 cola
    amount_due = 50
    
    # Calculate the amount left to pay
    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        insert = get_coin()
        amount_due = calc_amount_due(amount_due, insert)
        
    # Calculate change owed to user
    if amount_due <= 0:
        change = amount_due * -1
        print(f"Change Owed: {change}")

        
def get_coin():
    insert = int(input("Insert Coin: "))
    if insert in coins:
        return insert
    else:
        return 0
        

def calc_amount_due(amount_due, insert):
    return (amount_due - insert)
    

main()