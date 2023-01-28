"""
creating a program that converts weight either to kgs to lbs
"""
# gettung user input (intergers only)
weight = int(input("Enter your weight: "))

# kilos or pounds?
unit = input("(L)bs or (K)g: ")

# if and else statements
if unit.upper() == "K":
    conversion = round(weight / 0.45)   # rounding off to nearest decimal
    print(f"You are {conversion} pounds") 
else:
    conversion = round(weight * 0.45)
    print(f"You are {conversion} kilograms")
