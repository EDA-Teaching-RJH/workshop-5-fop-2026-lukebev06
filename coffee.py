#50p 20p 10p 5p

def coffee():
 needed_pay = int(input("what is the total amount need to pay in pennies? "))
 while needed_pay != 0 :
    coin = int(input("what is the first coin you are inputting?"))
    if coin ==50:
      total = total + coin
      needed_pay = needed_pay - coin
    elif coin == 20:
        total = total + coin
        needed_pay = total + coin
    elif coin == 10:
        total = total + coin
        needed_pay = total + coin
    elif coin == 5:
        total = total + coin
        needed_pay = total + coin
    else:
       print("that isnt a valid coin amount")
    if total%75 == 0 :
       print(f"you have a total of {needed_pay}p left to pay")

