# list of groceries
groceries = ["bread", "eggs", "milk"]

# checking for membership (if it's part of the list)
print("oats" in groceries)

# changing item in list
groceries[2] = "flour"
print(groceries)

'''
that was a list, now compare that to a tuple
'''

# tuple of cleaning products
cleaning_products = ("dettol", "handy andy", "toothpaste")


# you cant cleaning_products[1] = "jik"

# replace item in tuple
cleaning_products = cleaning_products + ("soap",)
print(cleaning_products)