# NESTED LOOP
# loop inside a loop

# the inner loop will be executed one time for each iteration of the outer loop

# print each adjective for every fruit
# declaring variables
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

# fetching all items from each list
for x in adj:
    for y in fruits:
        # calling both lists
        print(x, y)