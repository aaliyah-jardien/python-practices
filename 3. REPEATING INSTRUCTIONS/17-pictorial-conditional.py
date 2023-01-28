numb = int(input("Enter number: "))

for x in range(numb):
    for y in range(x):
        print ("*", end=" ")
    print(" ")

for x in range(numb, 0, -1):
    for y in range(x):
        print("*", end=" ")
    print()
    