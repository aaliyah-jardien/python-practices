# function that draws a down right triangle

# user row input
numb = int(input("Enter number of rows: "))

# defining function
def down_left_tri():
    for x in range(numb):   # starts with the number entered and creates that amount of rows
        for y in range(numb - x):   # takes number of rows amount and minuses every time
            print("*", end=" ")
        print()

# calling function
down_left_tri()