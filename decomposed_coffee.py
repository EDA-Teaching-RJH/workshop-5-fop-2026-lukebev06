
valid_coin = [50,20,10,5]

def main():
 change = 0
 amount_due = 75
 current = 0

 while amount_due > 0:
    coin = get_coin()
    coin = int(coin)
    amount_due = update_total(amount_due, coin, change)
    dispense_product(amount_due)
 if change >0 :
    print(f"{change}p change")
def get_coin():
    
    try:
        input_coin = int(input("input a coin value: "))
        if input_coin in  valid_coin :
            return input_coin
        else:
            print("that isnt a valid coin")
    except ValueError:
        print("invalid input. ")

def update_total(amount_due, coin, change):
    
    amount_due = amount_due - coin
    change = -amount_due
    return amount_due


def dispense_product(total_inserted):
    
    print(f"{total_inserted}p is left")
    

main()

