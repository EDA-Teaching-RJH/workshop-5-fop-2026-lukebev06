price = int(input("how much is the coffee (too the nearest 5p)? "))
valid_coin = [50,20,10,5]
current = 0


def get_coin():
    try:
       coin = int(input("please input a valid coin"))
       if coin in valid_coin :
          update_total(coin)
    except ValueError:
        print("that wasnt a valid input. please remove anything but the number")

 def update_total(current,coin):
    current = current + coin



 def dispense_product(total_inserted):



 get_coin()