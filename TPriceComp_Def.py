def usr_input():
    QuantApl = int(input("How many apples? \n> "))
    QuantOrng = int(input("\nHow many oranges? \n> "))
    return QuantApl,QuantOrng

def total_(NumApl, NumOrng):
    ttlprc_apl = NumApl*20
    ttlprc_orng = NumOrng*25
    summation = ttlprc_apl + ttlprc_orng
    return summation

raw_input = usr_input()
grnd_total = total_(raw_input[0], raw_input[1])

print(f"The total amount is {grnd_total}.")



