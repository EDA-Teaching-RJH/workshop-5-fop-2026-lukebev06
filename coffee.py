#statement of requirements

#       any valid integar that is a multiple of 5 above o
#       prevent invalid totals before going into while
#       remove errors in coin values before it goes into the if statement
p

def coffee():
 valid_coins = [50,20,10,5]

 price = int(input("how much is owed? "))
 total = 0  

 
 while total < price :
    try:
        coin = int(input("enter a valid coin: "))

        if coin in valid_coins:
           total = total + coin

    except ValueError:

        print("enter a valid input.")
    
    amount_over = total - price
 print(f"Amount owed: {amount_over}p")

    
    



    
coffee()
