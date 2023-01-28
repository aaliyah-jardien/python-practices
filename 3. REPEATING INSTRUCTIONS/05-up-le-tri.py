# declaring variable
numb = int(input("Enter number of rows: "))

# defining function
def up_lef_tri():
    for x in range(numb):
        for y in range(x + 1):
            print(" ", end=" ")
        for z in range(numb - x):   # here i am starting with the user input total the subtracting the x value everytime
            print("*", end=" ")
        print()

# calling function
up_lef_tri()
