# variable for user input
numb = (int(input("How many rows would you like? ")))

# defining function
def dow_lef_tri():
    for x in range(numb):
        for y in range(x):
            print(" ", end=' ')      # these are the empty spaces that take up spaces
        for z in range(x, numb):     # starts with x and ends with num
            print("*", end=" ")
        print()

# calling function
dow_lef_tri()
        

    