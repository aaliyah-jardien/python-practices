# break statement
# stops loops before it went through all the items

# declaring variable, as a list
fruits = ["apples", "bananas", "oranges"]

for alles in fruits:
    print(alles)
    # stating where to break the loop
    if alles == "bananas": #stops at bananas, doesn't show bananas, went pass bananas, and continues with next item in list
        break # prints apples, oranges