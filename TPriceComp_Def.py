def user_input():
    QuantApl = int(input("How many apples?\n> "))
    QuantOrng = int(input("\nHow many oranges?\n> "))
    return QuantApl, QuantOrng

multiplier = user_input()

print(multiplier)