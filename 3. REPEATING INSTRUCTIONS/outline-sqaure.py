# outline of a sqaure

# user input
number = int(input("Enter height: "))

for x in range(number):
    for y in range(number):
        if (x == 0) or (y == 0) or (x == number -1) or (y == number -1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
