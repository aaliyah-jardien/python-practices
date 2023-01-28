number = int(input("Enter total rows: "))

for x in range(number):     # prints rows
    for y in range(number -2): # prints columns
        print("*", end=" ")
    print()

