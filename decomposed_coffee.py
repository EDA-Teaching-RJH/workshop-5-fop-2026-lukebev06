amount_due = int(input("how much is the coffee (too the nearest 5p)? "))
valid_coin = [50,20,10,5]
current = 0


def main():
 amount_due = 75
 while amount_due > 0:
    coin = (get_coin())
    amount_due = update_total(amount_due, coin, current)
    dispense_product(amount_due)

def get_coin():
    
    try:
        input_coin = int(input("input a coin value: "))
        if input_coin in  valid_coin :
            return input_coin
        else:
            print("that isnt a valid coin")
    except ValueError:
        print("invalid input. ")

def update_total(amount_due, coin, current):
    total_inserted = current + coin
    amount_due = amount_due - coin
    return amount_due


def dispense_product(total_inserted):
    
    if total_inserted >= amount_due : 
        print(f"{total_inserted}p is left")
        change = -amount_due
        print(f"{change}p change")
main()

