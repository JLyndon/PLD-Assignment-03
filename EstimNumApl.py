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
def change_operator(balance, price):
    change = balance % price
    return change

dividend = user_money()
divisor = apl_price()

output_01 = quantity_operator(dividend, divisor)
output_02 = change_operator(dividend, divisor)

print(f"\nYou can purchase {output_01} apples and your change is {output_02:.2f} pesos.")

