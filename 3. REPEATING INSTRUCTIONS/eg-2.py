# creating downward pyramid

# create range 
#  for loop
for x in range(1, 7):  # creates number of rows
    for y in range(x - 1): # creates columns, uses current row number
        print("*", end=" ")
    print("\r")
    # print()