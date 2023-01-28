for x in range(5):
    for y in range(x+1):    # the start value is x, and x is 0, so we add 1 to zero to get
        print("*", end=' ')
    print()     # runs in a new row everytime, sticks until the end of the loop
    