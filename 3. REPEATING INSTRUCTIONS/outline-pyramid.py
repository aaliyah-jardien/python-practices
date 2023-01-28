"""# outline of a pyramid

for x in range(number):
    for y in range(number):
        if (x == number -1) or (y == 1) or (x == y +1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
"""

# user input
number = int(input("Enter height: "))

# defining function
def pyramid():
    for x in range(number):
        for y in range(number - x):
            print(" ", end=" ")     # prints empty triangle
        for z in range(x):
            if (x == number - 1) or (z == 0):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        for a in range(x + 1):
            if (x == number -1) or (a == x):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

# calling function
pyramid()
