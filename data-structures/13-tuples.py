# now we working with a tuple and a list

# list of items, holding tuple of items
pricelist = [("bread", 17.95), ("egss", 24.50), ("milk", 22.50)]

# iterating through items, stating the first value is the name and second value is the price
for name, price in pricelist:
    print("- Item: " + name)
    print(" Price: R{}".format(price))