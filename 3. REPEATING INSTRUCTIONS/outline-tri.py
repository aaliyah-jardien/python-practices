number = int(input("Enter height: "))

for x in range(1, number + 1):
    for y in range(1, number + 1):
        if(y == 1) or (x == number) or (x == y):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

