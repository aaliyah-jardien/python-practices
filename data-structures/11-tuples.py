veggies = ("mielies", "carrots", "potatos")

# adding to a tuple
veggies = veggies + ("cabbage",) # w/out the comma it will read as a str, and return an error
print(veggies)

# indexing through tuple
veggies[2]

# going through each veg, one by one
for item in veggies:
    print(item)