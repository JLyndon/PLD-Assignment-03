def user_money():
    usr_balance = float(input("Enter your balance: "))
    return usr_balance

def apl_price():
    cost = float(input("\nEnter the price of an apple: "))
    return cost

dividend = user_money()
divisor = apl_price()
print(f"\nBalance: {dividend} \nPrice of an Apple: {divisor}")

