number = int(input("Enter height: "))

for x in range(number - 1):
    for y in range(x, number):   
        print(" ", end=" ")
    for z in range(x):
        print("*", end=" ")
    for a in range(x + 1):
        print("*", end=" ")
    print()

for x in range(number):
    for y in range(x + 1):
        print(" ", end=' ')
    for z in range(x, number):   
        print("*", end=' ')
    for a in range(x, number -1):
        print("*", end=' ')
    print()



# for x in range(5 -1):
#     for y in range(x, 5):   
#         print(" ", end=" ")
#     for z in range(x):
#         print("*", end=" ")
#     for a in range(x + 1):
#         print("*", end=" ")
#     print()
# for x in range(5):
#     for y in range(x + 1):  # starts with 0 + 1
#         print(" ", end=' ')
#     for z in range(x, 5):   
#         print("*", end=' ')
#     for a in range(x, 4):
#         print("*", end=' ')
#     print()