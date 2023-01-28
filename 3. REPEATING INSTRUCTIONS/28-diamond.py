for x in range(5 -1):
    for y in range(x, 5):   
        print(" ", end=" ")
    for z in range(x):
        print("*", end=" ")
    for a in range(x + 1):
        print("*", end=" ")
    print()
for x in range(5):
    for y in range(x + 1):  # starts with 0 + 1
        print(" ", end=' ')
    for z in range(x, 5):   
        print("*", end=' ')
    for a in range(x, 4):
        print("*", end=' ')
    print()