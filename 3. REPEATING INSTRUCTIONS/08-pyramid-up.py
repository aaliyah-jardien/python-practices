number = int(input("Enter height: "))

for x in range(number):
    for y in range(x, number):   
        print(" ", end=" ")
    for z in range(x):
        print("*", end=" ")
    for a in range(x + 1):
        print("*", end=" ")
    print()
