# EXIT LOOP
# exits loop when looped item = the item

#  the break comes before the print

# declare variable
fruits = ["apples", "bananas", "oranges"]

for all in fruits:
    if all == "bananas":
        break
    print(all)

# stops at where you wanted to break and doesn't continue iterating over the rest of the items
# it stops right where it breaks

"""
difference between break and exit statement,

break line is coded after the program runs

exit line is coded before the print, before the program runs
"""