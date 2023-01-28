# for loop, while loop, and range() function to display various patterns
# By printing different patterns, you can build a solid understanding of loops in Python.


# steps to printing patterns in python
# 1
#  we use 2 loops to print any pattern, nested loops ( a loop inside a loop)
# the structure of printing any pattern is to decide the number of columns and rows

# outer loop show the number of rows
# inner loop shows the column pattern

# the "input()" function is used to decide the size of a pattern

# 2
# iterate rows
#  use a FOR LOOP and RANGE() function to write the number of rows for the outer loop

#  3
#  iterate the columns
# create an inner(nested loop) to make handle the number of coloumns
#  the internal loop iteration depends on the values of the outer loop

# 4
#  print a star or number
#  use the print() func in eaaach iteration of nested FOR LOOP to display the symbol or number of a pattern
#  numbers or *

#  5 
#  add a new line after each iteration og the outer loop
#  so that the pattern can display properly

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

rows = 5

#  outer loop
for i in range(rows+1):

    # nested loop
    for j in range(1, i+1):

        #  display number
        print(i, end=" ")

    # new line after each row
    print("")

# prints