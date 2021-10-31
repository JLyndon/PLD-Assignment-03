import math

def user_money():
    usr_balance = float(input("Enter your balance: "))
    return usr_balance

def apl_price():
    cost = float(input("\nEnter the price of an apple: "))
    return cost

def quantity_operator(balance, price):
    max_no_apl = math.floor(balance//price) 
    return max_no_apl

dividend = user_money()
divisor = apl_price()

output_01 = quantity_operator(dividend, divisor)

print(f"\nYou can purchase {output_01} apples.")

