
for x in range(5):  # creates number of rows
    for y in range(x + 1): # creates columns, uses current row number
        print("*", end=" ")
    for x in range(1, 7):
        print("*", end=" ")
    for y in range(x - 1):
        print

    print("\r") # \r returns a new line

#      # creates columns, uses current row number
#      print("*", end=" ")
# print("\r")