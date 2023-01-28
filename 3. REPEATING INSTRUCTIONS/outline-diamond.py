number = int(input("Enter height: "))

for x in range(number - 1):
    for y in range(x, number):   
        print(" ", end=" ")
    for z in range(x):
        if (x == number -1) or (z == 0):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    for a in range(x + 1):
        if (x == number -1) or (a == x):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

for x in range(number):
    for y in range(x + 1):
        print(" ", end=" ")
    for z in range(x, number):
        if (z == y):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    for a in range(x, number -1):
        if (a == z-1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
