# elif statement evaluates multiple expressions
# executes code if one condition is true

# declaring variable as input
amount = int(input("Enter amount: "))

# if and else
if amount < 1000:
    discount = amount * 0.05
elif amount < 5000:
    discount = amount * 0.10
else:
    discount = amount * 0.15

net_amount = amount - discount

print("Net payable: R" + str(net_amount))

