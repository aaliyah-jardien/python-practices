# declaring variable
numb = int(input("Enter a row: "))

# defining function
def pyramid():
    for x in range(numb):
        for y in range(numb - x):
            print(" ", end=" ")     # prints empty triangle
        for z in range(x):
            print("*", end=" ")
        for a in range(x + 1):
            print("*", end=" ")
        print()

# calling function
pyramid()