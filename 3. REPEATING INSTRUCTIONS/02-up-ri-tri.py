# variable for user input
numb_rows = int(input("Enter number of rows: "))

# turn this into a function
def up_right_tri():
    #  for loop
    for x in range(numb_rows):
        for y in range(x + 1):  # column starts with the row number then adds one each time
            print("*", end=" ")
        print()

# calling function
up_right_tri()

# naiiiiiooorrrceeeee