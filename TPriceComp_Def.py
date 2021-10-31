def apl_input():
    QuantApl = int(input("How many apples?\n> "))
    return QuantApl

def orng_input():
    QuantOrng = int(input("\nHow many oranges?\n> "))
    return QuantOrng

def total_prc(Apl_quant, Orng_quant):
    product_01 = Apl_quant*20
    product_02 = Orng_quant*25
    summation = product_01 + product_02
    return summation

Apple = apl_input()
Orange = orng_input()

grnd_total = total_prc(Apple, Orange)
print(f"\nThe total amount is {grnd_total}.")



