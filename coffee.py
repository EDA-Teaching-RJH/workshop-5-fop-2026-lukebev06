#statement of requirements

#       any valid integar that is a multiple of 5 above o
#       prevent invalid totals before going into while
#       remove errors in coin values before it goes into the if statement

def coffee():
 valid_coins = [50,20,10,5]
 total = 0 
 
 try:
    price = int(input("how much is owed? "))
 except ValueError:
    print(f"---that price isnt a multiple of 5---")
    print(f"---please try again---")
    price = int(input("how much is owed to the nearest 5p ? "))
 


 while total < price :
    
    try:
        coin = int(input("enter a valid coin: "))

        if coin in valid_coins:
            total = total + coin
        else:
            print("That coin was invalid. please try again")
        if total >=75 :
            remainder = price - total
            print(f"{remainder}p left to pay")

    except ValueError:

            print("enter a valid input.")
    
    amount_over = total - price

 print(f"Amount owed: {amount_over}p")

    
    
coffee()
