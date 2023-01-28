for x in range(5):
    for y in range(x + 1):  # starts at x value and increments by 1 
        print(" ", end=' ')
    for z in range(x, 5):     # starts with x and ends with 5
        print("*", end=' ')
    print()
