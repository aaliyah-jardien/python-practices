for x in range(6):          # range is 5
    #for y in range(x, 5):   # x is the start range
    for y in range(6 - x):  # this also works
        print("*", end=' ')
    print()