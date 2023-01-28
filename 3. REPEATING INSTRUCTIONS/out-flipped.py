numb = int(input("Enter number of rows: "))

for x in range(numb):   
    for y in range(x, numb):
        if (x == 0) or (y == x) or (y == numb - 1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

#  x == number
# x == y
# or (x == numb + 1)
#  or (x == numb - 1)